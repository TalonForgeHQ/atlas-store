#!/usr/bin/env python
"""Append Tenstorrent as lead index 235 to leads.csv (8-col schema).
Idempotent: re-checks for existing index 235 before appending.
"""
import csv
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
LEADS_CSV = REPO / "cold_email" / "leads.csv"
TIER_REASON_FILE = Path("C:/Users/Potts/AppData/Local/Temp/tier_reason_235_tenstorrent.txt")

INDEX = "235"
NAME = "Tenstorrent"
HANDLE = "@TenstorrentInc"
EMAIL = "privacy@tenstorrent.com"
VERTICAL = "ai_infra"
TIER = "1"
TEMPLATE = "325_tenstorrent.md"

# Pre-flight dedupe check (per-tenant column for THIS csv's schema)
with LEADS_CSV.open("r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

existing_idxs = {r.get("index") for r in rows}
assert INDEX not in existing_idxs, f"index {INDEX} already in leads.csv ({sum(1 for r in rows if r.get('index')==INDEX)} occurrences)"

# Read tier_reason as a single field value (NOT a CSV row)
tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").rstrip("\n")
assert not tier_reason.startswith('"'), f"tier_reason file is corrupt (starts with quote)"

# Append the row
with LEADS_CSV.open("a", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"],
        quoting=csv.QUOTE_ALL,
    )
    writer.writerow({
        "index": INDEX,
        "name": NAME,
        "handle": HANDLE,
        "email": EMAIL,
        "vertical": VERTICAL,
        "tier": TIER,
        "template": TEMPLATE,
        "tier_reason": tier_reason,
    })

# Parse-back verification
with LEADS_CSV.open("r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

last = rows[-1]
assert last["index"] == INDEX, f"last row index is {last['index']}, expected {INDEX}"
assert last["name"] == NAME
assert last["email"] == EMAIL
assert not last["tier_reason"].startswith('"'), "tier_reason was double-quoted (corrupt)"
print(f"OK leads.csv row {INDEX} ({NAME}) appended. total rows: {len(rows)}")
print(f"tier_reason length: {len(last['tier_reason'])} chars")
print(f"last 80 chars: ...{last['tier_reason'][-80:]}")