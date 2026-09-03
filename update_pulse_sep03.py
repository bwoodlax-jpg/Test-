#!/usr/bin/env python3
"""MARKET_PULSE -> Sep 2 close. Broad pullback; 7 names in zones, 1 gate pass (ANET)."""
import re, sys, os, shutil
FILE='templates/index.html'
shutil.copy(FILE, FILE+'.bak')
src=open(FILE).read()

NEW = """const MARKET_PULSE = {
  date: 'September 3, 2026',
  updated: 'Call Up &mdash; Sep 2 Close (Live Robinhood Data)',
  headline: 'Pullback Reopens The Board &mdash; SEVEN Names Back In Zones &mdash; ANET The Only Gate Pass &mdash; NOW POTW +32% &mdash; PANW &minus;15%, AVGO &minus;12%',
  sentiment: 'PULLBACK &mdash; ZONES REOPENED &mdash; ONE CLEAN SETUP',
  sentimentCls: 'mkt-caution',
  indices: [
    {name:'SPY',        val:'$765.16', chg:'&minus;0.9% since Aug 12 &mdash; off ATH',      dir:'down'},
    {name:'QQQ',        val:'$709.24', chg:'&minus;2.0% &mdash; tech leads lower',           dir:'down'},
    {name:'IWM',        val:'$294.01', chg:'&minus;2.9% &mdash; small caps hit hardest',     dir:'down'},
    {name:'DIA',        val:'$530.62', chg:'&minus;1.2% &mdash; Dow holding up',             dir:'down'},
    {name:'ANET',       val:'$186.10', chg:'&minus;11.6% &mdash; INTO ZONE, GATE PASS',      dir:'down'},
    {name:'NOW',        val:'$136.72', chg:'+9.4% &mdash; POTW now +32% from entry',         dir:'up'},
    {name:'PANW',       val:'$328.48', chg:'&minus;15.1% &mdash; biggest decliner',           dir:'down'},
    {name:'AVGO',       val:'$367.24', chg:'&minus;11.7% &mdash; broke BELOW its zone',       dir:'down'},
  ],
  events: [
    {tag:'SETUP',    tagCls:'evt-watch', headline:'ANET $186.10 &mdash; PERFECT BULLISH STACK IN ZONE &mdash; First Clean Entry In Weeks', body:'Arista fell 11.6% from $210.50 to $186.10, landing inside its buy zone $172&ndash;190 &mdash; and unlike the other six names now sitting in zones, ANET passes the SMA gate. The stack is textbook: SMA50 $181.83 &gt; SMA100 $170.62 &gt; SMA150 $158.55 &gt; SMA200 $151.32, in perfect descending order, with the SMA50 RISING and price above all four. This is the first zone entry the framework has produced with a fully bullish stack &mdash; NOW\\'s +32% winner was taken on an INVERTED stack as an early-recovery bet. Structurally, this is the higher-quality setup. Stop $170 sits on a triple confluence: 2x ATR ($15.63) below price, the SMA100 $170.62, and just under the zone floor $172. R/R = $78.90 up / $16.10 down = 4.90:1.'},
    {tag:'POTW',     tagCls:'evt-watch', headline:'NOW $136.72 &mdash; POTW Now +32.4% &mdash; Raise Trail $113 to $124', body:'ServiceNow added another 9.4% while the broad market fell, taking the Jul 19&ndash;25 zone-floor entry at $103.24 to +32.4%. It is the only watchlist name up meaningfully over the three-week pullback &mdash; relative strength in a down tape, the mirror image of the VRT warning. SMA50 $115.07 is rising steeply and price is $21 above it. ACTION: raise the trail from $113 to $124 (2x ATR of $6.09 below $136.72), locking in +20.1% from entry. Remaining R/R to the $175 target is 3.0:1, still through the gate. Do not add here.'},
    {tag:'ZONES',    tagCls:'evt-watch', headline:'SEVEN NAMES IN ZONES &mdash; SIX BLOCKED BY THE SMA GATE', body:'The pullback pushed seven names into their buy zones: ANET $186, PANW $328, VRT $257, AMD $457, ORCL $146, MRVL $206, LMND $53. Only ANET clears the SMA gate. PANW is the near-miss &mdash; its SMA50 $348.24 is RISING, but price fell $20 beneath it, which is a fresh breakdown rather than an established downtrend. AMD, VRT, MRVL and LMND all have falling SMA50s with price below. ORCL is the curiosity: price $145.75 has reclaimed its SMA50 $139.69 for the first time in months, but that average is still declining, so the gate holds. Exactly the inverse of three weeks ago, when eight names passed the gate and none were in a zone.'},
    {tag:'BROKEN',   tagCls:'evt-geo',   headline:'AVGO $367.24 &mdash; Broke BELOW Its Redrawn Zone &mdash; Second Structural Failure', body:'AVGO fell 11.7% and is now beneath the $390&ndash;408 zone redrawn only three weeks ago, with SMA50 $384.58 falling and price $17 under it. This is the second time AVGO has broken through a zone floor this cycle. The Aug 13 note flagged it as the weakest trend among the gate passers precisely because its SMA50 was flat rather than rising &mdash; that caution proved correct. AVGO now joins VRT in the broken column. No entry, no averaging down; a base plus an SMA50 reclaim is required before the name is tradeable again.'},
    {tag:'PANW',     tagCls:'evt-macro', headline:'PANW &minus;15.1% to $328.48 &mdash; Biggest Decliner &mdash; ZS Reports Thu Sep 3', body:'Palo Alto was the steadiest climber on the board three weeks ago and is now the biggest decliner, giving back 15.1% to $328.48. It sits inside its $322&ndash;350 zone but $20 below a still-RISING SMA50 $348.24 &mdash; the gate blocks. That combination (rising average, price newly beneath it) is a fresh breakdown, and the next two weeks decide whether it resolves as a pullback or a trend change. Zscaler reports Thursday Sep 3 after the close: a strong cybersecurity print would be the most direct read-through available for whether this is sector-wide de-rating or PANW-specific.'},
    {tag:'EARN',     tagCls:'evt-macro', headline:'No Watchlist Earnings Sep 3&ndash;9 &mdash; Labor Day Shortens Next Week', body:'No watchlist name reports through Sep 9, which removes earnings-gap risk from the ANET entry window entirely. The relevant peripheral prints are ZS Thu Sep 3 (cybersecurity read for PANW), plus DOCU, PATH and IOT the same day for enterprise software sentiment. Markets are closed Monday Sep 7 for Labor Day, making next week a four-day session. Entry timing for ANET: Thursday Sep 3 if volume confirms, otherwise Tuesday Sep 8.'},
  ],
  portfolio: [
    {ticker:'ANET', cls:'pi-green',   impact:'IN ZONE + GATE PASS &#10003;',       note:'$186.10 (&minus;11.6%). Zone $172&ndash;190. PERFECT bullish stack: SMA50 $181.83 &gt; SMA100 $170.62 &gt; SMA150 $158.55 &gt; SMA200 $151.32, all below price. R/R 4.90:1, stop $170. The only clean setup on the board.'},
    {ticker:'NOW',  cls:'pi-green',   impact:'WINNER +32% &mdash; $137 &#9650;',   note:'$136.72 (+9.4% while the market fell). POTW entry $103.24, now +32.4%. SMA50 $115.07 rising steeply. Raise trail $113 &rarr; $124, locking +20.1%. Target $175.'},
    {ticker:'PANW', cls:'pi-yellow',  impact:'&minus;15% &mdash; IN ZONE, BLOCKED', note:'$328.48. Biggest decliner. In zone $322&ndash;350 but $20 below a RISING SMA50 $348.24 &mdash; fresh breakdown. ZS earnings Thu Sep 3 is the read-through.'},
    {ticker:'AVGO', cls:'pi-red',     impact:'BROKE ZONE &mdash; $367 &#9888;',     note:'$367.24 (&minus;11.7%). Fell BELOW the $390&ndash;408 zone redrawn three weeks ago. SMA50 $384.58 falling. Second zone break this cycle. Joins VRT as broken.'},
    {ticker:'VRT',  cls:'pi-red',     impact:'STILL BROKEN &mdash; $257 &#9888;',   note:'$256.70 (&minus;11.0%). Reached the redrawn $255&ndash;275 zone but SMA50 $284.54 still falling with price below. Base + SMA50 reclaim required. No entry.'},
    {ticker:'AMD',  cls:'pi-yellow',  impact:'IN ZONE &mdash; BLOCKED &#9660;',     note:'$457.06 (&minus;5.4%). Entered zone $440&ndash;470 as designed, but SMA50 $501.70 still falling with price well below. The zone was set beneath the SMA50 deliberately &mdash; entry needs the reclaim.'},
    {ticker:'ORCL', cls:'pi-yellow',  impact:'RECLAIMED SMA50 &mdash; $146 &#9654;', note:'$145.75 (&minus;4.9%). In zone $138&ndash;150 AND price has reclaimed SMA50 $139.69 for the first time in months. But that average is still FALLING, so the gate holds. Closest ORCL has come.'},
    {ticker:'MRVL', cls:'pi-yellow',  impact:'IN ZONE &mdash; BLOCKED &#9660;',     note:'$206.48 (&minus;4.9%). Inside zone $195&ndash;215 but SMA50 $223.26 falling and price beneath it. Still recovering, not recovered.'},
    {ticker:'LMND', cls:'pi-yellow',  impact:'IN ZONE &mdash; STILL A KNIFE',       note:'$53.14 (+2.9%). Third straight call up inside zone $45&ndash;56 with a falling SMA50 $58.83 above price. Stabilising, but the gate still blocks.'},
    {ticker:'MSFT', cls:'pi-green',   impact:'HOLDING &mdash; $497 &#9650;',        note:'$496.82 (+0.9%). SMA50 $438.43 rising fast &mdash; it has climbed to the zone top $438, so the zone is closing from below. Above zone, no entry.'},
    {ticker:'NVDA', cls:'pi-green',   impact:'FLAT &mdash; $224 &#9654;',           note:'$224.41 (+0.1%). SMA50 $209.15 rising. Held its ground through the pullback. Zone $203&ndash;213 still $11 below.'},
    {ticker:'PLTR', cls:'pi-green',   impact:'FLAT &mdash; $169 &#9654;',           note:'$169.46 (&minus;0.9%). SMA50 $147.38 rising. Barely moved during the pullback. Zone $138&ndash;152 below.'},
    {ticker:'DELL', cls:'pi-yellow',  impact:'+1.6% BUT SMA50 FLAT &#9654;',        note:'$492.20. Only name up besides NOW and LMND, but SMA50 $434.17 has stopped rising. Watch for it to roll over. Zone $418&ndash;448.'},
  ],
  macro_watch: [
    'ANET IS THE FIRST PERFECT-STACK ZONE ENTRY: SMA50 $181.83 > SMA100 $170.62 > SMA150 $158.55 > SMA200 $151.32, in flawless descending order with price above all four and the SMA50 rising. Every prior POTW zone entry has been taken on a compromised stack &mdash; NOW at $103 was explicitly an inverted-stack, early-recovery bet that happened to work (+32%). ANET is what the framework looks like when it gets exactly what it asks for. Stop $170 on a triple confluence (2x ATR, SMA100, just below the zone floor). R/R 4.90:1.',
    'SEVEN IN ZONES, ONE GATE PASS &mdash; THE INVERSE OF AUG 13: Three weeks ago eight names passed the SMA gate and not one was in a zone, so the answer was zero entries. Today seven names sit in zones and only ANET clears the gate. Same discipline, opposite market. The screen is doing its job in both directions: it refused to chase the melt-up and it is refusing to catch six falling knives now.',
    'NOW IS THE RELATIVE-STRENGTH TELL: NOW rose 9.4% while SPY fell 0.9% and QQQ fell 2.0%. That is the exact mirror of the VRT warning from Aug 13, where VRT went flat while its whole sector ran and then broke down. Relative strength in a falling tape is as informative as relative weakness in a rising one. The +32.4% open gain is now protected by a $124 trail.',
    'AVGO BROKE A ZONE FOR THE SECOND TIME: The Aug 13 call up flagged AVGO as the weakest trend among the eight gate passers, on the specific ground that its SMA50 was flat rather than rising. Three weeks later it is 11.7% lower and beneath the zone redrawn at that time. A flat SMA50 is not a mild version of a rising one &mdash; it is the absence of trend, and it deserves the same caution as a falling one.',
    'PANW IS THE NEAR-MISS WORTH WATCHING: Price $328.48 is inside the zone but $20 under a RISING SMA50 $348.24. A rising average with price newly below it is a fresh breakdown, not an established downtrend, and it resolves one way or the other within a couple of weeks. If PANW reclaims $348 it becomes a strong second setup. ZS earnings Thu Sep 3 is the cleanest available read on whether this is sector de-rating or name-specific.',
    'CLEAN CALENDAR REMOVES GAP RISK: No watchlist name reports Sep 3&ndash;9, which matters because the MSFT lesson from Jul 30 was that a falling SMA50 cannot anticipate an earnings surprise. With no print inside the ANET holding window, the entry carries trend risk only. Labor Day Mon Sep 7 shortens next week to four sessions.',
    'ORCL HAS RECLAIMED ITS SMA50 &mdash; THE PRECONDITION IS MET: For the first time in months ORCL price ($145.75) sits above its SMA50 ($139.69), and it is inside the redrawn $138&ndash;150 zone. The average is still falling, so the gate holds and there is no entry. But the sequence that repairs a broken trend is reclaim first, then flatten, then rise. ORCL has completed step one. Watch for the SMA50 to flatten.',
  ],
  weekly: {
    week: 'Aug 13 &ndash; Sep 2, 2026 (3-week span)',
    updated: 'Wed Sep 2 close (Live Robinhood data)',
    headline: 'Pullback Reopens The Board &mdash; ANET Falls Into Zone With A Perfect Stack &mdash; NOW +32% &mdash; AVGO Breaks Down Again',
    week_chg: [
      {name:'SPY',       open:'$772.49', close:'$765.16', chg:'&minus;0.9% &mdash; off ATH',        dir:'down'},
      {name:'QQQ',       open:'$723.70', close:'$709.24', chg:'&minus;2.0% &mdash; tech leads',      dir:'down'},
      {name:'ANET',      open:'$210.50', close:'$186.10', chg:'&minus;11.6% &mdash; into zone',      dir:'down'},
      {name:'NOW',       open:'$124.94', close:'$136.72', chg:'+9.4% &mdash; POTW +32% total',       dir:'up'},
      {name:'PANW',      open:'$387.01', close:'$328.48', chg:'&minus;15.1% &mdash; biggest drop',   dir:'down'},
    ],
    potw: {
      ticker:'NOW', type:'Manage the Winner &mdash; Trail Raised',
      entry:'Zone floor $103.24 (Jul 19&ndash;25)', exit:'Open &mdash; $136.72 Sep 2',
      high:'$138.40 intraday Sep 1', pnl:'+32.4% and holding',
      verdict:'WINNER &mdash; +32% OPEN', verdictCls:'wr-win',
      note:'The Aug 13 call was to raise the trail to $113 and do nothing else. NOW then added 9.4% while SPY fell 0.9% and QQQ fell 2.0% &mdash; the strongest relative-strength signal on the board. The position is now +32.4% from the $103.24 zone-floor entry with the SMA50 at $115.07 and rising steeply. Trail moves again, $113 to $124 (2x ATR of $6.09), locking in +20.1%. Remaining R/R to $175 is 3.0:1. Still no adds: the entry was $103 and that window closed long ago.',
    },
    missed: {
      setup:'Nothing was missed &mdash; the Aug 13 answer was zero entries because every gate pass sat above its zone. The pullback has now brought seven names back into zones.',
      trade:'ANET is the one that arrived with its stack intact. PANW is the near-miss, inside its zone but $20 below a rising SMA50.',
      result:'Waiting three weeks with no new position produced a cleaner setup than anything available during the melt-up. Patience was the trade.',
    },
    lessons: [
      {tag:'PERFECT STACK', cls:'lsn-rule',  text:'ANET is the first zone entry with a fully bullish stack (50 &gt; 100 &gt; 150 &gt; 200, price above all four, SMA50 rising). Every previous POTW zone entry compromised somewhere &mdash; NOW was an explicitly inverted-stack recovery bet. When the screen finally delivers exactly what it asks for, that is the one to size properly.'},
      {tag:'FLAT = NO TREND', cls:'lsn-macro', text:'AVGO was flagged Aug 13 as the weakest gate pass because its SMA50 was flat, not rising. It is now 11.7% lower and through its zone floor for the second time this cycle. A flat SMA50 is the absence of trend, not a weaker version of one, and should be treated closer to falling than rising.'},
      {tag:'RELATIVE STRENGTH', cls:'lsn-next',  text:'NOW rose 9.4% into a falling tape. That is the same signal as the VRT warning inverted: VRT went flat while its sector ran and then broke down. Relative performance against the tape carries information in both directions and is worth checking on every call up.'},
      {tag:'PATIENCE',      cls:'lsn-rule',  text:'Zero entries on Aug 13 felt like inaction. Three weeks later the pullback delivered a 4.90:1 setup with a perfect stack and no earnings risk in the window. Not trading the melt-up was what made this entry available.'},
    ],
    eow: [
      {ticker:'ANET', price:'$186.10', sCls:'eow-green',  status:'ZONE + GATE &#10003;',        note:'Perfect stack. R/R 4.90:1. Stop $170'},
      {ticker:'NOW',  price:'$136.72', sCls:'eow-green',  status:'WINNER +32% &#9650;',          note:'Trail to $124. Target $175'},
      {ticker:'MSFT', price:'$496.82', sCls:'eow-green',  status:'HOLDING &#9650;',              note:'SMA50 $438 rising to zone top'},
      {ticker:'NVDA', price:'$224.41', sCls:'eow-green',  status:'FLAT &#9654;',                 note:'SMA50 $209 rising. Held up'},
      {ticker:'PLTR', price:'$169.46', sCls:'eow-green',  status:'FLAT &#9654;',                 note:'SMA50 $147 rising. Barely moved'},
      {ticker:'DELL', price:'$492.20', sCls:'eow-yellow', status:'+1.6% SMA50 FLAT &#9654;',     note:'Watch for the 50 to roll over'},
      {ticker:'ORCL', price:'$145.75', sCls:'eow-yellow', status:'RECLAIMED SMA50 &#9654;',      note:'In zone. SMA50 still falling'},
      {ticker:'LMND', price:'$53.14',  sCls:'eow-yellow', status:'IN ZONE, KNIFE &#9888;',       note:'3rd call up in zone. SMA50 $59'},
      {ticker:'MRVL', price:'$206.48', sCls:'eow-yellow', status:'IN ZONE, BLOCKED &#9660;',     note:'SMA50 $223 falling above price'},
      {ticker:'AMD',  price:'$457.06', sCls:'eow-yellow', status:'IN ZONE, BLOCKED &#9660;',     note:'SMA50 $502 falling. Needs reclaim'},
      {ticker:'PANW', price:'$328.48', sCls:'eow-yellow', status:'&minus;15% NEAR-MISS &#9660;', note:'In zone, $20 under RISING SMA50'},
      {ticker:'VRT',  price:'$256.70', sCls:'eow-red',    status:'STILL BROKEN &#9888;',         note:'Reached zone. SMA50 falling'},
      {ticker:'AVGO', price:'$367.24', sCls:'eow-red',    status:'BROKE ZONE &#9888;',           note:'2nd zone break. SMA50 $385 falling'},
    ],
  },
};"""

new_src,n = re.subn(r'const MARKET_PULSE = \{.*?\n\};', lambda m: NEW, src, flags=re.DOTALL)
if n!=1:
    print(f'ERROR: {n} replacements'); sys.exit(1)
open(FILE,'w').write(new_src)
print(f'OK - MARKET_PULSE replaced ({n})')
os.remove(FILE+'.bak')
