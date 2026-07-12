"""Recover from the bad lead-189 append and re-append correctly.

The previous append wrapped the tier_reason (which contained comma-separated
quoted-CSV-looking text) inside csv.QUOTE_ALL, producing broken output. Fix:
drop the broken last row, then re-append with the correct tier_reason (raw
description text, not a full row).
"""
import csv
import sys
from pathlib import Path

CSV_PATH = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv")
TIER_REASON_PATH = Path(r"C:\Users\Potts\AppData\Local\Temp\tier_reason_bland_189.txt")

with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

last = rows[-1]
if last["index"] != "189":
    print("FAIL: last row index is " + str(last["index"]) + ", not 189. Aborting.")
    sys.exit(1)

rows = rows[:-1]
print("OK: dropped broken last row (index=189, name=" + str(last["name"]) + ")")

tier_reason = TIER_REASON_PATH.read_text(encoding="utf-8").strip()

new_row = {
    "index": "189",
    "name": "Bland AI",
    "handle": "@usebland",
    "email": "hello@bland.ai",
    "vertical": "ai_voice_agents",
    "tier": "1",
    "template": "277_bland.md",
    "tier_reason": tier_reason,
}

with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for r in rows:
        writer.writerow(r)
    writer.writerow(new_row)

with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
    rows_after = list(csv.DictReader(f))
last2 = rows_after[-1]
print("OK: re-appended index=" + str(last2["index"]) + " name=" + str(last2["name"]) + " email=" + str(last2["email"]) + " template=" + str(last2["template"]))
print("OK: leads.csv now has " + str(len(rows_after)) + " rows total")
print("OK: tier_reason length = " + str(len(last2["tier_reason"])) + " chars")
print("OK: tier_reason starts with: " + str(last2["tier_reason"][:80]))
