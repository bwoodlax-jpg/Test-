#!/usr/bin/env python3
"""MOS_DATA -> Sep 2 closes. Formula inputs unchanged; only price-dependent fields move."""
import re, sys, os, shutil
FILE='templates/index.html'; shutil.copy(FILE,FILE+'.bak'); src=open(FILE).read()

def sub1(pat, rep, flags=0, label=''):
    global src
    src,n = re.subn(pat, lambda m: rep, src, count=1, flags=flags)
    if n!=1: print(f'ERROR: {label} matched {n}'); sys.exit(1)

sub1(r"updated: 'August 13, 2026 \(prices Aug 12 close\)',",
     "updated: 'September 3, 2026 (prices Sep 2 close)',", label='stamp')

ROWS = {
'NVDA': ("{ticker:'NVDA', price:224.41, eps:6.53,  growth:28,   industryPE:42, industryLabel:'Semiconductors 42&times;',     doublings:3, futureEPS:52.24, fairValue:549, mosPrice:274, verdict:'YES',  verdictCls:'mos-v-yes',  "
 "verdictNote:'&minus;59% below FV. Flat at $224.41 through the three-week pullback. Still $50 beneath the MOS price $274 &mdash; the formula margin has survived both a 10% rally and a market pullback. Semiconductor industry PE 42&times; (conservative; sector median 46&times;).'}"),
'ORCL': ("{ticker:'ORCL', price:145.75, eps:5.63,  growth:24,   industryPE:38, industryLabel:'Enterprise Software 38&times;',doublings:3, futureEPS:45.04, fairValue:428, mosPrice:214, verdict:'YES',  verdictCls:'mos-v-yes',  "
 "verdictNote:'&minus;66% below FV and the margin keeps widening: $4 below MOS price on Jun 8, $61 below on Aug 13, now $68 below at $145.75. Meanwhile the swing desk notes ORCL has just reclaimed its SMA50 for the first time in months. Long-horizon value and short-term structure are converging for the first time. &#9733; PICK'}"),
'TTD':  ("{ticker:'TTD',  price:14.55,  eps:2.07,  growth:16,   industryPE:35, industryLabel:'Ad-Tech 35&times;',            doublings:2, futureEPS:8.28,  fairValue:72,  mosPrice:36,  verdict:'YES',  verdictCls:'mos-v-yes',  "
 "verdictNote:'&minus;80% below FV. Bounced 7.9% off the lows to $14.55 &mdash; the first sign of stabilisation after halving twice. Still ~7&times; forward earnings. The value-trap question flagged Aug 13 stands unanswered: verify the 16% growth assumption at the next print before sizing. &#9888; DEEPEST DISCOUNT, HIGHEST BURDEN OF PROOF'}"),
'GOOGL':("{ticker:'GOOGL',price:337.12, eps:13.11, growth:15,   industryPE:28, industryLabel:'Internet / Mega-Cap 28&times;', doublings:2, futureEPS:52.44, fairValue:367, mosPrice:184, verdict:'NEAR', verdictCls:'mos-v-near', "
 "verdictNote:'Now $30 BELOW fair value $367, having slipped further from $343.54. The discount to FV is widening (was $1 ABOVE on Jun 8). But at $337.12 it remains $153 above the MOS price $184, so it still does not clear the half-of-fair-value bar. Genuinely cheap, not yet a formula buy.'}"),
'MSFT': ("{ticker:'MSFT', price:496.82, eps:16.79, growth:13.5, industryPE:38, industryLabel:'Enterprise Software 38&times;',doublings:1, futureEPS:33.58, fairValue:319, mosPrice:160, verdict:'NO',   verdictCls:'mos-v-no',   "
 "verdictNote:'+56% above FV, the widest gap yet (+31% Jun 8, +54% Aug 13). The Azure gap keeps pushing MSFT away from value. Only 1 doubling at 13.5% growth caps formula fair value at $319. Excellent business, no margin of safety &mdash; the swing desk rides it, the long-horizon screen will not buy it.'}"),
'META': ("{ticker:'META', price:592.85, eps:27.52, growth:13.5, industryPE:28, industryLabel:'Internet / Mega-Cap 28&times;', doublings:1, futureEPS:55.04, fairValue:385, mosPrice:193, verdict:'NO',   verdictCls:'mos-v-no',   "
 "verdictNote:'+54% above FV, back near the Jun 8 level after a brief dip to +50%. Same structural cap as MSFT: high EPS but 13.5% growth yields only 1 doubling, holding formula fair value at $385. No safety buffer.'}"),
}
for tk,newrow in ROWS.items():
    sub1(r"\{ticker:'"+tk+r"',\s*price:[\d.]+,.*?verdictNote:'(?:[^'\\]|\\.)*'\}", newrow, flags=re.DOTALL, label=f'row {tk}')

for tk,old,new in [('ORCL','153.28','145.75'), ('TTD','13.49','14.55')]:
    pat = r"(\n    ticker:'"+tk+r"',(?:(?!ticker:).)*?\n    price:)"+re.escape(old)+r","
    src,n = re.subn(pat, lambda m: m.group(1)+new+',', src, count=1, flags=re.DOTALL)
    if n!=1: print(f'ERROR: {tk} deep-dive {n}'); sys.exit(1)
    print(f'  {tk} deep-dive {old} -> {new}')

src = src.replace('Screener Results &mdash; Aug 13, 2026 (prices Aug 12 close)',
                  'Screener Results &mdash; Sep 3, 2026 (prices Sep 2 close)')
src = src.replace('&#10003; Margin of Safety Buy &mdash; reaffirmed Aug 13, 2026',
                  '&#10003; Margin of Safety Buy &mdash; reaffirmed Sep 3, 2026')
src = src.replace('&#9670; Deep Value Signal &mdash; reviewed Aug 13, 2026',
                  '&#9670; Deep Value Signal &mdash; reviewed Sep 3, 2026')
src = src.replace('&#10003; Margin of Safety Buy &mdash; reviewed Aug 13, 2026 &mdash; &#9888; DOWN 32% SINCE FIND',
                  '&#10003; Margin of Safety Buy &mdash; reviewed Sep 3, 2026 &mdash; &#9888; DOWN 27% SINCE FIND, BOUNCING')
src = src.replace('Research Source Log &mdash; formula inputs from Jun 8, 2026; prices Aug 12, 2026',
                  'Research Source Log &mdash; formula inputs from Jun 8, 2026; prices Sep 2, 2026')

open(FILE,'w').write(src); print('OK - MOS_DATA refreshed'); os.remove(FILE+'.bak')
