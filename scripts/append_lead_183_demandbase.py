"""Append Lead 183 (Demandbase) to cold_email/leads.csv using csv.DictWriter."""
import csv
import os

LEADS_CSV = r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv"
TIER_REASON_FILE = r"C:\Users\Potts\AppData\Local\Temp\tier_reason_183_demandbase.txt"

# Read the long tier_reason from disk
with open(TIER_REASON_FILE, "r", encoding="utf-8") as f:
    tier_reason = f.read().strip()

# Build the row
new_row = {
    "index": "183",
    "name": "Demandbase",
    "handle": "@Demandbase",
    "email": "privacy@demandbase.com",
    "vertical": "ai_sales_ai",
    "tier": "1",
    "template": "263_demandbase.md",
    "tier_reason": tier_reason,
}

# Verify last index is 182 before append
with open(LEADS_CSV, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    last_idx = int(rows[-1]["index"])
    assert last_idx == 182, f"Expected last index 182, got {last_idx}"
    print(f"Pre-append: {len(rows)} rows, last index = {last_idx}")

# Append
with open(LEADS_CSV, "a", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(new_row.keys()), quoting=csv.QUOTE_ALL)
    writer.writerow(new_row)

# Verify
with open(LEADS_CSV, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    last_row = rows[-1]
    print(f"Post-append: {len(rows)} rows")
    print(f"Last row index: {last_row['index']}")
    print(f"Last row name: {last_row['name']}")
    print(f"Last row email: {last_row['email']}")
    print(f"Last row vertical: {last_row['vertical']}")
    print(f"Last row template: {last_row['template']}")
    print(f"Last row tier_reason length: {len(last_row['tier_reason'])} chars")
    assert int(last_row["index"]) == 183, "Index mismatch"
    assert last_row["name"] == "Demandbase", "Name mismatch"
    assert last_row["email"] == "privacy@demandbase.com", "Email mismatch"
    print("VERIFICATION PASS: Lead 183 (Demandbase) appended cleanly with 8 columns.")
