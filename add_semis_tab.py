#!/usr/bin/env python3
path = '/home/user/Test-/templates/index.html'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

errors = []

def rep(old, new, label):
    global c
    if old in c:
        c = c.replace(old, new, 1)
        print(f'OK: {label}')
    else:
        errors.append(label)
        print(f'ERROR: {label} — not found')

# ── 1. Tab button ─────────────────────────────────────────────────────────────
rep(
    "  <button class=\"tab-btn\" :class=\"{'active': tab === 'sma'}\" @click=\"tab = 'sma'\" data-tab=\"sma\">&#9651; SMA Stack</button>",
    "  <button class=\"tab-btn\" :class=\"{'active': tab === 'sma'}\" @click=\"tab = 'sma'\" data-tab=\"sma\">&#9651; SMA Stack</button>\n"
    "  <button class=\"tab-btn\" :class=\"{'active': tab === 'semis'}\" @click=\"tab = 'semis'\" data-tab=\"semis\">&#9711; Semis &amp; AI</button>",
    'tab button'
)

# ── 2. CSS additions (after .sma-scan-btn:disabled rule) ──────────────────────
rep(
    "  .sma-scan-btn:disabled{opacity:.45;cursor:not-allowed}",
    "  .sma-scan-btn:disabled{opacity:.45;cursor:not-allowed}\n"
    "  .semi-desc{font-size:10px;color:var(--muted);max-width:320px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;cursor:help}\n"
    "  .semi-val{font-weight:700;font-size:12px;font-variant-numeric:tabular-nums;text-align:right}\n"
    "  .semi-fwd{font-size:11px;color:var(--dim);font-variant-numeric:tabular-nums;text-align:right}\n"
    "  .semi-pos{color:var(--green)}.semi-neg{color:var(--red)}.semi-na{color:var(--muted);font-size:10px}",
    'semi CSS'
)

# ── 3. bwoodApp state variables ───────────────────────────────────────────────
rep(
    "    smaMeta: { timestamp: '', scanned: 0, qualified: 0 },\n"
    "    init() { window._bwoodApp = this; },",
    "    smaMeta: { timestamp: '', scanned: 0, qualified: 0 },\n"
    "    semiRows: [],\n"
    "    semiLoading: false,\n"
    "    semiError: null,\n"
    "    semiLoaded: false,\n"
    "    semiProgress: 0,\n"
    "    semiProgressOf: 0,\n"
    "    init() {\n"
    "      window._bwoodApp = this;\n"
    "      this.semiRows = SEMI_AI_STOCKS.map(function(s) {\n"
    "        return {t:s.t, c:s.c, sec:s.s, desc:s.desc, ytd:null, pe:null, fwdPE:null, eps:null, fwdEPS:null, loaded:false, err:false};\n"
    "      });\n"
    "    },",
    'bwoodApp state + init'
)

