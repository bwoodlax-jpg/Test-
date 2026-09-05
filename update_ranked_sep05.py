#!/usr/bin/env python3
"""Ranked table -> Sep 4."""
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
row('&#9733;1','r1','ANET','Arista Networks','Zone Entry &mdash; OPEN +4.1%','Above, SMA50 rising &#9650;','sma-a','n/a &mdash; position open','Entry window closed','4.52:1','--green','$178','OPEN','fit-hi',
 'Entered $186.10 Sep 3, now <strong style="color:var(--green)">$193.77 (+4.12%)</strong>. Gate intact: SMA50 risen to $182.88, price above. '
 '<strong style="color:var(--accent)">Calibration: ATR $7.81 = 4.03% of price, so the gain is 0.98&times; ATR</strong> &mdash; under one average day. Working, not proven; judge at 2&ndash;3&times; ATR. '
 '<strong>Stop raised $170 &rarr; $178</strong>, cutting entry risk $16.10 &rarr; $8.10. Above the $190 zone top &mdash; no adds.', potw=True),

row('2','r1','NOW','ServiceNow Inc.','Manage the Winner &mdash; Trail Untouched','Above all 4 SMAs &#9650;','sma-a','n/a &mdash; position open','No new entry','3.0:1','--green','$124 trail','OPEN +37%','fit-hi',
 '$141.27 &mdash; <strong style="color:var(--green)">+36.8%</strong> from the $103.24 entry (touched $145.59 Sep 3). SMA50 $117.11 rising steeply. '
 'Trail $124 untouched, $17 beneath price. Managed across three call ups, raised twice, never tested &mdash; the work is in not interfering.'),

row('3','r2','VRT','Vertiv Holdings','Broken &mdash; Nearest To Reclaim','Below by $1.94 &#9888;','sma-b','&ge;6M shares/day','SMA50 reclaim + base','--','--muted','$240','WATCH','fit-mid',
 '$280.52 &mdash; <strong style="color:var(--green)">biggest bounce on the board (+9.3%)</strong>, now just <strong>$1.94 under SMA50 $282.46</strong>. Closest to a reclaim since the breakdown; one session flips it. '
 '<strong style="color:var(--accent)">But this was a rate-hold bounce</strong> &mdash; it re-prices duration, it does not repair a downtrend. Still needs base AND reclaim.'),

row('4','r2','LMND','Lemonade','In Zone 4th Time &mdash; SMA50 Flattening','Below, SMA50 nearly flat &#9888;','sma-b','&ge;3M shares/day','Base + flat SMA50','3.2:1','--accent','$38','CLOSEST YET','fit-mid',
 '$53.40 &mdash; in zone $45&ndash;56 for the <strong>fourth consecutive call up</strong>. SMA50 fell just <strong>$0.02</strong> on the day ($58.82 &rarr; $58.81) &mdash; effectively flat after months of decline. '
 'Price based above $52 the whole time. The stated trigger (base + flat SMA50) is finally being met rather than relaxed. Still $5.41 under the average &mdash; gate holds.'),

row('5','r2','PANW','Palo Alto Networks','Near-Miss &mdash; Barely Bounced','Below a RISING SMA50 &#9888;','sma-b','&ge;8M shares/day','SMA50 reclaim first','--','--muted','$300','WATCH','fit-mid',
 '$333.22 &mdash; up only 1.4% while beaten-down peers gained 8&ndash;9%. <strong style="color:var(--accent)">Underparticipating in a rate-relief bounce is itself a mild negative.</strong> '
 'In zone $322&ndash;350 but $16 under a RISING SMA50 $349.28. Unchanged from Sep 3: reclaim $349 and it is a strong setup; roll over and it joins the broken column.'),

row('6','r2','NVDA','NVIDIA','Above Zone &mdash; Held Both Directions','Above, both rising &#9650;','sma-a','&ge;180M shares/day','Waiting for pullback','5.8:1','--green','$192','WAIT','fit-mid',
 '$230.35 (+2.6%). Notable for what it did NOT do &mdash; held through the pullback that took six names into zones, then joined the bounce. '
 '<strong>The only name to manage both without drama.</strong> SMA50 $210.53 rising. Zone $203&ndash;213 now 8% below.'),

