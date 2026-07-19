"""Append lead 574 (Linear) to cold_email/leads.csv with idempotency guard."""
import csv
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
CSV_PATH = REPO / "cold_email" / "leads.csv"
TIER_REASON_FILE = Path(r"C:\Users\Potts\AppData\Local\Temp\tier_reason_574.txt")
INDEX = "574"

# Pre-flight idempotency: row-prefix anchor (pitfall #69)
csv_text = CSV_PATH.read_text(encoding="utf-8")
anchor = f'"{INDEX}","'
assert csv_text.count(anchor) == 0, f"Row {INDEX} already present in leads.csv — abort"

tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").strip()

row = {
    "index": INDEX,
    "name": "Linear",
    "handle": "@linear",
    "email": "hello@linear.app",
    "vertical": "ai_work_management",
    "tier": "1",
    "template": "574_linear.md",
    "tier_reason": tier_reason,
}

with CSV_PATH.open("a", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"],
        quoting=csv.QUOTE_ALL,
    )
    writer.writerow(row)

# Parse-back verification
with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
matches = [r for r in rows if r["index"] == INDEX]
assert len(matches) == 1, f"Expected 1 row for index {INDEX}, got {len(matches)}"
assert matches[0]["name"] == "Linear"
assert matches[0]["email"] == "hello@linear.app"
assert matches[0]["tier_reason"] == tier_reason
print(f"OK: lead {INDEX} appended ({len(rows)} total rows)")
