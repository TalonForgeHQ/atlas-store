"""Prepend tick entry to build-log.html before the first <h2> or <div class="tick"> block."""
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
BUILDLOG = REPO / "build-log.html"
ENTRY_PATH = Path("C:/Users/Potts/AppData/Local/Temp/tick_new_entry.txt")

content = BUILDLOG.read_text(encoding="utf-8")
entry = ENTRY_PATH.read_text(encoding="utf-8").strip()

# Prepend BEFORE the first topmost tick block. Two possible anchors: <h2> (Variant A)
# or <div class="tick"> (Variant B). The current file uses Variant B (data-tick wrapper at top).
ANCHOR = '<div class="tick-entry" data-tick="'
idx = content.find(ANCHOR)
assert idx >= 0, f"anchor {ANCHOR!r} not found in build-log.html"

# Sanity: wrapper-count check (only 1 wrapper inside the new entry)
assert entry.count('<div class="tick-entry"') == 1, "new entry should have exactly 1 wrapper"

new_content = entry + "\n" + content[idx:]
# Validate: first characters should still be the new entry's wrapper
# (we're prepending BEFORE the prior first wrapper, so position 0 should be our new wrapper)
assert new_content.startswith('<div class="tick-entry" data-tick="2026-07-16-1515Z"'), \
    "prepend ordering broken: new entry not at top"

BUILDLOG.write_text(new_content, encoding="utf-8")

# Verify
final = BUILDLOG.read_text(encoding="utf-8")
assert final.startswith('<div class="tick-entry" data-tick="2026-07-16-1515Z"'), "topmost wrapper != 1515Z"
print(f"OK prepended tick 2026-07-16-1515Z; build-log.html now {len(final)} bytes / ~{final.count(chr(10))} lines")
