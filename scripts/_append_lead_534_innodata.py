"""Append lead 534 (Innodata) to leads.csv (8-col) and leads_with_emails.csv (13-col).

Two-schema CSV append pattern verified across atlas-store ticks 49-2026-07-17.
"""
import csv
import sys
from pathlib import Path

ROOT = Path(r"C:\Users\Potts\projects\atlas-store")
LEADS = ROOT / "cold_email" / "leads.csv"
LWE   = ROOT / "cold_email" / "leads_with_emails.csv"
TIER_FILE = ROOT / "cold_email" / "tier_reason_534_innodata.txt"

LEAD_INDEX = "534"
COMPANY    = "Innodata"
HANDLE     = "@innodata"
EMAIL      = "info@innodata.com"
VERTICAL   = "ai_data_labeling"
TIER       = "1"
TEMPLATE   = "534_innodata.md"

DOMAIN   = "innodata.com"
WEBSITE  = "https://www.innodata.com/"
FOUNDER  = "Jack S. Abuhoff (Founder + Chairman + CEO, founded Innodata 2003; per first-party SEC 10-K + NASDAQ executive profile + SEC EDGAR DEF 14A)"
BEST_EMAIL = "info@innodata.com"
EMAILS_FOUND = "info@innodata.com"
GUESSED    = "info@|sales@|partnerships@|investor@|jack@|abuhoff@|press@|hr@|legal@|privacy@|dpo@|security@|compliance@"

TIER_REASON = TIER_FILE.read_text(encoding="utf-8").strip()

def preflight():
    for path, col in ((LEADS, "index"), (LWE, "lead_index")):
        if not path.exists():
            print(f"SKIP preflight (file missing): {path.name}")
            continue
        with open(path, "r", encoding="utf-8", newline="") as f:
            r = csv.DictReader(f)
            for row in r:
                if row.get(col) == LEAD_INDEX:
                    print(f"DUPE-FAIL: {path.name} already has {col}={LEAD_INDEX}")
                    sys.exit(2)
    print(f"preflight OK (no {LEAD_INDEX} in either CSV)")

def append_leads():
    new_row = [LEAD_INDEX, COMPANY, HANDLE, EMAIL, VERTICAL, TIER, TEMPLATE, TIER_REASON]
    with open(LEADS, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(new_row)
    with open(LEADS, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    assert rows[-1]["index"] == LEAD_INDEX, f"FAIL leads.csv last index = {rows[-1]['index']!r}"
    print(f"OK leads.csv row appended (last index = {rows[-1]['index']}, total = {len(rows)})")

def append_lwe():
    new_row = [LEAD_INDEX, COMPANY, HANDLE, DOMAIN, WEBSITE, FOUNDER,
               VERTICAL, TIER, BEST_EMAIL, EMAILS_FOUND, GUESSED, TEMPLATE, TIER_REASON]
    with open(LWE, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(new_row)
    with open(LWE, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    assert rows[-1]["lead_index"] == LEAD_INDEX, f"FAIL lwe last lead_index = {rows[-1]['lead_index']!r}"
    from collections import Counter
    c = Counter(r["lead_index"] for r in rows)
    dups = {k: v for k, v in c.items() if v > 1}
    assert not dups, f"DUPE in leads_with_emails.csv: {dups}"
    print(f"OK leads_with_emails.csv row appended (last = {rows[-1]['lead_index']}, total = {len(rows)})")

if __name__ == "__main__":
    preflight()
    append_leads()
    append_lwe()
    print("DONE — Innodata 534 appended to both CSVs")
