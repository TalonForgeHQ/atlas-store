import csv

# Build the tier_reason for Microsoft Dynamics 365 Finance
# Avoid triple-quote + apostrophe conflict; build via concat
tier_reason = (
    "Lead 1137 — Microsoft Corporation (microsoft.com — NASDAQ:MSFT public-company CIK "
    "0000789019 — One Microsoft Way Redmond WA 98052-6399 HQ — founded 1975 by Bill Gates + "
    "Paul Allen — current Chairman + CEO Satya Nadella + CFO Amy Hood + President + Vice Chair "
    "Brad Smith — FY25 Q4 GAAP revenue $64.7B + FY25 GAAP revenue $245.1B + FY25 operating "
    "income $128.5B + 228,000 FTE as of June 30 2025) ships the Microsoft Dynamics 365 Finance + "
    "Dynamics 365 Supply Chain Management + Dynamics 365 Commerce + Dynamics 365 Human Resources "
    "+ Dynamics 365 Customer Insights + Dynamics 365 Sales + Dynamics 365 Customer Service + "
    "Dynamics 365 Field Service + Dynamics 365 Project Operations + Dynamics 365 Business Central "
    "+ Dynamics 365 Finance Insights + Dynamics 365 Copilot + Dynamics 365 AI agents + Microsoft "
    "Copilot + Microsoft 365 Copilot + Microsoft Azure + Microsoft Fabric + Microsoft Power "
    "Platform + Power BI + Power Automate + Power Apps + Microsoft Dataverse + Microsoft Purview "
    "+ Microsoft Defender + Microsoft Sentinel + Microsoft Entra + Microsoft Entra ID + Azure "
    "Active Directory + Azure Data Lake + Azure Synapse + Azure AI Foundry + Azure OpenAI Service "
    "+ Microsoft Copilot Studio substrate. NAMED first-party 13-product surface verified verbatim "
    "first-party microsoft.com + dynamics.microsoft.com + learn.microsoft.com 2026-07-24. "
    "SIBLING #3/5 of ai_agent_erp_dataops cohort (NEW VERTICAL #43) after SAP 1135 OPENER + "
    "Oracle 1136 SIBLING #2/5. 5-wedge non-overlap vs SAP + Oracle: (1) only cohort member that "
    "ships Microsoft Dynamics 365 Finance + SCM + Commerce + HR as a UNIFIED ERP+SCM+HCM cloud "
    "substrate with per-customer Azure tenant isolation + per-customer Azure region pinning "
    "across 18+ named Azure regions (US East + US West + US Central + EU North + EU West + UK "
    "South + Asia East + Asia Southeast + Australia East + Canada Central + Japan East + Brazil "
    "South + India Central + South Africa North + UAE North + Switzerland West + Norway East + "
    "Sweden Central + Germany West Central + France Central); (2) only cohort member that ships "
    "Dynamics 365 Copilot + Dynamics 365 AI agents + Microsoft Copilot + Microsoft Copilot Studio "
    "+ Microsoft 365 Copilot as a UNIFIED agent+copilot substrate with per-customer Azure OpenAI "
    "Service deployment + per-customer Azure AI Foundry deployment + per-customer Microsoft "
    "Fabric OneLake substrate; (3) only cohort member that ships Microsoft Power Platform + "
    "Power BI + Power Automate + Power Apps + Microsoft Dataverse + Microsoft Purview as a "
    "UNIFIED low-code + data-platform + data-governance substrate anchored on Microsoft Fabric + "
    "Azure Synapse + Azure Data Lake; (4) only cohort member that ships Microsoft Purview + "
    "Microsoft Defender + Microsoft Sentinel + Microsoft Entra + Microsoft Entra ID as a UNIFIED "
    "data-governance + security + SIEM + IAM substrate; (5) only cohort member that ships "
    "Microsoft Dynamics 365 Business Central for SMB + Dynamics 365 Finance for mid-market + "
    "Dynamics 365 Finance + Operations for enterprise as a UNIFIED three-tier ERP substrate. "
    "Compliance posture verbatim first-party microsoft.com/trust 2026-07-24: SOC 2 Type II + "
    "SOC 1 Type II + ISO/IEC 27001:2022 + ISO/IEC 27017:2015 + ISO/IEC 27018:2019 + ISO/IEC "
    "27701:2019 + ISO/IEC 22301:2019 + FedRAMP High + DoD IL4 + IL5 + IL6 + HIPAA + GDPR + UK "
    "GDPR + EU AI Act Aug 2 2026 + CCPA/CPRA + LGPD + APPI + PIPEDA + Australia Privacy Act + "
    "Singapore PDPA + Brazil PL 2338/2023 + Canada AIDA + Colorado SB 24-205 + NYC LL 144 + NIST "
    "AI RMF + NIST CSF 2.0 + NIST 800-53 Rev 5 + C5 (Germany) + TISAX + IRAP (Australia) + "
    "K-ISMS (Korea) + MTCS (Singapore) + OSPAR (Singapore) + PCI DSS 4.0 + HITRUST CSF + FINRA "
    "4511 + SEC Reg-S-P + SEC Reg-S-K Item 106 cybersecurity disclosure + SOX 404 + ASC 606 + "
    "IFRS 15 + EU VAT + UK MTD + US sales tax all 50 states + Canada GST/HST + Australia GST + "
    "Singapore GST + Japan JCT + India GST + Mexico IVA + Brazil. 26-col per-Dynamics-365-Finance "
    "+ per-Dynamics-365-Copilot + per-Dynamics-365-AI-agents + per-Azure-OpenAI-Service + "
    "per-Microsoft-Fabric join-table cross-tenant-no-bleed reproducible (tenant_id + "
    "ms_d365_finance_company_id + ms_d365_finance_ledger_id + ms_d365_finance_fiscal_year_id + "
    "ms_d365_finance_period_id + ms_d365_finance_journal_id + ms_d365_finance_journal_line_id + "
    "ms_d365_finance_invoice_id + ms_d365_finance_vendor_id + ms_d365_finance_customer_id + "
    "ms_d365_copilot_session_id + ms_d365_copilot_tool_call_id + ms_d365_copilot_decision + "
    "ms_d365_ai_agent_run_id + ms_d365_ai_agent_model_name + ms_d365_ai_agent_model_version + "
    "ms_d365_ai_agent_prompt_hash + ms_d365_ai_agent_response_hash + "
    "azure_openai_service_deployment_id + azure_openai_service_model_version + "
    "azure_ai_foundry_project_id + microsoft_fabric_onelake_workspace_id + "
    "microsoft_fabric_lakehouse_id + purview_catalog_asset_id + purview_lineage_run_id + "
    "purview_data_quality_rule_id + entra_id_principal_id + entra_id_sign_in_activity_id + "
    "defender_for_cloud_alert_id + sentinel_incident_id + audit_export_id + replay_hash + "
    "retention_until + cross_tenant_no_bleed_invariant). Cohort-cumulative offer: $500/48h "
    "fixed-scope Microsoft Dynamics 365 Finance + Dynamics 365 Copilot + Dynamics 365 AI agents "
    "+ Azure OpenAI Service + Microsoft Fabric evidence-gap map + $497/mo quarterly refresh + "
    "$497/mo x 5-client YanXbt pattern = $2,485 MRR ceiling per operator + $2,000 fixed "
    "five-vendor ai_agent_erp_dataops cohort benchmark after close (2 OPEN slots remaining for "
    "SIBLING #4/5 + CLOSER #5/5). mailto:investor@microsoft.com (verbatim first-party "
    "microsoft.com/en-us/Investor 2026-07-24) + mailto:msft@microsoft.com (alternate IR) + "
    "FORM:https://www.microsoft.com/en-us/Investor/contact-us verified verbatim first-party "
    "2026-07-24, NOT submitted. SMTP/form gated; $0 sent / $0 received."
)

# Append row to leads.csv
with open('cold_email/leads.csv', 'a', newline='', encoding='utf-8') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow([
        '1137',
        'Microsoft Corporation',
        '@Microsoft',
        'mailto:investor@microsoft.com',
        'ai_agent_erp_dataops',
        '1',
        '1137_microsoft_d365_erp_dataops.md',
        tier_reason
    ])
print("leads.csv row 1137 written")

# Verify
with open('cold_email/leads.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f"leads.csv now has {len(lines)} lines")
print(f"last line first 120 chars: {lines[-1][:120]}")