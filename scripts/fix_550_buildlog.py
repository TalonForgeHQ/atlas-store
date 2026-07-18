#!/usr/bin/env python3
"""
Tick 550 build-log fix — restructure nested-div bug.
Prior commit (ccb7def) inserted tick 550 ship entry INSIDE the existing tick 549 opening tag.
Fix: extract tick 550 entry, close it properly, then prepend it BEFORE the tick 549 entry.
"""
from pathlib import Path
import subprocess

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
BUILDLOG = REPO / "build-log.html"
TICK_SHIP = "2026-07-19-fast-exec-roboflow-549-chunk-ship"

bl = BUILDLOG.read_text(encoding="utf-8")

# anchor constants (concat, not f-string)
ANCHOR_SHIP_OPENING = '<div class="tick-entry" data-tick="' + TICK_SHIP + '">'
ANCHOR_LEAD_OPENING = '<div class="tick-entry" data-tick="2026-07-19-fast-exec-roboflow-549">'

# Step 1: find the tick 550 ship entry's full block (from its opening tag to its closing </div>)
ship_open_idx = bl.find(ANCHOR_SHIP_OPENING)
assert ship_open_idx > 0, "ship opening tag not found"
# The entry's content goes from ship_open_idx to the matching </div>
# Since the entry is malformed (nested), find the </div> that closes the OUTER (tick 549) entry
# That's the LAST </div> in the file? No — find the closing </div> AFTER the ship entry's content
# Simpler: extract the entry from ship_open_idx up to the next </div> that closes a div whose opening tag is at ship_open_idx
# Trick: the entry content has its own <h2> and ends with </div>. We can find the </div> right before the LEAD tick entry's opening tag.
lead_open_idx = bl.find(ANCHOR_LEAD_OPENING)
assert lead_open_idx >= 0, "lead opening tag not found"
# But wait — LEAD opening tag is BEFORE ship opening in the broken file. Let me re-check.
# Actually after the broken write: tick 549 LEAD opening tag is at byte 0, then my ship opening tag at byte 41.
# So lead_open_idx = 0. ship_open_idx = 41.
# The SHIP entry's content is from ship_open_idx to the </div> that closes the LEAD entry (which is now the OUTERMOST div).
# That's the LAST </div> in the file before the next tick entry.

# Find the position where the LEAD entry's content (including nested ship entry) ends — that's the closing </div>
# Search for </div> AFTER the LEAD opening tag (which is at 0)
# But the LEAD entry is now nested inside itself — the SHIP entry is the OUTERMOST.
# Strategy: find </div> that's followed by either the next tick-entry or </body>
# Actually simpler: rebuild from scratch.

# Read the broken file and identify what needs to be re-arranged
# The structure is broken — easier to rebuild: get tick 549 LEAD entry (everything from byte 0 to its closing </div>),
# extract tick 550 SHIP entry, then re-write as: tick 550 ship + tick 549 lead + everything after

# Find the LEAD entry's closing </div> — it's at the end of tick 549's content
# Strategy: find the </div> that closes the FIRST tick-entry (lead) — but because of nesting,
# we need to find the </div> that appears BEFORE the NEXT tick-entry opening tag (tick 548 or earlier)

# Find the next tick-entry opening tag after the LEAD one
next_tick_pattern = '<div class="tick-entry" data-tick="2026-07-19-fast-exec-fiddler-548">'
next_tick_idx = bl.find(next_tick_pattern)
assert next_tick_idx > 0, "next tick entry (fiddler 548) not found"
# LEAD entry's closing </div> is somewhere between LEAD opening (byte 0) and next_tick_idx
# Find the LAST </div> before next_tick_idx
lead_close_idx = bl.rfind("</div>", 0, next_tick_idx)
assert lead_close_idx > 0, "no </div> before fiddler 548"

# Extract the LEAD entry (now contains the nested SHIP entry)
lead_block = bl[0:lead_close_idx + len("</div>")]

