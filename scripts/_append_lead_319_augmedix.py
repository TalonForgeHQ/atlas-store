"""Append lead 319 Augmedix to BOTH cold_email/leads.csv and leads_with_emails.csv."""
import csv
import os
import sys
from collections import Counter
from pathlib import Path

REPO = Path(r"C:/Users/Potts/projects/atlas-store")
TIER_REASON_FILE = Path(os.environ["TEMP"]) / "tier_reason_319_augmedix.txt"

# Read tier_reason (single field, may contain commas + quotes)
tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").rstrip("\n")

# Sanity: tier_reason must NOT start with quote (would indicate CSV escaping failure)
if tier_reason.startswith('"'):
    sys.exit("ABORT: tier_reason starts with quote — would corrupt the CSV row")

# === Append to cold_email/leads.csv (8 columns: index,name,handle,email,vertical,tier,template,tier_reason) ===
leads_path = REPO / "cold_email" / "leads.csv"
with leads_path.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    leads_header = reader.fieldnames
    leads_rows = list(reader)

# dedupe invariant: no duplicate indices
existing_idxs = [int(r["index"]) for r in leads_rows if r.get("index") and r["index"].isdigit()]
assert 319 not in existing_idxs, f"ABORT: 319 already in leads.csv"

new_lead = {
    "index": "319",
    "name": "Augmedix",
    "handle": "@Augmedix",
    "email": "info@augmedix.com",
    "vertical": "ai_healthcare_clinical_assistant",
    "tier": "1",
    "template": "319_augmedix.md",
    "tier_reason": tier_reason,
}

with leads_path.open("a", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=leads_header, quoting=csv.QUOTE_ALL)
    writer.writerow(new_lead)

# === Append to cold_email/leads_with_emails.csv (13 columns: lead_index,company,handle,domain,website,founder,vertical,tier,best_email,emails_found,guessed_emails,source_template,tier_reason) ===
emails_path = REPO / "cold_email" / "leads_with_emails.csv"
with emails_path.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    emails_header = reader.fieldnames
    emails_rows = list(reader)

existing_lead_idxs = [int(r["lead_index"]) for r in emails_rows if r.get("lead_index") and r["lead_index"].isdigit()]
assert 319 not in existing_lead_idxs, f"ABORT: 319 already in leads_with_emails.csv"

new_email_lead = {
    "lead_index": "319",
    "company": "Augmedix",
    "handle": "@Augmedix",
    "domain": "augmedix.com",
    "website": "https://www.augmedix.com",
    "founder": "Manny Krakaris (Co-Founder + CEO, ex-Banc of America Securities + ex-Asia Pacific Wire + ex-Cantor Fitzgerald) + Ian Shakil (Co-Founder + Chief Strategy Officer, ex-McKinsey + ex-iRobot + ex-Baxter + ex-Intuitive Surgical + ex-Johnson & Johnson) + Pelu Tran (Co-Founder, ex-Deloitte + ex-Stanford d.school) + Tony Vo (Co-Founder + CTO, ex-Boston Scientific + ex-St. Jude Medical)",
    "vertical": "ai_healthcare_clinical_assistant",
    "tier": "1",
    "best_email": "info@augmedix.com",
    "emails_found": "info@augmedix.com;support@augmedix.com",
    "guessed_emails": "privacy@augmedix.com;legal@augmedix.com",
    "source_template": "319_augmedix.md",
    "tier_reason": tier_reason,
}

with emails_path.open("a", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=emails_header, quoting=csv.QUOTE_ALL)
    writer.writerow(new_email_lead)

# === Re-read BOTH files + verify dedupe invariant ===
for path, idx_col in [(leads_path, "index"), (emails_path, "lead_index")]:
    with path.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    idxs = [r.get(idx_col) for r in rows]
    dupes = [k for k, v in Counter(idxs).items() if v > 1 and k is not None]
    assert not dupes, f"DEDUPE FAIL on {path.name}: duplicate {idx_col} values: {dupes}"
    # verify row 319 / lead_index 319 parses back
    new_row = next((r for r in rows if r.get(idx_col) == "319"), None)
    assert new_row is not None, f"PARSE-BACK FAIL on {path.name}: row 319 not found"
    print(f"  {path.name}: rows={len(rows)}, header cols={len(rows[0].keys())}, 319 present, no dupes, parses back OK")
    if path.name == "leads.csv":
        assert new_row["tier_reason"].startswith("Canonical"), f"tier_reason parse-back anomaly: starts with {new_row['tier_reason'][:30]!r}"
        print(f"    tier_reason starts: {new_row['tier_reason'][:80]!r}...")

# Cleanup tier_reason temp file
TIER_REASON_FILE.unlink()
print(f"\nOK: lead 319 Augmedix appended to both CSVs. tier_reason temp file removed.")
print(f"  leads.csv: {leads_path.stat().st_size} bytes")
print(f"  leads_with_emails.csv: {emails_path.stat().st_size} bytes")
