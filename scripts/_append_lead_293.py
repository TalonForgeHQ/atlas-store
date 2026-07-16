"""Append lead 293 (BigID) + verify. Idempotent on rerun."""
import csv
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
TIER = Path("C:/Users/Potts/AppData/Local/Temp/tier_bigid.txt")
leads = REPO / "cold_email" / "leads.csv"

# Read existing rows
with leads.open("r", encoding="utf-8", newline="") as f:
    rdr = csv.DictReader(f)
    header = rdr.fieldnames
    rows = list(rdr)

# Pre-flight: index 293 must NOT already be in leads.csv
existing_idxs = [r["index"] for r in rows]
assert "293" not in existing_idxs, f"293 already in leads.csv — aborting to avoid dup"

tier_reason = TIER.read_text(encoding="utf-8").strip()

new_row = {
    "index": "293",
    "name": "BigID",
    "handle": "@bigid",
    "email": "info@bigid.com",
    "vertical": "ai_data_security",
    "tier": "1",
    "template": "293_bigid.md",
    "tier_reason": tier_reason,
}

with leads.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL)
    w.writerow(new_row)

# Verify: re-parse, last row should be BigID 293
with leads.open("r", encoding="utf-8", newline="") as f:
    rdr = csv.DictReader(f)
    rows2 = list(rdr)
last = rows2[-1]
assert last["index"] == "293", f"last index != 293 (got {last['index']})"
assert last["name"] == "BigID", f"last name != BigID (got {last['name']})"
assert last["email"] == "info@bigid.com", f"email mismatch"
assert last["vertical"] == "ai_data_security", f"vertical mismatch"
print(f"OK appended row 293 (BigID); leads.csv now has {len(rows2)} rows")
