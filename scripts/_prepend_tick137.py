"""Prepend Tick 137 entry to build-log.html above Tick 136 wrapper."""
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
log = REPO / "build-log.html"
new_entry = (REPO / "_tick137_content.html").read_text(encoding="utf-8")
content = log.read_text(encoding="utf-8")

# Determine variant: Variant B (top is <div class="tick">)
assert content.startswith('<div class="tick">'), f"build-log.html does not start with <div class=\"tick\">: starts with {content[:30]!r}"

# Sanity check: new entry must contain exactly one <div class="tick"> wrapper
wrapper_count = new_entry.count('<div class="tick">')
assert wrapper_count == 1, f"new entry must have exactly 1 <div class=\"tick\"> wrapper, got {wrapper_count}"

# Locate the FIRST <div class="tick"> in the file (the topmost wrapper)
idx = content.find('<div class="tick">')
assert idx == 0, f"topmost <div class=\"tick\"> not at position 0 (got {idx})"

# Sanity: the Tick 136 <h2> marker must come AFTER position 0 (so we're splicing above Tick 136)
tick_136_pos = content.find("<h2>[Tick 136]")
assert tick_136_pos > 0, f"Tick 136 marker not found"

# Splice: prepend new_entry + content from idx onwards
new_content = new_entry + "\n" + content[idx:]
log.write_text(new_content, encoding="utf-8")
print(f"Prepended Tick 137 above Tick 136: log size {len(content)} -> {len(new_content)} bytes")

# Re-verify
verify = log.read_text(encoding="utf-8")
assert verify.startswith('<div class="tick">')
assert verify.find("<h2>[Tick 137]") == 0 or verify.find("<div class=\"tick\">") == 0
# Verify reverse-chronological ordering
pos_137 = verify.find("<h2>[Tick 137]")
pos_136 = verify.find("<h2>[Tick 136]")
pos_135 = verify.find("<h2>[Tick 135]")
assert pos_137 < pos_136 < pos_135, f"order broken: 137@{pos_137} 136@{pos_136} 135@{pos_135}"
# Verify exactly one Tick 137 wrapper
tick137_count = verify.count("<h2>[Tick 137]")
assert tick137_count == 1, f"Tick 137 appears {tick137_count} times"
# Verify the Tick 137 wrapper count
tick137_wrapper_count = sum(1 for i in range(len(verify)) if verify[i:].startswith('<div class="tick">') and verify.count('<div class="tick">', 0, i) == 0)
print(f"Tick 137 position: {pos_137}")
print(f"Tick 136 position: {pos_136}")
print(f"Tick 135 position: {pos_135}")
print(f"build-log.html prepended cleanly, reverse-chrono verified")