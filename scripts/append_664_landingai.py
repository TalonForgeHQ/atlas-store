#!/usr/bin/env python3
"""Append row 664 (LandingAI) to cold_email/leads.csv using csv.DictWriter."""
import csv
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
CSV_PATH = REPO / "cold_email" / "leads.csv"
TIER_REASON = (Path(r"C:\Users\Potts\AppData\Local\Temp\tier_reason_664_landingai.txt").read_text(encoding="utf-8")).strip()
INDEX = "664"

# Pre-flight: row-prefix anchor (avoids pitfall #69 false-positive on numeric-id substring)
csv_text = CSV_PATH.read_text(encoding="utf-8")
row_prefix = f'"{INDEX}","'
assert row_prefix not in csv_text, f"row {INDEX} already present in leads.csv - abort"
assert csv_text.count('"index","name","handle","email","vertical","tier","template","tier_reason"') == 1, "leads.csv header missing or duplicated"

# Read existing rows
with CSV_PATH.open("r", newline="", encoding="utf-8") as fh:
    reader = csv.reader(fh)
    rows = list(reader)
header = rows[0]
# new row
new_row = ["664", "LandingAI", "@landing_ai", "info@landing.ai", "ai_vision_computer_vision", "1", "664_landingai.md", TIER_REASON]
rows.append(new_row)

# Write back
with CSV_PATH.open("w", newline="", encoding="utf-8") as fh:
    writer = csv.writer(fh, quoting=csv.QUOTE_ALL, lineterminator="\n")
    writer.writerows(rows)

# Verify
verify_text = CSV_PATH.read_text(encoding="utf-8")
assert row_prefix in verify_text, f"row {INDEX} append failed - abort"
print(f"[ok] appended Lead 664 (LandingAI) to leads.csv ({len(rows)-1} data rows)")
