from datetime import datetime, time
from zoneinfo import ZoneInfo
import time as _time

import yfinance as yf
from flask import Flask, jsonify, render_template

app = Flask(__name__)

WATCHLIST = [
    {"ticker": "MSFT", "company": "Microsoft Corporation",    "tier": "AI Backbone",               "tier_class": "t1", "entry": "$393–$412", "target": "$625", "stop": "$372",  "catalyst": "Azure +40% YoY; 20M Copilot seats; Wedbush PT $625; Morgan Stanley PT $650", "note": "🔴 Jul 1 (live): $373.02 Jun 30 = $1 above stop $372. BEARISH SMA stack (below 50=$410/100=$401/150=$425/200=$447). Zone $393–$412 now sits above all price action = stale. Stand-down validated; no entry. If $372 breaks, thesis dead."},
    {"ticker": "NVDA", "company": "NVIDIA Corporation",       "tier": "AI Infrastructure",         "tier_class": "t2", "entry": "$175–$192", "target": "$300", "stop": "$155",  "catalyst": "Blackwell GB300 ramp; China H200 cleared; $500B rev visibility", "note": "Jul 1 (live): $200.09 Jun 30 (pulled back from $210). Above zone $175–192. Monitor for deeper pullback to zone. Stop $155, R/R 4.1:1 at zone."},
    {"ticker": "ORCL", "company": "Oracle Corporation",       "tier": "Long-Term Hold",            "tier_class": "t1", "entry": "$165–$182", "target": "$275", "stop": "$148",  "catalyst": "AI cloud RPO $523B; Wedbush PT $275; beat-but-fell Jun 10 driving toward zone", "note": "🔪 Jul 1 (live): $146.55 Jun 30 — BROKE $148 stop, fell $18 through zone $165–182. Setup DEAD (falling knife, not value). Had a zone entry triggered it would have stopped out ~-19%. Re-evaluate only after a base + reclaim $150+."},
    {"ticker": "AMD",  "company": "Advanced Micro Devices",   "tier": "Primary Pick",              "tier_class": "t2", "entry": "$370–$390", "target": "$550", "stop": "$348",  "catalyst": "MI400 Q3 2026 launch; $60B hyperscaler commits; record $5.8B DC revenue", "note": "Stop-becomes-entry: $370–$390 = pre-May-run consolidation base. Stop $348 = below DC re-rating floor. R/R 5.3:1."},
    {"ticker": "LMND", "company": "Lemonade Inc.",             "tier": "AI Disruption",             "tier_class": "t2", "entry": "$45–$56",   "target": "$88",  "stop": "$38",   "catalyst": "Tesla autonomous insurance AZ+OR LIVE; Q4 2026 EBITDA profitability; 6% LAE vs 8–10% industry", "note": "Stop-becomes-entry: $45–$56 = structural base below Tesla announcement move. Stop $38 = below IPO-era support. Target raised to $88 (Tesla full rollout). R/R 3.0:1. Currently ~$60, above zone."},
    {"ticker": "MRVL", "company": "Marvell Technology Inc",    "tier": "AI Custom Silicon",         "tier_class": "t2", "entry": "$220–$242", "target": "$350", "stop": "$198→trail $290",  "catalyst": "AWS Trainium3 + Google TPU contracts; S&P 500 inclusion Jun 22; AI ASIC rev +87% YoY", "note": "🟢 Jul 1 (live): $297.89 Jun 30 (AH $293.53). ONLY bullish full SMA stack on the board (above 50=$216 rising/100=$154/150=$131/200=$120). Trail $290 (~$3 under price). Trim above $305, hard exit below $290. No adds."},
    {"ticker": "DELL", "company": "Dell Technologies Inc",     "tier": "AI Server Assembly",        "tier_class": "t2", "entry": "$335–$355", "target": "$497", "stop": "$310",  "catalyst": "Q1 FY27: AI server rev $16.1B (+757% YoY); $51.3B record backlog; $24.4B new AI orders; FY guide $165–169B", "note": "Zone redrawn Jun 11: $335–355 = full gap-fill of May 29 earnings move. Stop $310 = below pre-earnings structural base. R/R 4.3:1."},
    {"ticker": "PANW", "company": "Palo Alto Networks",        "tier": "AI Security",               "tier_class": "t1", "entry": "$232–$252", "target": "$360", "stop": "$215",  "catalyst": "Q3 FY2026 beat + raise; NGS ARR +60% YoY; XSIAM SOC expansion; AI Firewall revenue", "note": "Stop-becomes-entry: $232–$252 = XSIAM re-rating base. Stop $215 = below platformization floor. R/R 4.4:1. Currently ~$257, approaching from above."},
    {"ticker": "PLTR", "company": "Palantir Technologies",     "tier": "AI Operating System",       "tier_class": "t1", "entry": "$108–$122", "target": "$183", "stop": "$95",   "catalyst": "85% YoY revenue; $7.65B FY2026 guide; DIA contract pending; AIP commercial tripling", "note": "🔪 Jul 1 (live): $116.67 Jun 30 — IN zone $108–122 but BELOW all SMAs (50=$136 falling/100=$140/150=$151/200=$159). Trend filter VETOES the zone: declining SMA50 negates entry. NO buy until SMA50 flattens/turns. Stop $95, target $183."},
    {"ticker": "VRT",  "company": "Vertiv Holdings Co",        "tier": "AI Infrastructure Hardware","tier_class": "t2", "entry": "$290–$312", "target": "$420", "stop": "$268",  "catalyst": "Order backlog $15B (+109% YoY); Q1 rev +30% YoY; EPS +83% YoY; BofA PT $440", "note": "Stop-becomes-entry: $290–$312 = AI DC buildout re-rating base. Stop $268 = below backlog-driven support. R/R 3.6:1."},
    {"ticker": "ANET", "company": "Arista Networks Inc",        "tier": "AI Networking",             "tier_class": "t1", "entry": "$128–$148", "target": "$220", "stop": "$112",  "catalyst": "Q1 rev +35% YoY beat; FY2026 guide $11.5B (+28%); $3.5B AI fabric revenue 2026; Ultra Ethernet Consortium leader", "note": "Stop-becomes-entry: $128–$148 = EOS switching cost base. Stop $112 = below structural moat floor. R/R 3.2:1. Currently ~$152, above zone."},
    {"ticker": "AVGO", "company": "Broadcom Inc",               "tier": "AI Custom Silicon",         "tier_class": "t2", "entry": "$350–$375", "target": "$550", "stop": "$328",  "catalyst": "Q1 AI rev $8.4B (+106% YoY); Q2 AI guide $10.7B; CEO $100B AI rev by 2027; Google TPU/Meta MTIA/ByteDance XPU lock-in", "note": "🟡 Jul 1 (live): $377.75 Jun 30 — right at zone top $375. First quality name pulling back TO its zone (not through). Not an entry yet; needs to hold + turn off rising SMA. Stop $328, target $550, R/R 5.4:1. One to watch."},
    {"ticker": "NOW",  "company": "ServiceNow Inc",             "tier": "AI Enterprise Control Plane","tier_class": "t1", "entry": "$103–$118", "target": "$175", "stop": "$88",   "catalyst": "Knowledge 2026: AI Control Tower + Otto agent; Experian multi-year agentic deal; consensus PT $142; 19/22 analysts Buy", "note": "🟡 Jul 1 (live): $99.28 Jun 30 (recovered from $95). Still below zone floor $103. Thesis intact (Otto AI + Experian). Re-entry only on sustained $103+ close. Stop $88 = hard floor."},
]

