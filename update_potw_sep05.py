#!/usr/bin/env python3
"""ANET POTW stays active (open position, gate holding). Add grade + stop raise."""
import re, sys, os, shutil
FILE='templates/index.html'; shutil.copy(FILE,FILE+'.bak'); src=open(FILE).read()

# Badge / header
src = src.replace(
 '<div class="potw-badge">&#9733; Play of the Week &mdash; September 3&ndash;11, 2026</div>',
 '<div class="potw-badge">&#9733; Play of the Week &mdash; September 3&ndash;11, 2026 &mdash; OPEN +4.1%</div>',1)
src = src.replace(
 'ZONE ENTRY &mdash; PERFECT BULLISH STACK &mdash; R/R 4.90:1 &mdash; ONLY GATE PASS</span>',
 'OPEN +4.1% &mdash; GATE HOLDING &mdash; STOP RAISED $170 &rarr; $178 &mdash; R/R 4.52:1</span>',1)

# Insert a grade panel right after the company line
anchor = 'OPEN +4.1% &mdash; GATE HOLDING &mdash; STOP RAISED $170 &rarr; $178 &mdash; R/R 4.52:1</span></div>\n'
GRADE = """
    <div style="background:rgba(0,200,122,.10);border:1px solid rgba(0,200,122,.45);border-radius:8px;padding:11px 14px;margin-bottom:14px;font-size:11px;color:var(--dim);line-height:1.65">
      <strong style="color:var(--green)">&#9679; TRADE GRADE &mdash; Sep 4 session close: WORKING, NOT YET PROVEN.</strong>
      Called at <strong style="color:var(--text)">$186.10</strong> on Sep 3; closed Sep 4 at <strong style="color:var(--green)">$193.77 = +4.12%</strong>. The gate that justified the entry is intact &mdash; SMA50 has kept rising to $182.88 with price above it.
      <strong style="color:var(--accent)">The honest calibration:</strong> ATR(14) is $7.81, which is 4.03% of price. So the entire gain equals <strong style="color:var(--text)">0.98&times; ATR &mdash; slightly less than one average day of range.</strong> Two sessions of movement inside a single ATR is not evidence of anything. Calling this a win at day two would be reading noise as signal. Judge it at 2&ndash;3&times; ATR.
      <br><strong style="color:var(--text)">Action taken:</strong> stop raised $170 &rarr; <strong style="color:var(--accent)">$178</strong> (2&times; ATR below price, sitting beneath the rising SMA50 so ordinary tests of the average do not trigger it). Risk from entry drops from $16.10 to $8.10 per share. R/R from $193.77: $71.23 up / $15.77 down = <strong style="color:var(--green)">4.52:1</strong>.
      <br><strong style="color:var(--text)">Entry window is now closed</strong> &mdash; price is above the $190 zone top. This is a management position, not an entry.
    </div>
"""
i = src.index(anchor)+len(anchor)
src = src[:i] + GRADE + src[i:]

