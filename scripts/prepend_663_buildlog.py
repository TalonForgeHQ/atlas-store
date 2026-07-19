#!/usr/bin/env python3
"""Prepend Roboflow 663 build-log entry to build-log.html.

Build-log is reverse-chronological (Variant C wrapper: <div class="tick-entry" data-tick="...">).
We prepend BEFORE the first existing tick-entry opening tag.
"""
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
BL = REPO / "build-log.html"
NEW_ENTRY = Path(r"C:\Users\Potts\AppData\Local\Temp\tick_663_buildlog_entry.html").read_text(encoding="utf-8")

TICK_ID = "2026-07-20-fast-exec-roboflow-663"

text = BL.read_text(encoding="utf-8")

# Pre-flight: anchor not already present
anchor = f'data-tick="{TICK_ID}"'
assert text.count(anchor) == 0, f"build-log already contains tick {TICK_ID} — refusing to double-write"

# Newest-first invariant: anchor must be prepended BEFORE first existing tick-entry opening tag
opening_tag = '<div class="tick-entry"'
opening_idx = text.find(opening_tag)
assert opening_idx >= 0, "no <div class=\"tick-entry\"> found — wrong build-log shape"

# Probe for CRLF leading (Variant C on Windows may start with \r\n)
# Allow up to 5 bytes of leading whitespace per pitfall #75a
assert opening_idx < 5, f"opening_tag not at top of file: opening_idx={opening_idx} — wrong shape"

new_text = NEW_ENTRY + "\n" + text[opening_idx:]
# Splice in: text[:opening_idx] + NEW_ENTRY + text[opening_idx:]
new_text = text[:opening_idx] + NEW_ENTRY + "\n" + text[opening_idx:]

# Verify post-write
assert new_text.count(anchor) == 1, f"anchor count != 1 after prepend: {new_text.count(anchor)}"

# Verify reverse-chronological: our anchor precedes the most-recent prior SHIP tick (Vapi 661)
prior_ship = 'data-tick="2026-07-20-fast-exec-vapi-661"'
our_attr_idx = new_text.find(anchor)
opening_tag_idx_after = new_text.find(opening_tag)
opening_tag_end = opening_tag_idx_after + len(opening_tag) + 1  # +1 for trailing space
# In Variant C, the opening tag is followed by the data-tick attribute directly
# Check our anchor is at opening_tag_end position
assert our_attr_idx == opening_tag_idx_after + len(opening_tag) + 1, \
    f"anchor offset wrong: our={our_attr_idx} expected={opening_tag_idx_after + len(opening_tag) + 1}"
prior_idx = new_text.find(prior_ship)
assert our_attr_idx < prior_idx, f"our anchor not before prior SHIP: our={our_attr_idx} prior={prior_idx}"

# Verify ONE wrapper around the new entry
new_entry_anchor = f'data-tick="{TICK_ID}"'
assert new_text.count(f'<div class="tick-entry" {new_entry_anchor}') == 1, "new entry not wrapped exactly once"

BL.write_text(new_text, encoding="utf-8")

# Verify on disk
disk_text = BL.read_text(encoding="utf-8")
assert disk_text.count(anchor) == 1, f"disk verify FAIL: {disk_text.count(anchor)} occurrences"
assert disk_text.find(anchor) < disk_text.find(prior_ship), "disk verify FAIL: not reverse-chronological"
print(f"[OK] build-log.html prepended with tick {TICK_ID}")
print(f"[OK] anchor position: {disk_text.find(anchor)}")
print(f"[OK] prior (Vapi 661) position: {disk_text.find(prior_ship)}")
print(f"[OK] reverse-chronological invariant: {disk_text.find(anchor) < disk_text.find(prior_ship)}")
print(f"[OK] file size: {len(disk_text)} chars")