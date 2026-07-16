"""Prepend build-log entry to build-log.html (Variant C: top-level wrapper is <div class="tick-entry">)."""
from pathlib import Path

BL = Path(r"C:\Users\Potts\projects\atlas-store\build-log.html")
ENTRY = Path(r"C:\Users\Potts\AppData\Local\Temp\build_log_entry_307.txt").read_text(encoding="utf-8")

text = BL.read_text(encoding="utf-8")

# Variant C: topmost block uses <div class="tick-entry" data-tick="...">
anchor = '<div class="tick-entry"'
idx = text.find(anchor)
assert idx == 0, f"expected Variant C anchor at 0, found at {idx}"

# Sanity: new entry contains exactly one <div class="tick-entry" wrapper
n_wrapper = ENTRY.count('<div class="tick-entry"')
assert n_wrapper == 1, f"expected 1 wrapper, found {n_wrapper}"

new_text = text[:idx] + ENTRY + "\n" + text[idx:]
BL.write_text(new_text, encoding="utf-8")

delta = len(new_text) - len(text)
print(f"Wrote build-log.html: {len(text)} -> {len(new_text)} bytes (+{delta})")
print(f"Anchor: Variant C (<div class=\"tick-entry\"> at pos 0)")

# Verify ordering: new entry appears before all prior entries
new_h2 = new_text.find("Tick 2026-07-16-1148Z")
prior_1115 = new_text.find("Tick 2026-07-16-1115Z", new_h2)
print(f"new entry at byte {new_h2}, prior 1115Z at byte {prior_1115} (relative to new)")
if prior_1115 != -1:
    print("ordering OK (new before prior):", new_h2 < prior_1115)