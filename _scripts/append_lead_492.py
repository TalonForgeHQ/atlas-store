import csv
import os

REPO = r"C:/Users/Potts/projects/atlas-store"

# Lead 492 — Agiloft
INDEX = "492"
NAME = "Agiloft"
HANDLE = "@agiloft"
EMAIL = "privacy@agiloft.com"
VERTICAL = "ai_contract_intelligence"
TIER = "1"
TEMPLATE = "492_agiloft.md"
TIER_REASON = (
    "Lead 492 - Agiloft (agiloft.com, AI-CLM + contract lifecycle management + KKR majority-stake platform + AI-tagging + AI-clause-extraction + AI-obligation-extraction + per-tenant workflow engine + Prighter EU-representative + per-customer-corpus-hash provenance). "
    "Tier-1 ai_contract_intelligence cohort sibling #3 (after LinkSquares 490 + ContractWorks 491). "
    "Real company verified live 2026-07-17: en.wikipedia.org/wiki/Agiloft returned HTTP 200 (Infobox verified; founded October 12 1990 in Redwood City California by Colin Earl; "
    "current CEO Eric Laughlin since 2020+; former name Integral Solutions Corporation; type Private; industry Contract Lifecycle Management; key people Eric Laughlin CEO + Kevin Niblock CRO + Andy Wishart CPO + John Pechacek CTO + Jason Barnwell CLO; "
    "May 2024 KKR & Co. acquired majority stake with FTV Capital follow-on + JMI Equity new investor). "
    "agiloft.com/privacy-policy returned HTTP 200 (full Privacy Notice; mailto:privacy@agiloft.com canonical privacy + DPA + EU AI Act + vendor-DD strategic-inbound channel exposed; "
    "mailto:marketing@agiloft.com marketing opt-out exposed; EEA + Switzerland + UK Prighter EU-representative prighter.com/q/19881203804 confirmed; 12-state US consumer-privacy disclosure + financial-incentive + authorized-agent + appeals + international-data-transfers Standard Contractual Clauses + California-notice-at-collection all confirmed). "
    "Founder Colin Earl is the 30-year pioneer of the 'highly-configurable CLM without code' category; current CEO Eric Laughlin transformed Agiloft from bootstrapped CLM into KKR-backed AI-CLM platform. "
    "5 audit gaps: (1) end-to-end 13-col per-contract-id -> per-clause-id -> per-AI-tagging-id -> per-clause-extraction-id -> per-workflow-step-id -> per-obligation-trigger-id -> per-renewal-alert-id -> per-tenant-id -> per-KKR-platform-event-id -> per-FTV-portfolio-event-id -> per-procurement-vendor-DD-event-id -> per-audit-log-entry-id -> per-residency-region-id provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + ABA Model Rule 1.1 + ABA Model Rule 5.3 + ABA Model Rule 1.6 + FRCP Rule 11 + IBA Rules on Technology and Confidentiality + EDRM + GDPR Art. 22 + GDPR Art. 9 + EU AI Act Annex III 4 high-risk, "
    "(2) AI-tagging + AI-clause-extraction + AI-obligation-extraction training-corpus + fine-tune-license-provenance per EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary + ISO 42001 6.1.4 (Agiloft corpus spans customer contracts + customer clause-library + customer workflow-history - canonical EU AI Act Aug 2 2026 GPAI documentation target + per-Prighter-EU-representative-registration-id cross-border-data-transfer-provenance), "
    "(3) prompt-injection + clause-poisoning + AI-tagging-poisoning + AI-clause-extraction-poisoning + AI-obligation-extraction-poisoning + automated-workflow-step-poisoning + renewal-alert-poisoning defense per OWASP LLM Top 10 LLM01+LLM03+LLM06+LLM08 + MITRE ATLAS + EU AI Act Art. 14 human-oversight + Art. 50 transparency-obligation + 12-state AI-disclosure (CA SB 1001 + CO SB 24-205 + IL AI Video Interview Act + TX + NY + 7 others - Agiloft AI-revisions reach General Counsel + Procurement + Compliance + Sales organizations across all 50 states + EU), "
    "(4) cross-tenant contract + clause + AI-tagging + AI-clause-extraction + AI-obligation-extraction + automated-workflow-step + renewal-alert + KKR-platform-event + FTV-portfolio-event + per-tenant-KMS-key-id + CMK/BYOK + per-tenant-isolation per SOC 2 CC6.1 + GDPR Art. 28 + Schrems II + Prighter-EU-representative cross-border-data-transfer (cross-tenant-isolation-evidence is auditable; critical for Fortune-1000 + global-2000 + procurement + healthcare + pharma + financial-services tenants where contract-tenant-isolation is auditable), "
    "(5) WORM retention + cost-attribution join-table linking per-AI-tagging-cost + per-AI-clause-extraction-cost + per-AI-obligation-extraction-cost + per-automated-workflow-step-cost + per-renewal-alert-cost + per-KKR-platform-event-cost + per-FTV-portfolio-event-cost + per-customer-tenant-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + EU AI Act Annex III 4 + Aug 2 2026 GPAI enforcement. "
    "privacy@agiloft.com is the verified SOC 2 + GDPR DPA + CCPA/CPRA + EU AI Act + Prighter EU-representative + enterprise-procurement-vendor-DD strategic-inbound channel for Agiloft + AI-CLM + AI-tagging + AI-clause-extraction + AI-obligation-extraction + KKR-majority-stake + enterprise-procurement-vendor-DD strategic-inbound inquiries."
)

