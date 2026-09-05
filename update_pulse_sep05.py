#!/usr/bin/env python3
"""MARKET_PULSE -> Sep 4. Waller rate-hold bounce; ANET POTW +4.1%; zero new entries."""
import re, sys, os, shutil
FILE='templates/index.html'; shutil.copy(FILE,FILE+'.bak'); src=open(FILE).read()

NEW = """const MARKET_PULSE = {
  date: 'September 5, 2026',
  updated: 'Call Up &mdash; Sep 4 Session Close (Live Robinhood; Sep 3 is the last SETTLED close)',
  headline: 'Waller Rate-Hold Bounce &mdash; ANET POTW +4.1% And Holding &mdash; Beaten-Down Names Lead &mdash; VRT +9%, ORCL +9%, MRVL +8% &mdash; Zero New Zone Entries',
  sentiment: 'RISK-ON BOUNCE &mdash; POTW WORKING &mdash; NO NEW ENTRIES',
  sentimentCls: 'mkt-up',
  indices: [
    {name:'SPY',        val:'$770.23', chg:'+0.7% since Sep 2 &mdash; Waller bounce',   dir:'up'},
    {name:'QQQ',        val:'$719.06', chg:'+1.4% &mdash; tech leads',                   dir:'up'},
    {name:'IWM',        val:'$295.95', chg:'+0.7% &mdash; small caps join',              dir:'up'},
    {name:'DIA',        val:'$534.10', chg:'+0.7% &mdash; broad participation',          dir:'up'},
    {name:'ANET',       val:'$193.77', chg:'+4.1% &mdash; POTW WORKING',                 dir:'up'},
    {name:'VRT',        val:'$280.52', chg:'+9.3% &mdash; biggest bounce, $2 under SMA50', dir:'up'},
    {name:'ORCL',       val:'$158.77', chg:'+8.9% &mdash; earnings Thu Sep 10',           dir:'up'},
    {name:'AVGO',       val:'$357.87', chg:'&minus;2.6% &mdash; ONLY name down',          dir:'down'},
  ],
  events: [
    {tag:'POTW',     tagCls:'evt-watch', headline:'ANET $193.77 &mdash; POTW +4.1% In Two Sessions &mdash; Gate Still Holding', body:'The Sep 3 Play of the Week called ANET at $186.10 with a perfect bullish stack and R/R 4.90:1. It closed the Sep 4 session at $193.77, up 4.12%. The gate is still intact: SMA50 has kept rising to $182.88 and price sits comfortably above it. HONEST CALIBRATION: ATR(14) is $7.81, which is 4.03% of price &mdash; so a 4.12% gain is 0.98x ATR, i.e. slightly less than one average day of range. Two sessions of movement inside one ATR is not yet evidence of anything. The thesis is intact and the trade is working; it is not yet proven. ACTION: raise the stop $170 to $178 (2x ATR below current price), which cuts risk from entry from $16.10 to $8.10 per share while sitting below the rising SMA50 so ordinary tests of the average do not trigger it. R/R from here: 4.52:1.'},
    {tag:'MACRO',    tagCls:'evt-macro', headline:'Fed\\'s Waller Hints At September Hold &mdash; Risk-On Bounce Sep 3', body:'Wall Street rallied Thursday Sep 3 after Fed Governor Waller signalled a likely September rate hold. That is the single driver behind this bounce, and its signature is unmistakable in the dispersion: the most beaten-down names rallied hardest. VRT +9.3%, ORCL +8.9%, MRVL +8.2%, DELL +6.4%, AMD +4.5%. A rate-relief bounce lifts the highest-duration, most-sold-off names first because it is a discount-rate move, not a fundamentals move. That distinction matters for what follows: none of these bounces repaired a broken trend.'},
    {tag:'ZONES',    tagCls:'evt-watch', headline:'ZERO NEW ZONE ENTRIES &mdash; The Bounce Cleared The Board Again', body:'Two sessions ago seven names sat in buy zones. After the bounce only two remain, and both fail the SMA gate. PANW $333.22 is inside $322&ndash;350 but still $16 beneath a rising SMA50 $349.28 &mdash; the same fresh-breakdown structure flagged on Sep 3, unchanged. LMND $53.40 is inside $45&ndash;56 with a falling SMA50 $58.81, though that average has nearly flattened (down just $0.02 on the day). Every other name ran above its zone. The answer is the same as Aug 13: no new positions, manage what is open.'},
    {tag:'ORCL',     tagCls:'evt-geo',   headline:'ORCL $158.77 &mdash; SMA50 Finally Flattened, But The Zone Is Already Gone', body:'A genuinely frustrating sequence. On Sep 3 ORCL was flagged as having completed step one of trend repair &mdash; price reclaiming a falling SMA50 &mdash; with the note to watch for the average to flatten. It has: SMA50 went $139.78, $139.71, then TICKED UP to $139.74. Step two is complete. But price ran 8.9% to $158.77 in the same two sessions, clearing the $138&ndash;150 zone entirely. The structure qualified only after the price left the zone behind. Worse for a swing entry: ORCL reports Q1 FY2027 on Thu Sep 10 (est. EPS $1.67), so any entry now is an earnings bet, not a technical one. RBC flags execution risk on the layoff-funded AI buildout; Jefferies cut its target to $290 from $320; Morgan Stanley sits at $210 Equalweight. Guidance calls for 58&ndash;64% cloud growth &mdash; that is the bar. Stand aside through the print.'},
    {tag:'DELL',     tagCls:'evt-watch', headline:'DELL $523.93 (+6.4%) &mdash; The Flat-SMA50 Caution Resolved UPWARD', body:'DELL was flagged on Sep 3 with a caution: its SMA50 had gone flat ($434.10, $434.22, $434.17 across three sessions), and the AVGO precedent said a flat average is the absence of trend. That caution has resolved to the upside &mdash; the SMA50 turned decisively back up to $439.30 and price gained 6.4% to $523.93. Recording this plainly: the flag was warranted on the evidence available, and the outcome went the other way. A flat SMA50 is genuinely ambiguous, which is exactly why it warrants watching rather than exiting. DELL is back to an unqualified gate pass.'},
    {tag:'AVGO',     tagCls:'evt-geo',   headline:'AVGO $357.87 &mdash; The ONLY Name Down In A Broad Risk-On Bounce', body:'Every other watchlist name rose. AVGO fell 2.6%, extending its decline while the most beaten-down names around it rallied 8&ndash;9%. SMA50 $383.65 continues falling with price $26 beneath it. This is now the third consecutive call up in which AVGO has been the weakest structure on the board, and it has broken two zone floors this cycle. Failing to participate in a rate-relief bounce that lifted the entire rest of the watchlist is the clearest relative-weakness signal available &mdash; the same read that preceded VRT\\'s 27% decline. No entry, no averaging down.'},
  ],
  portfolio: [
    {ticker:'ANET', cls:'pi-green',   impact:'POTW +4.1% &mdash; $194 &#9650;',    note:'$193.77 from the $186.10 POTW entry. SMA50 $182.88 rising, price above &mdash; gate holding. Gain is 0.98x ATR, so barely one day of range: working, not yet proven. Stop raised $170 &rarr; $178. R/R 4.52:1.'},
    {ticker:'NOW',  cls:'pi-green',   impact:'WINNER +37% &mdash; $141 &#9650;',   note:'$141.27, now +36.8% from the $103.24 entry (hit $145.59 Sep 3). SMA50 $117.11 rising steeply. Trail $124 untouched and $17 below price. Target $175.'},
    {ticker:'DELL', cls:'pi-green',   impact:'+6.4% &mdash; SMA50 TURNED UP',      note:'$523.93. The Sep 3 flat-SMA50 caution resolved upward &mdash; SMA50 turned decisively back up to $439.30. Unqualified gate pass again. Above zone $418&ndash;448.'},
    {ticker:'ORCL', cls:'pi-yellow',  impact:'+8.9% &mdash; ZONE GONE, EARNINGS',   note:'$158.77. SMA50 $139.74 finally FLATTENED (step 2 of 3) &mdash; but price cleared the $138&ndash;150 zone in the same move. Earnings Thu Sep 10. Stand aside through the print.'},
    {ticker:'VRT',  cls:'pi-yellow',  impact:'+9.3% &mdash; $2 UNDER SMA50',       note:'$280.52, the biggest bounce on the board. SMA50 $282.46 still falling but price is now just $1.94 beneath it &mdash; closest to a reclaim since the breakdown. One good session flips this. Still blocked.'},
    {ticker:'MRVL', cls:'pi-yellow',  impact:'+8.2% &mdash; RECLAIMED SMA50',      note:'$223.50 vs SMA50 $220.37 &mdash; price is back above the average for the first time since the stop-out. But the SMA50 is still FALLING, so this is step one of three, not a setup. Above zone now.'},
    {ticker:'AMD',  cls:'pi-yellow',  impact:'+4.5% &mdash; STILL UNDER SMA50',    note:'$477.45. Bounced out of the $440&ndash;470 zone without ever qualifying. SMA50 $498.85 still falling, price $21 below. Unchanged: needs the reclaim.'},
    {ticker:'NVDA', cls:'pi-green',   impact:'+2.6% &mdash; $230 &#9650;',         note:'$230.35. SMA50 $210.53 rising. Clean structure maintained through both the pullback and the bounce. Zone $203&ndash;213 well below.'},
    {ticker:'PLTR', cls:'pi-green',   impact:'+2.9% &mdash; $174 &#9650;',         note:'$174.31. SMA50 $150.05 rising fast &mdash; the extension gap keeps closing through time (16% above vs 28% in Aug). Zone $138&ndash;152.'},
    {ticker:'PANW', cls:'pi-yellow',  impact:'IN ZONE &mdash; STILL BLOCKED',       note:'$333.22, up only 1.4% &mdash; barely participated in the bounce. In zone $322&ndash;350 but $16 under a RISING SMA50 $349.28. Fresh-breakdown structure unchanged from Sep 3.'},
    {ticker:'MSFT', cls:'pi-green',   impact:'+0.6% &mdash; $500 &#9654;',          note:'$499.68. SMA50 $444.38 rising fast and has now climbed THROUGH the old zone top $438 &mdash; the $410&ndash;438 zone is effectively closed by its own trend filter.'},
    {ticker:'LMND', cls:'pi-yellow',  impact:'IN ZONE &mdash; SMA50 NEARLY FLAT',   note:'$53.40. Fourth consecutive call up in zone $45&ndash;56. SMA50 $58.81 fell just $0.02 on the day &mdash; effectively flat. The trigger (base above $52 plus a flat SMA50) is closer than it has ever been.'},
    {ticker:'AVGO', cls:'pi-red',     impact:'&minus;2.6% &mdash; ONLY DECLINER &#9888;', note:'$357.87. The ONLY watchlist name down in a broad risk-on bounce. SMA50 $383.65 falling, price $26 below. Third straight call up as the weakest structure. Two zone breaks this cycle.'},
  ],
  macro_watch: [
    'POTW GRADE - WORKING, NOT YET PROVEN: ANET is +4.12% two sessions after the call, with the SMA50 still rising beneath it. But ATR(14) is $7.81 = 4.03% of price, so the entire gain is 0.98x ATR - slightly less than one average day of range. Calling this a win would be reading noise as signal. The correct statement is: thesis intact, gate holding, stop raised to $178 to cut entry risk from $16.10 to $8.10. Judge it at 2-3x ATR.',
    'THE BOUNCE WAS A DISCOUNT-RATE MOVE, NOT A FUNDAMENTALS MOVE: Waller hinting at a September hold lifted the most beaten-down, highest-duration names hardest - VRT +9.3%, ORCL +8.9%, MRVL +8.2%. None of those bounces repaired a broken trend. VRT is still under a falling SMA50, MRVL is still under a falling SMA50, AVGO fell outright. A rate-relief rally changes what you pay for future cash flows; it does not change whether a stock is in a downtrend.',
    'ORCL IS THE SEQUENCING LESSON: The Sep 3 note said to watch for the SMA50 to flatten. It flattened - and price cleared the zone in the same two sessions. The structure qualified only after the entry was gone. That is not a framework failure; it is the cost of requiring two independent conditions that can resolve in either order. Worth logging: when a name is one condition away AND deeply oversold, the zone can vanish faster than the trend repairs.',
    'AVGO IS NOW THE CLEAREST AVOID ON THE BOARD: It is the only name that fell during a broad risk-on bounce, the third consecutive call up as the weakest structure, and it has broken two zone floors this cycle. Non-participation in a rally that lifted everything else is the same relative-weakness signal that preceded VRT falling 27%. There is no version of this that is a buy.',
    'THE DELL FLAG RESOLVED AGAINST ME - RECORDING IT: DELL was flagged Sep 3 for a flat SMA50 on the AVGO precedent. The average turned decisively back up and DELL gained 6.4%. The caution was warranted on the evidence at the time, and the outcome went the other way. A flat SMA50 is genuinely ambiguous - it resolves up as often as down - which is why it warrants watching rather than acting.',
    'ORCL EARNINGS THU SEP 10 IS THE WEEK\\'S EVENT: Q1 FY2027, est. EPS $1.67, with guidance calling for 58-64% cloud growth as the bar. RBC flags execution risk on the layoff-funded AI buildout; Jefferies cut to $290 from $320; Morgan Stanley Equalweight $210. ADBE reports the same evening - an enterprise-software read-through for NOW. Neither is a position, so both are information rather than risk.',
    'VRT AND LMND ARE THE TWO TO WATCH: VRT at $280.52 is $1.94 under its SMA50 - one good session from a reclaim after a 27% decline. LMND\\'s SMA50 fell $0.02 on the day, effectively flat, with price basing above $52 for a fourth call up. Both are one condition from becoming live setups. Neither is there yet, and neither should be anticipated.',
  ],
  weekly: {
    week: 'Sep 3 &ndash; Sep 4, 2026',
    updated: 'Fri Sep 4 session close (Sep 3 is the last settled close)',
    headline: 'Waller Rate-Hold Bounce &mdash; ANET POTW +4.1% &mdash; Beaten-Down Names Lead &mdash; ORCL Zone Vanishes As Its SMA50 Flattens &mdash; AVGO Alone In The Red',
    week_chg: [
      {name:'SPY',       open:'$765.16', close:'$770.23', chg:'+0.7% &mdash; Waller bounce',       dir:'up'},
      {name:'QQQ',       open:'$709.24', close:'$719.06', chg:'+1.4% &mdash; tech leads',           dir:'up'},
      {name:'ANET',      open:'$186.10', close:'$193.77', chg:'+4.1% &mdash; POTW working',         dir:'up'},
      {name:'VRT',       open:'$256.70', close:'$280.52', chg:'+9.3% &mdash; biggest bounce',       dir:'up'},
      {name:'AVGO',      open:'$367.24', close:'$357.87', chg:'&minus;2.6% &mdash; only decliner',  dir:'down'},
    ],
    potw: {
      ticker:'ANET', type:'Zone Entry &mdash; Perfect Stack &mdash; OPEN',
      entry:'$186.10 (Sep 3 POTW, zone $172&ndash;190)', exit:'Open &mdash; $193.77 Sep 4',
      high:'$194.07 Sep 4', pnl:'+4.12% (0.98x ATR)',
      verdict:'WORKING &mdash; NOT YET PROVEN', verdictCls:'wr-win',
      note:'Called at $186.10 on a perfect bullish stack with R/R 4.90:1. Up 4.12% in two sessions with the SMA50 still rising beneath price at $182.88 &mdash; the gate that justified the entry is intact. The honest calibration: ATR(14) is $7.81, or 4.03% of price, so the whole gain amounts to 0.98x ATR &mdash; slightly less than one average day of range. Two sessions inside a single ATR is not evidence. Stop raised $170 to $178 (2x ATR below price, sitting under the rising SMA50), cutting risk from entry from $16.10 to $8.10 and leaving R/R at 4.52:1. Judge this trade at 2&ndash;3x ATR, not at day two.',
    },
    missed: {
      setup:'ORCL completed the trend repair the Sep 3 note asked for &mdash; its SMA50 flattened and ticked up &mdash; but price ran 8.9% and cleared the $138&ndash;150 zone in the same two sessions.',
      trade:'The structure qualified only after the entry was gone. ORCL now reports Thu Sep 10, so any entry is an earnings bet rather than a technical one.',
      result:'Not a framework failure &mdash; the cost of requiring two conditions that can resolve in either order. Logged: when a name is one condition away AND deeply oversold, the zone can vanish faster than the trend repairs.',
    },
    lessons: [
      {tag:'CALIBRATE',  cls:'lsn-rule',  text:'ANET is +4.1%, which sounds like a win but equals 0.98x ATR &mdash; under one average day of range. Measuring a young trade in ATR rather than percent is the difference between reading signal and reading noise. Judge at 2&ndash;3x ATR.'},
      {tag:'RATE MOVE',  cls:'lsn-macro', text:'The Waller hold hint lifted the most beaten-down names hardest (VRT +9.3%, ORCL +8.9%, MRVL +8.2%). A discount-rate bounce re-prices future cash flows; it does not repair a downtrend. All three remain under falling SMA50s.'},
      {tag:'SEQUENCING', cls:'lsn-next',  text:'ORCL\\'s SMA50 flattened exactly as hoped, and its zone vanished in the same two sessions. Two independent conditions can resolve in either order, and the entry only exists while both hold at once.'},
      {tag:'FLAT SMA',   cls:'lsn-rule',  text:'DELL was flagged for a flat SMA50 on the AVGO precedent; the average turned back up and DELL gained 6.4%. A flat SMA50 is genuinely ambiguous and resolves both ways &mdash; it justifies watching, not acting. AVGO, by contrast, kept falling.'},
    ],
    eow: [
      {ticker:'ANET', price:'$193.77', sCls:'eow-green',  status:'POTW +4.1% &#9650;',          note:'Gate holding. Stop $170 &rarr; $178'},
      {ticker:'NOW',  price:'$141.27', sCls:'eow-green',  status:'WINNER +37% &#9650;',          note:'Trail $124 untouched. Target $175'},
      {ticker:'DELL', price:'$523.93', sCls:'eow-green',  status:'+6.4% SMA50 UP &#9650;',       note:'Flat-SMA caution resolved upward'},
      {ticker:'NVDA', price:'$230.35', sCls:'eow-green',  status:'+2.6% &#9650;',                note:'SMA50 $211 rising. Clean'},
      {ticker:'PLTR', price:'$174.31', sCls:'eow-green',  status:'+2.9% &#9650;',                note:'SMA50 $150 rising. Gap closing'},
      {ticker:'MSFT', price:'$499.68', sCls:'eow-green',  status:'+0.6% &#9654;',                note:'SMA50 $444 through old zone top'},
      {ticker:'ORCL', price:'$158.77', sCls:'eow-yellow', status:'+8.9% ZONE GONE &#9650;',      note:'SMA50 flat at last. Earnings Sep 10'},
      {ticker:'VRT',  price:'$280.52', sCls:'eow-yellow', status:'+9.3% NEAR RECLAIM &#9650;',   note:'$1.94 under SMA50 $282.46'},
      {ticker:'MRVL', price:'$223.50', sCls:'eow-yellow', status:'+8.2% ABOVE SMA50 &#9650;',    note:'But SMA50 $220 still falling'},
      {ticker:'AMD',  price:'$477.45', sCls:'eow-yellow', status:'+4.5% STILL UNDER &#9660;',    note:'SMA50 $499 falling. Left zone'},
      {ticker:'PANW', price:'$333.22', sCls:'eow-yellow', status:'IN ZONE, BLOCKED &#9660;',     note:'$16 under RISING SMA50 $349'},
      {ticker:'LMND', price:'$53.40',  sCls:'eow-yellow', status:'IN ZONE, SMA50 FLAT &#9654;',  note:'4th call up. SMA50 fell $0.02'},
      {ticker:'AVGO', price:'$357.87', sCls:'eow-red',    status:'ONLY DECLINER &#9888;',        note:'&minus;2.6% in a risk-on bounce'},
    ],
  },
};"""

new_src,n = re.subn(r'const MARKET_PULSE = \{.*?\n\};', lambda m: NEW, src, flags=re.DOTALL)
if n!=1: print(f'ERROR: {n}'); sys.exit(1)
open(FILE,'w').write(new_src); print(f'OK - MARKET_PULSE replaced ({n})'); os.remove(FILE+'.bak')
