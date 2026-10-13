#!/usr/bin/env python3
"""MARKET_PULSE -> Oct 12 settled close (Oct 13 intraday noted). ANET exit; NOW trail raise."""
import re, sys, os, shutil
FILE='templates/index.html'; shutil.copy(FILE,FILE+'.bak'); src=open(FILE).read()

NEW = """const MARKET_PULSE = {
  date: 'October 13, 2026',
  updated: 'Call Up &mdash; Oct 12 Settled Close (Oct 13 intraday noted; market open) &mdash; First refresh since Sep 5',
  headline: 'ANET POTW Peaked +16.5%, EXIT AT +6.8% &mdash; NOW +35.9% TRAIL TO $129 &mdash; Index Breadth Collapsing: QQQ +3.8% While IWM &minus;6.1% &mdash; Zero New Zone Entries',
  sentiment: 'NARROW TAPE &mdash; BOOK ANET &mdash; NO NEW ENTRIES',
  sentimentCls: 'mkt-caution',
  indices: [
    {name:'SPY',        val:'$778.10', chg:'+1.0% since Sep 4',                         dir:'up'},
    {name:'QQQ',        val:'$746.04', chg:'+3.8% &mdash; mega-cap tech carrying it',     dir:'up'},
    {name:'IWM',        val:'$277.90', chg:'&minus;6.1% &mdash; small caps BREAKING DOWN', dir:'down'},
    {name:'DIA',        val:'$517.91', chg:'&minus;3.0% &mdash; Dow rolling over',         dir:'down'},
    {name:'ANET',       val:'$210.88', chg:'POTW +13.3% at close; $198.67 intraday',      dir:'up'},
    {name:'AMD',        val:'$594.24', chg:'+24.5% &mdash; biggest gain, was BLOCKED',     dir:'up'},
    {name:'PANW',       val:'$403.83', chg:'+21.2% &mdash; reclaimed SMA50 and ran',       dir:'up'},
    {name:'LMND',       val:'$45.15',  chg:'&minus;15.5% &mdash; at the zone floor',       dir:'down'},
  ],
  events: [
    {tag:'POTW',     tagCls:'evt-watch', headline:'ANET &mdash; PEAKED +16.5%, NOW +6.8% AND SITTING ON ITS SMA50 &mdash; EXIT', body:'The Sep 3 Play of the Week entered ANET at $186.10. It ran to a closing high of $216.74 on Oct 9 (+16.5%) and an intraday high of $217.41, then faded: $210.88 at the Oct 12 close (+13.3%) and $198.67 intraday on Oct 13 (+6.8%). The stop at $178 was never threatened. THE DECISION POINT IS NOW: price is sitting on a rising SMA50 of $198.47 &mdash; exactly the line flagged on Sep 5 as the level that breaks the gate and warns before the stop. The RECOMMENDATION IS TO EXIT and book +6.8%, for three reasons that compound. One, the holding period is six weeks against a stated 2&ndash;4 day swing horizon, so the original thesis expired long ago. Two, the position has given back 59% of its peak gain. Three, a 2x ATR trail from the Oct 9 peak would sit at roughly $203 and has already been violated. The SMA stack is still perfectly ordered (SMA50 $198.47 &gt; SMA100 $182.53 &gt; SMA150 $170.50 &gt; SMA200 $161.47) which is the one argument for holding &mdash; but a weekly swing held six weeks is no longer the trade that was entered.'},
    {tag:'PROCESS',  tagCls:'evt-geo',   headline:'PROCESS GAP &mdash; The Trail Sat At $178 For Five Weeks With No Call Up', body:'Worth stating plainly rather than burying. The ANET stop was set to $178 on Sep 5 and never moved, because no call up happened for five weeks. ANET meanwhile ran to $216.74. A standing 2x ATR trailing rule, applied without needing a session, would have ratcheted the stop up behind the advance and exited near $203 for roughly +9% instead of the +6.8% now available. The gap between +9% and +6.8% is small; the principle is not. Every trail in this framework currently depends on a human-initiated call up to move it. That is a process dependency, not a strategy, and it is the single clearest improvement available: define the trail as a rule (2x ATR from the highest close since entry) rather than as a number set at each session.'},
    {tag:'BREADTH',  tagCls:'evt-macro', headline:'BREADTH IS COLLAPSING &mdash; QQQ +3.8% While IWM &minus;6.1% And DIA &minus;3.0%', body:'The index spread over five weeks is the most important macro fact on this board. QQQ rose 3.8% while IWM fell 6.1% and DIA fell 3.0% &mdash; a 10-point gap between mega-cap tech and small caps. SPY managed +1.0% only because its largest weights are doing all the work. A tape this narrow means the AI complex is absorbing capital from everything else rather than riding a broad expansion. It is a late-cycle signature: it can persist for months, and it also means any wobble in the handful of leaders has nothing beneath it to cushion the fall. Position sizing matters more in a narrow tape than in a broad one.'},
    {tag:'GATE',     tagCls:'evt-watch', headline:'THE GATE SCORECARD CUTS BOTH WAYS &mdash; Three Big Misses, Three Big Saves', body:'Over these five weeks the SMA gate blocked AMD (+24.5%), PANW (+21.2%) and MRVL (+19.0%), all of which reclaimed their falling SMA50s and ran hard. It also blocked ORCL (&minus;13.5% through its Sep 10 earnings), VRT (&minus;14.7%) and LMND (&minus;15.5%). That is three large winners missed and three large losers avoided in the same window, which is close to the cleanest natural experiment the framework has produced. The arithmetic roughly cancels; the asymmetry is in the distribution, because the losses avoided were in names with broken structure where a position could keep bleeding, while the winners missed were in names that had to first repair a falling average. The gate is doing what it was designed to do. It is not free.'},
    {tag:'ORCL',     tagCls:'evt-geo',   headline:'ORCL &minus;13.5% Through Earnings &mdash; The Stand-Aside Call Was Right', body:'The Sep 5 note said to stand aside through the Sep 10 print rather than enter on a technical setup that had only just qualified. ORCL reported and fell from $158.77 to $137.39, down 13.5%. It is now back inside the $138&ndash;150 zone with price at $139.20 intraday. The structural detail that matters: the SMA50 $145.90 is now RISING while price sits $6.70 BENEATH it. That is the inverse of the usual broken-trend setup and is genuinely interesting &mdash; a rising average with price below it after an earnings shock. If ORCL reclaims $145.90 it becomes a real setup with the zone and the gate aligned for the first time. Not yet.'},
    {tag:'EARN',     tagCls:'evt-macro', headline:'Bank Week Underway &mdash; TSM Thu Oct 15 Is The AI Read &mdash; No Watchlist Names Report', body:'Banks opened Q3 season Tuesday: GS crushed it at $17.01 against $13.05 expected, C beat at $2.85, WFC beat at $1.87, while JPM missed slightly at $5.75 against $5.94. UNH and JNJ both beat. MS and BAC report Wed Oct 14, SCHW Thu. THE ONE THAT MATTERS FOR THIS BOARD: TSM reports Thursday Oct 15 (est. EPS $4.45), with ASML Wednesday Oct 14 (est. $12.47). Those two are the upstream bellwethers for every AI name on the watchlist &mdash; TSMC fabricates the silicon and ASML sells the lithography. No watchlist name reports Oct 13&ndash;19, so both prints are information rather than position risk.'},
  ],
  portfolio: [
    {ticker:'ANET', cls:'pi-yellow',  impact:'EXIT &mdash; +6.8% FROM PEAK +16.5%', note:'$210.88 Oct 12 close, $198.67 intraday Oct 13. Peaked $216.74 Oct 9 (+16.5%). Now sitting ON the rising SMA50 $198.47 &mdash; the pre-committed warning line. Held 6 weeks vs a 2&ndash;4 day horizon; gave back 59% of peak gain. BOOK +6.8%.'},
    {ticker:'NOW',  cls:'pi-green',   impact:'WINNER +35.9% &mdash; TRAIL TO $129', note:'$140.32 Oct 12 close ($142.76 intraday), +35.9% from the $103.24 entry. SMA50 $132.81 rising. Stack has nearly repaired: 50 $132.81 &gt; 100 $119.21 &gt; 200 $115.27 &gt; 150 $112.45. RAISE TRAIL $124 &rarr; $129, locking +25.0%. R/R 3.06:1.'},
    {ticker:'AMD',  cls:'pi-green',   impact:'+24.5% &mdash; BIGGEST GAIN, WAS BLOCKED', note:'$594.24. Reclaimed its falling SMA50 and ran 24.5% &mdash; the largest winner the gate cost this cycle. SMA50 $531.28 now rising with price above. Far above the old $440&ndash;470 zone.'},
    {ticker:'PANW', cls:'pi-green',   impact:'+21.2% &mdash; NEAR-MISS RESOLVED UP',  note:'$403.83. The Sep 5 near-miss (in zone, $16 under a rising SMA50) resolved upward exactly as the better case described &mdash; it reclaimed $349 and ran 21.2%. SMA50 $372.29 rising.'},
    {ticker:'MRVL', cls:'pi-green',   impact:'+19.0% &mdash; STEP 2 AND 3 COMPLETED', note:'$265.86. Had reclaimed a falling SMA50 on Sep 5 (step 1 of 3). The average then flattened and turned up, completing the repair, and MRVL ran 19.0%. SMA50 $238.06 rising, SMA100 $238.76 &mdash; tight confluence.'},
    {ticker:'PLTR', cls:'pi-green',   impact:'+19.9% &mdash; EXTENSION RESOLVED UP',  note:'$209.00. The extension that was closing through time resolved upward instead. SMA50 $178.70 rising fast. Far above the old $138&ndash;152 zone.'},
    {ticker:'DELL', cls:'pi-green',   impact:'+10.1% &mdash; $577 &#9650;',           note:'$576.76. SMA50 $509.08 rising strongly. The Sep 3 flat-SMA caution is now two call ups resolved in favour of holding. Far above the old $418&ndash;448 zone.'},
    {ticker:'MSFT', cls:'pi-green',   impact:'+8.3% &mdash; $541 &#9650;',            note:'$541.15. SMA50 $501.98 rising. The old $410&ndash;438 zone is now $64 below the SMA50 and entirely obsolete &mdash; redrawn to $502&ndash;525.'},
    {ticker:'NVDA', cls:'pi-yellow',  impact:'&minus;1.8% &mdash; AT ITS SMA50 &#9654;', note:'$226.32 ($224.78 intraday). The only large AI name to go nowhere while AMD ran 24.5% and MRVL 19.0%. SMA50 $222.59 rising but price is only $2 above it &mdash; watch this.'},
    {ticker:'ORCL', cls:'pi-yellow',  impact:'&minus;13.5% ON EARNINGS &mdash; IN ZONE', note:'$137.39 ($139.20 intraday). Fell 13.5% through the Sep 10 print &mdash; the stand-aside call was right. Back in zone $138&ndash;150. SMA50 $145.90 is RISING with price BELOW it; a reclaim makes this a real setup.'},
    {ticker:'VRT',  cls:'pi-red',     impact:'&minus;14.7% &mdash; NEVER RECLAIMED &#9888;', note:'$239.36. Was $1.94 from its SMA50 on Sep 5; instead of reclaiming it fell 14.7%. SMA50 $259.56 has gone flat with price $20 below. Not anticipating that reclaim was correct. Still broken.'},
    {ticker:'AVGO', cls:'pi-red',     impact:'&minus;0.9% &mdash; FOURTH CALL UP BROKEN &#9888;', note:'$354.73. SMA50 $371.18 still falling, price $17 below. Fourth consecutive call up as a broken structure and it has now gone nowhere for five weeks while its sector ran. No entry.'},
    {ticker:'LMND', cls:'pi-red',     impact:'&minus;15.5% &mdash; AT THE ZONE FLOOR &#9888;', note:'$45.15, sitting exactly on the $45 zone floor after five call ups inside the zone. SMA50 $49.89 still falling. This is now the ORCL pattern &mdash; a zone about to be broken rather than defended. Zone redrawn down.'},
  ],
  macro_watch: [
    'ANET VERDICT - A WINNER, EXITED LATE: Entered $186.10, peaked $216.74 (+16.5%) on Oct 9, now $198.67 (+6.8%) and sitting on its rising SMA50. The call was right - a perfect bullish stack in a zone with R/R 4.90:1 produced a 16.5% advance and never came close to the $178 stop. The exit is what went wrong, and it went wrong for a structural reason rather than an analytical one: the trail depended on a call up to move it, and five weeks passed without one.',
    'THE FIX IS A RULE, NOT A NUMBER: Define the trail as 2x ATR below the highest CLOSE since entry, recomputed continuously, rather than a figure set at each session. Applied to ANET that rule would have ratcheted from $178 up behind the advance and exited near $203 (+9%) when price broke down on Oct 12-13. It removes the dependency on session timing entirely. This is the most valuable change available to the framework right now.',
    'BREADTH IS THE REAL STORY: QQQ +3.8%, IWM -6.1%, DIA -3.0% over five weeks. A 10-point gap between mega-cap tech and small caps means the AI complex is absorbing capital from the rest of the market rather than leading a broad advance. SPY is only +1.0% and that is entirely its top weights. Narrow tapes can persist for months - and they leave nothing beneath the leaders if those wobble. Size accordingly.',
    'THE GATE SCORECARD, STATED HONESTLY: Blocked AMD +24.5%, PANW +21.2%, MRVL +19.0% - all three reclaimed falling SMA50s and ran. Also blocked ORCL -13.5% (earnings), VRT -14.7%, LMND -15.5%. Three large winners missed, three large losers avoided, in the same five weeks. The count cancels. The asymmetry is distributional: avoided losses were in broken structures that keep bleeding, missed winners required a falling average to repair first. The gate works as designed and it is not free.',
    'ZERO DOUBLE-GATE PASSES FOR THE THIRD STRAIGHT CALL UP: Nine names now pass the SMA gate and all nine are above their zones. Only ORCL and LMND are in zones and both have price beneath their SMA50. The pattern across three sessions - Aug 13 (8 pass, 0 in zone), Sep 3 (7 in zone, 1 pass), Oct 13 (9 pass, 0 in zone) - says the zones cannot keep pace with a trending tape. All thirteen have been recalibrated again to the SMA50/SMA100 confluence.',
    'ORCL IS THE SETUP TO WATCH: Down 13.5% through earnings and back inside the $138-150 zone, with SMA50 $145.90 RISING while price sits $6.70 beneath it. That specific configuration - a rising average with price below after an earnings shock - is the inverse of the usual broken trend and resolves faster. A reclaim of $145.90 aligns the zone and the gate for the first time since ORCL broke down in June. Watch, do not anticipate; VRT was $1.94 from a reclaim on Sep 5 and fell 14.7% instead.',
    'TSM THU OCT 15 IS THE UPSTREAM READ: TSMC (est. EPS $4.45) fabricates the silicon for every AI name here, and ASML (est. $12.47, Wed Oct 14) sells the lithography that makes it possible. Neither is a position, so both are pure information. A strong TSM print with capex guidance up validates the AMD/MRVL/AVGO complex; a miss would hit the narrow leadership that is currently holding the indices up. Bank week is already in: GS beat huge, JPM missed slightly.',
  ],
  weekly: {
    week: 'Sep 4 &ndash; Oct 12, 2026 (5-week span)',
    updated: 'Mon Oct 12 settled close; Oct 13 intraday noted',
    headline: 'ANET POTW Peaked +16.5% And Faded To +6.8% &mdash; NOW +35.9% &mdash; Gate Missed AMD +24%, PANW +21%, MRVL +19% And Avoided ORCL, VRT, LMND &mdash; Breadth Collapsing',
    week_chg: [
      {name:'QQQ',       open:'$719.06', close:'$746.04', chg:'+3.8% &mdash; mega-cap only',      dir:'up'},
      {name:'IWM',       open:'$295.95', close:'$277.90', chg:'&minus;6.1% &mdash; breaking down', dir:'down'},
      {name:'ANET',      open:'$193.77', close:'$210.88', chg:'+8.8% &mdash; peaked $216.74',      dir:'up'},
      {name:'AMD',       open:'$477.45', close:'$594.24', chg:'+24.5% &mdash; was blocked',        dir:'up'},
      {name:'LMND',      open:'$53.40',  close:'$45.15',  chg:'&minus;15.5% &mdash; at zone floor', dir:'down'},
    ],
    potw: {
      ticker:'ANET', type:'Zone Entry &mdash; CLOSING AT +6.8%',
      entry:'$186.10 (Sep 3, zone $172&ndash;190)', exit:'$198.67 intraday Oct 13 &mdash; exit recommended',
      high:'$217.41 intraday / $216.74 close, Oct 9', pnl:'+6.8% (peaked +16.5%)',
      verdict:'WINNER &mdash; EXITED LATE', verdictCls:'wr-win',
      note:'The analysis was right and the exit was late. Entered at $186.10 on a perfect bullish stack inside the zone with R/R 4.90:1; ANET advanced to a $216.74 close on Oct 9 for +16.5% and never approached the $178 stop. It has since faded to $198.67, sitting exactly on the rising SMA50 $198.47 that was flagged on Sep 5 as the gate-break line. Exit and book +6.8%. THE LESSON IS PROCESS, NOT ANALYSIS: the stop sat at $178 for five weeks because moving it required a call up that did not happen. A standing rule &mdash; 2x ATR below the highest close since entry &mdash; would have exited near $203 for +9%. Define the trail as a rule, not a number.',
    },
    missed: {
      setup:'AMD +24.5%, PANW +21.2% and MRVL +19.0% all reclaimed falling SMA50s and ran. The gate blocked all three at the Sep 5 call up.',
      trade:'In the same window the gate blocked ORCL (&minus;13.5% through earnings), VRT (&minus;14.7%) and LMND (&minus;15.5%).',
      result:'Three large winners missed, three large losers avoided, same five weeks. Count cancels; the asymmetry is that avoided losses were in broken structures while missed winners first had to repair a falling average.',
    },
    lessons: [
      {tag:'TRAIL AS RULE', cls:'lsn-rule',  text:'ANET peaked +16.5% and is being exited at +6.8% because the stop sat at $178 for five weeks with no call up to raise it. Define the trail as 2x ATR below the highest close since entry, recomputed continuously. That removes the dependency on session timing and would have banked roughly +9%.'},
      {tag:'BREADTH',       cls:'lsn-macro', text:'QQQ +3.8% against IWM &minus;6.1% over five weeks is a 10-point dispersion. The AI complex is absorbing capital from the rest of the market, not leading a broad advance. Narrow leadership leaves nothing beneath it if the leaders wobble.'},
      {tag:'GATE COST',     cls:'lsn-next',  text:'Blocked AMD +24.5%, PANW +21.2%, MRVL +19.0% and also ORCL &minus;13.5%, VRT &minus;14.7%, LMND &minus;15.5%. Near-perfect natural experiment: the count cancels. Keep the gate, but note that a name reclaiming a falling SMA50 is a recognisable and recurring pattern worth a watch-list of its own.'},
      {tag:'NOT ANTICIPATING', cls:'lsn-rule', text:'VRT sat $1.94 beneath its SMA50 on Sep 5 and the note said watch, do not anticipate. It then fell 14.7% instead of reclaiming. That restraint is now worth applying verbatim to ORCL, which is $6.70 under a rising SMA50.'},
    ],
    eow: [
      {ticker:'ANET', price:'$210.88', sCls:'eow-yellow', status:'EXIT +6.8% &#9654;',           note:'Peaked +16.5%. On SMA50 $198.47'},
      {ticker:'NOW',  price:'$140.32', sCls:'eow-green',  status:'WINNER +35.9% &#9650;',         note:'Trail $124 &rarr; $129. Target $175'},
      {ticker:'AMD',  price:'$594.24', sCls:'eow-green',  status:'+24.5% WAS BLOCKED &#9650;',    note:'Reclaimed SMA50 and ran'},
      {ticker:'PANW', price:'$403.83', sCls:'eow-green',  status:'+21.2% RESOLVED UP &#9650;',    note:'Near-miss reclaimed $349'},
      {ticker:'PLTR', price:'$209.00', sCls:'eow-green',  status:'+19.9% &#9650;',                note:'SMA50 $178.70 rising fast'},
      {ticker:'MRVL', price:'$265.86', sCls:'eow-green',  status:'+19.0% REPAIRED &#9650;',       note:'Completed steps 2 and 3'},
      {ticker:'DELL', price:'$576.76', sCls:'eow-green',  status:'+10.1% &#9650;',                note:'SMA50 $509 rising strongly'},
      {ticker:'MSFT', price:'$541.15', sCls:'eow-green',  status:'+8.3% &#9650;',                 note:'SMA50 $502. Old zone obsolete'},
      {ticker:'NVDA', price:'$226.32', sCls:'eow-yellow', status:'&minus;1.8% AT SMA50 &#9654;',  note:'Only $2 above $222.59. Watch'},
      {ticker:'ORCL', price:'$137.39', sCls:'eow-yellow', status:'&minus;13.5% IN ZONE &#9660;',  note:'SMA50 $145.90 RISING, px below'},
      {ticker:'VRT',  price:'$239.36', sCls:'eow-red',    status:'&minus;14.7% NEVER RECLAIMED &#9888;', note:'Was $1.94 away. Fell instead'},
      {ticker:'AVGO', price:'$354.73', sCls:'eow-red',    status:'4TH CALL UP BROKEN &#9888;',    note:'SMA50 $371 falling. Went nowhere'},
      {ticker:'LMND', price:'$45.15',  sCls:'eow-red',    status:'&minus;15.5% AT FLOOR &#9888;', note:'5th call up in zone. ORCL pattern'},
    ],
  },
};"""

new_src,n = re.subn(r'const MARKET_PULSE = \{.*?\n\};', lambda m: NEW, src, flags=re.DOTALL)
if n!=1: print(f'ERROR: {n}'); sys.exit(1)
open(FILE,'w').write(new_src); print(f'OK - MARKET_PULSE replaced ({n})'); os.remove(FILE+'.bak')
