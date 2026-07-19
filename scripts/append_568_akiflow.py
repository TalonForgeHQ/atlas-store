"""Append Akiflow 568 lead row to cold_email/leads.csv. Idempotent: bails if index already present."""
import csv
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
CSV_PATH = REPO / "cold_email" / "leads.csv"
TIER_REASON_FILE = Path(r"C:\Users\Potts\AppData\Local\Temp\568_akiflow_tier_reason.txt")

INDEX = "568"
NAME = "Akiflow"
HANDLE = "@akiflowhq"
EMAIL = "support@akiflow.com"
VERTICAL = "ai_work_management"
TIER = "1"
TEMPLATE = "568_akiflow.md"
TIER_REASON = TIER_REASON_FILE.read_text(encoding="utf-8").strip()

# Pre-flight: row-prefix anchor (pitfall #69)
csv_text = CSV_PATH.read_text(encoding="utf-8")
assert f'"{INDEX}","' not in csv_text, f"Row {INDEX} already present; bail"
assert len(TIER_REASON) > 100, "tier_reason too short"

# Pre-flight: schema is 8 columns
fieldnames = ["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"]
with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    assert reader.fieldnames == fieldnames, f"Schema mismatch: {reader.fieldnames}"
    existing_rows = list(reader)

row = dict(zip(fieldnames, [INDEX, NAME, HANDLE, EMAIL, VERTICAL, TIER, TEMPLATE, TIER_REASON]))

with CSV_PATH.open("a", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writerow(row)

# Parse-back verify
with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
assert len(rows) == len(existing_rows) + 1, f"Row count delta wrong: {len(rows)} vs {len(existing_rows)+1}"
matches = [r for r in rows if r["index"] == INDEX]
assert len(matches) == 1, f"Expected exactly 1 row for {INDEX}, got {len(matches)}"
m = matches[0]
assert m["name"] == NAME and m["handle"] == HANDLE and m["email"] == EMAIL
assert m["vertical"] == VERTICAL and m["tier"] == TIER
assert m["template"] == TEMPLATE
assert "Brad Flora" in m["tier_reason"] and "Nunzio Martinello" in m["tier_reason"]
print(f"OK row {INDEX}: {NAME} / {EMAIL} / {VERTICAL} / tier {TIER}")
print(f"Total rows: {len(rows)}")
