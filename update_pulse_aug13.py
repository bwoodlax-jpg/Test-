#!/usr/bin/env python3
"""Update MARKET_PULSE with Aug 12 close data — 4-week melt-up, every zone cleared."""
import re, sys, os, shutil

FILE = 'templates/index.html'
shutil.copy(FILE, FILE + '.bak')
src = open(FILE, 'r').read()

NEW_PULSE = """const MARKET_PULSE = {
  date: 'August 13, 2026',
  updated: 'Call Up &mdash; Aug 12 Close (Live Robinhood Data) &mdash; First refresh since Jul 20',
  headline: 'Four-Week Melt-Up &mdash; SPY $772 ATH &mdash; MSFT +25% on Azure Gap &mdash; NOW POTW +21% WINNER &mdash; EVERY ZONE CLEARED &mdash; Zero New Setups',
  sentiment: 'MELT-UP &mdash; NO ENTRIES &mdash; MANAGE WINNERS',
  sentimentCls: 'mkt-up',
  indices: [
    {name:'SPY',        val:'$772.49', chg:'+3.9% since Jul 17 &mdash; new ATH',        dir:'up'},
    {name:'QQQ',        val:'$723.70', chg:'+4.1% &mdash; full recovery + more',         dir:'up'},
    {name:'IWM',        val:'$302.71', chg:'+2.9% &mdash; small caps participating',     dir:'up'},
    {name:'DIA',        val:'$537.15', chg:'+3.1% &mdash; broad strength',               dir:'up'},
    {name:'MSFT',       val:'$492.43', chg:'+25.0% &mdash; Azure earnings gap Jul 30',   dir:'up'},
    {name:'NOW',        val:'$124.94', chg:'+21.0% &mdash; POTW WINNER from $103',       dir:'up'},
    {name:'PLTR',       val:'$171.04', chg:'+29.2% &mdash; biggest move on the board',   dir:'up'},
    {name:'LMND',       val:'$51.64',  chg:'&minus;23.1% &mdash; only name in a zone',   dir:'down'},
  ],
  events: [
    {tag:'POTW',     tagCls:'evt-watch', headline:'NOW $124.94 &mdash; POTW IS A +21% WINNER &mdash; Above ALL Four SMAs', body:'The Jul 19&ndash;25 Play of the Week called NOW at the $103 zone floor with R/R 4.7:1. NOW closed Aug 12 at $124.94 &mdash; up 21.0% from the entry level. The zone-floor thesis worked exactly as designed: $103 held as support, the rising SMA50 confirmed the trend, and the stock ran. NOW is now trading ABOVE ALL FOUR moving averages for the first time in this cycle (SMA50 $107.59, SMA100 $102.84, SMA150 $107.83, SMA200 $122.44). Clearing the SMA200 at $122.44 is the milestone that converts this from early-stage recovery to confirmed uptrend. Target $175 remains live. This is now a MANAGE-THE-WINNER position, not an entry.'},
    {tag:'MSFT',     tagCls:'evt-macro', headline:'MSFT $492.43 &mdash; +25% on a 15.5% Azure Earnings Gap (Jul 30)', body:'MSFT closed Jul 29 at $390.54 and opened Jul 30 at $437.90, closing $451.10 &mdash; a 15.5% single-session earnings gap on Azure Q4 results. It has continued to $492.43. The SMA gate had blocked MSFT entry at $394 in July because the SMA50 was falling and the full stack was inverted. That block cost a 25% winner. But the same gate blocked ORCL through its zone and MRVL into its stop. SMA50 is now $410.30 and RISING &mdash; the trend has genuinely turned. MSFT is 20% above its SMA50, far too extended for a new entry. Wait for a pullback toward $410&ndash;435.'},
    {tag:'ZONES',    tagCls:'evt-watch', headline:'EVERY ZONE CLEARED &mdash; Zero Names Pass Both Gates', body:'The four-week melt-up pushed every watchlist name that passes the SMA gate ABOVE its buy zone. NOW $125 (zone $103&ndash;118), MSFT $492 (zone $393&ndash;412), NVDA $224 (zone $175&ndash;192), AVGO $416 (zone $350&ndash;375), PLTR $171 (zone $108&ndash;122), ANET $211 (zone $128&ndash;148), DELL $485 (zone $335&ndash;355), PANW $387 (zone $232&ndash;252). The only name still INSIDE a zone is LMND at $51.64 in zone $45&ndash;56 &mdash; and its SMA50 $60.04 is falling with price below it. That is the textbook falling-knife pattern the gate exists to block. Net result: ZERO actionable new entries this week. All watchlist zones have been recalibrated to current structure.'},
    {tag:'BROKEN',   tagCls:'evt-geo',   headline:'VRT $288.36 &mdash; Broke BELOW Zone Floor &mdash; The ORCL Pattern Again', body:'VRT is the one AI-infrastructure name that did not participate, closing &minus;0.4% over four weeks while the sector ran 10&ndash;29%. More importantly it broke BELOW its zone floor $290, with SMA50 $298.32 falling and SMA100 $303.38 above it. Price is beneath both. This is the identical structure ORCL showed before it fell 30% through its zone. The setup is dead until VRT builds a base and reclaims the SMA50. Monitor only &mdash; do not average into a broken zone.'},
    {tag:'EARN',     tagCls:'evt-macro', headline:'Retail Week Aug 18&ndash;19 &mdash; HD, LOW, TGT &mdash; No Watchlist Names Report', body:'No watchlist name reports Aug 13&ndash;19. The calendar is retail: Home Depot Tue Aug 18 (est. EPS $4.73), Lowe\\'s and Target Wed Aug 19 (est. $4.39 and $2.24). These are consumer-health reads, not AI-thesis reads, but a broad retail miss would test whether the melt-up has macro support or is purely an AI-capex narrative. Watch as a risk-sentiment gauge only.'},
    {tag:'RISK',     tagCls:'evt-geo',   headline:'LMND $51.64 &mdash; Down 23% &mdash; In Zone but Failing the SMA Gate', body:'LMND fell from $67.18 to $51.64 (&minus;23.1%), dropping into its buy zone $45&ndash;56. It is the only name in a zone. But SMA50 $60.04 is falling and price is $8.40 BELOW it. Zone presence without SMA confirmation is exactly the ORCL/MSFT-in-July setup &mdash; and the gate blocks it. If LMND bases above $52 and the SMA50 flattens, it becomes the first genuine new setup in weeks. Not yet.'},
  ],
  portfolio: [
    {ticker:'NOW',  cls:'pi-green',   impact:'WINNER +21% &mdash; $125 &#9650;',    note:'$124.94 from $103 POTW entry. Above ALL four SMAs (50/100/150/200). Cleared SMA200 $122.44 &mdash; uptrend confirmed. Trail stop to $113. Target $175 live. MANAGE, do not add.'},
    {ticker:'MSFT', cls:'pi-green',   impact:'+25% ON EARNINGS GAP &#9650;',       note:'$492.43. Gapped 15.5% Jul 30 on Azure. SMA50 $410.30 now RISING. 20% above SMA50 &mdash; extended. New zone $410&ndash;435. Gate had blocked at $394; cost a winner.'},
    {ticker:'PLTR', cls:'pi-green',   impact:'+29% &mdash; BIGGEST MOVE &#9650;',   note:'$171.04. SMA50 $133.89 rising. 28% above SMA50 &mdash; heavily extended. New zone $138&ndash;152. No entry at these levels.'},
    {ticker:'ANET', cls:'pi-green',   impact:'+25% &mdash; $211 &#9650;',           note:'$210.50. SMA50 $172.58 rising. Well above old zone $128&ndash;148. New zone $172&ndash;188.'},
    {ticker:'DELL', cls:'pi-green',   impact:'+22% &mdash; $485 &#9650;',           note:'$484.50. SMA50 $418.69 rising strongly. New zone $418&ndash;448. Recovered fully from the Jun redraw.'},
    {ticker:'ORCL', cls:'pi-yellow',  impact:'+21% BUT BELOW SMA50 &#9654;',        note:'$153.28. Big bounce off the lows but SMA50 $155.58 is still FALLING and price sits below it. Gate blocks. Zone redrawn $138&ndash;150.'},
    {ticker:'AVGO', cls:'pi-green',   impact:'+12% &mdash; $416 &#9650;',           note:'$416.05. Above SMA50 $393.47 (roughly flat). SMA50/100 confluence $391&ndash;393 is the new support shelf. New zone $390&ndash;408.'},
    {ticker:'NVDA', cls:'pi-green',   impact:'+10% &mdash; $224 &#9650;',           note:'$224.09. SMA50 $206.13 rising, SMA100 $203.20. Clean bullish stack. New zone $203&ndash;213. Above old zone top $192.'},
    {ticker:'MRVL', cls:'pi-yellow',  impact:'+15% RECOVERY &mdash; $217 &#9654;',  note:'$217.08. Strong bounce from $189 but still BELOW SMA50 $240.97. Gate blocks. Recovering, not recovered.'},
    {ticker:'PANW', cls:'pi-green',   impact:'+8% &mdash; $387 &#9650;',            note:'$387.01. SMA50 $322.21 rising sharply. 20% above SMA50. New zone $322&ndash;348.'},
    {ticker:'AMD',  cls:'pi-yellow',  impact:'&minus;3% &mdash; BELOW SMA50 &#9660;', note:'$482.93. SMA50 $511.56 FALLING, price below it. The only large AI name still under its trend filter. Gate blocks.'},
    {ticker:'VRT',  cls:'pi-red',     impact:'BROKE ZONE FLOOR &mdash; $288 &#9888;', note:'$288.36. Broke below zone floor $290. SMA50 $298.32 falling, SMA100 $303.38. Price under both. ORCL pattern. Setup dead.'},
    {ticker:'LMND', cls:'pi-yellow',  impact:'&minus;23% &mdash; IN ZONE, KNIFE &#9888;', note:'$51.64. Only name in a zone ($45&ndash;56). But SMA50 $60.04 falling, price $8.40 below. Falling knife. Gate blocks.'},
  ],
  macro_watch: [
    '🏆 POTW SCORECARD: The Jul 19–25 call on NOW at the $103 zone floor is a +21% winner. The thesis was that a pullback to the zone floor IMPROVES R/R (4.7:1 vs 3.4:1 the prior week) as long as the floor holds and the SMA50 keeps rising. Both conditions held. This is the framework working exactly as designed — the discipline was in waiting for the floor, not chasing at $108.',
    '📈 EVERY ZONE CLEARED — ZERO NEW ENTRIES: Eight watchlist names pass the SMA gate and all eight are ABOVE their buy zones. One name (LMND) is in a zone and fails the SMA gate. The correct framework answer this week is: no new positions. Manage what is open. A melt-up is the hardest tape to stay disciplined in — every name looks like it is running away. That is precisely when chasing does the most damage.',
    '🚪 ZONES RECALIBRATED: The old zones were drawn during the June–July selloff and are now 15–30% below market. Every zone has been redrawn to current structure using the SMA50/SMA100 confluence as the pullback anchor and the pre-breakout base as the stop. This is the same discipline applied to DELL (Jun 11) and AVGO (Jul) when price invalidated their zones — a zone that price has left behind is not a zone, it is a memory.',
    '💸 THE MSFT COST: The SMA gate blocked MSFT at $394 in July because the SMA50 was falling and the stack was inverted. MSFT then gapped 15.5% on Azure earnings and ran to $492 (+25%). That is the single largest winner the gate has cost. The honest tally: the gate has now missed AVGO (+11%, which round-tripped), VRT (+8%), and MSFT (+25%, which held). It blocked ORCL (−30%), MRVL (−19% into the stop), and VRT again (broke its floor). The gate is still net-positive on capital preserved, but MSFT is the strongest argument yet for adding an earnings-gap exception to the filter.',
    '⚠️ VRT IS THE TELL: While every other AI-infrastructure name ran 10–29%, VRT went −0.4% and broke below its zone floor. Relative weakness during a sector melt-up is a genuine warning, not noise. VRT was a high-conviction name (PP 7, Macro 9, Catalyst 8). It is now the ORCL pattern: price below SMA50 and SMA100, both falling. Setup dead pending a base and SMA50 reclaim.',
    '📅 QUIET CALENDAR: No watchlist name reports Aug 13–19. Retail dominates — HD Tue, LOW and TGT Wed. Use it as a consumer-health read. The next watchlist catalysts are the late-August/September prints. A quiet calendar in a melt-up tape argues for patience, not for manufacturing a trade.',
    '📉 TRAIL STOP DISCIPLINE: NOW is +21% with target $175 still 40% away. The framework rule from MRVL applies: raise the trail as the position runs. 2× ATR (ATR14 = $5.95) below $124.94 puts the trail at $113 — locking in +9.5% while leaving room for normal volatility. MRVL proved the trail is the most valuable rule in the book; NOW is where it gets applied to a winner instead of a loser.',
  ],
  weekly: {
    week: 'Jul 20 &ndash; Aug 12, 2026 (4-week span)',
    updated: 'Wed Aug 12 close (Live Robinhood data)',
    headline: 'Four-Week Melt-Up &mdash; SPY +3.9% to ATH &mdash; MSFT +25%, PLTR +29%, ANET +25% &mdash; NOW POTW +21% Winner &mdash; VRT Breaks Down',
    week_chg: [
      {name:'SPY',       open:'$743.29', close:'$772.49', chg:'+3.9% &mdash; new ATH',           dir:'up'},
      {name:'QQQ',       open:'$695.33', close:'$723.70', chg:'+4.1% &mdash; full recovery',      dir:'up'},
      {name:'MSFT',      open:'$393.82', close:'$492.43', chg:'+25.0% &mdash; Azure gap',         dir:'up'},
      {name:'NOW',       open:'$103.24', close:'$124.94', chg:'+21.0% &mdash; POTW winner',       dir:'up'},
      {name:'VRT',       open:'$289.56', close:'$288.36', chg:'&minus;0.4% &mdash; broke floor',  dir:'down'},
    ],
    potw: {
      ticker:'NOW', type:'Zone Floor Entry &mdash; WINNER',
      entry:'Zone floor $103.24 (Jul 19&ndash;25 POTW)', exit:'Open &mdash; $124.94 Aug 12',
      high:'$126.80 intraday Aug 11', pnl:'+21.0% and holding',
      verdict:'WINNER &mdash; +21% OPEN', verdictCls:'wr-win',
      note:'The zone-floor thesis was the whole call: at $103.24 the entry sat exactly on the zone floor with a rising SMA50, giving R/R 4.7:1 versus 3.4:1 the week before at $108. The floor held, the SMA50 kept rising, and NOW ran 21%. It has now cleared ALL FOUR moving averages including the SMA200 at $122.44 &mdash; the milestone that converts early-stage recovery into a confirmed uptrend. Target $175 is still 40% away. Position management now takes over from entry analysis: trail stop to $113 (2x ATR), let the rest run.',
    },
    missed: {
      setup:'MSFT was the big miss. Blocked at $394 by the SMA gate (falling SMA50, inverted stack), it gapped 15.5% on Azure earnings Jul 30 and ran to $492.',
      trade:'MSFT $394 entry would have returned +25%. The gate also correctly blocked VRT, which subsequently broke below its zone floor while the whole sector rallied.',
      result:'The gate cost its largest winner to date. It also avoided the one AI-infrastructure name that broke down. Net capital preserved still favors the gate, but the earnings-gap exception deserves a hard look.',
    },
    lessons: [
      {tag:'ZONE FLOOR', cls:'lsn-rule',  text:'NOW validated the zone-floor principle: a pullback to the floor improves R/R rather than degrading the setup, PROVIDED the floor holds and the SMA50 is rising. Entry at $103 (R/R 4.7:1) beat entry at $108 (R/R 3.4:1) on both risk and return. Patience at the floor paid 21%.'},
      {tag:'GAP COST',   cls:'lsn-macro', text:'MSFT gapped 15.5% on Azure earnings the week after the SMA gate blocked it at $394. A falling SMA50 cannot anticipate an earnings surprise. This is the gate\\'s structural blind spot: it filters trend, and an earnings gap is a trend discontinuity. Consider an explicit pre-earnings exception.'},
      {tag:'MELT-UP',    cls:'lsn-next',  text:'Eight names pass the SMA gate and all eight are above their zones. Zero entries is the correct answer, not a failure of the screen. The hardest discipline is doing nothing while everything runs. Zones were recalibrated to current structure so the board reflects reality.'},
      {tag:'VRT',        cls:'lsn-rule',  text:'Relative weakness during a sector melt-up is a real signal. VRT went &minus;0.4% while peers ran 10&ndash;29%, then broke its zone floor with price below a falling SMA50 and SMA100. Same structure ORCL showed before &minus;30%. Do not average into a broken zone.'},
    ],
    eow: [
      {ticker:'NOW',  price:'$124.94', sCls:'eow-green',  status:'WINNER +21% &#9650;',        note:'Above all 4 SMAs. Trail $113. Target $175'},
      {ticker:'MSFT', price:'$492.43', sCls:'eow-green',  status:'+25% GAP &#9650;',            note:'Azure gap Jul 30. SMA50 $410 rising'},
      {ticker:'PLTR', price:'$171.04', sCls:'eow-green',  status:'+29% EXTENDED &#9650;',       note:'28% above SMA50 $134. No entry'},
      {ticker:'ANET', price:'$210.50', sCls:'eow-green',  status:'+25% &#9650;',                note:'SMA50 $173 rising. New zone $172-188'},
      {ticker:'DELL', price:'$484.50', sCls:'eow-green',  status:'+22% &#9650;',                note:'SMA50 $419 rising. New zone $418-448'},
      {ticker:'ORCL', price:'$153.28', sCls:'eow-yellow', status:'+21% BUT BELOW SMA &#9654;',  note:'SMA50 $156 falling. Gate blocks'},
      {ticker:'AVGO', price:'$416.05', sCls:'eow-green',  status:'+12% &#9650;',                note:'SMA50 $393 flat. New zone $390-408'},
      {ticker:'NVDA', price:'$224.09', sCls:'eow-green',  status:'+10% &#9650;',                note:'Clean stack. New zone $203-213'},
      {ticker:'MRVL', price:'$217.08', sCls:'eow-yellow', status:'+15% RECOVERY &#9654;',       note:'Still below SMA50 $241. Gate blocks'},
      {ticker:'PANW', price:'$387.01', sCls:'eow-green',  status:'+8% &#9650;',                 note:'SMA50 $322 rising. New zone $322-348'},
      {ticker:'AMD',  price:'$482.93', sCls:'eow-yellow', status:'&minus;3% BELOW SMA50 &#9660;', note:'SMA50 $512 falling. Gate blocks'},
      {ticker:'VRT',  price:'$288.36', sCls:'eow-red',    status:'BROKE FLOOR &#9888;',          note:'Below SMA50 + SMA100. Setup dead'},
      {ticker:'LMND', price:'$51.64',  sCls:'eow-red',    status:'&minus;23% KNIFE &#9888;',     note:'In zone but SMA50 $60 falling'},
    ],
  },
};"""

pattern = r'const MARKET_PULSE = \{.*?\n\};'
new_src, count = re.subn(pattern, lambda m: NEW_PULSE, src, flags=re.DOTALL)

if count != 1:
    print(f'ERROR: expected 1 replacement, got {count}')
    sys.exit(1)

open(FILE, 'w').write(new_src)
print(f'OK - replaced MARKET_PULSE block ({count} substitution)')
os.remove(FILE + '.bak')
print('Cleaned up backup file')