# ── SMA Stack Scanner ────────────────────────────────────────────────────────
SMA_UNIVERSE = [
    # Mega/Large-cap tech
    "AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA",
    "AMD", "ORCL", "CRM", "ADBE", "INTC", "QCOM", "TXN", "AVGO", "MU",
    "AMAT", "LRCX", "KLAC", "MRVL", "SNPS", "CDNS", "DELL", "ANET", "IBM", "ACN", "INTU",
    # Cybersecurity / Cloud SaaS
    "PANW", "FTNT", "CRWD", "ZS", "NET", "OKTA",
    "DDOG", "SNOW", "PLTR", "NOW", "HUBS", "WDAY", "VEEV", "ZM", "UBER",
    # Financials
    "JPM", "BAC", "GS", "MS", "V", "MA", "AXP", "BLK", "SCHW", "COF",
    "SPGI", "CME", "ICE", "PNC", "USB",
    # Healthcare
    "LLY", "ABBV", "JNJ", "MRK", "AMGN", "REGN", "VRTX", "ISRG",
    "UNH", "MDT", "ABT", "SYK", "BSX", "EW", "HCA",
    # Consumer Discretionary
    "HD", "LOW", "TGT", "COST", "MCD", "SBUX", "CMG", "NKE",
    "TSCO", "BKNG", "MAR", "HLT", "ABNB",
    # Consumer Staples
    "WMT", "PG", "KO", "PEP", "PM", "MDLZ", "CL",
    # Energy
    "XOM", "CVX", "COP", "EOG", "DVN", "SLB", "OXY", "MPC", "VLO", "PSX",
    # Industrials
    "GE", "HON", "CAT", "DE", "UNP", "FDX", "UPS", "RTX", "LMT", "BA", "TDG",
    "ROK", "EMR", "ETN", "CARR",
    # Communication
    "NFLX", "DIS", "TMUS", "CMCSA",
    # Materials
    "FCX", "APD", "LIN", "SHW", "NEM", "ECL",
    # Real Estate / Infra
    "AMT", "PLD", "EQIX", "CCI", "DLR",
    # Utilities
    "NEE", "DUK", "SO",
    # Mid-cap specials
    "VRT", "LMND", "MELI", "SE", "DASH", "RBLX", "ARM", "SMCI", "MRNA",
]

