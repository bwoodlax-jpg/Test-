#!/usr/bin/env python3
"""Ranked table -> Oct 16."""
import re, sys, os, shutil
FILE='templates/index.html'; shutil.copy(FILE,FILE+'.bak'); src=open(FILE).read()

def row(rank,cls,tk,co,setup,sma,smacls,vol,volsub,rr,rrcol,stop,fit,fitcls,note,potw=False):
    badge=('\n            <div style="margin-top:4px"><span style="font-size:9px;font-weight:800;background:var(--accent);'
           'color:#000;padding:2px 7px;border-radius:2px;letter-spacing:.6px">PLAY OF THE WEEK</span></div>') if potw else ''
    tr='        <tr class="potw-row">' if potw else '        <tr>'
    tb=(f'\n            <span class="tk">{tk}</span>\n            <div class="co">{co}</div>{badge}\n          ') if potw else f'<span class="tk">{tk}</span><div class="co">{co}</div>'
    return f"""{tr}
          <td><span class="rank-dot {cls}">{rank}</span></td>
          <td>{tb}</td>
          <td style="font-size:11px">{setup}</td>
          <td><span class="{smacls}">{sma}</span></td>
          <td style="font-size:11px">{vol}<div class="co">{volsub}</div></td>
          <td class="r" style="font-size:12px;color:var({rrcol})">{rr}</td>
          <td class="r" style="font-size:12px;color:var(--red)">{stop}</td>
          <td><span class="{fitcls}">{fit}</span></td>
          <td style="font-size:11px;color:var(--dim);max-width:190px">
            {note}
          </td>
        </tr>"""