# Stat grid refresh
for old,new in [
 ('<div class="potw-stat-lbl">ANET Close</div><div class="potw-stat-val" style="color:var(--accent)">$186.10</div>',
  '<div class="potw-stat-lbl">Entry (Sep 3)</div><div class="potw-stat-val">$186.10</div>'),
 ('<div class="potw-stat-lbl">Zone</div><div class="potw-stat-val" style="color:var(--green)">$172&ndash;$190</div>',
  '<div class="potw-stat-lbl">Sep 4 Close</div><div class="potw-stat-val" style="color:var(--green)">$193.77 &#9650;</div>'),
 ('<div class="potw-stat-lbl">Stop</div><div class="potw-stat-val" style="color:var(--red)">$170</div>',
  '<div class="potw-stat-lbl">Open Gain</div><div class="potw-stat-val" style="color:var(--green)">+4.12%</div>'),
 ('<div class="potw-stat-lbl">R/R Ratio</div><div class="potw-stat-val" style="color:var(--green)">4.90:1 &#10003;</div>',
  '<div class="potw-stat-lbl">New Stop</div><div class="potw-stat-val" style="color:var(--accent)">$178 (2&times;ATR)</div>'),
 ('<div class="potw-stat-lbl">SMA50</div><div class="potw-stat-val" style="color:var(--green)">$181.83 RISING &#9650;</div>',
  '<div class="potw-stat-lbl">SMA50</div><div class="potw-stat-val" style="color:var(--green)">$182.88 RISING &#9650;</div>'),
 ('<div class="potw-stat-lbl">Stack</div><div class="potw-stat-val" style="color:var(--green)">PERFECT &#10003;</div>',
  '<div class="potw-stat-lbl">R/R Remaining</div><div class="potw-stat-val" style="color:var(--green)">4.52:1 &#10003;</div>'),
 ('<div class="potw-stat-lbl">Earnings Risk</div><div class="potw-stat-val" style="color:var(--green)">NONE</div>',
  '<div class="potw-stat-lbl">Gain in ATR</div><div class="potw-stat-val" style="color:var(--accent)">0.98&times; &mdash; early</div>'),
]:
    if old not in src: print(f'ERROR stat: {old[:60]}'); sys.exit(1)
    src = src.replace(old,new,1)

# Replace the decision tree with the current one
old_dt = re.search(r'      <strong style="color:var\(--text\)">Decision tree for the week:</strong>.*?\n    </div>\n  </div>', src, re.DOTALL)
if not old_dt: print('ERROR: decision tree'); sys.exit(1)
NEW_DT = """      <strong style="color:var(--text)">Decision tree from here:</strong>
      <strong>Done:</strong> stop raised to $178. That is the only required action on this position.
      <strong>All week:</strong> $182.88 (SMA50) is the line that matters &mdash; a close beneath it breaks the gate that justified the entry, and it sits $5 above the stop, so it warns first. Target $265 unchanged.
      <strong>Do not:</strong> add here. Price is above the $190 zone top and the entry window is closed. Do not lower the stop.
      <strong>Elsewhere:</strong> no new zone entries exist &mdash; only PANW and LMND remain in zones and both fail the SMA gate. ORCL reports Thu Sep 10; it is not a position and should not become one through the print.
      <strong>Watch:</strong> VRT is $1.94 under its SMA50 after a 9.3% bounce, and LMND's SMA50 fell just $0.02 (effectively flat) with price basing above $52. Both are one condition from live. Neither should be anticipated.
    </div>
  </div>"""
src = src.replace(old_dt.group(0), NEW_DT, 1)

# Banner
old_b = re.search(r'      <strong style="color:var\(--green\)">WEEK STATUS \(Sep 3\).*?RISING SMA50\.', src, re.DOTALL)
if not old_b: print('ERROR: banner'); sys.exit(1)
NEW_B = """      <strong style="color:var(--green)">WEEK STATUS (Sep 5): ANET POTW OPEN +4.1% &mdash; GATE HOLDING &mdash; STOP RAISED TO $178.</strong>
      Fed's Waller hinted at a September hold; the resulting risk-on bounce lifted the most beaten-down names hardest (VRT +9.3%, ORCL +8.9%, MRVL +8.2%) without repairing a single broken trend.
      <strong style="color:var(--accent)">ZERO new zone entries &mdash; the bounce cleared the board again. Only PANW and LMND remain in zones and both fail the SMA gate.</strong>
      Calibration on ANET: +4.12% equals 0.98&times; ATR, under one average day of range &mdash; working, not yet proven. ORCL's SMA50 finally flattened but its zone vanished in the same two sessions; earnings Thu Sep 10. AVGO was the ONLY name down."""
src = src.replace(old_b.group(0), NEW_B, 1)

open(FILE,'w').write(src); print('OK - ANET POTW card graded, stop raised, banner updated'); os.remove(FILE+'.bak')
