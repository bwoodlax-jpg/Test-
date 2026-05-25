"""
Document Sorter Agent
Scans Documents folder, identifies tax-related files, proposes moves, and
executes only after explicit user confirmation. Never deletes anything.
"""

import os
import re
import shutil
import logging
import sys
from datetime import datetime
from pathlib import Path


# ── Constants ────────────────────────────────────────────────────────────────

PEOPLE = ["Ben", "Quynh", "Hugh", "Sara"]

TAX_KEYWORDS = [
    r"\bw[-_]?2\b",
    r"\b1099\b", r"\b1040\b", r"\b1065\b", r"\b1120\b",
    r"\bschedule[-_ ]?c\b",
    r"\btax(es|return|_return|-return)?\b",
    r"\birs\b",
    r"\bfederal\b",
    r"\bstate[-_ ]?return\b",
    r"\brefund\b",
    r"\bwithholding\b",
    r"\bdeduction\b",
    r"\bturbotax\b",
    r"\bh&r[-_ ]?block\b",
    r"\bhrblock\b",
    r"\btaxact\b",
    r"\bestimated[-_ ]?tax\b",
    r"\bquarterly\b",
]

TAX_EXTENSIONS = {".pdf", ".tax", ".taxreturn"}

PROTECTED_PATHS = [
    "C:\\Windows",
    "C:\\Program Files",
    "C:\\Program Files (x86)",
    "AppData",
]

CURRENT_YEAR = datetime.now().year


# ── Helpers ──────────────────────────────────────────────────────────────────

def get_documents_path() -> Path:
    """Return the user's Documents folder path."""
    if sys.platform == "win32":
        docs = Path(os.environ.get("USERPROFILE", "C:\\Users\\User")) / "Documents"
    else:
        # Fallback for dev/testing on non-Windows
        docs = Path.home() / "Documents"
    return docs


def is_protected(path: Path) -> bool:
    path_str = str(path)
    for protected in PROTECTED_PATHS:
        if protected.lower() in path_str.lower():
            return True
    return False


def is_tax_related(filename: str) -> bool:
    name = filename.lower()
    stem = Path(filename).suffix.lower()

    if stem in TAX_EXTENSIONS:
        # Extension alone is enough for .tax / .taxreturn; .pdf needs a keyword
        if stem in {".tax", ".taxreturn"}:
            return True

    for pattern in TAX_KEYWORDS:
        if re.search(pattern, name, re.IGNORECASE):
            return True
    return False


def attribute_file(filepath: Path) -> str:
    """Return person name or '_Unassigned'."""
    name_lower = filepath.stem.lower()

    # Priority 1: explicit name in filename
    for person in PEOPLE:
        if person.lower() in name_lower:
            return person

    # Priority 2: file lives inside a folder named after a person
    for part in filepath.parts:
        for person in PEOPLE:
            if part.lower() == person.lower():
                return person

    return "_Unassigned"


def setup_logger(log_dir: Path) -> logging.Logger:
    log_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    log_path = log_dir / f"run_{timestamp}.log"

    logger = logging.getLogger("DocumentSorter")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(log_path, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter("%(asctime)s  %(levelname)-8s  %(message)s"))
    logger.addHandler(fh)

    return logger, log_path


# ── Phase 1: Scan ─────────────────────────────────────────────────────────────

def scan(docs_path: Path) -> list[dict]:
    """Recursively scan docs_path and return tax-file records."""
    records = []
    for filepath in docs_path.rglob("*"):
        if not filepath.is_file():
            continue
        if is_protected(filepath):
            continue
        if is_tax_related(filepath.name):
            person = attribute_file(filepath)
            stat = filepath.stat()
            records.append({
                "src": filepath,
                "person": person,
                "size": stat.st_size,
                "mtime": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d"),
            })
    return records


# ── Phase 2: Build move plan ──────────────────────────────────────────────────

def build_plan(records: list[dict], tax_root: Path) -> tuple[list[dict], list[dict]]:
    """Return (moves, conflicts)."""
    moves = []
    conflicts = []

    for rec in records:
        dest = tax_root / rec["person"] / rec["src"].name
        if dest.exists():
            conflicts.append({"src": rec["src"], "dest": dest})
        else:
            moves.append({**rec, "dest": dest})

    return moves, conflicts


# ── Phase 3: Preview report ───────────────────────────────────────────────────

