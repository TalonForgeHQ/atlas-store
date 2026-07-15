"""Append lead 273 (Secureframe) to cold_email/leads.csv + leads_with_emails.csv.
273 reserved because Kestra took 272 in the last tick."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEADS = ROOT / "cold_email" / "leads.csv"
LWE = ROOT / "cold_email" / "leads_with_emails.csv"
TIER = (ROOT / "cold_email" / "tier_reason_272_secureframe.txt").read_text(encoding="utf-8").strip()

IDX = "273"

new_lead_leads_csv = {
    "index": IDX,
    "name": "Secureframe",
    "handle": "@secureframe",
    "email": "privacy@secureframe.com",
    "vertical": "compliance_automation",
    "tier": "1",
    "template": "363_secureframe.md",
    "tier_reason": TIER,
}

new_lead_lwe = {
    "lead_index": IDX,
    "company": "Secureframe",
    "handle": "@secureframe",
    "domain": "secureframe.com",
    "website": "https://www.secureframe.com",
    "founder": "Shrav Naraghi (Co-Founder & CEO)",
    "vertical": "compliance_automation",
    "tier": "1",
    "best_email": "privacy@secureframe.com",
    "emails_found": "privacy@secureframe.com",
    "guessed_emails": "",
    "source_template": "363_secureframe.md",
    "tier_reason": TIER,
}

def append_csv(path, fieldnames, row, idcol):
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    if any(str(r.get(idcol)) == str(row[idcol]) for r in rows):
        print(f"SKIP: {path} already has {idcol}={row[idcol]}")
        return False
    with open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        w.writerow(row)
    print(f"OK: appended {idcol}={row[idcol]} to {path.name}")
    return True

with open(LEADS, encoding="utf-8") as f:
    leads_hdr = list(csv.DictReader(f).fieldnames or [])
with open(LWE, encoding="utf-8") as f:
    lwe_hdr = list(csv.DictReader(f).fieldnames or [])

ok1 = append_csv(LEADS, leads_hdr, new_lead_leads_csv, "index")
ok2 = append_csv(LWE, lwe_hdr, new_lead_lwe, "lead_index")

with open(LEADS, encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
last = rows[-1]
assert str(last["index"]) == IDX, f"leads.csv last idx={last['index']}"
assert last["email"] == "privacy@secureframe.com"
assert last["vertical"] == "compliance_automation"
print(f"VERIFY: leads.csv last idx={IDX} email=privacy@secureframe.com OK; total rows={len(rows)}")

with open(LWE, encoding="utf-8") as f:
    rows2 = list(csv.DictReader(f))
last2 = rows2[-1]
assert str(last2["lead_index"]) == IDX
assert last2["best_email"] == "privacy@secureframe.com"
assert "Shrav Naraghi" in last2["founder"]
print(f"VERIFY: leads_with_emails.csv last idx={IDX} OK; total rows={len(rows2)}")

# dedupe invariant
from collections import Counter
leads_dupes = [k for k, v in Counter(r["index"] for r in rows).items() if v > 1]
lwe_dupes = [k for k, v in Counter(r["lead_index"] for r in rows2).items() if v > 1]
assert not leads_dupes, f"leads.csv duplicate indices: {leads_dupes}"
assert not lwe_dupes, f"leads_with_emails.csv duplicate indices: {lwe_dupes}"
print("DEDUPE: both files have unique indices")
print("DONE")
