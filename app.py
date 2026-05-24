from datetime import datetime, time
from zoneinfo import ZoneInfo

import yfinance as yf
from flask import Flask, jsonify, render_template

app = Flask(__name__)

WATCHLIST = [
    {"ticker": "ORCL", "company": "Oracle Corporation",       "tier": "Long-Term Hold",   "tier_class": "t1", "entry": "$175–$185", "target": "$275", "stop": "$165",  "catalyst": "AI cloud RPO $523B; Wedbush PT $275",          "note": "Benjamin Graham value buy — March 2026 at −50% from ATH"},
    {"ticker": "AMD",  "company": "Advanced Micro Devices",   "tier": "Momentum / Swing", "tier_class": "t2", "entry": "$390–$400", "target": "$469", "stop": "$370",  "catalyst": "MI400 Q3 2026 launch; $60B hyperscaler commits", "note": "Data center dominance — fundamental + momentum play"},
    {"ticker": "TAP",  "company": "Molson Coors Beverage",    "tier": "Dividend Hold",    "tier_class": "t1", "entry": "$40–$44",   "target": "$49",  "stop": "$38",   "catalyst": "4.58% yield; ex-div May 29 🔔",                "note": "Long-term buy Dec 2025 — boring stock, real dividend"},
    {"ticker": "SG",   "company": "Sweetgreen Inc.",           "tier": "Swing / Growth",   "tier_class": "t2", "entry": "$9.00–$9.50","target": "$13", "stop": "$7.50", "catalyst": "Wrap launch; JPMorgan upgrade PT $13",          "note": "Oct 2025 rate-cut buy — menu pivot driving recovery"},
    {"ticker": "INTC", "company": "Intel Corporation",         "tier": "Watch Only ⚠",    "tier_class": "t3", "entry": "$95–$105",  "target": "$132+","stop": "N/A",   "catalyst": "Terafab; CHIPS Act; Apple foundry talks",      "note": "RSI 80+ — DO NOT CHASE. Josh's top 2026 call but up 5× from lows."},
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