# ── 4. loadSemiData method (insert before closing }; of bwoodApp) ─────────────
rep(
    "      this.smaLoaded = true;\n"
    "      this.smaLoading = false;\n"
    "    },\n"
    "  };\n"
    "}",
    "      this.smaLoaded = true;\n"
    "      this.smaLoading = false;\n"
    "    },\n"
    "\n"
    "    async loadSemiData() {\n"
    "      var apiKey = getKey();\n"
    "      if (!apiKey) {\n"
    "        this.semiError = 'Finnhub API key required — click the API Key button at the top and paste your free key from finnhub.io (same key the Live Watchlist uses).';\n"
    "        return;\n"
    "      }\n"
    "      this.semiLoading = true;\n"
    "      this.semiError = null;\n"
    "      this.semiProgress = 0;\n"
    "      this.semiProgressOf = SEMI_AI_STOCKS.length;\n"
    "      this.semiRows = SEMI_AI_STOCKS.map(function(s) {\n"
    "        return {t:s.t, c:s.c, sec:s.s, desc:s.desc, ytd:null, pe:null, fwdPE:null, eps:null, fwdEPS:null, loaded:false, err:false};\n"
    "      });\n"
    "      var self = this;\n"
    "      var BATCH = 3, MIN_MS = 3500, rateLimited = false;\n"
    "      for (var i = 0; i < SEMI_AI_STOCKS.length; i += BATCH) {\n"
    "        if (rateLimited) break;\n"
    "        var batch = SEMI_AI_STOCKS.slice(i, i + BATCH);\n"
    "        var t0 = Date.now();\n"
    "        var bres = await Promise.allSettled(batch.map(function(stock, bi) {\n"
    "          var idx = i + bi;\n"
    "          var url = 'https://finnhub.io/api/v1/stock/metric?symbol=' + stock.t + '&metric=all&token=' + apiKey;\n"
    "          return fetch(url, {signal: AbortSignal.timeout(10000)}).then(function(r) {\n"
    "            if (r.status === 429) { var e = new Error('RL'); e.rateLimit = true; throw e; }\n"
    "            if (!r.ok) { self.semiRows[idx].err = true; return; }\n"
    "            return r.json().then(function(d) {\n"
    "              var m = (d && d.metric) || {};\n"
    "              var pick = function(a,b){ return a != null ? a : (b != null ? b : null); };\n"
    "              self.semiRows[idx].ytd    = pick(m['ytdPriceReturnDaily'], m['yearToDatePriceReturn']);\n"
    "              self.semiRows[idx].pe     = pick(m['peTTM'], m['peNormalizedAnnual']);\n"
    "              self.semiRows[idx].fwdPE  = m['forwardPE'] != null ? m['forwardPE'] : null;\n"
    "              self.semiRows[idx].eps    = pick(m['epsTTM'], m['epsNormalizedAnnual']);\n"
    "              self.semiRows[idx].fwdEPS = pick(m['epsForward'], m['epsEstimateNextYear']);\n"
    "              self.semiRows[idx].loaded = true;\n"
    "            });\n"
    "          }).catch(function(e) {\n"
    "            if (e.rateLimit) throw e;\n"
    "            self.semiRows[idx].err = true;\n"
    "          });\n"
    "        }));\n"
    "        for (var j = 0; j < bres.length; j++) {\n"
    "          if (bres[j].status === 'rejected' && bres[j].reason && bres[j].reason.rateLimit) {\n"
    "            rateLimited = true; break;\n"
    "          }\n"
    "        }\n"
    "        this.semiProgress = Math.min(i + BATCH, SEMI_AI_STOCKS.length);\n"
    "        if (!rateLimited && i + BATCH < SEMI_AI_STOCKS.length) {\n"
    "          var wait = Math.max(0, MIN_MS - (Date.now() - t0));\n"
    "          if (wait > 0) await new Promise(function(r){ setTimeout(r, wait); });\n"
    "        }\n"
    "      }\n"
    "      if (rateLimited) this.semiError = 'Rate limit hit after ' + this.semiProgress + ' of ' + SEMI_AI_STOCKS.length + ' stocks. Wait 60s and click Load again.';\n"
    "      this.semiLoaded = true;\n"
    "      this.semiLoading = false;\n"
    "    },\n"
    "  };\n"
    "}",
    'loadSemiData method'
)

