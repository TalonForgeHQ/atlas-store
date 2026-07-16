"""Append lead 412 (NVIDIA Garak) to cold_email/leads.csv.

Schema (8 cols): index, name, handle, email, vertical, tier, template, tier_reason
"""
import csv
from pathlib import Path

CSV_PATH = Path("C:/Users/Potts/projects/atlas-store/cold_email/leads.csv")
TIER_REASON_PATH = Path("C:/Users/Potts/AppData/Local/Temp/tier_reason_412.txt")
LEAD_INDEX = "412"

tier_reason = TIER_REASON_PATH.read_text(encoding="utf-8").strip()
row = {
    "index": LEAD_INDEX,
    "name": "NVIDIA Garak",
    "handle": "@NVIDIA",
    "email": "egalinkin@nvidia.com",
    "vertical": "ai_safety_red_teaming_llm",
    "tier": "1",
    "template": f"{LEAD_INDEX}_nvidia_garak.md",
    "tier_reason": tier_reason,
}

with CSV_PATH.open("a", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(row.keys()), quoting=csv.QUOTE_ALL)
    writer.writerow(row)
print(f"OK appended {LEAD_INDEX}")

# Parse-back verify
with CSV_PATH.open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print(f"total rows: {len(rows)}")
print(f"last row index: {rows[-1]['index']}")
print(f"last row name: {rows[-1]['name']}")
print(f"last row email: {rows[-1]['email']}")
print(f"tier_reason starts with: {rows[-1]['tier_reason'][:60]}")
print(f"tier_reason ends with: ...{rows[-1]['tier_reason'][-60:]}")
assert rows[-1]["index"] == LEAD_INDEX
assert rows[-1]["name"] == "NVIDIA Garak"
assert rows[-1]["email"] == "egalinkin@nvidia.com"
assert not rows[-1]["tier_reason"].startswith('"')
assert "egalinkin@nvidia.com" in rows[-1]["tier_reason"]
print("VERIFIED")
