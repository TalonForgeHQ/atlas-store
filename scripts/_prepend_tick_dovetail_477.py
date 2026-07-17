"""Prepend tick entry for lead 477 (Dovetail) to build-log.html."""
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
BUILD_LOG = REPO / "build-log.html"
ENTRY_FILE = Path(r"C:\Users\Potts\AppData\Local\Temp\tick_entry_dovetail_477.html")

new_entry = ENTRY_FILE.read_text(encoding="utf-8").rstrip() + "\n"

content = BUILD_LOG.read_text(encoding="utf-8")

# Sanity: Variant C structure detection
assert content.startswith('<div class="tick-entry"'), f"Unexpected build-log top shape: {content[:60]!r}"

# Wrapper-count sanity: exactly one <div class="tick-entry" in the new entry
tick_wrapper_count = new_entry.count('<div class="tick-entry"')
assert tick_wrapper_count == 1, f"New entry must contain exactly one tick-entry wrapper; got {tick_wrapper_count}"

# Anchor: prepend before the FIRST <div class="tick-entry" (Variant C, position 0)
anchor = '<div class="tick-entry"'
idx = content.find(anchor)
assert idx == 0, f"Expected Variant C with first tick-entry at position 0; found at {idx}"

new_content = new_entry + "\n" + content
BUILD_LOG.write_text(new_content, encoding="utf-8")

# Verify
content_after = BUILD_LOG.read_text(encoding="utf-8")
assert content_after.startswith(new_entry.rstrip()), "Build-log does NOT start with new entry after prepend"

# Count tick-entry wrappers
n_ticks = content_after.count('<div class="tick-entry"')
print(f"Total tick-entry wrappers after prepend: {n_ticks}")

# Verify chunk-298 + chunk-299 cross-references appear in entry
for needle in ["chunk 299", "lead 477", "Dovetail", "legal@dovetail.com", "Benjamin Humphrey", "Bradley Ayers", "Didier Elzinga", "chunk_298"]:
    assert needle in new_entry, f"Missing required token in entry: {needle}"
    print(f"  OK: {needle!r} present")

# Verify cross-tick-inlining-regression fix claim is in entry
assert "chunk_298.html" in new_entry and "index.html" in new_entry and "sitemap.xml" in new_entry, "Cross-tick-inlining fix claim missing details"
print("  OK: cross-tick-inlining-regression fix claim present")

print("\nALL CHECKS PASSED — build-log entry prepended successfully")
