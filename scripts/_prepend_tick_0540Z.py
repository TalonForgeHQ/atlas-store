"""Prepend research-only tick entry to build-log.html (Variant C anchor)."""
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
BUILD_LOG = REPO / "build-log.html"
ENTRY_FILE = Path("C:/Users/Potts/AppData/Local/Temp/tick_0540Z_entry.html")

new_entry = ENTRY_FILE.read_text(encoding="utf-8")
content = BUILD_LOG.read_text(encoding="utf-8")

anchor = '<div class="tick-entry"'
wrapper_count = new_entry.count(anchor)
assert wrapper_count == 1, f"wrapper count wrong: {wrapper_count}"

# Prepend
new_content = new_entry + "\n" + content
BUILD_LOG.write_text(new_content, encoding="utf-8")

# Verify
verify = BUILD_LOG.read_text(encoding="utf-8")
assert verify.startswith(new_entry), "prepend failed"
new_idx = verify.find('data-tick="2026-07-17-0540Z"')
old_idx = verify.find('data-tick="2026-07-17-0530Z"')
assert new_idx < old_idx, "ordering wrong"
print(f"OK: prepend succeeded, new file size = {len(verify)} bytes")