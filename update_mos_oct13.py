#!/usr/bin/env python3
"""MOS_DATA -> Oct 12 closes. TTD downgraded: the value-trap question is now answered."""
import re, sys, os, shutil
FILE='templates/index.html'; shutil.copy(FILE,FILE+'.bak'); src=open(FILE).read()
def sub1(p,r,f=0,l=''):
    global src
    src,n=re.subn(p, lambda m:r, src, count=1, flags=f)
    if n!=1: print(f'ERROR {l}: {n}'); sys.exit(1)

sub1(r"updated: 'September 5, 2026 \(prices Sep 4 session close\)',",
     "updated: 'October 13, 2026 (prices Oct 12 settled close)',", l='stamp')

ROWS={
'NVDA':("{ticker:'NVDA', price:226.32, eps:6.53,  growth:28,   industryPE:42, industryLabel:'Semiconductors 42&times;',     doublings:3, futureEPS:52.24, fairValue:549, mosPrice:274, verdict:'YES',  verdictCls:'mos-v-yes',  "
 "verdictNote:'&minus;59% below FV. Flat at $226.32 over five weeks, still $48 beneath the MOS price $274. The formula margin has now survived a rally, a pullback, a bounce and a sector run that left NVDA behind &mdash; which is what a real margin of safety looks like. NOTE THE DIVERGENCE: the swing desk has just flagged NVDA for relative weakness ($2 above its SMA50 while peers ran 20%+). Long-horizon value is unbothered by five weeks of underperformance; the swing framework is not. Two clocks.'}"),
'ORCL':("{ticker:'ORCL', price:137.39, eps:5.63,  growth:24,   industryPE:38, industryLabel:'Enterprise Software 38&times;',doublings:3, futureEPS:45.04, fairValue:428, mosPrice:214, verdict:'YES',  verdictCls:'mos-v-yes',  "
 "verdictNote:'&minus;68% below FV &mdash; the widest margin this screen has recorded for ORCL. The earnings decline took it to $77 below the MOS price $214 (was $55 below on Sep 5, $4 below in June). The long-horizon screen and the swing desk have now CONVERGED for the first time: the swing side is watching for an SMA50 reclaim at $145.90 to validate a zone entry, and the value side already qualifies. If that reclaim comes, both frameworks point the same way. &#9733; PICK'}"),
'TTD': ("{ticker:'TTD',  price:11.94,  eps:2.07,  growth:16,   industryPE:35, industryLabel:'Ad-Tech 35&times;',            doublings:2, futureEPS:8.28,  fairValue:72,  mosPrice:36,  verdict:'NO',   verdictCls:'mos-v-no',   "
 "verdictNote:'&#9888; DOWNGRADED TO NO &mdash; THE VALUE-TRAP QUESTION IS ANSWERED. TTD is $11.94, down 40% from the $19.95 where this screen first flagged it in June, and down 17% in the last five weeks alone. It has not participated in ANY rally across four call ups. The formula still computes a &minus;83% discount to fair value, and that is precisely the problem: a formula that gets cheaper every time the stock halves is reporting broken inputs, not opportunity. The 16% growth assumption behind futureEPS $8.28 was flagged as unverified in August and September and remains unverified. VERDICT: do not treat the discount as a signal until the growth rate is confirmed from an actual filing. Logged as the clearest example of why a margin-of-safety screen needs a price-action override.'}"),
'GOOGL':("{ticker:'GOOGL',price:352.72, eps:13.11, growth:15,   industryPE:28, industryLabel:'Internet / Mega-Cap 28&times;', doublings:2, futureEPS:52.44, fairValue:367, mosPrice:184, verdict:'NEAR', verdictCls:'mos-v-near', "
 "verdictNote:'$14 below fair value $367 at $352.72, having risen 4.2% over five weeks. The discount to FV has narrowed from $30 to $14 and GOOGL has held its NEAR verdict across four consecutive call ups without ever approaching the MOS price $184 &mdash; it remains $169 above it. Consistently fair, never cheap. That is a useful reference point for how rarely a mega-cap clears a half-of-fair-value bar.'}"),
'MSFT':("{ticker:'MSFT', price:541.15, eps:16.79, growth:13.5, industryPE:38, industryLabel:'Enterprise Software 38&times;',doublings:1, futureEPS:33.58, fairValue:319, mosPrice:160, verdict:'NO',   verdictCls:'mos-v-no',   "
 "verdictNote:'+70% above FV at $541.15 &mdash; the widest gap recorded (+31% Jun, +54% Aug, +57% Sep). MSFT has moved further from formula value at every single call up since the Azure gap. Only 1 doubling at 13.5% growth caps fair value at $319. The swing desk holds it as a gate pass with a redrawn $502&ndash;525 zone; the long-horizon screen has never been close to buying it. Both readings are correct on their own terms.'}"),
'META':("{ticker:'META', price:742.96, eps:27.52, growth:13.5, industryPE:28, industryLabel:'Internet / Mega-Cap 28&times;', doublings:1, futureEPS:55.04, fairValue:385, mosPrice:193, verdict:'NO',   verdictCls:'mos-v-no',   "
 "verdictNote:'+93% above FV at $742.96 after a 20.5% five-week run &mdash; nearly double formula fair value and by far the widest gap on this screen. Same structural cap as MSFT: high EPS but 13.5% growth yields only 1 doubling, holding fair value at $385. No safety buffer anywhere near current levels.'}"),
}
for tk,r in ROWS.items():
    sub1(r"\{ticker:'"+tk+r"',\s*price:[\d.]+,.*?verdictNote:'(?:[^'\\]|\\.)*'\}", r, f=re.DOTALL, l=f'row {tk}')

for tk,old,new in [('ORCL','158.77','137.39'),('TTD','14.44','11.94')]:
    p=r"(\n    ticker:'"+tk+r"',(?:(?!ticker:).)*?\n    price:)"+re.escape(old)+r","
    src,n=re.subn(p, lambda m:m.group(1)+new+',', src, count=1, flags=re.DOTALL)
    if n!=1: print(f'ERROR {tk} deep-dive {n}'); sys.exit(1)
    print(f'  {tk} deep-dive {old} -> {new}')

for a,b in [('Screener Results &mdash; Sep 5, 2026 (prices Sep 4 session close)','Screener Results &mdash; Oct 13, 2026 (prices Oct 12 settled close)'),
            ('&#10003; Margin of Safety Buy &mdash; reaffirmed Sep 5, 2026','&#10003; Margin of Safety Buy &mdash; reaffirmed Oct 13, 2026 &mdash; widest margin yet'),
            ('&#9670; Deep Value Signal &mdash; reviewed Sep 5, 2026','&#9670; Deep Value Signal &mdash; DOWNGRADED Oct 13, 2026'),
            ('&#10003; Margin of Safety Buy &mdash; reviewed Sep 5, 2026 &mdash; &#9888; DID NOT JOIN THE BOUNCE','&#9888; DOWNGRADED TO NO &mdash; Oct 13, 2026 &mdash; DOWN 40% SINCE FIND, INPUTS UNVERIFIED'),
            ('Research Source Log &mdash; formula inputs from Jun 8, 2026; prices Sep 4, 2026','Research Source Log &mdash; formula inputs from Jun 8, 2026 (TTD growth rate UNVERIFIED); prices Oct 12, 2026')]:
    src=src.replace(a,b)
open(FILE,'w').write(src); print('OK - MOS refreshed'); os.remove(FILE+'.bak')
