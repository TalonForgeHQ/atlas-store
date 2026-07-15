"""Append Cyera (index 238) to leads.csv and leads_with_emails.csv.
Two-schema CSV append. Atomic via tempfile + os.replace.
"""
import csv
import os
import tempfile
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
LEADS_CSV = REPO / "cold_email" / "leads.csv"
LEADS_WITH_EMAILS = REPO / "cold_email" / "leads_with_emails.csv"
TIER_REASON_FILE = Path(r"C:\Users\Potts\AppData\Local\Temp\tier_reason_238_cyera.txt")

INDEX = "238"
NAME = "Cyera"
HANDLE = "@cyera"
EMAIL = "privacy@cyera.io"
VERTICAL = "ai_data_security"
TIER = "1"
TEMPLATE = "328_cyera.md"

tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").strip()

leads_row = {
    "index": INDEX,
    "name": NAME,
    "handle": HANDLE,
    "email": EMAIL,
    "vertical": VERTICAL,
    "tier": TIER,
    "template": TEMPLATE,
    "tier_reason": tier_reason,
}

lwe_row = {
    "lead_index": INDEX,
    "company": NAME,
    "handle": HANDLE,
    "domain": "cyera.io",
    "website": "https://www.cyera.io",
    "founder": "Yael Valier (Co-Founder + CEO, ex-Salesforce cybersecurity + ex-Microsoft CSG + ex-IronSource + IDF Unit 8200) + Amit Toren (Co-Founder + CTO, ex-Salesforce + ex-Microsoft + ex-Cisco + ex-Check Point + IDF veteran)",
    "vertical": VERTICAL,
    "tier": TIER,
    "best_email": EMAIL,
    "emails_found": "privacy@cyera.io",
    "guessed_emails": "privacy@cyera.io",
    "source_template": TEMPLATE,
    "tier_reason": tier_reason,
}


def append_csv_dedupe(path, fieldnames, row, key_field):
    """Atomic append: dedupe by key_field, then write back + append new row."""
    tmp = tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", newline="", delete=False, dir=str(path.parent)
    )
    tmp_path = tmp.name
    tmp.close()
    try:
        existing = []
        with open(path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            header = reader.fieldnames
            assert header == fieldnames, f"header mismatch: {header} != {fieldnames}"
            for r in reader:
                if r.get(key_field) and r[key_field] != row[key_field]:
                    existing.append(r)
        existing.append(row)
        with open(tmp_path, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            w.writeheader()
            for r in existing:
                w.writerow(r)
        os.replace(tmp_path, path)
    except Exception:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        raise


# Append to leads.csv (8 cols)
leads_fields = ["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"]
append_csv_dedupe(LEADS_CSV, leads_fields, leads_row, "index")

# Append to leads_with_emails.csv (13 cols)
lwe_fields = [
    "lead_index", "company", "handle", "domain", "website", "founder", "vertical",
    "tier", "best_email", "emails_found", "guessed_emails", "source_template", "tier_reason",
]
append_csv_dedupe(LEADS_WITH_EMAILS, lwe_fields, lwe_row, "lead_index")

# Verify
import collections
with open(LEADS_CSV, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
leads_idx = collections.Counter(r["index"] for r in rows)
assert leads_idx[INDEX] == 1, f"leads.csv: index {INDEX} dupes={leads_idx[INDEX]}"
assert not rows[-1]["tier_reason"].startswith('"'), "tier_reason double-wrap"

with open(LEADS_WITH_EMAILS, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows2 = list(reader)
lwe_idx = collections.Counter(r["lead_index"] for r in rows2)
assert lwe_idx[INDEX] == 1, f"leads_with_emails: lead_index {INDEX} dupes={lwe_idx[INDEX]}"

print(f"OK leads.csv row for index {INDEX} ({NAME}) | total rows: {len(rows)}")
print(f"OK leads_with_emails.csv row for lead_index {INDEX} | total rows: {len(rows2)}")
print(f"OK tier_reason length: {len(tier_reason)} chars")
