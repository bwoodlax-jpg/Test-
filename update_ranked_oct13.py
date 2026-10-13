#!/usr/bin/env python3
"""Ranked table -> Oct 12/13."""
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
row('&#9733;1','r1','NOW','ServiceNow Inc.','Manage the Winner &mdash; Trail Raise','Above all 4 SMAs &#9650;','sma-a','n/a &mdash; position open','No new entry','3.06:1','--green','$129 trail','OPEN +36%','fit-hi',
 '$140.32 Oct 12 close, <strong style="color:var(--green)">+35.9%</strong> from the $103.24 entry. <strong>The stack has REPAIRED</strong> &mdash; 50 $132.81 &gt; 100 $119.21 &gt; 200 $115.27 &gt; 150 $112.45, price above all four. '
 'At entry it was fully inverted. <strong>Raise trail $124 &rarr; $129</strong> (2&times;ATR $5.71), locking +25.0%. Target $175.', potw=True),

row('2','r1','ANET','Arista Networks','&#10003; CLOSED +6.8% &mdash; Peaked +16.5%','Fell to SMA50 $198.47 &#9654;','sma-a','n/a &mdash; closed','Position closed','&mdash;','--muted','$178','CLOSED','fit-mid',
 'Entered $186.10 Sep 3, peaked <strong style="color:var(--green)">$216.74 Oct 9 (+16.5%)</strong>, faded to $198.67 and landed exactly on the rising SMA50 &mdash; the Sep 5 warning line. '
 '<strong style="color:var(--accent)">Closed +6.8%.</strong> Analysis right, exit late: the stop sat at $178 for five weeks with no call up. <strong style="color:var(--red)">New rule: trail = 2&times;ATR below the highest close.</strong>'),

row('3','r2','ORCL','Oracle','Rising SMA50, Price Below &mdash; WATCH','Below a RISING SMA50 &#9888;','sma-b','&ge;20M shares/day','Reclaim $145.90 first','4.4:1','--accent','$128','WATCH','fit-mid',
 '$139.20 &mdash; fell <strong style="color:var(--red)">13.5% through Sep 10 earnings</strong>; the stand-aside call was right. Back in zone $138&ndash;150. '
 '<strong>Unusual configuration: SMA50 $145.90 is RISING with price $6.70 BELOW it</strong> &mdash; the inverse of a broken trend, and it resolves faster because the average comes to the price. Reclaim aligns zone and gate first time since June. Do not anticipate.'),

row('4','r2','NVDA','NVIDIA','&#9888; Above Zone &mdash; Relative Weakness','Above by only $2 &#9888;','sma-a','&ge;180M shares/day','Watch the $222.59 test','8.2:1','--accent','$208','CAUTION','fit-mid',
 '$226.32 &mdash; <strong style="color:var(--red)">DOWN 1.8% while AMD ran 24.5%, MRVL 19.0%, PANW 21.2%.</strong> The only large AI name to go nowhere as its sector advanced. '
 'Price sits just $2 above a rising SMA50 $222.59. Nothing broken, but relative weakness preceded VRT &minus;27% and AVGO&#39;s two zone breaks. TSM Thu Oct 15 is the upstream read.'),

row('5','r2','AMD','Advanced Micro Devices','Above Zone &mdash; Reclaimed And Ran','Above, SMA50 rising &#9650;','sma-a','&ge;40M shares/day','Waiting for pullback','5.3:1','--green','$505','WAIT','fit-mid',
 '$594.24 &mdash; <strong style="color:var(--green)">+24.5%, the biggest winner the gate cost.</strong> Reclaimed the falling SMA50 that blocked it twice, then ran. SMA50 $531.28 rising, SMA100 $521.74 just beneath &mdash; tight confluence. '
 'New zone $522&ndash;550. The old $440&ndash;470 zone was tagged twice and left unfilled, exactly as a zone set under a falling average should behave. 10% above the average &mdash; extended.'),

row('6','r2','PANW','Palo Alto Networks','Above Zone &mdash; Fresh Breakdown Resolved','Above, SMA50 rising &#9650;','sma-a','&ge;8M shares/day','Waiting for pullback','2.7:1','--green','$352','WAIT','fit-mid',
 '$403.83 (+21.2%). <strong style="color:var(--green)">The fresh-breakdown call was vindicated:</strong> on Sep 5 it was in zone but $16 under a RISING SMA50, and the note said reclaiming $349 would make it a strong setup. It reclaimed and ran. '
 'That distinction &mdash; rising average with price newly below vs an established downtrend &mdash; is the framework&#39;s most useful recent refinement.'),

