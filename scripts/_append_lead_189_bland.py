"""Append Bland AI (lead 189) to cold_email/leads.csv with QUOTE_ALL.

Two-tier pattern: long tier_reason lives in a temp .txt file; this small
script reads it + writes the CSV row with csv.DictWriter(quoting=QUOTE_ALL).
"""
import csv
import os
import sys
from pathlib import Path

CSV_PATH = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv")
TIER_REASON_PATH = Path(r"C:\Users\Potts\AppData\Local\Temp\tier_reason_bland_189.txt")

# Sanity check: no duplicate index
NEW_INDEX = "189"
with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)
    if any(r["index"] == NEW_INDEX for r in rows):
        print(f"FAIL: index {NEW_INDEX} already exists in leads.csv. Aborting.")
        sys.exit(1)

# Read tier_reason
tier_reason = TIER_REASON_PATH.read_text(encoding="utf-8").strip()

new_row = {
    "index": NEW_INDEX,
    "name": "Bland AI",
    "handle": "@usebland",
    "email": "hello@bland.ai",
    "vertical": "ai_voice_agents",
    "tier": "1",
    "template": "277_bland.md",
    "tier_reason": tier_reason,
}

with CSV_PATH.open("a", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writerow(new_row)

# Verify by re-reading
with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
    rows_after = list(csv.DictReader(f))
last = rows_after[-1]
print(f"OK: appended index={last['index']} name={last['name']} email={last['email']} template={last['template']}")
print(f"OK: leads.csv now has {len(rows_after)} rows total")
print(f"OK: tier_reason length = {len(last['tier_reason'])} chars")
