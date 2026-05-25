#!/usr/bin/env python3
"""Storage Analyst — read-only storage audit for Windows."""

import os
import sys
import hashlib
import datetime
from pathlib import Path
from collections import defaultdict

# ── Thresholds ──────────────────────────────────────────────────────────────
NOW = datetime.datetime.now()
ONE_YEAR_AGO       = NOW - datetime.timedelta(days=365)
EIGHTEEN_MOS_AGO   = NOW - datetime.timedelta(days=548)
SIX_MONTHS_AGO     = NOW - datetime.timedelta(days=183)
LARGE_FILE_BYTES   = 100 * 1024 * 1024  # 100 MB

# Keywords that identify system/runtime folders we must never flag as unused apps
SYSTEM_APP_KEYWORDS = {
    'microsoft', 'windows', 'visual c++', 'vcredist', '.net', 'dotnet',
    'directx', 'common files', 'internet explorer', 'msbuild', 'reference',
    'windowsapps', 'windowspowershell', 'windows defender', 'windows mail',
    'windows media', 'windows nt', 'windows photo',
}


# ── Path helpers ─────────────────────────────────────────────────────────────

def get_username() -> str:
    return os.environ.get('USERNAME') or os.environ.get('USER') or 'User'


def get_scan_paths(username: str) -> list[Path]:
    base = Path(f'C:/Users/{username}')
    temp = Path(os.environ.get('TEMP', str(base / 'AppData/Local/Temp')))
    paths = [
        base / 'Documents',
        base / 'Downloads',
        base / 'Desktop',
        base / 'AppData/Local/Temp',
        base / 'AppData/Local/Microsoft/Windows/INetCache',
        temp,
    ]
    # Deduplicate by resolved string (TEMP often aliases Local\Temp)
    seen, unique = set(), []
    for p in paths:
        key = str(p).lower()
        if key not in seen:
            seen.add(key)
            unique.append(p)
    return unique


def is_protected(path: Path) -> bool:
    """Return True if path falls under a protected directory."""
    parts_lower = [p.lower() for p in path.parts]
    protected_dirs = {'pictures', 'videos', 'music'}
    # Direct folder name match (catches C:\Users\Ben\Pictures\...)
    for part in parts_lower:
        if part in protected_dirs:
            return True
    # OneDrive\Pictures
    s = str(path).lower()
    if r'\onedrive\pictures' in s:
        return True
    if r'\appdata\roaming\microsoft' in s:
        return True
    if r'\windows\\' in s or s.startswith('c:\\windows'):
        return True
    if r'\program files\\' in s or r'\program files (x86)\\' in s:
        return True
    return False


def walk_files(root: Path):
    """Yield all accessible files under root, skipping protected dirs."""
    for dirpath, dirs, files in os.walk(str(root), topdown=True, onerror=lambda _: None):
        p = Path(dirpath)
        if is_protected(p):
            dirs.clear()
            continue
        # Prune subdirs that are protected before descending
        dirs[:] = [d for d in dirs if not is_protected(p / d)]
        for fname in files:
            yield p / fname


# ── File stat helpers ────────────────────────────────────────────────────────

def file_stat(path: Path) -> tuple[datetime.datetime | None, datetime.datetime | None, int]:
    try:
        st = path.stat()
        return (
            datetime.datetime.fromtimestamp(st.st_atime),
            datetime.datetime.fromtimestamp(st.st_mtime),
            st.st_size,
        )
    except OSError:
        return None, None, 0


def dir_total_size(path: Path) -> int:
    total = 0
    for dirpath, _, files in os.walk(str(path), onerror=lambda _: None):
        for fname in files:
            try:
                total += os.path.getsize(os.path.join(dirpath, fname))
            except OSError:
                pass
    return total


def hash_file(path: Path) -> str | None:
    try:
        h = hashlib.md5()
        with open(path, 'rb') as f:
            while chunk := f.read(65536):
                h.update(chunk)
        return h.hexdigest()
    except OSError:
        return None


def format_size(n: int) -> str:
    for unit in ('B', 'KB', 'MB', 'GB', 'TB'):
        if n < 1024:
            return f'{n:.1f} {unit}'
        n /= 1024
    return f'{n:.1f} PB'


def age_label(dt: datetime.datetime | None) -> str:
    if dt is None:
        return 'unknown'
    days = (NOW - dt).days
    if days < 1:
        return 'today'
    if days < 30:
        return f'{days} days ago'
    if days < 365:
        m = days // 30
        return f'{m} month{"s" if m > 1 else ""} ago'
    y = days // 365
    return f'{y} year{"s" if y > 1 else ""} ago'


