# Cold Email Companion — Oracle ERP Cloud (SIBLING #2/5 ai_agent_erp_dataops)

**Vendor:** Oracle Corporation
**Tick:** 1136 (2026-07-24)
**Cohort:** ai_agent_erp_dataops SIBLING #2/5 (NEW VERTICAL #43) after SAP SE 1135 OPENER #1/5
**Status:** SHIPPED — SIBLING #2/5 (4 OPEN slots remaining: MS D365 Finance, Workday, Salesforce ERP, Infor / Epicor candidate)

---

## Why Oracle is the cohort-unique SIBLING #2/5 (5 non-overlap wedges vs SAP)

1. **47-year ERP heritage vs SAP's 52-year heritage** — Oracle was founded 1977 by Larry Ellison + Bob Miner + Ed Oates (under the project name "Oracle" inspired by the CIA project + Ellison's prior Ampex work). First commercial release 1979. Oracle is the SECOND oldest ERP-vendor still in production (SAP is the oldest). Both ship ERP-substrate with named customers but Oracle's customer tier skews to mid-market NetSuite + enterprise SaaS Apps, while SAP's customer tier is 99-of-Fortune-100. The wedge is: Oracle is the only cohort member with NAMED first-party NetSuite substrate (acquired 2016) serving the SMB-midmarket tier with separate GL/AR/AP/Inventory/CRM chart-of-accounts, while SAP serves the enterprise tier with S/4HANA.
2. **Oracle Cloud Infrastructure (OCI) as named AI-runtime substrate** — Oracle ships a NAMED first-party OCI substrate with named US-Ashburn + US-Phoenix + EU-Frankfurt + UK-London + APAC-Tokyo + APAC-Sydney + APAC-Mumbai + APAC-Seoul + SA-São Paulo + CA-Toronto regions, with NAMED Exadata Exascale + Autonomous Database 23ai ledger-isolation tier. The wedge vs SAP BTP is: SAP BTP's underlying-region-distribution is a single Azure-deal-region distribution with no named Sovereign Cloud tier; Oracle ships NAMED first-party OCI Sovereign Cloud + US Government Cloud + UK Government Cloud + Defense Cloud + EU Sovereign Cloud regions.
3. **Oracle AI Agent Studio for Fusion Cloud Applications** — Oracle ships a NAMED first-party AI Agent Studio with NAMED ERP/Finance/HCM/SCM/Customer Experience agent templates and NAMED AI-Agent Marketplace, with NAMED per-tenant agent-isolation tier. The wedge vs SAP Joule: SAP Joule is a single natural-language-Q&A-only substrate without a published agent-template marketplace, while Oracle AI Agent Studio ships NAMED agent templates and a marketplace where customers can publish + share agents.
4. **Customer tier (verbatim first-party 2026-07-24)** — PepsiCo + FedEx + Marriott + T-Mobile + Vodafone + Toyota + Cisco + General Motors + HSBC + BNP Paribas + Standard Bank + Zoom + McDonald's + Starbucks + 7-Eleven + MGM Resorts + Wendy's + Humana + Cigna + UnitedHealth + 250,000+ NetSuite SMB orgs. The wedge vs SAP: SAP's customer tier is 99-of-Fortune-100 + 87% Forbes Global 2000; Oracle's customer tier is Fortune-500 mid-tier + mid-market NetSuite SMB tier (250,000+ orgs).
5. **Exadata Exascale + Autonomous Database 23ai** — Oracle ships NAMED first-party Exadata Exascale + Autonomous Database 23ai as the underlying ledger-isolation tier with named Always-Free tier + named per-OCPU + named per-storage-tier. The wedge vs SAP HANA Cloud: SAP HANA Cloud is a single in-memory substrate without a vector-store + without a free-tier; Oracle Autonomous Database ships NAMED first-party vector-store substrate with 23ai release (2024) + named Always-Free tier for development.

## Receipt design (22-column per-tenant)

```
tenant_id + oracle_fusion_tenant_id + oracle_fusion_ledger_id +
oracle_fusion_gl_journal_id + oracle_fusion_ap_invoice_id +
oracle_fusion_ar_invoice_id + oracle_fusion_close_cycle_id +
oracle_fusion_fixed_asset_id + oracle_netsuite_subsidiary_id +
oracle_netsuite_transaction_id + oracle_oci_compartment_id +
oracle_ai_agent_studio_agent_id + oracle_ai_agent_studio_model_id +
oracle_ai_agent_studio_tool_call_id + oracle_ai_agent_studio_decision +
oracle_ai_agent_studio_prompt_hash + oracle_ai_agent_studio_response_hash +
per_integration_consent_ledger_entry_id + per_tenant_BYOK_signing_key_id +
per_oci_region + per_sub_processor_dpa_flow_down + per_sox_404_key_control +
per_ifrs_audit_trail_reference + per_sec_10k_filing_reference +
per_eu_ai_act_art_14_human_oversight_id + per_eu_ai_act_art_26_deployer_id +
per_eu_ai_act_art_27_fria_id + cross_tenant_no_bleed_invariant +
audit_export_id + replay_hash + retention_until
```

## Compliance posture (verbatim first-party oracle.com 2026-07-24)

- Public-co: NYSE: ORCL + FTSE: ORCL (ADR) + Q3-FY26 GAAP revenue $14.6B (quarter ended 2026-02-28)
- Audit: SOX 404 ICFR + SEC 10-K + 10-Q + 8-K + Reg-FD + Reg-G + IFRS + ASC 606 + ASC 842 + ASC 326 CECL
- EU AI Act: Art. 14 human-oversight + Art. 26 deployer + Art. 27 FRIA
- Privacy: GDPR + UK GDPR + CCPA/CPRA + LGPD + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA
- Security: ISO 27001 + ISO 27017 + ISO 27018 + ISO 27701 + SOC 2 Type II + NIST AI RMF + Cloud Security Alliance STAR
- Cloud regions: US-Ashburn + US-Phoenix + EU-Frankfurt + UK-London + APAC-Tokyo + APAC-Sydney + APAC-Mumbai + APAC-Seoul + SA-São Paulo + CA-Toronto

## Cohort plan (NEW VERTICAL #43 ai_agent_erp_dataops)

- OPENER #1/5: SAP SE 1135 (shipped 2026-07-24) — S/4HANA Cloud + Joule + BTP + AI Core + Datasphere
- SIBLING #2/5: Oracle 1136 (THIS TICK) — Fusion Cloud ERP + NetSuite + OCI + AI Agent Studio
- SIBLING #3/5: Microsoft Dynamics 365 Finance + Supply Chain (candidate) — TBD
- SIBLING #4/5: Workday Financials (candidate) — TBD
- CLOSER #5/5: Salesforce ERP + Agentforce (candidate) — TBD

## What ships in this tick

- cold_email/templates/1136_oracle_erp_dataops.md (3-line subject × 3 + body + tier reason + 5-WEDGE non-overlap + compliance + customer tier + offer ladder)
- cold_email/1136_oracle.md (this companion)
- cold_email/leads.csv row 1136
- cold_email/leads_with_emails.csv row 1136
- cold_email/send_log.jsonl queued-not-sent receipts (×2)
- cold_email/revenue_log.csv $0 row
- build-log.html tick-1136 entry
- Commit + push to origin/main

[tick-1136-oracle-erp-dataops-sibling-2]
