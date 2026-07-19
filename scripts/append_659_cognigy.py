#!/usr/bin/env python3
"""Append lead 659 (Cognigy) to BOTH leads.csv and leads_with_emails.csv."""
import csv
import sys
from pathlib import Path

ROOT = Path(r"C:\Users\Potts\projects\atlas-store")
TIER = (ROOT / "cold_email" / "tier_reason_659_cognigy.txt").read_text(encoding="utf-8").strip()
LEADS_CSV = ROOT / "cold_email" / "leads.csv"
LWE_CSV   = ROOT / "cold_email" / "leads_with_emails.csv"
TICK_ID   = "2026-07-20-fast-exec-cognigy-659"
TARGET_IDX = "659"

def preflight(path, idx_col, row_idx):
    if not path.exists():
        return
    with open(path, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if row_idx in [r.get(idx_col) for r in rows]:
        print(f"DUPE-FAIL: {path.name} already has {idx_col}={row_idx}")
        sys.exit(2)

preflight(LEADS_CSV, "index", TARGET_IDX)
preflight(LWE_CSV, "lead_index", TARGET_IDX)

# Append to leads.csv (8-col)
leads_row = {
    "index": "659",
    "name": "Cognigy",
    "handle": "@cognigy",
    "email": "info@cognigy.com",
    "vertical": "voice_ai",
    "tier": "1",
    "template": "659_cognigy.md",
    "tier_reason": "Lead 659 — " + TIER,
}
with open(LEADS_CSV, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(leads_row.keys()))
    w.writerow(leads_row)

# Append to leads_with_emails.csv (13-col)
lwe_row = {
    "lead_index": "659",
    "company": "Cognigy",
    "handle": "@cognigy",
    "domain": "cognigy.com",
    "website": "https://www.cognigy.com/",
    "founder": "Philipp Heltewig (Co-Founder); Sascha Poggemann (Co-Founder)",
    "vertical": "voice_ai",
    "tier": "1",
    "best_email": "info@cognigy.com",
    "emails_found": "info@cognigy.com; PR@cognigy.com; info-jp@cognigy.com; info-ko@cognigy.com; info-uk@cognigy.com; info-us@cognigy.com",
    "guessed_emails": "",
    "source_template": "659_cognigy.md",
    "tier_reason": "Lead 659 — " + TIER,
}
with open(LWE_CSV, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(lwe_row.keys()))
    w.writerow(lwe_row)

# Post-append verify
with open(LEADS_CSV, "r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
assert rows[-1]["index"] == TARGET_IDX, f"leads.csv tail wrong: {rows[-1]}"
assert rows[-1]["tier_reason"].startswith("Lead 659 — ")

with open(LWE_CSV, "r", encoding="utf-8", newline="") as f:
    lwe_rows = list(csv.DictReader(f))
assert lwe_rows[-1]["lead_index"] == TARGET_IDX
from collections import Counter
c = Counter(r["lead_index"] for r in lwe_rows)
assert all(v == 1 for v in c.values()), f"duplicates: {[(k,v) for k,v in c.items() if v>1]}"

print(f"OK: lead {TARGET_IDX} appended to both CSVs (leads.csv len={len(rows)}, leads_with_emails.csv len={len(lwe_rows)})")
print(f"OK: tier_reason starts: {TIER[:80]}...")
