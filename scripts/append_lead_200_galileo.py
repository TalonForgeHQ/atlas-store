import csv, os, sys
from pathlib import Path

CSV_PATH = r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv"
TIER_PATH = r"C:\Users\Potts\AppData\Local\Temp\tier_reason_200_galileo.txt"
INDEX = "200"
NAME = "Galileo"
HANDLE = "@rungalileo"
EMAIL = "team@galileo.ai"
VERTICAL = "ai_infra"
TIER = "1"
TEMPLATE = "286_galileo.md"

tier_reason = Path(TIER_PATH).read_text(encoding="utf-8").strip()

row = {
    "index": INDEX,
    "name": NAME,
    "handle": HANDLE,
    "email": EMAIL,
    "vertical": VERTICAL,
    "tier": TIER,
    "template": TEMPLATE,
    "tier_reason": tier_reason,
}

with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

assert not any(r["index"] == INDEX for r in rows), f"index {INDEX} already exists"

rows.append(row)

with open(CSV_PATH, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), quoting=csv.QUOTE_ALL)
    w.writeheader()
    for r in rows:
        w.writerow(r)

# Parse-back verification
with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
    parsed = list(csv.DictReader(f))

last = parsed[-1]
assert last["index"] == INDEX, f"index mismatch: {last['index']}"
assert last["email"] == EMAIL, f"email mismatch: {last['email']}"
assert not last["tier_reason"].startswith('"'), f"tier_reason starts with quote (broken csv-write pattern)"
assert "Galileo Evaluate" in last["tier_reason"], "tier_reason missing key term"

print(f"OK: appended index {INDEX} ({NAME}) -- leads.csv now has {len(parsed)} rows")
print(f"  email: {last['email']}")
print(f"  tier_reason len: {len(last['tier_reason'])} chars")
