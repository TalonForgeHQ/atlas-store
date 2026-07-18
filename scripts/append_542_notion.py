#!/usr/bin/env python3
"""Append lead 542 (Notion) to leads.csv + leads_with_emails.csv (idempotency-guarded)."""
import csv
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
TIER_REASON = (Path(r"C:\Users\Potts\AppData\Local\Temp\tier_reason_542.txt")).read_text(encoding="utf-8").strip()

INDEX = "542"
NAME = "Notion"
HANDLE = "@notion"
EMAIL = "security@makenotion.com"
VERTICAL = "workspace_ai_ops"
TIER = "1"
TEMPLATE = "542_notion.md"

# 13-col leads_with_emails.csv schema
LEAD_INDEX = "542"
COMPANY = "Notion"
DOMAIN = "makenotion.com"
WEBSITE = "https://www.notion.com"
FOUNDER = "Ivan Zhao (Co-Founder + CEO) + Akshay Kothari (Co-Founder + COO)"
BEST_EMAIL = "security@makenotion.com"
SOURCE_TEMPLATE = "542_notion.md"

leads_path = REPO / "cold_email" / "leads.csv"
lwe_path = REPO / "cold_email" / "leads_with_emails.csv"

# Read existing rows
with leads_path.open("r", newline="", encoding="utf-8") as f:
    existing_rows = list(csv.reader(f))
    header = existing_rows[0]
    data_rows = existing_rows[1:]

# Idempotency: row-prefix anchor
row_prefix = f'"{INDEX}","'
csv_text = leads_path.read_text(encoding="utf-8")
assert row_prefix not in csv_text, f"lead {INDEX} already in leads.csv"

# Append 8-col row
new_row = [INDEX, NAME, HANDLE, EMAIL, VERTICAL, TIER, TEMPLATE, TIER_REASON]
assert len(new_row) == 8, f"row has {len(new_row)} fields, need 8"

with leads_path.open("a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(new_row)

# Verify parse-back
with leads_path.open("r", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
assert any(r["index"] == INDEX for r in rows), f"parse-back failed for {INDEX}"
print(f"leads.csv: appended row {INDEX} ({len(rows)} total)")

# Append 13-col row to leads_with_emails.csv
with lwe_path.open("r", newline="", encoding="utf-8") as f:
    lwe_text = f.read()
lwe_prefix = f'"{LEAD_INDEX}","'
assert lwe_prefix not in lwe_text, f"lead {LEAD_INDEX} already in leads_with_emails.csv"

# Read template for tier_reason in 13-col row
new_lwe_row = [
    LEAD_INDEX, COMPANY, HANDLE, DOMAIN, WEBSITE, FOUNDER, VERTICAL, TIER,
    BEST_EMAIL, "1", "security@makenotion.com", SOURCE_TEMPLATE, TIER_REASON,
]
assert len(new_lwe_row) == 13, f"row has {len(new_lwe_row)} fields, need 13"

with lwe_path.open("a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(new_lwe_row)

# Verify parse-back
with lwe_path.open("r", newline="", encoding="utf-8") as f:
    lwe_rows = list(csv.DictReader(f))
assert any(r["lead_index"] == LEAD_INDEX for r in lwe_rows), f"parse-back failed for {LEAD_INDEX} in lwe"
print(f"leads_with_emails.csv: appended row {LEAD_INDEX} ({len(lwe_rows)} total)")
