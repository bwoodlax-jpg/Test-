#!/usr/bin/env python3
"""MOS_DATA -> Sep 4 prices."""
import re, sys, os, shutil
FILE='templates/index.html'; shutil.copy(FILE,FILE+'.bak'); src=open(FILE).read()
def sub1(p,r,f=0,l=''):
    global src
    src,n=re.subn(p, lambda m:r, src, count=1, flags=f)
    if n!=1: print(f'ERROR {l}: {n}'); sys.exit(1)

sub1(r"updated: 'September 3, 2026 \(prices Sep 2 close\)',",
     "updated: 'September 5, 2026 (prices Sep 4 session close)',", l='stamp')

ROWS={
'NVDA':("{ticker:'NVDA', price:230.35, eps:6.53,  growth:28,   industryPE:42, industryLabel:'Semiconductors 42&times;',     doublings:3, futureEPS:52.24, fairValue:549, mosPrice:274, verdict:'YES',  verdictCls:'mos-v-yes',  "
 "verdictNote:'&minus;58% below FV. Rose to $230.35 on the rate-hold bounce, still $44 beneath the MOS price $274. The formula margin has now survived a rally, a pullback and a bounce &mdash; which is what a genuine margin of safety looks like. Semiconductor industry PE 42&times;.'}"),
'ORCL':("{ticker:'ORCL', price:158.77, eps:5.63,  growth:24,   industryPE:38, industryLabel:'Enterprise Software 38&times;',doublings:3, futureEPS:45.04, fairValue:428, mosPrice:214, verdict:'YES',  verdictCls:'mos-v-yes',  "
 "verdictNote:'&minus;63% below FV. Bounced 8.9% to $158.77, so the margin narrowed from $68 to $55 below the MOS price $214 &mdash; still comfortably qualifying. NOTE THE DIVERGENCE: the swing desk is standing aside through Thu Sep 10 earnings, while the long-horizon screen is indifferent to a single print. Two frameworks, two clocks, both valid. &#9733; PICK'}"),
'TTD': ("{ticker:'TTD',  price:14.44,  eps:2.07,  growth:16,   industryPE:35, industryLabel:'Ad-Tech 35&times;',            doublings:2, futureEPS:8.28,  fairValue:72,  mosPrice:36,  verdict:'YES',  verdictCls:'mos-v-yes',  "
 "verdictNote:'&minus;80% below FV at $14.44, drifting rather than recovering &mdash; it did NOT participate in the rate-hold bounce that lifted everything else, which is the same relative-weakness signal flagged on AVGO. Still ~7&times; forward earnings. The value-trap question raised in August is now two call ups old and unanswered. Verify the 16% growth assumption at the next print before sizing. &#9888; DEEPEST DISCOUNT, HIGHEST BURDEN OF PROOF'}"),
'GOOGL':("{ticker:'GOOGL',price:338.50, eps:13.11, growth:15,   industryPE:28, industryLabel:'Internet / Mega-Cap 28&times;', doublings:2, futureEPS:52.44, fairValue:367, mosPrice:184, verdict:'NEAR', verdictCls:'mos-v-near', "
 "verdictNote:'$29 below fair value $367 at $338.50. The discount to FV has held steady across three call ups (was $1 ABOVE in June). But at $338.50 it remains $155 above the MOS price $184, so it still does not clear the half-of-fair-value bar. Genuinely cheap on the formula, not a formula buy.'}"),
'MSFT':("{ticker:'MSFT', price:499.68, eps:16.79, growth:13.5, industryPE:38, industryLabel:'Enterprise Software 38&times;',doublings:1, futureEPS:33.58, fairValue:319, mosPrice:160, verdict:'NO',   verdictCls:'mos-v-no',   "
 "verdictNote:'+57% above FV, the widest gap recorded (+31% Jun, +54% Aug, +56% Sep 3). MSFT keeps moving away from value. Only 1 doubling at 13.5% growth caps formula fair value at $319. The swing desk holds it as a gate pass; the long-horizon screen will not buy it at any point in this range.'}"),
'META':("{ticker:'META', price:616.75, eps:27.52, growth:13.5, industryPE:28, industryLabel:'Internet / Mega-Cap 28&times;', doublings:1, futureEPS:55.04, fairValue:385, mosPrice:193, verdict:'NO',   verdictCls:'mos-v-no',   "
 "verdictNote:'+60% above FV at $616.75, up from +54% and now the widest gap of the three overvalued names. Same structural cap as MSFT: high EPS but 13.5% growth yields only 1 doubling, holding formula fair value at $385. No safety buffer.'}"),
}
for tk,r in ROWS.items():
    sub1(r"\{ticker:'"+tk+r"',\s*price:[\d.]+,.*?verdictNote:'(?:[^'\\]|\\.)*'\}", r, f=re.DOTALL, l=f'row {tk}')

for tk,old,new in [('ORCL','145.75','158.77'),('TTD','14.55','14.44')]:
    p=r"(\n    ticker:'"+tk+r"',(?:(?!ticker:).)*?\n    price:)"+re.escape(old)+r","
    src,n=re.subn(p, lambda m:m.group(1)+new+',', src, count=1, flags=re.DOTALL)
    if n!=1: print(f'ERROR {tk} deep-dive {n}'); sys.exit(1)
    print(f'  {tk} deep-dive {old} -> {new}')

for a,b in [('Screener Results &mdash; Sep 3, 2026 (prices Sep 2 close)','Screener Results &mdash; Sep 5, 2026 (prices Sep 4 session close)'),
            ('&#10003; Margin of Safety Buy &mdash; reaffirmed Sep 3, 2026','&#10003; Margin of Safety Buy &mdash; reaffirmed Sep 5, 2026'),
            ('&#9670; Deep Value Signal &mdash; reviewed Sep 3, 2026','&#9670; Deep Value Signal &mdash; reviewed Sep 5, 2026'),
            ('&#10003; Margin of Safety Buy &mdash; reviewed Sep 3, 2026 &mdash; &#9888; DOWN 27% SINCE FIND, BOUNCING','&#10003; Margin of Safety Buy &mdash; reviewed Sep 5, 2026 &mdash; &#9888; DID NOT JOIN THE BOUNCE'),
            ('Research Source Log &mdash; formula inputs from Jun 8, 2026; prices Sep 2, 2026','Research Source Log &mdash; formula inputs from Jun 8, 2026; prices Sep 4, 2026')]:
    src=src.replace(a,b)
open(FILE,'w').write(src); print('OK - MOS refreshed'); os.remove(FILE+'.bak')
