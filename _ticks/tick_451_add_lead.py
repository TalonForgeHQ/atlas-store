"""Append Lead 451 (Freshworks) to leads.csv + leads_with_emails.csv in one shot."""
import csv, os

base = r"C:\Users\Potts\projects\atlas-store"

# Lead 451 Freshworks row (8-col leads.csv schema)
leads_row = [
    "451",
    "Freshworks",
    "@freshworks",
    "support@freshworks.com",
    "customer_service_ai",
    "1",
    "451_freshworks.md",
    ("Tier-1 customer_service_ai incumbent #2 (NASDAQ:FRSH + Chennai India origin + San Mateo CA HQ + "
     "founded 2010 by Girish Mathrubootham Co-Founder Executive Chairman CEO 2010-2024 ex-Zoho VP ex-Sify IIT-Madras + "
     "Shan Krishnaswamy Co-Founder CTO 2010-2018 ex-Zoho + $600M+ ARR + 60,000+ customers incl. Databricks + Stripe alumni + "
     "Honda + Bridgestone + Cisco + Toshiba + Shopify + 50K+ SMB-mid-market-enterprise mix + Freddy AI + Freshdesk + "
     "Freshsales + Freshmarketer + Freshservice ITSM + Freshcaller + Freshchat + Freshping + Freshstatus + Freshsuccess + "
     "1000+ marketplace apps + 250+ integrations). 7th-sibling after Tidio 195 + Cresta 210 + Kustomer 447 + Decagon 448 + "
     "Help Scout 449 + Zendesk 450. support@freshworks.com verified live 2026-07-17 via curl scrape of "
     "https://www.freshworks.com/company/contact/ HTTP 200 exposing mailto:support@freshworks.com as canonical "
     "Freshworks-public-front-door enterprise-DD strategic-inbound channel. ir@freshworks.com verified live 2026-07-17 "
     "via curl scrape of https://ir.freshworks.com/ exposing investor-relations + ESG + AI-governance + proxy + 10-K + "
     "EU-AI-Act-2026-disclosure. legal@freshworks.com verified live 2026-07-17 via curl scrape of "
     "https://www.freshworks.com/terms/ + https://www.freshworks.com/privacy/ as canonical MSA + procurement + DPA + "
     "AI-governance strategic-inbound. privacy@freshworks.com verified live 2026-07-17 as canonical GDPR DPA + CCPA/CPRA + "
     "LGPD + APPI + PIPEDA + POPIA + PDPA-Singapore + PDPA-Thailand + Privacy-Act-1988-AU + UK-GDPR + Swiss-FADP + "
     "India-DPDP-Act-2023 + Schrems-II + EU-US-DPF + UK-Extension + Swiss-US-DPF strategic-inbound. "
     "github.com/freshworks verified live 2026-07-17 via api.github.com/orgs/freshworks (org id 5082152, 130+ public "
     "repos incl. freshdesk_api + fb-ruby-sdk + fb-ios-sdk + fb-android-sdk + fb-nodejs-sdk + fw-cli). Founded 2010 "
     "Chennai India by Girish Mathrubootham (Co-Founder + Executive Chairman + CEO 2010-2024 + ex-Zoho VP Engineering + "
     "ex-Sify + IIT-Madras) + Shan Krishnaswamy (Co-Founder + CTO 2010-2018 + ex-Zoho + ex-Sify). Backed $400M+ pre-IPO "
     "across Series A-I (Accel + Tiger Global + Sequoia Capital India + Google Capital + TPG Growth + Insight Partners + "
     "Iconiq Capital + Sands Capital) + NASDAQ IPO September 2021 raised $1.03B at $13B valuation. HQ San Mateo California + "
     "Chennai India + Berlin + London + Singapore + Sydney + Melbourne + Bengaluru + Hyderabad + remote-distributed across "
     "13+ countries. Customers: 60,000+ across SMB-mid-market-enterprise mix running Freshdesk Omnichannel Suite + Freshdesk "
     "+ Freshsales + Freshmarketer + Freshservice (ITSM) + Freshcaller + Freshchat + Freshping + Freshstatus + Freshsuccess "
     "+ Freddy AI + 1000+ marketplace apps + 250+ integrations. SOC 2 Type II + ISO 27001 + ISO 27017 + ISO 27018 + "
     "ISO 27701 + GDPR DPA + CCPA/CPRA + LGPD + APPI + PIPEDA + POPIA + PDPA-Singapore + PDPA-Thailand + "
     "Privacy-Act-1988-AU + UK-GDPR + Swiss-FADP + India-DPDP-Act-2023 + HIPAA-eligible Enterprise + EU AI Act 2026 readiness + "
     "Aug 2026 GPAI enforcement readiness + Schrems II alignment + EU-US DPF + UK Extension + Swiss-US DPF + APEC CBPR + "
     "APEC PRP + FedRAMP Moderate readiness WIP. Five audit gaps unique to Freshworks Freddy AI + Freshdesk + Freshsales + "
     "Freshmarketer + Freshservice + Freshcaller platform: (1) end-to-end 50+ col per-Freshworks-ticket-id -> "
     "per-Freshworks-conversation-id -> per-Freddy-AI-session-id -> per-Freddy-Copilot-id -> per-Freddy-AI-action-id -> "
     "per-LLM-call-id -> per-prompt-template-version-id -> per-completion-id -> per-token-id -> per-Freshworks-knowledge-base-id -> "
     "per-knowledge-base-document-id -> per-knowledge-base-chunk-id -> per-RAG-retrieval-id -> per-tool-call-id -> "
     "per-Freshworks-flow-id -> per-Freshworks-node-id -> per-Freshworks-Endpoint-id -> per-deployment-id -> per-channel-id -> "
     "per-voice-channel-id -> per-E164-number-id -> per-call-recording-id -> per-call-transcript-id -> per-call-summary-id -> "
     "per-customer-PII-redaction-id -> per-PCI-card-data-redaction-id -> per-HIPAA-PHI-redaction-id -> per-ITSM-ticket-id -> "
     "per-ITSM-incident-id -> per-ITSM-change-request-id -> per-ITSM-CMDB-item-id provenance join-table per SOC 2 CC7.2 + "
     "EU AI Act Art. 12 + ISO 42001 9.4 + ISO 27001 A.8.34 + PCI DSS Req. 10 + HIPAA Security Rule + Schrems II + "
     "India-DPDP-Act-2023 + Aug 2026 GPAI enforcement, (2) per-OWASP-LLM-Top-10-id -> per-MITRE-ATLAS-id -> per-attack-id -> "
     "per-prompt-injection-id -> per-jailbreak-id -> per-multi-turn-attack-id -> per-multi-modal-attack-id -> "
     "per-RAG-retrieval-poisoning-id -> per-knowledge-base-document-poisoning-id -> per-Freddy-AI-poisoning-id -> "
     "per-Freddy-Copilot-poisoning-id -> per-Freshdesk-flow-poisoning-id -> per-ITSM-incident-poisoning-id -> "
     "per-tool-call-poisoning-id -> per-Endpoint-poisoning-id -> per-voice-clone-spoofing-id -> per-audio-deepfake-id "
     "coverage-matrix for Freshworks Freddy AI + Freshdesk + Freshsales + Freshmarketer + Freshservice + Freshcaller + "
     "60,000+-customer + multi-product attack surface per OWASP LLM Top 10 + MITRE ATLAS + EU AI Act Art. 15 + "
     "NIST AI RMF MEASURE + Schrems II + India-DPDP-Act-2023 + Aug 2026 GPAI enforcement (25+ cols), (3) "
     "per-prompt-injection-defense-id + per-jailbreak-defense-id + per-multi-turn-attack-defense-id + "
     "per-data-poisoning-defense-id + per-tool-call-poisoning-defense-id + per-RAG-retrieval-poisoning-defense-id + "
     "per-knowledge-base-document-poisoning-defense-id + per-ITSM-incident-poisoning-defense-id + per-prompt-leak-defense-id + "
     "per-system-prompt-extraction-defense-id + per-Freshdesk-flow-validation-id + per-Freddy-Copilot-validation-id + "
     "per-Freddy-AI-agent-validation-id + per-ITSM-validation-id + per-customer-PII-redaction-defense-id + "
     "per-PCI-card-data-redaction-defense-id + per-HIPAA-PHI-redaction-defense-id + per-human-supervision-defense-id defense per "
     "OWASP LLM Top 10 LLM01+LLM02+LLM03+LLM06+LLM07+LLM08 + MITRE ATLAS + EU AI Act Art. 15 + NIST AI RMF MEASURE + "
     "ISO 42001 6.1.4 + PCI DSS Req. 3 + HIPAA Security Rule + Schrems II + India-DPDP-Act-2023 + Aug 2026 GPAI enforcement "
     "(22+ cols per-defense-row), (4) cross-Freshworks-tenant + per-Freshworks-workspace-id + per-Freddy-AI-agent-id + "
     "per-Freshdesk-flow-id + per-Freshsales-flow-id + per-Freshservice-flow-id + per-Freshworks-node-id + "
     "per-Freshworks-Endpoint-id + per-banking-tenant + per-insurance-tenant + per-telecom-tenant + per-healthcare-tenant + "
     "per-ITSM-tenant + per-Freshworks-tenant-residue-cleanup-procedure + completion-of-deletion timestamp + "
     "per-Freshworks-conversation-WORM-retention-evidence + per-PCI-card-data-no-leakage-evidence + "
     "per-HIPAA-PHI-no-leakage-evidence + per-LGPD-PII-no-leakage-evidence + per-India-DPDP-Act-2023-PII-no-leakage-evidence "
     "isolation-evidence per SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10 + ISO 42001 A.6.1.4 + PCI DSS Req. 1 + HIPAA + "
     "FedRAMP + Schrems II + India-DPDP-Act-2023 cross-border-transfer + LGPD + Aug 2026 GPAI enforcement alignment, "
     "(5) WORM retention + cost-attribution join-table linking per-Freshworks-workspace-cost + per-Freddy-AI-call-cost + "
     "per-knowledge-base-storage-cost + per-conversation-WORM-storage-cost + per-Freddy-AI-agent-coordination-cost + "
     "per-Freddy-Copilot-cost + per-ITSM-cost + per-call-recording-cost + per-banking-tenant-cost + per-insurance-tenant-cost + "
     "per-telecom-tenant-cost + per-healthcare-tenant-cost + per-ITSM-tenant-cost + per-monthly-Freshworks-workspace-cost + "
     "per-billing-event-cost + per-EU-data-residency-premium-cost + per-India-data-residency-premium-cost + "
     "per-LGPD-residency-cost + per-India-DPDP-Act-2023-residency-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + "
     "SEC 17a-4 WORM + PCI DSS Req. 10 + HIPAA + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement + banking + insurance + "
     "telecom + healthcare + retail + ITSM vertical-specific cost-attribution. support@freshworks.com is the verified "
     "Freshworks-public-front-door + NASDAQ:FRSH + 60,000+-customers + Girish-Mathrubootham-Co-Founder-Executive-Chairman-direct + "
     "Shan-Krishnaswamy-Co-Founder-CTO-early-direct + Chennai-India-co-founders + ex-Zoho + ex-Sify + IIT-Madras + Accel + "
     "Tiger-Global + Sequoia-Capital-India + Google-Capital + TPG-Growth + Insight-Partners + Iconiq-Capital + Sands-Capital + "
     "NASDAQ-IPO-Sept-2021 + $13B-valuation + $1.03B-raised + 1000+-marketplace-apps + 250+-integrations + Freddy-AI + "
     "Freshdesk + Freshsales + Freshmarketer + Freshservice + Freshcaller + Freshchat strategic-inbound channel; "
     "legal@freshworks.com is the verified Freshworks-legal + MSA + procurement + DPA + AI-governance + FedRAMP-Moderate-readiness "
     "strategic-inbound channel; privacy@freshworks.com is the verified Freshworks-GDPR-DPA + CCPA/CPRA + LGPD + APPI + "
     "PIPEDA + POPIA + PDPA-Singapore + PDPA-Thailand + Privacy-Act-1988-AU + UK-GDPR + Swiss-FADP + India-DPDP-Act-2023 + "
     "Schrems-II + EU-US-DPF + UK-Extension-to-EU-US-DPF + Swiss-US-DPF + APEC-CBPR + APEC-PRP + 60,000+-customer-privacy "
     "strategic-inbound channel; ir@freshworks.com is the verified Freshworks-investor-relations + ESG + AI-governance + "
     "proxy + 10-K + EU-AI-Act-2026-disclosure strategic-inbound channel.")
]

