#!/usr/bin/env python3
"""Append Portkey AI (lead 160) to leads.csv. Reads tier_reason from temp file."""
import csv
import os

leads_path = r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv"
tierreason_path = r"C:\Users\Potts\AppData\Local\Temp\atlas-tick59-portkey-tierreason.txt"

with open(tierreason_path, "r", encoding="utf-8") as f:
    tier_reason = f.read().strip()

# Strip outer quotes if present
if tier_reason.startswith('"') and tier_reason.endswith('"'):
    tier_reason = tier_reason[1:-1]

row = {
    "index": "160",
    "name": "Portkey AI",
    "handle": "@PortkeyAI",
    "email": "support@portkey.ai",
    "vertical": "ai_agents_infra",
    "tier": "1",
    "template": "240_portkey.md",
    "tier_reason": tier_reason,
}

# Verify index 160 doesn't already exist
with open(leads_path, "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
existing_indices = [r[0].strip('"') for r in rows[1:] if r]
assert "160" not in existing_indices, f"Index 160 already exists: {existing_indices[-5:]}"

with open(leads_path, "a", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=header,
        quoting=csv.QUOTE_MINIMAL,
        quotechar='"',
        doublequote=True,
    )
    writer.writerow(row)

print(f"Appended row 160: Portkey AI -> {leads_path}")
print(f"tier_reason length: {len(tier_reason)} chars")

# Parse-back verification
with open(leads_path, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    last = list(reader)[-1]
    assert last["name"] == "Portkey AI", f"Parse-back fail: name={last['name']}"
    assert last["email"] == "support@portkey.ai"
    assert last["template"] == "240_portkey.md"
    assert last["vertical"] == "ai_agents_infra"
    assert len(last["tier_reason"]) == len(tier_reason), f"tier_reason length mismatch: {len(last['tier_reason'])} vs {len(tier_reason)}"
    print(f"Parse-back PASS: index={last['index']} name={last['name']} template={last['template']}")
    print(f"Total rows now: {len(list(csv.DictReader(open(leads_path, encoding='utf-8'))))}")