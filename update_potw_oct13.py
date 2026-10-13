#!/usr/bin/env python3
"""POTW: NOW manage-the-winner active; ANET -> CLOSED card; NOW Jul 19-25 -> history."""
import re, sys, os, shutil
FILE='templates/index.html'; shutil.copy(FILE,FILE+'.bak'); src=open(FILE).read()

NEW_CARDS = """  <!-- ══ POTW: NOW MANAGE THE WINNER (Oct 13-20) ══ -->
  <div class="potw-wrap">
    <div class="potw-badge">&#9733; Play of the Week &mdash; October 13&ndash;20, 2026</div>
    <div class="potw-ticker">NOW</div>
    <div class="potw-company">ServiceNow Inc. &mdash; Manage the Winner &mdash; <span style="color:var(--green);font-size:12px;font-weight:800">+35.9% OPEN &mdash; TRAIL $124 &rarr; $129 &mdash; STACK HAS REPAIRED</span></div>

    <div style="background:rgba(224,62,62,.09);border:1px solid rgba(224,62,62,.4);border-radius:8px;padding:11px 14px;margin-bottom:14px;font-size:11px;color:var(--dim);line-height:1.65">
      <strong style="color:var(--red)">&#9888; FIRST ACTION THIS WEEK &mdash; CLOSE ANET AT +6.8%.</strong>
      The Sep 3 POTW entered ANET at $186.10 and it peaked at a $216.74 close on Oct 9 (<strong style="color:var(--green)">+16.5%</strong>). It has faded to $198.67 and is sitting <strong style="color:var(--text)">exactly on its rising SMA50 of $198.47</strong> &mdash; the line flagged on Sep 5 as the gate-break warning. Exit and book <strong style="color:var(--accent)">+6.8%</strong>: the position has been held six weeks against a stated 2&ndash;4 day horizon, has given back 59% of its peak gain, and a 2&times; ATR trail from the peak (~$203) is already violated. Full detail on the dimmed ANET card below.
    </div>

    <div style="background:rgba(0,200,122,.08);border:1px solid rgba(0,200,122,.35);border-radius:8px;padding:10px 14px;margin-bottom:14px;font-size:11px;color:var(--dim);line-height:1.65">
      <strong style="color:var(--green)">&#9733; WHY NOW IS THE PLAY:</strong>
      With ANET closed, NOW is the only open position and <strong style="color:var(--text)">there is no new zone entry available on the board</strong> &mdash; nine names pass the SMA gate and all nine trade above their zones. NOW is $140.32 at the Oct 12 close ($142.76 intraday), <strong style="color:var(--green)">+35.9%</strong> from the $103.24 zone-floor entry taken on Jul 19&ndash;25.
      <strong style="color:var(--text)">The structural milestone:</strong> the stack has effectively repaired. At entry it was fully inverted &mdash; an explicit early-recovery bet. It now reads SMA50 $132.81 &gt; SMA100 $119.21 &gt; SMA200 $115.27 &gt; SMA150 $112.45, with only a $2.82 inversion left between the 150 and 200, and price above all four. The thesis that justified a 0.5% position has matured into a confirmed uptrend.
    </div>

    <div style="background:rgba(244,176,74,.07);border:1px solid rgba(244,176,74,.3);border-radius:8px;padding:10px 14px;margin-bottom:14px;font-size:11px;color:var(--dim);line-height:1.65">
      <strong style="color:var(--accent)">&#9888; TRAIL $129 &mdash; AND A RULE CHANGE:</strong>
      ATR(14) = $5.71, so 2&times; ATR below the $140.32 settled close is <strong style="color:var(--text)">$128.90, rounded to $129</strong>. That locks in <strong style="color:var(--green)">+25.0%</strong> from entry and sits just beneath the rising SMA50 $132.81. R/R to the $175 target: $34.68 up / $11.32 down = <strong style="color:var(--green)">3.06:1</strong>.
      <br><strong style="color:var(--red)">THE RULE CHANGE MATTERS MORE THAN THE NUMBER.</strong> ANET was exited late purely because its stop sat at $178 for five weeks while no call up happened to raise it. From here the trail is defined as a <strong style="color:var(--text)">standing rule &mdash; 2&times; ATR below the highest CLOSE since entry, recomputed continuously</strong> &mdash; not a figure set at each session. Applied to ANET that rule would have banked roughly +9% instead of +6.8%. It removes the dependency on session timing entirely.
    </div>

    <div class="potw-grid">
      <div class="potw-stat"><div class="potw-stat-lbl">Entry (Jul 19&ndash;25)</div><div class="potw-stat-val">$103.24</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Oct 12 Close</div><div class="potw-stat-val" style="color:var(--green)">$140.32</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Open Gain</div><div class="potw-stat-val" style="color:var(--green)">+35.9% &#9650;</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">New Trail</div><div class="potw-stat-val" style="color:var(--accent)">$129 (2&times;ATR)</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Locked In</div><div class="potw-stat-val" style="color:var(--green)">+25.0%</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Target</div><div class="potw-stat-val" style="color:var(--green)">$175</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">R/R Remaining</div><div class="potw-stat-val" style="color:var(--green)">3.06:1 &#10003;</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Stack</div><div class="potw-stat-val" style="color:var(--green)">REPAIRED &#10003;</div></div>
    </div>

    <div style="font-size:12px;color:var(--dim);line-height:1.65;border-top:1px solid var(--border);padding-top:12px;margin-top:4px">
      <strong style="color:var(--text)">Decision tree for the week:</strong>
      <strong>Today:</strong> close ANET (+6.8%) and raise the NOW trail to $129. Those are the only two actions.
      <strong>Wed Oct 14 / Thu Oct 15:</strong> ASML (est. $12.47) then TSM (est. $4.45) &mdash; the upstream AI bellwethers. Neither is a position, so both are information. A strong TSM print with capex guidance up validates the AMD/MRVL/AVGO complex; a miss hits the narrow leadership currently holding the indices up.
      <strong>All week:</strong> $132.81 (SMA50) is the warning level on NOW, roughly $4 above the trail. No new entries exist &mdash; only ORCL and LMND sit in zones and both have price beneath their SMA50.
      <strong>Watch ORCL:</strong> it fell 13.5% through earnings into its $138&ndash;150 zone and its SMA50 $145.90 is now RISING with price $6.70 below. A reclaim aligns zone and gate for the first time since June. Do not anticipate it &mdash; VRT was $1.94 from a reclaim on Sep 5 and fell 14.7% instead.
      <strong>Breadth caution:</strong> QQQ +3.8% against IWM &minus;6.1% over five weeks. Narrow leadership argues for smaller size, not larger.
    </div>
  </div>

  <!-- ══ PRIOR POTW: ANET ZONE ENTRY (CLOSED +6.8%) ══ -->
  <div class="potw-wrap" style="opacity:0.7;border-color:var(--border)">
    <div class="potw-badge" style="background:var(--green)">CLOSED +6.8% &mdash; September 3 &ndash; October 13, 2026</div>
    <div class="potw-ticker" style="color:var(--green)">ANET</div>
    <div class="potw-company">Arista Networks Inc. &mdash; Zone Entry, Perfect Stack &mdash; <span style="color:var(--green);font-size:12px;font-weight:800">PEAKED +16.5% &mdash; CLOSED +6.8% &mdash; RIGHT CALL, LATE EXIT</span></div>

    <div style="background:rgba(0,200,122,.08);border:1px solid rgba(0,200,122,.35);border-radius:8px;padding:10px 14px;margin-bottom:14px;font-size:11px;color:var(--dim);line-height:1.65">
      <strong style="color:var(--green)">&#9650; RESULT: WINNER, EXITED LATE</strong> &mdash;
      Entered $186.10 on a perfect bullish stack inside zone $172&ndash;190 with R/R 4.90:1. ANET advanced to a <strong style="color:var(--green)">$216.74 close on Oct 9 (+16.5%)</strong>, intraday high $217.41, and never came within $8 of the $178 stop. It then faded to $210.88 (Oct 12) and $198.67 (Oct 13 intraday), landing exactly on the rising SMA50 $198.47 &mdash; the gate-break line flagged on Sep 5. Closed at <strong style="color:var(--accent)">+6.8%</strong>. The stack is still perfectly ordered, which was the one argument for holding; a weekly swing held six weeks is not the trade that was entered.
    </div>

    <div style="background:rgba(224,62,62,.07);border:1px solid rgba(224,62,62,.3);border-radius:8px;padding:10px 14px;margin-bottom:14px;font-size:11px;color:var(--dim);line-height:1.65">
      <strong style="color:var(--red)">&#9888; THE LESSON IS PROCESS, NOT ANALYSIS.</strong>
      The entry analysis was correct: a perfect stack in a zone produced +16.5% and never threatened the stop. What failed was the exit. The stop was set to $178 on Sep 5 and <strong style="color:var(--text)">never moved, because moving it required a call up that did not happen for five weeks.</strong> A standing rule &mdash; 2&times; ATR below the highest close since entry &mdash; would have ratcheted up behind the advance and exited near $203 for roughly +9%. The gap between +9% and +6.8% is small; the dependency it exposes is not. Every trail in this framework currently needs a human-initiated session to move. That is now fixed as a rule.
    </div>

    <div class="potw-grid">
      <div class="potw-stat"><div class="potw-stat-lbl">Entry</div><div class="potw-stat-val">$186.10</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Peak Close</div><div class="potw-stat-val" style="color:var(--green)">$216.74 (+16.5%)</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Exit</div><div class="potw-stat-val" style="color:var(--accent)">$198.67</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Result</div><div class="potw-stat-val" style="color:var(--green)">+6.8%</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Stop</div><div class="potw-stat-val">$178 &mdash; never hit</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Lesson</div><div class="potw-stat-val" style="color:var(--red)">Trail = rule</div></div>
    </div>
  </div>

  <!-- ══ PRIOR POTW: NOW MANAGE THE WINNER (Aug 13-21) ══ -->
  <div class="potw-wrap" style="opacity:0.7;border-color:var(--border)">
    <div class="potw-badge" style="background:var(--green)">WORKED &mdash; August 13&ndash;21, 2026</div>
    <div class="potw-ticker" style="color:var(--green)">NOW</div>
    <div class="potw-company">ServiceNow Inc. &mdash; Manage the Winner &mdash; <span style="color:var(--green);font-size:12px;font-weight:800">TRAIL $113 HELD &mdash; POSITION NOW +35.9%</span></div>

    <div style="background:rgba(0,200,122,.08);border:1px solid rgba(0,200,122,.35);border-radius:8px;padding:10px 14px;margin-bottom:14px;font-size:11px;color:var(--dim);line-height:1.65">
      <strong style="color:var(--green)">&#9650; RESULT: TRAIL NEVER TESTED</strong> &mdash;
      The call was to raise the trail to $113 and take no other action, alongside a "zero new entries" verdict. NOW has since risen from $124.94 to $140.32 and the trail has never been approached &mdash; it has been raised twice more since ($113 &rarr; $124 &rarr; $129) without ever being threatened. The accompanying decision to take no new positions during the melt-up is what kept capital free for the ANET setup the following pullback produced.
    </div>

    <div class="potw-grid">
      <div class="potw-stat"><div class="potw-stat-lbl">Aug 12 Close</div><div class="potw-stat-val">$124.94</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Oct 12 Close</div><div class="potw-stat-val" style="color:var(--green)">$140.32</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Since Call</div><div class="potw-stat-val" style="color:var(--green)">+12.3%</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Total Open</div><div class="potw-stat-val" style="color:var(--green)">+35.9%</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Verdict</div><div class="potw-stat-val" style="color:var(--green)">TRAIL HELD</div></div>
      <div class="potw-stat"><div class="potw-stat-lbl">Lesson</div><div class="potw-stat-val" style="color:var(--accent)">Do nothing well</div></div>
    </div>
  </div>"""

