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

# ── 1. History status cleanup ─────────────────────────────────────────────────
# v8→v9 (Jun 5): ACTIVE → SUPERSEDED
rep(
    "    ticker:'Watchlist v8→v9', company:'Call Up June 5, 2026 — ORCL POTW Loss; Rate Fear Week; New Put-Buying Rule',\n"
    "    added:'June 5, 2026', addedPrice:'—',\n"
    "    exitDate:'—', exitPrice:'—',\n"
    "    pnl:'—', status:'ACTIVE', statusCls:'hs-active',",
    "    ticker:'Watchlist v8→v9', company:'Call Up June 5, 2026 — ORCL POTW Loss; Rate Fear Week; New Put-Buying Rule',\n"
    "    added:'June 5, 2026', addedPrice:'—',\n"
    "    exitDate:'—', exitPrice:'—',\n"
    "    pnl:'—', status:'SUPERSEDED', statusCls:'hs-revised',",
    'history v8->v9 status'
)

# v12→v13 (Jun 11): ACTIVE → SUPERSEDED
rep(
    "    ticker:'Watchlist v12→v13', company:'Call Up June 11, 2026 — ORCL Beat-But-Fell (No Entry); Third Distribution Signal; DELL Zone Redrawn; STAND DOWN Week',\n"
    "    added:'June 11, 2026', addedPrice:'—',\n"
    "    exitDate:'—', exitPrice:'—',\n"
    "    pnl:'—', status:'ACTIVE', statusCls:'hs-active',",
    "    ticker:'Watchlist v12→v13', company:'Call Up June 11, 2026 — ORCL Beat-But-Fell (No Entry); Third Distribution Signal; DELL Zone Redrawn; STAND DOWN Week',\n"
    "    added:'June 11, 2026', addedPrice:'—',\n"
    "    exitDate:'—', exitPrice:'—',\n"
    "    pnl:'—', status:'SUPERSEDED', statusCls:'hs-revised',",
    'history v12->v13 status'
)

# v13→v14 (Jun 12): ACTIVE → SUPERSEDED
rep(
    "    ticker:'Watchlist v13→v14', company:'Call Up June 12, 2026 — Iran Deal Draft; Oil -12%; SpaceX IPO; MRVL +11% Activated; Stop-Becomes-Entry Board Restructure; Conditional Regime Shift',\n"
    "    added:'June 12, 2026', addedPrice:'—',\n"
    "    exitDate:'—', exitPrice:'—',\n"
    "    pnl:'—', status:'ACTIVE', statusCls:'hs-active',",
    "    ticker:'Watchlist v13→v14', company:'Call Up June 12, 2026 — Iran Deal Draft; Oil -12%; SpaceX IPO; MRVL +11% Activated; Stop-Becomes-Entry Board Restructure; Conditional Regime Shift',\n"
    "    added:'June 12, 2026', addedPrice:'—',\n"
    "    exitDate:'—', exitPrice:'—',\n"
    "    pnl:'—', status:'SUPERSEDED', statusCls:'hs-revised',",
    'history v13->v14 status'
)

# v14→v15 (Jun 15): ACTIVE → SUPERSEDED
rep(
    "    ticker:'Watchlist v14→v15', company:'Call Up June 15, 2026 — Iran Deal CONFIRMED (Trump Jun 14); Signing Geneva Jun 19; WTI $80.07 (-18% from $97+); VIX 16.73; Nasdaq +2.1%; MSFT POTW In Zone; Warsh FOMC Jun 16–17',\n"
    "    added:'June 15, 2026', addedPrice:'—',\n"
    "    exitDate:'—', exitPrice:'—',\n"
    "    pnl:'—', status:'ACTIVE', statusCls:'hs-active',",
    "    ticker:'Watchlist v14→v15', company:'Call Up June 15, 2026 — Iran Deal CONFIRMED (Trump Jun 14); Signing Geneva Jun 19; WTI $80.07 (-18% from $97+); VIX 16.73; Nasdaq +2.1%; MSFT POTW In Zone; Warsh FOMC Jun 16–17',\n"
    "    added:'June 15, 2026', addedPrice:'—',\n"
    "    exitDate:'—', exitPrice:'—',\n"
    "    pnl:'—', status:'SUPERSEDED', statusCls:'hs-revised',",
    'history v14->v15 status'
)

