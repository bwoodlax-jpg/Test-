#!/usr/bin/env python3
"""POTW: PLTR conditional zone entry (half size) active; NOW trail ratchets; ANET validated."""
import re, sys, os, shutil
FILE='templates/index.html'; shutil.copy(FILE,FILE+'.bak'); src=open(FILE).read()

NEW_CARDS = """  <!-- ══ POTW: PLTR ZONE ENTRY — CONDITIONAL, HALF SIZE (Oct 19-23) ══ -->
  <div class="potw-wrap">
    <div class="potw-badge">&#9733; Play of the Week &mdash; October 19&ndash;23, 2026</div>
    <div class="potw-ticker">PLTR</div>
    <div class="potw-company">Palantir Technologies &mdash; Zone Entry, CONDITIONAL &mdash; <span style="color:var(--accent);font-size:12px;font-weight:800">ONLY DOUBLE-GATE PASS &mdash; R/R 4.61:1 &mdash; HALF SIZE, VOLUME REQUIRED</span></div>

    <div style="background:rgba(0,200,122,.08);border:1px solid rgba(0,200,122,.35);border-radius:8px;padding:10px 14px;margin-bottom:14px;font-size:11px;color:var(--dim);line-height:1.65">
      <strong style="color:var(--green)">&#9733; WHY PLTR &mdash; THE ONLY NAME PASSING BOTH GATES:</strong>
      PLTR fell 11.0% from $209.00 and landed inside its $179&ndash;195 zone while <strong style="color:var(--text)">closing above a RISING SMA50 of $182.57</strong>. It is the only one of thirteen names to be in a zone and clear the trend gate at the same time. Four others sit in zones &mdash; NVDA, AMD and LMND among them &mdash; and every one has price BENEATH its SMA50.
      <strong style="color:var(--text)">The stack is near-perfect:</strong> SMA50 $182.57 &gt; SMA100 $157.19 &gt; SMA200 $152.65 &gt; SMA150 $152.25, with the 150 and 200 inverted by only $0.40, and price above all four.
      <strong style="color:var(--text)">Stop $170</strong> (2&times; ATR of $7.75 = $170.53), sitting below the $179 zone floor. R/R to the $260 target: $73.97 up / $16.03 down = <strong style="color:var(--green)">4.61:1</strong>.
    </div>

    <div style="background:rgba(224,62,62,.09);border:1px solid rgba(224,62,62,.4);border-radius:8px;padding:11px 14px;margin-bottom:14px;font-size:11px;color:var(--dim);line-height:1.65">
      <strong style="color:var(--red)">&#9888; THE TAPE IS THE RISK, NOT THE SETUP &mdash; CONDITIONS ARE BINDING:</strong>
      A mechanical double-gate pass during a sector-wide unwind is exactly where this framework has been hurt before. QQQ is down <strong style="color:var(--text)">4.9% in four sessions</strong>; DELL &minus;21.7%, ANET &minus;16.1%, PANW &minus;15.3%, MRVL &minus;14.3%. PLTR itself fell 11.0% to reach this zone and sits only <strong style="color:var(--text)">$3.46 above the gate &mdash; under half an ATR of cushion.</strong>
      <br><strong style="color:var(--text)">1. Volume is mandatory, not advisory:</strong> entry candle at or above 1.5&times; the 20-day average on a GREEN close. No volume, no trade.
      <br><strong style="color:var(--text)">2. Half size:</strong> 0.5% of bankroll, not the full 1%.
      <br><strong style="color:var(--text)">3. $182.57 is the kill line:</strong> a close beneath the SMA50 ends the thesis well before the $170 stop.
      <br><strong style="color:var(--text)">4. If the unwind continues, there is no entry at all.</strong> A valid setup and a hostile tape can coexist &mdash; the tape sets the size.
    </div>

    <div style="background:rgba(0,200,122,.07);border:1px solid rgba(0,200,122,.25);border-radius:6px;padding:10px 14px;margin-bottom:14px;font-size:11px;color:var(--dim);line-height:1.65">
      <strong style="color:var(--green)">&#9650; SECOND ACTION &mdash; NOW: THE TRAIL RULE RATCHETS ITSELF TO $135.40:</strong>
      NOW rose 1.2% to $141.95 while every other name fell, touching $148.57 on Oct 15. It is <strong style="color:var(--green)">+37.5%</strong> from the $103.24 entry. The standing rule adopted on Oct 13 &mdash; 2&times; ATR below the highest CLOSE since entry &mdash; now computes <strong style="color:var(--text)">$135.40</strong> from that $148.57 high, versus the $129 set by hand four days ago. <strong>A $6 ratchet with no judgement involved</strong>, which is precisely the dependency ANET exposed. Locks +31.2%; sits $0.55 above the rising SMA50 $134.85; R/R to $175 is 5.05:1.
      <br><strong style="color:var(--accent)">ANET exit validated:</strong> closed $198.67 on Oct 13 for +6.8%. It is now $177.03 &mdash; holding would show &minus;4.9% and the $178 stop has been breached. The exit saved 11.7 points.
    </div>

    <div class="potw-grid">
      <div class="potw-stat"><div class="potw-stat-lbl">PLTR Close</div><div class="potw-stat-val" style="color:var(--accent)">$186.03</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Zone</div><div class="potw-stat-val" style="color:var(--green)">$179&ndash;$195</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Stop</div><div class="potw-stat-val" style="color:var(--red)">$170 (2&times;ATR)</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Target</div><div class="potw-stat-val" style="color:var(--green)">$260</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">R/R Ratio</div><div class="potw-stat-val" style="color:var(--green)">4.61:1 &#10003;</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">SMA50 / Kill</div><div class="potw-stat-val" style="color:var(--accent)">$182.57 RISING</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Cushion</div><div class="potw-stat-val" style="color:var(--red)">$3.46 (0.45&times;ATR)</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Size</div><div class="potw-stat-val" style="color:var(--accent)">0.5% &mdash; HALF</div></div>
    </div>

    <div style="font-size:12px;color:var(--dim);line-height:1.65;border-top:1px solid var(--border);padding-top:12px;margin-top:4px">
      <strong style="color:var(--text)">Decision tree for the week:</strong>
      <strong>Monday Oct 19:</strong> raise the NOW trail to $135.40 &mdash; that is unconditional. PLTR entry only on a green close with volume &ge;1.5&times; the 20-day average. If Monday is another red day, do nothing.
      <strong>Wed Oct 21 is the crowded day:</strong> META, TSLA, IBM, TXN, LRCX and SAP all report. TXN and LRCX are the semis reads; META is the mega-cap AI capex read. No watchlist name reports, so this is sentiment risk rather than position risk &mdash; but it argues for entering before Wednesday or waiting until after it.
      <strong>All week:</strong> $182.57 is the PLTR kill line and $134.85 is the NOW warning level. Both sit above their respective stops, so both warn first.
      <strong>Not entries:</strong> NVDA, AMD and LMND are all in zones with price beneath their SMA50s. ORCL&#39;s reclaim watch is dead &mdash; its SMA50 turned back down. AVGO is broken for a fifth straight call up.
    </div>
  </div>

  <!-- ══ PRIOR POTW: NOW MANAGE THE WINNER (Oct 13-20) ══ -->
  <div class="potw-wrap" style="opacity:0.7;border-color:var(--border)">
    <div class="potw-badge" style="background:var(--green)">WORKED &mdash; ONLY NAME UP &mdash; October 13&ndash;20, 2026</div>
    <div class="potw-ticker" style="color:var(--green)">NOW</div>
    <div class="potw-company">ServiceNow Inc. &mdash; Manage the Winner &mdash; <span style="color:var(--green);font-size:12px;font-weight:800">+1.2% IN A &minus;4.9% TAPE &mdash; POSITION +37.5% &mdash; RULE RATCHETED THE TRAIL</span></div>

    <div style="background:rgba(0,200,122,.08);border:1px solid rgba(0,200,122,.35);border-radius:8px;padding:10px 14px;margin-bottom:14px;font-size:11px;color:var(--dim);line-height:1.65">
      <strong style="color:var(--green)">&#9650; RESULT: ONLY WATCHLIST NAME UP</strong> &mdash;
      The call was to raise the trail to $129, close ANET, and adopt a standing trail rule. All three held. NOW rose 1.2% to $141.95 (touching $148.57 on Oct 15) while QQQ fell 4.9% and every other name on the board declined &mdash; the third consecutive call up showing relative strength against the tape. <strong style="color:var(--text)">The new rule then did the work itself,</strong> ratcheting the trail from $129 to $135.40 off the $148.57 high with no session required. That is the ANET dependency fixed in practice, not just in principle.
    </div>

    <div class="potw-grid">
      <div class="potw-stat"><div class="potw-stat-lbl">Oct 12 Close</div><div class="potw-stat-val">$140.32</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Oct 16 Close</div><div class="potw-stat-val" style="color:var(--green)">$141.95</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">vs QQQ</div><div class="potw-stat-val" style="color:var(--green)">+1.2% vs &minus;4.9%</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Total Open</div><div class="potw-stat-val" style="color:var(--green)">+37.5%</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Trail Now</div><div class="potw-stat-val" style="color:var(--accent)">$135.40 (rule)</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Lesson</div><div class="potw-stat-val" style="color:var(--accent)">Rule &gt; number</div></div>
    </div>
  </div>

  <!-- ══ PRIOR POTW: ANET CLOSED +6.8% — EXIT VALIDATED ══ -->
  <div class="potw-wrap" style="opacity:0.7;border-color:var(--border)">
    <div class="potw-badge" style="background:var(--green)">CLOSED +6.8% &mdash; EXIT VALIDATED &mdash; Sep 3 &ndash; Oct 13, 2026</div>
    <div class="potw-ticker" style="color:var(--green)">ANET</div>
    <div class="potw-company">Arista Networks Inc. &mdash; Zone Entry, Perfect Stack &mdash; <span style="color:var(--green);font-size:12px;font-weight:800">EXITED $198.67 &mdash; NOW $177.03 AND BELOW ITS STOP</span></div>

    <div style="background:rgba(0,200,122,.08);border:1px solid rgba(0,200,122,.35);border-radius:8px;padding:10px 14px;margin-bottom:14px;font-size:11px;color:var(--dim);line-height:1.65">
      <strong style="color:var(--green)">&#9650; THE EXIT CALL WAS RIGHT &mdash; AND THE MARGIN WAS 11.7 POINTS</strong> &mdash;
      Entered $186.10, peaked at a $216.74 close (+16.5%), and was closed at $198.67 on Oct 13 for <strong style="color:var(--green)">+6.8%</strong> because price had reached the rising SMA50 named in advance on Sep 5, the trade had given back 59% of its peak, and six weeks had passed on a 2&ndash;4 day horizon.
      <strong style="color:var(--text)">Four sessions later ANET is $177.03.</strong> Holding would now show &minus;4.9% against the entry, and price has broken THROUGH the $178 stop &mdash; so the position would have closed anyway, 11.7 points lower. The exit converted a trade that is now a loss into a booked gain.
      <br><strong style="color:var(--accent)">Why it was available:</strong> the SMA50 was named as the exit level before price arrived there, which turned a judgement call under pressure into a pre-committed decision. Naming the level in advance is the transferable part.
    </div>

    <div class="potw-grid">
      <div class="potw-stat"><div class="potw-stat-lbl">Entry</div><div class="potw-stat-val">$186.10</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Peak Close</div><div class="potw-stat-val" style="color:var(--green)">$216.74 (+16.5%)</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Exited</div><div class="potw-stat-val" style="color:var(--green)">$198.67 (+6.8%)</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Oct 16</div><div class="potw-stat-val" style="color:var(--red)">$177.03 (&minus;4.9%)</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Saved</div><div class="potw-stat-val" style="color:var(--green)">11.7 points</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Lesson</div><div class="potw-stat-val" style="color:var(--accent)">Name the exit</div></div>
    </div>
  </div>"""