_COMPANY = {
    "AAPL":"Apple Inc","MSFT":"Microsoft Corp","GOOGL":"Alphabet Inc","AMZN":"Amazon.com Inc",
    "META":"Meta Platforms","NVDA":"NVIDIA Corp","TSLA":"Tesla Inc","AMD":"Advanced Micro Devices",
    "ORCL":"Oracle Corp","CRM":"Salesforce Inc","ADBE":"Adobe Inc","INTC":"Intel Corp",
    "QCOM":"Qualcomm Inc","TXN":"Texas Instruments","AVGO":"Broadcom Inc","MU":"Micron Technology",
    "AMAT":"Applied Materials","LRCX":"Lam Research","KLAC":"KLA Corp","MRVL":"Marvell Technology",
    "SNPS":"Synopsys Inc","CDNS":"Cadence Design","DELL":"Dell Technologies","ANET":"Arista Networks",
    "IBM":"IBM Corp","ACN":"Accenture plc","INTU":"Intuit Inc","PANW":"Palo Alto Networks",
    "FTNT":"Fortinet Inc","CRWD":"CrowdStrike Holdings","ZS":"Zscaler Inc","NET":"Cloudflare Inc",
    "OKTA":"Okta Inc","DDOG":"Datadog Inc","SNOW":"Snowflake Inc","PLTR":"Palantir Technologies",
    "NOW":"ServiceNow Inc","HUBS":"HubSpot Inc","WDAY":"Workday Inc","VEEV":"Veeva Systems",
    "ZM":"Zoom Video","UBER":"Uber Technologies","JPM":"JPMorgan Chase","BAC":"Bank of America",
    "GS":"Goldman Sachs","MS":"Morgan Stanley","V":"Visa Inc","MA":"Mastercard Inc",
    "AXP":"American Express","BLK":"BlackRock Inc","SCHW":"Charles Schwab","COF":"Capital One",
    "SPGI":"S&P Global Inc","CME":"CME Group","ICE":"Intercontinental Exchange",
    "PNC":"PNC Financial","USB":"U.S. Bancorp","LLY":"Eli Lilly & Co","ABBV":"AbbVie Inc",
    "JNJ":"Johnson & Johnson","MRK":"Merck & Co","AMGN":"Amgen Inc","REGN":"Regeneron Pharma",
    "VRTX":"Vertex Pharmaceuticals","ISRG":"Intuitive Surgical","UNH":"UnitedHealth Group",
    "MDT":"Medtronic plc","ABT":"Abbott Laboratories","SYK":"Stryker Corp","BSX":"Boston Scientific",
    "EW":"Edwards Lifesciences","HCA":"HCA Healthcare","HD":"Home Depot","LOW":"Lowe's Companies",
    "TGT":"Target Corp","COST":"Costco Wholesale","MCD":"McDonald's Corp","SBUX":"Starbucks Corp",
    "CMG":"Chipotle Mexican Grill","NKE":"Nike Inc","TSCO":"Tractor Supply Co","BKNG":"Booking Holdings",
    "MAR":"Marriott International","HLT":"Hilton Worldwide","ABNB":"Airbnb Inc",
    "WMT":"Walmart Inc","PG":"Procter & Gamble","KO":"Coca-Cola Co","PEP":"PepsiCo Inc",
    "PM":"Philip Morris","MDLZ":"Mondelez International","CL":"Colgate-Palmolive",
    "XOM":"Exxon Mobil","CVX":"Chevron Corp","COP":"ConocoPhillips","EOG":"EOG Resources",
    "DVN":"Devon Energy","SLB":"SLB (Schlumberger)","OXY":"Occidental Petroleum",
    "MPC":"Marathon Petroleum","VLO":"Valero Energy","PSX":"Phillips 66",
    "GE":"GE Aerospace","HON":"Honeywell International","CAT":"Caterpillar Inc","DE":"Deere & Co",
    "UNP":"Union Pacific","FDX":"FedEx Corp","UPS":"United Parcel Service","RTX":"RTX Corp",
    "LMT":"Lockheed Martin","BA":"Boeing Co","TDG":"TransDigm Group","ROK":"Rockwell Automation",
    "EMR":"Emerson Electric","ETN":"Eaton Corp","CARR":"Carrier Global",
    "NFLX":"Netflix Inc","DIS":"Walt Disney Co","TMUS":"T-Mobile US","CMCSA":"Comcast Corp",
    "FCX":"Freeport-McMoRan","APD":"Air Products & Chemicals","LIN":"Linde plc",
    "SHW":"Sherwin-Williams","NEM":"Newmont Corp","ECL":"Ecolab Inc",
    "AMT":"American Tower","PLD":"Prologis Inc","EQIX":"Equinix Inc","CCI":"Crown Castle",
    "DLR":"Digital Realty","NEE":"NextEra Energy","DUK":"Duke Energy","SO":"Southern Co",
    "VRT":"Vertiv Holdings","LMND":"Lemonade Inc","MELI":"MercadoLibre","SE":"Sea Limited",
    "DASH":"DoorDash Inc","RBLX":"Roblox Corp","ARM":"Arm Holdings",
    "SMCI":"Super Micro Computer","MRNA":"Moderna Inc",
}