# ── 5. SEMI_AI_STOCKS constant (insert before SMA_SCAN_TICKERS) ───────────────
SEMI_CONST = (
    "const SEMI_AI_STOCKS = [\n"
    "  {t:'MPWR', c:'Monolithic Power Systems', s:'Power Semis',         desc:'Power management ICs (VRMs, buck converters) for AI servers, data centers, and automotive. Every NVDA/AMD GPU rack runs on MPWR voltage regulators. ~80% gross margins. Direct AI capex beneficiary without chip supply constraints.'},\n"
    "  {t:'ENTG', c:'Entegris',                 s:'Semi Materials',      desc:'Semiconductor materials leader: CMP slurries, filters, carriers, and contamination control. No chip fab runs without Entegris materials. Acquired CMC Materials 2022. ~90% consumables revenue — repeatable across node transitions.'},\n"
    "  {t:'ONTO', c:'Onto Innovation',           s:'Process Control',     desc:'Optical critical dimension (OCD) metrology and inspection for advanced semiconductor nodes. Ensures chipmakers measure sub-5nm patterns. Sole-source for several advanced packaging steps critical to CoWoS AI accelerator packaging.'},\n"
    "  {t:'ACLS', c:'Axcelis Technologies',      s:'Fab Equipment',       desc:'Sole-source supplier of ion implant equipment — mandatory in every chip production flow including SiC power devices. SiC automotive/EV growth + AI logic ramp = dual tailwinds. Near-monopoly in ion implant.'},\n"
    "  {t:'LSCC', c:'Lattice Semiconductor',     s:'FPGA / Edge AI',      desc:'Low-power FPGAs and programmable logic for edge AI, server management (BMC), 5G, and industrial. Not competing at the high-end — owns the low-power FPGA segment. Nexus platform targets sensing and control at the edge.'},\n"
    "  {t:'FORM', c:'FormFactor',                s:'Test Equipment',      desc:'Wafer probe cards used to test semiconductor wafers before dicing. Every DRAM and logic chip requires probing. Near-monopoly in DRAM probe cards. HBM memory for AI accelerators requires next-gen probing technology.'},\n"
    "  {t:'CEVA', c:'CEVA Inc',                  s:'IP Licensing',        desc:'Licenses semiconductor IP cores — AI inference engines, DSPs, wireless connectivity — to chip designers worldwide. Revenue = royalty per chip shipped. Customers include Apple, Samsung, MediaTek. AI inference IP growing rapidly.'},\n"
    "  {t:'AMBA', c:'Ambarella Inc',             s:'AI Vision SoC',       desc:'AI vision SoCs for automotive cameras, security cameras, and robot perception. CVflow AI architecture processes video at the edge under 2W. Growing ADAS win rates at Tier-1 automotive suppliers as camera mandates expand globally.'},\n"
    "  {t:'RMBS', c:'Rambus Inc',                s:'Memory IP',           desc:'Licenses high-speed memory interface IP for DDR5, HBM, and CXL. Every AI data center memory interface — including HBM3 stacks on NVDA/AMD AI GPUs — incorporates Rambus IP. Also develops security silicon and memory subsystems.'},\n"
    "  {t:'WOLF', c:'Wolfspeed',                 s:'SiC Power Semis',     desc:'Leading SiC substrate and power device maker for EV charging, industrial motors, and data center power delivery. SiC enables efficient high-voltage power conversion. World\'s largest SiC fab in Mohawk Valley (NY). Key EV powertrain supplier.'},\n"
    "  {t:'NVTS', c:'Navitas Semiconductor',     s:'GaN / SiC Power',     desc:'GaN and SiC power ICs for EV chargers, solar inverters, AI data center PSUs, and consumer fast-chargers. GaN enables smaller, cooler, faster power conversion vs. silicon. Hyperscaler power supply design-wins accelerating.'},\n"
    "  {t:'ON',   c:'ON Semiconductor',          s:'SiC / Automotive',    desc:'Tier-1 SiC power device maker for automotive EV drivetrains and industrial. Grew SiC revenue 4x in 2023. IntelliSense for SiC manufacturing platform. Competing with Infineon and STM for EV powertrain socket wins at OEMs.'},\n"
    "  {t:'SITM', c:'SiTime Corp',               s:'MEMS Timing',         desc:'MEMS-based timing semiconductors — oscillators, resonators, clock generators — that replace quartz in high-reliability applications. MEMS timing is immune to shock, vibration, and temperature extremes. Hyperscaler and defense adoption growing.'},\n"
    "  {t:'ALGM', c:'Allegro MicroSystems',      s:'Sensors / Power ICs', desc:'Magnetic sensor ICs and power ICs for automotive and industrial. Hall-effect current and position sensors. Every EV has dozens of Allegro sensors. Spun off from Sanken Electric (Japan) in 2020, listed on Nasdaq.'},\n"
    "  {t:'CRUS', c:'Cirrus Logic',              s:'Audio / Power ICs',   desc:'Audio signal processing chips and codecs. Primary Apple iPhone audio IC supplier — near-single-customer but extremely sticky. Expanding into haptics, PC audio, and power conversion ICs for Apple products. ~100% EPS beat rate.'},\n"
    "  {t:'COHU', c:'Cohu Inc',                  s:'Test Handlers',       desc:'Semiconductor test handlers and contactors. Growing in SiC and power device test as automotive semis require 100% device screening. Works alongside ATE vendors (Teradyne, Advantest) to handle chips during test. Acquired Xcerra for scale.'},\n"
    "  {t:'ICHR', c:'Ichor Holdings',            s:'Gas Delivery',        desc:'Precision gas delivery subsystems for semiconductor process equipment (AMAT, Lam Research, KLAC). Revenue tracks directly with semiconductor capex. Pure-play: if etch or CVD tools ship, Ichor gas boxes ship with them.'},\n"
    "  {t:'ACMR', c:'ACM Research',              s:'Cleaning Equipment',  desc:'Single-wafer wet cleaning equipment with strong presence in Chinese fabs (CXMT, YMTC, SMIC) and expanding internationally. Beneficiary of Chinese domestic chip buildout. Low-profile but growing rapidly. CXMT memory expansion driving demand.'},\n"
    "  {t:'VECO', c:'Veeco Instruments',         s:'Deposition Equipment',desc:'Atomic layer deposition (ALD), ion beam, and laser annealing equipment for advanced semiconductor and compound semiconductor fabs. ALD enables the precise thin-film layers required at sub-3nm nodes. Growing in advanced packaging and compound semis.'},\n"
    "  {t:'UCTT', c:'Ultra Clean Holdings',      s:'Equipment Components',desc:'Sub-assemblies, weldments, and fluid delivery components for semiconductor equipment OEMs (AMAT, Lam, KLAC, TEL). Pure-play components play on overall semi capex. High-beta proxy: revenue rises when equipment OEMs ramp production.'},\n"
    "  {t:'AZTA', c:'Azenta Inc',                s:'Wafer Automation',    desc:'Automated wafer handling, storage systems, and semiconductor lifecycle services. Wafer automation critical as fabs scale to 300mm. Formerly Brooks Automation. Also operates Brooks Life Sciences (genomics biorepository).'},\n"
    "  {t:'SMTC', c:'Semtech Corp',              s:'Analog / IoT',        desc:'Analog/mixed-signal semis for IoT connectivity (LoRa LPWAN — dominant in industrial IoT), data center optical transceivers, and circuit protection. LoRa is deployed in billions of IoT sensors globally. ClearEdge acquisition for AI data center interconnects.'},\n"
    "  {t:'IPGP', c:'IPG Photonics',             s:'Fiber Lasers',        desc:'High-power fiber lasers for industrial manufacturing, EV battery welding, and semiconductor process support. Laser welding of EV battery cells uses IPG systems. Russia exposure has pressured stock since 2022 — discount vs. fundamentals.'},\n"
    "  {t:'POWI', c:'Power Integrations',        s:'Power Conversion',    desc:'Power conversion ICs for EV chargers, smart home appliances, industrial motors, and consumer fast-chargers. EcoSmart and GaN technology for ultra-compact chargers. Benefits from global electrification mandates. Consistent dividend payer.'},\n"
    "  {t:'DIOD', c:'Diodes Inc',                s:'Discrete Semis',      desc:'Discrete semiconductors (MOSFETs, Schottky diodes, BJTs, TVS), analog ICs, and logic chips for automotive, computing, and consumer. Over 90% own-brand products. Consistent, under-the-radar performer in commodity-adjacent semiconductor markets.'},\n"
    "  {t:'TER',  c:'Teradyne',                  s:'ATE / Robotics',      desc:'Automatic test equipment (ATE) for AI chips, memory, and storage — every NVDA GPU and AMD accelerator is tested on Teradyne systems before shipping. Also owns Universal Robots (UR), global leader in collaborative robot arms. Dual play: AI test + factory automation.'},\n"
    "  {t:'CAMT', c:'Camtek',                    s:'Advanced Packaging',  desc:'Optical inspection and metrology for advanced semiconductor packaging — fan-out, 2.5D/3D chiplet integration, CoWoS. TSMC\'s CoWoS packaging for AI accelerators (NVDA H100/H200) requires Camtek inspection tools. Direct heterogeneous integration beneficiary.'},\n"
    "  {t:'NXPI', c:'NXP Semiconductors',        s:'Automotive / Edge',   desc:'Automotive-grade MCUs, secure element chips (NFC payments), and industrial IoT SoCs. Processing chips in 90%+ of new vehicles. Automotive semi content per EV is 3-5x an ICE vehicle. Also makes radar processors for ADAS and V2X communication chips.'},\n"
    "  {t:'STM',  c:'STMicroelectronics',        s:'Automotive / SiC',    desc:'European semiconductor maker: automotive MCUs, SiC power MOSFETs, industrial analog, and IoT chips. Large Apple content supplier historically. Deep SiC manufacturing partnership with Sanan (China). Broad diversified semi portfolio.'},\n"
    "  {t:'MKSI', c:'MKS Instruments',           s:'Process Control',     desc:'Pressure/flow/temperature sensors, RF power generators, photonics, and laser technology for semiconductor fabs and industrial processes. Every etch and CVD tool uses MKS sensors and RF power systems. Also makes fiber laser systems for AI server PCB drilling.'},\n"
    "];\n"
    "\n"
)