start = src.index('  <!-- ══ POTW: NOW MANAGE THE WINNER (Oct 13-20) ══ -->')
end   = src.index('  <!-- Strategy banner: week label + thesis -->')
src = src[:start] + NEW_CARDS + "\n\n" + src[end:]

# Push NOW Aug 13-21 card into history
HIST = """        <tbody>
          <tr>
            <td style="white-space:nowrap">Aug 13&ndash;21</td>
            <td><strong>NOW</strong></td>
            <td>Manage the Winner</td>
            <td>Raise trail to $113 and take no other action, with a "zero new entries" verdict because all eight gate passes sat above their zones. Doing nothing was the whole play.</td>
            <td>Trail $88 &rarr; $113</td>
            <td>Trail never tested; ran to $148.57</td>
            <td><span style="color:var(--green);font-weight:800">TRAIL HELD</span></td>
            <td>Taking no position in the melt-up kept capital free for the ANET setup the next pullback produced.</td>
          </tr>
          <tr>
            <td style="white-space:nowrap">Jul 19&ndash;25</td>
            <td><strong>NOW</strong></td>"""
src = src.replace("""        <tbody>
          <tr>
            <td style="white-space:nowrap">Jul 19&ndash;25</td>
            <td><strong>NOW</strong></td>""", HIST, 1)

