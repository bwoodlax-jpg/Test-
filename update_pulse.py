#!/usr/bin/env python3
path = '/home/user/Test-/templates/index.html'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

errors = []

def rep(old, new, label):
    global c
    if old in c:
        c = c.replace(old, new, 1)
        print(f'OK: {label}')
    else:
        errors.append(label)
        print(f'ERROR: {label} not found')

# ── 1. Date ──────────────────────────────────────────────────────────────────
rep(
    "  date: 'June 15, 2026',",
    "  date: 'June 19, 2026',",
    'date'
)

# ── 2. Updated ───────────────────────────────────────────────────────────────
rep(
    "  updated: 'Call Up &mdash; Mon Jun 15',",
    "  updated: 'Call Up &mdash; Thu Jun 19',",
    'updated'
)

# ── 3. Headline ──────────────────────────────────────────────────────────────
rep(
    "  headline: 'Iran Deal CONFIRMED &mdash; Sign Geneva Fri Jun 19 &mdash; WTI $80 (-18% from $97+) &mdash; VIX 16.73 &mdash; Nasdaq +2.1% &mdash; MSFT POTW In Zone &mdash; Warsh Jun 16&ndash;17 Final Gate',",
    "  headline: 'Iran Deal SIGNED Geneva TODAY &mdash; MSFT $379 Stand-Down CORRECT ($7 from Stop) &mdash; MRVL $311 +18% (raise trail $290) &mdash; ORCL $184 AT Zone Top &mdash; QQQ +2.4% Jun 18',",
    'headline'
)

# ── 4. Sentiment ─────────────────────────────────────────────────────────────
rep(
    "  sentiment: 'RISK-ON &mdash; WARSH GATE TODAY',",
    "  sentiment: 'RISK-ON &mdash; ORCL ENTRY IMMINENT',",
    'sentiment'
)

# ── 5. Indices ────────────────────────────────────────────────────────────────
rep(
    "  indices: [\n"
    "    {name:'Nasdaq 100', val:'+2.1%',   chg:'futures Jun 15',      dir:'up'},\n"
    "    {name:'S&P 500',    val:'+1.3%',   chg:'futures Jun 15',      dir:'up'},\n"
    "    {name:'WTI Crude',  val:'$80.07',  chg:'&ndash;18% from $97+', dir:'down'},\n"
    "    {name:'VIX',        val:'16.73',   chg:'&ndash;13.9% Iran bid', dir:'down'},\n"
    "    {name:'MSFT',       val:'~$408',   chg:'in zone $393&ndash;412', dir:'up'},\n"
    "    {name:'MRVL',       val:'~$281',   chg:'capital play active',  dir:'up'},\n"
    "  ],",
    "  indices: [\n"
    "    {name:'QQQ',        val:'$739.68', chg:'+2.38% Jun 18',                   dir:'up'},\n"
    "    {name:'SPY',        val:'$746.57', chg:'+0.76% Jun 18',                   dir:'up'},\n"
    "    {name:'MSFT',       val:'$379.05', chg:'stand-down &mdash; $7 from stop', dir:'down'},\n"
    "    {name:'MRVL',       val:'$310.85', chg:'+18.2% from $263 &mdash; raise trail $290', dir:'up'},\n"
    "    {name:'ORCL',       val:'$184.31', chg:'zone top $182 &mdash; ENTRY TRIGGER', dir:'up'},\n"
    "    {name:'NOW',        val:'$95.14',  chg:'stand-down &mdash; below zone $103', dir:'down'},\n"
    "  ],",
    'indices'
)