start = src.index('  <!-- ══ POTW: ANET ZONE ENTRY + PERFECT STACK (Sep 3-11) ══ -->')
end   = src.index('  <!-- Strategy banner: week label + thesis -->')
src = src[:start] + NEW_CARDS + "\n\n" + src[end:]

# Push NOW Jul 19-25 zone-floor card into history (newest-first)
HIST = """        <tbody>
          <tr>
            <td style="white-space:nowrap">Jul 19&ndash;25</td>
            <td><strong>NOW</strong></td>
            <td>Zone Floor Entry</td>
            <td>Only name passing both gates. Called at the $103.24 zone floor with a rising SMA50, on the argument that a pullback to the floor IMPROVES R/R (4.7:1 vs 3.4:1) provided the floor holds. Taken on a fully INVERTED stack as a deliberate early-recovery bet.</td>
            <td>$103.24 / stop $88</td>
            <td>Open &mdash; $140.32 Oct 12</td>
            <td><span style="color:var(--green);font-weight:800">WINNER +35.9%</span></td>
            <td>Zone floor = best R/R. Stack has since fully repaired. Trail raised 3&times;, never tested.</td>
          </tr>
          <tr>
            <td style="white-space:nowrap">Jul 13&ndash;17</td>
            <td><strong>NOW</strong></td>"""
