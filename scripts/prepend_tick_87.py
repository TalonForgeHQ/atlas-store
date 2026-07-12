"""Prepend tick-87 build-log block using the str.find + concat pattern.

Reverse-chronological invariant: new tick goes BEFORE the first <div class="tick">.
"""
from pathlib import Path

BL = Path(r"C:\Users\Potts\projects\atlas-store\build-log.html")
NEW = Path(r"C:\Users\Potts\AppData\Local\Temp\tick_87_block.html")

content = BL.read_text(encoding="utf-8")
new_block = NEW.read_text(encoding="utf-8")

# Find first <div class="tick">
anchor = '<div class="tick">'
idx = content.find(anchor)
if idx < 0:
    raise SystemExit("ERROR: anchor <div class=\"tick\"> not found in build-log.html")

# Splice: new_block + content from idx onward
prepended = new_block + "\n" + content[idx:]

# Write
BL.write_text(prepended, encoding="utf-8")

# Verify newest-first invariant
new_pos = prepended.find("Tick 87")  # text inside new_block
old_pos = prepended.find("Tick 86", new_pos)  # first tick-86 after tick-87
print(f"tick-87 position: {new_pos}")
print(f"tick-86 position (after tick-87): {old_pos}")
print(f"newest-first invariant: {'OK' if new_pos < old_pos else 'VIOLATED'}")
print(f"build-log.html size: {len(prepended)} chars")