# ── 6. Events ─────────────────────────────────────────────────────────────────
old_events = (
    "  events: [\n"
    "    {tag:'GEO',      tagCls:'evt-geo',   headline:'Iran Deal CONFIRMED &mdash; Signing Geneva Fri Jun 19 &mdash; Strait of Hormuz Reopens in 30 Days', body:'Jun 14: Trump posted \"The Deal with the Islamic Republic of Iran is now complete\" on Truth Social. Both sides declare immediate and permanent termination of military operations. Signing ceremony Geneva, Jun 19 (Friday). Terms: US lifts oil sanctions, Iran reopens Strait of Hormuz within 30 days. Result as of Mon Jun 15 open: WTI $80.07 (-$17 from $97+ peak = -17.5%), Nasdaq 100 futures +2.1%, S&P futures +1.3%, VIX 16.73 (-14%). The primary macro headwind since Feb 28 is now resolved. Energy CPI reversal begins immediately as oil drops. Growth multiple expansion case is fully unlocked pending Warsh.'},\n"
    "    {tag:'MACRO',    tagCls:'evt-macro', headline:'Warsh FOMC Jun 16&ndash;17 &mdash; His First Meeting as Chair &mdash; Hold at 3.50&ndash;3.75% (99% Probability)', body:'Kevin Warsh (sworn in May 22) chairs his first FOMC meeting Jun 16-17. Hold at 3.50-3.75% is virtually certain (99% market-implied). Real focus: dot plot, bias shift from easing to neutral, press conference tone. Warsh is known for \"leaner Fed, less forward guidance.\" Key question: does the dot plot keep a September 2026 window open, or push first cut to 2027? Iran deal CHANGES his calculus: oil dropping 18% from peak = energy CPI relief starting in 30 days = Warsh has cover to stay neutral rather than hawkish. Best case: neutral hold + notes Iran deal reduces inflation pressure = full green light for all in-zone names. Worst case: dot plot explicitly hawkish + September window closed = growth sell-off.'},\n"
    "    {tag:'WATCH',    tagCls:'evt-watch', headline:'MRVL $281 &mdash; S&P 500 Inclusion Jun 22 = 7 Days &mdash; B. Riley Raises PT to $345', body:'B. Riley raised MRVL price target to $345 from $240 on Jun 12 &mdash; the highest street PT. MRVL ATH was $324.20 (Jun 3 intraday). Capital play: entered ~$263, trail stop $263, updated target $325 (ATH+recovery). Peak forced buying Jun 18-20 ($8T+ AUM index funds must own MRVL before Jun 22 effective date). This week is the MRVL bull run week. Iran deal risk-on bid + S&P inclusion run = dual tailwinds. Do not average up &mdash; structural entry was $220-242. Monitor and trail stop only.'},\n"
    "    {tag:'WATCH',    tagCls:'evt-watch', headline:'MSFT POTW &mdash; $408 In Zone $393&ndash;$412 &mdash; Entry Trigger: Warsh Hold Wed Jun 17', body:'MSFT opened ~$408 today (Jun 15), inside the structural entry zone $393-412 (2026 rate-fear consolidation base). Stop $372 (named structural level, below Feb re-accumulation floor). Target $625 Wedbush / $650 Morgan Stanley. R/R 6.0:1 from $408. Fundamental: Azure +40% YoY, 20M Copilot seats, non-discretionary enterprise spend. Trigger: Warsh hold + neutral language Wed Jun 17. Enter Wed AH after press conference or Thu Jun 18 open. Secondary: NOW in zone $103-118 simultaneously (stop $88, target $175, R/R 3.0:1). Combined 1.5% bankroll max.'},\n"
    "    {tag:'EARNINGS', tagCls:'evt-earn',  headline:'ORCL Beat-But-Fell Jun 10 &mdash; Approaching Zone $165&ndash;$182 &mdash; Watch Only', body:'ORCL Q4 FY2026 beat ($2.11 vs $1.97) but fell below $200 on $40B capital raise + $20B share sale. Now ~$193-199, approaching long-term Graham value zone $165-182. Iran deal + oil drop = AI cloud infrastructure spend remains intact. Do NOT anticipate zone entry — wait for price to reach zone, then wait for Warsh clearance. Stop $148 (below structural floor), target $275 (Wedbush). R/R 4.0:1 at zone. Patient entry only.'},\n"
    "  ],"
)

