#!/usr/bin/env python3
"""WL -> Oct 16. PLTR stop 165->170; NOW trail 129->135.40; notes refreshed."""
import re, sys, os, shutil
FILE='templates/index.html'; shutil.copy(FILE,FILE+'.bak'); src=open(FILE).read()

UP = {
'PLTR': (None,None,'$170',
 'ACTIVE SETUP &mdash; PLAY OF THE WEEK Oct 19&ndash;23, CONDITIONAL. PLTR fell 11.0% from $209.00 to $186.03, into zone $179&ndash;195, and closed ABOVE a RISING SMA50 $182.57 &mdash; the ONLY one of thirteen names to be in a zone and clear the trend gate simultaneously. Four others sit in zones (NVDA, AMD, LMND) and all have price beneath their SMA50. Stack near-perfect: SMA50 $182.57 &gt; SMA100 $157.19 &gt; SMA200 $152.65 &gt; SMA150 $152.25, inverted by only $0.40 at the back, price above all four. STOP TIGHTENED $165 &rarr; $170 (2x ATR of $7.75 = $170.53), below the $179 zone floor. R/R 4.61:1. BINDING CONDITIONS: volume &ge;1.5x the 20-day average on a green close (mandatory, not advisory); 0.5% size not 1%; a close under $182.57 kills it. Only $3.46 of cushion above the gate &mdash; under half an ATR. If the unwind continues there is no entry.'),
'NOW':  (None,None,'$135',
 'ACTIVE POSITION &mdash; +37.5% from the $103.24 entry, and the ONLY watchlist name UP over the unwind (+1.2% while QQQ fell 4.9%). $141.95 Oct 16 after touching $148.57 on Oct 15. Third consecutive call up showing relative strength against the tape. THE STANDING TRAIL RULE DID THE WORK: adopted Oct 13 as 2x ATR below the highest CLOSE since entry, it now computes $135.40 from the $148.57 high (ATR $6.59), versus the $129 set by hand four days ago &mdash; a $6 ratchet with no session required. That is the ANET dependency fixed in practice. Locks +31.2%, sits $0.55 above the rising SMA50 $134.85, R/R to $175 is 5.05:1.'),
'ANET': (None,None,'$178',
 'POSITION CLOSED +6.8% on Oct 13 &mdash; AND THE EXIT IS NOW VALIDATED. Entered $186.10, peaked at a $216.74 close (+16.5%), exited $198.67. ANET is now $177.03 &mdash; holding would show &minus;4.9% against the entry, and price has broken THROUGH the $178 stop, so the position would have closed anyway 11.7 points lower. The exit converted a trade that is now a loss into a booked gain. WHY IT WAS AVAILABLE: the SMA50 was named on Sep 5 as the line that mattered, before price reached it, which turned a judgement call under pressure into a pre-committed decision. SMA50 $198.42 has now turned DOWN and price is $21 beneath it. Zone $183&ndash;196 is broken. No re-entry until structure repairs.'),
'MSFT': (None,None,'$478',
 'CLOSEST THING TO A SECOND SETUP. MSFT $528.95 (&minus;2.3%) posted the second-best relative performance in a 4.9% QQQ decline. SMA50 $505.53 is still RISING with price $23 above it, and the stock sits just above the $502&ndash;525 zone &mdash; a further 1% decline puts MSFT IN zone with the gate intact, which would make it a genuine second entry. Worth watching closely this week. No watchlist earnings Oct 19&ndash;23, though SAP reports Wed Oct 21 as an enterprise-software read.'),
'NVDA': (None,None,'$208',
 'FLAG PLAYED OUT &mdash; BROKE THE SMA50. On Oct 13 NVDA was flagged for relative weakness (&minus;1.8% over five weeks while AMD ran 24.5% and MRVL 19.0%), sitting only $2 above a rising SMA50 $222.59, with the $222.59 test named as the thing to watch. It has fallen 5.4% to $214.14 and is now $9 BENEATH that average. It is inside the $214&ndash;223 zone and therefore blocked &mdash; in zone, below the gate. This is the THIRD time this cycle that relative weakness preceded a breakdown (VRT, AVGO, now NVDA), making it the most reliable early signal on this board.'),
'AMD':  (None,None,'$505',
 'IN ZONE, BELOW THE GATE. AMD fell 11.0% to $528.76, into the $522&ndash;550 zone, but price is now $8 BENEATH the rising SMA50 $537.14 &mdash; in zone, below the gate, blocked. It has given back nearly HALF of the +24.5% run that the gate blocked between Sep 4 and Oct 12. A rising SMA50 with price newly below it is the fresh-breakdown structure that resolved upward for PANW in September; it is unresolved here. Needs the reclaim, not just the zone tag. MI400 thesis unchanged.'),
'LMND': (None,None,'$33',
 'SIXTH CONSECUTIVE CALL UP IN ZONE, STILL BLOCKED. LMND $44.19 (&minus;2.1%), inside zone $36&ndash;45 with SMA50 $49.24 still falling and price beneath it. It fell less than the AI names this week only because it had already broken down months earlier. The answer has not changed across six sessions and the stated trigger has never been relaxed. Cumulative scorecard on this name: six blocked call ups, and LMND is 17% lower than when it first entered the zone in September. Repeating an unglamorous no is what the gate is for.'),
'ORCL': (None,None,'$128',
 'RECLAIM WATCH IS DEAD. On Oct 13 ORCL was the setup to watch &mdash; SMA50 $145.90 RISING with price $6.70 below, the inverse of a broken trend, with a reclaim of $145.90 flagged as the trigger and an explicit instruction not to anticipate it. The SMA50 has now turned back DOWN to $145.12 and price has fallen 6.7% to $128.22, $17 beneath it and below the $138&ndash;150 zone entirely. Not anticipating the reclaim was correct for the second consecutive instance (VRT was the first). The pattern is now clear: a rising average with price below is a WATCH, and it fails at least as often as it resolves.'),
'AVGO': (None,None,'$318',
 'FIFTH CONSECUTIVE CALL UP BROKEN. AVGO $328.81 (&minus;7.3%), now beneath the $330&ndash;350 zone redrawn only four days ago. SMA50 $365.73 falling with price $37 below. That is a third zone broken in this cycle. AVGO remains the control case for the flat-SMA50 rule first flagged on Aug 13 &mdash; every call up since has confirmed that reading, against DELL where the same flag resolved upward before reversing violently this week. No entry, no averaging down.'),
'MRVL': (None,None,'$225',
 'REPAIR REVERSED IN FOUR SESSIONS. MRVL fell 14.3% to $227.74 and has LOST the SMA50 $241.04 it reclaimed in the run-up to Oct 13, giving back roughly three quarters of the +19.0% advance. It is below the $238&ndash;252 zone. The full three-step repair that completed on Oct 13 has already undone itself, which is a useful caution about how quickly a freshly repaired trend can fail. The trail that exited this position at $272 in July still looks better than any point since.'),
'PANW': (None,None,'$352',
 'SMA50 HAS GONE FLAT &mdash; THE WARNING NOW APPLIES TO PANW. It fell 15.3% to $341.89, giving back three quarters of the +21.2% run, and the SMA50 $373.27 has gone FLAT with price $31 beneath it. PANW was the vindication case for the fresh-breakdown distinction in September; it is now on the other side of that same analysis. Below its $372&ndash;390 zone. The flat-SMA50 rule derived from AVGO applies here directly: a flat average is the absence of trend and should be treated closer to falling than rising.'),
'VRT':  (None,None,'$205',
 'THIRD ZONE BROKEN THIS CYCLE. VRT fell another 13.8% to $206.42, beneath the $215&ndash;235 zone redrawn four days ago. SMA50 $255.46 falling with price $49 below. VRT is now down roughly 36% since mid-August, and has broken three successive zone floors. The restraint shown on Sep 5 &mdash; when it sat $1.94 from an SMA50 reclaim and the note said watch, do not anticipate &mdash; has now been vindicated twice over. Backlog $15B (+109% YoY) intact throughout; purely a price-structure failure.'),
'DELL': (None,None,'$485',
 'WORST ON THE BOARD &mdash; &minus;21.7% IN FOUR SESSIONS. DELL $451.67, having given back the entire +10.1% gain and a great deal more. SMA50 $513.26 is still technically RISING but price is $62 beneath it and below the $509&ndash;535 zone &mdash; a rising average with price that far below is a fresh and violent breakdown. The flat-SMA50 flag raised on Sep 3 resolved upward twice and has now reversed hard, which is the honest coda: a flat average is genuinely ambiguous, and resolving upward once does not settle it.'),
}
for tk,(entry,target,stop,note) in UP.items():
    m = re.search(r"\{ticker:'"+tk+r"',.*?\n", src)
    if not m: print(f'ERROR: {tk}'); sys.exit(1)
    line=m.group(0); new=line
    if entry: new = re.sub(r"entry:'[^']*'", "entry:'"+entry+"'", new)
    if target: new = re.sub(r"target:'[^']*'", "target:'"+target+"'", new)
    if stop: new = re.sub(r"stop:'[^']*'", "stop:'"+stop+"'", new)
    new = re.sub(r"note:'(?:[^'\\]|\\.)*'\}", "note:'"+note.replace('\\','\\\\').replace("'","\\'")+"'}", new)
    if new==line: print(f'ERROR: {tk} unchanged'); sys.exit(1)
    src = src.replace(line,new,1); print(f'  {tk}'+(f' stop {stop}' if stop else ''))
open(FILE,'w').write(src); print('OK - WL refreshed'); os.remove(FILE+'.bak')
