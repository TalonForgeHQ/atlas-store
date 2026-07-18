#!/usr/bin/env python3
"""
Tick 550 build-log fix v2 — properly restructure nested-div bug.
Broken structure:
  [LEAD opening tag]\n
  [SHIP entry: opening tag + content + </div>]\n
  [LEAD h2 + LEAD content + LEAD closing </div>]

Right structure (Variant C reverse-chronological, newest first):
  [SHIP entry: opening tag + content + </div>]\n
  [LEAD entry: opening tag + h2 + content + </div>]\n
  ...
"""
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
BUILDLOG = REPO / "build-log.html"
TICK_SHIP = "2026-07-19-fast-exec-roboflow-549-chunk-ship"

ANCHOR_SHIP_OPENING = '<div class="tick-entry" data-tick="' + TICK_SHIP + '">'
ANCHOR_LEAD_OPENING = '<div class="tick-entry" data-tick="2026-07-19-fast-exec-roboflow-549">'

bl = BUILDLOG.read_text(encoding="utf-8")

# Step 1: find SHIP opening tag
ship_open_idx = bl.find(ANCHOR_SHIP_OPENING)
assert ship_open_idx >= 0, "ship opening tag not found"

# Step 2: find LEAD closing </div> by finding the </div> that appears right before the next tick-entry
next_tick = '<div class="tick-entry" data-tick="2026-07-19-fast-exec-fiddler-548">'
next_tick_idx = bl.find(next_tick)
assert next_tick_idx > 0, "next tick (fiddler 548) not found"
# LEAD closing </div> is the LAST </div> before next_tick_idx
# But because of nesting, the LEAD's content includes SHIP entry, and SHIP entry's </div> is BEFORE LEAD's </div>.
# So: rfind("</div>", 0, next_tick_idx) gives LEAD's </div>.
lead_close_idx = bl.rfind("</div>", 0, next_tick_idx)
assert lead_close_idx > 0, "LEAD closing </div> not found"

# Step 3: find SHIP closing </div> — it's the </div> that comes AFTER ship_open_idx
# Since SHIP content has no nested <div>, the first </div> after ship_open_idx is SHIP's closing
ship_close_idx = bl.find("</div>", ship_open_idx)
assert ship_close_idx > ship_open_idx and ship_close_idx < lead_close_idx, "SHIP closing </div> not between ship_open and lead_close"
# SHIP entry = ship_open_idx to ship_close_idx + len("</div>")
ship_entry = bl[ship_open_idx:ship_close_idx + len("</div>")] + "\n"
print(f"SHIP entry extracted: bytes {ship_open_idx}..{ship_close_idx+6} ({len(ship_entry)} bytes)")

# Step 4: extract LEAD content (h2 + body)
# LEAD opening tag is at byte 0. LEAD's actual <h2> starts AFTER the SHIP entry.
# LEAD h2 = position of "<h2>" AFTER the ship_close_idx + 6
lead_h2_idx = bl.find("<h2>", ship_close_idx)
assert lead_h2_idx > ship_close_idx, "LEAD h2 not after SHIP closing"

# LEAD closing tag: from ship_close_idx + 6 to lead_close_idx + 6 (which is "</div>")
lead_body_with_closing = bl[ship_close_idx + len("</div>"):lead_close_idx + len("</div>")]
# LEAD entry = LEAD opening + lead_body_with_closing + newline
lead_entry = ANCHOR_LEAD_OPENING + "\n" + lead_body_with_closing + "\n\n"
print(f"LEAD entry extracted: bytes {ship_close_idx+6}..{lead_close_idx+6} ({len(lead_entry)} bytes)")

# Step 5: build new build-log.html: ship_entry + lead_entry + rest
new_bl = ship_entry + lead_entry + bl[lead_close_idx + len("</div>"):]

# Verify
ship_count = new_bl.count('data-tick="' + TICK_SHIP + '"')
lead_count = new_bl.count('data-tick="2026-07-19-fast-exec-roboflow-549"')
assert ship_count == 1, f"SHIP anchor count {ship_count} != 1"
assert lead_count == 1, f"LEAD anchor count {lead_count} != 1"

# Verify SHIP at top
opening_tag_idx = new_bl.find('<div class="tick-entry" ')
assert opening_tag_idx == 0, f"opening_tag_idx {opening_tag_idx} != 0"
opening_tag_end = opening_tag_idx + len('<div class="tick-entry" ')
ship_attr_idx = new_bl.find('data-tick="' + TICK_SHIP + '"')
assert ship_attr_idx == opening_tag_end, f"SHIP anchor at {ship_attr_idx}, expected {opening_tag_end}"

# Verify LEAD has h2 + content (not empty)
lead_h2_new = new_bl.find("<h2>Tick 549: Roboflow")
assert lead_h2_new > 0, "LEAD h2 not found in new file"
print(f"LEAD h2 found at byte {lead_h2_new} in new file")

# Verify LEAD entry has actual content (not just opening + closing)
lead_entry_section = new_bl[opening_tag_idx:lead_h2_new + 100]
assert "Joseph Nelson" in lead_entry_section or "computer_vision cohort opener" in lead_entry_section, f"LEAD content missing: {lead_entry_section[:500]}"

BUILDLOG.write_text(new_bl, encoding="utf-8")
print(f"\n[OK] build-log.html restructured: {len(new_bl)} bytes (was {len(bl)})")
print(f"[OK] SHIP entry at top ({len(ship_entry)} bytes), LEAD entry second ({len(lead_entry)} bytes)")
print(f"[OK] SHIP anchor count={ship_count}, LEAD anchor count={lead_count}")