src = src.replace("""        <tbody>
          <tr>
            <td style="white-space:nowrap">Jul 13&ndash;17</td>
            <td><strong>NOW</strong></td>""", HIST, 1)

# Record line
old_rec = re.search(r'<div style="font-size:10px;color:var\(--muted\);margin-top:8px">Record:.*?</div>', src, re.DOTALL).group(0)
new_rec = ('<div style="font-size:10px;color:var(--muted);margin-top:8px">Record: 3 WINS (NOW +35.9% open, ANET +6.8% closed from a +16.5% peak), 1 LOSS, 3 STAND-DOWNS, 2 STOPPED OUT, 1 ROUND-TRIP, 2 SKIPS. '
 'SMA gate five-week scorecard Sep 4&ndash;Oct 12: missed AMD +24.5%, PANW +21.2%, MRVL +19.0% (all reclaimed falling SMA50s) and avoided ORCL &minus;13.5%, VRT &minus;14.7%, LMND &minus;15.5%. '
 'Three large winners missed, three large losers avoided in the same window &mdash; the count cancels; the asymmetry is that avoided losses sat in broken structures while missed winners first had to repair a falling average. '
 '<strong style="color:var(--red)">NEW RULE:</strong> the trail is 2&times; ATR below the highest CLOSE since entry, recomputed continuously &mdash; not a number set each session. ANET exposed that dependency.</div>')