def print_preview(records: list[dict], moves: list[dict], conflicts: list[dict]):
    total = len(records)
    tax_count = len(moves) + len(conflicts)
    per_person = {p: sum(1 for m in moves if m["person"] == p) for p in PEOPLE}
    unassigned = sum(1 for m in moves if m["person"] == "_Unassigned")

    print()
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║              DOCUMENT SORTER — DRY RUN PREVIEW                  ║")
    print("╠══════════════════════════════════════════════════════════════════╣")
    print(f"║  Files scanned:   {total:<47}║")
    print(f"║  Tax-related:     {tax_count:<47}║")
    assigned_str = " | ".join(f"{p}: {per_person[p]}" for p in PEOPLE)
    print(f"║  Assigned:        {len(moves) - unassigned:<47}║")
    print(f"║    ({assigned_str})")
    print(f"║  Unassigned:      {unassigned:<47}║")
    print(f"║  Conflicts:       {len(conflicts):<47}║")
    print("╚══════════════════════════════════════════════════════════════════╝")

    if not moves and not conflicts:
        print("\nNo tax-related documents found.")
        return

    print("\nPROPOSED MOVES:")
    print("─" * 66)
    for i, m in enumerate(moves, 1):
        src_rel = m["src"].name
        dest_rel = str(m["dest"]).replace(str(m["dest"].parent.parent.parent), "")
        attribution = (
            f'Name match ("{m["person"]}" in filename)'
            if m["person"] != "_Unassigned"
            else "UNASSIGNED — no name match found, needs manual review"
        )
        print(f"\n[{i}] {m['src']}")
        print(f"    → {m['dest']}")
        print(f"    Attribution: {attribution}")

    if conflicts:
        print("\n" + "─" * 66)
        print("SKIPPED (conflicts — would overwrite existing file):")
        for c in conflicts:
            print(f"[!] {c['src']} already exists at destination. Skipping.")

    print("\n" + "─" * 66)
    print("NO FILES HAVE BEEN MOVED YET.")
    print("Type CONFIRM to execute all proposed moves, or CANCEL to abort.")
    print()


# ── Phase 4: Execute ──────────────────────────────────────────────────────────

def execute(moves: list[dict], logger: logging.Logger) -> tuple[int, int]:
    succeeded = 0
    errors = 0

    for m in moves:
        dest: Path = m["dest"]
        src: Path = m["src"]
        try:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dest))
            logger.info(f"MOVED  {src}  →  {dest}")
            succeeded += 1
        except PermissionError:
            logger.error(f"LOCKED {src}  — file in use, skipped")
            print(f"  [!] Skipped (locked): {src.name}")
            errors += 1
        except OSError as exc:
            logger.error(f"ERROR  {src}  —  {exc}")
            print(f"  [!] Error moving {src.name}: {exc}")
            errors += 1

    return succeeded, errors


# ── Phase 5: Summary ──────────────────────────────────────────────────────────

def print_summary(succeeded: int, skipped: int, errors: int, log_path: Path):
    print()
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║              DOCUMENT SORTER — EXECUTION COMPLETE               ║")
    print("╠══════════════════════════════════════════════════════════════════╣")
    print(f"║  Moved successfully:   {succeeded:<43}║")
    print(f"║  Skipped (conflict):   {skipped:<43}║")
    print(f"║  Errors:               {errors:<43}║")
    print(f"║  Log saved to:         {str(log_path):<43}║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    docs_path = get_documents_path()

    if not docs_path.exists():
        print(f"[!] Documents folder not found at: {docs_path}")
        docs_path = Path(input("Enter the full path to your Documents folder: ").strip())
        if not docs_path.exists():
            print("[!] Path does not exist. Aborting.")
            sys.exit(1)

    tax_root = docs_path / "Tax Documents"
    log_dir = docs_path / "_SorterLogs"

    print(f"\nScanning: {docs_path}")
    print("Phase 1: Scanning for tax-related documents (read-only)...")

    records = scan(docs_path)

    if not records:
        print("No tax-related documents found. Nothing to do.")
        sys.exit(0)

    moves, conflicts = build_plan(records, tax_root)

    print_preview(records, moves, conflicts)

    if not moves:
        print("No moves to perform (all files either conflict or none found).")
        sys.exit(0)

    # Wait for confirmation
    while True:
        response = input("Your choice: ").strip().upper()
        if response in ("CONFIRM", "YES, PROCEED", "YES"):
            break
        if response in ("CANCEL", "NO", "ABORT"):
            print("Aborted. No files were moved.")
            sys.exit(0)
        print("Please type CONFIRM to proceed or CANCEL to abort.")

    logger, log_path = setup_logger(log_dir)
    logger.info(f"Session started. Docs path: {docs_path}")
    logger.info(f"Tax files found: {len(records)}  |  Planned moves: {len(moves)}  |  Conflicts: {len(conflicts)}")

    print("\nExecuting moves...")
    succeeded, errors = execute(moves, logger)

    logger.info(f"Session complete. Moved: {succeeded}  Errors: {errors}  Conflicts skipped: {len(conflicts)}")

    print_summary(succeeded, len(conflicts), errors, log_path)


if __name__ == "__main__":
    main()