# ── Scan functions ───────────────────────────────────────────────────────────

def scan_large_files(paths: list[Path]) -> list[dict]:
    results = []
    for root in paths:
        if not root.exists():
            continue
        for f in walk_files(root):
            accessed, modified, size = file_stat(f)
            if size >= LARGE_FILE_BYTES:
                results.append({'path': f, 'size': size, 'accessed': accessed, 'modified': modified})
    results.sort(key=lambda x: x['size'], reverse=True)
    return results


def scan_old_downloads(username: str) -> list[dict]:
    dl = Path(f'C:/Users/{username}/Downloads')
    results = []
    if not dl.exists():
        return results
    for f in dl.iterdir():
        if not f.is_file():
            continue
        accessed, modified, size = file_stat(f)
        if modified and modified < ONE_YEAR_AGO:
            results.append({'path': f, 'size': size, 'modified': modified, 'ext': f.suffix.lower() or '(none)'})
    results.sort(key=lambda x: x['modified'] or NOW)
    return results


def scan_duplicates(paths: list[Path]) -> list[list[tuple[Path, int]]]:
    # Pass 1 — group files by size (only same-size files can be duplicates)
    size_map: dict[int, list[Path]] = defaultdict(list)
    for root in paths:
        if not root.exists():
            continue
        for f in walk_files(root):
            _, _, size = file_stat(f)
            if size > 0:
                size_map[size].append(f)

    # Pass 2 — hash only files that share a size with at least one other file
    hash_map: dict[str, list[tuple[Path, int]]] = defaultdict(list)
    for size, files in size_map.items():
        if len(files) < 2:
            continue
        for f in files:
            h = hash_file(f)
            if h:
                hash_map[h].append((f, size))

    groups = [v for v in hash_map.values() if len(v) > 1]
    groups.sort(key=lambda g: g[0][1], reverse=True)
    return groups


def scan_junk(username: str) -> list[dict]:
    base = Path(f'C:/Users/{username}')
    results = []

    def _entry(category, location, size, safe):
        results.append({'category': category, 'location': str(location), 'size': size, 'safe': safe})

    # Windows Temp (deduplicated)
    temp_env = Path(os.environ.get('TEMP', str(base / 'AppData/Local/Temp')))
    seen_temp = set()
    for td in [base / 'AppData/Local/Temp', temp_env]:
        key = str(td).lower()
        if key not in seen_temp and td.exists():
            seen_temp.add(key)
            _entry('Windows Temp Files', td, dir_total_size(td), 'YES — safe')

    # Browser cache
    chrome_cache = base / 'AppData/Local/Google/Chrome/User Data/Default/Cache'
    inet_cache   = base / 'AppData/Local/Microsoft/Windows/INetCache'
    for cd, label in [(chrome_cache, 'Chrome Cache'), (inet_cache, 'IE/Edge INetCache')]:
        if cd.exists():
            _entry('Browser Cache', cd, dir_total_size(cd), 'YES — rebuilds automatically')

    # Crash dumps
    dump_total, dump_count = 0, 0
    scan_roots = [base / 'Documents', base / 'Downloads', base / 'Desktop',
                  base / 'AppData/Local/Temp']
    for root in scan_roots:
        if not root.exists():
            continue
        for dirpath, dirs, files in os.walk(str(root), onerror=lambda _: None):
            for fname in files:
                if fname.lower().endswith(('.dmp', '.mdmp')):
                    fp = Path(dirpath) / fname
                    try:
                        dump_total += fp.stat().st_size
                        dump_count += 1
                    except OSError:
                        pass
    if dump_count:
        _entry('Crash Dumps', f'{dump_count} .dmp/.mdmp files in scan scope', dump_total,
               'YES — diagnostic only')

    # Old log files (>6 months)
    log_total, log_count = 0, 0
    for root in scan_roots:
        if not root.exists():
            continue
        for dirpath, dirs, files in os.walk(str(root), onerror=lambda _: None):
            for fname in files:
                if fname.lower().endswith('.log'):
                    fp = Path(dirpath) / fname
                    try:
                        mtime = datetime.datetime.fromtimestamp(fp.stat().st_mtime)
                        if mtime < SIX_MONTHS_AGO:
                            log_total += fp.stat().st_size
                            log_count += 1
                    except OSError:
                        pass
    if log_count:
        _entry('Old Log Files (6+ months)', f'{log_count} .log files in scan scope', log_total,
               'REVIEW — verify before deleting')

    # Thumbnail cache
    thumb_dir = base / 'AppData/Local/Microsoft/Windows/Explorer'
    if thumb_dir.exists():
        thumb_total = 0
        try:
            for f in thumb_dir.glob('thumbcache_*.db'):
                try:
                    thumb_total += f.stat().st_size
                except OSError:
                    pass
        except OSError:
            pass
        if thumb_total:
            _entry('Thumbnail Cache', thumb_dir, thumb_total, 'YES — rebuilds automatically')

    # Recycle Bin (size only, no content listing)
    recycle = Path('C:/$Recycle.Bin')
    if recycle.exists():
        try:
            size = dir_total_size(recycle)
            _entry('Recycle Bin', recycle, size, 'YES — empty when ready')
        except OSError:
            _entry('Recycle Bin', recycle, -1, 'YES — empty when ready (size: access denied)')

    return results


