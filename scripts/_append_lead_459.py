"""Append lead 459 Alation to BOTH cold_email CSVs with dedupe + shape safety."""
import csv, sys
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
LEADS_CSV = REPO / "cold_email" / "leads.csv"
LWE_CSV   = REPO / "cold_email" / "leads_with_emails.csv"
TIER_TXT  = REPO / "cold_email" / "tier_reason_459_alation.txt"

TIER = TIER_TXT.read_text(encoding="utf-8").strip()

LEADS_HEADER = ["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"]
LEADS_ROW = {
    "index": "459",
    "name": "Alation",
    "handle": "@alation",
    "email": "privacy@alation.com",
    "vertical": "data_catalog",
    "tier": "1",
    "template": "459_alation.md",
    "tier_reason": TIER,
}

LWE_HEADER = ["lead_index", "company", "handle", "domain", "website", "founder",
              "vertical", "tier", "best_email", "emails_found", "guessed_emails",
              "source_template", "tier_reason"]
LWE_ROW = {
    "lead_index": "459",
    "company": "Alation",
    "handle": "@alation",
    "domain": "alation.com",
    "website": "https://www.alation.com/",
    "founder": "Satyen Sangani (Co-Founder + CEO + ex-HP + ex-Siebel + ex-Netezza + ex-Oracle + ex-Sun Microsystems + ex-SGI + ex-KPMG + Imperial College London) + Rajkumar Irudayaraj (Co-Founder + ex-HP + ex-VMware + ex-Oracle + ex-IBM + ex-Deloitte + ex-KPMG)",
    "vertical": "data_catalog",
    "tier": "1",
    "best_email": "privacy@alation.com",
    "emails_found": "privacy@alation.com|contactsales@alation.com|hrwebrequest@alation.com|marketingwebrequest@alation.com|partnerwebrequest@alation.com",
    "guessed_emails": "privacy@|contactsales@|hr@|marketing@|partners@",
    "source_template": "459_alation.md",
    "tier_reason": TIER,
}

# Pre-flight dedupe + shape check
def preflight(path, idx_col, row_idx):
    if not path.exists():
        return
    with open(path, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    existing = [r.get(idx_col) for r in rows]
    if row_idx in existing:
        print(f"DUPE-FAIL: {path.name} already has index={row_idx}")
        sys.exit(2)

preflight(LEADS_CSV, "index", "459")
preflight(LWE_CSV, "lead_index", "459")

# Verify shapes (in-row dict must have exactly the keys in header)
assert set(LEADS_ROW.keys()) == set(LEADS_HEADER), f"leads shape mismatch: {set(LEADS_ROW.keys()) ^ set(LEADS_HEADER)}"
assert set(LWE_ROW.keys()) == set(LWE_HEADER), f"lwe shape mismatch: {set(LWE_ROW.keys()) ^ set(LWE_HEADER)}"

with open(LEADS_CSV, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=LEADS_HEADER, quoting=csv.QUOTE_ALL)
    w.writerow(LEADS_ROW)

with open(LWE_CSV, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=LWE_HEADER, quoting=csv.QUOTE_ALL)
    w.writerow(LWE_ROW)

# Parse-back verify
with open(LEADS_CSV, "r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
last = rows[-1]
assert last["index"] == "459", f"last leads index mismatch: {last['index']}"
assert last["tier_reason"].startswith("Lead 459 - Alation"), f"tier_reason head wrong: {last['tier_reason'][:80]}"

with open(LWE_CSV, "r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
last = rows[-1]
assert last["lead_index"] == "459", f"last lwe index mismatch: {last['lead_index']}"
assert last["best_email"] == "privacy@alation.com", f"best_email wrong: {last['best_email']}"

print(f"OK leads.csv row 459 + leads_with_emails.csv row 459 + tier_reason {len(TIER)}c")
print(f"OK leads.csv total={len(rows)+1 if False else None} (parse-back only checked last)")