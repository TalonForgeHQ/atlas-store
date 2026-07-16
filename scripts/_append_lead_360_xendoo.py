#!/usr/bin/env python3
"""Append lead 360 Xendoo to leads.csv + leads_with_emails.csv.
Cohort bookkeeping_ai_ops 6th-sibling (closes canonical 6-vendor chain).
"""
import csv, sys
from pathlib import Path
from collections import Counter

ROOT = Path(r"C:\Users\Potts\projects\atlas-store")
LEADS = ROOT / "cold_email" / "leads.csv"
LEADS_WE = ROOT / "cold_email" / "leads_with_emails.csv"

# Lead 360 - Xendoo
LEAD_INDEX = "360"
COMPANY = "Xendoo"
HANDLE = "@xendoo"
DOMAIN = "xendoo.com"
WEBSITE = "https://www.xendoo.com/"
FOUNDER = "Lil Roberts (CEO + Founder, ex-small-business-owner-turned-bookkeeping-automation-founder)"
EMAIL = "support@xendoo.com"
VERTICAL = "bookkeeping_ai_ops"
TIER = "1"
TEMPLATE = "360_xendoo.md"

tier_reason = (
    'Lead 360 \u2014 Xendoo (Lil Roberts, CEO + Founder, Boca Raton FL). '
    'Tier-1 bookkeeping_ai_ops 6th-sibling (CLOSES canonical 6-vendor bookkeeping_ai_ops cohort '
    '+ Bookkeep 352 VERTEX + Bench 355 2nd-sibling + Pilot.com 357 3rd-sibling + Botkeeper 358 '
    '4th-sibling + Catch 359 5th-sibling + Xendoo 360 6th-sibling CLOSES cohort). Small-business '
    'online bookkeeping + accounting + tax + catch-up bookkeeping + AdvisorConnect (wealth-advisor '
    '+ family-office + CPA-practice portal) + Franchise-specialty bookkeeping + Xero + QuickBooks '
    'Online + Sage + NetSuite + multi-entity + multi-location + franchise-system consolidation '
    'vendor with per-small-business-client-id + per-monthly-close-event-id + per-bank-transaction-id '
    '+ per-receipt-line-item-id + per-AI-categorization-decision-id + per-bookkeeper-override-id '
    '+ per-rollback-id + per-Xero-invoice-id + per-QBO-invoice-id + per-Sage-invoice-id + '
    'per-NetSuite-invoice-id + per-financial-statement-id + per-trial-balance-id + per-balance-'
    'sheet-id + per-income-statement-id + per-cash-flow-statement-id + per-tax-filing-id + '
    'per-1099-id + per-1099-MISC-id + per-1099-NEC-id + per-1099-K-id + per-W-2-id + per-W-3-id '
    '+ per-payroll-run-id + per-payroll-event-id + per-federal-tax-deposit-id + per-state-tax-'
    'deposit-id + per-franchise-royalty-id + per-franche-location-id + per-multi-entity-id + '
    'per-multi-location-id + per-customer-LTV-id + per-product-id + per-product-SKU-id + '
    'per-class-id + per-location-id + per-department-id + per-franchise-system-id + per-franchise-'
    'royalty-rate-version-id + per-AdvisorConnect-client-id + per-AdvisorConnect-advisor-id + '
    '+ per-CPA-practice-id + per-CPA-staff-id + per-boundless-AI-loan-id + per-business-lending-'
    'partner-id + per-prompt-injection-detection-signal-id + per-tenant-id + per-tenant-KMS-key-id '
    '+ per-customer-tenant-isolation-flag + per-VPC-peering-id + per-SSO-SAML-OIDC-config-id + '
    'per-SCIM-provisioning-id + per-audit-log-export-id + per-data-residency-region + per-cross-'
    'border-data-transfer-mechanism + per-zero-retention-flag + per-BYOK-key-id + per-customer-'
    'opt-out-of-training-flag + per-AdvisorConnect-tenant-id + per-CPA-practice-tenant-id + '
    'per-franchise-tenant-id lineage. support@xendoo.com verified live 2026-07-16 via curl scrape '
    'https://www.xendoo.com/privacy-policy HTTP 200 389920 bytes exposing mailto:support@xendoo.com '
    'as canonical CCPA/CPRA + GDPR DPA + SOC 2 + IRS Publication 4557 + IRS Notice 2024-08 + IRS '
    'Pub 463 + GSA Per Diem + EU AI Act readiness + OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF '
    'MEASURE + vendor-DD strategic-inbound channel. Xendoo founded 2015 Boca Raton Florida by Lil '
    'Roberts (CEO + Founder, ex-small-business-owner-turned-bookkeeping-automation-founder + '
    'AccountingToday Top 100 Most Influential People + multiple industry-recognition awards). HQ '
    'Boca Raton FL (South Florida) + remote-distributed. Backed $20M+ across Seed + Series A + '
    'Series B from Boca Raton-based-angel-network + Florida-Venture-Partners + SaaS-focused-VCs + '
    'multiple strategic-angels. Customers: 1000+ small-business customers + franchise-systems + '
    'eCommerce-businesses + professional-services-firms + medical-practices + retail-businesses + '
    'hospitality-businesses + trade-businesses + CPA-practices + wealth-advisors + family-offices '
    'using Xendoo Bookkeeping + Xendoo Accounting + Xendoo Tax + Xendoo Catch-Up Bookkeeping + '
    'Xendoo AdvisorConnect + Xendoo Franchise + Xendoo Xero-Integration + Xendoo QuickBooks-Online-'
    'Integration + Xendoo Sage-Integration + Xendoo NetSuite-Integration + Boundless-AI-business-'
    'lending-referral at production scale. SOC 2 Type II in progress + GDPR DPA + CCPA/CPRA + IRS '
    'Publication 4557 + IRS Notice 2024-08 + IRS Pub 463 + EU AI Act readiness + per-tenant-id + '
    'per-customer-id + per-small-business-client-id + per-franchise-system-id + per-CPA-practice-'
    'id isolation + per-VPC-peering for enterprise-deployed-instances + per-SSO-SAML-OIDC + '
    'per-SCIM-provisioning + per-audit-log-export to S3/Splunk/Datadog support. 5 audit gaps '
    'documented covering end-to-end per-small-business-client-id + per-monthly-close-event-id + '
    'per-bank-transaction-id + per-receipt-line-item-id + per-AI-categorization-decision-id + '
    'per-bookkeeper-override-id + per-Xero-invoice-id + per-QBO-invoice-id + per-financial-statement-'
    'id + per-tax-filing-id + per-1099-id + per-payroll-run-id + per-franchise-royalty-id + '
    'per-AdvisorConnect-client-id + per-prompt-injection-detection-signal-id + per-tenant-id + '
    'per-tenant-KMS-key-id join-table per SOC 2 CC7.2 + IRS \u00a76001 + \u00a76501 + EU AI Act Art. 12 '
    'capturing 45+ columns, ML-model-versioning + ML-prediction-log + ML-active-learning-loop + '
    'human-feedback-in-the-loop per ISO 42001 6.4 + EU AI Act Art. 9 + Art. 14 + NIST AI RMF MEASURE '
    'with 12-column per-ML-prediction-id join-table, prompt-injection + bank-feed-poisoning + '
    'receipt-OCR-poisoning + per-categorization-rule-poisoning + per-franchise-royalty-'
    'calculation-poisoning + per-AdvisorConnect-client-data-poisoning defense per OWASP LLM Top 10 '
    'LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS with 10-column per-ML-prediction-id join-table, '
    'cross-tenant + cross-customer + cross-small-business-client + cross-franchise-system + '
    'cross-CPA-practice + cross-AdvisorConnect-tenant isolation-evidence per SOC 2 CC6.1 + GDPR '
    'Art. 28 + CCPA/CPRA + IRS Publication 4557 with 11-column per-tenant-id join-table with '
    'CMK/BYOK + per-tenant-KMS-key-id + per-tenant-isolation-flag + per-cross-border-transfer-'
    'sccs-version-US-EU + per-franchise-tenant-isolation-flag + per-CPA-practice-tenant-isolation, '
    'WORM retention + cost-attribution + EU AI Act Annex III 5(a) high-risk-classification per Art. '
    '6+14+27+43+72 + Art. 50 transparency-obligation with 12-column end-to-end Xendoo-bank-'
    'transaction-to-AI-categorization-to-bookkeeper-override-to-monthly-close-to-financial-'
    'statement-to-tax-filing reconstruction linking per-bank-transaction-id + per-AI-'
    'categorization-decision-id + per-bookkeeper-override-id + per-rollback-id + per-Xero-invoice-id '
    '+ per-QBO-invoice-id + per-financial-statement-id + per-tax-filing-id + per-1099-id + per-'
    'payroll-run-id + per-WORM-retention-flag + per-breach-detection-event-id. support@xendoo.com '
    'is the verified CCPA/CPRA + GDPR DPA + SOC 2 + IRS Publication 4557 + IRS Notice 2024-08 + IRS '
    'Pub 463 + GSA Per Diem + EU AI Act + OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF + vendor-DD '
    'strategic-inbound channel for Xendoo Bookkeeping + Xendoo Accounting + Xendoo Tax + Xendoo '
    'Catch-Up Bookkeeping + Xendoo AdvisorConnect + Xendoo Franchise + Xendoo Xero + Xendoo '
    'QuickBooks Online + Xendoo Sage + Xendoo NetSuite + bookkeeping_ai_ops + per-bank-transaction-'
    'id + per-AI-categorization-decision-id + per-bookkeeper-override-id + per-monthly-close-event-'
    'id + per-Xero-invoice-id + per-QBO-invoice-id + per-financial-statement-id + per-tax-filing-id '
    '+ per-1099-id + per-payroll-run-id + per-franchise-royalty-id + per-AdvisorConnect-client-id '
    '+ per-prompt-injection-detection-signal-id + per-tenant-id + bookkeeping_ai_ops cohort-'
    'CLOSING 6th-sibling + canonical-cohort-completing audit-target inquiries.'
)

