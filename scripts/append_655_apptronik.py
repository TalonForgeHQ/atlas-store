"""Append lead 655 (Apptronik) to leads.csv with row-prefix idempotency guard."""
import csv
from pathlib import Path

LEADS = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv")
TIER_REASON = Path(r"C:\Users\Potts\AppData\Local\Temp\tier_reason_655.txt")
INDEX = "655"
TEMPLATE = "655_apptronik.md"

# Read existing CSV
with LEADS.open("r", newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))
    fieldnames = rows[0]

# Idempotency guard (pitfall #69 — row-prefix anchor)
csv_text = LEADS.read_text(encoding="utf-8")
row_prefix = f'"{INDEX}","'
assert csv_text.count(row_prefix) == 0, f"row {INDEX} already present"

# Build new row
tier_reason = TIER_REASON.read_text(encoding="utf-8").strip()
new_row = {
    "index": INDEX,
    "name": "Apptronik",
    "handle": "@Apptronik",
    "email": "privacy@apptronik.com",
    "vertical": "physical_ai_robotics",
    "tier": "1",
    "template": TEMPLATE,
    "tier_reason": tier_reason,
}

# Append
with LEADS.open("a", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writerow(new_row)

# Parse-back verification
with LEADS.open("r", newline="", encoding="utf-8") as f:
    rows_after = list(csv.DictReader(f))
match = [r for r in rows_after if r["index"] == INDEX]
assert len(match) == 1, f"row {INDEX} not found exactly once"
assert match[0]["email"] == "privacy@apptronik.com"
assert match[0]["tier_reason"] == tier_reason
print(f"OK: appended row {INDEX} (Apptronik) to leads.csv")
print(f"   total rows now: {len(rows_after)}")
print(f"   tier_reason bytes: {len(tier_reason)}")