# ── 2. Update v15→v16 lesson (fill in the blank) ──────────────────────────────
rep(
    "    ticker:'Watchlist v15→v16', company:'Call Up June 19, 2026 — Iran Deal SIGNED Geneva Today; MSFT $379 Stand-Down CORRECT; MRVL $311 +18% (raise trail $290); ORCL $184 AT Zone Top; Warsh FOMC COMPLETE (Hold 3.50–3.75%)',\n"
    "    added:'June 19, 2026', addedPrice:'—',\n"
    "    exitDate:'—', exitPrice:'—',\n"
    "    pnl:'—', status:'ACTIVE', statusCls:'hs-active',\n"
    "    fw:'Josh + Kevin',",
    "    ticker:'Watchlist v15→v16', company:'Call Up June 19, 2026 — Iran Deal SIGNED Geneva Today; MSFT $379 Stand-Down CORRECT; MRVL $311 +18% (raise trail $290); ORCL $184 AT Zone Top; Warsh FOMC COMPLETE (Hold 3.50–3.75%)',\n"
    "    added:'June 19, 2026', addedPrice:'—',\n"
    "    exitDate:'—', exitPrice:'—',\n"
    "    pnl:'—', status:'SUPERSEDED', statusCls:'hs-revised',\n"
    "    fw:'Josh + Kevin',",
    'history v15->v16 status (superseded by v16->v17)'
)

# ── 3. Weekly section — replace Jun 2–5 with Jun 16–20 ───────────────────────
old_weekly = (
    "  weekly: {\n"
    "    week: 'June 2&ndash;5, 2026',\n"
    "    updated: 'Fri Jun 6 &middot; 8 PM ET',\n"
    "    headline: 'Rate-Hike Fear Erased the Week &mdash; Puts Would Have Paid 5&ndash;10&times;',\n"
    "    week_chg: [\n"
    "      {name:'S&P 500',   open:'7,609', close:'7,384',    chg:'-3.0%',   dir:'down'},\n"
    "      {name:'Nasdaq',    open:'27,200', close:'26,194',  chg:'-3.7%',   dir:'down'},\n"
    "      {name:'SOX Semi',  open:'&mdash;', close:'&mdash;', chg:'-10.4%', dir:'down'},\n"
    "      {name:'10Y Yield', open:'4.64%', close:'4.82%',    chg:'+0.18',   dir:'up'},\n"
    "      {name:'WTI Crude', open:'$93',   close:'$96',      chg:'+3.2%',   dir:'up'},\n"
    "    ],\n"
    "    potw: {\n"
    "      ticker:'ORCL', type:'Pre-Earnings Drift (Primary)',\n"
    "      entry:'$224 est. (zone mid)', exit:'$213.68 (Fri Jun 5 hard exit)',\n"
    "      high:'$249 (Thu Jun 4)', pnl:'-$10.32 (-4.6%)',\n"
    "      verdict:'LOSS', verdictCls:'wr-loss',\n"
    "      note:'Worked through Thursday ($249 high). NFP Friday crushed ORCL -9.6%. Hard exit honored. Framework prevented holding into Jun 10 earnings.',\n"
    "    },\n"
    "    missed: {\n"
    "      setup:'PANW full gap fade Tue + AVGO beat -8% AH Wed = two &ldquo;sell on good news&rdquo; signals in 48 hours.',\n"
    "      trade:'Buy QQQ puts or SMH puts at Thu Jun 4 open. 30 days out, 3&ndash;5% OTM. Size: 0.5% bankroll.',\n"
    "      result:'Thu Nasdaq -4%. Fri Nasdaq -4%. QQQ puts: 5&ndash;10&times; premium. SMH sector drop: -10.4% on week.',\n"
    "    },\n"
    "    lessons: [\n"
    "      {tag:'MISSED', cls:'lsn-miss', text:'Two &ldquo;sell on good news&rdquo; events in 48hrs = distribution signal. NEW RULE: buy sector puts immediately.'},\n"
    "      {tag:'MACRO',  cls:'lsn-macro', text:'NFP was in Macro Watch all week. ADP beat Wednesday was the warning. Should have triggered defensive hedging Thursday open.'},\n"
    "      {tag:'RULE',   cls:'lsn-rule', text:'Hard exit rule worked. ORCL out Fri Jun 5 before Jun 9 earnings. Framework prevented the worst-case binary hold.'},\n"
    "      {tag:'NEXT',   cls:'lsn-next', text:'Trail stops must tighten aggressively when AI sector sells -4% intraday. Did not execute this on Thursday.'},\n"
    "    ],\n"
    "    eow: [\n"
    "      {ticker:'NVDA', price:'$204', sCls:'eow-green',  status:'BACK IN ZONE',    note:'Zone $200&ndash;215 &#10003;'},\n"
    "      {ticker:'MSFT', price:'$412', sCls:'eow-red',    status:'BELOW ZONE &#9888;', note:'Stop $390 watch'},\n"
    "      {ticker:'ANET', price:'$154', sCls:'eow-green',  status:'BACK IN ZONE',    note:'Zone $148&ndash;168 &#10003;'},\n"
    "      {ticker:'NOW',  price:'$111', sCls:'eow-red',    status:'BELOW ZONE &#9888;', note:'Stop $103 critical'},\n"
    "      {ticker:'ORCL', price:'$213', sCls:'eow-yellow', status:'POTW EXIT &#10003;', note:'Out. Earnings Jun 9'},\n"
    "      {ticker:'PLTR', price:'$134', sCls:'eow-yellow', status:'HOLD &mdash; DOWN',  note:'Above stop $108'},\n"
    "      {ticker:'AMD',  price:'$458', sCls:'eow-yellow', status:'HOLD &mdash; DOWN',  note:'Above stop $370'},\n"
    "      {ticker:'AVGO', price:'$472', sCls:'eow-yellow', status:'ABOVE ZONE',       note:'Recovered. Stop $385'},\n"
    "      {ticker:'VRT',  price:'$323', sCls:'eow-green',  status:'IN ZONE',          note:'Zone $310&ndash;340'},\n"
    "      {ticker:'PANW', price:'$283', sCls:'eow-yellow', status:'HOLD &mdash; TRAIL', note:'Stop $275'},\n"
    "      {ticker:'LMND', price:'~$62', sCls:'eow-yellow', status:'NEAR ZONE',        note:'Watch $52&ndash;60'},\n"
    "    ],\n"
    "  },"
)