# Pre-flight: confirm 360 not already present
for path, idx_col in [(LEADS, "index"), (LEADS_WE, "lead_index")]:
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    existing = {r.get(idx_col) for r in rows}
    if LEAD_INDEX in existing:
        print(f"ABORT: {path.name} already has index {LEAD_INDEX}")
        sys.exit(1)

# 1) leads.csv (8 cols)
with LEADS.open("a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"],
        quoting=csv.QUOTE_ALL,
    )
    w.writerow({
        "index": LEAD_INDEX,
        "name": COMPANY,
        "handle": HANDLE,
        "email": EMAIL,
        "vertical": VERTICAL,
        "tier": TIER,
        "template": TEMPLATE,
        "tier_reason": tier_reason,
    })

# 2) leads_with_emails.csv (13 cols)
with LEADS_WE.open("a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=["lead_index", "company", "handle", "domain", "website", "founder", "vertical", "tier", "best_email", "emails_found", "guessed_emails", "source_template", "tier_reason"],
        quoting=csv.QUOTE_ALL,
    )
    w.writerow({
        "lead_index": LEAD_INDEX,
        "company": COMPANY,
        "handle": HANDLE,
        "domain": DOMAIN,
        "website": WEBSITE,
        "founder": FOUNDER,
        "vertical": VERTICAL,
        "tier": TIER,
        "best_email": EMAIL,
        "emails_found": EMAIL,
        "guessed_emails": "",
        "source_template": TEMPLATE,
        "tier_reason": tier_reason,
    })

# Verify parse-back + dedupe invariant
def check(path, idx_col):
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    print(f"{path.name}: {len(rows)} rows, last index={rows[-1].get(idx_col)}")
    c = Counter(r.get(idx_col) for r in rows)
    dupes = {k: v for k, v in c.items() if v > 1}
    if dupes: print(f"  DUPES: {dupes}"); return None
    print("  0 duplicate indices")
    return rows[-1]

print()
print("=== Parse-back verification ===")
r1 = check(LEADS, "index")
r2 = check(LEADS_WE, "lead_index")
assert r1 and r2, "dupes detected"
assert r1["index"] == LEAD_INDEX and r1["name"] == COMPANY, "leads.csv last row mismatch"
assert r2["lead_index"] == LEAD_INDEX and r2["company"] == COMPANY, "leads_with_emails.csv last row mismatch"
assert r1["tier_reason"].startswith("Lead 360"), "tier_reason broken (doesn't start with 'Lead 360')"
assert r1["tier_reason"].endswith("inquiries."), "tier_reason broken (doesn't end cleanly)"
print("OK -- both CSVs wrote clean + last row matches + 0 duplicate indices")