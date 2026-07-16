"""Prepend tick 283 entry to build-log.html. Newest-first invariant.
Build-log structure: starts with `<!-- TICK ... -->\n<div class="tick-entry" data-tick="...">`
"""
import re, sys
from pathlib import Path

BL = Path(r"C:\Users\Potts\projects\atlas-store\build-log.html")
ENTRY = Path(r"C:\Users\Potts\AppData\Local\Temp\tick_283_entry.html").read_text(encoding="utf-8")

content = BL.read_text(encoding="utf-8")

# Sanity
assert content.startswith('<!-- TICK'), f"Unexpected build-log start: {content[:30]!r}"
assert ENTRY.count('<div class="tick-entry"') == 1, "Entry should have exactly 1 tick-entry wrapper"
assert ENTRY.startswith('<!-- TICK'), "Entry should start with TICK comment"

# Prepend
new_content = ENTRY + "\n" + content

# Wrapper count invariant
new_count = new_content.count('<div class="tick-entry"')
old_count = content.count('<div class="tick-entry"')
assert new_count == old_count + 1, f"Wrapper count mismatch: {new_count} vs {old_count}+1"

# Verify newest-first invariant: find all tick timestamps in file order
# Use [^>]+ instead of \S+ (escape issue from shell)
positions = [(m.start(), m.group(1)) for m in re.finditer(r'<!-- TICK ([^>]+)-->', new_content)]
positions.sort()
sys.stdout.write("First 5 ticks in file order:\n")
for pos, ts in positions[:5]:
    sys.stdout.write(f"  pos={pos:>6d}  ts={ts}\n")

# Verify new entry is at position 0
assert positions[0][0] == 0, f"New entry should be at pos 0, got {positions[0][0]}"
# Verify new entry timestamp is 07:30Z
assert "07:30Z" in positions[0][1], f"New entry ts should contain 07:30Z, got {positions[0][1]!r}"
# Verify second entry is 07:20Z
assert "07:20Z" in positions[1][1], f"Second entry should be 07:20Z, got {positions[1][1]!r}"

BL.write_text(new_content, encoding="utf-8")
sys.stdout.write(f"\nPrepended tick 283 entry. New size: {len(new_content)} bytes\n")
sys.stdout.write(f"First 80 chars: {new_content[:80]!r}\n")
sys.stdout.flush()