def scan_unused_apps() -> list[dict]:
    app_roots = [Path('C:/Program Files'), Path('C:/Program Files (x86)')]
    apps = []

    for app_root in app_roots:
        if not app_root.exists():
            continue
        try:
            entries = list(app_root.iterdir())
        except OSError:
            continue
        for app_dir in entries:
            if not app_dir.is_dir():
                continue
            name_lower = app_dir.name.lower()
            if any(kw in name_lower for kw in SYSTEM_APP_KEYWORDS):
                continue

            # Find the most recently accessed .exe in the top-level folder
            latest_exe_atime = None
            try:
                for exe in app_dir.glob('*.exe'):
                    try:
                        atime = exe.stat().st_atime
                        if latest_exe_atime is None or atime > latest_exe_atime:
                            latest_exe_atime = atime
                    except OSError:
                        pass
            except OSError:
                pass

            if latest_exe_atime is None:
                continue  # no exe found, skip

            last_used = datetime.datetime.fromtimestamp(latest_exe_atime)
            if last_used < EIGHTEEN_MOS_AGO:
                apps.append({
                    'name': app_dir.name,
                    'path': str(app_dir),
                    'size': dir_total_size(app_dir),
                    'last_used': last_used,
                })

    apps.sort(key=lambda x: x['size'], reverse=True)
    return apps


def scan_empty_folders(paths: list[Path]) -> list[Path]:
    empty = []
    for root in paths:
        if not root.exists():
            continue
        for dirpath, dirs, files in os.walk(str(root), topdown=False, onerror=lambda _: None):
            p = Path(dirpath)
            if is_protected(p):
                continue
            if not dirs and not files:
                empty.append(p)
    return empty


# ── Report builder ───────────────────────────────────────────────────────────

_W = 72  # inner box width


def _sep():
    return '─' * (_W + 2)


def _hdr(title: str, subtitle: str = '') -> list[str]:
    lines = [_sep(), title]
    if subtitle:
        lines.append(subtitle)
    lines.append(_sep())
    return lines


