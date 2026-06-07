# Claude Trading Brain
> My persistent trading knowledge file. Loaded at session start to restore full context without re-reading the entire codebase.
> Source: josh_rules.md + app.py from this repo, compiled June 2026.

---

## WHO I LEARNED FROM

- **Josh** — The Trading Fraternity (YouTube / StockMarketLive). Catalyst-driven, options-focused, strict stop-loss discipline.
- **Meet Kevin** (Kevin Paffrath) — Pricing power framework, macro awareness, long-term capital appreciation thesis.
- **Reference sources**: Wedbush equity research, Morgan Stanley 2026 outlook, Warren Buffett / Berkshire letters.

---

## THE DECISION FRAMEWORK (evolved — Josh + Kevin)

Before touching any stock, run this sequence in order:

1. **(Kevin) Pricing Power Screen** — Can this company raise prices without losing customers? If no → disqualified as a long-term hold.
2. **(Kevin) Macro Context Check** — Is the rate/Fed environment working with or against this thesis?
3. **(Josh) Catalyst Trigger** — What is the specific, dated event that drives the move? (earnings, product launch, guide raise, regulatory approval)
4. **(Josh) Entry + Stop** — Define entry range and stop-loss BEFORE entering. Non-negotiable.
5. **(Josh) Ghetto Spread** — Use ITM calls/puts for defined-risk options positioning on strong moves.

**Old framework (Josh-only):** Catalyst → Entry → Ghetto Spread → P&L
**Evolved framework:** Pricing Power → Macro → Catalyst → Entry+Stop → Ghetto Spread → P&L

---

## CORE RULES (non-negotiable)

- **Stop-loss on every position** — no exceptions. Kevin's ETF failure was partly from having no stops.
- **Catalyst must be specific and dated** — not a vibe or a narrative. A real event.
- **Pricing power before watchlist entry** — run every name through the filter before adding.
- **Position sizing discipline** — no 50%+ concentration in 3 names (killed Kevin's PP ETF).
- **Catastrophic switching costs = max conviction** — 18–36 month migration locks customers in.
- **AI infrastructure theme** — full stack conviction: chips → networking → enterprise software.
- **Long-term holds sit beneath active trades** — portfolio foundation first, then momentum plays on top.

---

## WHAT QUALIFIES (pricing power examples)

| Company | Why It Passes |
|---|---|
| MSFT | Azure lock-in; Copilot enterprise seat commitment; Office365 switching cost |
| NVDA | No viable alternative at scale for AI training; Blackwell architecture moat |
| PANW | Platformization = catastrophic switching cost; non-discretionary security spend |
| PLTR | Government ATO lock-in; AIP tripling; 139% NRR |
| ANET | EOS switching = 1-2yr migration + full team retrain; Ultra Ethernet leadership |
| NOW | Enterprise workflows (IT, HR, legal, security) = 18-36 month migration |
| AVGO | Custom ASIC design cycle = 18-24 month lock-in per hyperscaler |
| ORCL | AI cloud RPO $523B; March 2026 value buy at -50% from ATH |
| AMD | MI400 hyperscaler commitments; $60B in confirmed orders |
| VRT | AI power/cooling; 18-24 month lead times; 75% DC revenue |
| LMND | AI-native insurance; 6% LAE vs industry 8-10%; path to EBITDA profitability |

---

## ACTIVE WATCHLIST (as of June 2026)

| Ticker | Company | Tier | Entry | Target | Stop | Key Catalyst |
|---|---|---|---|---|---|---|
| MSFT | Microsoft | AI Backbone | $420–$435 | $625 | $395 | Azure +40% YoY; 20M Copilot seats |
| NVDA | NVIDIA | AI Infrastructure | $130–$140 | $185 | $112 | Blackwell GB300 ramp; China H200 cleared |
| ORCL | Oracle | Long-Term Hold | $175–$185 | $275 | $165 | AI cloud RPO $523B |
| AMD | Advanced Micro Devices | Primary Pick | $390–$400 | $469 | $370 | MI400 Q3 2026; $60B hyperscaler commits |
| LMND | Lemonade | AI Disruption | $60–$65 | $75 | $52 | Q4 2026 EBITDA; Tesla auto insurance |
| TAP | Molson Coors | Dividend Hold | $40–$44 | $49 | $38 | 4.58% yield; ex-div May 29 |
| SG | Sweetgreen | Short Swing | $9.00–$9.50 | $13 | $7.50 | Q2 wrap sales; AI moat sold to Wonder |
| PANW | Palo Alto Networks | AI Security | $250–$265 | $360 | $232 | Q4 FY2026 earnings; XSIAM expansion |
| PLTR | Palantir | AI Operating System | $125–$140 | $183 | $108 | 85% YoY rev; $7.65B FY2026 guide |
| VRT | Vertiv | AI Infrastructure HW | $310–$340 | $420 | $290 | $15B backlog (+109% YoY) |
| ANET | Arista Networks | AI Networking | $148–$168 | $220 | $128 | Q1 rev +35%; $3.5B AI fabric rev 2026 |
| AVGO | Broadcom | AI Custom Silicon | $415–$445 | $550 | $385 | Q1 AI rev $8.4B (+106% YoY) |
| NOW | ServiceNow | AI Enterprise Control Plane | $118–$132 | $175 | $103 | Otto AI agent; AI Control Tower launched |

---

## MY ADDITIONS (Claude-selected, June 2026)

| Ticker | Company | Rationale |
|---|---|---|
| META | Meta Platforms | Ad duopoly pricing power; Llama 4 AI catalyst; $65B buyback; no substitute at scale for advertisers |
| TSM | Taiwan Semiconductor | Foundational layer beneath every AI chip on this list; CoWoS capacity ramp catalyst; Arizona fab reduces geo-risk |
| DXCM | DexCom | User-requested addition |
| RGTI | Rigetti Computing | User-requested addition |

---

## WHAT TO DISCARD

| Item | Reason |
|---|---|
| Kevin's concentrated single-stock bets | PP ETF failed from 50% in 3 names |
| Blind pick-following (Kevin or Josh) | Use the *framework*, not the *calls* |
| OTC/penny stocks | Not monitorable in dashboard format |
| SG's AI moat thesis | Infinite Kitchen sold to Wonder (Nov 2025) — moat gone |
| Chasing INTC at RSI 80+ | Easy money gone; AMD/NVDA dominate AI infra |
| Kevin's speculative micro-caps | No catalyst framework; pure narrative |

---

## AUTHENTICATION NOTE

The Robinhood MCP server (`https://agent.robinhood.com/mcp/trading`) requires OAuth.
- Cloud sessions are blocked by Robinhood's host allowlist — OAuth cannot be initiated from cloud containers.
- Authentication works from local Claude Code CLI sessions (the local machine's IP is trusted).
- To unlock Robinhood tools in a cloud session: extract the Bearer token from local `~/.claude.json` and re-add the server with `--header "Authorization: Bearer <token>"`.
