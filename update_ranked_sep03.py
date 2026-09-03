#!/usr/bin/env python3
"""Ranked swing candidates -> Sep 2. ANET to #1 as POTW; gate passes above blocks."""
import re, sys, os, shutil
FILE='templates/index.html'; shutil.copy(FILE,FILE+'.bak'); src=open(FILE).read()

def row(rank, cls, tk, co, setup, sma, smacls, vol, volsub, rr, rrcol, stop, fit, fitcls, note, potw=False):
    badge = ('\n            <div style="margin-top:4px"><span style="font-size:9px;font-weight:800;background:var(--accent);'
             'color:#000;padding:2px 7px;border-radius:2px;letter-spacing:.6px">PLAY OF THE WEEK</span></div>') if potw else ''
    tr = '        <tr class="potw-row">' if potw else '        <tr>'
    tkblock = (f'\n            <span class="tk">{tk}</span>\n            <div class="co">{co}</div>{badge}\n          ') if potw else f'<span class="tk">{tk}</span><div class="co">{co}</div>'
    return f"""{tr}
          <td><span class="rank-dot {cls}">{rank}</span></td>
          <td>{tkblock}</td>
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

rows = [
row('&#9733;1','r1','ANET','Arista Networks','Zone Entry &mdash; Perfect Stack','Above, SMA50 rising &#9650;','sma-a','&ge;8M shares/day','Rule 4 gate applies','4.90:1','--green','$170','BEST','fit-hi',
 '$186.10 (&minus;11.6%) &mdash; fell into zone $172&ndash;190. <strong style="color:var(--green)">The only one of SEVEN names in zones that passes the SMA gate.</strong> '
 'Stack is flawless: SMA50 $181.83 &gt; SMA100 $170.62 &gt; SMA150 $158.55 &gt; SMA200 $151.32, price above all four. '
 'Stop $170 = triple confluence (2&times;ATR $170.47, SMA100 $170.62, just under zone floor $172). <strong>Needs volume &ge;1.5&times; ADV to trigger.</strong>', potw=True),

row('2','r1','NOW','ServiceNow Inc.','Manage the Winner &mdash; Trail Raise','Above all 4 SMAs &#9650;','sma-a','n/a &mdash; position open','No new entry','3.0:1','--green','$124 trail','OPEN +32%','fit-hi',
 'Entered $103.24, now <strong style="color:var(--green)">$136.72 (+32.4%)</strong>. Rose 9.4% while SPY fell 0.9% and QQQ fell 2.0% &mdash; '
 'strongest relative strength on the board. <strong>Action: raise trail $113 &rarr; $124</strong> (2&times;ATR $6.09), locking +20.1%. Target $175. No adds.'),

row('3','r2','PANW','Palo Alto Networks','Near-Miss &mdash; Fresh Breakdown','Below a RISING SMA50 &#9888;','sma-b','&ge;8M shares/day','SMA50 reclaim first','--','--muted','$300','WATCH','fit-mid',
 '$328.48 &mdash; <strong style="color:var(--red)">biggest decliner (&minus;15.1%)</strong>, was the steadiest climber three weeks ago. In zone $322&ndash;350 but $20 under a '
 '<strong>RISING</strong> SMA50 $348.24 &mdash; a fresh breakdown, not an established downtrend. Reclaim $348 and it becomes a strong second setup. ZS earnings Thu Sep 3 is the read-through.'),

row('4','r2','NVDA','NVIDIA','Above Zone &mdash; Cleanest Structure','Above, both rising &#9650;','sma-a','&ge;180M shares/day','Waiting for pullback','5.8:1','--green','$192','WAIT','fit-mid',
 '$224.41 (+0.1%) &mdash; flat through a pullback that took QQQ down 2.0%. Quiet relative strength. '
 'SMA50 $209.15 and SMA100 $203.20 both rising, price above both. Zone $203&ndash;213 still $11 below. The pullback that hit six names did not reach NVDA.'),

row('5','r2','MSFT','Microsoft','Above Zone &mdash; Zone Closing','Above, SMA50 rising fast &#9650;','sma-a','&ge;45M shares/day','Waiting for pullback','5.2:1','--green','$385','WAIT','fit-mid',
 '$496.82 (+0.9%) &mdash; held the post-gap level. <strong>SMA50 has climbed $410 &rarr; $438 and caught the zone TOP</strong>, so $410&ndash;438 is closing from beneath. '
 'Any future pullback into it arrives with the SMA50 right there &mdash; a far cleaner test than July.'),

row('6','r2','PLTR','Palantir','Above Zone &mdash; Extension Resolving','Above by 15% (was 28%) &#9650;','sma-a','&ge;60M shares/day','Waiting for pullback','3.75:1','--green','$125','WAIT','fit-mid',
 '$169.46 (&minus;0.9%) &mdash; barely moved. The "most extended" flag is resolving the healthy way: SMA50 rose $134 &rarr; $147 while price held flat, '
 'narrowing the gap from 28% to 15% <strong>through time, not a drawdown</strong>. Moving from "do not chase" toward "watch for a routine pullback."'),

row('7','r3','DELL','Dell Technologies','&#9888; Above Zone &mdash; SMA50 Flattening','Above, but SMA50 FLAT &#9888;','sma-a','&ge;12M shares/day','Watch the 50','4.1:1','--accent','$392','CAUTION','fit-mid',
 '$492.20 (+1.6%) &mdash; one of only three names up. <strong style="color:var(--accent)">But SMA50 $434.17 has gone FLAT</strong> after weeks of steep gains. '
 'The AVGO lesson from this call up applies: a flat SMA50 is the absence of trend, and AVGO broke its zone three weeks after being flagged for exactly this. Watch for it to turn up or roll over.'),

row('8','r3','ORCL','Oracle','Repairing &mdash; Step 1 of 3','Above a FALLING SMA50 &#9654;','sma-b','&ge;20M shares/day','SMA50 must flatten','4.4:1','--accent','$128','BLOCKED','fit-lo',
 '$145.75 &mdash; <strong>closest ORCL has come.</strong> In zone $138&ndash;150 AND price has reclaimed SMA50 $139.69 for the first time in months. '
 'But that average is still FALLING, so the gate holds. Trend repair goes reclaim &rarr; flatten &rarr; rise; ORCL has done step one.'),

row('9','r3','AMD','Advanced Micro Devices','In Zone &mdash; Blocked By Design','Below, SMA50 falling &#9888;','sma-b','&ge;40M shares/day','SMA50 reclaim first','3.6:1','--accent','$415','BLOCKED','fit-lo',
 '$457.06 (&minus;5.4%) &mdash; entered zone $440&ndash;470 <strong>exactly as the Aug 13 redraw anticipated</strong>. That zone was set deliberately beneath the falling SMA50 '
 'so a zone tag alone could not trigger entry. SMA50 $501.70 still falling, price $45 below. Design working; entry needs the reclaim.'),

row('10','r3','MRVL','Marvell Technology','In Zone &mdash; Recovering Not Recovered','Below SMA50 $223 &#9888;','sma-b','&ge;12M shares/day','SMA50 reclaim first','4.6:1','--accent','$182','BLOCKED','fit-lo',
 '$206.48 (&minus;4.9%) &mdash; inside zone $195&ndash;215 but SMA50 $223.26 falling with price $17 beneath. Verdict unchanged. '
 'The trail that exited at $272 has avoided roughly 24% of downside at current prices, having peaked above 35% at the $189 low.'),

row('11','r3','LMND','Lemonade','In Zone 3rd Time &mdash; Knife Slowing','Below, SMA50 falling &#9888;','sma-b','&ge;3M shares/day','Base + SMA50 flatten','3.2:1','--accent','$38','BLOCKED','fit-lo',
 '$53.14 (+2.9%) &mdash; in zone $45&ndash;56 for the <strong>third consecutive call up</strong>. The knife is decelerating: basing sideways in the low $50s rather than making new lows. '
 'But SMA50 $58.83 still falls, price $5.69 below. Trigger unchanged: base above $52 <em>plus</em> a flattening SMA50. Has the first half only.'),

row('12','r3','VRT','Vertiv Holdings','&#9888; BROKEN &mdash; Warning Played Out','Below SMA50 + SMA100 &#9888;','sma-b','n/a &mdash; structure broken','Base + reclaim required','--','--muted','$240','AVOID','fit-lo',
 '$256.70 (&minus;11.0%) &mdash; now <strong style="color:var(--red)">27% below the Jul 17 level.</strong> The Aug 13 relative-weakness warning has played out in full. '
 'Price reached the $255&ndash;275 zone but SMA50 $284.54 still falls with price $28 under. <strong>That zone marks where a base might form, not a buy trigger.</strong>'),

row('13','r3','AVGO','Broadcom Inc.','&#9888; BROKEN &mdash; 2nd Zone Failure','Below, SMA50 falling &#9888;','sma-b','n/a &mdash; structure broken','Base + reclaim required','--','--muted','$340','AVOID','fit-lo',
 '$367.24 (&minus;11.7%) &mdash; broke BELOW the $390&ndash;408 zone redrawn just three weeks ago. <strong>Second zone break this cycle.</strong> '
 'Flagged Aug 13 as the weakest gate pass because its SMA50 was FLAT not rising &mdash; that caution was correct. A flat SMA50 is the absence of trend. Joins VRT as broken.'),
]

NEW = """  <!-- Swing candidates ranked table -->
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
""" + "\n".join(rows) + """
      </tbody>
    </table>
  </div>"""

pat = r'  <!-- Swing candidates ranked table -->\n  <div class="tbl-wrap">.*?\n      </tbody>\n    </table>\n  </div>'
src,n = re.subn(pat, lambda m: NEW, src, flags=re.DOTALL)
if n!=1: print(f'ERROR: {n} replacements'); sys.exit(1)
open(FILE,'w').write(src); print(f'OK - ranked table rebuilt ({len(rows)} rows)'); os.remove(FILE+'.bak')