new_events = (
    "  events: [\n"
    "    {tag:'GEO',      tagCls:'evt-geo',   headline:'Iran Deal SIGNED Geneva Today Jun 19 &mdash; Strait of Hormuz Reopens 30 Days &mdash; Oil Headwind Resolved', body:'Signing ceremony confirmed Geneva, Thu Jun 19 (today). Both sides declared permanent end to military operations Jun 14. US lifts oil sanctions, Iran reopens Strait of Hormuz within 30 days. WTI dropped from $97+ peak toward $78&ndash;$80 range (-18%+). VIX compressed from 22+ to mid-16s. Nasdaq +2.38% Jun 18, SPY +0.76%. Energy CPI reversal begins as oil prices in deal execution. Primary macro headwind since Feb 28 structurally RESOLVED.'},\n"
    "    {tag:'MACRO',    tagCls:'evt-macro', headline:'Warsh FOMC Jun 16&ndash;17 COMPLETE &mdash; Held 3.50&ndash;3.75% &mdash; Tone Neutral &mdash; Sep 2026 Window Preserved', body:'Kevin Warsh chaired his first FOMC meeting Jun 16-17. Result: hold at 3.50-3.75% as expected. Tone was neutral, noting Iran deal reduces near-term energy inflation. September 2026 rate cut window remains OPEN per dot plot. This was the formal entry gate for MSFT/NOW. MSFT fell to $379 by Jun 18 close, breaking below zone $393-412. NOW fell to $95, breaking below zone floor $103. Both STAND-DOWN decisions were CORRECT.'},\n"
    "    {tag:'WATCH',    tagCls:'evt-watch', headline:'MRVL $310.85 &mdash; +18.2% from Entry $263 &mdash; S&P 500 Inclusion Jun 22 = 3 Days &mdash; Raise Trail Stop to $290', body:'MRVL closed $310.85 Jun 18 (AH $313.57). S&P 500 inclusion effective Mon Jun 22 = 3 trading days. Peak forced buying window is NOW (Jun 19&ndash;22). From entry ~$263: +$47.85/share (+18.2%). ACTION: Raise trail stop from $263 to $290 (Jun 17 structural floor). Do NOT add to position above zone &mdash; monitor and trail only. B. Riley PT $345. Post-inclusion: if holds $290+ after Jun 22, hold toward $325 ATH. If drops below $290, exit immediately.'},\n"
    "    {tag:'WATCH',    tagCls:'evt-watch', headline:'MSFT $379 &mdash; POTW Stand-Down CORRECT &mdash; $7 from Stop $372 &mdash; Reassess at Stop or July Catalyst', body:'MSFT closed $379.05 Jun 18, BELOW zone $393&ndash;$412. Warsh hold was insufficient to pull MSFT into zone. Stop $372 is only $7 away. STAND-DOWN was the RIGHT call. Thesis intact (Azure +40% YoY, 20M Copilot seats). Two scenarios: (1) $372 breaks = exit &mdash; zone reload fails. (2) $379 base holds into July Azure earnings = re-approach from $393. DO NOT enter at $379.'},\n"
    "    {tag:'WATCH',    tagCls:'evt-watch', headline:'ORCL $184.31 &mdash; Zone Top $182 Only $2 Away &mdash; Entry Trigger Ready &mdash; AI RPO $523B', body:'ORCL closed $184.31 Jun 18. Long-term zone TOP is $182 &mdash; ORCL is $2.31 above zone. Beat-but-fell Jun 10 drove it toward this Graham value zone. Iran deal = AI cloud spend intact. Stop $148, target $275 (Wedbush PT), R/R 4.0:1. ACTION: Set buy alert $183. If ORCL touches $182 or below, enter. Warsh neutral + oil down = favorable macro. Entry could trigger this week.'},\n"
    "  ],"
)
rep(old_events, new_events, 'events')

