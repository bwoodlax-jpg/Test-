#!/usr/bin/env python3
"""MOS_DATA -> Oct 16 closes."""
import re, sys, os, shutil
FILE='templates/index.html'; shutil.copy(FILE,FILE+'.bak'); src=open(FILE).read()
def sub1(p,r,f=0,l=''):
    global src
    src,n=re.subn(p, lambda m:r, src, count=1, flags=f)
    if n!=1: print(f'ERROR {l}: {n}'); sys.exit(1)

sub1(r"updated: 'October 13, 2026 \(prices Oct 12 settled close\)',",
     "updated: 'October 17, 2026 (prices Oct 16 session close)',", l='stamp')

ROWS={
'NVDA':("{ticker:'NVDA', price:214.14, eps:6.53,  growth:28,   industryPE:42, industryLabel:'Semiconductors 42&times;',     doublings:3, futureEPS:52.24, fairValue:549, mosPrice:274, verdict:'YES',  verdictCls:'mos-v-yes',  "
 "verdictNote:'&minus;61% below FV at $214.14 after a 5.4% decline, now $60 beneath the MOS price $274 &mdash; the margin keeps widening as the AI complex de-rates. THE DIVERGENCE IS NOW SHARP: the swing desk has NVDA blocked, in zone but below a broken SMA50, with the relative-weakness flag fully played out. The value screen is indifferent to four sessions of positioning unwind and sees only a widening discount. Both are correct on their own horizons &mdash; which is precisely why the two tabs are kept separate.'}"),
'ORCL':("{ticker:'ORCL', price:128.22, eps:5.63,  growth:24,   industryPE:38, industryLabel:'Enterprise Software 38&times;',doublings:3, futureEPS:45.04, fairValue:428, mosPrice:214, verdict:'YES',  verdictCls:'mos-v-yes',  "
 "verdictNote:'&minus;70% below FV at $128.22 &mdash; now $86 beneath the MOS price $214, the widest margin ever recorded on this screen for any name. The convergence noted on Oct 13 has broken down again: the swing desk&#39;s reclaim watch is dead (SMA50 turned back down, price $17 under it). So ORCL is deeply cheap on the formula and structurally broken on the chart, for the third call up running. That is a holding pattern, not a contradiction &mdash; the value side waits for the chart, the chart has not come. &#9733; PICK'}"),
'TTD': ("{ticker:'TTD',  price:12.24,  eps:2.07,  growth:16,   industryPE:35, industryLabel:'Ad-Tech 35&times;',            doublings:2, futureEPS:8.28,  fairValue:72,  mosPrice:36,  verdict:'NO',   verdictCls:'mos-v-no',   "
 "verdictNote:'&#9888; REMAINS NO &mdash; the Oct 13 downgrade stands. TTD $12.24, down 39% from the $19.95 where this screen flagged it in June, and it has now failed to participate in every single rally across five call ups. The formula computes a &minus;83% discount, which is the problem rather than the signal: a screen that gets cheaper each time the stock falls is reporting broken inputs. The 16% growth assumption behind futureEPS $8.28 has been flagged unverified in August, September and twice in October and remains unverified. No change until the growth rate is confirmed from a filing.'}"),
'GOOGL':("{ticker:'GOOGL',price:340.59, eps:13.11, growth:15,   industryPE:28, industryLabel:'Internet / Mega-Cap 28&times;', doublings:2, futureEPS:52.44, fairValue:367, mosPrice:184, verdict:'NEAR', verdictCls:'mos-v-near', "
 "verdictNote:'$26 below fair value $367 at $340.59, having given back the recent gain in the unwind. GOOGL has now held a NEAR verdict across five consecutive call ups without once approaching the MOS price $184 &mdash; it remains $157 above it. Consistently fair, never cheap, through a melt-up and a de-rating alike. A useful calibration point for how rarely a quality mega-cap clears a half-of-fair-value bar.'}"),
'MSFT':("{ticker:'MSFT', price:528.95, eps:16.79, growth:13.5, industryPE:38, industryLabel:'Enterprise Software 38&times;',doublings:1, futureEPS:33.58, fairValue:319, mosPrice:160, verdict:'NO',   verdictCls:'mos-v-no',   "
 "verdictNote:'+66% above FV at $528.95, narrowing from +70% on Oct 13 as the unwind trimmed the price. Only 1 doubling at 13.5% growth caps formula fair value at $319. NOTE THE CONTRAST WITH THE SWING DESK, which has MSFT as the closest thing to a second setup (1% above its zone with the gate intact). A name can be the best technical candidate on the board and still be 66% above formula value &mdash; the two frameworks are answering different questions.'}"),
'META':("{ticker:'META', price:709.34, eps:27.52, growth:13.5, industryPE:28, industryLabel:'Internet / Mega-Cap 28&times;', doublings:1, futureEPS:55.04, fairValue:385, mosPrice:193, verdict:'NO',   verdictCls:'mos-v-no',   "
 "verdictNote:'+84% above FV at $709.34, down from +93% on Oct 13 after a 3.7% decline. Still the widest gap on this screen and nearly double formula fair value. Same structural cap as MSFT: high EPS but 13.5% growth yields only 1 doubling, holding fair value at $385. META reports Q3 on Wed Oct 21 &mdash; not a position on either tab, but the single most important AI-capex read-through for the names that are.'}"),
}
for tk,r in ROWS.items():
    sub1(r"\{ticker:'"+tk+r"',\s*price:[\d.]+,.*?verdictNote:'(?:[^'\\]|\\.)*'\}", r, f=re.DOTALL, l=f'row {tk}')

for tk,old,new in [('ORCL','137.39','128.22'),('TTD','11.94','12.24')]:
    p=r"(\n    ticker:'"+tk+r"',(?:(?!ticker:).)*?\n    price:)"+re.escape(old)+r","
    src,n=re.subn(p, lambda m:m.group(1)+new+',', src, count=1, flags=re.DOTALL)
    if n!=1: print(f'ERROR {tk} deep-dive {n}'); sys.exit(1)
    print(f'  {tk} deep-dive {old} -> {new}')

for a,b in [('Screener Results &mdash; Oct 13, 2026 (prices Oct 12 settled close)','Screener Results &mdash; Oct 17, 2026 (prices Oct 16 session close)'),
            ('&#10003; Margin of Safety Buy &mdash; reaffirmed Oct 13, 2026 &mdash; widest margin yet','&#10003; Margin of Safety Buy &mdash; reaffirmed Oct 17, 2026 &mdash; widest margin ever recorded'),
            ('&#9670; Deep Value Signal &mdash; DOWNGRADED Oct 13, 2026','&#9670; Deep Value Signal &mdash; STILL DOWNGRADED Oct 17, 2026'),
            ('&#9888; DOWNGRADED TO NO &mdash; Oct 13, 2026 &mdash; DOWN 40% SINCE FIND, INPUTS UNVERIFIED','&#9888; NO &mdash; Oct 17, 2026 &mdash; DOWN 39% SINCE FIND, INPUTS STILL UNVERIFIED'),
            ('Research Source Log &mdash; formula inputs from Jun 8, 2026 (TTD growth rate UNVERIFIED); prices Oct 12, 2026','Research Source Log &mdash; formula inputs from Jun 8, 2026 (TTD growth rate UNVERIFIED); prices Oct 16, 2026')]:
    src=src.replace(a,b)
open(FILE,'w').write(src); print('OK - MOS refreshed'); os.remove(FILE+'.bak')
