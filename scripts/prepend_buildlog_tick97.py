"""Prepend Tick 97 build-log entry using str.find + concat (not patch — anchor appears 96+ times)."""
BUILD_LOG = r"C:\Users\Potts\projects\atlas-store\build-log.html"
ENTRY_FILE = r"C:\Users\Potts\AppData\Local\Temp\tick97_buildlog_entry.html"

with open(ENTRY_FILE, encoding="utf-8") as f:
    new_entry = f.read().rstrip() + "\n"

with open(BUILD_LOG, encoding="utf-8") as f:
    content = f.read()

# Reverse-chronological invariant: prepend at position 0.
# The current topmost tick (Tick 96) is NOT wrapped in <div class="tick"> —
# its <h2> is at the very start of the file. So we prepend before <h2>.
anchor = '<h2>'
idx = content.find(anchor)
assert idx == 0, f"expected first <h2> at position 0, got {idx} — file structure unexpected"
assert not new_entry.startswith(anchor), "entry contains anchor — would double-insert"

# Prepend the new entry block (wrapped in <div class="tick">) BEFORE the first <h2>
new_block = f'<div class="tick">\n{new_entry}\n</div>\n'

# Offset assertions (pitfall #21: newest-first invariant)
# After prepend, the new Tick 97 h2 must appear BEFORE the existing Tick 96 h2.
prepended = content[:idx] + new_block + content[idx:]
# Verify newest-first invariant
tick97_pos = prepended.find('Tick 97')
tick96_pos = prepended.find('Tick 96')
assert 0 <= tick97_pos < tick96_pos, (
    f"NEWEST-FIRST INVARIANT VIOLATED: tick97_pos={tick97_pos}, tick96_pos={tick96_pos}"
)

with open(BUILD_LOG, "w", encoding="utf-8") as f:
    f.write(prepended)

print(f"[ok] prepended Tick 97 entry ({len(new_entry)} chars) to build-log.html")
print(f"[verify] tick97_pos={tick97_pos} < tick96_pos={tick96_pos} (newest-first OK)")
print(f"[verify] total file size now: {len(prepended)} bytes")