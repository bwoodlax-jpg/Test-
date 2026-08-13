#!/usr/bin/env python3
"""Rewrite the swing candidates ranked table with Aug 12 structure.
The prior table was May-era (MRVL as POTW, SG archived) and contradicted the POTW cards."""
import re, sys, os, shutil

FILE = 'templates/index.html'
shutil.copy(FILE, FILE + '.bak')
src = open(FILE, 'r').read()

NEW_TABLE = """  <!-- Swing candidates ranked table -->
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
        <tr class="potw-row">
          <td><span class="rank-dot r1">&#9733;1</span></td>
          <td>
            <span class="tk">NOW</span>
            <div class="co">ServiceNow Inc.</div>
            <div style="margin-top:4px"><span style="font-size:9px;font-weight:800;background:var(--accent);color:#000;padding:2px 7px;border-radius:2px;letter-spacing:.6px">PLAY OF THE WEEK</span></div>
          </td>
          <td style="font-size:11px">Manage the Winner &mdash; Trail Raise</td>
          <td><span class="sma-a">Above all 4 SMAs &#9650;</span></td>
          <td style="font-size:11px">n/a &mdash; position open<div class="co">No new entry</div></td>
          <td class="r" style="font-size:12px;color:var(--green)">4.2:1</td>
          <td class="r" style="font-size:12px;color:var(--red)">$113 trail</td>
          <td><span class="fit-hi">OPEN +21%</span></td>
          <td style="font-size:11px;color:var(--dim);max-width:190px">
            Entered $103.24 at the zone floor (Jul 19&ndash;25 POTW), now $124.94 for <strong style="color:var(--green)">+21.0%</strong>.
            Cleared SMA200 $122.44 &mdash; uptrend confirmed, inverted-stack caveat retired.
            <strong>Action: raise stop $88 &rarr; $113</strong> (2&times;ATR $5.95), locking +9.5%. Target $175 still 40% away.
            Do not add at $125 &mdash; entry window closed.
          </td>
        </tr>
        <tr>
          <td><span class="rank-dot r1">2</span></td>
          <td><span class="tk">LMND</span><div class="co">Lemonade</div></td>
          <td style="font-size:11px">Only Name In Zone &mdash; Watch</td>
          <td><span class="sma-b">Below, SMA50 falling &#9888;</span></td>
          <td style="font-size:11px">&ge;3M shares/day<div class="co">Base confirmation</div></td>
          <td class="r" style="font-size:12px;color:var(--accent)">3.2:1</td>
          <td class="r" style="font-size:12px;color:var(--red)">$38</td>
          <td><span class="fit-lo">BLOCKED</span></td>
          <td style="font-size:11px;color:var(--dim);max-width:190px">
            $51.64, down 23% &mdash; the <strong>only watchlist name inside its zone</strong> ($45&ndash;56).
            But SMA50 $60.04 is falling with price $8.40 beneath it: falling-knife structure the gate exists to catch.
            <strong style="color:var(--accent)">Trigger to watch:</strong> base above $52 + SMA50 flattening. That would make it the first new entry in weeks.
          </td>
        </tr>
        <tr>
          <td><span class="rank-dot r2">3</span></td>
          <td><span class="tk">AVGO</span><div class="co">Broadcom Inc.</div></td>
          <td style="font-size:11px">Zone Redrawn &mdash; SMA Confluence</td>
          <td><span class="sma-a">Above, SMA50 flat &#9654;</span></td>
          <td style="font-size:11px">&ge;25M shares/day<div class="co">Avg ~20M</div></td>
          <td class="r" style="font-size:12px;color:var(--green)">4.9:1</td>
          <td class="r" style="font-size:12px;color:var(--red)">$368</td>
          <td><span class="fit-mid">WAIT</span></td>
          <td style="font-size:11px;color:var(--dim);max-width:190px">
            $416.05 (+12%). SMA50 $393.47 and SMA100 $390.98 sit almost on top of each other &mdash; an unusually tight support shelf.
            New zone $390&ndash;408. <strong style="color:var(--accent)">Caveat:</strong> SMA50 is flat, not rising &mdash; weakest trend of the eight gate-passers.
            Messy history: POTW at $360, blocked, +11%, round-tripped, now recovered.
          </td>
        </tr>
        <tr>
          <td><span class="rank-dot r2">4</span></td>
          <td><span class="tk">NVDA</span><div class="co">NVIDIA</div></td>
          <td style="font-size:11px">Zone Redrawn &mdash; Cleanest Stack</td>
          <td><span class="sma-a">Above, both rising &#9650;</span></td>
          <td style="font-size:11px">&ge;180M shares/day<div class="co">Avg ~150M</div></td>
          <td class="r" style="font-size:12px;color:var(--green)">5.8:1</td>
          <td class="r" style="font-size:12px;color:var(--red)">$192</td>
          <td><span class="fit-mid">WAIT</span></td>
          <td style="font-size:11px;color:var(--dim);max-width:190px">
            $224.09 (+10.5%). <strong>Cleanest SMA structure on the board:</strong> SMA50 $206.13 and SMA100 $203.20 both rising, price above both.
            New zone $203&ndash;213 at the confluence; stop $192 = old zone top, now flipped to support.
            No entry at $224 &mdash; the setup is a pullback to the averages.
          </td>
        </tr>
        <tr>
          <td><span class="rank-dot r2">5</span></td>
          <td><span class="tk">MSFT</span><div class="co">Microsoft</div></td>
          <td style="font-size:11px">Post-Gap &mdash; Extended</td>
          <td><span class="sma-a">Above, SMA50 now rising &#9650;</span></td>
          <td style="font-size:11px">&ge;45M shares/day<div class="co">Avg ~32M</div></td>
          <td class="r" style="font-size:12px;color:var(--green)">5.2:1</td>
          <td class="r" style="font-size:12px;color:var(--red)">$385</td>
          <td><span class="fit-mid">WAIT</span></td>
          <td style="font-size:11px;color:var(--dim);max-width:190px">
            $492.43 (+25%). <strong style="color:var(--red)">The gate's biggest miss.</strong> Blocked at $394 on a falling SMA50, then gapped 15.5% Jul 30 on Azure.
            SMA50 $410.30 now rising &mdash; trend genuinely turned. But 20% above it = extended. New zone $410&ndash;438, stop $385 below the gap origin.
            Argues for an earnings-gap exception to the filter.
          </td>
        </tr>
        <tr>
          <td><span class="rank-dot r3">6</span></td>
          <td><span class="tk">ANET</span><div class="co">Arista Networks</div></td>
          <td style="font-size:11px">Zone Redrawn &mdash; Trend Intact</td>
          <td><span class="sma-a">Above, rising &#9650;</span></td>
          <td style="font-size:11px">&ge;8M shares/day<div class="co">Avg ~5M</div></td>
          <td class="r" style="font-size:12px;color:var(--green)">3.7:1</td>
          <td class="r" style="font-size:12px;color:var(--red)">$158</td>
          <td><span class="fit-mid">WAIT</span></td>
          <td style="font-size:11px;color:var(--dim);max-width:190px">
            $210.50 (+25%). Spring supply-chain fears did not derail anything &mdash; the $8.9B defensive purchase commitments look like good management.
            SMA50 $172.58 rising. New zone $172&ndash;190. Ultra Ethernet taking real share from InfiniBand; $3.5B AI fabric revenue confirms it.
          </td>
        </tr>
        <tr>
          <td><span class="rank-dot r3">7</span></td>
          <td><span class="tk">DELL</span><div class="co">Dell Technologies</div></td>
          <td style="font-size:11px">Zone Redrawn (2nd) &mdash; Recovered</td>
          <td><span class="sma-a">Above, rising strongly &#9650;</span></td>
          <td style="font-size:11px">&ge;12M shares/day<div class="co">Avg ~9M</div></td>
          <td class="r" style="font-size:12px;color:var(--green)">4.1:1</td>
          <td class="r" style="font-size:12px;color:var(--red)">$392</td>
          <td><span class="fit-mid">WAIT</span></td>
          <td style="font-size:11px;color:var(--dim);max-width:190px">
            $484.50 (+22%). <strong style="color:var(--green)">Vindication for the Jun 11 redraw:</strong> setting the zone at the gap origin $335&ndash;355 rather than a shallow pullback
            is why the recovery was tradeable &mdash; DELL based there and ran 40%. New zone $418&ndash;448 on the rising SMA50.
          </td>
        </tr>
        <tr>
          <td><span class="rank-dot r3">8</span></td>
          <td><span class="tk">PANW</span><div class="co">Palo Alto Networks</div></td>
          <td style="font-size:11px">Zone Redrawn &mdash; Steadiest Trend</td>
          <td><span class="sma-a">Above, rising sharply &#9650;</span></td>
          <td style="font-size:11px">&ge;8M shares/day<div class="co">Avg ~6M</div></td>
          <td class="r" style="font-size:12px;color:var(--green)">3.4:1</td>
          <td class="r" style="font-size:12px;color:var(--red)">$300</td>
          <td><span class="fit-mid">WAIT</span></td>
          <td style="font-size:11px;color:var(--dim);max-width:190px">
            $387.01 (+7.9%). Smaller move than the AI names but the <strong>steadiest climb on the board</strong> &mdash; SMA50 went $258 &rarr; $322.
            Widest SMA50/SMA100 spread on the watchlist = very strong trend, but 20% above its own filter = extended. New zone $322&ndash;350.
          </td>
        </tr>
        <tr>
          <td><span class="rank-dot r3">9</span></td>
          <td><span class="tk">PLTR</span><div class="co">Palantir Technologies</div></td>
          <td style="font-size:11px">Most Extended &mdash; Do Not Chase</td>
          <td><span class="sma-a">Above by 28% &#9888;</span></td>
          <td style="font-size:11px">&ge;60M shares/day<div class="co">Avg ~45M</div></td>
          <td class="r" style="font-size:12px;color:var(--accent)">3.75:1</td>
          <td class="r" style="font-size:12px;color:var(--red)">$125</td>
          <td><span class="fit-lo">NO CHASE</span></td>
          <td style="font-size:11px;color:var(--dim);max-width:190px">
            $171.04 &mdash; <strong>biggest four-week move on the board (+29%)</strong> and the most extended name here.
            New zone $138&ndash;152 at the SMA50/SMA100 confluence. PLTR is the name that produced the SMA filter in the first place;
            it is now on the right side of it. Respect the filter both ways &mdash; do not chase 29% in four weeks.
          </td>
        </tr>
        <tr>
          <td><span class="rank-dot r3">10</span></td>
          <td><span class="tk">MRVL</span><div class="co">Marvell Technology</div></td>
          <td style="font-size:11px">Recovering &mdash; Gate Still Blocks</td>
          <td><span class="sma-b">Below SMA50 $241 &#9888;</span></td>
          <td style="font-size:11px">&ge;12M shares/day<div class="co">SMA50 reclaim first</div></td>
          <td class="r" style="font-size:12px;color:var(--accent)">4.6:1</td>
          <td class="r" style="font-size:12px;color:var(--red)">$182</td>
          <td><span class="fit-lo">BLOCKED</span></td>
          <td style="font-size:11px;color:var(--dim);max-width:190px">
            $217.08 (+15% off the $189 low). New zone $195&ndash;215 anchored on SMA100 $195.12 and the recovery base.
            <strong style="color:var(--accent)">Recovering, not recovered</strong> &mdash; SMA50 $240.97 still above price.
            The trail that exited at $272 avoided a further 35% of downside. No re-entry until the SMA50 is reclaimed.
          </td>
        </tr>
        <tr>
          <td><span class="rank-dot r3">11</span></td>
          <td><span class="tk">AMD</span><div class="co">Advanced Micro Devices</div></td>
          <td style="font-size:11px">Divergence &mdash; Below Trend Filter</td>
          <td><span class="sma-b">Below, SMA50 falling &#9888;</span></td>
          <td style="font-size:11px">&ge;40M shares/day<div class="co">SMA50 reclaim first</div></td>
          <td class="r" style="font-size:12px;color:var(--accent)">3.6:1</td>
          <td class="r" style="font-size:12px;color:var(--red)">$415</td>
          <td><span class="fit-lo">BLOCKED</span></td>
          <td style="font-size:11px;color:var(--dim);max-width:190px">
            $482.93 &mdash; <strong style="color:var(--red)">DOWN 2.6% while peers ran 10&ndash;29%.</strong>
            The only large AI name still beneath its own trend filter (SMA50 $511.56, falling).
            MI400 thesis unchanged ($60B committed) but relative weakness in a melt-up deserves respect. New zone $440&ndash;470, set below the SMA50 by design.
          </td>
        </tr>
        <tr>
          <td><span class="rank-dot r3">12</span></td>
          <td><span class="tk">ORCL</span><div class="co">Oracle</div></td>
          <td style="font-size:11px">Bounced &mdash; Trend Not Repaired</td>
          <td><span class="sma-b">Below, SMA50 falling &#9888;</span></td>
          <td style="font-size:11px">&ge;20M shares/day<div class="co">SMA50 reclaim first</div></td>
          <td class="r" style="font-size:12px;color:var(--accent)">4.4:1</td>
          <td class="r" style="font-size:12px;color:var(--red)">$128</td>
          <td><span class="fit-lo">BLOCKED</span></td>
          <td style="font-size:11px;color:var(--dim);max-width:190px">
            $153.28 (+21% off the lows &mdash; strongest bounce on the board in percentage terms). Still blocked:
            SMA50 $155.58 falling, price beneath it. <strong>A 21% bounce does not undo a broken trend.</strong>
            ORCL is the name that validated the gate (&minus;30% through its zone). New zone $138&ndash;150 reflects where it actually based.
          </td>
        </tr>
        <tr>
          <td><span class="rank-dot r3">13</span></td>
          <td><span class="tk">VRT</span><div class="co">Vertiv Holdings</div></td>
          <td style="font-size:11px">&#9888; BROKEN &mdash; Zone Floor Failed</td>
          <td><span class="sma-b">Below SMA50 + SMA100 &#9888;</span></td>
          <td style="font-size:11px">n/a &mdash; structure broken<div class="co">Base + reclaim required</div></td>
          <td class="r" style="font-size:12px;color:var(--muted)">&mdash;</td>
          <td class="r" style="font-size:12px;color:var(--red)">$240</td>
          <td><span class="fit-lo">AVOID</span></td>
          <td style="font-size:11px;color:var(--dim);max-width:190px">
            $288.36 &mdash; fell <strong style="color:var(--red)">through</strong> the $290 zone floor. SMA50 $298 and SMA100 $303 both above price, both falling.
            <strong>The damning detail:</strong> &minus;0.4% over four weeks while every AI-infra peer ran 10&ndash;29%.
            Identical structure to ORCL before &minus;30%. Zone redrawn down to $255&ndash;275; entry requires base AND SMA50 reclaim.
          </td>
        </tr>
      </tbody>
    </table>
  </div>"""

# Replace from the ranked-table comment through its closing </div>
pattern = r'  <!-- Swing candidates ranked table -->\n  <div class="tbl-wrap">.*?\n      </tbody>\n    </table>\n  </div>'
new_src, count = re.subn(pattern, lambda m: NEW_TABLE, src, flags=re.DOTALL)

if count != 1:
    print(f'ERROR: expected 1 replacement, got {count}')
    sys.exit(1)

open(FILE, 'w').write(new_src)
print(f'OK - replaced ranked table ({count} substitution)')
os.remove(FILE + '.bak')
print('Cleaned up backup file')