rows=[
row('&#9733;1','r1','PLTR','Palantir','Zone Entry &mdash; CONDITIONAL','Above by $3.46 &#9650;','sma-a','&ge;1.5&times; ADV MANDATORY','Green close required','4.61:1','--green','$170','HALF SIZE','fit-hi',
 '$186.03 (&minus;11.0%) &mdash; <strong style="color:var(--green)">the ONLY double-gate pass of thirteen names.</strong> In zone $179&ndash;195, closed above a RISING SMA50 $182.57. Stack near-perfect. '
 '<strong style="color:var(--red)">But only $3.46 cushion (0.45&times;ATR) and QQQ is &minus;4.9% in four sessions.</strong> Volume mandatory, 0.5% size, $182.57 kills it. If the unwind continues, no entry.', potw=True),

row('2','r1','NOW','ServiceNow Inc.','Manage the Winner &mdash; Rule Trail','Above all 4 SMAs &#9650;','sma-a','n/a &mdash; position open','No new entry','5.05:1','--green','$135.40','OPEN +38%','fit-hi',
 '$141.95 &mdash; <strong style="color:var(--green)">the ONLY watchlist name UP (+1.2%) while QQQ fell 4.9%.</strong> Touched $148.57 Oct 15. +37.5% from $103.24. '
 '<strong>The standing rule ratcheted the trail $129 &rarr; $135.40 by itself</strong> off the highest close &mdash; no session required. That is the ANET dependency fixed. Locks +31.2%.'),

row('3','r2','MSFT','Microsoft','Closest To A Second Setup','Above, SMA50 rising &#9650;','sma-a','&ge;45M shares/day','Watch for zone entry','3.9:1','--green','$478','WATCH','fit-mid',
 '$528.95 (&minus;2.3%) &mdash; second-best relative performance behind NOW. SMA50 $505.53 still rising, price $23 above. '
 '<strong style="color:var(--accent)">Sits just 1% above the $502&ndash;525 zone</strong> &mdash; a small further decline puts MSFT in zone with the gate intact, making it a genuine second entry. Watch daily.'),

row('4','r2','AMD','Advanced Micro Devices','In Zone &mdash; Below The Gate','Below a RISING SMA50 &#9888;','sma-b','&ge;40M shares/day','SMA50 reclaim first','&mdash;','--muted','$505','BLOCKED','fit-mid',
 '$528.76 (&minus;11.0%) &mdash; fell INTO the $522&ndash;550 zone but is now $8 BENEATH the rising SMA50 $537.14. In zone, below the gate. '
 'Gave back nearly half the +24.5% run the gate blocked. Same fresh-breakdown structure that resolved UP for PANW in September &mdash; unresolved here. Needs the reclaim.'),

row('5','r2','NVDA','NVIDIA','&#9888; Broke SMA50 &mdash; Flag Played Out','Below by $9 &#9888;','sma-b','&ge;180M shares/day','SMA50 reclaim first','&mdash;','--muted','$208','BLOCKED','fit-lo',
 '$214.14 (&minus;5.4%) &mdash; <strong style="color:var(--red)">broke the SMA50 it was flagged for sitting $2 above on Oct 13.</strong> Now $9 beneath $223.08. In zone $214&ndash;223, below the gate. '
 '<strong>Third time this cycle relative weakness preceded a breakdown</strong> (VRT, AVGO, NVDA). That check now earns a line in every call up.'),

row('6','r3','LMND','Lemonade','In Zone 6th Time &mdash; Blocked','Below, SMA50 falling &#9888;','sma-b','&ge;3M shares/day','Base + flat SMA50','&mdash;','--muted','$33','BLOCKED','fit-lo',
 '$44.19 (&minus;2.1%) &mdash; <strong>sixth consecutive call up in a zone with the same blocked answer</strong>, and the trigger has never been relaxed to fit the stock. '
 'SMA50 $49.24 still falling. Cumulative: six blocked sessions and LMND is ~17% lower than when it entered the zone. Repeating an unglamorous no is the job.'),

row('7','r3','ANET','Arista Networks','&#10003; CLOSED +6.8% &mdash; EXIT VALIDATED','Below by $21, SMA50 turned down &#9888;','sma-b','n/a &mdash; closed','Position closed','&mdash;','--muted','$178','CLOSED','fit-mid',
 'Closed $198.67 Oct 13 for +6.8%. <strong style="color:var(--green)">Now $177.03 &mdash; holding would show &minus;4.9% and the $178 stop is BREACHED.</strong> The exit saved 11.7 points. '
 '<strong style="color:var(--accent)">It was available because the SMA50 was named as the exit level on Sep 5, before price arrived.</strong> Naming the level in advance is the transferable part.'),

row('8','r3','ORCL','Oracle','&#9888; Reclaim Watch DEAD','Below by $17, SMA50 turned down &#9888;','sma-b','n/a &mdash; no setup','No entry','&mdash;','--muted','$128','AVOID','fit-lo',
 '$128.22 (&minus;6.7%) &mdash; the Oct 13 reclaim watch is dead. SMA50 turned back DOWN to $145.12; price is $17 under and below the zone. '
 '<strong>Not anticipating the reclaim was right for the second straight instance</strong> (VRT first). New rule: a rising average with price below is a WATCH, and it fails at least as often as it resolves.'),

row('9','r3','MRVL','Marvell Technology','&#9888; Repair Reversed In Four Days','Lost SMA50 &#9888;','sma-b','&ge;12M shares/day','SMA50 reclaim first','&mdash;','--muted','$225','AVOID','fit-lo',
 '$227.74 (&minus;14.3%) &mdash; lost the SMA50 $241.04 it had just reclaimed, giving back three quarters of the +19.0% run. '
 '<strong style="color:var(--accent)">The three-step repair completed Oct 13 undid itself in four sessions</strong> &mdash; a freshly repaired trend is the most fragile kind, with no structure beneath it.'),

row('10','r3','PANW','Palo Alto Networks','&#9888; Reversed &mdash; SMA50 Now FLAT','Below by $31, SMA50 flat &#9888;','sma-b','&ge;8M shares/day','No entry','&mdash;','--muted','$352','AVOID','fit-lo',
 '$341.89 (&minus;15.3%) &mdash; gave back three quarters of the +21.2% run; SMA50 $373.27 has gone FLAT with price $31 under. '
 '<strong>PANW was the vindication case for the fresh-breakdown call in September and is now on the other side of the same analysis.</strong> Both readings were right at the time.'),

row('11','r3','VRT','Vertiv Holdings','&#9888; THIRD Zone Floor Broken','Below by $49 &#9888;','sma-b','n/a &mdash; structure broken','No entry','&mdash;','--muted','$205','AVOID','fit-lo',
 '$206.42 (&minus;13.8%) &mdash; beneath the zone redrawn four days ago, a <strong>third successive zone floor broken</strong>, and ~36% below mid-August. '
 'The Sep 5 restraint (watch, do NOT anticipate the reclaim) is now vindicated twice. Backlog +109% YoY intact throughout &mdash; the cleanest case of sound business, broken structure.'),

row('12','r3','AVGO','Broadcom Inc.','&#9888; BROKEN &mdash; Fifth Call Up','Below by $37, SMA50 falling &#9888;','sma-b','n/a &mdash; structure broken','No entry','&mdash;','--muted','$318','AVOID','fit-lo',
 '$328.81 (&minus;7.3%) &mdash; beneath the zone redrawn four days ago; a third zone broken. <strong>Fifth consecutive call up as a broken structure.</strong> '
 'Remains the control case for the flat-SMA50 rule from Aug 13. Set against DELL &mdash; same flag, resolved up twice, then reversed 21.7% &mdash; the conclusion is that a flat average stays ambiguous and the flag should persist.'),

row('13','r3','DELL','Dell Technologies','&#9888; Worst On Board &mdash; &minus;21.7%','Below by $62 &#9888;','sma-b','n/a &mdash; structure broken','No entry','&mdash;','--muted','$485','AVOID','fit-lo',
 '$451.67 &mdash; <strong style="color:var(--red)">the sharpest decline on the board</strong>, giving back the entire +10.1% gain and more. SMA50 $513.26 still technically rising but price is $62 beneath and below the zone. '
 '<strong style="color:var(--accent)">The honest coda on the flat-SMA50 flag:</strong> raised Sep 3, resolved upward twice, now reversed hard. Resolving up once does not retire the warning.'),
]
NEW="""  <!-- Swing candidates ranked table -->
  <div class="tbl-wrap">
    <table>
      <thead>
        <tr>
          <th>Swing Rank</th>
          <th>Ticker</th>
          <th>Setup Type</th>
          <th>SMA50 Position</th>
          <th>Vol Confirm Threshold</th>
          <th class="r">Target R/R</th>
          <th class="r">Stop Zone</th>
          <th>1% Fit</th>
          <th>Weekly Swing Note</th>
        </tr>
      </thead>
      <tbody>
"""+"\n".join(rows)+"""
      </tbody>
    </table>
  </div>"""
pat=r'  <!-- Swing candidates ranked table -->\n  <div class="tbl-wrap">.*?\n      </tbody>\n    </table>\n  </div>'
src,n=re.subn(pat, lambda m:NEW, src, flags=re.DOTALL)
if n!=1: print(f'ERROR {n}'); sys.exit(1)
open(FILE,'w').write(src); print(f'OK - ranked table rebuilt ({len(rows)} rows)'); os.remove(FILE+'.bak')
