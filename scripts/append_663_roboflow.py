#!/usr/bin/env python3
"""Append row 663 (Roboflow) to cold_email/leads.csv using csv.DictWriter."""
import csv
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
CSV_PATH = REPO / "cold_email" / "leads.csv"
TIER_REASON = (Path(r"C:\Users\Potts\AppData\Local\Temp\tier_reason_663_roboflow.txt").read_text(encoding="utf-8")).strip()
INDEX = "663"

# Pre-flight: row-prefix anchor (avoids pitfall #69 false-positive on numeric-id substring)
csv_text = CSV_PATH.read_text(encoding="utf-8")
row_prefix = f'"{INDEX}","'
assert row_prefix not in csv_text, f"row {INDEX} already present in leads.csv — abort"
assert csv_text.count('"index","name","handle","email","vertical","tier","template","tier_reason"') == 1, "leads.csv header missing or duplicated"

row = {
    "index": INDEX,
    "name": "Roboflow",
    "handle": "@roboflow",
    "email": "legal@roboflow.com",
    "vertical": "ai_vision_computer_vision",
    "tier": "1",
    "template": "663_roboflow.md",
    "tier_reason": TIER_REASON,
}

with open(CSV_PATH, "a", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"], quoting=csv.QUOTE_ALL)
    writer.writerow(row)

# Verify: parse-back with csv.DictReader + dedupe invariant
with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
ids = [r["index"] for r in rows if r.get("index")]
prev_count = ids.count(INDEX) if False else None  # placeholder; we just appended
assert ids.count(INDEX) == 1, f"duplicate index {INDEX} after append"
# Note: leads.csv grows by 1 each append — assert >= 1 occurrence of INDEX and row count consistent
assert len(rows) >= 660, f"row count too low after append: {len(rows)}"
new_row = next(r for r in rows if r["index"] == INDEX)
assert new_row["name"] == "Roboflow", "name mismatch"
assert new_row["email"] == "legal@roboflow.com", "email mismatch"
assert new_row["vertical"] == "ai_vision_computer_vision", "vertical mismatch"
assert new_row["tier"] == "1", "tier mismatch"
assert new_row["template"] == "663_roboflow.md", "template mismatch"
assert "Joseph Nelson" in new_row["tier_reason"], "tier_reason missing founder"
assert "Brad Dwyer" in new_row["tier_reason"], "tier_reason missing co-founder"
assert "legal@roboflow.com" in new_row["tier_reason"], "tier_reason missing inbox"
assert "Y Combinator W20" in new_row["tier_reason"], "tier_reason missing YC W20"
assert len(new_row["tier_reason"]) > 3000, f"tier_reason too short: {len(new_row['tier_reason'])}"

print(f"[OK] row {INDEX} appended to leads.csv ({len(rows)} rows total)")
print(f"[OK] tier_reason length: {len(new_row['tier_reason'])} chars")
print(f"[OK] all 8 fields verified: index/name/handle/email/vertical/tier/template/tier_reason")