def build_report(username: str,
                 large: list[dict],
                 old_dl: list[dict],
                 dupes: list[list[tuple[Path, int]]],
                 junk: list[dict],
                 apps: list[dict],
                 empty_dirs: list[Path]) -> str:

    large_total = sum(f['size'] for f in large)
    dl_total    = sum(f['size'] for f in old_dl)
    dupe_total  = sum(g[0][1] * (len(g) - 1) for g in dupes)
    junk_total  = sum(j['size'] for j in junk if j['size'] >= 0)
    apps_total  = sum(a['size'] for a in apps)
    grand_total = large_total + dl_total + dupe_total + junk_total + apps_total

    ts = NOW.strftime('%Y-%m-%d %H:%M')
    L: list[str] = []

    # ── Header box
    L += [
        f'╔{"═" * _W}╗',
        f'║{"STORAGE ANALYST — AUDIT REPORT":^{_W}}║',
        f'║{"Generated: " + ts:^{_W}}║',
        f'╠{"═" * _W}╣',
        f'║  {"Potential recoverable:  " + format_size(grand_total) + "  (if ALL flagged items were removed)":<{_W-2}}║',
        f'║  {"Protected paths:  SKIPPED (Pictures, Videos, Music, System)":<{_W-2}}║',
        f'╚{"═" * _W}╝',
        '',
    ]

    # ── Section 1: Large files
    L += _hdr('SECTION 1 — LARGE FILES  (Top space consumers over 100MB)',
              f'Potential savings if removed: {format_size(large_total)}')
    L.append('')
    if large:
        L.append(f'{"#":<4} | {"Size":<10} | {"Last Accessed":<17} | {"Last Modified":<12} | File')
        L.append(f'{"─"*4}-+-{"─"*10}-+-{"─"*17}-+-{"─"*12}-+-{"─"*40}')
        for i, f in enumerate(large[:30], 1):
            mod = f['modified'].strftime('%Y-%m-%d') if f['modified'] else 'unknown  '
            L.append(f'{i:<4} | {format_size(f["size"]):<10} | {age_label(f["accessed"]):<17} | {mod:<12} | {f["path"]}')
    else:
        L.append('No files over 100MB found in scanned paths.')
    L += [
        '',
        'ACTION: Review each file above and delete manually if no longer needed.',
        '        File Explorer → navigate to path → right-click → Delete',
        '',
    ]

    # ── Section 2: Old downloads
    L += _hdr('SECTION 2 — OLD DOWNLOADS  (Not modified in 1+ year)',
              f'Potential savings if removed: {format_size(dl_total)}')
    L.append('')
    if old_dl:
        L.append(f'{"File":<45} | {"Size":<10} | {"Last Modified":<12} | Type')
        L.append(f'{"─"*45}-+-{"─"*10}-+-{"─"*12}-+-{"─"*20}')
        for f in old_dl[:40]:
            mod = f['modified'].strftime('%Y-%m-%d') if f['modified'] else 'unknown'
            L.append(f'{f["path"].name[:44]:<45} | {format_size(f["size"]):<10} | {mod:<12} | {f["ext"]}')
    else:
        L.append('No downloads older than 1 year found.')
    L += [
        '',
        f'ACTION: Open C:\\Users\\{username}\\Downloads',
        '        Sort by "Date Modified" — review and delete files you no longer need.',
        '',
    ]

    # ── Section 3: Duplicates
    L += _hdr('SECTION 3 — DUPLICATE FILES',
              f'Potential savings if duplicates removed: {format_size(dupe_total)}')
    L.append('')
    if dupes:
        for i, group in enumerate(dupes[:25], 1):
            size = group[0][1]
            L.append(f'GROUP {i} — {format_size(size)} each  ({len(group)} identical copies)')
            stamped = []
            for f, s in group:
                try:
                    mt = datetime.datetime.fromtimestamp(f.stat().st_mtime)
                except OSError:
                    mt = None
                stamped.append((f, s, mt))
            stamped.sort(key=lambda x: x[2] or datetime.datetime.min, reverse=True)
            newest = stamped[0]
            mod_newest = newest[2].strftime('%Y-%m-%d') if newest[2] else 'unknown'
            L.append(f'  KEEP?  → {newest[0]}  (newest, modified {mod_newest})')
            for f, s, mt in stamped[1:]:
                mod_str = mt.strftime('%Y-%m-%d') if mt else 'unknown'
                L.append(f'  DUPE?  → {f}  (older, modified {mod_str})')
            L.append('')
    else:
        L.append('No duplicate files found in scanned paths.')
    L += [
        'ACTION: For each group, keep the version you want and delete the other manually.',
        '        Identical content = same bytes, not necessarily the same purpose.',
        '',
    ]

    # ── Section 4: Junk
    L += _hdr('SECTION 4 — TEMPORARY & JUNK FILES',
              f'Potential savings if cleared: {format_size(junk_total)}')
    L.append('')
    if junk:
        L.append(f'{"Category":<28} | {"Location":<38} | {"Size":<10} | Safe to Clear?')
        L.append(f'{"─"*28}-+-{"─"*38}-+-{"─"*10}-+-{"─"*24}')
        for j in junk:
            size_str = format_size(j['size']) if j['size'] >= 0 else 'n/a'
            L.append(f'{j["category"][:27]:<28} | {j["location"][:37]:<38} | {size_str:<10} | {j["safe"]}')
    else:
        L.append('No junk files found.')
    L += [
        '',
        'ACTION: Use Windows built-in Disk Cleanup for the safest approach:',
        '        Start Menu → search "Disk Cleanup" → select C: drive → OK',
        '        For browser cache: Chrome → Settings → Privacy → Clear browsing data',
        '',
    ]

    # ── Section 5: Unused apps
    L += _hdr('SECTION 5 — POTENTIALLY UNUSED APPLICATIONS',
              "Apps whose main .exe hasn't been accessed in 18+ months")
    L.append('')
    if apps:
        L.append(f'{"App Name":<32} | {"Install Path":<42} | {"Size":<10} | Last Used')
        L.append(f'{"─"*32}-+-{"─"*42}-+-{"─"*10}-+-{"─"*12}')
        for a in apps[:20]:
            used = a['last_used'].strftime('%Y-%m-%d') if a['last_used'] else 'unknown'
            L.append(f'{a["name"][:31]:<32} | {a["path"][:41]:<42} | {format_size(a["size"]):<10} | {used}')
    else:
        L.append('No potentially unused applications found (or Program Files access denied).')
    L += [
        '',
        'WARNING: DO NOT UNINSTALL based on this list alone.',
        '         Verify you no longer need each app before removing it.',
        'ACTION:  Settings → Apps → Apps & Features → find the app → Uninstall',
        "         Never uninstall something you don't recognize — it may be a dependency.",
        '',
    ]

    # ── Section 6: Empty folders
    L += _hdr('SECTION 6 — EMPTY FOLDERS')
    L.append('')
    if empty_dirs:
        for d in empty_dirs[:40]:
            L.append(str(d))
    else:
        L.append('No empty folders found in scanned paths.')
    L += [
        '',
        'ACTION: Safe to delete manually if you do not recognise the folder purpose.',
        '',
    ]

    # ── Summary
    L += [
        _sep(),
        'SUMMARY — PRIORITIZED ACTION LIST',
        _sep(),
        '',
        f'{"Priority":<10} | {"Action":<46} | Est. Savings',
        f'{"─"*10}-+-{"─"*46}-+-{"─"*14}',
        f'{"HIGH":<10} | {"Run Disk Cleanup (temp + cache)":<46} | ~{format_size(junk_total)}',
        f'{"HIGH":<10} | {"Delete old Downloads (1+ yr untouched)":<46} | ~{format_size(dl_total)}',
        f'{"MEDIUM":<10} | {"Review & remove duplicate files":<46} | ~{format_size(dupe_total)}',
        f'{"MEDIUM":<10} | {"Remove large unused files":<46} | ~{format_size(large_total)}',
        f'{"LOW":<10} | {"Uninstall unused applications":<46} | ~{format_size(apps_total)}',
        f'{"LOW":<10} | {"Delete empty folders":<46} | ~0 B',
        '',
        f'TOTAL POTENTIAL RECOVERY: ~{format_size(grand_total)}',
        '',
        _sep(),
        'IMPORTANT REMINDERS',
        _sep(),
        '• This report is READ-ONLY. No files were moved, deleted, or modified.',
        '• All actions above must be taken manually by you.',
        '• Pictures folder was fully protected and excluded from all scans.',
        '• When in doubt about a file — keep it. Storage is cheap; lost files are not.',
        f'• Full report saved to: Documents\\_StorageReports\\report_{NOW.strftime("%Y-%m-%d_%H-%M")}.txt',
        '',
    ]

    return '\n'.join(L)