DOMAIN = "agiloft.com"
WEBSITE = "https://www.agiloft.com"
FOUNDER = "Colin Earl (Founder + original CEO since 1990); Eric Laughlin (current CEO since 2020+)"

# ---- Append to leads.csv (8-col schema) ----
leads_csv = os.path.join(REPO, "cold_email", "leads.csv")
with open(leads_csv, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = reader.fieldnames

# baseline check BEFORE append
baseline = len(rows)
print(f"leads.csv baseline rows: {baseline}")
assert baseline >= 365, f"baseline too low: {baseline}"

# Check no dup
existing = [r for r in rows if r["index"] == INDEX]
assert not existing, f"Lead {INDEX} already exists in leads.csv"

with open(leads_csv, "a", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writerow({
        "index": INDEX,
        "name": NAME,
        "handle": HANDLE,
        "email": EMAIL,
        "vertical": VERTICAL,
        "tier": TIER,
        "template": TEMPLATE,
        "tier_reason": TIER_REASON,
    })

# parse back
with open(leads_csv, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows2 = list(reader)
print(f"leads.csv after append rows: {len(rows2)}")
print(f"Last row index: {rows2[-1]['index']} | name: {rows2[-1]['name']}")
assert len(rows2) == baseline + 1, "row count mismatch in leads.csv"
assert rows2[-1]["index"] == INDEX, "last row index mismatch"

# dedupe invariant
from collections import Counter
counts = Counter(r["index"] for r in rows2)
dupes = [k for k, v in counts.items() if v > 1]
assert not dupes, f"dupes in leads.csv: {dupes}"

# ---- Append to leads_with_emails.csv (13-col schema) ----
leads_w_csv = os.path.join(REPO, "cold_email", "leads_with_emails.csv")
with open(leads_w_csv, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rowsw = list(reader)
    fieldnamesw = reader.fieldnames

baselinew = len(rowsw)
print(f"leads_with_emails.csv baseline rows: {baselinew}")
assert baselinew >= 325, f"baselinew too low: {baselinew}"

existing_w = [r for r in rowsw if r["lead_index"] == INDEX]
assert not existing_w, f"Lead {INDEX} already exists in leads_with_emails.csv"

with open(leads_w_csv, "a", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnamesw, quoting=csv.QUOTE_ALL)
    writer.writerow({
        "lead_index": INDEX,
        "company": NAME,
        "handle": HANDLE,
        "domain": DOMAIN,
        "website": WEBSITE,
        "founder": FOUNDER,
        "vertical": VERTICAL,
        "tier": TIER,
        "best_email": EMAIL,
        "emails_found": EMAIL,
        "guessed_emails": EMAIL,
        "source_template": TEMPLATE,
        "tier_reason": TIER_REASON,
    })

# parse back
with open(leads_w_csv, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rowsw2 = list(reader)
print(f"leads_with_emails.csv after append rows: {len(rowsw2)}")
print(f"Last row lead_index: {rowsw2[-1]['lead_index']} | company: {rowsw2[-1]['company']}")
assert len(rowsw2) == baselinew + 1, "row count mismatch in leads_with_emails.csv"
assert rowsw2[-1]["lead_index"] == INDEX, "last row lead_index mismatch"

countsw = Counter(r["lead_index"] for r in rowsw2)
dupesw = [k for k, v in countsw.items() if v > 1]
assert not dupesw, f"dupes in leads_with_emails.csv: {dupesw}"

print("OK — Lead 492 Agiloft appended to both CSVs cleanly")