row('7','r3','DELL','Dell Technologies','Flat-SMA Flag Resolved UP','Above, SMA50 turned up &#9650;','sma-a','&ge;12M shares/day','Waiting for pullback','4.1:1','--green','$392','WAIT','fit-mid',
 '$523.93 (+6.4%). The Sep 3 flat-SMA50 caution <strong style="color:var(--green)">resolved to the upside</strong> &mdash; the average turned decisively back up to $439.30. '
 'Recording plainly: the flag was warranted on the evidence, the outcome went the other way. A flat SMA50 is genuinely ambiguous &mdash; watch, do not act. Contrast AVGO, flagged the same way, still falling.'),

row('8','r3','PLTR','Palantir','Above Zone &mdash; Gap Closing','Above by 16% (was 28%) &#9650;','sma-a','&ge;60M shares/day','Waiting for pullback','3.75:1','--green','$125','WAIT','fit-mid',
 '$174.31 (+2.9%). Extension resolving <strong>through time, not a drawdown</strong> &mdash; SMA50 rose to $150.05, narrowing the gap from 28% in August to 16%. '
 'The SMA50 is now inside the $138&ndash;152 zone, so a routine pullback would meet both at once. Converging, not deteriorating.'),

row('9','r3','MSFT','Microsoft','Above Zone &mdash; Zone Now Closed','Above, SMA50 rising fast &#9650;','sma-a','&ge;45M shares/day','Zone needs redraw','5.2:1','--green','$385','WAIT','fit-mid',
 '$499.68 (+0.6%). SMA50 $444.38 has now climbed <strong>THROUGH the old zone top $438</strong> &mdash; the $410&ndash;438 zone no longer exists as a reachable structure and needs redrawing. '
 'The Jul 30 Azure gap remains the largest winner the gate has cost.'),

row('10','r3','ORCL','Oracle','Repaired Late &mdash; Zone Gone, Earnings','Above a FLAT SMA50 &#9654;','sma-a','n/a &mdash; earnings Sep 10','Stand aside','--','--muted','$128','AVOID','fit-lo',
 '$158.77 (+8.9%). <strong>SMA50 finally FLATTENED</strong> ($139.71 &rarr; $139.74) &mdash; step two complete, exactly as the Sep 3 note asked. '
 '<strong style="color:var(--accent)">But price cleared the $138&ndash;150 zone in the same two sessions.</strong> Structure qualified after the entry vanished. '
 'Earnings Thu Sep 10 (est. $1.67; bar is 58&ndash;64% cloud growth). Any entry now is an earnings bet.'),

row('11','r3','MRVL','Marvell Technology','Reclaimed SMA50 &mdash; Step 1 of 3','Above a FALLING SMA50 &#9654;','sma-b','&ge;12M shares/day','SMA50 must flatten','--','--muted','$182','BLOCKED','fit-lo',
 '$223.50 (+8.2%) &mdash; back above SMA50 $220.37 for the first time since the stop-out. But that average is <strong>still falling</strong>, so this is where ORCL stood three weeks ago: '
 'reclaim done, flatten and rise pending. Price has also left the $195&ndash;215 zone. Not a setup.'),

row('12','r3','AMD','Advanced Micro Devices','Tagged Zone And Left &mdash; Again','Below, SMA50 falling &#9888;','sma-b','&ge;40M shares/day','SMA50 reclaim first','--','--muted','$415','BLOCKED','fit-lo',
 '$477.45 (+4.5%) &mdash; bounced back OUT of the $440&ndash;470 zone <strong>without ever qualifying while inside it</strong>. Second time tagged and left unfilled. '
 'SMA50 $498.85 still falling, price $21 under. The zone was set beneath the average by design so a tag alone cannot trigger entry &mdash; working as intended.'),

row('13','r3','AVGO','Broadcom Inc.','&#9888; BROKEN &mdash; Only Decliner','Below, SMA50 falling &#9888;','sma-b','n/a &mdash; structure broken','No entry','--','--muted','$340','AVOID','fit-lo',
 '$357.87 &mdash; <strong style="color:var(--red)">the ONLY watchlist name DOWN (&minus;2.6%) in a broad risk-on bounce</strong> that lifted beaten-down peers 8&ndash;9%. '
 'Third consecutive call up as the weakest structure; two zone breaks this cycle. Non-participation in a rally that lifted everything else is the same signal that preceded VRT falling 27% &mdash; '
 'and VRT at least bounced. No entry, no averaging down.'),
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
