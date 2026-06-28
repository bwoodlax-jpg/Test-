# Scalper Brief — Saturday June 27, 2026 (EOW)
> Manually curated — live news requires: `FINNHUB_KEY=xxx python3 news_scalper.py` (run locally)
> Zone data current as of Jun 22 call up | Prices last confirmed Jun 18–22

---

## ZONE ALERTS

| Level | Ticker | Last Known Price | Zone | Stop | Status | Action |
|-------|--------|-----------------|------|------|--------|--------|
| 🔴 RED | **MSFT** | ~$379 (Jun 18) | $393–$412 | $372 | NEAR STOP | WATCH — $379 vs stop $372 = ~$7 buffer. Any move to $373 or below = EXIT immediately. |
| 🔴 RED | **NOW** | ~$95 (Jun 18) | $103–$118 | $88 | STAND-DOWN / BELOW ZONE | Stand-down in effect. Price must reclaim $103+ before any entry. Stop $88 is the floor. |
| 🟢 GREEN | **ORCL** | ~$184 (Jun 18) | $165–$182 | $148 | APPROACHING ZONE ($2 above top) | ENTRY TRIGGER WATCH — Alert live at $183. Zone top $182. Touch = entry. Stop $148. Target $275. R/R 4.0:1. SIZE: 1% bankroll. |
| 🟡 YELLOW | **MRVL** | ~$311 (Jun 18) | $220–$242 | trail $290 | ABOVE ZONE — TRAIL STOP ACTIVE | Trail stop raised to $290 after S&P 500 inclusion Jun 22. If MRVL closed week below $290 = EXIT. Hold if $290+. CHECK FRIDAY CLOSE. |
| ⚪ GRAY | **NVDA** | ~$210 (Jun 18) | $175–$192 | $155 | ABOVE ZONE | No action. Monitor $192 for re-entry pullback. |
| ⚪ GRAY | **AMD** | ~$536 (Jun 18) | $370–$390 | $348 | FAR ABOVE ZONE | No action. |
| ⚪ GRAY | **PLTR** | ~$128 (Jun 18) | $108–$122 | $95 | ABOVE ZONE | Trail stop $95 intact. Monitor. |
| ⚪ GRAY | **AVGO** | ~$411 (Jun 18) | $350–$375 | $328 | ABOVE ZONE | Monitor $375 for re-entry. |
| ⚪ GRAY | **ANET** | ~$170 (Jun 18) | $128–$148 | $112 | ABOVE ZONE | No action. |
| ⚪ GRAY | **PANW** | ~$288 (Jun 18) | $232–$252 | $215 | ABOVE ZONE | No action. |
| ⚪ GRAY | **DELL** | ~$410 (Jun 18) | $335–$355 | $310 | ABOVE ZONE | No action. |
| ⚪ GRAY | **VRT** | ~$333 (Jun 18) | $290–$312 | $268 | ABOVE ZONE | No action. |
| ⚪ GRAY | **LMND** | ~$59 (Jun 18) | $45–$56 | $38 | ABOVE ZONE | No action. No chase. |

**⚠️ CRITICAL FIRST CHECK FOR MONDAY JUN 30:** Get MSFT, ORCL, and MRVL Friday Jun 27 closes before anything else.

---

## ⚡ GAP WATCH

No live gap data — requires local `news_scalper.py` with Finnhub key.

**Framework gap rules to apply when Monday prices come in:**
- MSFT gap down through $372 → STOP TRIGGERED. Exit before open if possible.
- ORCL gap down to $182 or below → ENTRY TRIGGERED. Size 1% bankroll. Stop $148.
- MRVL gap down through $290 → TRAIL STOP TRIGGERED. Exit.
- Any name gap up >3% above zone → do NOT chase. Wait for zone re-test.

---

## 📅 EARNINGS CALENDAR (Next 30 Days — Watchlist)

