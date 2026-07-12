"""Append Spellbook (index 204) to cold_email/leads.csv with tier_reason read from a temp file."""
import csv
import sys
from pathlib import Path

LEADS = Path("C:/Users/Potts/projects/atlas-store/cold_email/leads.csv")
TIER = Path("C:/Users/Potts/AppData/Local/Temp/tier_reason_204_spellbook.txt")

tier_reason = TIER.read_text(encoding="utf-8").strip()
assert tier_reason, "tier_reason file empty"
assert not tier_reason.startswith('"'), "tier_reason must be plain field text"

row = {
    "index": "204",
    "name": "Spellbook",
    "handle": "@spellbooklegal",
    "email": "security@spellbook.legal",
    "vertical": "legal_ops",
    "tier": "1",
    "template": "291_spellbook.md",
    "tier_reason": tier_reason,
}

with LEADS.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(
        f,
        fieldnames=["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"],
        quoting=csv.QUOTE_ALL,
    )
    w.writerow(row)

# Parse-back verify
import csv as _csv
with LEADS.open("r", encoding="utf-8") as f:
    rows = list(_csv.DictReader(f))
last = rows[-1]
assert last["index"] == "204", f"index mismatch: {last['index']}"
assert last["name"] == "Spellbook", f"name mismatch: {last['name']}"
assert last["email"] == "security@spellbook.legal", f"email mismatch: {last['email']}"
assert not last["tier_reason"].startswith('"'), "tier_reason double-quote wrap bug"
assert "5K+" in last["tier_reason"], "tier_reason body sanity fail"
print(f"PASS row_count={len(rows)} last_index={last['index']} name={last['name']} email={last['email']}")
