#!/usr/bin/env python3
"""
news_scalper.py — Daily News Scalper for Bwoodshares Trading

Pulls financial news from RSS feeds + Finnhub API, scores headlines by signal type,
analyzes watchlist zone proximity from live quotes, and writes scalper_brief.md
for the Claude Trading session to consume via Read tool.

Usage (run LOCALLY — RSS + Finnhub are blocked from cloud containers):
  python3 news_scalper.py --key YOUR_FINNHUB_KEY
  FINNHUB_KEY=xxx python3 news_scalper.py
  python3 news_scalper.py --rss-only   # headlines only, skip Finnhub calls

Output:
  scalper_brief.md  — structured markdown brief consumed by Claude Trading session
  → Claude Trading: "Read scalper_brief.md and identify the top signals."

Signal types: ZONE ALERTS | GAP WATCH | CATALYST | UPGRADE | DOWNGRADE | RISK | MACRO
"""

import argparse
import json
import os
import sys
import time as _time
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

# ── Config ────────────────────────────────────────────────────────────────────
ET_TZ      = ZoneInfo('America/New_York')
OUT_FILE   = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scalper_brief.md')
LOOKBACK_H = 24   # hours of news to pull
RATE_DELAY = 0.6  # seconds between Finnhub calls (60/min limit)

# ── Watchlist — mirrors app.py zone data ─────────────────────────────────────
WATCHLIST = [
    {'t':'MSFT','co':'Microsoft',         'lo':393,  'hi':412,  'stop':372,  'tgt':625,  'rr':7.3},
    {'t':'NVDA','co':'NVIDIA',             'lo':175,  'hi':192,  'stop':155,  'tgt':300,  'rr':4.1},
    {'t':'ORCL','co':'Oracle',             'lo':165,  'hi':182,  'stop':148,  'tgt':275,  'rr':4.0},
    {'t':'AMD', 'co':'AMD',                'lo':370,  'hi':390,  'stop':348,  'tgt':550,  'rr':5.3},
    {'t':'LMND','co':'Lemonade',           'lo':45,   'hi':56,   'stop':38,   'tgt':88,   'rr':3.0},
    {'t':'MRVL','co':'Marvell',            'lo':220,  'hi':242,  'stop':198,  'tgt':350,  'rr':3.7},
    {'t':'DELL','co':'Dell',               'lo':335,  'hi':355,  'stop':310,  'tgt':497,  'rr':4.3},
    {'t':'PANW','co':'Palo Alto Networks', 'lo':232,  'hi':252,  'stop':215,  'tgt':360,  'rr':4.4},
    {'t':'PLTR','co':'Palantir',           'lo':108,  'hi':122,  'stop':95,   'tgt':183,  'rr':3.4},
    {'t':'VRT', 'co':'Vertiv',             'lo':290,  'hi':312,  'stop':268,  'tgt':420,  'rr':3.6},
    {'t':'ANET','co':'Arista Networks',    'lo':128,  'hi':148,  'stop':112,  'tgt':220,  'rr':3.2},
    {'t':'AVGO','co':'Broadcom',           'lo':350,  'hi':375,  'stop':328,  'tgt':550,  'rr':5.4},
    {'t':'NOW', 'co':'ServiceNow',         'lo':103,  'hi':118,  'stop':88,   'tgt':175,  'rr':3.0},
]
TICKERS = [w['t'] for w in WATCHLIST]

# ── RSS feeds (primary source) ────────────────────────────────────────────────
RSS_FEEDS = [
    {'name':'CNBC Markets',     'url':'https://www.cnbc.com/id/100003114/device/rss/rss.html'},
    {'name':'CNBC Technology',  'url':'https://www.cnbc.com/id/19854910/device/rss/rss.html'},
    {'name':'MarketWatch',      'url':'https://feeds.marketwatch.com/marketwatch/topstories/'},
    {'name':'Reuters Business', 'url':'https://feeds.reuters.com/reuters/businessNews'},
    {'name':'Reuters Tech',     'url':'https://feeds.reuters.com/reuters/technologyNews'},
    {'name':'Benzinga',         'url':'https://www.benzinga.com/feed'},
    {'name':'Seeking Alpha',    'url':'https://seekingalpha.com/feed.xml'},
    {'name':'Investopedia',     'url':'https://www.investopedia.com/feedbuilder/feed/getfeed/?feedName=rss_headlines'},
]