_SECTOR = {
    "AAPL":"Technology","MSFT":"Technology","GOOGL":"Technology","AMZN":"Consumer Discr.",
    "META":"Technology","NVDA":"Technology","TSLA":"Consumer Discr.","AMD":"Technology",
    "ORCL":"Technology","CRM":"Technology","ADBE":"Technology","INTC":"Technology",
    "QCOM":"Technology","TXN":"Technology","AVGO":"Technology","MU":"Technology",
    "AMAT":"Technology","LRCX":"Technology","KLAC":"Technology","MRVL":"Technology",
    "SNPS":"Technology","CDNS":"Technology","DELL":"Technology","ANET":"Technology",
    "IBM":"Technology","ACN":"Technology","INTU":"Technology","PANW":"Technology",
    "FTNT":"Technology","CRWD":"Technology","ZS":"Technology","NET":"Technology",
    "OKTA":"Technology","DDOG":"Technology","SNOW":"Technology","PLTR":"Technology",
    "NOW":"Technology","HUBS":"Technology","WDAY":"Technology","VEEV":"Healthcare",
    "ZM":"Technology","UBER":"Consumer Discr.","JPM":"Financials","BAC":"Financials",
    "GS":"Financials","MS":"Financials","V":"Financials","MA":"Financials",
    "AXP":"Financials","BLK":"Financials","SCHW":"Financials","COF":"Financials",
    "SPGI":"Financials","CME":"Financials","ICE":"Financials","PNC":"Financials",
    "USB":"Financials","LLY":"Healthcare","ABBV":"Healthcare","JNJ":"Healthcare",
    "MRK":"Healthcare","AMGN":"Healthcare","REGN":"Healthcare","VRTX":"Healthcare",
    "ISRG":"Healthcare","UNH":"Healthcare","MDT":"Healthcare","ABT":"Healthcare",
    "SYK":"Healthcare","BSX":"Healthcare","EW":"Healthcare","HCA":"Healthcare",
    "HD":"Consumer Discr.","LOW":"Consumer Discr.","TGT":"Consumer Discr.",
    "COST":"Consumer Staples","MCD":"Consumer Discr.","SBUX":"Consumer Discr.",
    "CMG":"Consumer Discr.","NKE":"Consumer Discr.","TSCO":"Consumer Discr.",
    "BKNG":"Consumer Discr.","MAR":"Consumer Discr.","HLT":"Consumer Discr.",
    "ABNB":"Consumer Discr.","WMT":"Consumer Staples","PG":"Consumer Staples",
    "KO":"Consumer Staples","PEP":"Consumer Staples","PM":"Consumer Staples",
    "MDLZ":"Consumer Staples","CL":"Consumer Staples","XOM":"Energy","CVX":"Energy",
    "COP":"Energy","EOG":"Energy","DVN":"Energy","SLB":"Energy","OXY":"Energy",
    "MPC":"Energy","VLO":"Energy","PSX":"Energy","GE":"Industrials","HON":"Industrials",
    "CAT":"Industrials","DE":"Industrials","UNP":"Industrials","FDX":"Industrials",
    "UPS":"Industrials","RTX":"Industrials","LMT":"Industrials","BA":"Industrials",
    "TDG":"Industrials","ROK":"Industrials","EMR":"Industrials","ETN":"Industrials",
    "CARR":"Industrials","NFLX":"Communication","DIS":"Communication",
    "TMUS":"Communication","CMCSA":"Communication","FCX":"Materials","APD":"Materials",
    "LIN":"Materials","SHW":"Materials","NEM":"Materials","ECL":"Materials",
    "AMT":"Real Estate","PLD":"Real Estate","EQIX":"Real Estate","CCI":"Real Estate",
    "DLR":"Real Estate","NEE":"Utilities","DUK":"Utilities","SO":"Utilities",
    "VRT":"Industrials","LMND":"Financials","MELI":"Consumer Discr.","SE":"Consumer Discr.",
    "DASH":"Consumer Discr.","RBLX":"Communication","ARM":"Technology",
    "SMCI":"Technology","MRNA":"Healthcare",
}