# ── 7. Portfolio ──────────────────────────────────────────────────────────────
old_portfolio = (
    "  portfolio: [\n"
    "    {ticker:'ORCL', cls:'pi-red',    impact:'GAP PLAY DEAD &mdash; NO ENTRY',  note:'Beat ($2.11 vs $1.97) but FELL below $200 on $20B share-sale dilution + light cloud rev ($9.91B). Gap condition failed &mdash; no entry, capital preserved. Now ~$193&ndash;$199, approaching long-term WL zone $175&ndash;$185 from above. Watch only.'},\n"
    "    {ticker:'DELL', cls:'pi-red',    impact:'ZONE REDRAWN &#9888;',          note:'~$369 &mdash; blew through $420&ndash;450 zone and $395 stop in 3 sessions on sector de-risk + Silver Lake insider supply. Thesis intact ($51.3B backlog). New zone: gap-fill $335&ndash;$355, stop $310. Stabilization + Warsh clearance required.'},\n"
    "    {ticker:'MRVL', cls:'pi-green',  impact:'CAPITAL PLAY RUNNING &#10003;',  note:'~$281 (Jun 15). B. Riley raised PT to $345 (Jun 12). ATH $324.20 (Jun 3). S&P 500 inclusion Jun 22 = 7 days &mdash; peak forced buying Jun 18&ndash;20. If entered at $263: P&L ~+$18/share (+6.8%). Trail stop $263. Updated target $325 (ATH recovery). Iran deal risk-on + inclusion run = dual tailwinds this week.'},\n"
    "    {ticker:'NVDA', cls:'pi-yellow', impact:'ABOVE ZONE &mdash; MONITOR',     note:'~$201 (Jun 12). Above redrawn zone $175&ndash;$192 (Blackwell re-rating base). Iran deal + SpaceX IPO risk-on bid. Monitor only until Warsh Jun 16&ndash;17. R/R 4.1:1 at zone.'},\n"
    "    {ticker:'MSFT', cls:'pi-green',  impact:'POTW &mdash; IN ZONE &#10003;',          note:'~$408 (Jun 15 open, Iran rally). In zone $393&ndash;$412. Stop $372. TRIGGER: Warsh hold Wed Jun 17 AH → ENTER. Target $625. R/R 6.0:1 &#10003;. THIS IS THE WEEK.'},\n"
    "    {ticker:'ANET', cls:'pi-yellow', impact:'ABOVE ZONE &mdash; WAIT',              note:'~$152 (Jun 11). Above redrawn patient zone $128&ndash;$148 (EOS switching cost base). Stop $112. Wait for pullback to zone. Distribution regime = no entries. R/R 3.2:1 at zone.'},\n"
    "    {ticker:'NOW',  cls:'pi-green',  impact:'SECONDARY &mdash; IN ZONE &#10003;',    note:'~$108 (Jun 15). In zone $103&ndash;$118. Stop $88. TRIGGER: Warsh hold Wed Jun 17 → ENTER alongside MSFT. Target $175. R/R 3.0:1 &#10003;.'},\n"
    "    {ticker:'PANW', cls:'pi-yellow', impact:'APPROACHING ZONE',                     note:'~$257 (Jun 11). Just above redrawn patient zone $232&ndash;$252 (XSIAM re-rating base). Stop $215. $5 above zone top &mdash; distribution regime keeps us sidelined. If $252 holds post-Warsh: first entry condition met. R/R 4.4:1.'},\n"
    "    {ticker:'AVGO', cls:'pi-yellow', impact:'ABOVE ZONE &mdash; WATCH',             note:'$382.57 (Jun 15). Zone $350&ndash;$375. $7.57 above zone top. Iran deal rally bid. Stop $328. If pulls back into zone post-Warsh: 5.4:1 R/R entry. Do not chase above zone.'},\n"
    "    {ticker:'LMND', cls:'pi-yellow', impact:'ABOVE ZONE &mdash; WAIT',              note:'~$60 (Jun 15). Above patient zone $45&ndash;$56. Tesla autonomous insurance catalyst still live. Stop $38. Target $88. R/R 3.0:1 at zone. Iran deal = macro risk-on could push higher &mdash; no chase above $56.'},\n"
    "  ],"
)