# ── Signal keyword classifier ─────────────────────────────────────────────────
SIGNAL_RULES = {
    'UPGRADE':   ['upgrade', 'raises price target', 'raises pt', 'outperform', 'overweight',
                  'initiates buy', 'starts at buy', 'raises to buy', 'positive catalyst watch'],
    'DOWNGRADE': ['downgrade', 'cuts price target', 'cuts pt', 'underperform', 'underweight',
                  'neutral from buy', 'reduces to', 'lowers to hold', 'cautious on'],
    'CATALYST':  ['beats estimates', 'tops estimates', 'record revenue', 'record earnings',
                  'raises guidance', 'raises full-year', 'ai contract', 'data center deal',
                  'announces deal', 'signs agreement', 'partnership with', 'acquires',
                  'merger', 'spinoff', 's&p 500', 'index inclusion', 'fda approval',
                  'product launch', 'launches new'],
    'RISK':      ['misses estimates', 'falls short', 'cuts guidance', 'lowers guidance',
                  'warning', 'recall', 'investigation', 'doj', 'sec charges', 'sec probe',
                  'antitrust', 'fine', 'tariff', 'trade war', 'export restriction',
                  'default', 'bankruptcy', 'layoffs', 'restructuring', 'write-down',
                  'data breach', 'hack', 'cyberattack'],
    'MACRO':     ['federal reserve', 'fomc', 'powell', 'warsh', 'rate cut', 'rate hike',
                  'interest rate', 'cpi report', 'pce', 'inflation', 'gdp', 'jobs report',
                  'nonfarm payroll', 'nfp', 'treasury yield', '10-year yield', '2-year yield',
                  'wti crude', 'oil price', 'iran', 'china tariff', 'opec', 'dollar index',
                  'vix', 'recession', 'soft landing', 'yield curve', 'debt ceiling'],
}

def classify_headline(text):
    """Return (signal_type, matched_keyword) for a headline. NEUTRAL if no match."""
    lower = text.lower()
    for signal, keywords in SIGNAL_RULES.items():
        for kw in keywords:
            if kw in lower:
                return signal, kw
    # Check for ticker mentions as fallback catalyst
    for t in TICKERS:
        if t in text.upper().split():
            return 'CATALYST', f'mentions {t}'
    return 'NEUTRAL', ''

def ticker_in_headline(text):
    """Return list of watchlist tickers mentioned in headline."""
    words = text.upper().replace(',','').replace('.','').replace('(','').replace(')','').split()
    found = [t for t in TICKERS if t in words]
    # Also check company names
    lower = text.lower()
    for w in WATCHLIST:
        if w['co'].lower() in lower and w['t'] not in found:
            found.append(w['t'])
    return found

# ── Fetch helpers ─────────────────────────────────────────────────────────────
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (compatible; BwoodsharesScalper/1.0)',
    'Accept': 'application/rss+xml, application/xml, text/xml, */*',
}

def fetch_url(url, timeout=8):
    """Fetch URL, return (bytes, None) or (None, error_string)."""
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read(), None
    except Exception as e:
        return None, str(e)[:80]

def fetch_finnhub(path, api_key, params=None, timeout=8):
    """Call Finnhub API, return (dict, None) or (None, error_string)."""
    base = 'https://finnhub.io/api/v1'
    qs   = f'&{"&".join(f"{k}={v}" for k,v in params.items())}' if params else ''
    url  = f'{base}{path}?token={api_key}{qs}'
    data, err = fetch_url(url, timeout)
    if err:
        return None, err
    try:
        return json.loads(data), None
    except Exception as e:
        return None, str(e)[:80]

