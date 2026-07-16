#!/usr/bin/env python3
"""Prepend tick 2026-07-16-1907Z entry to build-log.html (Variant C, data-tick anchor)."""
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
BUILD_LOG = REPO / "build-log.html"
ENTRY_FILE = Path("C:/Users/Potts/AppData/Local/Temp/tick_2026-07-16-1907Z_buildlog_entry.html")

entry = ENTRY_FILE.read_text(encoding="utf-8").strip()
text = BUILD_LOG.read_text(encoding="utf-8")

# Variant C anchor: first <div class="tick-entry" data-tick=...> wrapper
anchor = '<div class="tick-entry" data-tick='
idx = text.find(anchor)
assert idx > 0, f"no data-tick anchor at top of file; first 80 chars: {text[:80]!r}"

new = text[:idx] + entry + "\n\n" + text[idx:]
BUILD_LOG.write_text(new, encoding="utf-8")

# verify
verify = BUILD_LOG.read_text(encoding="utf-8")
assert 'data-tick="2026-07-16-1907Z"' in verify
# Must contain new entry exactly once (no double-prepend)
new_entry_count = verify.count('data-tick="2026-07-16-1907Z"')
assert new_entry_count == 1, f"new entry count = {new_entry_count}, expected 1"
# Counter checks
promptarmor_count = verify.count("PromptArmor")
promptarmor_347_count = verify.count("lead 347") + verify.count("Lead 347") + verify.count("347 PromptArmor")
print(f"OK: prepended. PromptArmor mentions={promptarmor_count}, lead-347 refs={promptarmor_347_count}")
