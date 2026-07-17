import pathlib

REPO = pathlib.Path(r"C:\Users\Potts\projects\atlas-store")
BUILD_LOG = REPO / "build-log.html"
TICK_ENTRY = pathlib.Path(r"C:\Users\Potts\AppData\Local\Temp\tick_0908Z_entry.html")

text = BUILD_LOG.read_text(encoding="utf-8")
entry = TICK_ENTRY.read_text(encoding="utf-8").strip()

# Detect Variant C: starts with `<div class="tick-entry"` — prepend before the FIRST existing tick-entry
if not text.startswith('<div class="tick-entry"'):
    raise SystemExit(f"ERROR: build-log.html is not Variant C; starts with: {text[:80]!r}")

# Prepend: place new entry at position 0, then a newline, then the rest.
new_text = entry + "\n" + text
BUILD_LOG.write_text(new_text, encoding="utf-8")

# Verify
v = BUILD_LOG.read_text(encoding="utf-8")
assert v.startswith('<div class="tick-entry" data-tick="2026-07-17-0908Z">')
assert v.count('<div class="tick-entry" data-tick="2026-07-17-0908Z">') == 1
# Sanity: the previous tick (0858Z) should still be present and now AFTER ours
assert 'data-tick="2026-07-17-0858Z"' in v
# Confirm newest-first order
pos_new = v.find('data-tick="2026-07-17-0908Z"')
pos_prev = v.find('data-tick="2026-07-17-0858Z"')
assert pos_new < pos_prev, f"ERROR: new tick at {pos_new} not before previous tick at {pos_prev}"
print(f"OK build-log.html: {len(text)} -> {len(v)} bytes (+{len(v)-len(text)})")
print(f"   new tick at byte {pos_new}, prev (0858Z) tick at byte {pos_prev}")