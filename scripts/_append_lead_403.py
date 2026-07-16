#!/usr/bin/env python3
"""Append Lead 403 (Arize AI) to BOTH cold_email CSVs with correct schemas."""
import csv
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
TIER_REASON = (Path("C:/Users/Potts/AppData/Local/Temp/tier_reason_403.txt")).read_text(encoding="utf-8").strip()

# ============ cold_email/leads.csv (8 cols: index, name, handle, email, vertical, tier, template, tier_reason) ============
leads_path = REPO / "cold_email" / "leads.csv"
with open(leads_path, "r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
print(f"leads.csv: {len(rows)} rows BEFORE; last index={rows[-1]['index']}")

new_lead = {
    "index": "403",
    "name": "Arize AI",
    "handle": "@arize",
    "email": "support@arize.com",
    "vertical": "ai_eval_observability",
    "tier": "1",
    "template": "403_arize.md",
    "tier_reason": TIER_REASON,
}
with open(leads_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["index","name","handle","email","vertical","tier","template","tier_reason"], quoting=csv.QUOTE_ALL)
    w.writerow(new_lead)

# ============ cold_email/leads_with_emails.csv (13 cols: lead_index, company, handle, domain, website, founder, vertical, tier, best_email, emails_found, guessed_emails, source_template, tier_reason) ============
leads_with_emails_path = REPO / "cold_email" / "leads_with_emails.csv"
with open(leads_with_emails_path, "r", encoding="utf-8", newline="") as f:
    rows2 = list(csv.DictReader(f))
print(f"leads_with_emails.csv: {len(rows2)} rows BEFORE; last lead_index={rows2[-1]['lead_index']}")

new_lead2 = {
    "lead_index": "403",
    "company": "Arize AI",
    "handle": "@arize",
    "domain": "arize.com",
    "website": "https://arize.com",
    "founder": "Jason Lopatecki (Co-Founder & CEO); Aparna Dhinakaran (Co-Founder & CPO)",
    "vertical": "ai_eval_observability",
    "tier": "1",
    "best_email": "support@arize.com",
    "emails_found": "support@arize.com;privacy@arize.com",
    "guessed_emails": "",
    "source_template": "403_arize.md",
    "tier_reason": TIER_REASON,
}
with open(leads_with_emails_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["lead_index","company","handle","domain","website","founder","vertical","tier","best_email","emails_found","guessed_emails","source_template","tier_reason"], quoting=csv.QUOTE_ALL)
    w.writerow(new_lead2)

# ============ Parse-back verification ============
with open(leads_path, "r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
last = rows[-1]
assert last["index"] == "403", f"FAIL leads.csv last index {last['index']}"
assert last["name"] == "Arize AI", f"FAIL name {last['name']}"
assert last["email"] == "support@arize.com", f"FAIL email {last['email']}"
assert last["vertical"] == "ai_eval_observability", f"FAIL vertical {last['vertical']}"
assert last["tier_reason"].startswith("Lead 403"), f"FAIL tier_reason shape: {last['tier_reason'][:60]}"
print(f"leads.csv: {len(rows)} rows AFTER; last = {last['index']} {last['name']} | {last['email']} | tier_reason starts OK")

with open(leads_with_emails_path, "r", encoding="utf-8", newline="") as f:
    rows2 = list(csv.DictReader(f))
last2 = rows2[-1]
assert last2["lead_index"] == "403", f"FAIL leads_with_emails.csv last lead_index {last2['lead_index']}"
assert last2["best_email"] == "support@arize.com"
assert last2["company"] == "Arize AI"
print(f"leads_with_emails.csv: {len(rows2)} rows AFTER; last = {last2['lead_index']} {last2['company']} | {last2['best_email']}")

# Dedupe invariant
from collections import Counter
leads_idxs = [r.get("index") for r in rows]
leads_with_emails_idxs = [r.get("lead_index") for r in rows2]
dupes1 = [k for k, v in Counter(leads_idxs).items() if v > 1]
dupes2 = [k for k, v in Counter(leads_with_emails_idxs).items() if v > 1]
print(f"dupes leads.csv: {dupes1}")
print(f"dupes leads_with_emails.csv: {dupes2}")
assert not dupes1, f"FAIL leads.csv has duplicate indices: {dupes1}"
assert not dupes2, f"FAIL leads_with_emails.csv has duplicate indices: {dupes2}"
print("ALL OK - Lead 403 (Arize AI) appended to BOTH CSVs cleanly")