new_portfolio = (
    "  portfolio: [\n"
    "    {ticker:'GFS',  cls:'pi-green',  impact:'POSITION HELD &#10003;',       note:'12 shares @ $85.24 avg. Jun 18 close $85.86 (+0.7% from avg, +6.5% on day). Only actual position. $1,197 total portfolio ($1,028 equity). Monitor.'},\n"
    "    {ticker:'MRVL', cls:'pi-green',  impact:'CAPITAL PLAY +18% &#10003;',   note:'$310.85 Jun 18 (AH $313.57). Entry ~$263. P&L: +$47.85/share (+18.2%). S&P 500 inclusion Jun 22 = 3 days. ACTION: Raise trail stop $263 &rarr; $290. Hold toward $325 ATH. Peak forced buying Jun 19&ndash;22.'},\n"
    "    {ticker:'MSFT', cls:'pi-red',    impact:'POTW STAND-DOWN &#9888;',      note:'$379.05 Jun 18. Zone $393&ndash;$412. BELOW zone. Stop $372 only $7 away. Stand-down was CORRECT. Do not enter at $379. Scenarios: $372 breaks = exit thesis; $379 holds + July Azure earnings = re-approach $393.'},\n"
    "    {ticker:'NOW',  cls:'pi-red',    impact:'STAND-DOWN &#9888;',            note:'$95.14 Jun 18. Zone $103&ndash;$118. BELOW zone floor $103. Stop $88. Stand-down was CORRECT. Otto AI + Experian deal intact. Wait for $103+ price action before entry.'},\n"
    "    {ticker:'ORCL', cls:'pi-yellow', impact:'ENTRY TRIGGER READY &#9650;',  note:'$184.31 Jun 18. Zone top $182 = $2.31 away. Set buy alert $183. AI cloud RPO $523B. Stop $148, target $275, R/R 4.0:1. Iran deal + Warsh neutral = favorable. Entry imminent.'},\n"
    "    {ticker:'NVDA', cls:'pi-yellow', impact:'ABOVE ZONE &mdash; MONITOR',   note:'$210.20 Jun 18. Above zone $175&ndash;$192. Iran deal risk-on sustaining above zone. Monitor only. R/R 4.1:1 at zone.'},\n"
    "    {ticker:'AMD',  cls:'pi-yellow', impact:'FAR ABOVE ZONE &mdash; WAIT',  note:'$536.44 Jun 18. Zone $370&ndash;$390. +37% above zone top. No position. MI400 Q3 2026. Wait for pullback to zone.'},\n"
    "    {ticker:'AVGO', cls:'pi-yellow', impact:'ABOVE ZONE &mdash; WATCH',     note:'$410.79 Jun 18. Zone $350&ndash;$375. $35 above zone top. Stop $328. Target $550. R/R 5.4:1. Wait for zone test.'},\n"
    "    {ticker:'PLTR', cls:'pi-yellow', impact:'ABOVE ZONE &mdash; HOLD',      note:'$128.49 Jun 18. Zone $108&ndash;$122. Above zone. AIP commercial tripling. Stop $95. Target $183. R/R 3.4:1.'},\n"
    "    {ticker:'LMND', cls:'pi-yellow', impact:'ABOVE ZONE &mdash; WAIT',      note:'$58.90 Jun 18. Zone $45&ndash;$56. Above zone. Tesla autonomous insurance AZ+OR LIVE. Stop $38. Target $88. R/R 3.0:1.'},\n"
    "  ],"
)
rep(old_portfolio, new_portfolio, 'portfolio')

# ── 8. Macro Watch ────────────────────────────────────────────────────────────
old_macro = (
    "  macro_watch: [\n"
    "    'IRAN DEAL CONFIRMED: Trump declared \"complete\" Jun 14 via Truth Social. Signing Geneva Fri Jun 19. Terms: US lifts oil sanctions, Iran reopens Strait of Hormuz in 30 days. WTI $80.07 (-18% from $97+ peak). Energy CPI relief begins within 30 days. Dec 2026 rate-hike probability falling. Growth multiples unlocking.',\n"
    "    'WARSH FOMC JUN 16&ndash;17 (TODAY): His first meeting as chair. Hold at 3.50&ndash;3.75% is 99% probability. Focus: dot plot, bias shift easing&rarr;neutral, press conference tone. Key question: September 2026 window kept open (BULLISH) or pushed to 2027 (BEARISH)? Iran deal gives Warsh cover to stay neutral. ENTRY GATE for MSFT + NOW.',\n"
    "    'MSFT POTW: In zone $393&ndash;$412 at ~$408. Stop $372. Target $625. R/R 6.0:1. Trigger: Warsh hold Wed Jun 17 AH → enter. Azure +40% YoY, 20M Copilot seats. Highest conviction entry on the board this week.',\n"
    "    'NOW SECONDARY: In zone $103&ndash;$118 simultaneously. Stop $88. Target $175. R/R 3.0:1. Otto AI agent + Experian agentic deal. Enter alongside MSFT post-Warsh. Combined 1.5% bankroll max.',\n"
    "    'MRVL CAPITAL PLAY WEEK: S&P 500 inclusion Jun 22 = 7 days. B. Riley raised PT to $345. ATH $324.20 (Jun 3). Trail stop $263, updated target $325+. Peak forced buying Jun 18&ndash;20 ($8T+ AUM). Iran deal risk-on + inclusion run = dual tailwinds. This is the MRVL bull week.',\n"
    "    'ORCL APPROACHING ZONE: ~$193&ndash;$199 falling toward long-term zone $165&ndash;$182. Iran deal + oil drop = AI cloud spend intact. Stop $148, target $275 (4.0:1). Patient entry only when price reaches zone AND Warsh clears. Do not anticipate.',\n"
    "    'AVGO $382.57: Zone $350&ndash;$375. Iran deal rally may push AVGO away from zone temporarily. Wait for pullback to zone if market rips. Stop $328, target $550, R/R 5.4:1. Best entry candidate after MSFT/NOW if zone holds.',\n"
    "    'NEW RULE: PAUSED during regime shift. Distribution put-buying rule (3 sell-on-good-news = buy QQQ/SMH puts) is suspended while macro unlock is in progress. Reassess only if Warsh triggers new distribution signal.',\n"
    "  ],"
)

