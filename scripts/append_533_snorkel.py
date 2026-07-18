#!/usr/bin/env python3
"""Append Lead 533 (Snorkel AI) to cold_email/leads.csv."""
import csv
from pathlib import Path

CSV = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv")
REASON = Path(r"C:\Users\Potts\AppData\Local\Temp\533_tier_reason.txt")

INDEX = "533"
NAME = "Snorkel AI"
HANDLE = "@snorkelai"
EMAIL = "info@snorkel.ai"
VERTICAL = "ai_data_labeling"
TIER = "1"
TEMPLATE = "533_snorkel_ai.md"

reason_text = REASON.read_text(encoding="utf-8").rstrip()
assert f"Lead {INDEX} - " in reason_text, "tier_reason anchor missing"

# Pre-flight row-prefix idempotency guard (pitfall #69 — row-prefix anchor)
csv_text = CSV.read_text(encoding="utf-8")
row_anchor = f'"{INDEX}","'
assert csv_text.count(row_anchor) == 0, f"row {INDEX} already exists"

# Append row
row = [INDEX, NAME, HANDLE, EMAIL, VERTICAL, TIER, TEMPLATE, reason_text]
with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(row)

# Parse-back verification
with open(CSV, "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
match = [r for r in rows if r["index"] == INDEX]
assert len(match) == 1, f"expected 1 row, got {len(match)}"
assert match[0]["name"] == NAME
assert match[0]["email"] == EMAIL
assert match[0]["vertical"] == VERTICAL
print(f"OK lead {INDEX} ({NAME}) appended, total rows = {len(rows)}")