#!/usr/bin/env python3
"""Append Veryfi lead 335 to BOTH leads.csv (8-col) and leads_with_emails.csv (13-col)."""
import csv
import os
import sys
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
TIER_TXT = Path(os.environ["TEMP"]) / "tier_reason_335_veryfi.txt"
tier_reason = TIER_TXT.read_text(encoding="utf-8").strip()

INDEX = "335"
NAME = "Veryfi"
HANDLE = "@VeryfiOfficial"
EMAIL = "privacy@veryfi.com"
VERTICAL = "ai_document_processing_idp"
TIER = "1"
TEMPLATE = "335_veryfi.md"
FOUNDER = "Dmitry Svetlov (CEO, ex-Moscow State Technical Univ) + Ernest Semida (COO)"

# leads.csv (8 columns)
leads_csv = REPO / "cold_email" / "leads.csv"
with leads_csv.open("r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
existing_idxs = {r["index"] for r in rows}
assert INDEX not in existing_idxs, f"lead {INDEX} already in leads.csv"
existing_idxs.add(INDEX)

with leads_csv.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(
        f,
        fieldnames=["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"],
        quoting=csv.QUOTE_ALL,
    )
    w.writerow({
        "index": INDEX,
        "name": NAME,
        "handle": HANDLE,
        "email": EMAIL,
        "vertical": VERTICAL,
        "tier": TIER,
        "template": TEMPLATE,
        "tier_reason": tier_reason,
    })

# leads_with_emails.csv (13 columns)
leads_email_csv = REPO / "cold_email" / "leads_with_emails.csv"
with leads_email_csv.open("r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
existing_idxs2 = {r["lead_index"] for r in rows}
assert INDEX not in existing_idxs2, f"lead {INDEX} already in leads_with_emails.csv"

with leads_email_csv.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "lead_index", "company", "handle", "domain", "website", "founder", "vertical",
            "tier", "best_email", "emails_found", "guessed_emails", "source_template", "tier_reason",
        ],
        quoting=csv.QUOTE_ALL,
    )
    w.writerow({
        "lead_index": INDEX,
        "company": NAME,
        "handle": HANDLE,
        "domain": "veryfi.com",
        "website": "https://www.veryfi.com",
        "founder": FOUNDER,
        "vertical": VERTICAL,
        "tier": TIER,
        "best_email": EMAIL,
        "emails_found": "privacy@veryfi.com;cso@veryfi.com;support@veryfi.com;hello@veryfi.com",
        "guessed_emails": "cfo@veryfi.com;legal@veryfi.com;security@veryfi.com;dpo@veryfi.com",
        "source_template": TEMPLATE,
        "tier_reason": tier_reason,
    })

# Verify both files
print(f"--- leads.csv last 2 rows ---")
with leads_csv.open("r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
for r in rows[-2:]:
    print(f"  index={r['index']} name={r['name']} vertical={r['vertical']}")
print(f"  total rows: {len(rows)}")
assert rows[-1]["index"] == INDEX
assert rows[-1]["tier_reason"].startswith("Canonical ") and not rows[-1]["tier_reason"].startswith('"')

print(f"--- leads_with_emails.csv last 2 rows ---")
with leads_email_csv.open("r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
for r in rows[-2:]:
    print(f"  lead_index={r['lead_index']} company={r['company']} best_email={r['best_email']}")
print(f"  total rows: {len(rows)}")
assert rows[-1]["lead_index"] == INDEX

# Dedup invariant
from collections import Counter
with leads_csv.open("r", encoding="utf-8", newline="") as f:
    idxs = [r["index"] for r in csv.DictReader(f)]
c1 = Counter(idxs)
dupes1 = [k for k, v in c1.items() if v > 1]
print(f"leads.csv dupes: {dupes1}")
assert not dupes1, f"leads.csv has duplicate indices: {dupes1}"

with leads_email_csv.open("r", encoding="utf-8", newline="") as f:
    idxs2 = [r["lead_index"] for r in csv.DictReader(f)]
c2 = Counter(idxs2)
dupes2 = [k for k, v in c2.items() if v > 1]
print(f"leads_with_emails.csv dupes: {dupes2}")
assert not dupes2, f"leads_with_emails.csv has duplicate indices: {dupes2}"

print(f"\nOK: lead {INDEX} ({NAME}) appended to both CSVs, no dupes, tier_reason shape verified.")