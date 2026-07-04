#!/usr/bin/env python3
"""Update MARKET_PULSE in templates/index.html with Jul 2 close data."""
import re, shutil

SRC = 'templates/index.html'

NEW_PULSE = r"""const MARKET_PULSE = {
  date: 'July 4, 2026',
  updated: 'Holiday Update &mdash; Fri Jul 4 (Jul 2 close, web-sourced data)',
  headline: 'ROTATION WEEK &mdash; MRVL $272 BROKE $290 TRAIL STOP (exit) &mdash; AVGO $360 FELL INTO ZONE $350&ndash;375 (watch) &mdash; VRT $300 IN ZONE $290&ndash;312 (watch) &mdash; QQQ &minus;3.2% tech selloff &mdash; Buying power $13.64',
  sentiment: 'ROTATION &mdash; DEFENSE + NEW SETUPS',
  sentimentCls: 'mkt-caution',
  indices: [
    {name:'SPY',        val:'$744.80', chg:'&minus;0.3% &mdash; flat near ATH',     dir:'down'},
    {name:'QQQ',        val:'$712.60', chg:'&minus;3.2% &mdash; tech rotation',     dir:'down'},
    {name:'VIX',        val:'16.15',   chg:'&minus;1.8% &mdash; still calm',        dir:'down'},
    {name:'10Y',        val:'4.48%',   chg:'+0.06 &mdash; Warsh: inflation softening', dir:'up'},
    {name:'MRVL',       val:'$272.05', chg:'&minus;8.7% BROKE $290 stop &mdash; EXIT', dir:'down'},
    {name:'AVGO',       val:'$360.45', chg:'IN ZONE $350&ndash;375 &mdash; WATCH',  dir:'down'},
    {name:'VRT',        val:'$300.53', chg:'IN ZONE $290&ndash;312 &mdash; WATCH',  dir:'down'},
    {name:'PLTR',       val:'$129.78', chg:'+11.2% rally &mdash; reclaiming SMAs?', dir:'up'},
  ],
  events: [
    {tag:'RISK',     tagCls:'evt-geo',   headline:'MRVL $272.05 &mdash; BROKE $290 TRAIL STOP &mdash; Exit Signal Triggered', body:'MRVL closed $272.05 Jul 2, down 8.7% from $297.89 Jun 30. The $290 trail stop is blown by $18. The only bullish-stack name on the board is now a casualty of the broader tech rotation (QQQ &minus;3.2%). The all-time high was $316 on Jun 4; price has now retraced 14% from peak. If the trail stop was set, exit was triggered. If not, close the position. The SMA50 ($216) is still well below, so a base could form, but the trend has broken. Re-evaluate only after price stabilizes above $280+ and the SMA stack is re-confirmed.'},
    {tag:'ENTRY',    tagCls:'evt-watch', headline:'AVGO $360.45 &mdash; FELL INTO ZONE $350&ndash;375 &mdash; First Entry Setup in Weeks', body:'AVGO closed $360.45 Jul 2, down from $377.75 Jun 30. It has pulled back INTO the buy zone ($350&ndash;375) that we flagged as the one to watch. This is the first clean pullback-to-zone on the board. Stop $328, target $550. R/R at $360: risk $32, reward $190 = 5.9:1 &mdash; well above the 2.5:1 gate. CRITICAL: before entering, confirm the SMA stack is bullish (need price above rising SMA50). With buying power at $13.64, this is paper unless cash is added or fractional shares are used.'},
    {tag:'ENTRY',    tagCls:'evt-watch', headline:'VRT $300.53 &mdash; FELL INTO ZONE $290&ndash;312 &mdash; Second Potential Entry Setup', body:'VRT dropped 10.2% from $334.82 to $300.53 Jul 2, falling into the buy zone $290&ndash;312. Stop $268, target $420. R/R at $300: risk $32, reward $120 = 3.8:1 &mdash; passes the 2.5:1 gate. Like AVGO, need to confirm SMA stack before entry. AI power infrastructure thesis (liquid cooling for data centers) remains intact. Watch for a hold at $290 zone floor; if it falls through, setup invalidates like ORCL did.'},
    {tag:'WATCH',    tagCls:'evt-macro', headline:'MSFT $390.49 &mdash; Bounced +4.7% From $372 Stop &mdash; Approaching Zone Bottom $393', body:'MSFT rallied from $373.02 to $390.49 Jul 2 &mdash; a sharp bounce off the $372 stop level. Now $3 below the zone bottom ($393). Still below all SMAs (bearish stack), so the zone is still stale from a trend-filter perspective. But the bounce shows the $372 stop held as support. Watch for a sustained move above $393 + SMA50 flattening before considering any entry. Stand-down remains correct until trend improves.'},
    {tag:'WATCH',    tagCls:'evt-watch', headline:'PLTR $129.78 &mdash; Rallied +11.2% From $116 Knife &mdash; SMA50 Reclaim?', body:'PLTR rallied hard from $116.67 to $129.78 Jul 2. Was a &ldquo;falling knife&rdquo; last week (below all SMAs, SMA50 falling). The $13 bounce is notable but needs follow-through. Key question: has it reclaimed the SMA50 ($136 last measured)? If SMA50 is still above $130, the trend filter still vetoes entry. Need to re-run the SMA scanner to confirm. The zone $108&ndash;122 is now below price again.'},
    {tag:'MACRO',    tagCls:'evt-macro', headline:'QQQ &minus;3.2% &mdash; Tech Rotation, Not Broad Risk-Off &mdash; SPY Flat Near ATH', body:'QQQ dropped 3.2% ($736&rarr;$712) while SPY was roughly flat ($746&rarr;$744). Classic sector rotation out of tech/AI into other sectors. VIX at 16.15 shows no panic. Fed Chair Warsh noted &ldquo;inflation risks softening&rdquo; &mdash; dovish signal. 10Y rose to 4.48%. The rotation is bringing extended names (AMD, DELL, MRVL, VRT) back toward zones while lifting beaten-down names (MSFT, PLTR, NOW). This is exactly the environment the zone framework is built for.'},
  ],
  portfolio: [
    {ticker:'ACCOUNT', cls:'pi-red',    impact:'BUYING POWER $13.64 &#9888;',   note:'Margin acct ••8092: total ~$1,205. Buying power $13.64 &mdash; NONE of the $100&ndash;500 watchlist names is buyable. AVGO and VRT are pulling into zones but entries require adding cash or using fractional shares. The board is paper until capital is added.'},
    {ticker:'QCML',  cls:'pi-red',    impact:'REAL POSITION &mdash; DOWN ~7% &#9660;', note:'55 shares @ $21.37 avg. Still the actual equity holding. No stop defined &mdash; SET ONE. Not on the AI watchlist.'},
    {ticker:'OPTIONS', cls:'pi-red',  impact:'SOFI/CLOV EXPIRED Jul 2 &#9888;', note:'SOFI x15 and CLOV x12 expired Jul 2 worthless as expected. KWEB x4 (exp Jul 17) remains, mark ~$0.01. Accept the loss.'},
    {ticker:'MRVL', cls:'pi-red',     impact:'BROKE $290 STOP &mdash; EXIT &#9888;', note:'$272.05 Jul 2 (from $297.89 Jun 30). Dropped 8.7%, blew through $290 trail by $18. If trail stop was set, exit triggered. If not, close position NOW. Was the only bullish stack; now broken. Re-evaluate after price stabilizes above $280+ and SMA stack re-confirms.'},
    {ticker:'AVGO', cls:'pi-green',   impact:'IN ZONE $350&ndash;375 &mdash; FIRST SETUP &#10003;', note:'$360.45 Jul 2. Fell into the zone we flagged. R/R 5.9:1 at $360 (stop $328, target $550). First clean pullback-to-zone in weeks. Need SMA stack confirmation before entry. Paper without added capital.'},
    {ticker:'VRT',  cls:'pi-green',   impact:'IN ZONE $290&ndash;312 &mdash; SECOND SETUP &#10003;', note:'$300.53 Jul 2. Dropped 10.2% into zone. R/R 3.8:1 (stop $268, target $420). AI power infra thesis intact. Need SMA confirmation + watch $290 floor hold. Paper without added capital.'},
    {ticker:'MSFT', cls:'pi-yellow',  impact:'BOUNCED TO $390 &mdash; NEAR ZONE &#9650;', note:'$390.49 Jul 2, +4.7% from $373. $3 below zone bottom $393. Still bearish SMA stack &mdash; no entry yet. But $372 stop held as support. Watch for zone reclaim + SMA50 turn.'},
    {ticker:'PLTR', cls:'pi-yellow',  impact:'RALLIED TO $129 &mdash; SMA RECLAIM? &#9650;', note:'$129.78 Jul 2, +11.2% from $116. Was falling knife last week. Need SMA50 re-check ($136 last); if still below, trend filter still vetoes. Zone $108&ndash;122 now below price.'},
    {ticker:'NOW',  cls:'pi-yellow',  impact:'RECLAIMED $103 FLOOR &#9650;', note:'$105.88 Jul 2, +6.6%. Back above zone floor $103. Thesis (Otto + Experian) intact. Zone $103&ndash;118, stop $88. Watch for sustained hold above $103.'},
    {ticker:'ORCL', cls:'pi-red',     impact:'CONTINUED FALLING &mdash; $141 &#9660;', note:'~$141 Jul 2 (from $146.55). Dropped further below $148 stop. Setup remains dead. Now $24 below zone floor $165. No action until base + reclaim $150.'},
    {ticker:'NVDA', cls:'pi-yellow',  impact:'PULLED BACK TO $194 &#9660;',   note:'$194.83 Jul 2 (from $200). Approaching zone top $192. One more leg down and it enters zone $175&ndash;192. R/R 4.1:1 at zone. Monitor.'},
    {ticker:'AMD',  cls:'pi-yellow',  impact:'DROPPED 11% &mdash; $517 &#9660;', note:'$517.82 Jul 2 (from $580.91). Big pullback, still +33% above zone top $390. Getting closer but not actionable yet. MI400 Q3 2026.'},
    {ticker:'PANW', cls:'pi-green',   impact:'HELD &mdash; $349 &#9650;',     note:'$349.68 Jul 2, +2.5%. Resilient while other tech dropped. Above zone $232&ndash;252. No entry at these levels.'},
    {ticker:'DELL', cls:'pi-yellow',  impact:'DROPPED 9% &mdash; $394 &#9660;', note:'$394.32 Jul 2 (from $431). Approaching zone top $355. One more pullback leg could bring it into range. Monitor.'},
    {ticker:'ANET', cls:'pi-yellow',  impact:'DROPPED 6% &mdash; $159 &#9660;', note:'$159.99 Jul 2 (from $169). Above zone $128&ndash;148. Monitor.'},
    {ticker:'LMND', cls:'pi-yellow',  impact:'ABOVE ZONE &mdash; $71 &#9650;',  note:'~$71.70 Jul 2 (from $65). Above zone $45&ndash;56. Tesla autonomous insurance thesis. No chase.'},
  ],
  macro_watch: [
    '🔄 ROTATION WEEK: QQQ &minus;3.2% while SPY flat. Classic tech-to-value rotation bringing extended AI names (MRVL, AMD, DELL, VRT) back toward zones while lifting beaten-down names (MSFT +4.7%, PLTR +11%, NOW +6.6%). This is exactly the pullback-to-zone environment the framework is built for &mdash; patience is being rewarded.',
    '🚨 MRVL $290 TRAIL STOP BLOWN: $272.05 Jul 2, down 8.7%. The only bullish-stack name broke its trail. Exit triggered. Was the entire active playbook last week; now closed. Lesson: trail stops work &mdash; they lock in gains and force discipline on the exit.',
    '🎯 AVGO FIRST ENTRY SETUP: $360.45, IN zone $350&ndash;375. R/R 5.9:1 at $360 (stop $328, target $550). The name we flagged last week as &ldquo;the one to watch at $375&rdquo; has arrived. Need SMA stack confirmation before entry. Paper without added capital.',
    '🎯 VRT SECOND ENTRY SETUP: $300.53, IN zone $290&ndash;312. R/R 3.8:1 (stop $268, target $420). AI power infrastructure (liquid cooling for data centers). Dropped 10.2% in a week. Need SMA confirmation + zone floor $290 must hold.',
    '📈 MSFT BOUNCE: $390.49, up 4.7% from $372 stop. Held the $372 support level and rallied toward zone bottom $393. Still bearish SMA stack &mdash; no entry &mdash; but the bounce is constructive. If it reclaims $393 with improving SMAs, revisit.',
    '📈 PLTR REVERSAL: $129.78, up 11.2% from $116 knife. Was vetoed by falling SMA50 last week. The rally is notable but SMA50 was at $136 &mdash; still above price. Need fresh SMA scan to re-evaluate.',
    '💵 BUYING POWER $13.64: Two names are now in zones (AVGO, VRT) and a third is approaching (MSFT). But the account has $13.64 cash. Every setup on the board is paper until capital is added or fractional shares are used. The framework is generating signals; execution requires funding.',
    '📊 SMA SCANNER STALE: Last server-side SMA run was Jun 30 (MRVL bullish, MSFT/PLTR bearish). With this week&#39;s rotation, the SMA stacks may have shifted. AVGO and VRT zone entries REQUIRE SMA confirmation before action. Re-run scanner when Robinhood MCP reconnects.',
  ],
  weekly: {
    week: 'Jun 30 &ndash; Jul 3, 2026',
    updated: 'Fri Jul 4 &middot; Holiday Update (Jul 2 close, web data)',
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
      note:'MRVL was the only bullish-stack name and the entire active playbook. The $290 trail stop was set after the post-inclusion fade from $311. Price dropped 8.7% in the tech rotation (QQQ &minus;3.2%), closing at $272.05 &mdash; $18 below the $290 stop. The trail did its job: it defined risk and forced a disciplined exit. The uptrend that started at $120 is broken for now. Re-evaluate after price stabilizes above $280+ and SMA stack re-confirms.',
    },
    missed: {
      setup:'AVGO and VRT pulled into their buy zones while MRVL and AMD sold off. The rotation created new entry setups exactly where the framework wants them &mdash; at zones with favorable R/R.',
      trade:'AVGO $360 in zone $350&ndash;375 (R/R 5.9:1) and VRT $300 in zone $290&ndash;312 (R/R 3.8:1) are the first actionable setups in weeks. Both require SMA confirmation and capital ($13.64 buying power blocks execution).',
      result:'Framework is generating the right signals at the right time. Execution is blocked by capital, not by analysis.',
    },
    lessons: [
      {tag:'STOP',      cls:'lsn-rule',  text:'MRVL $290 trail stop worked exactly as designed. Price dropped 8.7% in one week; the trail locked in the exit level and forced discipline. Without it, holding through a &minus;25% drawdown (from $311 peak to $272) would have been the outcome.'},
      {tag:'ROTATION',  cls:'lsn-macro', text:'QQQ &minus;3.2% while SPY flat = classic tech rotation. Extended names (MRVL, AMD, DELL) sold off while beaten-down names (MSFT, PLTR, NOW) bounced. The zone framework is designed for exactly this &mdash; pullbacks to support in uptrends.'},
      {tag:'ZONES',     cls:'lsn-next',  text:'Two names entered zones this week: AVGO $360 (zone $350&ndash;375, R/R 5.9:1) and VRT $300 (zone $290&ndash;312, R/R 3.8:1). Both pass the 2.5:1 R/R gate. But entries REQUIRE SMA stack confirmation &mdash; learned from the PLTR lesson (in-zone but falling knife).'},
      {tag:'CAPITAL',   cls:'lsn-rule',  text:'The framework is working &mdash; ORCL knife avoided, MRVL trail stop honored, AVGO/VRT zones arrived on schedule. But $13.64 buying power means every signal is paper. Add capital or use fractional shares to act on the analysis.'},
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

# Find and replace the MARKET_PULSE block
pattern = r'const MARKET_PULSE = \{.*?\n\};'
match = re.search(pattern, html, re.DOTALL)
if not match:
    raise RuntimeError("Could not find MARKET_PULSE block")

old = match.group(0)
print(f"Found MARKET_PULSE: {len(old)} chars, lines {html[:match.start()].count(chr(10))+1}-{html[:match.end()].count(chr(10))+1}")

html_new = html[:match.start()] + NEW_PULSE + html[match.end():]

shutil.copy(SRC, SRC + '.bak')
with open(SRC, 'w') as f:
    f.write(html_new)

print(f"Updated MARKET_PULSE: {len(NEW_PULSE)} chars")
print("Done — templates/index.html updated")
