from datetime import datetime, time
from zoneinfo import ZoneInfo

import yfinance as yf
from flask import Flask, jsonify, render_template

app = Flask(__name__)

WATCHLIST = [
    {"ticker": "MSFT", "company": "Microsoft Corporation",    "tier": "AI Backbone",               "tier_class": "t1", "entry": "$393–$412", "target": "$625", "stop": "$372",  "catalyst": "Azure +40% YoY; 20M Copilot seats; Wedbush PT $625; Morgan Stanley PT $650", "note": "Stop-becomes-entry: $393–$412 = 2026 rate-fear consolidation base. Stop $372 = below Feb re-accumulation floor. R/R 7.3:1. ~$402 currently in zone."},
    {"ticker": "NVDA", "company": "NVIDIA Corporation",       "tier": "AI Infrastructure",         "tier_class": "t2", "entry": "$175–$192", "target": "$300", "stop": "$155",  "catalyst": "Blackwell GB300 ramp; China H200 cleared; $500B rev visibility", "note": "Stop-becomes-entry: $175–$192 = Blackwell re-rating + H200 China-clearance base. Stop $155 = below pre-China structural floor. R/R 4.1:1. Currently ~$202, above zone."},
    {"ticker": "ORCL", "company": "Oracle Corporation",       "tier": "Long-Term Hold",            "tier_class": "t1", "entry": "$165–$182", "target": "$275", "stop": "$148",  "catalyst": "AI cloud RPO $523B; Wedbush PT $275; beat-but-fell Jun 10 driving toward zone", "note": "Stop-becomes-entry: $165–$182 = Graham value zone + DB lock-in structural support. Stop $148 = below all 2025–2026 support. R/R 4.0:1."},
    {"ticker": "AMD",  "company": "Advanced Micro Devices",   "tier": "Primary Pick",              "tier_class": "t2", "entry": "$370–$390", "target": "$550", "stop": "$348",  "catalyst": "MI400 Q3 2026 launch; $60B hyperscaler commits; record $5.8B DC revenue", "note": "Stop-becomes-entry: $370–$390 = pre-May-run consolidation base. Stop $348 = below DC re-rating floor. R/R 5.3:1."},
    {"ticker": "LMND", "company": "Lemonade Inc.",             "tier": "AI Disruption",             "tier_class": "t2", "entry": "$45–$56",   "target": "$88",  "stop": "$38",   "catalyst": "Tesla autonomous insurance AZ+OR LIVE; Q4 2026 EBITDA profitability; 6% LAE vs 8–10% industry", "note": "Stop-becomes-entry: $45–$56 = structural base below Tesla announcement move. Stop $38 = below IPO-era support. Target raised to $88 (Tesla full rollout). R/R 3.0:1. Currently ~$60, above zone."},
    {"ticker": "MRVL", "company": "Marvell Technology Inc",    "tier": "AI Custom Silicon",         "tier_class": "t2", "entry": "$220–$242", "target": "$350", "stop": "$198",  "catalyst": "AWS Trainium3 + Google TPU contracts; S&P 500 inclusion Jun 22; AI ASIC rev +87% YoY", "note": "Stop-becomes-entry: $220–$242 = hyperscaler custom silicon contract base. Stop $198 = below re-rating floor. R/R 3.7:1. Currently ~$250s, above zone."},
    {"ticker": "DELL", "company": "Dell Technologies Inc",     "tier": "AI Server Assembly",        "tier_class": "t2", "entry": "$335–$355", "target": "$497", "stop": "$310",  "catalyst": "Q1 FY27: AI server rev $16.1B (+757% YoY); $51.3B record backlog; $24.4B new AI orders; FY guide $165–169B", "note": "Zone redrawn Jun 11: $335–355 = full gap-fill of May 29 earnings move. Stop $310 = below pre-earnings structural base. R/R 4.3:1."},
    {"ticker": "PANW", "company": "Palo Alto Networks",        "tier": "AI Security",               "tier_class": "t1", "entry": "$232–$252", "target": "$360", "stop": "$215",  "catalyst": "Q3 FY2026 beat + raise; NGS ARR +60% YoY; XSIAM SOC expansion; AI Firewall revenue", "note": "Stop-becomes-entry: $232–$252 = XSIAM re-rating base. Stop $215 = below platformization floor. R/R 4.4:1. Currently ~$257, approaching from above."},
    {"ticker": "PLTR", "company": "Palantir Technologies",     "tier": "AI Operating System",       "tier_class": "t1", "entry": "$108–$122", "target": "$183", "stop": "$95",   "catalyst": "85% YoY revenue; $7.65B FY2026 guide; DIA contract pending; AIP commercial tripling", "note": "Stop-becomes-entry: $108–$122 = AIP commercial ramp base. Stop $95 = below ATO lock-in support. R/R 3.4:1. Currently ~$134, above zone."},
    {"ticker": "VRT",  "company": "Vertiv Holdings Co",        "tier": "AI Infrastructure Hardware","tier_class": "t2", "entry": "$290–$312", "target": "$420", "stop": "$268",  "catalyst": "Order backlog $15B (+109% YoY); Q1 rev +30% YoY; EPS +83% YoY; BofA PT $440", "note": "Stop-becomes-entry: $290–$312 = AI DC buildout re-rating base. Stop $268 = below backlog-driven support. R/R 3.6:1."},
    {"ticker": "ANET", "company": "Arista Networks Inc",        "tier": "AI Networking",             "tier_class": "t1", "entry": "$128–$148", "target": "$220", "stop": "$112",  "catalyst": "Q1 rev +35% YoY beat; FY2026 guide $11.5B (+28%); $3.5B AI fabric revenue 2026; Ultra Ethernet Consortium leader", "note": "Stop-becomes-entry: $128–$148 = EOS switching cost base. Stop $112 = below structural moat floor. R/R 3.2:1. Currently ~$152, above zone."},
    {"ticker": "AVGO", "company": "Broadcom Inc",               "tier": "AI Custom Silicon",         "tier_class": "t2", "entry": "$350–$375", "target": "$550", "stop": "$328",  "catalyst": "Q1 AI rev $8.4B (+106% YoY); Q2 AI guide $10.7B; CEO $100B AI rev by 2027; Google TPU/Meta MTIA/ByteDance XPU lock-in", "note": "Zone redrawn: prior $415–$445 + stop $385 invalidated at ~$378. New zone = pre-Q1 accumulation base. Stop $328 = below Q4 2025 structural support. R/R 5.4:1."},
    {"ticker": "NOW",  "company": "ServiceNow Inc",             "tier": "AI Enterprise Control Plane","tier_class": "t1", "entry": "$103–$118", "target": "$175", "stop": "$88",   "catalyst": "Knowledge 2026: AI Control Tower + Otto agent; Experian multi-year agentic deal; consensus PT $142; 19/22 analysts Buy", "note": "Stop-becomes-entry: $103–$118 = AI Control Plane re-rating base. Stop $88 = below enterprise switching cost floor. R/R 3.0:1. Currently ~$108, in zone."},
]