new_weekly = (
    "  weekly: {\n"
    "    week: 'June 16&ndash;20, 2026',\n"
    "    updated: 'Sat Jun 21 &middot; Call Up',\n"
    "    headline: 'Iran Deal Signed + Warsh Hold = Full Risk-On &mdash; MSFT/NOW Stand-Down Correct &mdash; MRVL +18% Inclusion Week',\n"
    "    week_chg: [\n"
    "      {name:'SPY',       open:'TBD', close:'TBD',     chg:'TBD (risk-on week)', dir:'up'},\n"
    "      {name:'QQQ',       open:'TBD', close:'$739+',   chg:'TBD (Iran + Warsh bid)', dir:'up'},\n"
    "      {name:'10Y Yield', open:'TBD', close:'TBD',     chg:'TBD',              dir:'down'},\n"
    "      {name:'WTI Crude', open:'~$80', close:'TBD',    chg:'&ndash;18% from $97+ peak', dir:'down'},\n"
    "      {name:'VIX',       open:'16.73', close:'TBD',   chg:'Iran deal compressed',  dir:'down'},\n"
    "    ],\n"
    "    potw: {\n"
    "      ticker:'MSFT', type:'Post-Warsh Swing Entry (Primary)',\n"
    "      entry:'$393&ndash;$412 zone (trigger: Warsh hold Jun 17)', exit:'STAND DOWN &mdash; price broke below zone',\n"
    "      high:'~$408 Mon Jun 16 (Iran rally)', pnl:'$0 &mdash; Capital Preserved',\n"
    "      verdict:'STAND DOWN', verdictCls:'wr-neutral',\n"
    "      note:'Warsh held neutral Jun 17 (gate &#10003;) but MSFT fell to $379.05 by Jun 18 &mdash; BELOW zone $393&ndash;$412. Framework requires price IN zone at trigger. Stand-down was correct. Stop $372 only $7 away. Capital preserved = framework win.',\n"
    "    },\n"
    "    missed: {\n"
    "      setup:'ORCL $184 touching zone top $182 &mdash; entry trigger imminent. Alert $183 set.',\n"
    "      trade:'Buy ORCL at $182 or below. Stop $148. Target $275. R/R 4.0:1 at zone mid.',\n"
    "      result:'Pending &mdash; zone entry may trigger week of Jun 22. ORCL at $184.31 Jun 18, $2 above zone top.',\n"
    "    },\n"
    "    lessons: [\n"
    "      {tag:'STAND DOWN', cls:'lsn-rule', text:'MSFT/NOW stand-down framework validated: macro gates cleared (Iran deal &#10003; + Warsh hold &#10003;) but price broke BELOW zones. Framework requires price IN zone, not approaching from above.'},\n"
    "      {tag:'MACRO',      cls:'lsn-macro', text:'Maximum risk-on macro (Iran signed + Warsh neutral) still did not pull MSFT into zone. Price structure overrides macro narrative. Zones are anchored to structural support, not macro catalysts.'},\n"
    "      {tag:'MRVL',       cls:'lsn-rule', text:'MRVL +18.2% from $263 entry by Thu Jun 18. S&P 500 inclusion effective Mon Jun 22. Raised trail stop $263 &rarr; $290. Post-inclusion discipline is the next test: hold $290+ or exit.'},\n"
    "      {tag:'NEXT',       cls:'lsn-next', text:'Two high-priority action items entering week of Jun 22: (1) MRVL S&P inclusion Monday &mdash; peak forced buying, trail stop $290. (2) ORCL $184 touching zone top $182 &mdash; entry alert live.'},\n"
    "    ],\n"
    "    eow: [\n"
    "      {ticker:'MSFT', price:'$379', sCls:'eow-red',    status:'STAND-DOWN &#9888;',     note:'Below zone $393&ndash;412. Stop $372 = $7 away'},\n"
    "      {ticker:'MRVL', price:'$311', sCls:'eow-green',  status:'CAPITAL PLAY &#10003;',  note:'+18% from $263. S&P inclusion Mon Jun 22'},\n"
    "      {ticker:'ORCL', price:'$184', sCls:'eow-yellow', status:'AT ZONE TOP &#9650;',    note:'Zone top $182 = $2 away. Alert $183'},\n"
    "      {ticker:'NOW',  price:'$95',  sCls:'eow-red',    status:'STAND-DOWN &#9888;',     note:'Below zone floor $103. Stop $88'},\n"
    "      {ticker:'NVDA', price:'$210', sCls:'eow-yellow', status:'ABOVE ZONE',             note:'Zone $175&ndash;192. Monitor'},\n"
    "      {ticker:'AMD',  price:'$536', sCls:'eow-yellow', status:'FAR ABOVE ZONE',         note:'Zone $370&ndash;390. No entry'},\n"
    "      {ticker:'AVGO', price:'$411', sCls:'eow-yellow', status:'ABOVE ZONE',             note:'Zone $350&ndash;375. Watch pullback'},\n"
    "      {ticker:'PLTR', price:'$128', sCls:'eow-yellow', status:'ABOVE ZONE',             note:'Zone $108&ndash;122. Trail stop $95'},\n"
    "      {ticker:'ANET', price:'$170', sCls:'eow-yellow', status:'ABOVE ZONE',             note:'Zone $128&ndash;148. Monitor'},\n"
    "      {ticker:'PANW', price:'$288', sCls:'eow-yellow', status:'ABOVE ZONE',             note:'Zone $232&ndash;252. Watch'},\n"
    "      {ticker:'DELL', price:'$410', sCls:'eow-yellow', status:'ABOVE ZONE',             note:'Zone $335&ndash;355. Thesis intact'},\n"
    "      {ticker:'VRT',  price:'$333', sCls:'eow-yellow', status:'ABOVE ZONE',             note:'Zone $290&ndash;312. Monitor'},\n"
    "      {ticker:'LMND', price:'$59',  sCls:'eow-yellow', status:'ABOVE ZONE',             note:'Zone $45&ndash;56. No chase'},\n"
    "    ],\n"
    "  },"
)

rep(old_weekly, new_weekly, 'weekly section Jun 2-5 → Jun 16-20')

# ── Result ────────────────────────────────────────────────────────────────────
if errors:
    print(f'\nFAILED: {errors}')
    print('File NOT written.')
else:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print('\nAll replacements applied. File written.')
