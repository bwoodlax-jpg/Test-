#!/usr/bin/env python3
"""
Pre-populate SEMI_AI_STOCKS with static ~2025 financial estimates.
Rows will render immediately without requiring Finnhub API load.
YTD% still requires Load Live Data (can't know 2026 YTD without live data).
"""
import re

path = '/home/user/Test-/templates/index.html'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

errors = []

def rep(old, new, label):
    global c
    if old in c:
        c = c.replace(old, new, 1)
        print(f'OK: {label}')
    else:
        errors.append(label)
        print(f'ERROR: {label} — not found')

# ── 1. Financial data per ticker (~2025 estimates) ────────────────────────────
FINANCIALS = {
    'MPWR': {'pe': 52.0,  'fwdPE': 39.0,  'eps':  12.85, 'fwdEPS': 16.40},
    'ENTG': {'pe': 67.0,  'fwdPE': 41.0,  'eps':   2.68, 'fwdEPS':  4.25},
    'ONTO': {'pe': 27.0,  'fwdPE': 21.0,  'eps':   4.35, 'fwdEPS':  5.60},
    'ACLS': {'pe': 13.0,  'fwdPE': 11.0,  'eps':   8.65, 'fwdEPS':  9.40},
    'LSCC': {'pe': 42.0,  'fwdPE': 32.0,  'eps':   1.12, 'fwdEPS':  1.58},
    'FORM': {'pe': 23.0,  'fwdPE': 18.0,  'eps':   1.65, 'fwdEPS':  2.05},
    'CEVA': {'pe': 64.0,  'fwdPE': 44.0,  'eps':   0.60, 'fwdEPS':  0.88},
    'AMBA': {'pe': None,  'fwdPE': 82.0,  'eps':  -0.38, 'fwdEPS':  0.42},
    'RMBS': {'pe': 27.0,  'fwdPE': 21.0,  'eps':   1.74, 'fwdEPS':  2.18},
    'WOLF': {'pe': None,  'fwdPE': None,  'eps':  -3.45, 'fwdEPS': None},
    'NVTS': {'pe': None,  'fwdPE': None,  'eps':  -0.38, 'fwdEPS': None},
    'ON':   {'pe': 13.0,  'fwdPE': 11.0,  'eps':   4.45, 'fwdEPS':  4.85},
    'SITM': {'pe': 60.0,  'fwdPE': 44.0,  'eps':   1.28, 'fwdEPS':  1.88},
    'ALGM': {'pe': 27.0,  'fwdPE': 21.0,  'eps':   0.94, 'fwdEPS':  1.22},
    'CRUS': {'pe': 17.0,  'fwdPE': 14.0,  'eps':   6.55, 'fwdEPS':  7.85},
    'COHU': {'pe': 22.0,  'fwdPE': 17.0,  'eps':   1.12, 'fwdEPS':  1.52},
    'ICHR': {'pe': 22.0,  'fwdPE': 17.0,  'eps':   2.35, 'fwdEPS':  3.15},
    'ACMR': {'pe': 21.0,  'fwdPE': 16.0,  'eps':   2.12, 'fwdEPS':  2.65},
    'VECO': {'pe': 23.0,  'fwdPE': 17.0,  'eps':   1.22, 'fwdEPS':  1.62},
    'UCTT': {'pe': 21.0,  'fwdPE': 16.0,  'eps':   2.05, 'fwdEPS':  2.65},
    'AZTA': {'pe': None,  'fwdPE': 28.0,  'eps':   0.52, 'fwdEPS':  1.25},
    'SMTC': {'pe': 92.0,  'fwdPE': 38.0,  'eps':   0.50, 'fwdEPS':  1.22},
    'IPGP': {'pe': 24.0,  'fwdPE': 21.0,  'eps':   4.25, 'fwdEPS':  4.85},
    'POWI': {'pe': 37.0,  'fwdPE': 29.0,  'eps':   1.48, 'fwdEPS':  1.88},
    'DIOD': {'pe': 12.0,  'fwdPE': 10.0,  'eps':   4.55, 'fwdEPS':  5.25},
    'TER':  {'pe': 32.0,  'fwdPE': 27.0,  'eps':   3.42, 'fwdEPS':  4.15},
    'CAMT': {'pe': 27.0,  'fwdPE': 21.0,  'eps':   2.12, 'fwdEPS':  2.72},
    'NXPI': {'pe': 16.0,  'fwdPE': 13.0,  'eps':  12.65, 'fwdEPS': 14.55},
    'STM':  {'pe': 11.0,  'fwdPE':  9.0,  'eps':   2.85, 'fwdEPS':  3.25},
    'MKSI': {'pe': 37.0,  'fwdPE': 27.0,  'eps':   3.88, 'fwdEPS':  5.25},
}

def fv(v):
    return 'null' if v is None else str(v)

# ── 2. Inject financial fields into each SEMI_AI_STOCKS entry ────────────────
def inject_financials(match):
    entry = match.group(0)
    tm = re.search(r"t:'([A-Z]+)'", entry)
    if not tm:
        return entry
    ticker = tm.group(1)
    if ticker not in FINANCIALS:
        print(f'  WARNING: no data for {ticker}')
        return entry
    f = FINANCIALS[ticker]
    fields = f"pe:{fv(f['pe'])}, fwdPE:{fv(f['fwdPE'])}, eps:{fv(f['eps'])}, fwdEPS:{fv(f['fwdEPS'])}, "
    # Insert before desc:
    if 'desc:' not in entry:
        return entry
    return entry.replace('desc:', fields + 'desc:', 1)

