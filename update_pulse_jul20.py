#!/usr/bin/env python3
"""Update MARKET_PULSE with Jul 17 close data — tech selloff reverses bounce."""
import re, sys, shutil

FILE = 'templates/index.html'
shutil.copy(FILE, FILE + '.bak')
src = open(FILE, 'r').read()

NEW_PULSE = r"""const MARKET_PULSE = {
  date: 'July 20, 2026',
  updated: 'Call Up &mdash; Jul 17 Close (Live Robinhood + FMP Data)',
  headline: 'Tech Selloff Reverses Bounce &mdash; QQQ &minus;4.2% &mdash; AVGO Back In Zone $371 &mdash; MSFT Enters Zone $394 &mdash; NOW $103 Only SMA Gate Pass &mdash; GOOGL Earnings Mon',
  sentiment: 'SELLOFF &mdash; ZONES REOPENED &mdash; SMA GATES BLOCKING',
  sentimentCls: 'mkt-caution',
  indices: [
    {name:'SPY',        val:'$743.29', chg:'&minus;1.5% &mdash; pulled back from ATH $755',  dir:'down'},
    {name:'QQQ',        val:'$695.33', chg:'&minus;4.2% &mdash; tech selloff',                dir:'down'},
    {name:'IWM',        val:'$294.04', chg:'&minus;0.7% &mdash; small caps held',             dir:'down'},
    {name:'DIA',        val:'$520.81', chg:'&minus;0.9% &mdash; Dow holding',                 dir:'down'},
    {name:'AVGO',       val:'$370.83', chg:'&minus;7.3% &mdash; BACK IN ZONE $350&ndash;375', dir:'down'},
    {name:'MSFT',       val:'$393.82', chg:'+2.3% &mdash; ENTERED ZONE $393&ndash;412',       dir:'up'},
    {name:'NOW',        val:'$103.24', chg:'&minus;4.1% &mdash; AT ZONE FLOOR $103',          dir:'down'},
    {name:'MRVL',       val:'$188.68', chg:'&minus;19.9% &mdash; freefall continues',          dir:'down'},
  ],
  events: [
    {tag:'ZONES',    tagCls:'evt-watch', headline:'THREE NAMES IN ZONES &mdash; SMA GATE BLOCKS ALL BUT ONE', body:'The tech selloff pushed multiple names back into buy zones: AVGO $371 in zone $350&ndash;375, MSFT $394 in zone $393&ndash;412, VRT $290 at zone floor $290&ndash;312, NOW $103 at zone floor $103&ndash;118. But the SMA gate is blocking: AVGO SMA50 $403 (falling), MSFT SMA50 $402 (falling), VRT SMA50 $322 (falling). Only NOW has a RISING SMA50 ($103.34). The framework went from 1 setup to 4 zone entries but only 1 passes both gates.'},
    {tag:'NOW',      tagCls:'evt-watch', headline:'NOW $103.24 &mdash; AT ZONE FLOOR &mdash; ONLY SETUP PASSING BOTH GATES', body:'NOW pulled back from $108 to $103, now sitting at the zone floor ($103 in zone $103&ndash;118). SMA50 $103.34 is RISING (up from $102.28 over 5 sessions). Price is $0.10 below SMA50 &mdash; essentially AT it. Stop $88, target $175. R/R = ($175&minus;$103)/($103&minus;$88) = 4.7:1. This is the TIGHTEST setup on the board: zone floor entry = maximum R/R. If $103 breaks, setup dies (ORCL lesson). If it holds, this is the strongest risk/reward the framework has generated.'},
    {tag:'MSFT',     tagCls:'evt-watch', headline:'MSFT $393.82 &mdash; ENTERED ZONE $393&ndash;412 FOR FIRST TIME', body:'MSFT rose from $385 to $394 while tech sold off around it, entering zone $393&ndash;412 for the first time. SMA50 $402 (falling from $403). SMA stack INVERTED: SMA200 $439 &gt; SMA150 $417 &gt; SMA50 $402 &gt; SMA100 $399. Price below all four moving averages. This is a textbook falling knife environment per the framework. The SMA gate says STAND DOWN. Watch for SMA50 to flatten near $400 &mdash; Azure Q4 earnings late July could be the catalyst.'},
    {tag:'AVGO',     tagCls:'evt-watch', headline:'AVGO $370.83 &mdash; BACK IN ZONE &mdash; Gave Back Entire +11% Bounce', body:'AVGO gave back its entire +11% bounce, dropping from $401 to $371 in one week. Now back in zone $350&ndash;375 after clearing it last week. SMA50 $403 (falling from $406). Stack order still bullish (50&gt;100&gt;150&gt;200) but SMA50 declining and price $33 below it. Same SMA gate that blocked the +11% winner is now blocking re-entry. If SMA50 turns (needs $403 to flatten/rise), AVGO becomes actionable again. Until then, stand down.'},
    {tag:'EARN',     tagCls:'evt-macro', headline:'GOOGL Mon Jul 21, TSLA Tue Jul 22, INTC Wed Jul 23', body:'Google reports Monday (est. EPS $2.87). Cloud + AI revenue growth is the focus &mdash; strong results validate the AI infrastructure spending thesis that supports AVGO, NVDA, AMD. Tesla reports Tuesday. Intel reports Wednesday &mdash; competitor benchmark for AMD. None are watchlist names but GOOGL and INTC results have direct read-through to our positions.'},
    {tag:'RISK',     tagCls:'evt-geo',   headline:'MRVL $188.68 &mdash; Freefall: Trail Stop Has Saved 35% More Downside', body:'MRVL dropped from $236 to $189 this week (&minus;19.9%), now $101 below the $290 trail stop. From the stop level, the trail has avoided 35% more downside ($290 to $189). From peak $311, holding without the trail would mean &minus;39% drawdown. SMA50 $236 is falling and price is $47 below it. MRVL is in a structural downtrend. No re-entry until price stabilizes above SMA50 for multiple weeks.'},
  ],
  portfolio: [
    {ticker:'NOW',  cls:'pi-green',   impact:'AT ZONE FLOOR &mdash; $103 &#10003;', note:'$103.24. Zone $103&ndash;118 (at floor). SMA50 $103.34 RISING. R/R 4.7:1. Only name passing both gates. Tightest entry = highest R/R. If $103 breaks, setup dies.'},
    {ticker:'AVGO', cls:'pi-yellow',  impact:'BACK IN ZONE &mdash; $371 &#9660;',   note:'$370.83. Zone $350&ndash;375 (re-entered). SMA50 $403 falling. Gave back +11% bounce. Gate blocks. Stack bullish but SMA declining.'},
    {ticker:'MSFT', cls:'pi-yellow',  impact:'ENTERED ZONE &mdash; $394 &#9650;',   note:'$393.82. Zone $393&ndash;412 (first time). SMA50 $402 falling. Stack inverted (200>150>50>100). Gate blocks.'},
    {ticker:'VRT',  cls:'pi-yellow',  impact:'AT ZONE FLOOR &mdash; $290 &#9660;',  note:'$289.56. Zone $290&ndash;312 (at floor). SMA50 $322 falling. Price $32 below SMA50. Gate blocks.'},
    {ticker:'NVDA', cls:'pi-yellow',  impact:'LOST SMA50 &mdash; $203 &#9660;',     note:'$202.81. Lost SMA50 reclaim ($210). Now $7 below SMA50 $210. Above zone $175&ndash;192. Trend signal reversed.'},
    {ticker:'AMD',  cls:'pi-yellow',  impact:'DROPPED &minus;11% &mdash; $496 &#9660;', note:'$495.76. At SMA50 $499. Big drop from $558. Zone $370&ndash;390 still far ($106 away).'},
    {ticker:'DELL', cls:'pi-yellow',  impact:'DROPPED &minus;9% &mdash; $396 &#9660;', note:'$396.34. Continued selloff from $435. Zone $310&ndash;355 still above.'},
    {ticker:'ANET', cls:'pi-yellow',  impact:'DROPPED &minus;10% &mdash; $169 &#9660;', note:'$168.61. Gave back bounce gains. Zone $128&ndash;148 still above.'},
    {ticker:'PANW', cls:'pi-yellow',  impact:'RALLIED +10% &mdash; $359 &#9650;',   note:'$358.68. Bucked the selloff. Well above zone $232&ndash;252.'},
    {ticker:'PLTR', cls:'pi-yellow',  impact:'BOUNCED +4% &mdash; $132 &#9650;',    note:'$132.38. Slight bounce. Still below SMA50.'},
    {ticker:'LMND', cls:'pi-yellow',  impact:'DROPPED &mdash; $67 &#9660;',         note:'$67.18. Above zone $45&ndash;56. No chase.'},
    {ticker:'ORCL', cls:'pi-red',     impact:'CONTINUED FALL &mdash; $126 &#9888;',  note:'$126.41. Down from $141. Well below $148 stop. Dead setup.'},
    {ticker:'MRVL', cls:'pi-red',     impact:'FREEFALL &mdash; $189 &#9888;',        note:'$188.68. Down 35% from $290 stop. Trail saved $101/share. No re-entry.'},
  ],
  macro_watch: [
    '🎯 FOUR ZONES, ONE GATE PASS: AVGO ($371 in zone), MSFT ($394 in zone), VRT ($290 at floor), NOW ($103 at floor). The selloff reopened zones that were cleared last week. But the SMA gate blocks all except NOW — AVGO, MSFT, and VRT all have falling SMA50s. NOW is the only name with a RISING SMA50 ($103.34). Quality over quantity.',
    '📊 NOW AT ZONE FLOOR = MAXIMUM R/R: NOW $103.24 at zone floor $103. Stop $88, target $175. R/R = 4.7:1 — the highest R/R the framework has generated. Last week at $108 the R/R was 3.4:1. The pullback IMPROVED the setup. If $103 holds, this is the optimal entry point. If it breaks, exit immediately (ORCL lesson).',
    '📈 GOOGL EARNINGS MON JUL 21: Google est. EPS $2.87. Cloud + AI revenue is the focus. Strong GOOGL = AI infrastructure thesis validated = positive for AVGO, NVDA, AMD. TSLA Tue Jul 22. INTC Wed Jul 23 (AMD competitor read-through).',
    '⚠️ AVGO ROUND-TRIP: AVGO rallied +11% from $360 to $401 (SMA gate blocked entry), then sold off −7.3% back to $371. The entire bounce has been given back. If the gate HAD been ignored, a $360 entry would now show +3% (not the +11% it showed last week). The gate decision looks even better in hindsight — the bounce was temporary.',
    '📉 MSFT ENTERED ZONE BUT STACK IS INVERTED: MSFT $394 entered zone $393–412 for the first time, but SMA stack is bearish: SMA200 $439 > SMA150 $417 > SMA50 $402 > SMA100 $399. Price below ALL four MAs. This is a long-term downtrend with no reversal signal. The zone entry alone is insufficient — the SMA gate exists for exactly this scenario.',
    '🔻 QQQ −4.2% TECH SELLOFF: QQQ dropped from $726 to $695, the biggest weekly decline since the Jun rotation. SPY −1.5% held up better. The selloff is concentrated in tech/AI names: AVGO −7%, AMD −11%, DELL −9%, ANET −10%. Defensive names (PANW +10%, PLTR +4%) outperformed.',
    '📉 MRVL TRAIL STOP: ULTIMATE VALIDATION: $290 stop → $189 current = $101/share of avoided loss (35%). From peak $311 to $189 = −39% drawdown without the trail. The trail stop is now the most proven rule in the framework by a massive margin.',
  ],
  weekly: {
    week: 'Jul 14 &ndash; Jul 17, 2026',
    updated: 'Thu Jul 17 close (Live Robinhood + FMP data)',
    headline: 'Tech Selloff Reverses Bounce &mdash; QQQ &minus;4.2% &mdash; AVGO Back in Zone &mdash; MSFT Enters Zone &mdash; NOW Only Gate Pass',
    week_chg: [
      {name:'SPY',       open:'$754.95', close:'$743.29', chg:'&minus;1.5% &mdash; off ATH',           dir:'down'},
      {name:'QQQ',       open:'$725.51', close:'$695.33', chg:'&minus;4.2% &mdash; tech selloff',       dir:'down'},
      {name:'AVGO',      open:'$399.99', close:'$370.83', chg:'&minus;7.3% &mdash; back in zone',       dir:'down'},
      {name:'MSFT',      open:'$385.09', close:'$393.82', chg:'+2.3% &mdash; entered zone',             dir:'up'},
      {name:'MRVL',      open:'$235.67', close:'$188.68', chg:'&minus;19.9% &mdash; freefall',           dir:'down'},
    ],
    potw: {
      ticker:'NOW', type:'Zone + SMA Confirmed &mdash; AT ZONE FLOOR',
      entry:'Zone $103&ndash;118 / SMA50 $103 rising', exit:'$103.24 Jul 17 &mdash; at zone floor',
      high:'$113.50 intraday Jul 14', pnl:'&minus;4.1% from $108 entry level',
      verdict:'HELD IN ZONE &mdash; PULLED TO FLOOR', verdictCls:'wr-miss',
      note:'NOW was POTW at $108 in zone $103&ndash;118 with rising SMA50 $102. The tech selloff pulled NOW from $108 to $103 &mdash; still in zone but now at the floor. SMA50 continued rising to $103.34, confirming the trend filter. R/R IMPROVED from 3.4:1 to 4.7:1 because entry is now at the floor with tighter distance to stop. The setup is technically STRONGER this week despite the price drop. Key level: $103 must hold.',
    },
    missed: {
      setup:'AVGO re-entered zone at $371 (was above at $400). MSFT entered zone at $394. VRT at zone floor $290. All three have falling SMA50s.',
      trade:'NOW $103 at zone floor is the only setup passing both gates. R/R improved to 4.7:1. All other zone entries blocked by SMA gate.',
      result:'Tech selloff opened 3 new zone entries but SMA gate correctly identifies all as falling-knife environments. NOW rising SMA50 is the differentiator.',
    },
    lessons: [
      {tag:'ROUND-TRIP', cls:'lsn-rule',  text:'AVGO round-tripped its entire +11% bounce back to $371. If the SMA gate had been ignored and entry taken at $360, the position would show +3% not +11%. The bounce was temporary. Gate decision vindicated further.'},
      {tag:'ZONES',      cls:'lsn-macro', text:'The selloff reopened 3 zones (AVGO, MSFT, VRT) while keeping NOW in zone. But zone entry alone is insufficient &mdash; the SMA gate is the quality filter. 4 zone entries, 1 gate pass.'},
      {tag:'MSFT',       cls:'lsn-next',  text:'MSFT entered zone $393&ndash;412 for the first time but SMA stack is fully inverted (200>150>50>100). Price below all 4 MAs. The falling-knife SMA gate was designed for exactly this scenario.'},
      {tag:'MRVL',       cls:'lsn-rule',  text:'MRVL trail stop has now avoided 35% additional downside ($290 to $189). From peak $311, the untrailed drawdown is &minus;39%. Framework rule validated to framework record.'},
    ],
    eow: [
      {ticker:'NOW',  price:'$103.24', sCls:'eow-green',  status:'AT ZONE FLOOR &#10003;',       note:'SMA50 rising. R/R 4.7:1. Only gate pass'},
      {ticker:'AVGO', price:'$370.83', sCls:'eow-yellow', status:'BACK IN ZONE &#9660;',          note:'Zone $350&ndash;375. SMA50 $403 falling'},
      {ticker:'MSFT', price:'$393.82', sCls:'eow-green',  status:'ENTERED ZONE &#9650;',          note:'Zone $393&ndash;412. SMA50 $402 falling'},
      {ticker:'VRT',  price:'$289.56', sCls:'eow-yellow', status:'AT ZONE FLOOR &#9660;',         note:'Zone $290&ndash;312. SMA50 $322 falling'},
      {ticker:'NVDA', price:'$202.81', sCls:'eow-yellow', status:'LOST SMA50 &#9660;',            note:'Below $210. Trend reversed'},
      {ticker:'AMD',  price:'$495.76', sCls:'eow-yellow', status:'AT SMA50 &minus;11% &#9660;',   note:'SMA50 $499. Zone $370 far'},
      {ticker:'PANW', price:'$358.68', sCls:'eow-green',  status:'RALLIED +10% &#9650;',          note:'Bucked selloff. Above zone'},
      {ticker:'PLTR', price:'$132.38', sCls:'eow-yellow', status:'BOUNCED +4% &#9650;',           note:'Still below SMA50'},
      {ticker:'DELL', price:'$396.34', sCls:'eow-yellow', status:'DROPPED &minus;9% &#9660;',     note:'Above zone $310&ndash;355'},
      {ticker:'ANET', price:'$168.61', sCls:'eow-yellow', status:'DROPPED &minus;10% &#9660;',    note:'Above zone $128&ndash;148'},
      {ticker:'LMND', price:'$67.18',  sCls:'eow-yellow', status:'DROPPED &#9660;',               note:'Above zone $45&ndash;56'},
      {ticker:'ORCL', price:'$126.41', sCls:'eow-red',    status:'CONTINUED FALL &#9888;',        note:'Below $148 stop. Dead'},
      {ticker:'MRVL', price:'$188.68', sCls:'eow-red',    status:'FREEFALL &#9888;',              note:'&minus;35% from stop. Trail record'},
    ],
  },
};"""

pattern = r'const MARKET_PULSE = \{.*?\n\};'
new_src, count = re.subn(pattern, NEW_PULSE, src, flags=re.DOTALL)

if count != 1:
    print(f'ERROR: expected 1 replacement, got {count}')
    sys.exit(1)

open(FILE, 'w').write(new_src)
print(f'OK — replaced MARKET_PULSE block ({count} substitution)')

import os
os.remove(FILE + '.bak')
print('Cleaned up backup file')