# ── RSS parsing ───────────────────────────────────────────────────────────────
def parse_rss(raw_bytes):
    """Parse RSS/Atom XML, return list of {title, link, published, source}."""
    items = []
    try:
        root = ET.fromstring(raw_bytes)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        # RSS 2.0
        for item in root.iter('item'):
            title = (item.findtext('title') or '').strip()
            link  = (item.findtext('link')  or '').strip()
            pub   = (item.findtext('pubDate') or item.findtext('dc:date', namespaces={'dc':'http://purl.org/dc/elements/1.1/'}) or '').strip()
            if title:
                items.append({'title': title, 'link': link, 'published': pub})
        # Atom
        if not items:
            for entry in root.findall('atom:entry', ns):
                title = (entry.findtext('atom:title', namespaces=ns) or '').strip()
                link_el = entry.find('atom:link', ns)
                link  = link_el.get('href', '') if link_el is not None else ''
                pub   = (entry.findtext('atom:updated', namespaces=ns) or '').strip()
                if title:
                    items.append({'title': title, 'link': link, 'published': pub})
    except Exception:
        pass
    return items

def pull_rss_headlines():
    """Fetch all RSS feeds, return merged list of headlines with source."""
    all_items = []
    for feed in RSS_FEEDS:
        data, err = fetch_url(feed['url'])
        if err or not data:
            print(f'  RSS [{feed["name"]}]: blocked/error — {err or "no data"}')
            continue
        items = parse_rss(data)
        for it in items:
            it['source'] = feed['name']
        print(f'  RSS [{feed["name"]}]: {len(items)} headlines')
        all_items.extend(items)
    return all_items

# ── Finnhub data ──────────────────────────────────────────────────────────────
def pull_finnhub_news(api_key):
    """Pull company news for each watchlist ticker + general market news."""
    headlines = []
    today_str = datetime.now(ET_TZ).strftime('%Y-%m-%d')
    yest_str  = (datetime.now(ET_TZ) - timedelta(days=2)).strftime('%Y-%m-%d')

    # General market news
    data, err = fetch_finnhub('/news', api_key, {'category': 'general'})
    if data and isinstance(data, list):
        for item in data[:30]:
            headlines.append({
                'title':     item.get('headline', ''),
                'source':    f'Finnhub/{item.get("source", "Market")}',
                'link':      item.get('url', ''),
                'published': str(item.get('datetime', '')),
                'tickers':   [],
            })
        print(f'  Finnhub general news: {len(data[:30])} items')
    else:
        print(f'  Finnhub general news: error — {err}')
    _time.sleep(RATE_DELAY)

    # Company news per watchlist ticker
    for w in WATCHLIST:
        data, err = fetch_finnhub('/company-news', api_key,
                                   {'symbol': w['t'], 'from': yest_str, 'to': today_str})
        if data and isinstance(data, list):
            for item in data[:5]:
                headlines.append({
                    'title':     item.get('headline', ''),
                    'source':    f'Finnhub/{item.get("source", w["t"])}',
                    'link':      item.get('url', ''),
                    'published': str(item.get('datetime', '')),
                    'tickers':   [w['t']],
                })
            print(f'  Finnhub [{w["t"]}]: {len(data[:5])} items')
        _time.sleep(RATE_DELAY)

    return headlines

def pull_finnhub_quotes(api_key):
    """Pull current quotes for all watchlist tickers."""
    quotes = {}
    for w in WATCHLIST:
        data, err = fetch_finnhub('/quote', api_key, {'symbol': w['t']})
        if data and data.get('c'):
            quotes[w['t']] = {
                'price':    data['c'],
                'prev':     data['pc'],
                'pct_chg':  round((data['c'] - data['pc']) / data['pc'] * 100, 2) if data['pc'] else 0,
                'high':     data['h'],
                'low':      data['l'],
                'open':     data['o'],
            }
        _time.sleep(RATE_DELAY)
    return quotes

