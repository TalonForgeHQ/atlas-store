"""
Append lead 457 (Informatica) to BOTH cold_email CSVs.
Schema for leads.csv (8-col): index, name, handle, email, vertical, tier, template, tier_reason
Schema for leads_with_emails.csv (13-col): lead_index, company, handle, domain, website, founder, vertical, tier, best_email, emails_found, guessed_emails, source_template, tier_reason
"""
import csv
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
TIER_REASON_FILE = Path("C:/Users/Potts/AppData/Local/Temp/tick457_inf_tier_reason.txt")
tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").strip()

LEADS_CSV = REPO / "cold_email" / "leads.csv"
LEADS_WITH_EMAILS_CSV = REPO / "cold_email" / "leads_with_emails.csv"

# Pre-flight dedupe check per file
def existing_indices(path, idx_col):
    if not path.exists():
        return set()
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return {row[idx_col] for row in reader if row.get(idx_col)}

leads_idx = existing_indices(LEADS_CSV, "index")
lwe_idx = existing_indices(LEADS_WITH_EMAILS_CSV, "lead_index")

needs_leads = "457" not in leads_idx
needs_lwe = "457" not in lwe_idx
if not needs_leads and not needs_lwe:
    print(f"Both CSVs already have 457 — nothing to do")
    raise SystemExit(0)
if not needs_leads:
    print(f"leads.csv already has 457 (skipping leads append)")
if not needs_lwe:
    print(f"leads_with_emails.csv already has 457 (skipping lwe append)")
if needs_leads:
    with LEADS_CSV.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"],
            quoting=csv.QUOTE_ALL,
        )
        w.writerow({
            "index": "457",
            "name": "Informatica",
            "handle": "@informatica",
            "email": "privacy@informatica.com",
            "vertical": "data_governance",
            "tier": "1",
            "template": "457_informatica.md",
            "tier_reason": tier_reason,
        })

if needs_lwe:
    with LEADS_WITH_EMAILS_CSV.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["lead_index", "company", "handle", "domain", "website", "founder", "vertical", "tier", "best_email", "emails_found", "guessed_emails", "source_template", "tier_reason"],
            quoting=csv.QUOTE_ALL,
        )
        w.writerow({
            "lead_index": "457",
            "company": "Informatica",
            "handle": "@informatica",
            "domain": "informatica.com",
            "website": "https://www.informatica.com",
            "founder": "Gaurav Dhillon",
            "vertical": "data_governance",
            "tier": "1",
            "best_email": "privacy@informatica.com",
            "emails_found": "1",
            "guessed_emails": "privacy@informatica.com",
            "source_template": "457_informatica.md",
            "tier_reason": tier_reason,
        })

# Parse-back verification
def parse_back(path, idx_col, expected="457"):
    with path.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    last = rows[-1]
    assert last[idx_col] == expected, f"{path.name}: last row {idx_col}={last[idx_col]}, expected {expected}"
    assert last["vertical"] == "data_governance", f"{path.name}: vertical={last['vertical']}"
    name_field = "company" if "company" in last else "name"
    assert "Informatica" in last[name_field], f"{path.name}: {name_field}={last.get(name_field)} missing Informatica"
    assert "privacy@informatica.com" in last["best_email"] or "privacy@informatica.com" in last["email"], f"{path.name}: email missing"
    assert len(rows) == 337, f"{path.name}: expected 337 rows (336+1), got {len(rows)}"
    return rows

rows1 = parse_back(LEADS_CSV, "index")
rows2 = parse_back(LEADS_WITH_EMAILS_CSV, "lead_index")
print(f"OK: leads.csv + leads_with_emails.csv both at 337 rows, lead 457 = Informatica / data_governance / privacy@informatica.com")
print(f"  leads.csv last row keys: {list(rows1[-1].keys())}")
print(f"  leads_with_emails.csv last row keys: {list(rows2[-1].keys())}")