# Now extract the SHIP entry from within lead_block
ship_open_in_lead = lead_block.find(ANCHOR_SHIP_OPENING)
assert ship_open_in_lead > 0, "ship opening not in lead block"
# The SHIP entry starts at ship_open_in_lead and ends at... well it's nested, so we need to find the SHIP entry's </div>
# The SHIP entry's own closing </div> was the one that closes the OUTER (LEAD) entry in the broken state.
# That's the LEAD entry's closing </div> at lead_close_idx.
# But there might be more </div> inside the SHIP entry's content (for <ul>/<li> nesting? no, ul/li don't use </div>)
# Actually checking my BL_ENTRY: it has <p>, <ul><li>...</li></ul>, <p> — no nested <div>.
# So the SHIP entry's </div> IS the LEAD entry's </div> at lead_close_idx.

# Build: extract SHIP entry (from ship_open_in_lead to end of lead_block - 6 for "</div>")
# Actually let's just take everything from ship_open_in_lead to lead_close_idx (exclusive)
ship_content = lead_block[ship_open_in_lead:lead_close_idx]
# Add a fresh </div> at the end for the SHIP entry
ship_entry = ship_content + "</div>\n"

# Extract the LEAD entry without the SHIP entry nested inside
# LEAD = opening tag + content (without ship) + closing </div>
lead_after_ship_open = lead_block.find(">", ship_open_in_lead) + 1  # position right after SHIP opening tag's ">"
# Skip the SHIP entry's content — find the SHIP entry's closing </div> which is at lead_close_idx
# So LEAD entry content is: from opening tag (byte 0) to ship_open_in_lead (exclusive), then from lead_close_idx (exclusive) to end of lead_block
# But that's not right either — the LEAD entry's content is everything between LEAD's opening tag and LEAD's </div>
# LEAD opening tag = "<div class=\"tick-entry\" data-tick=\"...roboflow-549\">"
# LEAD opening tag end: position of ">" in LEAD opening
lead_open_end = lead_block.find(">", 0) + 1
# LEAD content = lead_block[lead_open_end:lead_close_idx]
# But that content INCLUDES the SHIP entry. We need to extract SHIP first, then build LEAD without it.
# LEAD without SHIP = lead_block[lead_open_end:ship_open_in_lead] + lead_block[lead_close_idx:lead_close_idx + len("</div>")]
# Actually lead_close_idx already points to "</div>" of LEAD. So LEAD closing is lead_block[lead_close_idx:lead_close_idx+6]
lead_closing = lead_block[lead_close_idx:lead_close_idx + len("</div>")]

# Reconstruct LEAD entry without the nested SHIP
lead_entry_without_ship = (
    lead_block[0:lead_open_end] +  # LEAD opening tag
    lead_block[lead_open_end:ship_open_in_lead] +  # LEAD content before SHIP
    lead_closing +  # LEAD closing </div>
    "\n"
)

# Now reconstruct build-log.html:
#   ship_entry + lead_entry_without_ship + everything after lead_block
new_bl = ship_entry + lead_entry_without_ship + bl[lead_close_idx + len("</div>"):]

# Verify: new file should have exactly 1 SHIP anchor and 1 LEAD anchor (each in their own entry)
ship_count = new_bl.count('data-tick="' + TICK_SHIP + '"')
lead_count = new_bl.count('data-tick="2026-07-19-fast-exec-roboflow-549"')
assert ship_count == 1, f"SHIP anchor count {ship_count} != 1"
assert lead_count == 1, f"LEAD anchor count {lead_count} != 1"

# Verify SHIP entry is at the very top (Variant C: opening_tag_idx == 0)
opening_tag_idx = new_bl.find('<div class="tick-entry" ')
assert opening_tag_idx == 0, f"opening_tag_idx {opening_tag_idx} != 0"
opening_tag_end = opening_tag_idx + len('<div class="tick-entry" ')
ship_attr_idx = new_bl.find('data-tick="' + TICK_SHIP + '"')
assert ship_attr_idx == opening_tag_end, f"SHIP anchor at {ship_attr_idx}, expected {opening_tag_end}"

BUILDLOG.write_text(new_bl, encoding="utf-8")
print(f"[OK] build-log.html restructured: ship_entry={len(ship_entry)} bytes, lead_entry_without_ship={len(lead_entry_without_ship)} bytes")
print(f"[OK] SHIP anchor count={ship_count}, LEAD anchor count={lead_count}")
print(f"[OK] SHIP entry at top (Variant C opening_tag_idx=0, anchor at byte {ship_attr_idx})")
print(f"[OK] Total file size: {len(new_bl)} bytes (was {len(bl)})")