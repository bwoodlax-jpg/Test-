#!/usr/bin/env python3
"""POTW rotation: ANET in as active; NOW cards demote; NOW Jul 13-17 -> history."""
import re, sys, os, shutil
FILE='templates/index.html'
shutil.copy(FILE, FILE+'.bak')
src=open(FILE).read()

# ── 1. New active ANET card + demoted NOW (Aug 13-21) + NOW (Jul 19-25) ──
NEW_CARDS = """  <!-- ══ POTW: ANET ZONE ENTRY + PERFECT STACK (Sep 3-11) ══ -->
  <div class="potw-wrap">
    <div class="potw-badge">&#9733; Play of the Week &mdash; September 3&ndash;11, 2026</div>
    <div class="potw-ticker">ANET</div>
    <div class="potw-company">Arista Networks Inc. &mdash; AI Networking &mdash; <span style="color:var(--green);font-size:12px;font-weight:800">ZONE ENTRY &mdash; PERFECT BULLISH STACK &mdash; R/R 4.90:1 &mdash; ONLY GATE PASS</span></div>

    <div style="background:rgba(0,200,122,.08);border:1px solid rgba(0,200,122,.35);border-radius:8px;padding:10px 14px;margin-bottom:14px;font-size:11px;color:var(--dim);line-height:1.65">
      <strong style="color:var(--green)">&#9733; WHY ANET &mdash; THE FIRST PERFECT-STACK ZONE ENTRY:</strong>
      ANET fell 11.6% from $210.50 to <strong style="color:var(--text)">$186.10</strong>, landing inside its buy zone $172&ndash;190. Seven watchlist names are now in zones; ANET is the <strong style="color:var(--green)">only one that passes the SMA gate</strong>.
      <strong style="color:var(--text)">The stack is textbook:</strong> SMA50 $181.83 &gt; SMA100 $170.62 &gt; SMA150 $158.55 &gt; SMA200 $151.32 &mdash; flawless descending order, SMA50 RISING, price above all four. Every prior POTW zone entry compromised somewhere; NOW at $103 was explicitly an inverted-stack recovery bet that happened to work. This is what the framework looks like when it gets exactly what it asks for.
      <strong style="color:var(--text)">Thesis:</strong> Arista EOS runs inside Meta, Microsoft, Google and Apple hyperscale clusters &mdash; migration is a 1&ndash;2 year project. Ultra Ethernet Consortium (Arista-founded) is the only viable alternative to NVIDIA InfiniBand for lossless AI cluster networking. FY2026 guide $11.5B (+28%), AI fabric revenue $3.5B.
    </div>

    <div style="background:rgba(244,176,74,.07);border:1px solid rgba(244,176,74,.3);border-radius:8px;padding:10px 14px;margin-bottom:14px;font-size:11px;color:var(--dim);line-height:1.65">
      <strong style="color:var(--accent)">&#9888; STOP $170 &mdash; TRIPLE CONFLUENCE:</strong>
      ATR(14) = $7.81, so 2&times; ATR below $186.10 is <strong style="color:var(--text)">$170.47</strong>. That lands on the SMA100 ($170.62) and just beneath the zone floor ($172). Three independent structural reasons converge on the same level, which is the cleanest stop the board has offered.
      Risk $16.10, reward $78.90 to the $265 target = <strong style="color:var(--green)">R/R 4.90:1</strong>.
      <strong style="color:var(--text)">Entry gate:</strong> Rule 4 still applies &mdash; the entry candle needs volume &ge;1.5&times; the 20-day average. Price being in the zone is necessary, not sufficient. If volume is thin, wait for the next candle.
    </div>

    <div style="background:rgba(0,200,122,.07);border:1px solid rgba(0,200,122,.25);border-radius:6px;padding:10px 14px;margin-bottom:14px;font-size:11px;color:var(--dim);line-height:1.65">
      <strong style="color:var(--green)">&#9650; SECONDARY ACTION &mdash; NOW: RAISE TRAIL $113 &rarr; $124:</strong>
      NOW rose 9.4% to $136.72 while SPY fell 0.9% and QQQ fell 2.0% &mdash; the strongest relative-strength signal on the board and the exact mirror of the VRT warning. The Jul 19&ndash;25 entry at $103.24 is now <strong style="color:var(--green)">+32.4%</strong>. Raise the trail to $124 (2&times; ATR of $6.09), locking in +20.1%. Remaining R/R to $175 is 3.0:1. No adds.
      <br><strong style="color:var(--accent)">Calendar:</strong> no watchlist name reports Sep 3&ndash;9, so the ANET window carries trend risk only &mdash; no earnings gap. Labor Day Mon Sep 7 makes next week four sessions.
    </div>

    <div class="potw-grid">
      <div class="potw-stat"><div class="potw-stat-lbl">ANET Close</div><div class="potw-stat-val" style="color:var(--accent)">$186.10</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Zone</div><div class="potw-stat-val" style="color:var(--green)">$172&ndash;$190</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Stop</div><div class="potw-stat-val" style="color:var(--red)">$170</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Target</div><div class="potw-stat-val" style="color:var(--green)">$265</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">R/R Ratio</div><div class="potw-stat-val" style="color:var(--green)">4.90:1 &#10003;</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">SMA50</div><div class="potw-stat-val" style="color:var(--green)">$181.83 RISING &#9650;</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Stack</div><div class="potw-stat-val" style="color:var(--green)">PERFECT &#10003;</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Earnings Risk</div><div class="potw-stat-val" style="color:var(--green)">NONE</div></div>
    </div>

    <div style="font-size:12px;color:var(--dim);line-height:1.65;border-top:1px solid var(--border);padding-top:12px;margin-top:4px">
      <strong style="color:var(--text)">Decision tree for the week:</strong>
      <strong>Thu Sep 3:</strong> ANET entry valid on a green candle with volume &ge;1.5&times; the 20-day average. If volume is thin, do not force it &mdash; the zone runs to $190 and the setup keeps.
      <strong>Mon Sep 7:</strong> Labor Day, markets closed.
      <strong>Tue Sep 8:</strong> Second entry window if Thursday did not confirm.
      <strong>All week:</strong> $181.83 (SMA50) is the line &mdash; a close beneath it invalidates the gate before the $170 stop is reached. Also raise the NOW trail to $124 immediately; that is a separate, non-optional action.
      <strong>Watch:</strong> PANW at $328 is the near-miss &mdash; if it reclaims its rising SMA50 $348, it becomes a strong second setup. ZS earnings Thu Sep 3 is the read-through.
    </div>
  </div>

  <!-- ══ PRIOR POTW: NOW MANAGE THE WINNER (Aug 13-21) ══ -->
  <div class="potw-wrap" style="opacity:0.7;border-color:var(--border)">
    <div class="potw-badge" style="background:var(--green)">WORKED &mdash; NOW +32% &mdash; August 13&ndash;21, 2026</div>
    <div class="potw-ticker" style="color:var(--green)">NOW</div>
    <div class="potw-company">ServiceNow Inc. &mdash; Manage the Winner &mdash; <span style="color:var(--green);font-size:12px;font-weight:800">TRAIL $113 HELD &mdash; RAN TO $136.72 &mdash; NOW +32.4% FROM ENTRY</span></div>

    <div style="background:rgba(0,200,122,.08);border:1px solid rgba(0,200,122,.35);border-radius:8px;padding:10px 14px;margin-bottom:14px;font-size:11px;color:var(--dim);line-height:1.65">
      <strong style="color:var(--green)">&#9650; RESULT: TRAIL NEVER TESTED, POSITION ADDED 9.4%</strong> &mdash;
      The call was to raise the trail to $113 and take no other action. NOW then rose 9.4% to $136.72 <em>while SPY fell 0.9% and QQQ fell 2.0%</em> &mdash; relative strength into a falling tape. The trail was never approached. Doing nothing was the entire play, and the "zero new entries" verdict that accompanied it kept capital free for the ANET setup that the pullback has now produced.
    </div>

    <div class="potw-grid">
      <div class="potw-stat"><div class="potw-stat-lbl">Aug 12 Close</div><div class="potw-stat-val">$124.94</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Sep 2 Close</div><div class="potw-stat-val" style="color:var(--green)">$136.72</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">3-Week Move</div><div class="potw-stat-val" style="color:var(--green)">+9.4%</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Total Open</div><div class="potw-stat-val" style="color:var(--green)">+32.4%</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Verdict</div><div class="potw-stat-val" style="color:var(--green)">TRAIL HELD</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Lesson</div><div class="potw-stat-val" style="color:var(--accent)">Do nothing well</div></div>
    </div>
  </div>

  <!-- ══ PRIOR POTW: NOW ZONE FLOOR (Jul 19-25) — WINNER ══ -->
  <div class="potw-wrap" style="opacity:0.7;border-color:var(--border)">
    <div class="potw-badge" style="background:var(--green)">WINNER +32% &mdash; July 19&ndash;25, 2026</div>
    <div class="potw-ticker" style="color:var(--green)">NOW</div>
    <div class="potw-company">ServiceNow Inc. &mdash; Zone Floor Entry &mdash; <span style="color:var(--green);font-size:12px;font-weight:800">$103.24 &rarr; $136.72 &mdash; POSITION STILL OPEN</span></div>

    <div style="background:rgba(0,200,122,.08);border:1px solid rgba(0,200,122,.35);border-radius:8px;padding:10px 14px;margin-bottom:14px;font-size:11px;color:var(--dim);line-height:1.65">
      <strong style="color:var(--green)">&#9650; RESULT: +32.4% AND RUNNING</strong> &mdash;
      Called at the $103.24 zone floor with R/R 4.7:1, on the argument that a pullback to the floor <em>improves</em> the setup provided the floor holds and the SMA50 is rising. Both held. NOW has since cleared its SMA200 and run to $136.72. Trail has been raised twice, $88 &rarr; $113 &rarr; $124, locking +20.1%. Target $175 still live. Notably this entry was taken on an INVERTED stack as a deliberate early-recovery bet &mdash; compare ANET, which arrives with a perfect stack.
    </div>

    <div class="potw-grid">
      <div class="potw-stat"><div class="potw-stat-lbl">Entry Level</div><div class="potw-stat-val">$103.24</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Sep 2 Close</div><div class="potw-stat-val" style="color:var(--green)">$136.72</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Gain</div><div class="potw-stat-val" style="color:var(--green)">+32.4%</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Trail Now</div><div class="potw-stat-val" style="color:var(--accent)">$124</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Verdict</div><div class="potw-stat-val" style="color:var(--green)">WINNER &mdash; OPEN</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Lesson</div><div class="potw-stat-val" style="color:var(--accent)">Floor = R/R up</div></div>
    </div>
  </div>"""

