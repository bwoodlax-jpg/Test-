#!/usr/bin/env python3
"""Update MARKET_PULSE with Jul 10 (Fri) close data — end of week."""
import re, sys

FILE = 'templates/index.html'
src = open(FILE, 'r').read()

NEW_PULSE = r"""const MARKET_PULSE = {
  date: 'July 12, 2026',
  updated: 'Weekend Call Up &mdash; Jul 10 Close (Live Robinhood + FMP Data)',
  headline: 'SPY $755 New Closing High &mdash; NVDA $211 Reclaims SMA50 &mdash; NOW $108 Only Zone + SMA Confirmed Setup &mdash; Bank Earnings Monday &mdash; TSM Thursday',
  sentiment: 'BULLISH &mdash; ONE CONFIRMED SETUP &mdash; EARNINGS WEEK',
  sentimentCls: 'mkt-up',
  indices: [
    {name:'SPY',        val:'$754.95', chg:'+0.43% &mdash; new closing high',        dir:'up'},
    {name:'QQQ',        val:'$725.51', chg:'+0.31% &mdash; 3% off ATH $748',         dir:'up'},
    {name:'DIA',        val:'$525.78', chg:'+0.30% &mdash; near ATH $532',            dir:'up'},
    {name:'IWM',        val:'$295.99', chg:'&minus;0.42% &mdash; small caps pause',   dir:'down'},
    {name:'NVDA',       val:'$210.96', chg:'+4.0% &mdash; RECLAIMED SMA50 $209',      dir:'up'},
    {name:'AVGO',       val:'$399.99', chg:'flat &mdash; holding $400, SMA50 $406',    dir:'down'},
    {name:'NOW',        val:'$107.69', chg:'IN ZONE $103&ndash;118 + SMA50 RISING',   dir:'up'},
    {name:'MRVL',       val:'$235.67', chg:'&minus;3.1% &mdash; continued fall',       dir:'down'},
  ],
  events: [
    {tag:'SETUP',    tagCls:'evt-watch', headline:'NOW $107.69 &mdash; ONLY NAME WITH ZONE + SMA CONFIRMATION', body:'ServiceNow is the sole watchlist name passing BOTH framework gates. IN ZONE: $107.69 inside $103&ndash;118. SMA50 RISING: $101.83, up from $101.12 three days ago, price above it. At $107.69: stop $88, target $175, R/R = 3.4:1 (passes 2.5:1 gate). CAVEAT: the full SMA stack is inverted (SMA200 $131 > SMA150 $115 > SMA100 $103 > SMA50 $102) &mdash; this is early-stage recovery, not a confirmed uptrend. The SMA50 turn is the first sign of trend reversal. Higher confidence if SMA50 crosses above SMA100 ($103). Q2 earnings upcoming as catalyst.'},
    {tag:'SIGNAL',   tagCls:'evt-watch', headline:'NVDA $210.96 &mdash; Reclaims SMA50 $209 for First Time Since Selloff', body:'NVDA closed above its SMA50 ($209.20) for the first time since the tech rotation began. SMA stack: SMA50 $209 > SMA100 $198 > SMA200 $192 &mdash; BULLISH ORDER confirmed. But NVDA is NOT in zone ($175&ndash;192) &mdash; price is $19 above zone top. This is a trend-health signal, not an entry signal. If NVDA holds above SMA50 next week, it confirms the broader tech recovery is real. Watch for a re-test of $209 as support.'},
    {tag:'EARN',     tagCls:'evt-macro', headline:'Bank Earnings Mon Jul 14 &mdash; JPM, BAC, WFC, C, GS + TSM Thu Jul 16', body:'Five major banks report Monday. JPM est. EPS $5.52, BAC $1.12, WFC $1.74, C $2.72, GS $14.01. Strong results = risk-on continues, SPY pushes toward ATH $760. TSM reports Thursday (est. EPS $3.77, rev $40B) &mdash; the most important print for our AI thesis. TSM makes every chip for NVDA, AVGO, AMD. A beat + strong AI demand guide = structural validation. NFLX also Thu.'},
    {tag:'WATCH',    tagCls:'evt-watch', headline:'AVGO $400 Holding Below SMA50 $406 &mdash; Consolidation Zone', body:'AVGO rallied from $360 to $401 (+11%) then consolidated around $400. SMA50 $406 is flattening (was $409, now $406). If AVGO reclaims $406 with SMA50 turning, this re-enters setup territory. A strong TSM print Thursday could be the catalyst. For now: monitor, no action.'},
    {tag:'WATCH',    tagCls:'evt-watch', headline:'MSFT $385 &mdash; Gap to Zone $393 Narrowing &mdash; SMA50 $404 Falling', body:'MSFT inched up to $385 from $384. Zone bottom $393 is $8 away. SMA50 $404 continues falling (was $405). MSFT needs a catalyst to close the gap &mdash; Azure earnings late July could be it. Monitor.'},
    {tag:'RISK',     tagCls:'evt-geo',   headline:'MRVL $235.67 &mdash; Trail Stop Has Now Saved 23% of Additional Downside', body:'MRVL dropped from $243 to $236 this week, now $54 below the $290 trail stop. From the stop level, the trail has avoided 18.7% more downside ($290 &rarr; $236). The stop continues to validate as the framework\'s best rule. MRVL SMA50 $231 is still below price, but the stock is in freefall. No re-entry until clear basing pattern.'},
  ],
  portfolio: [
    {ticker:'NOW',  cls:'pi-green',   impact:'IN ZONE + SMA CONFIRMED &#10003;', note:'$107.69. Zone $103&ndash;118. SMA50 $102 RISING, price above. R/R 3.4:1. Only confirmed setup. Full stack inverted (early recovery) &mdash; lower conviction than a full bullish stack.'},
    {ticker:'NVDA', cls:'pi-green',   impact:'RECLAIMED SMA50 &#9650;',          note:'$210.96. Above SMA50 $209 for first time since rotation. Stack bullish (50>100>200). NOT in zone &mdash; $19 above zone top $192. Trend signal, not entry signal.'},
    {ticker:'AVGO', cls:'pi-yellow',  impact:'CONSOLIDATING $400 &#9654;',       note:'$399.99. Above zone $375. SMA50 $406 (flattening). Needs $406 reclaim + TSM catalyst. Monitor.'},
    {ticker:'VRT',  cls:'pi-yellow',  impact:'PULLBACK FROM BOUNCE &mdash; $319 &#9660;', note:'$318.87. Above zone $312. SMA50 $325 (falling). Gave back some gains.'},
    {ticker:'MSFT', cls:'pi-yellow',  impact:'BELOW ZONE &mdash; $385 &#9660;',  note:'$385.09. Zone $393&ndash;412. $8 below zone. SMA50 $404 falling. Needs catalyst.'},
    {ticker:'ANET', cls:'pi-yellow',  impact:'EXTENDED &mdash; $187 &#9650;',    note:'$187.00. +16% from last week. Well above zone $128&ndash;148. No chase.'},
    {ticker:'AMD',  cls:'pi-yellow',  impact:'EXTENDED &mdash; $558 &#9650;',    note:'$557.99. +7.8% WoW. Still $170 above zone $370&ndash;390. MI400 Q3 catalyst.'},
    {ticker:'DELL', cls:'pi-yellow',  impact:'GAVE BACK &minus;3.4% &mdash; $435 &#9660;', note:'$434.83. Pulled back from $450 bounce high. Above zone $310&ndash;355.'},
    {ticker:'PLTR', cls:'pi-yellow',  impact:'FADING &mdash; $127 &#9660;',      note:'$126.79. Gave back rally gains. Below SMA50. Not confirming.'},
    {ticker:'PANW', cls:'pi-yellow',  impact:'DROPPED &minus;3.7% &mdash; $326 &#9660;', note:'$325.91. Notable pullback from $338. Still above zone $232&ndash;252.'},
    {ticker:'LMND', cls:'pi-yellow',  impact:'FLAT &mdash; $70 &#9654;',         note:'$70.47. Above zone $45&ndash;56. No chase.'},
    {ticker:'ORCL', cls:'pi-yellow',  impact:'EX-DIV &mdash; $141 &#9660;',      note:'$140.69. Went ex-dividend. Below $148 stop. Dead setup.'},
    {ticker:'MRVL', cls:'pi-red',     impact:'FREEFALL &mdash; $236 &#9888;',    note:'$235.67. Down 18.7% from $290 stop. Trail saved 23% more downside. No re-entry.'},
  ],
  macro_watch: [
    '🎯 ONE CONFIRMED SETUP: NOW $107.69 is the only name passing both gates (zone $103&ndash;118 + rising SMA50 $102). All other names either exited zones (AVGO, VRT) or have falling SMA50s (MSFT, AVGO). The framework narrowed from two candidates last week to one confirmed setup.',
    '📊 NVDA SMA50 RECLAIM: NVDA $211 closed above SMA50 $209 with a bullish stack (50>100>200). This is the strongest trend signal on the board &mdash; but NVDA is $19 above its zone ($175&ndash;192), so no entry. The reclaim validates that the tech bounce is real, not just a dead-cat. Watch for $209 to hold as support.',
    '🏦 BANK EARNINGS MON JUL 14: JPM ($5.52), BAC ($1.12), WFC ($1.74), C ($2.72), GS ($14.01). Strong bank earnings = credit confidence, risk-on extends, SPY pushes to ATH $760. Weak results = rotation risk. Banks set the tone for earnings season.',
    '🔬 TSM EARNINGS THU JUL 16: TSMC est. rev $40B, EPS $3.77. This is THE print for the AI thesis. TSMC manufactures chips for NVDA, AVGO, AMD &mdash; every name on the watchlist. Strong AI demand commentary + upside guide = structural bull case confirmed. Watch for AVGO $406 breakout if TSM beats.',
    '📈 SPY $754.95 &mdash; NEW CLOSING HIGH: SPY closed at its highest level ever, just $5 below the intraday ATH $760. Broad market is bullish. This is the environment where pullbacks get bought &mdash; the tech rotation two weeks ago was exactly that.',
    '⚠️ SMA GATE COST TRACKER: AVGO rallied +11% from the POTW zone entry level without us (SMA gate blocked). VRT rallied +8% without us. The gate also blocked ORCL (which fell through its zone &minus;30%) and would have blocked MRVL (which hit its stop &minus;19%). Net: the gate has prevented 2 losers and missed 2 winners. Break-even on count, positive on magnitude (losses avoided > gains missed).',
    '📉 MRVL TRAIL STOP UPDATE: $290 stop &rarr; $236 current = $54/share of avoided loss (18.7%). From peak $311, holding without the trail would mean &minus;24% drawdown and counting. Most validated rule in the framework.',
  ],
  weekly: {
    week: 'Jul 7 &ndash; Jul 10, 2026',
    updated: 'Fri Jul 10 close (Live Robinhood + FMP data)',
    headline: 'SPY New High &mdash; NVDA Reclaims SMA50 &mdash; NOW Only Confirmed Setup &mdash; MRVL Freefall Continues',
    week_chg: [
      {name:'SPY',       open:'$751.71', close:'$754.95', chg:'+0.43% &mdash; new closing high', dir:'up'},
      {name:'QQQ',       open:'$723.28', close:'$725.51', chg:'+0.31% &mdash; holding gains',    dir:'up'},
      {name:'NVDA',      open:'$202.78', close:'$210.96', chg:'+4.0% &mdash; SMA50 reclaim',     dir:'up'},
      {name:'AVGO',      open:'$401.11', close:'$399.99', chg:'&minus;0.3% &mdash; consolidating', dir:'down'},
      {name:'MRVL',      open:'$243.27', close:'$235.67', chg:'&minus;3.1% &mdash; freefall',     dir:'down'},
    ],
    potw: {
      ticker:'AVGO', type:'Zone Entry Watch &mdash; SMA GATE BLOCKED',
      entry:'Zone $350&ndash;375 (entered at $360 Jul 2)', exit:'$400 Jul 10 &mdash; above zone, SMA50 still falling',
      high:'$407.52 intraday Jul 9', pnl:'+11.3% from zone entry level (not entered)',
      verdict:'GATE BLOCKED &mdash; ZONES CLEARED', verdictCls:'wr-miss',
      note:'AVGO was POTW at $360 in zone $350&ndash;375. SMA gate correctly identified SMA50 $409 was falling. Price rallied +11% to $401 without entry. Now consolidating at $400, SMA50 $406 flattening. The gate sacrificed a winner to protect framework integrity. If SMA50 turns up and AVGO re-enters or holds near zone, setup may return. TSM earnings Thu could catalyze.',
    },
    missed: {
      setup:'NOW $108 emerged as the only confirmed setup: in zone $103&ndash;118 with rising SMA50 $102. NVDA reclaimed SMA50 but is above zone.',
      trade:'NOW is the sole actionable play. R/R 3.4:1 at $108, stop $88, target $175. Q2 earnings upcoming. SMA stack inverted (early recovery) tempers conviction.',
      result:'Framework narrowed from two zone candidates (AVGO, VRT) to one confirmed setup (NOW). Quality over quantity.',
    },
    lessons: [
      {tag:'SMA GATE',   cls:'lsn-rule',  text:'SMA gate blocked AVGO (+11%) and VRT (+8%). Also blocked ORCL (&minus;30% through zone) and MRVL (trail stop &minus;19%). Net positive: losses avoided exceed gains missed. Framework integrity holds.'},
      {tag:'NVDA',       cls:'lsn-macro', text:'NVDA reclaiming SMA50 with bullish stack (50>100>200) is the strongest trend confirmation signal. Validates that the 2-week tech bounce is structural, not a dead cat.'},
      {tag:'NOW',        cls:'lsn-next',  text:'NOW is the only confirmed setup: zone + rising SMA50. Full stack inverted (early recovery) &mdash; lower conviction than a full bullish stack but the SMA50 turn is the key filter that PLTR failed.'},
      {tag:'TRAIL',      cls:'lsn-rule',  text:'MRVL trail stop has now avoided 18.7% additional downside ($290 &rarr; $236). From peak $311, the untrailed drawdown would be &minus;24%. Best-performing rule in the framework.'},
    ],
    eow: [
      {ticker:'NOW',  price:'$107.69', sCls:'eow-green',  status:'ZONE + SMA &#10003;',         note:'Only confirmed setup. R/R 3.4:1'},
      {ticker:'NVDA', price:'$210.96', sCls:'eow-green',  status:'SMA50 RECLAIMED &#9650;',     note:'Above $209. Bullish stack. Not in zone'},
      {ticker:'AVGO', price:'$399.99', sCls:'eow-yellow', status:'CONSOLIDATING &#9654;',       note:'$400. SMA50 $406 flattening'},
      {ticker:'ANET', price:'$187.00', sCls:'eow-yellow', status:'EXTENDED +16% &#9650;',       note:'Well above zone $128&ndash;148'},
      {ticker:'AMD',  price:'$557.99', sCls:'eow-yellow', status:'EXTENDED +8% &#9650;',        note:'$170 above zone $370&ndash;390'},
      {ticker:'VRT',  price:'$318.87', sCls:'eow-yellow', status:'PULLBACK &#9660;',            note:'Above zone. SMA50 $325 falling'},
      {ticker:'MSFT', price:'$385.09', sCls:'eow-yellow', status:'BELOW ZONE &#9660;',          note:'$8 below zone $393. SMA50 $404'},
      {ticker:'DELL', price:'$434.83', sCls:'eow-yellow', status:'GAVE BACK &minus;3.4% &#9660;', note:'Above zone $310&ndash;355'},
      {ticker:'PLTR', price:'$126.79', sCls:'eow-yellow', status:'FADING &#9660;',              note:'Below SMA50. Not confirming'},
      {ticker:'PANW', price:'$325.91', sCls:'eow-yellow', status:'DROPPED &minus;3.7% &#9660;', note:'Above zone $232&ndash;252'},
      {ticker:'LMND', price:'$70.47',  sCls:'eow-yellow', status:'FLAT &#9654;',                note:'Above zone $45&ndash;56'},
      {ticker:'ORCL', price:'$140.69', sCls:'eow-yellow', status:'EX-DIV &#9660;',              note:'Below $148 stop. Dead'},
      {ticker:'MRVL', price:'$235.67', sCls:'eow-red',    status:'FREEFALL &#9888;',            note:'&minus;18.7% from stop. Trail validated'},
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
