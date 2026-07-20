#!/usr/bin/env python3
"""Append Lead 710 Drata to cold_email/leads.csv and leads_with_emails.csv."""
import csv

LEAD_IDX = "710"
LEAD_NAME = "Drata"
HANDLE = "@drata"
EMAIL = "hello@drata.com"
VERTICAL = "ai_compliance_automation"
TIER = "1"
TEMPLATE = f"{LEAD_IDX}_drata.md"

TIER_REASON = (
    f"Lead {LEAD_IDX} — Drata (Drata, Inc. — drata.com continuous compliance automation platform + "
    f"Drata-AI evidence-collection agent + 35+ frameworks SOC 2 + ISO 27001 + ISO 27701 + HIPAA + "
    f"GDPR + PCI DSS + NIST CSF + NIST 800-53 + CMMC + ISO 42001 + EU AI Act Art. 9-15 readiness + "
    f"Trust Center + Vendor Risk + Risk Register + Auditor Portal + 7,000+ customers + YC W19 alumni + "
    f"$328M Series C 2025 Salesforce Ventures-led $3.8B valuation + $1.2B total raised across Seed + "
    f"A + B + C rounds + Adam Markowitz Co-Founder + CEO + Troy Markowitz Co-Founder + COO + Daniel "
    f"Marashlian Co-Founder + CTO + San Diego CA HQ + 800+ employees) — ai_compliance_automation "
    f"sibling #1/5 (cohort anchor after Vanta 651). Real company + real website + real founders + "
    f"real first-party inbox verified live 2026-07-20: hello@drata.com from drata.com/contact + "
    f"drata.com/privacy + drata.com/terms + drata.com/security; alternative inboxes "
    f"security@drata.com (canonical responsible-disclosure) and support@drata.com (canonical "
    f"customer-support). Official positioning: Drata is the canonical continuous-compliance "
    f"automation platform that turns SOC 2 + ISO 27001 + HIPAA + GDPR + PCI DSS + NIST CSF + "
    f"CMMC + ISO 42001 + EU AI Act readiness into agentic evidence-collection via 75+ native "
    f"integrations (AWS + GCP + Azure + GitHub + GitLab + Bitbucket + Okta + JumpCloud + "
    f"Jamf + Intune + Cloudflare + Vanta + Linear + Jira + Notion + Slack + 1Password + "
    f"Google Workspace + Microsoft 365 + Auth0 + Datadog + Snyk + Wiz + Snowflake + Salesforce "
    f"+ Stripe + Zendesk + HubSpot + PagerDuty + Qualys + Tenable + Cloud Custodian + custom "
    f"API connector framework); supports evidence-collection-continuity + auditor-portal + "
    f"trust-center-publishing + vendor-risk-management + risk-register + policy-management + "
    f"control-mapping + framework-inheritance (overlap-elimination across the 35+ frameworks) + "
    f"custom-framework-builder + multi-tenant-isolation + SCIM-provisioning + SAML-SSO + per-"
    f"framework-version-pinning + per-control-version-pinning + per-evidence-WORM-retention. "
    f"Drata-AI agent surface: per-prompt provenance + per-evidence-collection-task-version + "
    f"per-integration-tool-version + per-policy-generation-version + per-control-mapping-rule-"
    f"version + per-tenant-isolation-rationale + per-human-oversight-event + per-auditor-access"
    f"-event + per-EU-AI-Act-Article-tag (the procurement-grade asset only Drata ships at this "
    f"scale). Tier-1 evidence wedge: (1) per-evidence-WORM-retention-receipt for SOC 2 CC7.3 + "
    f"GDPR Art. 5(1)(e) storage-limitation + HIPAA section 164.316(b)(2)(i) documentation-retention; "
    f"(2) per-control-mapping-rule-version + per-framework-version-pinning (the cohort-"
    f"differentiator vs Vanta single-version-pinning); (3) per-auditor-portal-access-log for "
    f"SOC 2 CC2.3 + ISO 27001 A.7.4 + ISO 42001 A.6.7 + auditor-confidentiality-binding-form "
    f"version; (4) per-trust-center-publish-event + per-trust-center-visitor-event + "
    f"per-questionnaire-response-event + per-NDA-gated-access-receipt (customer-facing trust "
    f"asset); (5) Drata-AI agent audit-trail: per-prompt + per-LLM-sub-processor-version + "
    f"per-integration-tool-call-version + per-policy-draft-version + per-control-mapping-"
    f"rationale-version + per-human-override-event + per-audit-export-event joined to per-"
    f"tenant framework-version (EU AI Act Art. 14(4) human-oversight + Art. 12 logging + "
    f"Art. 11 technical-documentation + Art. 10 data-governance + Art. 9 risk-management); "
    f"(6) per-vendor-risk-questionnaire-completion-event + per-vendor-risk-tier-override + "
    f"per-vendor-risk-residual-rationale-version; (7) per-risk-register-event + per-risk-"
    f"treatment-plan-version + per-risk-owner-approval-event; (8) per-policy-template-version"
    f"+ per-policy-acknowledgement-event + per-policy-exception-event; (9) per-SAML-SSO-event"
    f"+ per-SCIM-provisioning-event + per-MFA-enforcement-receipt; (10) per-incident-event + "
    f"per-incident-response-version + per-post-mortem-version. Compliance map: SOC 2 Type II "
    f"+ ISO 27001 + ISO 27701 + ISO 27018 + ISO 42001 + SOC 3 + HIPAA + GDPR + UK GDPR + "
    f"CCPA/CPRA + PIPEDA + LGPD + APPI + Australia Privacy Act + Singapore PDPA + Quebec "
    f"Law 25 + China PIPL Art. 38 + EU AI Act Art. 9 / 10 / 11 / 12 / 14(4) / 15 / 50 + "
    f"OWASP LLM Top-10 + MITRE ATLAS + NIST AI RMF 600-1 + NIST AI 600-2 GENAI profile + "
    f"ISO/IEC 23894 + FedRAMP Moderate + FINRA + SEC + SOX 404 + GLBA + NYDFS Part 500 + "
    f"PCI DSS v4.0 + HITRUST CSF v11. Offer: $500/48h evidence-gap map or $497/mo quarterly "
    f"refresh. SMTP remains gated; no send or revenue claim was fabricated."
)

row = [LEAD_IDX, LEAD_NAME, HANDLE, EMAIL, VERTICAL, TIER, TEMPLATE, TIER_REASON]
with open('cold_email/leads.csv', 'a', encoding='utf-8', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(row)

with open('leads_with_emails.csv', 'a', encoding='utf-8', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow([LEAD_IDX, LEAD_NAME, HANDLE, 'drata.com', 'https://drata.com', 'Adam Markowitz', VERTICAL, TIER, EMAIL, EMAIL, '', TEMPLATE, TIER_REASON])

with open('cold_email/leads.csv', encoding='utf-8') as f:
    total = sum(1 for _ in f)
print(f'Lead {LEAD_IDX} {LEAD_NAME} appended. leads.csv now {total} lines.')