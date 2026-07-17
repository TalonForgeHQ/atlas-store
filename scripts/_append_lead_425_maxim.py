"""Append Lead 425 Maxim AI to leads.csv + leads_with_emails.csv. Two-schema discipline."""
import csv
import tempfile
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
LEADS_CSV = REPO / "cold_email" / "leads.csv"
LEADS_WITH_EMAILS_CSV = REPO / "cold_email" / "leads_with_emails.csv"
TIER_REASON_TXT = Path(tempfile.gettempdir()) / "tier_reason_425_maxim.txt"

# === Dedup guard (must run BEFORE append) ===
with open(LEADS_CSV, "r", encoding="utf-8", newline="") as f:
    existing_leads = list(csv.DictReader(f))
existing_lead_idxs = {r["index"] for r in existing_leads}
assert "425" not in existing_lead_idxs, "Lead 425 already in leads.csv — aborting"

with open(LEADS_WITH_EMAILS_CSV, "r", encoding="utf-8", newline="") as f:
    existing_lwe = list(csv.DictReader(f))
existing_lwe_idxs = {r["lead_index"] for r in existing_lwe}
assert "425" not in existing_lwe_idxs, "Lead 425 already in leads_with_emails.csv — aborting"

tier_reason = TIER_REASON_TXT.read_text(encoding="utf-8").strip()

# === Append to leads.csv (8 cols: index, name, handle, email, vertical, tier, template, tier_reason) ===
with open(LEADS_CSV, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(
        f,
        fieldnames=["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"],
        quoting=csv.QUOTE_ALL,
    )
    w.writerow({
        "index": "425",
        "name": "Maxim AI",
        "handle": "@getmaximai",
        "email": "roroghost17@gmail.com",
        "vertical": "ai_agents_infra",
        "tier": "1",
        "template": "425_maxim.md",
        "tier_reason": tier_reason,
    })

# === Append to leads_with_emails.csv (13 cols: lead_index, company, handle, domain, website, founder, vertical, tier, best_email, emails_found, guessed_emails, source_template, tier_reason) ===
with open(LEADS_WITH_EMAILS_CSV, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(
        f,
        fieldnames=["lead_index", "company", "handle", "domain", "website", "founder",
                    "vertical", "tier", "best_email", "emails_found", "guessed_emails",
                    "source_template", "tier_reason"],
        quoting=csv.QUOTE_ALL,
    )
    w.writerow({
        "lead_index": "425",
        "company": "Maxim AI",
        "handle": "@getmaximai",
        "domain": "getmaxim.ai",
        "website": "https://www.getmaxim.ai/",
        "founder": "Vaibhavi Agrawal (CEO) + Aryan Deshmukh (CTO) + Akshay Deo (Chief AI Officer)",
        "vertical": "ai_agents_infra",
        "tier": "1",
        "best_email": "roroghost17@gmail.com",
        "emails_found": "1",
        "guessed_emails": "roroghost17@gmail.com | akshay@akshaydeo.com | madhu.shantan@getmaxim.ai | contact@getmaxim.ai | security@getmaxim.ai",
        "source_template": "425_maxim.md",
        "tier_reason": tier_reason,
    })

# === Parse-back verification ===
print("=== Verifying appends ===")
with open(LEADS_CSV, "r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
last_leads = rows[-1]
assert last_leads["index"] == "425", f"leads.csv last index {last_leads['index']} != 425"
assert last_leads["name"] == "Maxim AI"
assert last_leads["email"] == "roroghost17@gmail.com"
assert "Aryan" in last_leads["tier_reason"]
assert not last_leads["tier_reason"].startswith('"'), "tier_reason wraps in quotes — DictWriter corruption"
print(f"leads.csv: {len(rows)} rows, last index={last_leads['index']} ✓")

with open(LEADS_WITH_EMAILS_CSV, "r", encoding="utf-8", newline="") as f:
    rows_lwe = list(csv.DictReader(f))
last_lwe = rows_lwe[-1]
assert last_lwe["lead_index"] == "425"
assert last_lwe["company"] == "Maxim AI"
assert last_lwe["best_email"] == "roroghost17@gmail.com"
print(f"leads_with_emails.csv: {len(rows_lwe)} rows, last index={last_lwe['lead_index']} ✓")

# === Dedupe invariant ===
from collections import Counter
leads_dupes = {k: v for k, v in Counter(r["index"] for r in rows).items() if v > 1}
lwe_dupes = {k: v for k, v in Counter(r["lead_index"] for r in rows_lwe).items() if v > 1}
assert not leads_dupes, f"leads.csv duplicate indices: {leads_dupes}"
assert not lwe_dupes, f"leads_with_emails.csv duplicate lead_index: {lwe_dupes}"
print("Zero duplicate indices in both CSVs ✓")
print("Lead 425 Maxim AI appended + verified.")