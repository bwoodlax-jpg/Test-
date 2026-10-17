#!/usr/bin/env python3
"""MARKET_PULSE -> Oct 16 close. AI unwind; ANET exit validated; PLTR double-gate pass."""
import re, sys, os, shutil
FILE='templates/index.html'; shutil.copy(FILE,FILE+'.bak'); src=open(FILE).read()

NEW = """const MARKET_PULSE = {
  date: 'October 17, 2026',
  updated: 'Call Up &mdash; Oct 16 Session Close (Fri; Oct 15 is the last SETTLED close)',
  headline: 'Sharp AI Unwind &mdash; QQQ &minus;4.9% In Four Sessions &mdash; ANET EXIT VALIDATED (now below its stop) &mdash; NOW The Only Name Up &mdash; PLTR Is The One Double-Gate Pass',
  sentiment: 'AI UNWIND &mdash; EXIT VALIDATED &mdash; ONE SETUP',
  sentimentCls: 'mkt-caution',
  indices: [
    {name:'SPY',        val:'$763.30', chg:'&minus;1.9% since Oct 12',                      dir:'down'},
    {name:'QQQ',        val:'$709.86', chg:'&minus;4.9% &mdash; AI complex unwinding',        dir:'down'},
    {name:'IWM',        val:'$270.48', chg:'&minus;2.7% &mdash; small caps still bleeding',   dir:'down'},
    {name:'DIA',        val:'$519.09', chg:'+0.2% &mdash; Dow the only index up',             dir:'up'},
    {name:'NOW',        val:'$141.95', chg:'+1.2% &mdash; ONLY watchlist name up',            dir:'up'},
    {name:'PLTR',       val:'$186.03', chg:'&minus;11.0% &mdash; INTO ZONE, GATE HOLDS',       dir:'down'},
    {name:'ANET',       val:'$177.03', chg:'&minus;16.1% &mdash; BELOW the $178 stop',         dir:'down'},
    {name:'DELL',       val:'$451.67', chg:'&minus;21.7% &mdash; worst on the board',          dir:'down'},
  ],
  events: [
    {tag:'VALIDATED', tagCls:'evt-watch', headline:'ANET EXIT WAS RIGHT &mdash; $198.67 Then, $177.03 Now, And Below Its Stop', body:'The Oct 13 call up recommended closing ANET at $198.67 for +6.8%, on the grounds that price was sitting on its rising SMA50, the position had given back 59% of a +16.5% peak, and six weeks was far outside the 2&ndash;4 day horizon. Four sessions later ANET is $177.03. Holding would now show &minus;4.9% against the $186.10 entry, and price has broken THROUGH the $178 stop &mdash; so the position would have been closed anyway, just 11.7 points lower. The exit converted a trade that is now a loss into a booked +6.8% gain. Two things made that call available: the SMA50 was named in advance on Sep 5 as the line that mattered, and the holding-period rule flagged the trade as stale before the price did.'},
    {tag:'SETUP',    tagCls:'evt-watch', headline:'PLTR $186.03 &mdash; The ONLY Double-Gate Pass On The Board', body:'Palantir fell 11.0% from $209.00 and landed inside its $179&ndash;195 zone while holding above a RISING SMA50 of $182.57 &mdash; the only name of thirteen to be in a zone and pass the trend gate simultaneously. Four others are in zones (NVDA, AMD, LMND and, marginally, nothing else) and every one of them has price beneath its SMA50. The stack is near-perfect: SMA50 $182.57 &gt; SMA100 $157.19 &gt; SMA200 $152.65 &gt; SMA150 $152.25, with the 150 and 200 inverted by only $0.40 and price above all four. ATR(14) $7.75 puts a 2x ATR stop at $170.53, rounded to $170, which sits below the $179 zone floor. R/R to the $260 target: $73.97 up / $16.03 down = 4.61:1. THE CAVEAT IS THE TAPE, NOT THE SETUP &mdash; see the sizing note below.'},
    {tag:'RISK',     tagCls:'evt-geo',   headline:'THE TAPE IS THE RISK &mdash; Entering A Setup Mid-Unwind Needs Half Size And Volume', body:'PLTR passes both gates mechanically, and mechanical passes during a sector-wide unwind are exactly where this framework has previously been hurt. QQQ is down 4.9% in four sessions; DELL &minus;21.7%, ANET &minus;16.1%, PANW &minus;15.3%, MRVL &minus;14.3%. PLTR itself fell 11.0% to get here and sits only $3.46 above its SMA50 &mdash; less than half an ATR of cushion. THE CONDITIONS, therefore: Rule 4 volume confirmation is mandatory, not advisory (entry candle at or above 1.5x the 20-day average on a green close); position at 0.5% of bankroll rather than 1%; and a close beneath $182.57 kills the thesis well before the $170 stop. If the unwind continues, there is no entry here at all. A valid setup and a hostile tape can coexist, and the tape decides the size.'},
    {tag:'POTW',     tagCls:'evt-watch', headline:'NOW $141.95 &mdash; The ONLY Watchlist Name Up &mdash; New Trail Rule Ratchets To $135', body:'NOW rose 1.2% while every other name on the board fell, after touching $148.57 on Oct 15. It is +37.5% from the $103.24 entry and SMA50 $134.85 continues rising. THE NEW STANDING RULE IS DOING ITS JOB: adopted on Oct 13 as 2x ATR below the highest CLOSE since entry, it now computes from the $148.57 Oct 15 high with ATR $6.59, giving a trail of <strong>$135.40</strong> rather than the $129 set four days ago. That is a $6 ratchet produced by the rule itself rather than by a judgement call &mdash; precisely the dependency ANET exposed. The trail now sits $0.55 above the SMA50, locking +31.2%, with R/R to $175 at 5.05:1.'},
    {tag:'NVDA',     tagCls:'evt-geo',   headline:'NVDA Broke Its SMA50 &mdash; The Oct 13 Relative-Weakness Flag Played Out', body:'NVDA was flagged on Oct 13 for relative weakness: down 1.8% over five weeks while AMD ran 24.5% and MRVL 19.0%, sitting only $2 above a rising SMA50 at $222.59, with the note that the $222.59 test was the thing to watch. It has since fallen 5.4% to $214.14 and is now $9 BENEATH that average. It is also inside its redrawn $214&ndash;223 zone and therefore blocked &mdash; in zone, below the gate. That is the third time this cycle relative weakness during or after a sector move has preceded a breakdown (VRT, AVGO, now NVDA), and it is becoming the most reliable early signal on this board.'},
    {tag:'EARN',     tagCls:'evt-macro', headline:'TSM Reported And The Sector Sold Off Anyway &mdash; Big Week Ahead, No Watchlist Names', body:'TSM reported Thursday Oct 15 and the AI complex fell regardless; TSM itself went from $422.25 to $412.51 over the following session. An upstream print validating demand did not stop a de-rating, which says this unwind is about multiples and positioning rather than end-demand. NO WATCHLIST NAME REPORTS Oct 19&ndash;23, but the read-throughs are heavy: NFLX Tue Oct 20, then META, TSLA, IBM, TXN, LRCX and SAP all Wed Oct 21, with WDC Thu Oct 22. TXN and LRCX are the semis reads; META is the mega-cap AI capex read. Any PLTR entry sits inside that cluster, which is another argument for half size.'},
  ],
  portfolio: [
    {ticker:'NOW',  cls:'pi-green',   impact:'ONLY NAME UP &mdash; +37.5% &#9650;', note:'$141.95 (+1.2%), the only watchlist name higher in the unwind. Touched $148.57 Oct 15. SMA50 $134.85 rising. NEW RULE ratchets the trail $129 &rarr; $135.40 automatically (2x ATR below the highest close), locking +31.2%. R/R 5.05:1.'},
    {ticker:'PLTR', cls:'pi-green',   impact:'IN ZONE + GATE PASS &#10003;',        note:'$186.03 (&minus;11.0%). The ONLY double-gate pass: in zone $179&ndash;195 with a RISING SMA50 $182.57 above which it closed. Stack near-perfect. Stop $170 (2x ATR), R/R 4.61:1. BUT only $3.46 above the gate &mdash; half size, volume confirmation mandatory.'},
    {ticker:'MSFT', cls:'pi-green',   impact:'&minus;2.3% &mdash; HELD UP &#9654;',  note:'$528.95. Second-best relative performance. SMA50 $505.53 still rising, price $23 above. Just above the redrawn $502&ndash;525 zone &mdash; a further 1% decline puts MSFT in zone with the gate intact. The closest thing to a second setup.'},
    {ticker:'LMND', cls:'pi-yellow',  impact:'&minus;2.1% &mdash; IN ZONE, BLOCKED',  note:'$44.19. Sixth consecutive call up in a zone with price beneath a falling SMA50 ($49.24). Fell less than the AI names only because it had already broken down. Zone $36&ndash;45. Still no entry; the answer has not changed in six sessions.'},
    {ticker:'NVDA', cls:'pi-red',     impact:'BROKE SMA50 &mdash; $214 &#9888;',      note:'$214.14 (&minus;5.4%). The Oct 13 relative-weakness flag played out: it has broken BELOW the $223.08 SMA50 it was sitting $2 above. In zone $214&ndash;223 but beneath the gate &mdash; blocked. Third time relative weakness preceded a breakdown.'},
    {ticker:'ORCL', cls:'pi-red',     impact:'&minus;6.7% &mdash; WATCH DEAD &#9888;', note:'$128.22. The Oct 13 reclaim-watch is dead: SMA50 $145.12 has turned back DOWN and price is now $17 beneath it, below the $138&ndash;150 zone entirely. Not anticipating the reclaim was right for the second time running.'},
    {ticker:'AVGO', cls:'pi-red',     impact:'&minus;7.3% &mdash; 5TH CALL UP BROKEN &#9888;', note:'$328.81. SMA50 $365.73 falling, price $37 below, now beneath the $330&ndash;350 zone redrawn four days ago. Fifth consecutive call up as a broken structure. No entry.'},
    {ticker:'AMD',  cls:'pi-yellow',  impact:'&minus;11.0% &mdash; IN ZONE, BLOCKED', note:'$528.76. Fell into the $522&ndash;550 zone but price is now $8 BENEATH the rising SMA50 $537.14 &mdash; in zone, below the gate. Gave back nearly half of the +24.5% run the gate had blocked. Needs the reclaim.'},
    {ticker:'MRVL', cls:'pi-red',     impact:'&minus;14.3% &mdash; LOST SMA50 &#9888;', note:'$227.74. Lost the SMA50 $241.04 it had reclaimed, giving back three quarters of the +19.0% run. Below the $238&ndash;252 zone. The full repair completed on Oct 13 has already reversed.'},
    {ticker:'PANW', cls:'pi-red',     impact:'&minus;15.3% &mdash; SMA50 FLAT &#9888;', note:'$341.89. Gave back three quarters of the +21.2% run; SMA50 $373.27 has gone FLAT with price $31 beneath. Below its zone. The flat-SMA50 warning now applies to PANW itself.'},
    {ticker:'ANET', cls:'pi-yellow',  impact:'EXIT VALIDATED &mdash; $177 &#9888;',   note:'$177.03 (&minus;16.1%). Closed at $198.67 on Oct 13 for +6.8%; holding would now show &minus;4.9% and the $178 stop has been BREACHED. SMA50 $198.42 turned down. The exit saved 11.7 points.'},
    {ticker:'VRT',  cls:'pi-red',     impact:'&minus;13.8% &mdash; STILL FALLING &#9888;', note:'$206.42. Below the $215&ndash;235 zone redrawn four days ago &mdash; a third zone broken this cycle. SMA50 $255.46 falling, price $49 beneath. Down 36% since mid-August.'},
    {ticker:'DELL', cls:'pi-red',     impact:'&minus;21.7% &mdash; WORST ON BOARD &#9888;', note:'$451.67. The sharpest decline, giving back the entire +10.1% gain and more. SMA50 $513.26 still technically rising but price is $62 beneath it and below the $509&ndash;535 zone. A rising average with price far below is a fresh, violent breakdown.'},
  ],
  macro_watch: [
    'THE ANET EXIT IS THE RESULT THAT MATTERS: Recommended at $198.67 on Oct 13 for +6.8%. ANET is now $177.03 - holding would show -4.9%, and the $178 stop has been breached, so the position would have closed anyway 11.7 points lower. Two things made that call possible: the SMA50 was named in advance on Sep 5 as the line that mattered, and the holding-period rule flagged the trade as stale (six weeks on a 2-4 day horizon) before the price confirmed it. Naming the exit level in advance is what turned a judgement call into a decision.',
    'THE NEW TRAIL RULE PROVED ITSELF IN FOUR DAYS: Adopted Oct 13 as 2x ATR below the highest CLOSE since entry. NOW touched $148.57 on Oct 15, and the rule now computes a trail of $135.40 against the $129 set by hand four days earlier - a $6 ratchet produced by the rule rather than by a session. That is exactly the dependency ANET exposed when its stop sat at $178 for five weeks. The rule is now locking +31.2% instead of +25.0%.',
    'ONE DOUBLE-GATE PASS, AND THE TAPE ARGUES FOR HALF SIZE: PLTR is in its zone with a rising SMA50 above which it closed - the only name of thirteen to manage both. The stack is near-perfect and R/R is 4.61:1. But it fell 11% to get here, sits only $3.46 (under half an ATR) above the gate, and the whole complex is down hard. Conditions: mandatory volume confirmation, 0.5% size not 1%, and a close under $182.57 ends it. A valid setup and a hostile tape can coexist; the tape sets the size.',
    'RELATIVE WEAKNESS IS NOW THE MOST RELIABLE SIGNAL ON THIS BOARD: NVDA was flagged Oct 13 for going nowhere while its sector ran, sitting $2 above its SMA50, with the $222.59 test named as the thing to watch. It has broken below. That is three for three this cycle - VRT (flat while peers ran, then -36%), AVGO (nowhere for five weeks, then five call ups broken), NVDA (now below its average). Checking relative performance against the sector belongs in every call up.',
    'TSM REPORTED AND THE SECTOR FELL ANYWAY: The upstream bellwether printed on Oct 15 and the AI complex sold off regardless, with TSM itself dropping to $412.51. An upstream validation that does not stop a de-rating says this move is about multiples and positioning, not end-demand. That distinction matters for what comes next: a positioning unwind can overshoot far below fair value and reverse quickly, which is an argument for patience rather than for catching it.',
    'THE GATE GAVE BACK ITS MISSES: AMD, PANW and MRVL were the three big winners the gate cost between Sep 4 and Oct 12 (+24.5%, +21.2%, +19.0%). In four sessions AMD gave back nearly half, PANW three quarters, MRVL three quarters. All three are now below their SMA50s again. The gate did not capture those gains, and it also did not participate in the reversal - which is the clearest illustration yet of what the filter actually buys: not maximum return, but avoided round-trips.',
    'HEAVY READ-THROUGH WEEK, NO WATCHLIST NAMES: Nothing on the board reports Oct 19-23, but NFLX Tue, then META, TSLA, IBM, TXN, LRCX and SAP all Wed Oct 21, and WDC Thu. TXN and LRCX are the semis reads; META is the mega-cap AI capex read. Any PLTR entry would sit inside that cluster with no direct earnings risk but substantial sentiment risk - another reason for half size and for waiting on volume confirmation rather than anticipating.',
  ],
  weekly: {
    week: 'Oct 13 &ndash; Oct 16, 2026',
    updated: 'Fri Oct 16 session close (Oct 15 is the last settled close)',
    headline: 'Sharp AI Unwind &mdash; QQQ &minus;4.9% &mdash; ANET Exit Validated Below Its Stop &mdash; NOW The Only Name Up &mdash; PLTR The One Double-Gate Pass',
    week_chg: [
      {name:'QQQ',       open:'$746.04', close:'$709.86', chg:'&minus;4.9% &mdash; AI unwind',        dir:'down'},
      {name:'NOW',       open:'$140.32', close:'$141.95', chg:'+1.2% &mdash; only name up',           dir:'up'},
      {name:'PLTR',      open:'$209.00', close:'$186.03', chg:'&minus;11.0% &mdash; into zone',        dir:'down'},
      {name:'ANET',      open:'$210.88', close:'$177.03', chg:'&minus;16.1% &mdash; below its stop',   dir:'down'},
      {name:'DELL',      open:'$576.76', close:'$451.67', chg:'&minus;21.7% &mdash; worst on board',   dir:'down'},
    ],
    potw: {
      ticker:'NOW', type:'Manage the Winner &mdash; Rule-Driven Trail',
      entry:'$103.24 (Jul 19&ndash;25 zone floor)', exit:'Open &mdash; $141.95 Oct 16',
      high:'$148.57 close, Oct 15', pnl:'+37.5% and holding',
      verdict:'WINNER &mdash; ONLY NAME UP', verdictCls:'wr-win',
      note:'NOW rose 1.2% while every other name on the board fell, which is the third consecutive call up in which it has shown relative strength against the tape. The Oct 13 action was to raise the trail to $129 and adopt a standing rule &mdash; 2x ATR below the highest close since entry. That rule has now done the work by itself: the $148.57 Oct 15 high puts the trail at $135.40 rather than $129, a $6 ratchet with no judgement involved. It locks +31.2% and sits $0.55 above the rising SMA50 $134.85, with R/R to $175 at 5.05:1. The companion decision &mdash; closing ANET on Oct 13 &mdash; is what makes this the only open position going into a heavy earnings week.',
    },
    missed: {
      setup:'Nothing was missed. The Oct 13 call up produced two actions: close ANET at +6.8% and raise the NOW trail. Both were correct within four sessions.',
      trade:'ANET fell to $177.03, breaching its $178 stop; holding would show &minus;4.9%. NOW ran to $148.57 and the new rule ratcheted the trail automatically.',
      result:'The three winners the gate had missed (AMD +24.5%, PANW +21.2%, MRVL +19.0%) gave back half to three quarters of those gains in four sessions and are all back below their SMA50s.',
    },
    lessons: [
      {tag:'NAME THE EXIT', cls:'lsn-rule',  text:'The ANET exit worked because the SMA50 was named in advance on Sep 5 as the line that mattered, so when price reached it the decision was already made. Naming the level before it arrives converts a judgement call under pressure into a pre-committed decision.'},
      {tag:'RULE &gt; NUMBER', cls:'lsn-macro', text:'The standing trail rule adopted Oct 13 ratcheted NOW from $129 to $135.40 in four days with no session required. ANET&#39;s stop sat at $178 for five weeks because it was a number. A rule compounds; a number decays.'},
      {tag:'TAPE SETS SIZE', cls:'lsn-next',  text:'PLTR passes both gates with a near-perfect stack and 4.61:1 R/R, and it is being taken at half size with mandatory volume confirmation because QQQ is down 4.9% in four sessions and it sits under half an ATR above its gate. A valid setup and a hostile tape can coexist.'},
      {tag:'REL. WEAKNESS',  cls:'lsn-rule',  text:'NVDA broke the SMA50 it was flagged for sitting $2 above. Three for three this cycle: VRT, AVGO, NVDA. Relative performance against the sector now earns a line in every call up.'},
    ],
    eow: [
      {ticker:'NOW',  price:'$141.95', sCls:'eow-green',  status:'ONLY NAME UP +37.5% &#9650;',   note:'Rule ratchets trail to $135.40'},
      {ticker:'PLTR', price:'$186.03', sCls:'eow-green',  status:'ZONE + GATE &#10003;',          note:'Only double pass. Half size, stop $170'},
      {ticker:'MSFT', price:'$528.95', sCls:'eow-green',  status:'&minus;2.3% HELD UP &#9654;',    note:'1% from its zone with gate intact'},
      {ticker:'LMND', price:'$44.19',  sCls:'eow-yellow', status:'IN ZONE, BLOCKED &#9888;',      note:'6th call up. SMA50 $49.24 falling'},
      {ticker:'NVDA', price:'$214.14', sCls:'eow-red',    status:'BROKE SMA50 &#9888;',           note:'Flag played out. In zone, below gate'},
      {ticker:'ORCL', price:'$128.22', sCls:'eow-red',    status:'&minus;6.7% WATCH DEAD &#9888;', note:'SMA50 turned down. Below zone'},
      {ticker:'AVGO', price:'$328.81', sCls:'eow-red',    status:'5TH CALL UP BROKEN &#9888;',    note:'Below the zone redrawn Oct 13'},
      {ticker:'AMD',  price:'$528.76', sCls:'eow-yellow', status:'IN ZONE, BELOW GATE &#9660;',   note:'Gave back half the +24.5% run'},
      {ticker:'MRVL', price:'$227.74', sCls:'eow-red',    status:'LOST SMA50 &#9888;',            note:'Repair reversed in four sessions'},
      {ticker:'PANW', price:'$341.89', sCls:'eow-red',    status:'&minus;15.3% SMA50 FLAT &#9888;', note:'Gave back 3/4 of the +21.2% run'},
      {ticker:'VRT',  price:'$206.42', sCls:'eow-red',    status:'&minus;13.8% &#9888;',           note:'Third zone broken. &minus;36% since Aug'},
      {ticker:'ANET', price:'$177.03', sCls:'eow-yellow', status:'EXIT VALIDATED &#9888;',        note:'Below $178 stop. Exit saved 11.7 pts'},
      {ticker:'DELL', price:'$451.67', sCls:'eow-red',    status:'&minus;21.7% WORST &#9888;',     note:'$62 below a still-rising SMA50'},
    ],
  },
};"""
new_src,n = re.subn(r'const MARKET_PULSE = \{.*?\n\};', lambda m: NEW, src, flags=re.DOTALL)
if n!=1: print(f'ERROR: {n}'); sys.exit(1)
open(FILE,'w').write(new_src); print(f'OK - MARKET_PULSE replaced'); os.remove(FILE+'.bak')