_sma_cache = {"data": None, "ts": 0}
SMA_CACHE_TTL = 900  # 15 minutes


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


@app.route("/api/sma_scan")
def sma_scan():
    global _sma_cache
    now_ts = _time.time()
    if _sma_cache["data"] and (now_ts - _sma_cache["ts"]) < SMA_CACHE_TTL:
        return jsonify(_sma_cache["data"])

    try:
        raw = yf.download(
            SMA_UNIVERSE, period="13mo",
            auto_adjust=True, progress=False,
            group_by="ticker", threads=True,
        )

        results = []
        for ticker in SMA_UNIVERSE:
            try:
                closes = raw[ticker]["Close"].dropna() if len(SMA_UNIVERSE) > 1 else raw["Close"].dropna()
                if len(closes) < 200:
                    continue

                r50  = closes.rolling(50).mean()
                r100 = closes.rolling(100).mean()
                r150 = closes.rolling(150).mean()
                r200 = closes.rolling(200).mean()

                sma50  = float(r50.iloc[-1])
                sma100 = float(r100.iloc[-1])
                sma150 = float(r150.iloc[-1])
                sma200 = float(r200.iloc[-1])
                price  = float(closes.iloc[-1])

                # Full bullish SMA stack: P > SMA50 > SMA100 > SMA150 > SMA200
                if not (price > sma50 > sma100 > sma150 > sma200):
                    continue

                # Count consecutive trading days the full stack has been aligned
                aligned = (closes > r50) & (r50 > r100) & (r100 > r150) & (r150 > r200)
                days_aligned = 0
                for v in reversed(aligned.dropna().values.tolist()):
                    if v:
                        days_aligned += 1
                    else:
                        break

                results.append({
                    "ticker":        ticker,
                    "company":       _COMPANY.get(ticker, ticker),
                    "sector":        _SECTOR.get(ticker, "—"),
                    "price":         round(price, 2),
                    "sma50":         round(sma50, 2),
                    "sma100":        round(sma100, 2),
                    "sma150":        round(sma150, 2),
                    "sma200":        round(sma200, 2),
                    "pct_above_200": round((price - sma200) / sma200 * 100, 2),
                    "days_aligned":  int(days_aligned),
                })
            except Exception:
                continue

        # Sort: freshest alignment first — smallest days_aligned = most recent 200 cross
        results.sort(key=lambda x: x["days_aligned"])
        top10 = results[:10]

        et = ZoneInfo("America/New_York")
        ts = datetime.now(et).strftime("%b %d, %Y  %I:%M:%S %p ET")

        out = {
            "results":   top10,
            "timestamp": ts,
            "scanned":   len(SMA_UNIVERSE),
            "qualified": len(results),
        }
        _sma_cache["data"] = out
        _sma_cache["ts"]   = now_ts
        return jsonify(out)

    except Exception as e:
        return jsonify({
            "error":     str(e),
            "results":   [],
            "timestamp": "",
            "scanned":   0,
            "qualified": 0,
        }), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
