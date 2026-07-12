"""
Tick 73 build-log prepend helper.

Strategy: read build-log.html, find the FIRST '<div class="tick">', splice
the new Tick 73 entry (from scripts/tick_73_entry.html) in BEFORE that anchor.
This preserves the newest-first invariant (Tick 73 at lowest offset).
"""
import sys

BUILD_LOG = r"C:\Users\Potts\projects\atlas-store\build-log.html"
ENTRY_FILE = r"C:\Users\Potts\projects\atlas-store\scripts\tick_73_entry.html"

ANCHOR = '<div class="tick">'

with open(BUILD_LOG, "r", encoding="utf-8") as f:
    build_log = f.read()

with open(ENTRY_FILE, "r", encoding="utf-8") as f:
    new_entry = f.read()

# Pre-flight: refuse if Tick 73 already prepended (re-entry guard)
if "Tick 73" in build_log and "Apollo.io lead (174)" in build_log:
    print("  RE-ENTRY: Tick 73 already prepended — refusing to write again")
    sys.exit(0)

# Pre-flight: refuse if anchor isn't unique-ish (sanity check — should appear ~70+ times)
anchor_count = build_log.count(ANCHOR)
print(f"  anchor {ANCHOR!r} appears {anchor_count} times in build-log.html (sanity check; should be 60+)")

idx = build_log.find(ANCHOR)
if idx == -1:
    print("  FATAL: anchor not found — build-log.html structure may have changed")
    sys.exit(1)

print(f"  first anchor offset: {idx}")
print(f"  new entry length: {len(new_entry)} chars")

new_content = build_log[:idx] + new_entry + build_log[idx:]

# Verification
# 1. New entry must be BEFORE the existing first tick
tick73_offset = new_content.find("Tick 73 — Shipped: Apollo.io lead (174)")
old_first_tick_offset = new_content.find(ANCHOR)
assert tick73_offset != -1, "Tick 73 entry not found in new content"
assert old_first_tick_offset != -1, "old first tick anchor missing"
assert tick73_offset < old_first_tick_offset, f"newest-first invariant violated: tick73={tick73_offset} >= old_first_tick={old_first_tick_offset}"
print(f"  PASS: tick73_offset={tick73_offset} < old_first_tick_offset={old_first_tick_offset}")

# 2. Apollo.io + privacy@apollo.io + Tim Zheng + 254_apollo.md all present
assert "Apollo.io" in new_content
assert "privacy@apollo.io" in new_content
assert "Tim Zheng" in new_content
assert "254_apollo.md" in new_content
assert ("8th `ai_sales_ai`" in new_content) or ("ai_sales_ai 8th" in new_content), "missing '8th ai_sales_ai sibling' marker"
assert "EU AI Act Art. 53(d)" in new_content
assert "MMM-incrementality" in new_content
print("  PASS: all required Apollo anchors present in new build-log")

# 3. Pre-existing tick-72 anchor still present (no clobber)
assert "id=\"tick-72\"" in new_content
print("  PASS: tick-72 anchor preserved")

with open(BUILD_LOG, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"  write OK: build-log.html now {len(new_content)} bytes (was {len(build_log)})")