| Ticker | Expected Window | Key Metric to Watch |
|--------|----------------|---------------------|
| No imminent earnings for the 13 names in next 2 weeks | | |
| PLTR | ~Early Aug 2026 | AIP commercial revenue growth + DIA contract update |
| NVDA | ~Late Aug 2026 | Q2 FY2027 — Blackwell GB300 ramp, China export update |
| ORCL | ~Sep 2026 | Q1 FY2027 — AI cloud RPO growth vs $523B backlog |
| AVGO | ~Sep 2026 | Q3 FY2026 — AI revenue rate toward CEO $100B guide |

*Dates approximate — verify with Finnhub or Robinhood before event.*

---

## 🚀 CATALYST SIGNALS

### 🟢 MRVL — S&P 500 Inclusion (Jun 22) `[MRVL]`
- S&P 500 index funds (Vanguard, BlackRock, State Street) forced to buy on Monday Jun 22.
- Price was $311 going in (+18% from $263 entry). Trail stop $290.
- **Action:** Post-inclusion selling is common after forced buying exhausts. Check if $290 held all week. If yes, hold. If no, exit was triggered.

### 🟢 ORCL — Beat-But-Fell Recovery + Zone Entry `[ORCL]`
- ORCL reported Jun 10, beat estimates, fell -9% toward zone.
- $184 on Jun 18 = $2 above zone top $182. Alert at $183.
- **Action:** Any Jun 22–27 touch of $182 or below = entry triggered. Confirm with Robinhood.

### 🟡 GFS — Existing Position `[GFS]`
- 12 shares @ $85.24. No imminent catalyst. Hold. Check current price.

---

## 🌐 MACRO SIGNALS

### ✅ CLEARED — Iran Nuclear Deal (Geneva Jun 19)
- Risk-on maximum. WTI $80 (-18% from $97+). VIX ~16. QQQ $739+.
- No further macro drag from oil or geopolitical risk for now.

### ✅ CLEARED — Warsh FOMC Hold (Jun 17, 3.50–3.75%)
- Rate neutral. No hike. No cut. Framework gates cleared for MSFT/NOW zone entries.
- Next FOMC: late July 2026. Watch Warsh commentary on jobs vs inflation balance.

### 🔍 WATCH — AI Capex Cycle
- NVDA Blackwell GB300 ramp, AMD MI400 Q3 2026 launch approaching.
- Any hyperscaler capex revision = major signal for NVDA/AMD/DELL/VRT/ANET/AVGO.

---

## ⚠️ RISK SIGNALS

### MSFT — Stop $372 Proximity `[MSFT]`
- $379 on Jun 18 = $7 above stop. One red day can trigger it.
- Stand-down remains in effect (price below zone $393–$412).
- **Action:** If $372 breaks → EXIT. No averaging down. No adds below zone.

### NOW — Below Zone Stand-Down `[NOW]`
- $95 on Jun 18 vs zone floor $103. Stand-down until $103 reclaimed.
- Thesis intact (Otto AI agent + Experian deal). Just below structural support.
- **Action:** Watch for $103 reclaim as re-entry trigger. Stop $88 is hard floor.

---

## 📋 MONDAY JUN 30 OPEN CHECKLIST (For Claude Trading)

1. [ ] Get MRVL Friday close → held $290 trail? Yes = hold | No = exit was triggered
2. [ ] Get ORCL price → touched $182 this week? Yes = entry filled | No = alert still live
3. [ ] Get MSFT price → above $376? Red alert if $373 or below
4. [ ] Get GFS current price → check vs $85.24 cost basis
5. [ ] Run SMA Stack scanner → SMA tab in dashboard → Run Scan with Finnhub key
6. [ ] Check NOW → did it reclaim $103? If yes, entry window opens
7. [ ] No new positions until zone confirmations above are resolved

**Scalper sizing this week:** 1% bankroll max per new entry. ORCL is the primary. No chasing.

---

> **Live news:** Run locally before market open: `FINNHUB_KEY=your_key python3 news_scalper.py`
> **Brief written:** Jun 27, 2026 — manual curation (cloud session blocks all external news sources)
> **Claude Trading:** "Read scalper_brief.md — give me the top 3 actionable items for Monday open."