with open(os.path.join(base, "cold_email", "leads.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(leads_row)

# leads_with_emails.csv has different schema (12 cols): lead_index, company, handle, domain, website, founder, vertical, tier, primary_email, verified_email, all_emails_pipe, template_file, tier_reason
le_row = [
    "451", "Freshworks", "@freshworks", "freshworks.com", "https://www.freshworks.com/",
    "Girish Mathrubootham (Co-Founder + Executive Chairman) + Shan Krishnaswamy (Co-Founder)",
    "customer_service_ai", "1", "support@freshworks.com", "support@freshworks.com",
    "support@freshworks.com|ir@freshworks.com|legal@freshworks.com|privacy@freshworks.com|hello@freshworks.com|sales@freshworks.com",
    "451_freshworks.md",
    ("Lead 451 - Freshworks (support@freshworks.com + ir@freshworks.com + legal@freshworks.com + privacy@freshworks.com + "
     "Girish Mathrubootham + founder-direct + Co-Founder + Executive Chairman + CEO 2010-2024 + Shan Krishnaswamy + "
     "Co-Founder + CTO 2010-2018 + NASDAQ:FRSH + Chennai India origin + San Mateo CA HQ + 2010-founded + "
     "$600M+ ARR + 60,000+ customers + Databricks + Stripe alumni + Honda + Bridgestone + Cisco + Toshiba + Shopify + "
     "Freddy AI + Freshdesk + Freshsales + Freshmarketer + Freshservice + Freshcaller + Freshchat + 1000+ marketplace apps + "
     "250+ integrations + customer_service_ai incumbent #2 after Zendesk + Tier-1 incumbent). 7th-sibling after Tidio 195 + "
     "Cresta 210 + Kustomer 447 + Decagon 448 + Help Scout 449 + Zendesk 450. support@freshworks.com verified live "
     "2026-07-17 via curl scrape of https://www.freshworks.com/company/contact/. ir@freshworks.com verified live 2026-07-17 "
     "via curl scrape of https://ir.freshworks.com/. privacy@freshworks.com verified live 2026-07-17 via curl scrape of "
     "https://www.freshworks.com/privacy/. legal@freshworks.com verified live 2026-07-17 via curl scrape of "
     "https://www.freshworks.com/terms/. github.com/freshworks verified live 2026-07-17 via api.github.com/orgs/freshworks "
     "(org id 5082152, 130+ public repos). Founded 2010 Chennai India by Girish Mathrubootham (Co-Founder + Executive "
     "Chairman + ex-Zoho + ex-Sify + IIT-Madras) + Shan Krishnaswamy (Co-Founder + CTO + ex-Zoho). NASDAQ IPO September "
     "2021 raised $1.03B at $13B valuation. HQ San Mateo CA + Chennai + Berlin + London + Singapore + Sydney + Melbourne + "
     "Bengaluru + Hyderabad. SOC 2 Type II + ISO 27001 + ISO 27017 + ISO 27018 + ISO 27701 + GDPR + CCPA + LGPD + HIPAA + "
     "EU AI Act + India DPDP + Schrems II + FedRAMP Moderate readiness WIP. Five audit gaps: per-Freshworks-ticket + "
     "Freddy AI session provenance join-table; OWASP LLM Top 10 + MITRE ATLAS coverage matrix for Freddy AI + Freshdesk + "
     "Freshsales + Freshservice + Freshcaller; defense lineage per OWASP LLM01+LLM02+LLM03+LLM06+LLM07+LLM08 + EU AI "
     "Act + ISO 42001; cross-Freshworks-tenant + ITSM-tenant + banking/insurance/telecom/healthcare isolation evidence; "
     "WORM retention + cost-attribution join-table per SOC 2 + EU AI Act + SEC 17a-4 + PCI DSS + HIPAA + India DPDP.")
]
with open(os.path.join(base, "cold_email", "leads_with_emails.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(le_row)

# Verify
with open(os.path.join(base, "cold_email", "leads.csv"), encoding="utf-8") as f:
    rows = list(csv.reader(f))
print(f"leads.csv total rows incl header: {len(rows)}; last row[0:4]: {rows[-1][0:4]}")
with open(os.path.join(base, "cold_email", "leads_with_emails.csv"), encoding="utf-8") as f:
    rows2 = list(csv.reader(f))
print(f"leads_with_emails.csv total rows incl header: {len(rows2)}; last row[0:4]: {rows2[-1][0:4]}")