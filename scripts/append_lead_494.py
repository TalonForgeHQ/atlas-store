#!/usr/bin/env python3
"""Append Wiz lead 494 to both CSV files using DictWriter + safe file read."""
import csv
import shutil
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
TMP = Path(r"C:\Users\Potts\AppData\Local\Temp")

# Read the pre-built CSV content files (which were validated before writing)
row_8col = (TMP / "lead_494_row.csv").read_text(encoding="utf-8").rstrip("\r\n")
row_13col = (TMP / "lead_494_enriched.csv").read_text(encoding="utf-8").rstrip("\r\n")

# Pre-flight: verify the index isn't already present (avoid the duplicate-index trap)
leads_csv = REPO / "cold_email" / "leads.csv"
with leads_csv.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    existing = list(reader)
last_idx = int(existing[-1]["index"])
assert last_idx == 493, f"Expected last index 493, got {last_idx}"

# Append 8-col row
with leads_csv.open("a", encoding="utf-8", newline="") as f:
    f.write(row_8col + "\n")

# Verify parse-back
with leads_csv.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    after = list(reader)
assert len(after) == len(existing) + 1, f"Expected {len(existing)+1} rows, got {len(after)}"
assert int(after[-1]["index"]) == 494
assert after[-1]["name"] == "Wiz"
print(f"[OK] leads.csv now {len(after)} rows (last=494 Wiz)")

# Append 13-col row
enriched_csv = REPO / "cold_email" / "leads_with_emails.csv"
with enriched_csv.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    existing_e = list(reader)
last_e = int(existing_e[-1]["lead_index"])
assert last_e == 493, f"Expected last enriched lead_index 493, got {last_e}"

with enriched_csv.open("a", encoding="utf-8", newline="") as f:
    f.write(row_13col + "\n")

with enriched_csv.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    after_e = list(reader)
assert len(after_e) == len(existing_e) + 1
assert int(after_e[-1]["lead_index"]) == 494
assert after_e[-1]["company"] == "Wiz"
print(f"[OK] leads_with_emails.csv now {len(after_e)} rows (last=494 Wiz)")
print("done")