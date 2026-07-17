"""Append Lead 440 Cresta to leads.csv (8-col schema)."""
import csv, sys
from pathlib import Path

CSV = Path("cold_email/leads.csv")
TIER_REASON_FILE = Path("/tmp/tier_reason_440_cresta.txt")  # already in Temp as C:/Users/Potts/AppData/Local/Temp/tier_reason_440_cresta.txt

# Will read from the actual Temp path the write_file tool used
TIER_REASON_FILE = Path("C:/Users/Potts/AppData/Local/Temp/tier_reason_440_cresta.txt")

tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").strip()

# Read existing rows + dedupe invariant
with CSV.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    header = reader.fieldnames

existing = [int(r["index"]) for r in rows if r["index"].isdigit()]
print(f"leads.csv: {len(rows)} rows, last index = {max(existing)}")

new_index = max(existing) + 1  # 440
print(f"new index = {new_index}")

assert new_index == 440, f"expected 440 got {new_index}"
assert str(new_index) not in existing, f"index {new_index} already exists"

new_row = {
    "index": str(new_index),
    "name": "Cresta",
    "handle": "@cresta",
    "email": "team@cresta.ai",
    "vertical": "voice_agents",
    "tier": "1",
    "template": "440_cresta.md",
    "tier_reason": tier_reason,
}

# Append with QUOTE_ALL
with CSV.open("a", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL)
    writer.writerow(new_row)

# Verify
with CSV.open("r", encoding="utf-8", newline="") as f:
    rows2 = list(csv.DictReader(f))

print(f"after append: {len(rows2)} rows")
last = rows2[-1]
print(f"last index = {last['index']}")
print(f"last name = {last['name']}")
print(f"last tier_reason starts: {last['tier_reason'][:80]}...")
print(f"last tier_reason starts with quote? {last['tier_reason'].startswith(chr(34))}")

# Dedupe invariant
from collections import Counter
dupes = [k for k, v in Counter(r["index"] for r in rows2).items() if v > 1]
print(f"dupes: {dupes}")
assert not dupes, f"DUPLICATES FOUND: {dupes}"
print("OK: leads.csv updated with index 440")
