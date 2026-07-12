"""Append CelerData/Phoenix Data (index 189) to cold_email/leads.csv using two-tier pattern.

Tier 1: long tier_reason content lives in AppData/Local/Temp/tier_reason_189.txt (avoids
        bash heredoc quote-escape issues for embedded commas + double-quotes).
Tier 2: this script reads the temp file + writes the CSV row with csv.DictWriter.
"""
import csv
from pathlib import Path

LEADS_CSV = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv")
TIER_REASON_FILE = Path(r"C:\Users\Potts\AppData\Local\Temp\tier_reason_189.txt")

# Read tier_reason (one big string)
tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").rstrip()

# Sanity check length
print(f"tier_reason length: {len(tier_reason)} chars (expect ~7700)")

row = {
    "index": "189",
    "name": "CelerData (Phoenix Data)",
    "handle": "@CelerData",
    "email": "privacy@phoenixdata.ai",
    "vertical": "ai_data_warehouse",
    "tier": "1",
    "template": "269_celerdata.md",
    "tier_reason": tier_reason,
}

# Parse existing CSV to verify column order
with open(LEADS_CSV, encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

print(f"existing rows: {len(rows)}, last index: {rows[-1]['index']} ({rows[-1]['name']})")
print(f"fieldnames: {fieldnames}")

# Verify row-189 doesn't already exist (avoid duplicate-index failure)
existing_indexes = {r["index"] for r in rows}
if "189" in existing_indexes:
    raise SystemExit("ERROR: row 189 already exists in leads.csv — abort to avoid duplicate-index")

# Append the new row
with open(LEADS_CSV, encoding="utf-8", newline="", mode="a") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writerow(row)
print("row 189 written")

# Parse-back verification
with open(LEADS_CSV, encoding="utf-8", newline="") as f:
    rows2 = list(csv.DictReader(f))
new_row = rows2[-1]
print(f"verification: last row index={new_row['index']} name={new_row['name']} email={new_row['email']} tier_reason_len={len(new_row['tier_reason'])}")
print(f"total rows now: {len(rows2)}")