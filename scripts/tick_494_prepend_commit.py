#!/usr/bin/env python3
"""Prepend tick-494 build-log entry + verify + commit + push."""
import subprocess
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
ENTRY_FILE = Path(r"C:\Users\Potts\AppData\Local\Temp\tick_494_entry.html")
BL = REPO / "build-log.html"
TICK_ID = "2026-07-18-fast-exec-wiz-494"

# 1) Prepend entry before the FIRST <div class="tick-entry">
content = BL.read_text(encoding="utf-8")
entry = ENTRY_FILE.read_text(encoding="utf-8").rstrip("\n") + "\n"

# Detect variant via first-50-chars heuristic (Variant C: <div class="tick-entry" data-tick="...">)
first50 = content[:50]
assert first50.startswith('<div class="tick-entry"'), f"Unexpected BL variant: {first50!r}"

anchor = '<div class="tick-entry" data-tick="'
idx = content.find(anchor)
assert idx >= 0, "no tick-entry anchor found"

# Self-check: the entry MUST contain exactly one wrapper of type 'tick-entry'
wrapper_marker = '<div class="tick-entry"'
entry_wrapper_count = entry.count(wrapper_marker)
assert entry_wrapper_count == 1, f"entry wrapper count != 1: {entry_wrapper_count}"

# Self-check: data-tick attribute is the canonical anchor
assert f'data-tick="{TICK_ID}"' in entry, "tick id not in entry"

# Prepend (newest-first invariant)
new_content = content[:idx] + entry + content[idx:]
BL.write_text(new_content, encoding="utf-8")

# 2) Parse-back verify
post = BL.read_text(encoding="utf-8")
assert f'data-tick="{TICK_ID}"' in post[:5000], "tick-494 not in first 5KB"
# Locate it
tick_pos = post.find(f'data-tick="{TICK_ID}"')
# Find the previous tick
prev_pos = post[:tick_pos].rfind('data-tick="')
assert prev_pos < tick_pos
print(f"[OK] tick-494 at byte {tick_pos}, previous tick at byte {prev_pos}")
print(f"[OK] build-log size: {len(post):,} bytes")

# 3) Git add + commit + push
import os
os.chdir(REPO)
subprocess.run(["git", "add", "-A"], check=True)
result = subprocess.run(
    ["git", "commit", "-m", "fast-exec-494: Wiz lead + template + chunk_315 (ai_data_security NEW VERTICAL cohort opener + Google Cloud $32B acquisition March 2026 + 14-col provenance row + wizdom2025@wiz.io canonical strategic-inbound + 4-founder ex-Adallom + 5 audit gaps + EU AI Act Aug 2 2026 GPAI documentation package + Cyera 495 + Sentra 496 next-tick queue)"],
    check=True, capture_output=True, text=True,
)
print(f"[OK] commit: {result.stdout.strip()}")

result = subprocess.run(
    ["git", "push", "origin", "main"],
    check=True, capture_output=True, text=True,
)
print(f"[OK] push: {result.stdout.strip()}")

# 4) Cleanup one-shot helpers
for p in [Path(r"C:\Users\Potts\AppData\Local\Temp\lead_494_row.csv"),
          Path(r"C:\Users\Potts\AppData\Local\Temp\lead_494_enriched.csv"),
          Path(r"C:\Users\Potts\AppData\Local\Temp\tick_494_entry.html"),
          REPO / "scripts" / "append_lead_494.py"]:
    if p.exists():
        p.unlink()
        print(f"[OK] removed {p}")

print("done")