def pull_earnings_calendar(api_key):
    """Pull earnings dates for our tickers in the next 14 days."""
    today = datetime.now(ET_TZ)
    to    = (today + timedelta(days=14)).strftime('%Y-%m-%d')
    fr    = today.strftime('%Y-%m-%d')
    data, err = fetch_finnhub('/calendar/earnings', api_key, {'from': fr, 'to': to})
    if not data or 'earningsCalendar' not in data:
        return []
    watchlist_earnings = []
    for e in data['earningsCalendar']:
        sym = e.get('symbol', '')
        if sym in TICKERS:
            watchlist_earnings.append({
                'ticker': sym,
                'date':   e.get('date', ''),
                'eps_est': e.get('epsEstimate'),
                'rev_est': e.get('revenueEstimate'),
                'hour':   e.get('hour', ''),
            })
    return sorted(watchlist_earnings, key=lambda x: x['date'])

# ── Zone alert engine ─────────────────────────────────────────────────────────
def analyze_zones(quotes):
    """
    Compare current prices to watchlist zones.
    Returns list of zone alert dicts sorted by urgency.
    """
    alerts = []
    for w in WATCHLIST:
        t = w['t']
        if t not in quotes:
            alerts.append({**w, 'price': None, 'pct_chg': None,
                           'status': 'NO QUOTE', 'level': 'INFO', 'action': '—'})
            continue

        q   = quotes[t]
        px  = q['price']
        pct = q['pct_chg']

        dist_to_stop   = round((px - w['stop']) / w['stop'] * 100, 1)
        dist_to_lo     = round((px - w['lo'])   / w['lo']   * 100, 1)
        dist_to_hi     = round((px - w['hi'])   / w['hi']   * 100, 1)
        dist_to_tgt    = round((w['tgt'] - px)  / px        * 100, 1)

        if px <= w['stop']:
            status, level, action = 'STOP HIT', 'CRITICAL', f'EXIT — stop ${w["stop"]} breached'
        elif dist_to_stop <= 2.0:
            status, level, action = 'NEAR STOP', 'RED', f'WATCH — ${px:.2f} / stop ${w["stop"]} = {dist_to_stop:.1f}% buffer'
        elif w['lo'] <= px <= w['hi']:
            status, level, action = 'IN ZONE', 'GREEN', f'ENTRY TRIGGER — zone ${w["lo"]}–${w["hi"]}. Stop ${w["stop"]}. R/R {w["rr"]}:1'
        elif dist_to_hi >= 0 and dist_to_hi <= 3.0:
            status, level, action = 'APPROACHING ZONE', 'YELLOW', f'WATCH — {dist_to_hi:.1f}% above zone top ${w["hi"]}'
        elif dist_to_lo <= 0 and abs(dist_to_lo) <= 3.0:
            status, level, action = 'JUST BELOW ZONE', 'YELLOW', f'WATCH — {abs(dist_to_lo):.1f}% below zone floor ${w["lo"]}'
        elif dist_to_tgt <= 5.0:
            status, level, action = 'NEAR TARGET', 'BLUE', f'TAKE PROFIT WATCH — {dist_to_tgt:.1f}% to target ${w["tgt"]}'
        elif px < w['lo']:
            status, level, action = 'BELOW ZONE', 'GRAY', f'No action — below zone ${w["lo"]}'
        else:
            status, level, action = 'ABOVE ZONE', 'GRAY', f'No action — above zone ${w["hi"]}'

        alerts.append({
            **w, 'price': px, 'pct_chg': pct,
            'status': status, 'level': level, 'action': action,
        })

    # Sort: CRITICAL > RED > GREEN > YELLOW > BLUE > GRAY > INFO
    order = ['CRITICAL','RED','GREEN','YELLOW','BLUE','GRAY','INFO']
    alerts.sort(key=lambda a: order.index(a['level']) if a['level'] in order else 99)
    return alerts

