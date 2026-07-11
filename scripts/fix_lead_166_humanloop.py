#!/usr/bin/env python
"""Fix the broken lead 166 in CSV by:
1. Reading the CSV (rows up to lead 165)
2. Removing the malformed lead 166 row
3. Re-appending a clean lead 166 with correct tier_reason
"""
import csv
import os
import sys

CSV_PATH = r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv"
TIER_REASON_PATH = r"C:\Users\Potts\AppData\Local\Temp\humanloop_tier_reason_166.txt"
BACKUP_PATH = CSV_PATH + ".bak"

# 1. Backup the current CSV
import shutil
shutil.copy2(CSV_PATH, BACKUP_PATH)
print(f"BACKUP: {BACKUP_PATH}")

# 2. Read existing rows, filter out malformed lead 166
with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

pre_count = len(rows)
rows = [r for r in rows if r.get("index") != "166"]
post_count = len(rows)
print(f"FILTER: removed {pre_count - post_count} malformed row(s). Now {post_count} rows.")

# 3. Read clean tier_reason
with open(TIER_REASON_PATH, "r", encoding="utf-8") as f:
    tier_reason = f.read().strip()
print(f"TIER_REASON_LEN: {len(tier_reason)} chars")
print(f"TIER_REASON_START: {tier_reason[:80]}")
print(f"TIER_REASON_END: {tier_reason[-80:]}")

# 4. Re-write CSV (header + clean rows) — strip extra fields per row
with open(CSV_PATH, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for row in rows:
        clean_row = {k: (row.get(k) or "") for k in fieldnames}
        writer.writerow(clean_row)
    # Append clean lead 166
    writer.writerow({
        "index": "166",
        "name": "Humanloop",
        "handle": "@humanloop",
        "email": "privacy@humanloop.com",
        "vertical": "ai_agents_infra",
        "tier": "1",
        "template": "246_humanloop.md",
        "tier_reason": tier_reason,
    })

# 5. Verify
with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    lead_166 = next((r for r in rows if r["index"] == "166"), None)
    print(f"FINAL: {len(rows)} rows")
    print(f"LEAD_166_NAME: {lead_166['name']}")
    print(f"LEAD_166_EMAIL: {lead_166['email']}")
    print(f"LEAD_166_VERTICAL: {lead_166['vertical']}")
    print(f"LEAD_166_TEMPLATE: {lead_166['template']}")
    print(f"LEAD_166_TIER_REASON_LEN: {len(lead_166['tier_reason'])} chars")
    # Sanity: tier_reason should NOT contain '","' which is the CSV-quoted-row signature
    if '","' in lead_166['tier_reason']:
        print("ERROR: tier_reason still contains quoted-row pattern '\"'\"'! Aborting commit.")
        sys.exit(1)
    print("TIER_REASON_OK: no quoted-row contamination")
    # Show first 200 chars
    print(f"TIER_REASON_START: {lead_166['tier_reason'][:200]}")