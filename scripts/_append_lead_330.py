#!/usr/bin/env python3
"""Append lead 330 (Cognigy) to leads.csv with QUOTE_ALL to preserve the long tier_reason.
Uses the two-tier pattern: tier_reason content is in _ticks/tick_cognigy_330.csv (already
written by write_file), this script reads it, reconstructs the 8-field dict, and appends
with csv.DictWriter + QUOTE_ALL.
"""
import csv
import sys
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
LEADS = REPO / "cold_email" / "leads.csv"
TICK_CONTENT = REPO / "_ticks" / "tick_cognigy_330.csv"

# Read the full line from the tick file
line = TICK_CONTENT.read_text(encoding="utf-8").strip()
parts = next(csv.reader([line]))

assert len(parts) == 8, f"expected 8 fields, got {len(parts)}: {parts}"
assert parts[0] == "330", f"expected index 330, got {parts[0]}"

row = {
    "index": parts[0],
    "name": parts[1],
    "handle": parts[2],
    "email": parts[3],
    "vertical": parts[4],
    "tier": parts[5],
    "template": parts[6],
    "tier_reason": parts[7],
}

# Read existing leads to find header + check for dupes
with LEADS.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    header = reader.fieldnames
    existing_idxs = [r["index"] for r in reader if r.get("index")]

assert "330" not in existing_idxs, "duplicate index 330 in leads.csv"

# Verify header matches our dict keys
assert list(row.keys()) == header, f"dict keys {list(row.keys())} != header {header}"

# Append
with LEADS.open("a", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL)
    writer.writerow(row)

# Parse-back verify
with LEADS.open("r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
last = rows[-1]
assert last["index"] == "330", f"last row index is {last['index']}, expected 330"
assert last["name"] == "Cognigy", f"last row name is {last['name']}, expected Cognigy"
assert last["tier_reason"].startswith("Canonical ai_customer_support_agents 3rd-sibling"), \
    f"tier_reason did not survive: starts with {last['tier_reason'][:100]}"
assert "Cognigy" in last["tier_reason"], "tier_reason missing Cognigy"
assert "info@cognigy.com" in last["tier_reason"], "tier_reason missing email"
assert last["tier_reason"].endswith("production scale.\""), \
    f"tier_reason ending suspicious: ...{last['tier_reason'][-100:]}"

# Dedupe invariant
from collections import Counter
dupes = [k for k, v in Counter(r["index"] for r in rows).items() if v > 1]
assert not dupes, f"duplicate indices: {dupes}"

print(f"OK: appended lead 330 (Cognigy). Total rows: {len(rows)}. Last row parse-back clean.")
print(f"OK: tier_reason length: {len(last['tier_reason'])} chars")