# Record line
old_rec = re.search(r'<div style="font-size:10px;color:var\(--muted\);margin-top:8px">Record:.*?</div>', src, re.DOTALL).group(0)
new_rec = ('<div style="font-size:10px;color:var(--muted);margin-top:8px">Record: 3 WINS (NOW +37.5% open, ANET +6.8% closed from a +16.5% peak), 1 LOSS, 3 STAND-DOWNS, 2 STOPPED OUT, 1 ROUND-TRIP, 2 SKIPS. '
 '<strong style="color:var(--green)">ANET EXIT VALIDATED Oct 17:</strong> closed $198.67 on Oct 13, now $177.03 &mdash; holding would show &minus;4.9% and the $178 stop is breached. The exit saved 11.7 points. It was available because the SMA50 was named as the exit level on Sep 5, before price reached it. '
 '<strong style="color:var(--red)">TRAIL RULE PROVED ITSELF IN FOUR DAYS:</strong> 2&times; ATR below the highest CLOSE since entry ratcheted NOW from $129 to $135.40 off the $148.57 Oct 15 high, with no session required. '
 'Gate scorecard update: the three winners it missed Sep 4&ndash;Oct 12 (AMD +24.5%, PANW +21.2%, MRVL +19.0%) gave back half to three quarters in four sessions and are all back below their SMA50s &mdash; the filter buys avoided round-trips, not maximum return.</div>')
