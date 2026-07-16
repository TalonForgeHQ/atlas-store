"""Prepend tick 0640Z entry to build-log.html (Variant C)."""
from pathlib import Path

LOG = Path("C:/Users/Potts/projects/atlas-store/build-log.html")
ENTRY_PATH = Path("C:/Users/Potts/AppData/Local/Temp/tick_0640Z_entry.html")

content = LOG.read_text(encoding="utf-8")
entry = ENTRY_PATH.read_text(encoding="utf-8")

# Detect variant
print(f"top 50 chars: {repr(content[:50])}")
assert content.startswith('<div class="tick-entry"'), "expected Variant C"

# Wrap entry in Variant C wrapper
wrapper_open = '<div class="tick-entry" data-tick="2026-07-17-0640Z">\n'
wrapper_close = '\n</div>\n'
full_entry = wrapper_open + entry + wrapper_close

# Anchor on the first <div class="tick-entry"
anchor = '<div class="tick-entry"'
idx = content.find(anchor)
assert idx == 0, f"expected anchor at position 0, found at {idx}"

new_content = full_entry + content
LOG.write_text(new_content, encoding="utf-8")

# Verify
print(f"top 80 chars: {repr(new_content[:80])}")
print(f"total bytes: {len(new_content)}")
assert new_content.startswith('<div class="tick-entry" data-tick="2026-07-17-0640Z"'), "wrong prepend position"
# New entry wrapper count == 1
assert new_content.count('<div class="tick-entry" data-tick="2026-07-17-0640Z"') == 1, "wrapper check failed"
# data-tick for 0640Z exactly 1
tick_count = new_content.count('data-tick="2026-07-17-0640Z"')
print(f"data-tick 0640Z count: {tick_count}")
assert tick_count == 1, f"expected 1 occurrence of data-tick 0640Z, got {tick_count}"
# New entry <div class="tick-entry"> count
entry_div_count = new_content.count('<div class="tick-entry"')
print(f"<div class=\"tick-entry\"> count: {entry_div_count}")
print("OK build-log prepended")
