"""Append lead 272 (Secureframe) to cold_email/leads.csv + leads_with_emails.csv."""
import csv, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEADS = ROOT / "cold_email" / "leads.csv"
LWE = ROOT / "cold_email" / "leads_with_emails.csv"
TIER = (ROOT / "cold_email" / "tier_reason_272_secureframe.txt").read_text(encoding="utf-8")

new_lead_leads_csv = {
    "index": "272",
    "name": "Secureframe",
    "handle": "@secureframe",
    "email": "privacy@secureframe.com",
    "vertical": "compliance_automation",
    "tier": "1",
    "template": "362_secureframe.md",
    "tier_reason": TIER.strip(),
}

new_lead_lwe = {
    "lead_index": "272",
    "company": "Secureframe",
    "handle": "@secureframe",
    "domain": "secureframe.com",
    "website": "https://www.secureframe.com",
    "founder": "Shrav Naraghi (Co-Founder & CEO)",
    "vertical": "compliance_automation",
    "tier": "1",
    "best_email": "privacy@secureframe.com",
    "emails_found": "1",
    "guessed_emails": "0",
    "source_template": "362_secureframe.md",
    "tier_reason": TIER.strip(),
}

def append_csv(path, fieldnames, row):
    existing = list(csv.DictReader(open(path, encoding="utf-8")))
    if any(str(r.get(fieldnames[0])) == str(row[fieldnames[0]]) for r in existing):
        print(f"SKIP: {path} already has index={row[fieldnames[0]]}")
        return False
    with open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        w.writerow(row)
    print(f"OK: appended index={row[fieldnames[0]]} to {path.name}")
    return True

with open(LEADS, encoding="utf-8") as f:
    leads_hdr = list(csv.DictReader(f).fieldnames or [])
with open(LWE, encoding="utf-8") as f:
    lwe_hdr = list(csv.DictReader(f).fieldnames or [])

ok1 = append_csv(LEADS, leads_hdr, new_lead_leads_csv)
ok2 = append_csv(LWE, lwe_hdr, new_lead_lwe)

# Verify parse-back
import re
with open(LEADS, encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
last = rows[-1]
assert str(last["index"]) == "272", f"leads.csv last idx={last['index']}"
assert "privacy@secureframe.com" in last["email"]
assert "compliance_automation" == last["vertical"]
print(f"VERIFY: leads.csv last row idx=272 OK; total rows={len(rows)}")

with open(LWE, encoding="utf-8") as f:
    rows2 = list(csv.DictReader(f))
last2 = rows2[-1]
assert str(last2["lead_index"]) == "272", f"lwe last idx={last2['lead_index']}"
assert "Shrav Naraghi" in last2["founder"]
assert "privacy@secureframe.com" in last2["best_email"]
print(f"VERIFY: leads_with_emails.csv last row idx=272 OK; total rows={len(rows2)}")
print("DONE")