new_macro = (
    "  macro_watch: [\n"
    "    'IRAN DEAL SIGNED TODAY JUN 19: Signing ceremony Geneva today. Both sides declared permanent end Jun 14. US lifts oil sanctions, Iran reopens Strait of Hormuz in 30 days. WTI down from $97+ to ~$78&ndash;$80 range (-18%+). Energy CPI reversal begins. Nasdaq +2.38% Jun 18, SPY +0.76%. Primary macro headwind since Feb 28 RESOLVED.',\n"
    "    'WARSH FOMC COMPLETE: Held 3.50&ndash;3.75% Jun 16&ndash;17. Tone neutral, noted Iran deal reduces energy inflation. September 2026 cut window PRESERVED per dot plot. Market accepted as neutral-dovish. Growth multiples unlocked. MSFT/NOW entry gate triggered but BOTH broke below zones &mdash; stand-downs CORRECT.',\n"
    "    'MSFT $379 STAND-DOWN CORRECT: Closed $379.05 Jun 18. Zone $393&ndash;$412. Stop $372 = only $7 away. DO NOT enter at $379. Scenarios: (1) $372 breaks = exit thesis, zone reload failed. (2) $379 holds + July Azure earnings = next entry at $393+. Watch stop $372 closely.',\n"
    "    'NOW $95 STAND-DOWN CORRECT: Closed $95.14 Jun 18. Zone $103&ndash;$118. Below zone floor. Stand-down correct. Otto AI + Experian deal intact. Do not enter until $103+ price action confirms. Stop $88 if entered.',\n"
    "    'MRVL $311 ACTION &mdash; RAISE TRAIL STOP TO $290: Closed $310.85 Jun 18 (+18.2% from $263 entry). S&P 500 inclusion Jun 22 = 3 trading days. Raise trail stop $263 &rarr; $290 NOW. Peak forced buying window Jun 19&ndash;22. B. Riley PT $345. Post-inclusion: if holds $290+ &rarr; hold toward $325 ATH. If drops below $290 post-Jun 22 &rarr; exit.',\n"
    "    'ORCL $184 ENTRY TRIGGER IMMINENT: Closed $184.31 Jun 18. Zone top $182 = $2.31 away. Set buy alert $183. AI cloud RPO $523B. Stop $148, target $275, R/R 4.0:1. Iran deal + Warsh neutral = favorable macro. Be ready for ORCL entry this week.',\n"
    "    'GFS ONLY POSITION: 12 shares @ $85.24 avg. Jun 18 close $85.86 (+0.7% from cost basis). Jun 18 +6.5% on day. Total portfolio $1,197 ($1,028 equity + $43 options + $83 crypto + $43 cash). Agentic account empty.',\n"
    "    'MRVL POST-INCLUSION PLAN: Inclusion effective Jun 22. If price holds $290+ post-Jun 22: hold toward $325 ATH (B. Riley PT $345). If drops below $290 post-inclusion: exit immediately. Inclusion pump rarely holds &mdash; trail discipline critical.',\n"
    "  ],"
)
rep(old_macro, new_macro, 'macro_watch')

# ── Result ────────────────────────────────────────────────────────────────────
if errors:
    print(f'\nFAILED replacements: {errors}')
    print('File NOT written.')
else:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print('\nAll 8 replacements applied. File written.')
