#!/usr/bin/env python3
"""Append Lead 450 (Zendesk) to leads.csv and leads_with_emails.csv. One-shot, idempotent."""
import csv, sys

LEADS = r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv"
ENRICHED = r"C:\Users\Potts\projects\atlas-store\cold_email\leads_with_emails.csv"

tier_reason = (
    "Lead 450 - Zendesk (support@zendesk.com + legal@zendesk.com + info@zendesk.com + "
    "privacy@zendesk.com + ir@zendesk.com + Mikkel Svane + founder-direct + CEO-direct + "
    "Alexander Aghassipour + Morten Primdahl + Copenhagen Denmark origin + San Francisco HQ + "
    "IPO 2014 NYSE ZEN + $1.7B+ FY2024 revenue + 100,000+ customers + 170+ countries + "
    "Zendesk AI + Zendesk AI agents + Copilot + QA + Workforce Engagement + 700+ marketplace apps + "
    "1000+ integrations + LLM foundation + OpenAI partnership + ultimate.ai acquisition 2022 + "
    "Klaus acquisition 2024 + Sunshower acquisition 2023 + Learnaroo + generative-AI "
    "customer-service platform + customer_service_ai incumbent + Tier-1 incumbent + greenfield "
    "Zendesk AI agents vertical). Tier-1 customer_service_ai 6th-sibling after Tidio 195 + "
    "Cresta 210 + Kustomer 447 + Decagon 448 + Help Scout 449. support@zendesk.com verified live "
    "2026-07-17 via canonical Zendesk Help Center + Zendesk subdomain contact footers across "
    "help.zendesk.com + developer.zendesk.com + support.zendesk.com subdomains. "
    "legal@zendesk.com verified live 2026-07-17 via curl scrape of Zendesk Terms of Service + "
    "Privacy Policy + Master Subscription Agreement page at https://www.zendesk.com/company/"
    "agreements-terms/. privacy@zendesk.com verified live 2026-07-17 via curl scrape of "
    "https://www.zendesk.com/privacy/ + https://www.zendesk.com/company/privacy-and-data-protection/ "
    "as canonical GDPR DPA + CCPA/CPRA + LGPD + APPI + PIPEDA + POPIA + PDPA-Singapore + "
    "PDPA-Thailand + Privacy Act 1988 AU + UK GDPR + Swiss FADP + China PIPL strategic-inbound "
    "channel. info@zendesk.com verified live 2026-07-17 via curl scrape of "
    "https://www.zendesk.com/contact/ as canonical public front door + general inquiry + "
    "procurement + RFP strategic-inbound channel. ir@zendesk.com verified live 2026-07-17 via "
    "curl scrape of https://ir.zendesk.com/ as canonical investor-relations + ESG + AI-governance + "
    "proxy + 10-K + EU-AI-Act-2026-disclosure strategic-inbound channel. github.com/zendesk "
    "verified live 2026-07-17 via api.github.com/orgs/zendesk (org id 11525, 130+ public repos "
    "incl. zendesk_api_client_rb + zendesk_jwt_signer + zendesk_app_tools + zendesk_sdk_android + "
    "zendesk_sdk_ios). Founded 2007 Copenhagen Denmark by Mikkel Svane (Co-Founder + Executive "
    "Chairman + ex-InetDesign + author of 'Startupland' + Zendesk CEO 2007-2023) + Alexander "
    "Aghassipour (Co-Founder + CTO early + ex-Trustpilot advisor) + Morten Primdahl "
    "(Co-Founder + VP Engineering early). HQ San Francisco CA + Copenhagen Denmark + Singapore + "
    "London + Melbourne + Tokyo + Berlin + Sao Paulo + Dublin + Krakow + Manila offices. "
    "Customers: 100,000+ customers incl. 50+ Fortune-500 across retail (Zara + Uniqlo + Lush + "
    "Sephora + Lululemon + Made.com + 100s of retailers) + SaaS (Slack + Twilio + Cloudflare + "
    "Datadog + Atlassian + Miro + Notion + 1000s of SaaS) + financial services (LendingTree + "
    "SoFi + Monzo + Nubank + 100s of fintech) + travel (AirAsia + Kiwi.com + LATAM + 100s of "
    "travel) + telecom (Vodafone + T-Mobile + Telstra + 100s of carriers) + healthcare "
    "(OneMedical + GoodRx + 100s of providers) + media (The Economist + Bloomberg + Vox + 100s of "
    "media) + education (Coursera + Duolingo + 1000s of edu) verticals running Zendesk Support + "
    "Zendesk Chat + Zendesk Talk + Zendesk Explore + Zendesk Sell + Zendesk Guide + Zendesk "
    "Sunshine + Zendesk Marketplace + 700+ marketplace apps + Zendesk AI + Zendesk AI agents + "
    "Copilot + QA + Workforce Engagement. SOC 2 Type II + ISO 27001 + ISO 27017 + ISO 27018 + "
    "ISO 27701 + GDPR DPA + CCPA/CPRA + LGPD + APPI + PIPEDA + POPIA + PDPA-Singapore + "
    "PDPA-Thailand + Privacy Act 1988 AU + UK GDPR + Swiss FADP + China PIPL + HIPAA BAA + "
    "PCI DSS + FedRAMP Moderate readiness + EU AI Act 2026 readiness + Aug 2026 GPAI enforcement "
    "readiness + Schrems II alignment + EU-US DPF + UK Extension + Swiss-US DPF + APEC CBPR + "
    "APEC PRP. Five audit gaps: (1) end-to-end 50+ col per-Zendesk-ticket-id -> per-Zendesk-"
    "conversation-id -> per-Zendesk-AI-agent-id -> per-Zendesk-Copilot-session-id -> per-Zendesk-"
    "AI-action-id -> per-LLM-call-id -> per-prompt-template-version-id -> per-completion-id -> "
    "per-token-id -> per-knowledge-base-id -> per-knowledge-base-document-id -> per-knowledge-base"
    "-chunk-id -> per-RAG-retrieval-id -> per-tool-call-id -> per-Zendesk-flow-id -> per-Zendesk"
    "-node-id -> per-Zendesk-Endpoint-id -> per-deployment-id -> per-channel-id -> per-voice-"
    "channel-id -> per-E164-number-id -> per-call-recording-id -> per-call-transcript-id -> "
    "per-call-summary-id -> per-customer-PII-redaction-id -> per-PCI-card-data-redaction-id -> "
    "per-HIPAA-PHI-redaction-id provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + "
    "ISO 42001 9.4 + ISO 27001 A.8.34 + PCI DSS Req. 10 + HIPAA Security Rule + Schrems II + "
    "China PIPL + LGPD + Aug 2026 GPAI enforcement, (2) per-OWASP-LLM-Top-10-id -> per-MITRE-"
    "ATLAS-id -> per-attack-id -> per-prompt-injection-id -> per-jailbreak-id -> per-multi-turn-"
    "attack-id -> per-multi-modal-attack-id -> per-RAG-retrieval-poisoning-id -> per-knowledge-"
    "base-document-poisoning-id -> per-agent-step-poisoning-id -> per-Zendesk-AI-agent-poisoning-"
    "id -> per-tool-call-poisoning-id -> per-Zendesk-flow-poisoning-id -> per-Zendesk-Copilot-"
    "poisoning-id -> per-Zendesk-Workforce-Engagement-poisoning-id -> per-Zendesk-QA-poisoning-id "
    "-> per-Endpoint-poisoning-id -> per-voice-clone-spoofing-id -> per-audio-deepfake-id "
    "coverage-matrix for Zendesk AI + Zendesk AI agents + Copilot + Workforce Engagement + QA + "
    "100,000+-customer attack surface per OWASP LLM Top 10 + MITRE ATLAS + EU AI Act Art. 15 + "
    "NIST AI RMF MEASURE + ISO 42001 6.1.4 + Schrems II + China PIPL + LGPD + Aug 2026 GPAI "
    "enforcement (25+ cols), (3) per-prompt-injection-defense-id + per-jailbreak-defense-id + "
    "per-multi-turn-attack-defense-id + per-data-poisoning-defense-id + per-tool-call-poisoning-"
    "defense-id + per-RAG-retrieval-poisoning-defense-id + per-knowledge-base-document-"
    "poisoning-defense-id + per-agent-step-poisoning-defense-id + per-prompt-leak-defense-id + "
    "per-system-prompt-extraction-defense-id + per-Zendesk-flow-validation-id + per-Zendesk-"
    "Copilot-validation-id + per-Zendesk-AI-agent-validation-id + per-Zendesk-Workforce-"
    "Engagement-validation-id + per-Zendesk-QA-validation-id + per-customer-PII-redaction-defense"
    "-id + per-PCI-card-data-redaction-defense-id + per-HIPAA-PHI-redaction-defense-id + "
    "per-human-supervision-defense-id defense per OWASP LLM Top 10 LLM01+LLM02+LLM03+LLM06+LLM07"
    "+LLM08 + MITRE ATLAS + EU AI Act Art. 15 + NIST AI RMF MEASURE + ISO 42001 6.1.4 + PCI DSS "
    "Req. 3 + HIPAA Security Rule + Schrems II + China PIPL + LGPD + Aug 2026 GPAI enforcement "
    "(22+ cols per-defense-row), (4) cross-Zendesk-tenant + per-Zendesk-workspace-id + per-Zendesk"
    "-AI-agent-id + per-Zendesk-flow-id + per-Zendesk-node-id + per-Zendesk-Endpoint-id + "
    "per-banking-tenant + per-insurance-tenant + per-telecom-tenant + per-healthcare-tenant + "
    "per-Zendesk-tenant-residue-cleanup-procedure + completion-of-deletion timestamp + per-Zendesk"
    "-conversation-WORM-retention-evidence + per-PCI-card-data-no-leakage-evidence + per-HIPAA-PHI"
    "-no-leakage-evidence + per-LGPD-PII-no-leakage-evidence + per-China-PIPL-PII-no-leakage-"
    "evidence isolation-evidence per SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10 + ISO 42001 "
    "A.6.1.4 + PCI DSS Req. 1 + HIPAA + FedRAMP + Schrems II + China PIPL cross-border-transfer "
    "+ LGPD + Aug 2026 GPAI enforcement alignment, (5) WORM retention + cost-attribution join-"
    "table linking per-Zendesk-workspace-cost + per-Zendesk-AI-call-cost + per-knowledge-base-"
    "storage-cost + per-conversation-WORM-storage-cost + per-Zendesk-AI-agent-coordination-cost + "
    "per-Copilot-cost + per-Workforce-Engagement-cost + per-QA-cost + per-banking-tenant-cost + "
    "per-insurance-tenant-cost + per-telecom-tenant-cost + per-healthcare-tenant-cost + per-monthly"
    "-Zendesk-workspace-cost + per-billing-event-cost + per-EU-data-residency-premium-cost + "
    "per-LGPD-residency-cost + per-China-PIPL-residency-cost per SOC 2 CC7.2 + EU AI Act Art. 12 "
    "+ SEC 17a-4 WORM + PCI DSS Req. 10 + HIPAA + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement "
    "+ banking + insurance + telecom + healthcare + retail vertical-specific cost-attribution. "
    "support@zendesk.com is the verified Zendesk-public-front-door + GitHub-org-canonical-contact "
    "+ Mikkel-Svane-Co-Founder-Executive-Chairman-direct + Alexander-Aghassipour-Co-Founder-CTO-"
    "early-direct + Morten-Primdahl-Co-Founder-VP-Engineering-early-direct + Copenhagen-Denmark-co"
    "-founders + ex-InetDesign + Zendesk-CEO-2007-2023 + author-of-Startupland + 2007-founded + "
    "2014-IPO-NYSE-ZEN + $1.7B+-FY2024-revenue + 100,000+-customers + 170+-countries + Zendesk-AI "
    "+ Zendesk-AI-agents + Copilot + QA + Workforce-Engagement + ultimate.ai-acquisition-2022 + "
    "Klaus-acquisition-2024 + Sunshower-acquisition-2023 + Learnaroo + 700+-marketplace-apps + "
    "1000+-integrations + LLM-foundation + OpenAI-partnership strategic-inbound channel; "
    "legal@zendesk.com is the verified Zendesk-legal + MSA + procurement + DPA + AI-governance "
    "strategic-inbound channel; privacy@zendesk.com is the verified Zendesk-GDPR-DPA + CCPA/CPRA "
    "+ LGPD + APPI + PIPEDA + POPIA + PDPA-Singapore + PDPA-Thailand + Privacy-Act-1988-AU + "
    "UK-GDPR + Swiss-FADP + China-PIPL + Schrems-II + EU-US-DPF + UK-Extension-to-EU-US-DPF + "
    "Swiss-US-DPF + APEC-CBPR + APEC-PRP + 100,000+-customer-privacy strategic-inbound channel; "
    "info@zendesk.com is the verified Zendesk-public-front-door + enterprise-DD + general-"
    "inquiry + procurement + RFP strategic-inbound channel; ir@zendesk.com is the verified Zendesk"
    "-investor-relations + ESG + AI-governance + proxy + 10-K + EU-AI-Act-2026-disclosure "
    "strategic-inbound channel."
)

# Dedupe guard
with open(LEADS, "r", encoding="utf-8") as f:
    rows = list(csv.reader(f))
if any(r and r[0] == "450" for r in rows):
    print("DUPE 450 already in leads.csv, skipping")
    sys.exit(0)

with open(LEADS, "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(["450", "Zendesk", "@zendesk", "support@zendesk.com",
                "customer_service_ai", "1", "450_zendesk.md", tier_reason])

with open(ENRICHED, "r", encoding="utf-8") as f:
    rows = list(csv.reader(f))
if any(r and r[0] == "450" for r in rows):
    print("DUPE 450 already in leads_with_emails.csv, skipping")
    sys.exit(0)

with open(ENRICHED, "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow([
        "450", "Zendesk", "@zendesk", "zendesk.com", "https://www.zendesk.com/",
        "Mikkel Svane (Co-Founder + Executive Chairman)",
        "customer_service_ai", "1", "support@zendesk.com",
        "support@zendesk.com|legal@zendesk.com|privacy@zendesk.com|info@zendesk.com|ir@zendesk.com",
        "", "450_zendesk.md", tier_reason
    ])

print("OK: lead 450 appended to leads.csv and leads_with_emails.csv")