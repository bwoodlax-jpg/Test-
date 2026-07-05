#!/usr/bin/env python3
"""Update MARKET_PULSE in templates/index.html — Jul 7 week-ahead call-up."""
import re

SRC = 'templates/index.html'

NEW_PULSE = r"""const MARKET_PULSE = {
  date: 'July 5, 2026',
  updated: 'Week-Ahead Call Up &mdash; Jul 7&ndash;11 (Jul 2 close)',
  headline: 'AVGO $360 IN ZONE &mdash; First Entry Setup in Weeks (R/R 5.9:1) &mdash; VRT $300 IN ZONE (R/R 3.8:1) &mdash; MRVL Stopped Out &mdash; FOMC Minutes Wed &mdash; Buying Power $13.64',
  sentiment: 'ZONE ENTRIES FORMING &mdash; CONFIRM SMAs BEFORE ACTION',
  sentimentCls: 'mkt-caution',
  indices: [
    {name:'SPY',        val:'$744.80', chg:'&minus;0.3% &mdash; flat near ATH',     dir:'down'},
    {name:'QQQ',        val:'$712.60', chg:'&minus;3.2% &mdash; tech rotation',     dir:'down'},
    {name:'VIX',        val:'16.15',   chg:'&minus;1.8% &mdash; no panic',          dir:'down'},
    {name:'10Y',        val:'4.48%',   chg:'+0.06 &mdash; Warsh: inflation softening', dir:'up'},
    {name:'AVGO',       val:'$360.45', chg:'IN ZONE $350&ndash;375 &mdash; ENTRY WATCH', dir:'down'},
    {name:'VRT',        val:'$300.53', chg:'IN ZONE $290&ndash;312 &mdash; ENTRY WATCH', dir:'down'},
    {name:'MSFT',       val:'$390.49', chg:'+4.7% bounce &mdash; near zone $393',   dir:'up'},
    {name:'PLTR',       val:'$129.78', chg:'+11.2% rally &mdash; SMA reclaim?',     dir:'up'},
  ],
  events: [
    {tag:'ENTRY',    tagCls:'evt-watch', headline:'AVGO $360.45 &mdash; IN ZONE $350&ndash;375 &mdash; Play of the Week Candidate', body:'AVGO pulled back into the buy zone for the first time. At $360, stop $328, target $550: R/R = 5.9:1, well above the 2.5:1 gate. This is the cleanest setup on the board &mdash; the name we flagged last week as &ldquo;the one to watch at $375.&rdquo; CRITICAL GATE: must confirm SMA stack is bullish before any entry. Run the SMA scanner Monday. If SMA50 is rising and price is above it, this is a go. If SMA50 is falling (like PLTR was), it is another knife. Buying power $13.64 blocks execution without adding cash or using fractional shares.'},
    {tag:'ENTRY',    tagCls:'evt-watch', headline:'VRT $300.53 &mdash; IN ZONE $290&ndash;312 &mdash; Second Setup', body:'VRT dropped 10.2% from $334 into zone $290&ndash;312. At $300, stop $268, target $420: R/R = 3.8:1. AI power infrastructure thesis (liquid cooling for data centers) is structural. Same gate as AVGO: need SMA confirmation. Watch the zone floor $290 &mdash; if it breaks, this becomes another ORCL (falling through zone = dead setup). Hold above $290 + rising SMA50 = valid entry.'},
    {tag:'MACRO',    tagCls:'evt-macro', headline:'FOMC Minutes Wednesday Jul 8 &mdash; Watch for Rate Path Signals', body:'FOMC minutes from the June meeting drop Wednesday. Fed Chair Warsh already signaled &ldquo;inflation risks softening&rdquo; &mdash; dovish tilt. Markets expect rate cuts later in 2026. If minutes confirm dovish tone, tech/growth could bounce (good for AVGO/VRT zone entries). If hawkish surprise, expect continued rotation pressure. Next actual FOMC rate decision is Jul 28&ndash;29.'},
    {tag:'WATCH',    tagCls:'evt-macro', headline:'MSFT $390.49 &mdash; $3 Below Zone Bottom $393 &mdash; Bounce or Fade?', body:'MSFT bounced +4.7% from the $372 stop level to $390 &mdash; approaching zone bottom $393. Still below all SMAs (bearish stack from Jun 30 scan). The bounce is constructive but needs follow-through. If MSFT reclaims $393 this week with the SMA50 starting to flatten, it becomes a potential setup for the FOLLOWING week. No entry this week &mdash; just monitoring.'},
    {tag:'WATCH',    tagCls:'evt-watch', headline:'NVDA $194.83 &mdash; Approaching Zone Top $192 &mdash; One More Leg Down', body:'NVDA pulled back from $200 to $194, now just $3 above zone top $192. One more session of selling and it enters zone $175&ndash;192. R/R at $185: risk $30, reward $115 = 3.8:1. The biggest AI name is getting closer to a framework entry for the first time. Monitor closely this week.'},
    {tag:'RISK',     tagCls:'evt-geo',   headline:'MRVL $272.05 &mdash; Stopped Out Last Week &mdash; Remove from Active Book', body:'MRVL broke the $290 trail stop, closing at $272 Jul 2 (&minus;8.7%). The only bullish-stack name is out. Trail stop did its job &mdash; forced a disciplined exit. MRVL moves to the monitor list. Re-evaluate only after price stabilizes above $280 and the SMA stack re-confirms bullish (50 > 100 > 150 > 200, all rising). Not actionable this week.'},
  ],
  portfolio: [
    {ticker:'ACCOUNT', cls:'pi-red',    impact:'BUYING POWER $13.64 &#9888;',   note:'Margin acct ••8092: total ~$1,205. Two names are in zones (AVGO, VRT) but $13.64 cash blocks all entries. Priority this week: add capital or set up fractional share trading if you want to act on these setups. The framework is generating signals; execution requires funding.'},
    {ticker:'QCML',  cls:'pi-red',    impact:'REAL POSITION &mdash; DOWN ~7% &#9660;', note:'55 shares @ $21.37 avg. Still the actual equity holding. No stop defined &mdash; SET ONE. Not on the AI watchlist.'},
    {ticker:'AVGO', cls:'pi-green',   impact:'IN ZONE &mdash; ENTRY WATCH &#10003;', note:'$360.45. Zone $350&ndash;375, stop $328, target $550. R/R 5.9:1. Gate: confirm SMA stack Monday. If bullish, this is the #1 setup. Paper without added capital.'},
    {ticker:'VRT',  cls:'pi-green',   impact:'IN ZONE &mdash; ENTRY WATCH &#10003;', note:'$300.53. Zone $290&ndash;312, stop $268, target $420. R/R 3.8:1. Gate: SMA stack + $290 floor must hold. Paper without added capital.'},
    {ticker:'MSFT', cls:'pi-yellow',  impact:'NEAR ZONE &mdash; MONITOR &#9650;', note:'$390.49. $3 below zone $393&ndash;412. Bounced from $372 stop. Bearish SMA stack still. Watch for zone reclaim + SMA50 turn. Not actionable this week.'},
    {ticker:'PLTR', cls:'pi-yellow',  impact:'RALLIED +11% &mdash; SMA CHECK &#9650;', note:'$129.78. Was falling knife at $116. Rally is notable but SMA50 was $136 &mdash; likely still above price. Need fresh SMA scan to evaluate. No entry until confirmed.'},
    {ticker:'NOW',  cls:'pi-yellow',  impact:'RECLAIMED $103 FLOOR &#9650;', note:'$105.88. Back above zone floor $103. Zone $103&ndash;118, stop $88, target $165. Watch for sustained hold. R/R 2.7:1 at $105 &mdash; barely passes gate.'},
    {ticker:'NVDA', cls:'pi-yellow',  impact:'APPROACHING ZONE TOP $192 &#9660;',   note:'$194.83. One more down day enters zone $175&ndash;192. R/R 3.8:1 at $185. Monitor closely.'},
    {ticker:'AMD',  cls:'pi-yellow',  impact:'PULLED BACK &minus;11% TO $517 &#9660;', note:'$517.82. Still +33% above zone $370&ndash;390. Getting closer but needs another $130 down to reach zone. MI400 Q3 2026.'},
    {ticker:'DELL', cls:'pi-yellow',  impact:'PULLED BACK &minus;9% TO $394 &#9660;', note:'$394.32. Approaching zone top $355. Needs another $40 down. Monitor.'},
    {ticker:'PANW', cls:'pi-green',   impact:'RESILIENT &mdash; $349 &#9650;',     note:'$349.68. Up 2.5% while rest of tech dropped. Above zone $232&ndash;252. Strongest relative strength on the board.'},
    {ticker:'ANET', cls:'pi-yellow',  impact:'DROPPED 6% &mdash; $159 &#9660;', note:'$159.99. Above zone $128&ndash;148. Monitor.'},
    {ticker:'LMND', cls:'pi-yellow',  impact:'ABOVE ZONE &mdash; $71 &#9650;',  note:'~$71.70. Above zone $45&ndash;56. No chase.'},
    {ticker:'MRVL', cls:'pi-red',     impact:'STOPPED OUT &mdash; $272 &#9888;', note:'$272.05. Broke $290 trail. Moved to monitor list. Re-evaluate after $280+ base + SMA re-confirm.'},
    {ticker:'ORCL', cls:'pi-red',     impact:'STILL FALLING &mdash; $141 &#9888;', note:'~$141. Below $148 stop. Setup dead. No action until base + reclaim $150.'},
  ],
  macro_watch: [
    '🎯 WEEK AHEAD PLAYBOOK: Two names in zones (AVGO $360, VRT $300). One approaching (NVDA $194, zone top $192). FOMC minutes Wednesday. SMA scanner must run Monday before any entry decisions. The framework is generating pullback-to-zone setups for the first time in weeks &mdash; confirm trend filters before acting.',
    '📊 SMA SCANNER CRITICAL: AVGO and VRT zone entries REQUIRE SMA stack confirmation. Learned from PLTR: being in-zone means nothing if the SMA50 is falling. Run the scanner when Robinhood MCP reconnects or manually via the SMA Stack tab with a Finnhub key. DO NOT enter without this check.',
    '💵 CAPITAL CONSTRAINT: $13.64 buying power. AVGO is $360/share, VRT is $300. Even fractional shares need more capital. If you want to act on these setups, add funds this week. Otherwise the analysis is correct but the execution is paper.',
    '📉 FOMC MINUTES (Wed Jul 8): June meeting minutes release. Warsh already said &ldquo;inflation softening&rdquo; &mdash; dovish. If minutes confirm, expect growth/tech relief rally (helps zone entries). If hawkish surprise, more rotation pressure (entries may cheapen further). Rate decision Jul 28&ndash;29.',
    '🔄 ROTATION CONTEXT: QQQ &minus;3.2% while SPY flat = tech-to-value rotation. Extended names (MRVL, AMD, DELL, VRT) sold off; beaten-down names (MSFT +4.7%, PLTR +11%, NOW +6.6%) bounced. The zone framework is designed for pullbacks in uptrends &mdash; this is the first time the right names are arriving at the right levels.',
    '⚠️ ORCL LESSON APPLIES: ORCL fell INTO its zone and kept falling through the stop. AVGO and VRT are now in their zones. The difference: ORCL had a falling SMA50 (trend filter vetoed). AVGO/VRT need RISING SMA50s to confirm. If their SMA50s are falling, they are ORCL repeats. The filter is the only thing separating a value entry from a falling knife.',
    '📅 EARNINGS: No watchlist names report this week. Light calendar &mdash; PEP (Jul 9) is the marquee name. AVGO reported Jun 3 (beat), next Sep 3. MRVL reported May 27. AMD earnings expected late July. NVDA late Aug.',
    '🚫 MRVL EXIT: $290 trail stop worked. Price dropped 8.7% to $272 in one week. Without the trail, the drawdown from peak ($311) would be &minus;12.5% and counting. The stop forced the discipline the framework demands. MRVL moves to the monitor list; re-enter only on SMA re-confirmation above $280.',
  ],
  weekly: {
    week: 'Jun 30 &ndash; Jul 3, 2026',
    updated: 'Fri Jul 4 &middot; Holiday (Jul 2 close, web data)',
    headline: 'Tech Rotation Week &mdash; MRVL Stopped Out, AVGO &amp; VRT Enter Zones, QQQ &minus;3.2%, MSFT/PLTR Bounce',
    week_chg: [
      {name:'SPY',       open:'$746.77', close:'$744.80', chg:'&minus;0.3% &mdash; flat',         dir:'down'},
      {name:'QQQ',       open:'$736.40', close:'$712.60', chg:'&minus;3.2% &mdash; tech rotation', dir:'down'},
      {name:'10Y Yield', open:'4.42%',   close:'4.48%',   chg:'+0.06 &mdash; Warsh dovish',       dir:'up'},
      {name:'VIX',       open:'16.45',   close:'16.15',   chg:'&minus;1.8% &mdash; calm',          dir:'down'},
      {name:'MRVL',      open:'$297.89', close:'$272.05', chg:'&minus;8.7% &mdash; STOP BLOWN',   dir:'down'},
    ],
    potw: {
      ticker:'MRVL', type:'Hold &amp; Trail (Primary) &mdash; STOPPED OUT',
      entry:'Trail stop $290', exit:'Closed $272.05 Jul 2 &mdash; $18 below stop',
      high:'$297.89 Jun 30', pnl:'Trail stop triggered at $290',
      verdict:'STOPPED OUT', verdictCls:'wr-loss',
      note:'MRVL was the only bullish-stack name and the entire active playbook. The $290 trail stop was set after the post-inclusion fade from $311. Price dropped 8.7% in the tech rotation (QQQ &minus;3.2%), closing at $272.05 &mdash; $18 below the $290 stop. The trail did its job: it defined risk and forced a disciplined exit.',
    },
    missed: {
      setup:'AVGO and VRT pulled into their buy zones while MRVL and AMD sold off. The rotation created new entry setups exactly where the framework wants them.',
      trade:'AVGO $360 in zone $350&ndash;375 (R/R 5.9:1) and VRT $300 in zone $290&ndash;312 (R/R 3.8:1) are the first actionable setups in weeks. Both require SMA confirmation and capital.',
      result:'Framework generating signals; execution blocked by $13.64 buying power.',
    },
    lessons: [
      {tag:'STOP',      cls:'lsn-rule',  text:'MRVL $290 trail stop worked as designed. Forced exit at $290 while price continued to $272. Without it, holding through a &minus;12.5% drawdown from peak.'},
      {tag:'ROTATION',  cls:'lsn-macro', text:'QQQ &minus;3.2% while SPY flat = classic tech rotation. Extended names sold off, beaten-down names bounced. The zone framework is built for this environment.'},
      {tag:'ZONES',     cls:'lsn-next',  text:'Two names entered zones: AVGO $360 (R/R 5.9:1) and VRT $300 (R/R 3.8:1). Both pass the R/R gate but REQUIRE SMA confirmation &mdash; learned from PLTR.'},
      {tag:'CAPITAL',   cls:'lsn-rule',  text:'Framework is working &mdash; ORCL knife avoided, MRVL trail honored, AVGO/VRT zones arrived. But $13.64 buying power means every signal is paper.'},
    ],
    eow: [
      {ticker:'AVGO', price:'$360.45', sCls:'eow-green',  status:'IN ZONE &#10003;',           note:'Zone $350&ndash;375. R/R 5.9:1. First setup'},
      {ticker:'VRT',  price:'$300.53', sCls:'eow-green',  status:'IN ZONE &#10003;',           note:'Zone $290&ndash;312. R/R 3.8:1'},
      {ticker:'NOW',  price:'$105.88', sCls:'eow-green',  status:'RECLAIMED $103 &#9650;',     note:'Above zone floor. Recovering'},
      {ticker:'PANW', price:'$349.68', sCls:'eow-green',  status:'HELD &mdash; RESILIENT &#9650;', note:'Above zone. Up 2.5%'},
      {ticker:'MSFT', price:'$390.49', sCls:'eow-yellow', status:'BOUNCED &#9650;',            note:'$3 below zone $393. Bearish SMAs'},
      {ticker:'PLTR', price:'$129.78', sCls:'eow-yellow', status:'RALLIED +11% &#9650;',      note:'Need SMA50 re-check ($136)'},
      {ticker:'NVDA', price:'$194.83', sCls:'eow-yellow', status:'NEAR ZONE TOP &#9660;',     note:'Zone $175&ndash;192. Approaching'},
      {ticker:'LMND', price:'$71.70',  sCls:'eow-yellow', status:'ABOVE ZONE &#9650;',        note:'Zone $45&ndash;56. No chase'},
      {ticker:'AMD',  price:'$517.82', sCls:'eow-yellow', status:'PULLED BACK &minus;11% &#9660;', note:'Still +33% above zone $390'},
      {ticker:'DELL', price:'$394.32', sCls:'eow-yellow', status:'PULLED BACK &minus;9% &#9660;',  note:'Approaching zone top $355'},
      {ticker:'ANET', price:'$159.99', sCls:'eow-yellow', status:'DROPPED 6% &#9660;',        note:'Above zone $128&ndash;148'},
      {ticker:'MRVL', price:'$272.05', sCls:'eow-red',    status:'STOP BLOWN &#9888;',        note:'Broke $290 trail. Exit triggered'},
      {ticker:'ORCL', price:'$141.01', sCls:'eow-red',    status:'STILL FALLING &#9888;',     note:'Below $148 stop. Dead'},
    ],
  },
};"""

with open(SRC) as f:
    html = f.read()

pattern = r'const MARKET_PULSE = \{.*?\n\};'
match = re.search(pattern, html, re.DOTALL)
if not match:
    raise RuntimeError("Could not find MARKET_PULSE block")

print(f"Found MARKET_PULSE at lines {html[:match.start()].count(chr(10))+1}-{html[:match.end()].count(chr(10))+1}")
html_new = html[:match.start()] + NEW_PULSE + html[match.end():]

with open(SRC, 'w') as f:
    f.write(html_new)

print(f"Updated MARKET_PULSE: {len(NEW_PULSE)} chars")
print("Done")
