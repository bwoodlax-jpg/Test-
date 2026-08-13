#!/usr/bin/env python3
"""Refresh MOS_DATA prices and verdicts with Aug 12 closes.
Formula inputs (EPS, growth, industry PE) are unchanged — only price-dependent
fields move: current price, distance to fair value, and the verdict."""
import re, sys, os, shutil

FILE = 'templates/index.html'
shutil.copy(FILE, FILE + '.bak')
src = open(FILE, 'r').read()

def sub1(pattern, repl, flags=0, label=''):
    global src
    src, n = re.subn(pattern, lambda m: repl, src, count=1, flags=flags)
    if n != 1:
        print(f'ERROR: {label} matched {n} times (expected 1)')
        sys.exit(1)

# 1. Refresh the updated stamp
sub1(r"const MOS_DATA = \{\n  updated: 'June 8, 2026',",
     "const MOS_DATA = {\n  updated: 'August 13, 2026 (prices Aug 12 close)',",
     label='updated stamp')

# 2. Per-stock price + verdict refresh. Fair value and MOS price are formula
#    outputs from EPS/growth/industry PE, so they do not move with price.
ROWS = {
'NVDA':  ("{ticker:'NVDA', price:224.09, eps:6.53,  growth:28,   industryPE:42, industryLabel:'Semiconductors 42&times;',     doublings:3, futureEPS:52.24, fairValue:549, mosPrice:274, verdict:'YES',  verdictCls:'mos-v-yes',  "
          "verdictNote:'&minus;59% below FV. Rose from $205 to $224.09 since the Jun 8 run but still $50 beneath the MOS price $274 &mdash; the formula margin survived a 10% rally. Semiconductor industry avg PE 42&times; (conservative; sector median 46&times;).'}"),
'ORCL':  ("{ticker:'ORCL', price:153.28, eps:5.63,  growth:24,   industryPE:38, industryLabel:'Enterprise Software 38&times;',doublings:3, futureEPS:45.04, fairValue:428, mosPrice:214, verdict:'YES',  verdictCls:'mos-v-yes',  "
          "verdictNote:'&minus;64% below FV. The margin WIDENED dramatically: ORCL was $4 below MOS price $214 on Jun 8, it is now $61 below at $153.28. Long-horizon value improved even as the swing setup broke (SMA50 falling). Two frameworks, two answers &mdash; that is by design. &#9733; PICK'}"),
'TTD':   ("{ticker:'TTD',  price:13.49,  eps:2.07,  growth:16,   industryPE:35, industryLabel:'Ad-Tech 35&times;',            doublings:2, futureEPS:8.28,  fairValue:72,  mosPrice:36,  verdict:'YES',  verdictCls:'mos-v-yes',  "
          "verdictNote:'&minus;81% below FV. Fell another 32% from $19.95 to $13.49 &mdash; now ~6.5&times; forward earnings. The formula margin has never been wider, but a stock cutting in half twice demands the value-trap question: is the 16% growth assumption still real? Verify next earnings before sizing. &#9888; DEEPEST DISCOUNT, HIGHEST BURDEN OF PROOF'}"),
'GOOGL': ("{ticker:'GOOGL',price:343.54, eps:13.11, growth:15,   industryPE:28, industryLabel:'Internet / Mega-Cap 28&times;', doublings:2, futureEPS:52.44, fairValue:367, mosPrice:184, verdict:'NEAR', verdictCls:'mos-v-near', "
          "verdictNote:'Now $23 BELOW fair value $367 (was $1 above on Jun 8) after slipping from $368 to $343.54. Genuinely cheap against the formula for the first time &mdash; but still $160 above the MOS price $184, so it does not clear the half-of-fair-value bar. Watch, do not buy on formula grounds.'}"),
'MSFT':  ("{ticker:'MSFT', price:492.43, eps:16.79, growth:13.5, industryPE:38, industryLabel:'Enterprise Software 38&times;',doublings:1, futureEPS:33.58, fairValue:319, mosPrice:160, verdict:'NO',   verdictCls:'mos-v-no',   "
          "verdictNote:'+54% above FV, up from +31% on Jun 8 &mdash; the Azure earnings gap pushed MSFT further from value, not closer. Only 1 doubling at 13.5% growth is what caps the formula value. Excellent business, no margin of safety. The swing desk is riding it; the long-horizon screen will not buy it.'}"),
'META':  ("{ticker:'META', price:578.85, eps:27.52, growth:13.5, industryPE:28, industryLabel:'Internet / Mega-Cap 28&times;', doublings:1, futureEPS:55.04, fairValue:385, mosPrice:193, verdict:'NO',   verdictCls:'mos-v-no',   "
          "verdictNote:'+50% above FV, marginally improved from +54% as price eased from $594 to $578.85. Same structural issue as MSFT: high EPS but 13.5% growth yields only 1 doubling, so the formula caps fair value at $385. No safety buffer.'}"),
}

for ticker, newrow in ROWS.items():
    pat = r"\{ticker:'" + ticker + r"',\s*price:[\d.]+,.*?verdictNote:'(?:[^'\\]|\\.)*'\}"
    sub1(pat, newrow, flags=re.DOTALL, label=f'MOS row {ticker}')

# 3. Deep-dive price fields for ORCL and TTD
for ticker, old, new in [('ORCL', '210', '153.28'), ('TTD', '19.95', '13.49')]:
    pat = r"(\n    ticker:'" + ticker + r"',(?:(?!ticker:).)*?\n    price:)" + re.escape(old) + r","
    src, n = re.subn(pat, lambda m: m.group(1) + new + ',', src, count=1, flags=re.DOTALL)
    if n != 1:
        print(f'ERROR: {ticker} deep-dive price matched {n} times (expected 1)')
        sys.exit(1)
    print(f'  {ticker} deep-dive price {old} -> {new}')

open(FILE, 'w').write(src)
print('OK - MOS_DATA refreshed')
os.remove(FILE + '.bak')
print('Cleaned up backup file')
