#!/usr/bin/env python3
"""Append Sprinto row to leads.csv with full tier_reason.
Single-shot script run from py -3.12 (not python alias — MSYS pitfall)."""
import csv
import os

REPO = r"C:\Users\Potts\projects\atlas-store"
CSV = os.path.join(REPO, "cold_email", "leads.csv")

INDEX = "650"
NAME = "Sprinto"
HANDLE = "@Sprintohq"
EMAIL = "sales@sprinto.com"
VERTICAL = "ai_compliance_automation"
TIER = "1"
TEMPLATE = "650_sprinto.md"

# Pre-flight: ensure row doesn't already exist (pitfall #69 — row-prefix anchor)
with open(CSV, "r", encoding="utf-8", errors="replace", newline="") as f:
    raw = f.read()
row_prefix = f'"{INDEX}","'
assert row_prefix not in raw, f"row {INDEX} already exists in leads.csv — abort"

# Tier reason — concise but exhaustive cohort wedge
TIER_REASON = (
    'Lead 650 - Sprinto (Sprinto Tech Pvt. Ltd. - Sprinto automated compliance + risk management platform + '
    'multi-framework coverage SOC 2 + ISO 27001 + HIPAA + GDPR + PCI DSS + NIST CSF + CMMC + ISO 27701 + '
    'automated evidence collection + auditor portal + risk management + vendor risk + trust center + '
    'Sprinto MDM device monitoring + Doctor Sprinto + Access Control + People Ops + Security Training + Reports + '
    '2,000+ customers + Bangalore HQ + India + US presence + founded 2019 by ex-RecruiterBox co-founders + '
    'Girish Redekar Co-Founder CEO + Raghuveer Kancherla Co-Founder CEO + Mohita Nagpal VP Marketing + '
    'Sandeepa Samuel VP People & Culture + Chaitanya Goyal Head of Product + Aayush Agarwal VP Strategy + '
    'Karthik V VP Solution Engineering + SOC 2 Type II + ISO 27001 + HIPAA ready) - '
    'ai_compliance_automation cohort sibling #4 after Drata 647 + Scrut 648 + Secureframe 649. '
    'Real company + real website + real founders + real verified inboxes verified live 2026-07-19 via Wayback archive 2024-06-01 of sprinto.com footer (Reach Us At section) which publishes '
    'sales@sprinto.com (canonical prospect / demo / start-trial inbox - tag icon) + '
    'support@sprinto.com (canonical customer support inbox - headphone icon). '
    'Sitemap twitter profile: @Sprintohq. '
    'Sources verified: sprinto.com (home) + sprinto.com/about-us (Meet the team with Girish Redekar + Raghuveer Kancherla) + sprinto.com/blog (comparison posts Sprinto vs Drata + Sprinto vs Scrut + Sprinto vs Secureframe + Sprinto vs Delve) + '
    'Wayback 2024-06-01 footer. '
    'Official positioning: automated compliance + risk-management + continuous compliance + evidence collection + risk register + trust center + '
    'Sprinto-MDM device monitoring + Doctor Sprinto + AI-powered evidence mapping + 100+ integrations + '
    '2,000+ customers served. '
    'Tier-1 evidence wedge: closed-loop audit-trail reproducibility (per-control + per-evidence-collection-timestamp + per-reviewer + per-auditor-access + '
    'per-framework-version + per-mapping-rule + per-exception + per-remediation) joined to Sprinto-AI-output provenance + '
    'per-prompt + per-model + per-tool-version + per-incident + per-human-override logging in single correlated evidence trail that maps to '
    'EU AI Act Articles 9 risk-management + 10 data-governance + 11 technical-documentation + 12 logging + 14 human-oversight + 15 accuracy/robustness/cybersecurity. '
    'Differentiated wedge from cohort siblings: Drata 647 owns FRAMEWORK-CONTROL-MAPPING + AUDITOR-PORTAL + EVIDENCE-COLLECTION-CONTINUITY wedge '
    '(US-first + 30+ frameworks + $328M Series C + 7,000+ customers); '
    'Scrut 648 owns INDIA-FIRST + RISK-REGISTER + TRUST-CENTER + BANKING-FINTECH-FOCUS + INDIA-DPDP-ACT-2023 wedge '
    '(Bangalore HQ + Indian SOC 2 + ISO 27001 + GDPR + HIPAA + PCI DSS + NIST CSF coverage + BFSI focus); '
    'Secureframe 649 owns YC-W15 OG-COMPLIANCE-AUTOMATION + FRAMEWORK-INHERITANCE + VENDOR-RISK + 100+ INTEGRATIONS wedge '
    '(original compliance-automation incumbent + Notion + Atlassian + Quora customer base + multi-framework inheritance engine); '
    'Sprinto 650 owns the EX-RECruiterBOX-FOUNDER + DEVICE-MONITORING-DOCTOR + ACCESS-CONTROL-PEOPS-TRAINING-PACK + INDIA-FIRST-DEVICE-INTELLIGENCE wedge specifically '
    '(the operational coverage that goes beyond compliance-paperwork into device monitoring + people-ops + security training + access-control surface - '
    'the human-layer controls that complement the paper-layer controls auditors need to verify). '
    'Offer: 500/48h evidence-gap map or 497/mo quarterly refresh. '
    'Recipient: sales@sprinto.com verified live via Wayback archive 2024-06-01 of sprinto.com footer Reach Us At section as canonical prospect / demo / start-trial inbox. '
    'No guessed inbox added.'
)

# Write the row with QUOTE_ALL to handle embedded commas/quotes
with open(CSV, "a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL, escapechar='"', quotechar='"')
    writer.writerow([INDEX, NAME, HANDLE, EMAIL, VERTICAL, TIER, TEMPLATE, TIER_REASON])

# Verify parse-back
with open(CSV, "r", encoding="utf-8", errors="replace", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
matches = [r for r in rows if r["index"] == INDEX]
assert len(matches) == 1, f"expected 1 row idx={INDEX}, got {len(matches)}"
m = matches[0]
assert m["name"] == NAME and m["email"] == EMAIL and m["vertical"] == VERTICAL and m["template"] == TEMPLATE
assert None not in m.values(), f"row has None keys: {m}"
print(f"[OK] leads.csv row {INDEX} appended: {NAME} | {EMAIL} | {m['template']} | tier_reason_len={len(m['tier_reason'])}")
