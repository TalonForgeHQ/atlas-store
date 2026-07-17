#!/usr/bin/env python3
"""Append lead 487 (UserTesting) to cold_email/leads.csv using the safe two-tier pattern."""
import csv
import sys
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
CSV_PATH = REPO / "cold_email" / "leads.csv"
TIER_REASON_FILE = Path(r"C:\Users\Potts\AppData\Local\Temp\lead487_tier_reason.txt")

tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").strip()

row = {
    "index": "487",
    "name": "UserTesting",
    "handle": "@usertesting",
    "email": "press@usertesting.com",
    "vertical": "ai_research",
    "tier": "1",
    "template": "487_usertesting.md",
    "tier_reason": tier_reason,
}

# Pre-flight: read existing rows, verify schema + baseline + no dup index
with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    existing = list(reader)

assert fieldnames == ["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"], \
    f"unexpected schema: {fieldnames}"
print(f"[pre-flight] rows={len(existing)}, last_index={existing[-1]['index']}")
assert len(existing) >= 360, f"baseline too low: {len(existing)} (expected >=360)"
indices = [r["index"] for r in existing]
assert indices.count("487") == 0, "index 487 already present"
assert all(indices.count(i) == 1 for i in indices), "duplicate index found"

# Append (mode='a' is the ONLY safe mode per tick 116 + tick 485 lessons)
with open(CSV_PATH, "a", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writerow(row)

# Parse-back verification
with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
assert rows[-1]["index"] == "487", f"append failed; last row index={rows[-1]['index']}"
assert rows[-1]["name"] == "UserTesting"
assert rows[-1]["vertical"] == "ai_research"
assert "press@usertesting.com" in rows[-1]["email"]
assert "Darrell Benatar" in rows[-1]["tier_reason"]
assert "Hans Larsen" in rows[-1]["tier_reason"]
assert "Eric Johnson" in rows[-1]["tier_reason"]
assert "Thoma Bravo" in rows[-1]["tier_reason"]
print(f"[verify] rows now={len(rows)} (was {len(existing)}; +1 expected)")
print(f"[verify] last_index={rows[-1]['index']} name={rows[-1]['name']} vertical={rows[-1]['vertical']}")
print(f"[verify] tier_reason_chars={len(rows[-1]['tier_reason'])} (expected ~5937)")
print("OK: lead 487 appended safely")