src = src.replace(old_rec, new_rec, 1)

# Banner
old_b = re.search(r'      <strong style="color:var\(--green\)">WEEK STATUS \(Sep 5\).*?AVGO was the ONLY name down\.', src, re.DOTALL)
if not old_b: print('ERROR: banner'); sys.exit(1)
NEW_B = """      <strong style="color:var(--green)">WEEK STATUS (Oct 13): CLOSE ANET +6.8% (peaked +16.5%) &mdash; NOW +35.9%, TRAIL TO $129 &mdash; NO NEW ENTRIES.</strong>
      ANET is sitting exactly on its rising SMA50 $198.47 after fading from a $216.74 peak &mdash; six weeks held against a 2&ndash;4 day horizon. Book it.
      <strong style="color:var(--accent)">NINE names now pass the SMA gate and all nine are above their zones; only ORCL and LMND sit in zones and both have price beneath their SMA50. Third straight call up with zero double-gate passes &mdash; all 13 zones recalibrated again.</strong>
      Breadth is collapsing: QQQ +3.8% while IWM &minus;6.1% and DIA &minus;3.0%. Gate missed AMD +24.5%, PANW +21.2%, MRVL +19.0% and avoided ORCL &minus;13.5%, VRT &minus;14.7%, LMND &minus;15.5%. TSM Thu Oct 15 is the upstream AI read."""
src = src.replace(old_b.group(0), NEW_B, 1)

open(FILE,'w').write(src); print('OK - POTW rotated; ANET closed; history, record, banner updated'); os.remove(FILE+'.bak')
