#!/usr/bin/env python3
"""Update MARKET_PULSE with Jul 9 close data — tech bounce week."""
import re, sys, shutil

FILE = 'templates/index.html'
shutil.copy(FILE, FILE + '.bak')
src = open(FILE, 'r').read()

NEW_PULSE = r"""const MARKET_PULSE = {
  date: 'July 10, 2026',
  updated: 'Call Up &mdash; Jul 9 Close (Live Robinhood + FMP Data)',
  headline: 'Tech Snapback &mdash; AVGO +11% to $401 (ABOVE zone) &mdash; VRT +8% to $324 (ABOVE zone) &mdash; ANET +15% &mdash; SMA50 Falling on All Three &mdash; Bank Earnings Mon',
  sentiment: 'BOUNCE &mdash; ZONES CLEARED &mdash; SMA FILTERS HELD',
  sentimentCls: 'mkt-caution',
  indices: [
    {name:'SPY',        val:'$751.71', chg:'+0.85% &mdash; near ATH $760',       dir:'up'},
    {name:'QQQ',        val:'$723.28', chg:'+1.66% &mdash; tech bounce',          dir:'up'},
    {name:'IWM',        val:'$297.24', chg:'+1.28% &mdash; small caps strong',    dir:'up'},
    {name:'DIA',        val:'$524.19', chg:'+0.27% &mdash; Dow flat',             dir:'up'},
    {name:'AVGO',       val:'$401.11', chg:'+11.3% WoW &mdash; ABOVE zone $375', dir:'up'},
    {name:'VRT',        val:'$323.92', chg:'+7.8% WoW &mdash; ABOVE zone $312',  dir:'up'},
    {name:'NVDA',       val:'$202.78', chg:'+4.1% WoW &mdash; above zone top $192', dir:'up'},
    {name:'MRVL',       val:'$243.27', chg:'&minus;10.6% WoW &mdash; continued selloff', dir:'down'},
  ],
  events: [
    {tag:'SMA',      tagCls:'evt-macro', headline:'SMA50 FALLING on AVGO, VRT, NVDA &mdash; Framework Gate Held Correctly', body:'The SMA gate prevented entries last week. Result: AVGO SMA50 $406 (falling, price $401 = BELOW), VRT SMA50 $324 (falling, price $324 = AT), NVDA SMA50 $209 (falling, price $203 = BELOW). All three names rallied +8-11% but remain below their declining SMA50s. The gate was RIGHT to block entries &mdash; these bounces happened from below the trend filter, not from confirmed uptrends. A falling SMA50 bounce is a relief rally, not a trend resumption. Do not chase.'},
    {tag:'AVGO',     tagCls:'evt-watch', headline:'AVGO $401.11 &mdash; ABOVE Zone $350&ndash;375 &mdash; +11% from POTW Level', body:'AVGO ripped from $360 (Jul 2 POTW level) to $401 in one week (+11.3%). Now ABOVE the zone top $375. SMA stack: SMA50 $406 (falling) > SMA100 $375 > SMA150 $366 > SMA200 $362. The stack ORDER is bullish (50>100>150>200) but SMA50 is declining and price is $5 below it. If AVGO reclaims $406 with SMA50 flattening, the trend is re-establishing. Until then, this is a bounce within a pullback, not a confirmed entry. Stop $328 still valid if re-entered.'},
    {tag:'EARN',     tagCls:'evt-macro', headline:'Bank Earnings Mon Jul 14 &mdash; JPM, BAC, WFC, C, GS', body:'All five major banks report Monday. Strong results = risk-on, helps tech bounce extend. Weak results = credit fears, rotation risk. TSM reports Thu Jul 16 &mdash; the most important for AI thesis (TSMC makes every AI chip). NFLX also Jul 16. No watchlist names report this week but TSM is the upstream bellwether for NVDA/AVGO/AMD.'},
    {tag:'WATCH',    tagCls:'evt-watch', headline:'ANET $184.69 (+15.4% WoW) &amp; DELL $450.22 (+14.2% WoW) &mdash; Massive Rallies', body:'ANET and DELL posted the biggest moves on the board. ANET $184 is well above zone $128&ndash;148. DELL $450 is far above zone $310&ndash;355. Both are extended &mdash; no framework entry. But the magnitude confirms: the tech rotation was a dip-buy event, not a trend change. Institutional money rotated back into AI infrastructure aggressively.'},
    {tag:'ZONE',     tagCls:'evt-watch', headline:'NOW $108.84 &mdash; Only Name Still IN ZONE $103&ndash;118', body:'ServiceNow is the only watchlist name still inside its buy zone. At $108.84: stop $88, target $175, R/R 3.2:1 (passes 2.5:1 gate). MSFT SMA50 $404 (falling, same issue). Need to check NOW SMA50 before any entry. If SMA50 is rising and price is above it, NOW becomes the only actionable setup on the board.'},
    {tag:'RISK',     tagCls:'evt-geo',   headline:'MRVL $243.27 &mdash; Down Another 10.6% After Stop-Out', body:'MRVL continued falling from $272 (stop-out level) to $243 this week. Now $47 below the $290 trail stop. The stop saved 17% of additional downside. MRVL SMA50 is $230 &mdash; price is above SMA50, which could indicate a base forming. But the damage is significant. Monitor only &mdash; not actionable until clear base + volume confirmation.'},
  ],
  portfolio: [
    {ticker:'AVGO', cls:'pi-yellow',  impact:'ABOVE ZONE &mdash; $401 &#9650;', note:'$401.11. Was in zone last week at $360. Rallied +11.3%. Now above zone top $375. SMA50 $406 (falling, price below). Stack order bullish but SMA50 declining. Watch for $406 reclaim.'},
    {ticker:'VRT',  cls:'pi-yellow',  impact:'ABOVE ZONE &mdash; $324 &#9650;', note:'$323.92. Was in zone last week at $300. Rallied +7.8%. Now above zone top $312. At SMA50 $324 (falling). Same SMA gate issue as AVGO.'},
    {ticker:'NOW',  cls:'pi-green',   impact:'IN ZONE &mdash; $108 &#10003;',   note:'$108.84. Zone $103&ndash;118. R/R 3.2:1. Only name still in zone. SMA check needed before entry.'},
    {ticker:'NVDA', cls:'pi-yellow',  impact:'ABOVE ZONE TOP $192 &#9650;',     note:'$202.78. Bounced +4.1% from $194. Above zone top $192. SMA50 $209 (falling). Not in zone. Monitor.'},
    {ticker:'MSFT', cls:'pi-yellow',  impact:'BELOW ZONE &mdash; $384 &#9660;', note:'$384.36. Zone $393&ndash;412. SMA50 $404 (falling). Needs $393 reclaim + SMA turn. Not actionable.'},
    {ticker:'PLTR', cls:'pi-yellow',  impact:'FLAT &mdash; $129 &#9654;',       note:'$129.04. Flat week. Still below SMA50. No change in setup status.'},
    {ticker:'ANET', cls:'pi-yellow',  impact:'RALLIED +15% &mdash; $185 &#9650;', note:'$184.69. Massive bounce. Well above zone $128&ndash;148. Extended &mdash; no entry.'},
    {ticker:'DELL', cls:'pi-yellow',  impact:'RALLIED +14% &mdash; $450 &#9650;', note:'$450.22. Massive bounce. Well above zone $310&ndash;355. Extended &mdash; no entry.'},
    {ticker:'AMD',  cls:'pi-yellow',  impact:'BOUNCED +5.6% &mdash; $547 &#9650;', note:'$546.72. Still well above zone $370&ndash;390. Needs $150 more downside to reach zone.'},
    {ticker:'PANW', cls:'pi-yellow',  impact:'FLAT &mdash; $338 &#9654;',       note:'$338.31. Above zone $232&ndash;252. Steady.'},
    {ticker:'LMND', cls:'pi-yellow',  impact:'FLAT &mdash; $70 &#9654;',        note:'$70.33. Above zone $45&ndash;56. No chase.'},
    {ticker:'MRVL', cls:'pi-red',     impact:'CONTINUED SELLOFF &mdash; $243 &#9888;', note:'$243.27. Down another 10.6% after $290 stop-out. Now $47 below stop. Trail saved 17% additional downside. Monitor only.'},
    {ticker:'ORCL', cls:'pi-yellow',  impact:'STABILIZING &mdash; $144 &#9654;', note:'$144.22. Was $140 last week. Slight bounce. Still below $148 stop. Not actionable.'},
  ],
  macro_watch: [
    '🎯 SMA GATE VINDICATED: AVGO and VRT were in zones last week but the SMA50 was falling on both. The framework said STAND DOWN. Both rallied 8-11% without us — but both remain below their declining SMA50s. A falling-SMA50 bounce is a relief rally, not a confirmed entry. The gate protected against chasing.',
    '📊 AVGO SMA STACK: SMA50 $406 > SMA100 $375 > SMA150 $366 > SMA200 $362. Stack order is BULLISH (50>100>150>200) but SMA50 is DECLINING and price ($401) is BELOW it. If price reclaims SMA50 and the 50 flattens/turns up, this becomes the strongest setup on the board. Key level: $406.',
    '📅 BANK EARNINGS MON JUL 14: JPM, BAC, WFC, C, GS all report. Strong bank earnings = risk-on momentum continues (helps tech bounce). Weak results = credit rotation risk. This is the first major earnings week of Q2 season.',
    '🔬 TSM EARNINGS THU JUL 16: TSMC is the upstream bellwether for every AI chip name on the watchlist (NVDA, AVGO, AMD, MRVL). A strong TSM report = AI capex thesis intact. Revenue estimate $40B. This is the most important earnings print for our thesis this week.',
    '⚠️ ONLY ONE ZONE ENTRY: NOW $108 is the only name still in its buy zone ($103–118). All others either rallied above zones (AVGO, VRT) or remain far from zones (AMD, DELL, ANET). The framework went from two setups to one in a week. If NOW SMA50 is rising, it becomes the sole actionable play.',
    '🚫 DO NOT CHASE THE BOUNCE: AVGO +11%, ANET +15%, DELL +14% in one week. These are relief rallies from oversold conditions, not new entries. The framework does not chase — it waits for zone + SMA confirmation. If another rotation hits, these names will pull back again. Patience.',
    '📉 MRVL TRAIL STOP SAVED 17%: MRVL dropped from $272 (stop-out) to $243 this week (−10.6% more). From the $290 stop level, that is $47 of additional downside avoided. The trail stop is now the most validated rule in the framework.',
  ],
  weekly: {
    week: 'Jul 7 &ndash; Jul 9, 2026',
    updated: 'Wed Jul 9 close (Live Robinhood + FMP data)',
    headline: 'Tech Snapback Week &mdash; AVGO +11%, ANET +15%, DELL +14% &mdash; Zones Cleared &mdash; SMA Gate Held',
    week_chg: [
      {name:'SPY',       open:'$744.80', close:'$751.71', chg:'+0.9% &mdash; near ATH',        dir:'up'},
      {name:'QQQ',       open:'$712.60', close:'$723.28', chg:'+1.5% &mdash; tech bounce',      dir:'up'},
      {name:'AVGO',      open:'$360.45', close:'$401.11', chg:'+11.3% &mdash; above zone',      dir:'up'},
      {name:'VRT',       open:'$300.53', close:'$323.92', chg:'+7.8% &mdash; above zone',       dir:'up'},
      {name:'MRVL',      open:'$272.05', close:'$243.27', chg:'&minus;10.6% &mdash; continued fall', dir:'down'},
    ],
    potw: {
      ticker:'AVGO', type:'Zone Entry Watch &mdash; ZONES CLEARED',
      entry:'Zone $350&ndash;375 (POTW at $360)', exit:'$401.11 Jul 9 &mdash; above zone',
      high:'$407.52 intraday Jul 9', pnl:'+11.3% from POTW level (not entered &mdash; SMA gate)',
      verdict:'ZONE CLEARED &mdash; NOT ENTERED', verdictCls:'wr-miss',
      note:'AVGO was the Play of the Week at $360 with zone $350&ndash;375 and R/R 5.9:1. The SMA gate said STAND DOWN (SMA50 $409 was falling, price below it). AVGO then rallied +11.3% to $401 without us. The gate prevented a +11% winner BUT it also would have prevented an ORCL-style knife. The gate is working as designed — it sacrifices some winners to protect against all losers. Framework integrity > individual trade outcome.',
    },
    missed: {
      setup:'AVGO and VRT both rallied out of their zones. The SMA gate prevented entries on both. NOW remains in zone at $108.',
      trade:'NOW $108 in zone $103–118 (R/R 3.2:1) is the only remaining setup. SMA check needed.',
      result:'Framework generated correct zone entries; SMA gate filtered them. The gate’s job is capital protection, not profit maximization.',
    },
    lessons: [
      {tag:'SMA GATE',   cls:'lsn-rule',  text:'AVGO +11% and VRT +8% rallied without us. The SMA gate blocked both. This is the cost of the filter — it sacrifices some winners to avoid all knives. ORCL proved the filter works on the downside; AVGO shows the cost on the upside. Framework integrity over individual outcomes.'},
      {tag:'BOUNCE',     cls:'lsn-macro', text:'Tech snapped back hard: AVGO +11%, ANET +15%, DELL +14%. The prior week rotation was a dip-buy event, not a trend change. Institutional money rotated back into AI infrastructure aggressively.'},
      {tag:'TRAIL',      cls:'lsn-rule',  text:'MRVL trail stop saved 17% more downside. From $290 stop to $243 close = $47/share of avoided loss. Most validated rule in the framework.'},
      {tag:'NOW',        cls:'lsn-next',  text:'NOW $108 is the only name still in its zone ($103–118). If SMA50 confirms, it becomes the sole actionable play. One setup > zero setups.'},
    ],
    eow: [
      {ticker:'AVGO', price:'$401.11', sCls:'eow-yellow', status:'ABOVE ZONE &#9650;',          note:'+11.3%. Zone cleared. SMA50 $406 falling'},
      {ticker:'VRT',  price:'$323.92', sCls:'eow-yellow', status:'ABOVE ZONE &#9650;',          note:'+7.8%. Zone cleared. At SMA50'},
      {ticker:'NOW',  price:'$108.84', sCls:'eow-green',  status:'IN ZONE &#10003;',            note:'Zone $103–118. Only zone entry left'},
      {ticker:'ANET', price:'$184.69', sCls:'eow-green',  status:'RALLIED +15% &#9650;',        note:'Massive bounce. Extended'},
      {ticker:'DELL', price:'$450.22', sCls:'eow-green',  status:'RALLIED +14% &#9650;',        note:'Massive bounce. Extended'},
      {ticker:'NVDA', price:'$202.78', sCls:'eow-yellow', status:'ABOVE ZONE TOP &#9650;',      note:'Zone $175–192. Bounced from $194'},
      {ticker:'AMD',  price:'$546.72', sCls:'eow-yellow', status:'BOUNCED +5.6% &#9650;',       note:'Still far above zone $370–390'},
      {ticker:'MSFT', price:'$384.36', sCls:'eow-yellow', status:'BELOW ZONE &#9660;',          note:'Zone $393–412. SMA50 $404 falling'},
      {ticker:'PLTR', price:'$129.04', sCls:'eow-yellow', status:'FLAT &#9654;',                note:'Below SMA50. No change'},
      {ticker:'PANW', price:'$338.31', sCls:'eow-yellow', status:'FLAT &#9654;',                note:'Above zone $232–252'},
      {ticker:'LMND', price:'$70.33',  sCls:'eow-yellow', status:'FLAT &#9654;',                note:'Above zone $45–56'},
      {ticker:'ORCL', price:'$144.22', sCls:'eow-yellow', status:'STABILIZING &#9654;',         note:'Slight bounce. Below $148 stop'},
      {ticker:'MRVL', price:'$243.27', sCls:'eow-red',    status:'CONTINUED FALL &#9888;',      note:'&minus;10.6% more. Trail saved 17%'},
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