src = src.replace(old_rec, new_rec, 1)

# Banner
old_b = re.search(r'      <strong style="color:var\(--green\)">WEEK STATUS \(Oct 13\).*?upstream AI read\.', src, re.DOTALL)
if not old_b: print('ERROR: banner'); sys.exit(1)
NEW_B = """      <strong style="color:var(--green)">WEEK STATUS (Oct 17): PLTR IS THE ONLY DOUBLE-GATE PASS &mdash; CONDITIONAL, HALF SIZE &mdash; NOW TRAIL RATCHETS TO $135.40.</strong>
      Sharp AI unwind: QQQ &minus;4.9% in four sessions. DELL &minus;21.7%, ANET &minus;16.1%, PANW &minus;15.3%, MRVL &minus;14.3%. NOW is the ONLY watchlist name up (+1.2%).
      <strong style="color:var(--accent)">ANET EXIT VALIDATED &mdash; closed $198.67 for +6.8%, now $177.03 and below its $178 stop. The exit saved 11.7 points, and it was available because the SMA50 was named as the exit level in advance.</strong>
      PLTR $186.03 is in zone $179&ndash;195 above a rising SMA50 $182.57 with R/R 4.61:1 &mdash; but only $3.46 of cushion, so volume confirmation is mandatory and size is 0.5%. NVDA broke its SMA50 exactly as flagged; relative weakness is now 3-for-3 this cycle."""
src = src.replace(old_b.group(0), NEW_B, 1)

open(FILE,'w').write(src); print('OK - POTW rotated to PLTR; history, record, banner updated'); os.remove(FILE+'.bak')
