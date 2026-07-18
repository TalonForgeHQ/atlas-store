"""Append lead 522 (Bill.com / BILL Holdings) to cold_email/leads.csv — finance_ops cohort sibling #2 after Brex 521."""
import csv
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
LEADS = REPO / "cold_email" / "leads.csv"
TIER_REASON_FILE = Path(r"C:\Users\Potts\AppData\Local\Temp\lead522_tier_reason.txt")

INDEX = "522"
NAME = "Bill.com (BILL Holdings)"
HANDLE = "@bill"
EMAIL = "privacy@hq.bill.com"
VERTICAL = "finance_ops"
TIER = "1"
TEMPLATE = "522_bill.md"

with open(TIER_REASON_FILE, encoding="utf-8") as f:
    TIER_REASON = f.read().strip()

# Pre-flight: confirm row 522 not yet present
csv_text = LEADS.read_text(encoding="utf-8")
row_prefix = f'"{INDEX}","'
assert row_prefix not in csv_text, f"FAIL: row prefix {row_prefix!r} already present — aborting"

row = {
    "index": INDEX,
    "name": NAME,
    "handle": HANDLE,
    "email": EMAIL,
    "vertical": VERTICAL,
    "tier": TIER,
    "template": TEMPLATE,
    "tier_reason": TIER_REASON,
}

with open(LEADS, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow([row["index"], row["name"], row["handle"], row["email"], row["vertical"], row["tier"], row["template"], row["tier_reason"]])

# Parse-back verify
with open(LEADS, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
match = [r for r in rows if r["index"] == INDEX]
assert len(match) == 1, f"FAIL: expected 1 row with index={INDEX}, got {len(match)}"
m = match[0]
assert m["name"] == NAME
assert m["email"] == EMAIL
assert m["vertical"] == VERTICAL
assert m["tier"] == TIER
assert m["template"] == TEMPLATE
print(f"OK: appended lead {INDEX} ({NAME}) → {EMAIL} | vertical={VERTICAL} tier={TIER}")
print(f"OK: leads.csv now has {len(rows)} rows")
