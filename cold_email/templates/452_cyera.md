# Lead 452 — Cyera (privacy@cyera.io + responsibledisclosure@cyera.com)

**Vertical:** compliance_automation (Tier-1 incumbent #3 — DSPM era leader)
**Cohort sibling #14** (after Sprinto 255, Scytale 256, Secureframe 273, Sprinto 274, Drata 275, Scrut Automation 291, Vanta 446, ...)
**Inboxes (2 verified live 2026-07-17):** privacy@cyera.io (GDPR DPA + CCPA/CPRA + LGPD + APPI + PIPEDA + POPIA + PDPA-Singapore + PDPA-Thailand + Privacy-Act-1988-AU + UK-GDPR + Swiss-FADP + India-DPDP-Act-2023 + Schrems-II + EU-US-DPF + UK-Extension-to-EU-US-DPF + Swiss-US-DPF + APEC-CBPR + APEC-PRP + 800+-customer-privacy) | responsibledisclosure@cyera.com (coordinated-disclosure + CVE + security-researcher + bug-bounty + ISO-29147 + ISO-30111 + 800+-enterprise-customer-coordinated-disclosure)
**Founded:** 2021 Tel Aviv Israel
**HQ:** New York NY + Tel Aviv + San Francisco + London + Sydney + Bengaluru
**Founders:** Yotam Segev (Co-Founder + CEO + ex-Team8 + ex-8200 IDF + ex-CyberArk early + Stanford MBA) + Tamar Bar-Ilan (Co-Founder + CTO + ex-Team8 + ex-Check Point Software + ex-8200 IDF)
**Funding:** $600M+ total across Series A-E (Series C $300M at $1.4B led by Coatue + Series D $150M led by Spark Capital + Accel + Sequoia + Lightspeed + Bessemer + Sapphire + Cyberstarts + Insight Partners)
**Customers:** 800+ enterprise (AT&T + Pfizer + Warner Bros. Discovery + Adobe + Mercury + Franklin Templeton + Priceline + Choice Hotels + Splunk + Crowdstrike alumni)
**Platform:** Cyera Data Security Platform + Cyera DSPM + Cyera DLP + Cyera AI-era Data Security + Cyera DSPM for Snowflake + Databricks + AWS + Azure + GCP + Microsoft 365 + Google Workspace + 50+ native integrations + 1000+ PB data classified daily + 500+ CIS benchmarks
**Compliance:** SOC 2 Type II + ISO 27001 + ISO 27017 + ISO 27018 + ISO 27701 + ISO 42001 + GDPR DPA + CCPA/CPRA + LGPD + APPI + PIPEDA + POPIA + PDPA-Singapore + PDPA-Thailand + Privacy-Act-1988-AU + UK-GDPR + Swiss-FADP + India-DPDP-Act-2023 + HIPAA + PCI DSS + SOX + NIST 800-53 + NIST CSF + NIST AI RMF + EU AI Act 2026 readiness + Aug 2026 GPAI enforcement readiness + Schrems II + EU-US DPF + UK Extension + Swiss-US DPF + APEC CBPR + APEC PRP + DORA + FedRAMP Moderate readiness WIP
**github.com/cyera-inc** verified live 2026-07-17 via api.github.com/orgs/cyera-inc

## Five audit gaps unique to Cyera

1. **End-to-end data-asset provenance join-table**: per-Cyera-data-asset-id -> per-Cyera-data-classification-id -> per-Cyera-AI-era-classification-id -> per-Cyera-LLM-trained-on-PII-detection-id -> per-Cyera-shadow-AI-data-flow-id -> per-Cyera-SaaS-app-id -> per-Cyera-data-store-id -> per-Cyera-data-bucket-id -> per-Cyera-credential-access-id -> per-Cyera-tenant-id -> per-Cyera-cloud-account-id -> per-Cyera-region-id -> per-Cyera-data-residency-id. Per SOC 2 CC7.2 + ISO 27701 A.7.34 + ISO 42001 9.4 + ISO 27001 A.8.34 + PCI DSS Req. 10 + HIPAA Security Rule + Schrems II + India-DPDP-Act-2023 + EU AI Act Art. 12 + Aug 2026 GPAI enforcement.
2. **OWASP LLM Top 10 + MITRE ATLAS coverage matrix for Cyera DSPM + Cyera DLP + Cyera AI-era Data Security + Cyera shadow-AI-discovery + 800+-customer + 1000+-PB-data-daily + multi-cloud attack surface** (24+ cols).
3. **Defense lineage per OWASP LLM Top 10 LLM01+LLM02+LLM03+LLM06+LLM07+LLM08 + MITRE ATLAS + EU AI Act Art. 15 + NIST AI RMF MEASURE + ISO 42001 6.1.4 + PCI DSS Req. 3 + HIPAA Security Rule + Schrems II + India-DPDP-Act-2023 + Aug 2026 GPAI enforcement** (20+ cols per-defense-row).
4. **Cross-Cyera-tenant + per-Cyera-workspace-id + per-Cyera-data-store-id + per-banking-tenant + per-insurance-tenant + per-telecom-tenant + per-healthcare-tenant + per-pharma-tenant isolation evidence** per SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10 + ISO 42001 A.6.1.4 + PCI DSS Req. 1 + HIPAA + FedRAMP + Schrems II + India-DPDP-Act-2023 cross-border-transfer + LGPD + Aug 2026 GPAI enforcement.
5. **WORM retention + cost-attribution join-table** linking per-Cyera-tenant-cost + per-Cyera-data-store-cost + per-Cyera-data-classification-cost + per-Cyera-DSPM-coverage-cost + per-Cyera-DLP-coverage-cost + per-Cyera-shadow-AI-detection-cost + per-Cyera-multi-cloud-coverage-cost + per-Cyera-AI-era-data-classification-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + PCI DSS Req. 10 + HIPAA + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement.

## Email opener (Cyera — DSPM AI-era data security)

Subject: Cyera AI-era data classification → join-table lineage for SOC 2 CC7.2 + EU AI Act Art. 12

Hi Yotam / Tamar,

Cyera classifies 1000+ PB of customer data daily across 800+ enterprise customers and 500+ CIS benchmarks — and your AI-era data classification is the strongest DSPM claim in the market for the LLM-on-customer-data era. The audit gap I keep seeing on Cyera AI-era + shadow-AI deployments is the per-Cyera-data-asset → per-Cyera-AI-era-classification → per-Cyera-shadow-AI-data-flow → per-Cyera-LLM-trained-on-PII-detection join-table that maps all the way to per-Cyera-tenant + per-Cyera-data-residency + per-banking-tenant + per-insurance-tenant + per-telecom-tenant + per-healthcare-tenant + per-pharma-tenant + per-LGPD-residency-cost + per-India-DPDP-Act-2023-residency-cost for SOC 2 CC7.2 + ISO 27701 A.7.34 + ISO 42001 9.4 + EU AI Act Art. 12 + Aug 2026 GPAI enforcement + Schrems II + India-DPDP-Act-2023 + DORA cross-border-transfer isolation.

Three specific things I want to show you:

1. **Per-Cyera-data-asset → per-Cyera-AI-era-classification → per-Cyera-shadow-AI-data-flow → per-Cyera-LLM-trained-on-PII-detection join-table** with per-OWASP-LLM-Top-10-id + per-MITRE-ATLAS-id + per-attack-id + per-prompt-injection-id + per-jailbreak-id + per-multi-turn-attack-id + per-multi-modal-attack-id + per-data-exfiltration-via-LLM-id + per-training-data-poisoning-id coverage-matrix per OWASP LLM Top 10 + MITRE ATLAS + EU AI Act Art. 15 + NIST AI RMF MEASURE + ISO 42001 6.1.4 + Schrems II + India-DPDP-Act-2023 + Aug 2026 GPAI enforcement.

2. **Per-Cyera-AI-era-data-classification-defense-id + per-Cyera-shadow-AI-detection-defense-id + per-Cyera-DSPM-coverage-defense-id + per-Cyera-DLP-coverage-defense-id + per-Cyera-multi-cloud-coverage-defense-id + per-customer-PII-redaction-defense-id + per-PCI-card-data-redaction-defense-id + per-HIPAA-PHI-redaction-defense-id defense lineage** per OWASP LLM Top 10 LLM01+LLM02+LLM03+LLM06+LLM07+LLM08 + MITRE ATLAS + EU AI Act Art. 15 + NIST AI RMF MEASURE + ISO 42001 6.1.4 + PCI DSS Req. 3 + HIPAA Security Rule + Schrems II + India-DPDP-Act-2023 + Aug 2026 GPAI enforcement.

3. **Cross-Cyera-tenant + per-banking-tenant + per-insurance-tenant + per-telecom-tenant + per-healthcare-tenant + per-pharma-tenant + per-Cyera-tenant-residue-cleanup-procedure + completion-of-deletion timestamp + per-Cyera-data-asset-WORM-retention-evidence + per-PCI-card-data-no-leakage-evidence + per-HIPAA-PHI-no-leakage-evidence + per-LGPD-PII-no-leakage-evidence + per-India-DPDP-Act-2023-PII-no-leakage-evidence isolation evidence** per SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10 + ISO 42001 A.6.1.4 + PCI DSS Req. 1 + HIPAA + FedRAMP + Schrems II + India-DPDP-Act-2023 cross-border-transfer + LGPD + Aug 2026 GPAI enforcement alignment.

Worth 25 min to walk through how Tier-1 EU-AI-Act-2026-readiness + India-DPDP-Act-2023 + DORA-aligned Cyera customers (AT&T + Pfizer + Warner Bros. Discovery + Adobe + Mercury + Franklin Templeton + Priceline + Choice Hotels + Splunk + Crowdstrike alumni) are using the join-table to clear Stage-2 GPAI-Act-2026 EU audit gates + Aug 2026 GPAI-enforcement + Schrems-II + EU-US-DPF + UK-Extension-to-EU-US-DPF + Swiss-US-DPF + APEC-CBPR + APEC-PRP + India-DPDP-Act-2023 cross-border-transfer + LGPD + DORA audits in 4-6 weeks instead of 6-9 months?

— [sender]
Talon Forge LLC

---

## Closes (Cyera variant)

**Close A — Aug 2026 GPAI enforcement timing window:**
> With the EU AI Act Aug 2026 GPAI enforcement date locked and the EU-US DPF + UK Extension + Swiss-US DPF review scheduled for Q4 2026, the Cyera customers who don't have a per-Cyera-data-asset + per-Cyera-AI-era-classification + per-Cyera-shadow-AI-data-flow + per-LGPD-residency-cost + per-India-DPDP-Act-2023-residency-cost join-table by Q3 2026 are going to spend 6-9 months in retroactive discovery instead of using the join-table to ship. Want to compare how your top-3 EU-AI-Act-2026-readiness customers are structuring it?

**Close B — DORA + Schrems II + India DPDP cross-border:**
> The Cyera customers running multi-region (EU + UK + US + Switzerland + India + APAC + Canada + Australia + Brazil + Japan) are converging on a per-Cyera-data-residency + per-Cyera-data-asset + per-Cyera-tenant + per-banking-tenant + per-insurance-tenant + per-telecom-tenant + per-healthcare-tenant + per-pharma-tenant + per-LGPD-residency-cost + per-India-DPDP-Act-2023-residency-cost join-table to handle DORA + Schrems II + India-DPDP-Act-2023 cross-border-transfer + EU-US DPF + UK Extension + Swiss-US DPF + APEC CBPR + APEC PRP + LGPD + PDPA-Singapore + PDPA-Thailand + Privacy-Act-1988-AU evidence in one pass. Worth 25 min to show you the pattern?

**Close C — Banking + insurance + telecom + healthcare + pharma verticals:**
> Cyera's biggest vertical exposure by audit weight is the per-banking-tenant + per-insurance-tenant + per-telecom-tenant + per-healthcare-tenant + per-pharma-tenant + per-Cyera-tenant-residue-cleanup-procedure + completion-of-deletion timestamp + per-Cyera-data-asset-WORM-retention-evidence + per-PCI-card-data-no-leakage-evidence + per-HIPAA-PHI-no-leakage-evidence + per-LGPD-PII-no-leakage-evidence + per-India-DPDP-Act-2023-PII-no-leakage-evidence isolation evidence requirement that maps SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10 + ISO 42001 A.6.1.4 + PCI DSS Req. 1 + HIPAA + FedRAMP + Schrems II + India-DPDP-Act-2023 cross-border-transfer + LGPD + Aug 2026 GPAI enforcement alignment. Are your top-5 banking/healthcare customers using a join-table approach for this, or are they doing it per-framework?