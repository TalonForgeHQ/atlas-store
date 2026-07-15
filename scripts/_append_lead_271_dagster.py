import csv, sys
from pathlib import Path

REPO = Path(r"C:/Users/Potts/projects/atlas-store")
LEADS_CSV = REPO / "cold_email" / "leads.csv"
TIERREASON_FILE = REPO / "_tick179_tierreason.txt"

INDEX = "271"
NAME = "Dagster"
HANDLE = "@dagster"
EMAIL = "privacy@elementl.com"
VERTICAL = "ai_agents_infra"
TIER = "1"
TEMPLATE = "360_dagster.md"

tier_reason = TIERREASON_FILE.read_text(encoding="utf-8").rstrip()

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

with LEADS_CSV.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["index","name","handle","email","vertical","tier","template","tier_reason"], quoting=csv.QUOTE_ALL)
    w.writerow(row)

print(f"APPENDED: {INDEX} {NAME} ({EMAIL}) -> {LEADS_CSV}")

# parse-back verify
with LEADS_CSV.open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
last = rows[-1]
assert last["index"] == INDEX, f"INDEX mismatch: expected {INDEX} got {last['index']}"
assert last["email"] == EMAIL, f"EMAIL mismatch"
assert len(last["tier_reason"]) > 1500, f"tier_reason too short: {len(last['tier_reason'])}"
print(f"PARSE-BACK OK: index={last['index']} email={last['email']} tier_reason_len={len(last['tier_reason'])}")
print(f"TOTAL ROWS NOW: {len(rows)}")