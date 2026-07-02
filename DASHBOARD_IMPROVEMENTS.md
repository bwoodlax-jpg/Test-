# Dashboard Improvement Roadmap
*Synthesized Jul 1, 2026 from a 6-dimension audit (trading-logic, data-integration, UX, code-quality, reliability, automation). Every item is grounded in the actual repo.*

---

## ⭐ The one change that matters most

**Connect the dashboard to the real account and real live data.** Right now the dashboard is an elegant *paper* simulation disconnected from reality:

- It tracks a **13-name AI watchlist of $100–580 stocks** while the account has **$13.64 buying power** — none of it is actionable.
- It showed a **phantom "GFS" position**; the real holding is **QCML** (−7%, no stop), plus 3 deep-OTM options expiring.
- **Robinhood MCP** (real quotes, positions, historicals) is available but **unused** — prices are hand-typed via Python `replace()` scripts each "call up," and `app.py`'s `/api/quotes` still imports `yfinance`, which is **403-blocked** in this environment.

Every other improvement is secondary to closing this paper-vs-real gap.

---

## A. Ship-now quick wins (small effort, high value)

| # | Problem | Fix | Sev |
|---|---------|-----|-----|
| A1 | `dashboard.html` is a 272 KB **hand-synced duplicate** of `templates/index.html` — drift risk on every commit | Add a pre-commit check (or a 1-line `make sync`) that fails if the two differ; or generate `dashboard.html` from the template in CI | high |
| A2 | The **real account isn't shown**. Phantom "GFS" was tracked instead of QCML | Add a "Real Book" strip at the top of Live Watchlist: QCML −7% (no stop!), 3 expiring options, **buying power $13.64** — already drafted in the MARKET_PULSE portfolio, promote it to a pinned banner | critical |
| A3 | **No stop on QCML**, and SOFI/CLOV expire Jul 2 with no on-screen countdown | Surface a "positions at risk" list: unprotected positions + options expiring ≤3 days | high |
| A4 | **Zone-vs-SMA conflict** (PLTR "in zone" but below all SMAs) is only explained in prose | Add a computed `smaVeto` flag per name; render a red "SMA VETO" chip next to any zone-entry verdict that fails the trend filter | high |
| A5 | Many values have **no as-of timestamp** — stale prices read as current | Add a freshness badge (`as of Jun 30 close` / `LIVE`) on every price block; grey out anything older than 1 session | medium |
| A6 | **Semis & AI** tab ships static ~2025 PE/EPS | Label it "static estimates — click Load for live," which is half-done; wire the Load button to the same live source as everything else | medium |

## B. High-impact projects (medium/large effort)

| # | Problem | Fix | Sev |
|---|---------|-----|-----|
| B1 | **Live data is manual.** Prices updated by hand; `yfinance` backend is blocked | Build a data backend that pulls **Robinhood (primary) + FMP (fallback)** for quotes/positions/historicals, writes a `state.json`, and serves it to the frontend. Kills the hand-update `replace()` scripts | critical |
| B2 | **SMA scanner runs in-browser only** (needs a pasted Finnhub key) and can't run at call-up | Move SMA computation **server-side** using Robinhood historicals (proven this session: MRVL bullish / MSFT+PLTR below all SMAs, computed from real bars). Store results in `state.json` | high |
| B3 | **The watchlist is duplicated 3×** — `app.py` `WATCHLIST`, `index.html` `MARKET_PULSE`, and `news_scalper.py` — each hand-edited | Single source of truth: one `watchlist.json` (zones/stops/targets/catalysts) consumed by app, dashboard, and scalper | high |
| B4 | **No position tracking / P&L / cost-basis** anywhere real | Pull `get_equity_positions` + `get_option_positions`, compute live P&L vs cost basis, show per-position and portfolio totals | high |
| B5 | **No alerting** on stop breaches or zone touches | A scheduled job (or session hook) that pulls quotes, diffs against stops/zones, and emits alerts ("MSFT $372 stop breached", "AVGO tagged zone top") | high |
| B6 | **Data lives inside 3,500 lines of markup**; JS entities are hand-escaped (the WOLF/CAMT apostrophe bug this session) | Extract all data blocks (`MARKET_PULSE`, `HISTORY`, `SEMI_AI_STOCKS`, `SP500_LOSERS`) to JSON files loaded at runtime; render from data, not hand-written HTML strings | medium |

## C. Nice-to-have

| # | Problem | Fix | Sev |
|---|---------|-----|-----|
| C1 | Dense 10-column tables don't reflow on mobile | Card layout under ~600px; horizontal scroll containers already partly used | medium |
| C2 | Three equal-weight "Play of the Week" cards compete for attention | Collapse historical POTWs; keep one active card expanded | low |
| C3 | **Zero tests, no build step** | Add a JS syntax check (already run manually via `node --check`) + a JSON-schema validation of the data files to CI | medium |
| C4 | `SP500_LOSERS` YTD figures stale since May; `news_scalper.py` blocked from cloud | Fold both into the B1 data backend so they refresh with everything else | low |
| C5 | Default tab is the paper watchlist | Default to a "Today" view: real book + at-risk positions + the one actionable setup | medium |

---

## 🎯 If you only do five things

1. **Pin the real account** to the top of the dashboard — QCML (set a stop!), expiring options, **$13.64 buying power** — so the paper watchlist can never again be mistaken for the real book. *(A2/A3, small)*
2. **Build the Robinhood/FMP data backend** (`state.json`) and delete the hand-update `replace()` scripts + the dead `yfinance` path. *(B1, large)*
3. **Move the SMA scan server-side** off Robinhood historicals and store the stack per name. *(B2, medium)*
4. **One `watchlist.json` source of truth** feeding app + dashboard + scalper. *(B3, medium)*
5. **Add stop/zone-breach alerting** so a $372 MSFT break or an AVGO zone tag reaches you without a manual call-up. *(B5, medium)*

*Audit method: 6 parallel dimension reviewers → adversarial verification → synthesis. Verification/synthesis were cut short by a session cap; findings were re-verified against the code by hand.*
