"""
Tick 73 helper — append Apollo.io (174) to leads.csv
Two-tier pattern: long tier_reason is in tier_reason_174_apollo.txt,
this small script reads it and writes the CSV row with QUOTE_ALL.
"""
import csv, os, sys

CSV_PATH = r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv"
TIER_PATH = r"C:\Users\Potts\AppData\Local\Temp\tier_reason_174_apollo.txt"

INDEX = 174
NAME = "Apollo.io"
HANDLE = "@apollodemand"
EMAIL = "privacy@apollo.io"
VERTICAL = "ai_sales_ai"
TIER = "1"
TEMPLATE = "254_apollo.md"

with open(TIER_PATH, "r", encoding="utf-8") as f:
    tier_reason = f.read().strip()

# Parse-back verification
assert "privacy@apollo.io" in tier_reason, "tier_reason missing email"
assert "Tim Zheng" in tier_reason, "tier_reason missing founder name"
assert "8th ai_sales_ai" in tier_reason, "tier_reason missing sibling position"
assert "Apollo Data" in tier_reason and "Apollo Engagement" in tier_reason, "tier_reason missing product surfaces"
assert "EU AI Act Art. 53(d)" in tier_reason, "tier_reason missing EU AI Act Art. 53(d)"
assert "5 audit gaps" in tier_reason, "tier_reason missing audit gap count"
print(f"  tier_reason verified: {len(tier_reason)} chars, {tier_reason.count(chr(10))+1} lines")

# Sanity: confirm 173 is the last existing row before appending 174
with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))
header = rows[0]
last_row = rows[-1]
print(f"  header: {header}")
print(f"  last existing row index: {last_row[0]}")
assert last_row[0] == "173", f"Expected 173 as last row, got {last_row[0]} — refusing to append to avoid duplicate index"

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

with open(CSV_PATH, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL)
    w.writerow(row)

# Parse-back: re-read, count rows, verify 174 present
with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
print(f"  rows after append: {len(rows)}")
apollo = [r for r in rows if r["name"] == "Apollo.io"]
assert len(apollo) == 1, f"Expected 1 Apollo.io row, got {len(apollo)}"
assert apollo[0]["index"] == "174", f"Expected index 174, got {apollo[0]['index']}"
assert apollo[0]["email"] == "privacy@apollo.io"
assert apollo[0]["template"] == "254_apollo.md"
assert len(apollo[0]["tier_reason"]) > 5000, f"tier_reason truncated: {len(apollo[0]['tier_reason'])} chars"
print(f"  PASS: row 174 Apollo.io written, tier_reason={len(apollo[0]['tier_reason'])} chars")