rep(
    "const SMA_SCAN_TICKERS = [",
    SEMI_CONST + "const SMA_SCAN_TICKERS = [",
    'SEMI_AI_STOCKS constant'
)

# ── 6. HTML tab panel (insert after end tab-sma) ─────────────────────────────
SEMI_HTML = (
    "\n"
    "<!-- ── Semis & AI Discovery Tab ──────────────────────────── -->\n"
    "<div id=\"tab-semis\" class=\"tab-panel\" x-show=\"tab === 'semis'\" x-cloak>\n"
    "\n"
    "  <div class=\"sec-label\">Semiconductor &amp; AI Infrastructure &mdash; Discovery Screen</div>\n"
    "  <p class=\"monitor-sub\">\n"
    "    30 mid/large-cap semiconductor and AI infrastructure names beyond the obvious (NVDA, AMD, AVGO, MRVL &mdash; already on the watchlist).\n"
    "    Covers power semis, fab equipment, process control, IP licensing, edge AI, and advanced packaging.\n"
    "    Click <strong style=\"color:var(--accent)\">Load Live Data</strong> to fetch YTD%, PE, and EPS from Finnhub (requires API key &mdash; free tier, same key as Live Watchlist).\n"
    "    Forward PE / Forward EPS populated if available from Finnhub free tier; otherwise shown as N/A.\n"
    "  </p>\n"
    "\n"
    "  <!-- Load button + progress -->\n"
    "  <div style=\"display:flex;align-items:center;gap:16px;margin-bottom:20px;flex-wrap:wrap\">\n"
    "    <button class=\"sma-scan-btn\" @click=\"loadSemiData()\" :disabled=\"semiLoading\">\n"
    "      <span x-show=\"!semiLoading\">&#9889; Load Live Data</span>\n"
    "      <span x-show=\"semiLoading\">Loading&hellip; (<span x-text=\"semiProgress\"></span>/<span x-text=\"semiProgressOf\"></span>)</span>\n"
    "    </button>\n"
    "    <div x-show=\"semiLoading\" style=\"flex:1;min-width:160px\">\n"
    "      <div style=\"height:4px;background:var(--surf2);border-radius:2px;overflow:hidden\">\n"
    "        <div style=\"height:100%;background:var(--accent);border-radius:2px;transition:width .4s\"\n"
    "             :style=\"'width:' + (semiProgressOf > 0 ? Math.round(semiProgress/semiProgressOf*100) : 0) + '%'\"></div>\n"
    "      </div>\n"
    "    </div>\n"
    "    <div x-show=\"semiLoaded && !semiLoading\" style=\"font-size:11px;color:var(--muted)\">\n"
    "      &#10003; <span x-text=\"semiRows.filter(function(r){return r.loaded;}).length\"></span> of 30 loaded\n"
    "    </div>\n"
    "  </div>\n"
    "\n"
    "  <!-- Error -->\n"
    "  <div x-show=\"semiError\" style=\"background:rgba(255,80,80,.08);border:1px solid rgba(255,80,80,.3);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:11px;color:var(--red)\" x-text=\"semiError\"></div>\n"
    "\n"
    "  <!-- Table -->\n"
    "  <div style=\"overflow-x:auto\">\n"
    "    <table class=\"sp500-table\" style=\"min-width:900px\">\n"
    "      <thead>\n"
    "        <tr>\n"
    "          <th style=\"width:60px\">#</th>\n"
    "          <th style=\"width:110px\">Ticker</th>\n"
    "          <th style=\"width:160px\">Company</th>\n"
    "          <th>Synopsis</th>\n"
    "          <th style=\"width:72px;text-align:right\">YTD%</th>\n"
    "          <th style=\"width:65px;text-align:right\">PE</th>\n"
    "          <th style=\"width:72px;text-align:right\">Fwd PE</th>\n"
    "          <th style=\"width:70px;text-align:right\">EPS</th>\n"
    "          <th style=\"width:78px;text-align:right\">Fwd EPS</th>\n"
    "        </tr>\n"
    "      </thead>\n"
    "      <tbody>\n"
    "        <template x-for=\"(row, idx) in semiRows\" :key=\"row.t\">\n"
    "          <tr>\n"
    "            <td class=\"sp-rank\" x-text=\"idx + 1\"></td>\n"
    "            <td>\n"
    "              <div class=\"sp-ticker\" x-text=\"row.t\"></div>\n"
    "              <div class=\"sp-sector-badge sec-tech\" x-text=\"row.sec\" style=\"display:inline-block;margin-top:3px\"></div>\n"
    "            </td>\n"
    "            <td><div class=\"sp-company\" style=\"font-weight:700;font-size:11px\" x-text=\"row.c\"></div></td>\n"
    "            <td><div class=\"semi-desc\" :title=\"row.desc\" x-text=\"row.desc\"></div></td>\n"
    "            <td style=\"text-align:right\">\n"
    "              <span class=\"semi-val\"\n"
    "                    :class=\"row.ytd != null ? (row.ytd >= 0 ? 'semi-pos' : 'semi-neg') : ''\"\n"
    "                    x-text=\"row.ytd != null ? (row.ytd >= 0 ? '+' : '') + row.ytd.toFixed(1) + '%' : (row.err ? 'ERR' : (row.loaded ? '&mdash;' : '&hellip;'))\"></span>\n"
    "            </td>\n"
    "            <td style=\"text-align:right\">\n"
    "              <span class=\"semi-val\"\n"
    "                    x-text=\"row.pe != null ? row.pe.toFixed(1) + 'x' : (row.err ? 'ERR' : (row.loaded ? '&mdash;' : '&hellip;'))\"></span>\n"
    "            </td>\n"
    "            <td style=\"text-align:right\">\n"
    "              <span class=\"semi-fwd\"\n"
    "                    x-text=\"row.fwdPE != null ? row.fwdPE.toFixed(1) + 'x' : (row.loaded ? 'N/A' : (row.err ? 'ERR' : '&hellip;'))\"></span>\n"
    "            </td>\n"
    "            <td style=\"text-align:right\">\n"
    "              <span class=\"semi-val\"\n"
    "                    x-text=\"row.eps != null ? '$' + row.eps.toFixed(2) : (row.err ? 'ERR' : (row.loaded ? '&mdash;' : '&hellip;'))\"></span>\n"
    "            </td>\n"
    "            <td style=\"text-align:right\">\n"
    "              <span class=\"semi-fwd\"\n"
    "                    x-text=\"row.fwdEPS != null ? '$' + row.fwdEPS.toFixed(2) : (row.loaded ? 'N/A' : (row.err ? 'ERR' : '&hellip;'))\"></span>\n"
    "            </td>\n"
    "          </tr>\n"
    "        </template>\n"
    "      </tbody>\n"
    "    </table>\n"
    "  </div>\n"
    "\n"
    "  <div style=\"margin-top:14px;font-size:10px;color:var(--muted);line-height:1.6\">\n"
    "    <strong style=\"color:var(--dim)\">Data source:</strong> Finnhub.io free tier &mdash; YTD% uses <code>ytdPriceReturnDaily</code>, PE/EPS use <code>peTTM</code>/<code>epsTTM</code>.\n"
    "    Forward PE and Fwd EPS use <code>forwardPE</code>/<code>epsForward</code> &mdash; shown as N/A if not in free tier response.\n"
    "    Hover any synopsis cell for the full description. Rates: 30 stocks = 30 API calls ~20s at Finnhub free tier (60 calls/min).\n"
    "  </div>\n"
    "\n"
    "</div><!-- end tab-semis -->\n"
)

rep(
    "</div><!-- end tab-sma -->",
    "</div><!-- end tab-sma -->\n" + SEMI_HTML,
    'semis HTML panel'
)

# ── Result ────────────────────────────────────────────────────────────────────
if errors:
    print(f'\nFAILED: {errors}')
    print('File NOT written.')
else:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print('\nAll 6 changes applied. File written.')