row('7','r3','MRVL','Marvell Technology','Above Zone &mdash; Full Repair Complete','Above, SMA50 rising &#9650;','sma-a','&ge;12M shares/day','Waiting for pullback','4.75:1','--green','$225','WAIT','fit-mid',
 '$265.86 (+19.0%) &mdash; completed the three-step repair mapped on Sep 5 (reclaim &rarr; flatten &rarr; rise). SMA50 $238.06 and SMA100 $238.76 within <strong>$0.70</strong> &mdash; tightest confluence on the board. '
 '<strong style="color:var(--accent)">Longer arc:</strong> stopped out at $272 in July, fell to $189, back to $266 &mdash; still beneath its own stop-out level fifteen weeks later. Best evidence in the log for the trail rule.'),

row('8','r3','PLTR','Palantir','Above Zone &mdash; Extension Resolved Up','Above by 17% &#9650;','sma-a','&ge;60M shares/day','Waiting for pullback','3.3:1','--green','$165','WAIT','fit-mid',
 '$209.00 (+19.9%). For two call ups the note described the extension closing through time as the SMA50 rose toward a flat price. It resolved the other way &mdash; price ran, the average chased. '
 'SMA50 $178.70 rising fast. New zone $179&ndash;195, target raised to $260. Three straight call ups on the right side of the filter PLTR originally inspired.'),

row('9','r3','DELL','Dell Technologies','Above Zone &mdash; Flat-SMA Flag Resolved','Above, SMA50 rising &#9650;','sma-a','&ge;12M shares/day','Waiting for pullback','4.3:1','--green','$485','WAIT','fit-mid',
 '$576.76 (+10.1%). The flat-SMA50 caution is now <strong>two call ups resolved in favour of holding</strong>. New zone $509&ndash;535, target raised to $680. '
 '<strong style="color:var(--accent)">Pair with AVGO:</strong> both flagged in August for the identical flat average &mdash; DELL is 10% higher, AVGO broke two zone floors. Which is why a flat SMA50 earns a flag and a watch, not an action.'),

row('10','r3','MSFT','Microsoft','Above Zone &mdash; Old Zone Obsolete','Above, SMA50 rising &#9650;','sma-a','&ge;45M shares/day','Waiting for pullback','3.9:1','--green','$478','WAIT','fit-mid',
 '$541.15 (+8.3%). <strong>SMA50 $501.98 is now $64 ABOVE the old $410&ndash;438 zone top</strong> &mdash; that zone could never have been reached without a thesis break, and has been redrawn to $502&ndash;525 with target $650. '
 'The clean illustration of why zones need recalibrating in a trending tape. The Jul 30 Azure gap remains the gate&#39;s largest cost.'),

row('11','r3','VRT','Vertiv Holdings','&#9888; BROKEN &mdash; Second Zone Floor Failed','Below a FLAT SMA50 &#9888;','sma-b','n/a &mdash; structure broken','Base + reclaim required','&mdash;','--muted','$205','AVOID','fit-lo',
 '$239.36 (&minus;14.7%) &mdash; <strong style="color:var(--red)">restraint vindicated.</strong> On Sep 5 it sat $1.94 under its SMA50 and the note said watch, do NOT anticipate. It never reclaimed; it fell 14.7% through the September zone. '
 'Two zone floors broken this cycle, 27% below mid-August. Has now failed the base-plus-reclaim test twice. Zone redrawn $215&ndash;235.'),

row('12','r3','AVGO','Broadcom Inc.','&#9888; BROKEN &mdash; Fourth Call Up','Below, SMA50 falling &#9888;','sma-b','n/a &mdash; structure broken','No entry','&mdash;','--muted','$318','AVOID','fit-lo',
 '$354.73 (&minus;0.9%) &mdash; went <strong style="color:var(--red)">nowhere for five weeks while AMD ran 24.5%, MRVL 19.0%, PANW 21.2%.</strong> Its own sector left it behind. SMA50 $371.18 still falling. '
 '<strong>Fourth consecutive call up broken; two zone floors gone.</strong> AVGO is the control case for the flat-SMA50 rule first flagged Aug 13. Zone redrawn $330&ndash;350.'),

row('13','r3','LMND','Lemonade','&#9888; ZONE BREAKING &mdash; Fifth Call Up','Below, SMA50 falling &#9888;','sma-b','n/a &mdash; zone breaking','No entry','&mdash;','--muted','$33','AVOID','fit-lo',
 '$45.15 &mdash; sitting <strong>exactly ON the old $45 floor after FIVE call ups in the zone</strong>, down 15.5%. The trigger was stated identically every time (base above $52 + flattening SMA50) and never relaxed; the base broke and the average never flattened. '
 '<strong style="color:var(--accent)">A zone price keeps sinking through is being broken, not defended</strong> &mdash; the ORCL pattern. Zone redrawn down to $36&ndash;45. The gate earned this one.'),
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