def is_market_open():
    et = ZoneInfo("America/New_York")
    now = datetime.now(et)
    if now.weekday() >= 5:
        return False
    return time(9, 30) <= now.time() <= time(16, 0)


def fetch_quote(ticker: str) -> dict:
    try:
        t = yf.Ticker(ticker)
        fi = t.fast_info
        current   = round(float(fi.last_price), 2)
        open_p    = round(float(fi.open), 2) if fi.open else None
        prev      = round(float(fi.previous_close), 2)
        day_high  = round(float(fi.day_high), 2) if fi.day_high else None
        day_low   = round(float(fi.day_low), 2) if fi.day_low else None
        change    = round(current - prev, 2)
        change_pct = round((change / prev) * 100, 2)
        return {"current": current, "open": open_p, "prev_close": prev,
                "high": day_high, "low": day_low, "change": change,
                "change_pct": change_pct, "error": None}
    except Exception as e:
        return {"current": None, "open": None, "prev_close": None,
                "high": None, "low": None, "change": None,
                "change_pct": None, "error": str(e)}


@app.route("/")
def index():
    return render_template("index.html", watchlist=WATCHLIST)


@app.route("/api/quotes")
def quotes():
    results = {s["ticker"]: fetch_quote(s["ticker"]) for s in WATCHLIST}
    return jsonify({
        "quotes": results,
        "market_open": is_market_open(),
        "source": "yfinance",
        "timestamp": datetime.now(ZoneInfo("America/New_York")).strftime("%b %d, %Y  %I:%M:%S %p ET"),
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
