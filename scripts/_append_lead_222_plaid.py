"""Append lead 222 (Plaid) to leads.csv using the tier_reason file."""
import csv
from pathlib import Path

CSV = Path(r"C:/Users/Potts/projects/atlas-store/cold_email/leads.csv")
TIER_FILE = Path(r"C:/Users/Potts/AppData/Local/Temp/tier_reason_222_plaid.txt")

with open(TIER_FILE, "r", encoding="utf-8") as f:
    tier_reason = f.read().strip()

row = {
    "index": "222",
    "name": "Plaid",
    "handle": "@plaid",
    "email": "privacy@plaid.com",
    "vertical": "finance_ops",
    "tier": "1",
    "template": "310_plaid.md",
    "tier_reason": tier_reason,
}

with open(CSV, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

# Duplicate-index guard
existing = {r["index"] for r in rows}
assert "222" not in existing, f"index 222 already exists"

with open(CSV, "a", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writerow(row)

# Parse-back verification
with open(CSV, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
last = rows[-1]
print(f"OK rows={len(rows)} index={last['index']} name={last['name']} email={last['email']} tlen={len(last['tier_reason'])}")
assert last["index"] == "222"
assert last["name"] == "Plaid"
assert last["email"] == "privacy@plaid.com"
assert last["tier_reason"].startswith("Canonical"), f"tier_reason must start with description, got: {last['tier_reason'][:50]}"