# ── Gap scanner ───────────────────────────────────────────────────────────────
def find_gaps(quotes, threshold=1.5):
    """Return watchlist tickers with pre-market/day gap > threshold%."""
    gaps = []
    for w in WATCHLIST:
        t = w['t']
        if t not in quotes:
            continue
        q   = quotes[t]
        pct = q['pct_chg']
        if abs(pct) >= threshold:
            direction = 'GAP UP' if pct > 0 else 'GAP DOWN'
            gaps.append({
                'ticker':    t,
                'company':   w['co'],
                'price':     q['price'],
                'pct_chg':   pct,
                'direction': direction,
                'zone_lo':   w['lo'],
                'zone_hi':   w['hi'],
                'stop':      w['stop'],
            })
    gaps.sort(key=lambda g: abs(g['pct_chg']), reverse=True)
    return gaps

# ── Dedup + enrich headlines ──────────────────────────────────────────────────
def process_headlines(rss_items, finnhub_items):
    """Merge, dedup, classify, and tag all headlines."""
    seen   = set()
    output = []
    all_items = rss_items + finnhub_items

    for item in all_items:
        title = (item.get('title') or '').strip()
        if not title or title.lower() in seen:
            continue
        seen.add(title.lower())

        signal, kw       = classify_headline(title)
        related_tickers  = item.get('tickers') or ticker_in_headline(title)

        output.append({
            'title':    title,
            'source':   item.get('source', 'Unknown'),
            'link':     item.get('link', ''),
            'signal':   signal,
            'keyword':  kw,
            'tickers':  related_tickers,
        })

    return output

# ── Brief writer ──────────────────────────────────────────────────────────────
LEVEL_EMOJI = {'CRITICAL':'🔴🔴', 'RED':'🔴', 'GREEN':'🟢', 'YELLOW':'🟡',
               'BLUE':'🔵', 'GRAY':'⚪', 'INFO':'ℹ️'}
SIGNAL_EMOJI = {'UPGRADE':'📈', 'DOWNGRADE':'📉', 'CATALYST':'🚀',
                'RISK':'⚠️', 'MACRO':'🌐', 'GAP':'⚡', 'NEUTRAL':'📰'}