# Replace the three existing cards (Aug 13-21 active through Jul 13-17 prior)
start = src.index('  <!-- ══ POTW: NOW MANAGE THE WINNER (Aug 13-21) ══ -->')
end   = src.index('  <!-- Strategy banner: week label + thesis -->')
src = src[:start] + NEW_CARDS + "\n\n" + src[end:]

# ── 2. Push NOW (Jul 13-17) into the history table, newest-first ──
HIST_ROW = """        <tbody>
          <tr>
            <td style="white-space:nowrap">Jul 13&ndash;17</td>
            <td><strong>NOW</strong></td>
            <td>Zone + SMA Confirmed</td>
            <td>NOW the only name passing both gates at $108 in zone $103&ndash;118 with a rising SMA50. Tech selloff (QQQ &minus;4.2%) pulled it to the $103 floor &mdash; still in zone, R/R improved 3.4:1 to 4.7:1.</td>
            <td>Zone $103&ndash;118 / stop $88</td>
            <td>$103.24 &mdash; held at floor</td>
            <td><span style="color:var(--accent);font-weight:800">HELD IN ZONE</span></td>
            <td>Pullback to the floor improved the setup. Next week's entry there returned +32%.</td>
          </tr>
          <tr>
            <td style="white-space:nowrap">Jul 6&ndash;11</td>
            <td><strong>AVGO</strong></td>"""
