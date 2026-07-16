"""Append Lead 365 Salesloft to BOTH leads.csv (8-col) and leads_with_emails.csv (13-col).

SCHEMA — KEEP THEM IN SYNC WITH PRIOR TICKS:

leads.csv (8 cols): index, name, handle, email, vertical, tier, template, tier_reason
leads_with_emails.csv (13 cols): lead_index, company, handle, domain, website,
  founder, vertical, tier, best_email, emails_found, guessed_emails,
  source_template, tier_reason
"""
import csv
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
TIER_REASON_FILE = Path("C:/Users/Potts/AppData/Local/Temp/tier_reason_365.txt")
tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").strip()

# ===== leads.csv (8 cols) =====
leads_csv = REPO / "cold_email" / "leads.csv"
with leads_csv.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(
        f,
        fieldnames=["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"],
        quoting=csv.QUOTE_ALL,
    )
    w.writerow({
        "index": "365",
        "name": "Salesloft",
        "handle": "@salesloft",
        "email": "privacy@salesloft.com",
        "vertical": "ai_revenue_intelligence",
        "tier": "1",
        "template": "365_salesloft.md",
        "tier_reason": tier_reason,
    })

# Verify parse-back
with leads_csv.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
print(f"leads.csv: {len(rows)} rows; last index = {rows[-1]['index']}")
print(f"leads.csv last tier_reason starts with: {rows[-1]['tier_reason'][:80]!r}")
print(f"leads.csv last email = {rows[-1]['email']!r}")
print(f"leads.csv last template = {rows[-1]['template']!r}")
assert rows[-1]["index"] == "365", "wrong index"
assert rows[-1]["email"] == "privacy@salesloft.com", "wrong email"
assert rows[-1]["tier_reason"] == tier_reason, "tier_reason corruption"
print("leads.csv OK")

# ===== leads_with_emails.csv (13 cols) =====
emails_csv = REPO / "cold_email" / "leads_with_emails.csv"
with emails_csv.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "lead_index", "company", "handle", "domain", "website", "founder",
            "vertical", "tier", "best_email", "emails_found", "guessed_emails",
            "source_template", "tier_reason",
        ],
        quoting=csv.QUOTE_ALL,
    )
    w.writerow({
        "lead_index": "365",
        "company": "Salesloft",
        "handle": "@salesloft",
        "domain": "salesloft.com",
        "website": "https://www.salesloft.com/",
        "founder": "David Obrand (CEO, formerly founder of Contrast Security + 20-years-B2B-SaaS-sales-veteran + founding father of the SaaS sales-engagement category)",
        "vertical": "ai_revenue_intelligence",
        "tier": "1",
        "best_email": "privacy@salesloft.com",
        "emails_found": "privacy@salesloft.com",
        "guessed_emails": "security@salesloft.com, legal@salesloft.com, dpo@salesloft.com",
        "source_template": "365_salesloft.md",
        "tier_reason": tier_reason,
    })

# Verify parse-back
with emails_csv.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
print(f"leads_with_emails.csv: {len(rows)} rows; last lead_index = {rows[-1]['lead_index']}")
print(f"leads_with_emails.csv last best_email = {rows[-1]['best_email']!r}")
print(f"leads_with_emails.csv last founder starts with: {rows[-1]['founder'][:80]!r}")
assert rows[-1]["lead_index"] == "365", "wrong lead_index"
assert rows[-1]["best_email"] == "privacy@salesloft.com", "wrong best_email"
assert rows[-1]["tier_reason"] == tier_reason, "tier_reason corruption"
print("leads_with_emails.csv OK")

# Dedupe invariant check across BOTH files
from collections import Counter
def dedupe_check(path, idx):
    with path.open(encoding="utf-8", newline="") as f:
        rs = list(csv.DictReader(f))
    c = Counter(r.get(idx) for r in rs)
    dupes = {k: v for k, v in c.items() if v > 1}
    assert not dupes, f"{path.name} has duplicate {idx}: {dupes}"
    print(f"{path.name}: zero duplicate {idx} ✓")

dedupe_check(leads_csv, "index")
dedupe_check(emails_csv, "lead_index")
print("DEDUPE INVARIANT OK across both files")