def write_brief(zone_alerts, gaps, headlines, earnings, api_available, now_et, out_path=None):
    """Write the full scalper_brief.md."""
    ts     = now_et.strftime('%A %B %-d, %Y  %I:%M %p ET')
    lines  = []
    W      = lines.append

    W(f'# Scalper Brief — {ts}')
    W(f'> Auto-generated by news_scalper.py | '
      f'{"Finnhub + RSS" if api_available else "RSS-only (no API key)"} | '
      f'Watchlist: {len(WATCHLIST)} names')
    W('')
    W('---')
    W('')

    # ── 1. Zone Alerts ──────────────────────────────────────────────────────
    W('## ZONE ALERTS')
    W('')

    critical = [a for a in zone_alerts if a['level'] in ('CRITICAL','RED','GREEN','YELLOW')]
    if not critical:
        W('_No critical zone alerts. All names above zone or data unavailable._')
    else:
        W('| Level | Ticker | Price | Day% | Zone | Stop | Status | Action |')
        W('|-------|--------|-------|------|------|------|--------|--------|')
        for a in zone_alerts:
            if a['level'] not in ('CRITICAL','RED','GREEN','YELLOW','BLUE'):
                continue
            em   = LEVEL_EMOJI.get(a['level'], '')
            px   = f'${a["price"]:.2f}' if a['price'] else 'N/A'
            pct  = f'{a["pct_chg"]:+.1f}%' if a['pct_chg'] is not None else '—'
            zone = f'${a["lo"]}–${a["hi"]}'
            W(f'| {em} {a["level"]} | **{a["t"]}** | {px} | {pct} | {zone} | ${a["stop"]} | {a["status"]} | {a["action"]} |')

    W('')
    W('**All names:**')
    W('')
    W('| Ticker | Price | Day% | Status |')
    W('|--------|-------|------|--------|')
    for a in zone_alerts:
        px   = f'${a["price"]:.2f}' if a['price'] else 'N/A'
        pct  = f'{a["pct_chg"]:+.1f}%' if a['pct_chg'] is not None else '—'
        em   = LEVEL_EMOJI.get(a['level'], '')
        W(f'| {a["t"]} | {px} | {pct} | {em} {a["status"]} |')
    W('')
    W('---')
    W('')

    # ── 2. Gap Watch ────────────────────────────────────────────────────────
    W('## ⚡ GAP WATCH (≥1.5% move from prior close)')
    W('')
    if not gaps:
        W('_No significant gaps on watchlist names today._')
    else:
        for g in gaps:
            dir_em = '📈' if g['direction'] == 'GAP UP' else '📉'
            W(f'### {dir_em} {g["direction"]} — {g["ticker"]} ({g["company"]})')
            W(f'- **Price:** ${g["price"]:.2f}  |  **Move:** {g["pct_chg"]:+.1f}%')
            W(f'- **Zone:** ${g["zone_lo"]}–${g["zone_hi"]}  |  **Stop:** ${g["stop"]}')
            if g['direction'] == 'GAP DOWN':
                W(f'- ⚠️ **Check:** Is price approaching or through zone/stop?')
            else:
                W(f'- 📊 **Check:** Does gap create momentum entry or overextension?')
            W('')
    W('---')
    W('')

    # ── 3. Earnings Calendar ────────────────────────────────────────────────
    W('## 📅 EARNINGS CALENDAR (Next 14 Days — Watchlist Only)')
    W('')
    if not earnings:
        W('_No watchlist earnings in the next 14 days, or data unavailable._')
    else:
        W('| Ticker | Date | Time | EPS Est | Rev Est |')
        W('|--------|------|------|---------|---------|')
        for e in earnings:
            eps = f'${e["eps_est"]:.2f}' if e['eps_est'] else '—'
            rev = f'${e["rev_est"]/1e9:.2f}B' if e['rev_est'] else '—'
            hr  = e['hour'].upper() if e['hour'] else '—'
            W(f'| **{e["ticker"]}** | {e["date"]} | {hr} | {eps} | {rev} |')
    W('')
    W('---')
    W('')

    # ── 4. Catalyst Signals ─────────────────────────────────────────────────
    for sig_type in ['CATALYST', 'UPGRADE', 'DOWNGRADE', 'RISK', 'MACRO']:
        filtered = [h for h in headlines if h['signal'] == sig_type]
        if not filtered:
            continue
        em = SIGNAL_EMOJI.get(sig_type, '📰')
        W(f'## {em} {sig_type} SIGNALS ({len(filtered)})')
        W('')
        watchlist_first = sorted(filtered, key=lambda h: len(h['tickers']), reverse=True)
        for h in watchlist_first[:15]:
            tickers_str = ' '.join(f'`{t}`' for t in h['tickers']) if h['tickers'] else ''
            W(f'- {tickers_str}**{h["title"]}**')
            W(f'  _Source: {h["source"]}  |  Keyword: {h["keyword"]}_')
        if len(filtered) > 15:
            W(f'  _... and {len(filtered)-15} more {sig_type} headlines_')
        W('')
        W('---')
        W('')

    # ── 5. All Headlines (raw dump) ─────────────────────────────────────────
    non_neutral = [h for h in headlines if h['signal'] != 'NEUTRAL']
    neutral     = [h for h in headlines if h['signal'] == 'NEUTRAL']
    W(f'## 📰 ALL HEADLINES ({len(headlines)} total | {len(non_neutral)} signals | {len(neutral)} neutral)')
    W('')
    for h in headlines[:60]:
        em = SIGNAL_EMOJI.get(h['signal'], '📰')
        tickers_str = ' '.join(f'[{t}]' for t in h['tickers']) if h['tickers'] else ''
        W(f'- {em} `{h["signal"]}` {tickers_str} {h["title"]}  _{h["source"]}_')
    if len(headlines) > 60:
        W(f'_... {len(headlines)-60} additional headlines omitted_')
    W('')
    W('---')
    W('')
    W(f'_Brief generated: {ts}_')
    W(f'_Source priority: RSS feeds → Finnhub company news → Finnhub market news_')
    W(f'_Signal classifier: keyword-match on {sum(len(v) for v in SIGNAL_RULES.values())} rules_')
    W(f'_Zone engine: {len(WATCHLIST)} watchlist names, stops/entries/targets from app.py_')

    content  = '\n'.join(lines)
    dest     = out_path or OUT_FILE
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(content)
    return len(lines)

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description='Bwoodshares News Scalper')
    parser.add_argument('--key', '-k', default=os.environ.get('FINNHUB_KEY',''),
                        help='Finnhub API key (or set FINNHUB_KEY env var)')
    parser.add_argument('--rss-only', action='store_true',
                        help='Skip Finnhub calls, RSS feeds only')
    parser.add_argument('--out', default=None,
                        help=f'Output file path (default: scalper_brief.md in script dir)')
    args = parser.parse_args()
    out_file = args.out or OUT_FILE

    now_et       = datetime.now(ET_TZ)
    api_key      = args.key
    api_available = bool(api_key) and not args.rss_only

    print(f'\n=== Bwoodshares Scalper Brief — {now_et.strftime("%Y-%m-%d %H:%M ET")} ===')
    print(f'API key: {"SET ✓" if api_key else "NOT SET — RSS only"}')
    print()

    # ── Step 1: RSS feeds ────────────────────────────────────────────────────
    print('[ 1/5 ] Fetching RSS feeds...')
    rss_items = pull_rss_headlines()
    print(f'        Total RSS headlines: {len(rss_items)}')
    print()

    # ── Step 2: Finnhub news (if key available) ──────────────────────────────
    finnhub_items = []
    if api_available:
        print('[ 2/5 ] Fetching Finnhub company news...')
        finnhub_items = pull_finnhub_news(api_key)
        print(f'        Total Finnhub headlines: {len(finnhub_items)}')
    else:
        print('[ 2/5 ] Skipping Finnhub news (no key).')
    print()

    # ── Step 3: Live quotes + gap scan ──────────────────────────────────────
    quotes = {}
    if api_available:
        print('[ 3/5 ] Fetching live quotes...')
        quotes = pull_finnhub_quotes(api_key)
        print(f'        Quotes received: {len(quotes)}/{len(WATCHLIST)}')
    else:
        print('[ 3/5 ] Skipping quotes (no key) — zone alerts will show N/A.')
    print()

    # ── Step 4: Earnings calendar ────────────────────────────────────────────
    earnings = []
    if api_available:
        print('[ 4/5 ] Fetching earnings calendar...')
        earnings = pull_earnings_calendar(api_key)
        _time.sleep(RATE_DELAY)
        print(f'        Watchlist earnings: {len(earnings)}')
    else:
        print('[ 4/5 ] Skipping earnings calendar (no key).')
    print()

    # ── Step 5: Process + write brief ────────────────────────────────────────
    print('[ 5/5 ] Processing signals and writing brief...')
    all_headlines = process_headlines(
        [{'title':it['title'],'source':it['source'],'link':it.get('link','')} for it in rss_items],
        finnhub_items
    )
    zone_alerts = analyze_zones(quotes)
    gaps        = find_gaps(quotes)

    # Stats
    sig_counts = {}
    for h in all_headlines:
        sig_counts[h['signal']] = sig_counts.get(h['signal'], 0) + 1
    print(f'        Headlines processed: {len(all_headlines)}')
    for sig, count in sorted(sig_counts.items(), key=lambda x:-x[1]):
        if sig != 'NEUTRAL':
            print(f'          {SIGNAL_EMOJI.get(sig,"")}{sig}: {count}')
    print(f'          NEUTRAL: {sig_counts.get("NEUTRAL",0)}')
    print(f'        Gap alerts: {len(gaps)}')
    print(f'        Zone alerts (non-gray): {sum(1 for a in zone_alerts if a["level"] not in ("GRAY","INFO"))}')
    print()

    n_lines = write_brief(zone_alerts, gaps, all_headlines, earnings, api_available, now_et, out_file)
    print(f'Brief written → {out_file}  ({n_lines} lines)')
    print()
    print('To use in Claude Trading session:')
    print(f'  Read tool → {out_file}')
    print('  Or: "Read the scalper brief and tell me the top signals."')

if __name__ == '__main__':
    main()