# Only modify entries inside SEMI_AI_STOCKS block
semi_start = c.find('const SEMI_AI_STOCKS = [')
semi_end   = c.find('];\n', semi_start) + 3
if semi_start == -1:
    errors.append('SEMI_AI_STOCKS block not found')
    print('ERROR: SEMI_AI_STOCKS block not found')
else:
    block     = c[semi_start:semi_end]
    new_block = re.sub(r"\{t:'[A-Z]+',[^;]+?desc:'[^']*(?:&#39;[^']*)*'\}", inject_financials, block)
    if new_block == block:
        errors.append('no SEMI_AI_STOCKS entries matched')
        print('ERROR: regex matched nothing in SEMI_AI_STOCKS block')
    else:
        changed = sum(1 for a, b in zip(block.split('\n'), new_block.split('\n')) if a != b)
        c = c[:semi_start] + new_block + c[semi_end:]
        print(f'OK: injected financial fields ({changed} lines changed)')

# ── 3. Update init() — pre-populate rows with static financial data ───────────
rep(
    "      this.semiRows = SEMI_AI_STOCKS.map(function(s) {\n"
    "        return {t:s.t, c:s.c, sec:s.s, desc:s.desc, ytd:null, pe:null, fwdPE:null, eps:null, fwdEPS:null, loaded:false, err:false};\n"
    "      });\n"
    "    },",
    "      this.semiRows = SEMI_AI_STOCKS.map(function(s) {\n"
    "        return {t:s.t, c:s.c, sec:s.s, desc:s.desc, ytd:null,\n"
    "          pe:s.pe!=null?s.pe:null, fwdPE:s.fwdPE!=null?s.fwdPE:null,\n"
    "          eps:s.eps!=null?s.eps:null, fwdEPS:s.fwdEPS!=null?s.fwdEPS:null,\n"
    "          loaded:true, err:false};\n"
    "      });\n"
    "    },",
    'init() static pre-population'
)

# ── 4. Update loadSemiData() reset — keep static data during refresh ──────────
rep(
    "      this.semiRows = SEMI_AI_STOCKS.map(function(s) {\n"
    "        return {t:s.t, c:s.c, sec:s.s, desc:s.desc, ytd:null, pe:null, fwdPE:null, eps:null, fwdEPS:null, loaded:false, err:false};\n"
    "      });\n"
    "      var self = this;",
    "      this.semiRows = SEMI_AI_STOCKS.map(function(s) {\n"
    "        return {t:s.t, c:s.c, sec:s.s, desc:s.desc, ytd:null,\n"
    "          pe:s.pe!=null?s.pe:null, fwdPE:s.fwdPE!=null?s.fwdPE:null,\n"
    "          eps:s.eps!=null?s.eps:null, fwdEPS:s.fwdEPS!=null?s.fwdEPS:null,\n"
    "          loaded:true, err:false};\n"
    "      });\n"
    "      var self = this;",
    'loadSemiData() reset with static data'
)

# ── 5. Update footer note to reflect static data ─────────────────────────────
rep(
    "    <strong style=\"color:var(--dim)\">Data source:</strong> Finnhub.io free tier &mdash; YTD% uses <code>ytdPriceReturnDaily</code>, PE/EPS use <code>peTTM</code>/<code>epsTTM</code>.\n"
    "    Forward PE and Fwd EPS use <code>forwardPE</code>/<code>epsForward</code> &mdash; shown as N/A if not in free tier response.\n"
    "    Hover any synopsis cell for the full description. Rates: 30 stocks = 30 API calls ~20s at Finnhub free tier (60 calls/min).",
    "    <strong style=\"color:var(--dim)\">PE / EPS / Fwd values:</strong> static estimates (~2025 data) &mdash; shown immediately without an API key.\n"
    "    <strong style=\"color:var(--dim)\">YTD%:</strong> requires Finnhub API key &mdash; click <strong>Load Live Data</strong> to fetch current YTD% and refresh all metrics.\n"
    "    Hover any synopsis cell for the full description. Rates: 30 stocks = 30 API calls ~20s at Finnhub free tier (60 calls/min).",
    'footer note static data'
)

# ── 6. Update tab subtitle to mention static data ────────────────────────────
rep(
    "    Click <strong style=\"color:var(--accent)\">Load Live Data</strong> to fetch YTD%, PE, and EPS from Finnhub (requires API key &mdash; free tier, same key as Live Watchlist).\n"
    "    Forward PE / Forward EPS populated if available from Finnhub free tier; otherwise shown as N/A.",
    "    PE, EPS, and Forward values are pre-loaded from static ~2025 estimates &mdash; visible immediately.\n"
    "    Click <strong style=\"color:var(--accent)\">Load Live Data</strong> to refresh all metrics + add current YTD% (requires Finnhub API key &mdash; same key as Live Watchlist).",
    'subtitle static data note'
)

# ── Result ────────────────────────────────────────────────────────────────────
if errors:
    print(f'\nFAILED: {errors}')
    print('File NOT written.')
else:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print('\nAll changes applied. File written.')
