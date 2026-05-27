from datetime import datetime, time
from zoneinfo import ZoneInfo

import yfinance as yf
from flask import Flask, jsonify, render_template

app = Flask(__name__)

WATCHLIST = [
    {"ticker": "MSFT", "company": "Microsoft Corporation",    "tier": "AI Backbone",      "tier_class": "t1", "entry": "$420–$435", "target": "$625", "stop": "$395",  "catalyst": "Azure +40% YoY; 20M Copilot seats; Wedbush PT $625",      "note": "Pricing power maximum — enterprise AI backbone. Both frameworks max conviction."},
    {"ticker": "NVDA", "company": "NVIDIA Corporation",       "tier": "AI Infrastructure","tier_class": "t2", "entry": "$130–$140", "target": "$185", "stop": "$112",  "catalyst": "Blackwell GB300 ramp; China H200 cleared; $500B rev visibility", "note": "Dominant AI chip supplier — no substitute at scale. China reopening unlocked."},
    {"ticker": "ORCL", "company": "Oracle Corporation",       "tier": "Long-Term Hold",   "tier_class": "t1", "entry": "$175–$185", "target": "$275", "stop": "$165",  "catalyst": "AI cloud RPO $523B; Wedbush PT $275",                     "note": "Benjamin Graham value buy — March 2026 at −50% from ATH"},
    {"ticker": "AMD",  "company": "Advanced Micro Devices",   "tier": "Primary Pick",     "tier_class": "t2", "entry": "$390–$400", "target": "$469", "stop": "$370",  "catalyst": "MI400 Q3 2026 launch; $60B hyperscaler commits",          "note": "Data center dominance — fundamental + momentum play"},
    {"ticker": "LMND", "company": "Lemonade Inc.",             "tier": "AI Disruption",    "tier_class": "t2", "entry": "$60–$65",   "target": "$75",  "stop": "$52",   "catalyst": "Q4 2026 EBITDA profitability; Tesla auto insurance",       "note": "Kevin's explicit buy — AI-native insurance, 6% LAE vs industry 8-10%"},
    {"ticker": "TAP",  "company": "Molson Coors Beverage",    "tier": "Dividend Hold",    "tier_class": "t1", "entry": "$40–$44",   "target": "$49",  "stop": "$38",   "catalyst": "4.58% yield; ex-div May 29 🔔",                           "note": "Long-term buy Dec 2025 — boring stock, real dividend"},
    {"ticker": "SG",   "company": "Sweetgreen Inc.",           "tier": "Short Swing",      "tier_class": "t2", "entry": "$9.00–$9.50","target": "$13", "stop": "$7.50", "catalyst": "Q2 wrap sales data — AI moat sold to Wonder Nov 2025",    "note": "Oct 2025 rate-cut buy — menu pivot; shorter horizon, tighter stop"},
    {"ticker": "PANW", "company": "Palo Alto Networks",        "tier": "AI Security",      "tier_class": "t1", "entry": "$250–$265",  "target": "$360", "stop": "$232",  "catalyst": "Q4 FY2026 earnings; XSIAM SOC expansion; AI Firewall revenue category",         "note": "Platformization = catastrophic switching cost. Non-discretionary spend + AI attack surface expansion."},
    {"ticker": "PLTR", "company": "Palantir Technologies",     "tier": "AI Operating System","tier_class": "t1", "entry": "$125–$140",  "target": "$183", "stop": "$108",  "catalyst": "85% YoY revenue; $7.65B FY2026 guide; government ATO lock-in; commercial AIP tripling", "note": "AI data fabric for government + enterprise. 139% NRR. Verified ~$137 May 26."},
    {"ticker": "VRT",  "company": "Vertiv Holdings Co",        "tier": "AI Infrastructure Hardware","tier_class": "t2", "entry": "$310–$340",  "target": "$420", "stop": "$290",  "catalyst": "Order backlog $15B (+109% YoY); Q1 rev +30% YoY; EPS +83% YoY; BofA PT $440", "note": "Power + cooling for every AI GPU rack. 18-24 month lead times. 75% DC revenue. Verified $327 May 26."},
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
