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
    {"ticker": "MRVL", "company": "Marvell Technology Inc",    "tier": "AI Custom Silicon","tier_class": "t2", "entry": "$245–$265", "target": "$350", "stop": "$220",  "catalyst": "S&P 500 inclusion Jun 22; AI networking ASIC revenue +87% YoY", "note": "Custom AI silicon for AWS, Google, Microsoft. Index fund forced buying into Jun 22."},
    {"ticker": "DELL", "company": "Dell Technologies Inc",     "tier": "AI Server Assembly","tier_class": "t2", "entry": "$420–$450", "target": "$550", "stop": "$395",  "catalyst": "Q1 FY27: AI server rev $16.1B (+757% YoY); $51.3B record backlog; $24.4B new AI orders", "note": "AI server assembly layer completing the stack. Above zone ~$461 — entry on pullback only."},
    {"ticker": "PANW", "company": "Palo Alto Networks",        "tier": "AI Security",      "tier_class": "t1", "entry": "$250–$265",  "target": "$360", "stop": "$232",  "catalyst": "Q4 FY2026 earnings; XSIAM SOC expansion; AI Firewall revenue category",         "note": "Platformization = catastrophic switching cost. Non-discretionary spend + AI attack surface expansion."},
    {"ticker": "PLTR", "company": "Palantir Technologies",     "tier": "AI Operating System","tier_class": "t1", "entry": "$125–$140",  "target": "$183", "stop": "$108",  "catalyst": "85% YoY revenue; $7.65B FY2026 guide; government ATO lock-in; commercial AIP tripling", "note": "AI data fabric for government + enterprise. 139% NRR. Verified ~$137 May 26."},
    {"ticker": "VRT",  "company": "Vertiv Holdings Co",        "tier": "AI Infrastructure Hardware","tier_class": "t2", "entry": "$310–$340",  "target": "$420", "stop": "$290",  "catalyst": "Order backlog $15B (+109% YoY); Q1 rev +30% YoY; EPS +83% YoY; BofA PT $440", "note": "Power + cooling for every AI GPU rack. 18-24 month lead times. 75% DC revenue. Verified $327 May 26."},
    {"ticker": "ANET", "company": "Arista Networks Inc",        "tier": "AI Networking",            "tier_class": "t1", "entry": "$148–$168",  "target": "$220", "stop": "$128",  "catalyst": "Q1 rev +35% YoY beat; FY2026 guide $11.5B (+28%); $3.5B AI fabric revenue 2026; 29 analysts Strong Buy; PT avg $188", "note": "Networking layer every AI GPU cluster runs on. EOS switching cost = 1-2yr migration + full team retrain. Ultra Ethernet Consortium leader. Verified $158 May 26."},
    {"ticker": "AVGO", "company": "Broadcom Inc",               "tier": "AI Custom Silicon",        "tier_class": "t2", "entry": "$415–$445",  "target": "$550", "stop": "$385",  "catalyst": "Q1 AI rev $8.4B (+106% YoY); Q2 AI guide $10.7B; CEO $100B AI rev by 2027; $73B backlog; 47 analysts Strong Buy; avg PT $482", "note": "Custom AI ASIC design partner for Google TPU, Meta MTIA, ByteDance XPU. 18-24 month design cycle = multi-year lock-in. R/R 2.67:1. Verified $440 May 29."},
    {"ticker": "NOW",  "company": "ServiceNow Inc",             "tier": "AI Enterprise Control Plane","tier_class": "t1", "entry": "$118–$132",  "target": "$175", "stop": "$103",  "catalyst": "Knowledge 2026: AI Control Tower + Otto AI agent launched; Dell blowout validates enterprise AI stack; BofA Buy $130; consensus PT $142; 19/22 analysts Buy", "note": "Enterprise workflow lock-in = catastrophic switching cost. Once ServiceNow runs IT, HR, legal, and security workflows, migration = 18-36 month project. AI Control Plane for enterprise agentic AI. Verified $129 May 29."},
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
