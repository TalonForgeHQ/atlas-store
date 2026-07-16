"""
Append Lead 378 Cresta to both leads.csv (8-col) and leads_with_emails.csv (13-col).
Two schemas — DO NOT confuse dict shapes.
"""
import csv
import os
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
LEADS = REPO / "cold_email" / "leads.csv"
LWE = REPO / "cold_email" / "leads_with_emails.csv"
TIER_REASON = Path("C:/Users/Potts/AppData/Local/Temp/tier_reason_378_cresta.md")
TEMPLATE = REPO / "cold_email" / "templates" / "378_cresta.md"

tier_reason = TIER_REASON.read_text(encoding="utf-8").strip()

# === leads.csv (8-col schema) ===
# index, name, handle, email, vertical, tier, template, tier_reason
row8 = {
    "index": "378",
    "name": "Cresta",
    "handle": "@crestaai",
    "email": "cresta-privacy@cresta.ai",
    "vertical": "ai_voice_agents_orchestration",
    "tier": "1",
    "template": "378_cresta.md",
    "tier_reason": tier_reason,
}

with LEADS.open("a", newline="", encoding="utf-8") as f:
    cols = ["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"]
    w = csv.DictWriter(f, fieldnames=cols, quoting=csv.QUOTE_ALL)
    w.writerow(row8)

# === leads_with_emails.csv (13-col schema) ===
# lead_index, company, handle, domain, website, founder, vertical, tier, best_email, emails_found, guessed_emails, source_template, tier_reason
row13 = {
    "lead_index": "378",
    "company": "Cresta",
    "handle": "@crestaai",
    "domain": "cresta.ai",
    "website": "https://cresta.com",
    "founder": "Tim Shi (Co-Founder & CEO) + Zayd Enam (Co-Founder & CTO) + Sebastian Thrun (Co-Founder)",
    "vertical": "ai_voice_agents_orchestration",
    "tier": "1",
    "best_email": "cresta-privacy@cresta.ai",
    "emails_found": '["cresta-privacy@cresta.ai"]',
    "guessed_emails": '["privacy@cresta.ai", "security@cresta.ai", "legal@cresta.ai"]',
    "source_template": "378_cresta.md",
    "tier_reason": tier_reason,
}

with LWE.open("a", newline="", encoding="utf-8") as f:
    cols = ["lead_index", "company", "handle", "domain", "website", "founder", "vertical", "tier",
            "best_email", "emails_found", "guessed_emails", "source_template", "tier_reason"]
    w = csv.DictWriter(f, fieldnames=cols, quoting=csv.QUOTE_ALL)
    w.writerow(row13)

# === Parse-back verification ===
print(f"=== Last rows of leads.csv ===")
with LEADS.open("r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print(f"total rows: {len(rows)}")
print(f"last row index: {rows[-1]['index']} | name: {rows[-1]['name']} | email: {rows[-1]['email']}")
print(f"tier_reason len: {len(rows[-1]['tier_reason'])} chars")
print(f"tier_reason starts with quote: {rows[-1]['tier_reason'].startswith(chr(34))}")

print(f"\n=== Last rows of leads_with_emails.csv ===")
with LWE.open("r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print(f"total rows: {len(rows)}")
print(f"last row lead_index: {rows[-1]['lead_index']} | company: {rows[-1]['company']} | best_email: {rows[-1]['best_email']}")

# === Dedupe invariant ===
from collections import Counter
with LEADS.open("r", encoding="utf-8") as f:
    lead_idxs = [r["index"] for r in csv.DictReader(f)]
with LWE.open("r", encoding="utf-8") as f:
    lwe_idxs = [r["lead_index"] for r in csv.DictReader(f)]
print(f"\n=== Dedupe invariants ===")
print(f"leads.csv: {len(lead_idxs)} entries, {len(set(lead_idxs))} unique, dupes: {[k for k,v in Counter(lead_idxs).items() if v>1]}")
print(f"leads_with_emails.csv: {len(lwe_idxs)} entries, {len(set(lwe_idxs))} unique, dupes: {[k for k,v in Counter(lwe_idxs).items() if v>1]}")

# === Template file presence check ===
print(f"\n=== Template ===")
print(f"378_cresta.md exists: {TEMPLATE.exists()}")
if TEMPLATE.exists():
    tpl = TEMPLATE.read_text(encoding="utf-8")
    print(f"  size: {len(tpl)} chars")
    print(f"  contains Tim Shi: {'Tim Shi' in tpl}")
    print(f"  contains Zayd Enam: {'Zayd Enam' in tpl}")
    print(f"  contains cresta-privacy@cresta.ai: {'cresta-privacy@cresta.ai' in tpl}")
    print(f"  contains $500: {'$500' in tpl}")
    print(f"  contains $497: {'$497' in tpl}")