# ── Save & entry point ───────────────────────────────────────────────────────

def save_report(username: str, text: str) -> Path:
    report_dir = Path(f'C:/Users/{username}/Documents/_StorageReports')
    report_dir.mkdir(parents=True, exist_ok=True)
    fname = f'report_{NOW.strftime("%Y-%m-%d_%H-%M")}.txt'
    out = report_dir / fname
    out.write_text(text, encoding='utf-8')
    return out


def main() -> None:
    print('Storage Analyst — starting read-only scan. No files will be modified.\n')

    username = get_username()
    print(f'User: {username}')

    scan_paths = get_scan_paths(username)
    existing = [p for p in scan_paths if p.exists()]
    print(f'Scan paths: {len(existing)} of {len(scan_paths)} exist\n')

    print('Scanning large files (>100MB)...')
    large = scan_large_files(existing)
    print(f'  {len(large)} found')

    print('Scanning Downloads for old files (1+ year)...')
    old_dl = scan_old_downloads(username)
    print(f'  {len(old_dl)} found')

    print('Scanning for duplicate files (MD5)...')
    dupes = scan_duplicates(existing)
    print(f'  {len(dupes)} duplicate groups found')

    print('Scanning for junk & temporary files...')
    junk = scan_junk(username)
    print(f'  {len(junk)} categories found')

    print('Scanning for unused applications...')
    apps = scan_unused_apps()
    print(f'  {len(apps)} potentially unused apps found')

    print('Scanning for empty folders...')
    empty_dirs = scan_empty_folders(existing)
    print(f'  {len(empty_dirs)} empty folders found')

    print('\nBuilding report...\n')
    report = build_report(username, large, old_dl, dupes, junk, apps, empty_dirs)

    print(report)

    try:
        saved = save_report(username, report)
        print(f'\nReport saved to: {saved}')
    except OSError as e:
        print(f'\nWarning: could not save report file — {e}')


if __name__ == '__main__':
    main()