src = src.replace("""        <tbody>
          <tr>
            <td style="white-space:nowrap">Jul 6&ndash;11</td>
            <td><strong>AVGO</strong></td>""", HIST_ROW, 1)

# ── 3. Record line ──
old_rec = re.search(r'<div style="font-size:10px;color:var\(--muted\);margin-top:8px">Record:.*?</div>', src, re.DOTALL).group(0)
new_rec = ('<div style="font-size:10px;color:var(--muted);margin-top:8px">Record: 2 WINS (NOW +32.4% open), 1 LOSS, 3 STAND-DOWNS, 2 STOPPED OUT, 1 ROUND-TRIP, 2 SKIPS. '
 'SMA gate has missed 3 winners (AVGO +11% then round-tripped and broke down, VRT +8% then broke down, MSFT +25% held) and blocked 4 losers (ORCL &minus;30%, MRVL &minus;19% to stop, VRT broke its floor, AVGO broke its zone twice). '
 'Two of the three "missed winners" subsequently broke down &mdash; the gate\'s cost is smaller than it looked. MSFT\'s earnings gap remains the one genuine miss.</div>')
src = src.replace(old_rec, new_rec, 1)

# ── 4. Strategy banner ──
old_b = re.search(r'      <strong style="color:var\(--green\)">WEEK STATUS \(Aug 13\).*?4 zone entries, 1 gate pass\.|      <strong style="color:var\(--green\)">WEEK STATUS \(Aug 13\).*?the ORCL pattern, setup dead\.', src, re.DOTALL)
if not old_b:
    print('ERROR: banner not found'); sys.exit(1)
new_b = """      <strong style="color:var(--green)">WEEK STATUS (Sep 3): ONE CLEAN SETUP &mdash; ANET $186 IN ZONE WITH A PERFECT BULLISH STACK.</strong>
      Three-week pullback: SPY &minus;0.9%, QQQ &minus;2.0%. Seven names fell back into zones (ANET, PANW, VRT, AMD, ORCL, MRVL, LMND) &mdash; only ANET passes the SMA gate.
      <strong style="color:var(--accent)">ANET stack is flawless: SMA50 $181.83 &gt; SMA100 $170.62 &gt; SMA150 $158.55 &gt; SMA200 $151.32, price above all four. Stop $170 on a triple confluence. R/R 4.90:1. No earnings risk in the window.</strong>
      NOW POTW is +32.4% &mdash; raise trail $113 &rarr; $124. AVGO broke its redrawn zone (2nd break); PANW is the near-miss, in zone but $20 under a RISING SMA50."""
src = src.replace(old_b.group(0), new_b, 1)

open(FILE,'w').write(src)
print('OK - POTW rotated, history + record + banner updated')
os.remove(FILE+'.bak')
