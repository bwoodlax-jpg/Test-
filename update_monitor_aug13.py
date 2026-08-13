#!/usr/bin/env python3
"""Refresh MONITOR_DATA thesis/verdict/alert fields with Aug 12 data.
Preserves the pp/mac/cat research scores and notes."""
import re, sys, os, shutil

FILE = 'templates/index.html'
shutil.copy(FILE, FILE + '.bak')
src = open(FILE, 'r').read()

# ticker -> (thesis, verdict, verdictCls, alert)
UPDATES = {
'MSFT': ('INTACT — EARNINGS GAP CONFIRMED', 'ABOVE ZONE — $492 EXTENDED', 'vd-caution',
  'Call Up — Aug 13, 2026: MSFT $492.43. THE BIG ONE THE GATE MISSED. MSFT closed Jul 29 at $390.54 and opened Jul 30 at $437.90, closing $451.10 — a 15.5% single-session earnings gap on Azure Q4 results. It has run to $492.43 since, up 25.0% in four weeks. The SMA gate had blocked entry at $394 in July because the SMA50 was falling and the full stack was inverted; that block cost the largest winner in the framework to date. SMA50 is now $410.30 and RISING — the trend has genuinely turned, and the inverted stack has resolved. But price is 20% above the SMA50, far too extended for new money. ZONE REDRAWN to $410-438 (SMA50 up to the first post-gap shelf), stop $385 just below the gap origin $390.54. HOLDERS: thesis fully confirmed, ride it. NEW MONEY: wait for a pullback toward the SMA50. STRUCTURAL LESSON: a falling SMA50 cannot anticipate an earnings surprise — the gate filters trend, and an earnings gap is a trend discontinuity. This is the strongest argument yet for an explicit pre-earnings exception to the filter.'),

'NVDA': ('INTACT — CLEANEST STACK ON THE BOARD', 'ABOVE ZONE — $224 TRENDING', 'vd-caution',
  'Call Up — Aug 13, 2026: NVDA $224.09, up 10.5% in four weeks. Textbook bullish structure: SMA50 $206.13 and SMA100 $203.20, both rising, price comfortably above both. This is the cleanest SMA stack on the watchlist. The old entry zone $175-192 is now 15% below market and unreachable absent a thesis break — ZONE REDRAWN to $203-213, which is the SMA100/SMA50 confluence and the first genuine support shelf. Stop $192 = the old zone top, which flipped from resistance to support during the July run. Blackwell GB300 ramping, $500B revenue visibility intact, Vera Rubin on track. No entry at $224 — the setup is a pullback to the moving averages, and nothing about the current tape suggests one is imminent. Patience.'),

'ORCL': ('RECOVERING — STILL BELOW TREND FILTER', 'BELOW SMA50 — GATE BLOCKS', 'vd-caution',
  'Call Up — Aug 13, 2026: ORCL $153.28, up 21.3% off the lows — the strongest bounce on the board in percentage terms. But the framework still says NO. SMA50 $155.58 is FALLING and price sits beneath it. ORCL is the name that validated the SMA gate in the first place: it broke through its zone floor and fell roughly 30% while the gate kept capital out. A 21% bounce does not undo a broken trend — it is a recovery in progress, not a completed repair. ZONE REDRAWN to $138-150, reflecting where the stock actually based rather than the aspirational $165-182 that was never reached. Stop $128 below the July low. ENTRY REQUIRES an SMA50 reclaim first, even inside the zone. AI cloud RPO $553B and OCI +84% YoY mean the business thesis is intact; only the price structure is damaged.'),

'AMD':  ('INTACT — ONLY LARGE AI NAME BELOW SMA50', 'BELOW SMA50 — GATE BLOCKS', 'vd-caution',
  'Call Up — Aug 13, 2026: AMD $482.93, DOWN 2.6% over four weeks while every AI peer ran 10-29%. This is the notable divergence on the board alongside VRT. SMA50 $511.56 is FALLING and price is beneath it — AMD is the only large AI name still under its own trend filter. The MI400 Helios thesis is unchanged: $60B committed from OpenAI and Meta, racks shipping. But relative weakness during a sector melt-up deserves respect rather than dismissal. ZONE REDRAWN to $440-470, deliberately set beneath the falling SMA50 so that a zone tag alone cannot trigger entry. Stop $415 below the July consolidation. ENTRY REQUIRES an SMA50 reclaim. Monitor whether this is rotation out of AMD specifically or the early stage of a broader semis pause.'),

'LMND': ('INTACT — IN ZONE BUT KNIFE STRUCTURE', 'IN ZONE — SMA GATE BLOCKS', 'vd-caution',
  'Call Up — Aug 13, 2026: LMND $51.64, down 23.1% in four weeks and now the ONLY watchlist name inside its buy zone ($45-56). That makes it the single most interesting name on the board — and still not a trade. SMA50 $60.04 is falling and price is $8.40 beneath it: the exact falling-knife structure the gate was built to catch after ORCL. Zone presence without SMA confirmation is not a setup. WHAT WOULD CHANGE THIS: a base above $52 holding for several sessions plus an SMA50 that flattens or turns up. That combination would make LMND the first genuine new entry in weeks, with R/R roughly 3.2:1 from the zone mid. Tesla FSD insurance is live in AZ and OR and the Q4 EBITDA target is unchanged, so the business thesis has not broken — this is a price-structure problem. Watch it closely.'),

'DELL': ('INTACT — FULL RECOVERY FROM JUN DRAWDOWN', 'ABOVE ZONE — $485 TRENDING', 'vd-caution',
  'Call Up — Aug 13, 2026: DELL $484.50, up 22.2% in four weeks and fully recovered from the June drawdown that forced the first zone redraw. Vindication for that redraw: the Jun 11 zone $335-355 was set at the gap origin rather than the shallow 2-9% pullback, DELL based almost exactly there, and has since run 40% off it. Getting the zone depth right is what made the recovery tradeable. SMA50 $418.69 rising strongly, SMA100 $320.36 far below — a well-established trend. ZONE REDRAWN AGAIN to $418-448 on the rising SMA50, stop $392 below the August breakout base. AI server revenue +757% YoY and the record $51.3B backlog remain intact. No entry at $485; wait for the SMA50.'),

'PANW': ('INTACT — STEADIEST TREND ON THE BOARD', 'ABOVE ZONE — $387 EXTENDED', 'vd-caution',
  'Call Up — Aug 13, 2026: PANW $387.01, up 7.9% in four weeks — a smaller move than the AI names, but the steadiest and most consistent climb on the watchlist. SMA50 has risen from $258 to $322.21, and the SMA50/SMA100 spread ($322 vs $258) is the widest of any name here, which marks a very strong and well-supported trend. The flip side: price is 20% above its own SMA50, so this is extended. ZONE REDRAWN to $322-350 on the rising SMA50, stop $300 at round-number support beneath it. NGS ARR +60% YoY and XSIAM consolidation continue to compound. Cybersecurity spend is non-discretionary, which is exactly why PANW held up during the July selloff and kept grinding higher. No entry here — wait for the SMA50 to catch up.'),

'PLTR': ('INTACT — MOST EXTENDED NAME ON BOARD', 'ABOVE ZONE — $171 DO NOT CHASE', 'vd-caution',
  'Call Up — Aug 13, 2026: PLTR $171.04, up 29.2% in four weeks — the biggest move on the entire watchlist. SMA50 $133.89 and SMA100 $137.89 are both rising and price is well above both, so the trend is confirmed. But price is 28% above the SMA50, making PLTR the most extended name on the board by a clear margin. ZONE REDRAWN to $138-152 on the SMA50/SMA100 confluence, stop $125 below both averages and the July base. 85% YoY revenue growth, $7.65B FY2026 guide, and the DIA contract challenge remain live catalysts. HISTORICAL NOTE: PLTR is the name that produced the SMA filter in the first place — it spent months below a falling SMA50 while the story stayed exciting. It has now been on the right side of that filter for weeks. The lesson cuts both ways: respect the filter when it says no, and respect valuation when it says extended. Do not chase 29% in four weeks.'),

'VRT':  ('BROKEN — ZONE FLOOR FAILED', 'BROKEN — MONITOR ONLY', 'vd-avoid',
  'Call Up — Aug 13, 2026 (STRUCTURE BROKEN): VRT $288.36 — fell THROUGH its $290 zone floor. SMA50 $298.32 and SMA100 $303.38 are both ABOVE price and both falling. This is the identical structure ORCL showed immediately before it fell roughly 30% through its own zone. THE DAMNING DETAIL: VRT went -0.4% over four weeks while every AI-infrastructure peer ran 10-29% — ANET +25%, DELL +22%, AVGO +12%, NVDA +10%. Relative weakness during a sector-wide melt-up is a genuine warning, not noise. When the tide lifts everything except one boat, look at that boat. The business thesis has not visibly broken: $15B backlog (+109% YoY), BofA PT $440, 18-24 month lead times. But price structure leads narrative, and the framework does not average into a broken zone. ZONE REDRAWN DOWN to $255-275, marking the next structural base beneath the break. ENTRY REQUIRES BOTH a stabilization base AND an SMA50 reclaim. Until then: monitor only, no new capital.'),

'ANET': ('INTACT — SUPPLY CHAIN FEARS OVERBLOWN', 'ABOVE ZONE — $211 TRENDING', 'vd-caution',
  'Call Up — Aug 13, 2026: ANET $210.50, up 24.8% in four weeks. The spring supply-chain concern — semiconductor wafer, memory, and CPU shortages flagged by CEO Ullal — has not derailed anything; the $8.9B defensive purchase commitments look like good management rather than a warning. SMA50 $172.58 rising, SMA100 $161.06 below it, price above both: clean structure. ZONE REDRAWN to $172-190 on the rising SMA50, stop $158 beneath it but above the SMA100. FY2026 guide $11.5B (+28%) and $3.5B of AI fabric revenue confirm that Ultra Ethernet is taking real share from InfiniBand in AI cluster networking. The EOS switching-cost moat is structural and supply-independent. No entry at $211 — wait for a pullback toward the SMA50.'),

'AVGO': ('INTACT — WEAKEST TREND AMONG GATE PASSES', 'ABOVE ZONE — $416 WATCH SMA50', 'vd-caution',
  'Call Up — Aug 13, 2026: AVGO $416.05, up 12.2% in four weeks. Notable structure: SMA50 $393.47 and SMA100 $390.98 sit almost exactly on top of each other, forming an unusually tight and well-defined support shelf. ZONE REDRAWN to $390-408 on that confluence, stop $368 below the July low $370.83. THE CAVEAT: the SMA50 is roughly FLAT rather than clearly rising, which makes AVGO the weakest trend among the eight names currently passing the gate. It also has the messiest recent history — POTW at $360, blocked by the gate, rallied +11% to $401, round-tripped back to $371, and has now recovered to $416. That whipsaw is why the gate exists and also why this name demands patience. Q1 AI revenue $8.4B (+106% YoY), Hock Tan targeting $100B AI revenue by 2027, $73B backlog. Watch whether the SMA50 turns up or rolls over — that resolves the trend question.'),

'NOW':  ('CONFIRMED — UPTREND ESTABLISHED', 'OPEN +21% — TRAIL TO $113', 'vd-strong',
  'Call Up — Aug 13, 2026 (POTW WINNER): NOW $124.94 — up 21.0% from the $103.24 zone-floor entry called in the Jul 19-25 Play of the Week. The thesis was that a pullback to the zone floor IMPROVES risk/reward rather than degrading the setup, provided the floor holds and the SMA50 keeps rising. Both conditions held exactly. THE STRUCTURAL MILESTONE: NOW now trades above ALL FOUR moving averages — SMA50 $107.59, SMA100 $102.84, SMA150 $107.83, and critically SMA200 $122.44. Clearing the SMA200 is what converts this from the early-stage recovery flagged with an inverted-stack caveat since May into a confirmed uptrend. That caveat is now retired. ACTION: raise the trail stop from $88 to $113 (2x ATR of $5.95 below current price), locking in +9.5% while leaving a full two-ATR band for normal volatility. Remaining R/R to the $175 target is 4.2:1 — still through the gate. DO NOT add at $125; the entry was $103 and that window is closed. Zone redrawn to $112-122 for new money only. Watch $122.44 — the reclaimed SMA200 should now act as support, and a close back beneath it would be the first warning well before the trail is reached.'),
}

count = 0
for ticker, (thesis, verdict, vcls, alert) in UPDATES.items():
    def esc(s):
        return s.replace('\\', '\\\\').replace("'", "\\'")
    replacement = (
        "    thesis:'" + esc(thesis) + "', verdict:'" + esc(verdict) +
        "', verdictCls:'" + vcls + "',\n"
        "    alert:'" + esc(alert) + "',\n"
    )
    # match the thesis+alert pair inside this ticker's block
    pat = (r"(\n  " + ticker + r": \{.*?)"
           r"\n    thesis:'(?:[^'\\]|\\.)*', verdict:'(?:[^'\\]|\\.)*', verdictCls:'[^']*',"
           r"\n    alert:'(?:[^'\\]|\\.)*',\n")
    new_src, n = re.subn(pat, lambda m: m.group(1) + "\n" + replacement, src, flags=re.DOTALL)
    if n != 1:
        print(f'ERROR: {ticker} matched {n} times (expected 1)')
        sys.exit(1)
    src = new_src
    count += 1

open(FILE, 'w').write(src)
print(f'OK - updated {count} MONITOR_DATA entries')
os.remove(FILE + '.bak')
print('Cleaned up backup file')
