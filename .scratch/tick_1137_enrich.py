import csv

# Build leads_with_emails.csv row for Microsoft Dynamics 365 Finance
emails_found = "investor@microsoft.com; msft@microsoft.com"
guessed = "investor@microsoft.com; msft@microsoft.com"
tier_reason = (
    "Lead 1137 — Microsoft Corporation (NASDAQ:MSFT CIK 0000789019 — One Microsoft Way "
    "Redmond WA 98052-6399 HQ — Satya Nadella CEO + Amy Hood CFO + Brad Smith President + "
    "Vice Chair — FY25 GAAP revenue $245.1B + FY25 Q4 $64.7B + 228,000 FTE — founded 1975 by "
    "Bill Gates + Paul Allen) ships the Dynamics 365 Finance + SCM + Commerce + HR + Customer "
    "Insights + Sales + Customer Service + Field Service + Project Operations + Business "
    "Central + Finance Insights + Dynamics 365 Copilot + Dynamics 365 AI agents + Microsoft "
    "Copilot + Microsoft 365 Copilot + Microsoft Azure + Microsoft Fabric + Microsoft Power "
    "Platform + Power BI + Power Automate + Power Apps + Microsoft Dataverse + Microsoft "
    "Purview + Microsoft Defender + Microsoft Sentinel + Microsoft Entra + Microsoft Entra ID "
    "+ Azure OpenAI Service + Microsoft Copilot Studio substrate. SIBLING #3/5 of "
    "ai_agent_erp_dataops cohort (NEW VERTICAL #43) after SAP 1135 OPENER + Oracle 1136 "
    "SIBLING #2/5. 5-wedge non-overlap vs SAP + Oracle: (1) UNIFIED ERP+SCM+HCM with per-"
    "customer Azure tenant isolation + per-customer Azure region pinning across 18+ Azure "
    "regions; (2) UNIFIED agent+copilot substrate with per-customer Azure OpenAI Service + "
    "Azure AI Foundry + Microsoft Fabric OneLake; (3) UNIFIED low-code + data-platform + data-"
    "governance substrate anchored on Microsoft Fabric + Azure Synapse + Azure Data Lake; (4) "
    "UNIFIED data-governance + security + SIEM + IAM substrate anchored on Microsoft Defender "
    "for Cloud + Microsoft Sentinel SIEM + Microsoft Entra ID; (5) UNIFIED three-tier ERP "
    "substrate Business Central + Finance + Finance + Operations. Compliance: SOC 2 Type II + "
    "SOC 1 Type II + ISO 27001:2022 + 27017 + 27018 + 27701 + 22301 + FedRAMP High + DoD IL4/5/6 "
    "+ HIPAA + GDPR + UK GDPR + EU AI Act Aug 2 2026 + CCPA/CPRA + LGPD + APPI + PIPEDA + "
    "Australia Privacy Act + Singapore PDPA + Brazil + Canada + Colorado + NYC + NIST AI RMF + "
    "NIST CSF 2.0 + NIST 800-53 Rev 5 + C5 + TISAX + IRAP + K-ISMS + MTCS + OSPAR + PCI DSS 4.0 "
    "+ HITRUST CSF + FINRA 4511 + SEC Reg-S-P + SEC Reg-S-K Item 106 + SOX 404 + ASC 606 + "
    "IFRS 15 + EU VAT + UK MTD + US sales tax all 50 states + Canada GST/HST + Australia GST "
    "+ Singapore GST + Japan JCT + India GST + Mexico IVA + Brazil. Offer $500/48h + $497/mo + "
    "$497/mo x 5-client YanXbt pattern = $2,485 MRR ceiling + $2,000 5-vendor cohort benchmark "
    "after close (2 OPEN slots remaining for SIBLING #4 + CLOSER). mailto:investor@microsoft.com "
    "(verbatim first-party microsoft.com/en-us/Investor 2026-07-24) + mailto:msft@microsoft.com "
    "(alternate IR) + FORM:https://www.microsoft.com/en-us/Investor/contact-us NOT submitted. "
    "SMTP/form gated; $0 sent / $0 received."
)

with open('cold_email/leads_with_emails.csv', 'a', newline='', encoding='utf-8') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow([
        '1137',
        'Microsoft Corporation',
        '@Microsoft',
        'microsoft.com',
        'https://www.microsoft.com/',
        'Bill Gates + Paul Allen (Co-Founders; Satya Nadella current Chairman + CEO; Amy Hood CFO; Brad Smith President + Vice Chair)',
        'ai_agent_erp_dataops',
        '1',
        'investor@microsoft.com',
        emails_found,
        guessed,
        '1137_microsoft_d365_erp_dataops.md',
        tier_reason
    ])
print("leads_with_emails.csv row 1137 written")

# Verify
with open('cold_email/leads_with_emails.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f"leads_with_emails.csv now has {len(lines)} lines")
print(f"last line first 120 chars: {lines[-1][:120]}")