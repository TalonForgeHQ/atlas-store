#!/usr/bin/env python
"""Append lead 166 (Humanloop) to cold_email/leads.csv using csv.DictWriter.
Reads the long tier_reason text from a separate .txt file to avoid shell heredoc traps.
"""
import csv
import os
import sys

CSV_PATH = r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv"
TIER_REASON_PATH = r"C:\Users\Potts\AppData\Local\Temp\humanloop_lead_166.txt"

# Read tier reason text
with open(TIER_REASON_PATH, "r", encoding="utf-8") as f:
    tier_reason = f.read().strip()

# Verify the file doesn't already contain lead 166
with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    if any(r.get("index") == "166" for r in rows):
        print("ALREADY_PRESENT: lead 166 already exists in CSV. Aborting.")
        sys.exit(0)
    max_index = max((int(r["index"]) for r in rows if r["index"].isdigit()), default=0)
    print(f"PRE_APPEND: {len(rows)} rows, max index = {max_index}")

# Append row
with open(CSV_PATH, "a", encoding="utf-8", newline="") as f:
    fieldnames = ["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"]
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
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

# Verify the append
with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    new_max = max((int(r["index"]) for r in rows if r["index"].isdigit()), default=0)
    lead_166 = next((r for r in rows if r["index"] == "166"), None)
    print(f"POST_APPEND: {len(rows)} rows, max index = {new_max}")
    if lead_166:
        print(f"LEAD_166_VERIFIED: name={lead_166['name']} | email={lead_166['email']} | vertical={lead_166['vertical']} | template={lead_166['template']}")
        print(f"TIER_REASON_LEN: {len(lead_166['tier_reason'])} chars")
    else:
        print("FAILED: lead 166 not found after append")
        sys.exit(1)