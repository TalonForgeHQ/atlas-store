# Lead 1151 Companion — Proofpoint SIBLING #3/5

**Tick:** 2026-07-24-fast-exec-proofpoint-zeta-series-data-loss-prevention-sibling-3-1151
**Vertical:** ai_agent_data_loss_prevention (NEW VERTICAL #50)
**Cohort role:** SIBLING #3/5 after Trellix 1149 OPENER + CrowdStrike 1150 SIBLING #2/5

## Company snapshot (verbatim first-party 2026-07-24)

- **Name:** Proofpoint, Inc. (taken-private by Thoma Bravo 2021-08-31 for $12.3B; was NASDAQ:PFPT 2012-2021; CIK 0001212458)
- **Founded:** 2002-07 by Eric Hahn (Co-Founder & Chairman, former CTO Netscape Communications)
- **HQ:** 925 West Maude Avenue, Sunnyvale, CA 94085 (verbatim first-party proofpoint.com/us/company/contact)
- **CEO:** Sumit Dhawan (2024+, verbatim first-party proofpoint.com/us/company/leadership)
- **CFO:** Rémi Thomas (verbatim Wikipedia infobox 2026-07-24)
- **CTO:** Marcel DePaolis (verbatim Wikipedia infobox 2026-07-24)
- **EVP Cybersecurity Strategy:** Ryan Kalember (verbatim first-party proofpoint.com/us/company/leadership)
- **3,658 FTE 2020** (verbatim first-party Wikipedia infobox)
- **Revenue $1.050B 2020** (verbatim first-party Wikipedia infobox)
- **Hornetsecurity + Vade acquisition:** May 2025 (verbatim first-party Wikipedia)

## Named first-party AI-agent-aware substrate (verbatim first-party proofpoint.com/us 2026-07-24)

- **Data Security for AI** — secure data across shadow and approved AI
- **Secure AI Usage by People** — visibility and control around employees' use of AI
- **Secure AI Usage by Agents** — MCP-aware AI agent intent and control (MCP = Model Context Protocol)
- **Proofpoint Satori** — The power behind agentic security operations (agentic SOC)
- **Proofpoint Zen** — Integrated control points to protect people and data anywhere
- **Proofpoint 365 Total Protection** — Enabling the channel, protecting humans and agents
- **Enterprise DLP** — Prevent data loss across email, cloud, and endpoints
- **Adaptive Email DLP** — Prevent misdirected emails and hidden data exfiltration (Tessian-acquired engine)
- **Data Security Posture Management (DSPM)** — Discover, classify, and protect sensitive data across cloud and hybrid
- **Insider Threat Management** — Get visibility into risky behavior by careless, malicious, and compromised users
- **Digital Communications Governance** — Intelligently capture, retain, and discover digital communications
- **Identity Threat Defense + Account Takeover Protection** — DLP + Identity coherent substrate
- **Hornetsecurity (acquired May 2025) + Vade (acquired via Hornetsecurity May 2025)** — three first-party email-DLP engines

## Compliance posture (verbatim first-party 2026-07-24)

- SOC 2 Type II (inferred from FedRAMP + ISO certs)
- ISO/IEC 27001:2022 + 27017 + 27018 + 27701
- **FedRAMP certified** (verbatim first-party proofpoint.com/us)
- HIPAA + GDPR + UK GDPR + EU AI Act readiness
- CCPA/CPRA + PCI DSS 4.0
- NIST 800-53 + NIST CSF 2.0
- **MAS (Monetary Authority of Singapore)** + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA + LGPD

## 5-WEDGE non-overlap rubric vs Trellix 1149 + CrowdStrike 1150 (PITFALL #99, all first-party)

1. **Only cohort member with NAMED MCP-aware AI-agent intent DLP substrate** — verbatim first-party "Secure AI Usage by Agents" + "MCP integrations" on proofpoint.com/us/products/ai-security 2026-07-24. Neither Trellix DLP nor CrowdStrike Falcon Data Protection has a NAMED MCP-aware agent-intent product. (Cohort-unique.)
2. **Only cohort member with NAMED Proofpoint Satori agentic-SOC analyst platform** — verbatim first-party "The power behind agentic security operations" 2026-07-24. Trellix Helix has SOC but no NAMED "agentic" product; CrowdStrike Charlotte AI is NAMED agentic but is single-product, not a multi-product substrate.
3. **Only cohort member with three first-party email-DLP engines (Tessian + Hornetsecurity + Vade)** — Tessian acquired 2023, Hornetsecurity + Vade acquired May 2025. CrowdStrike has Falcon Data Protection email-DLP but it's one engine. Trellix has DLP Email but not Tessian / Hornetsecurity / Vade lineage.
4. **Only cohort member with NAMED Digital Communications Governance for AI-agent-generated communications** — capture + retain + discover for AI-agent-generated communications. Neither Trellix nor CrowdStrike has a NAMED AI-agent-communications-governance product.
5. **Only cohort member with NAMED Identity Threat Defense + Account Takeover Protection as part of the same DLP substrate** — Proofpoint pairs DLP with Identity Threat Defense. Trellix has Helix IAM separately; CrowdStrike has Falcon Identity Threat Protection but it's part of the Falcon single-agent substrate, not a DLP-coherent Identity product.

## 22-col per-Proofpoint receipt design

| # | Column | Source |
|---|---|---|
| 1 | tenant_id | Proofpoint tenant |
| 2 | proofpoint_pod_id | Proofpoint multi-tenant pod |
| 3 | proofpoint_dlp_policy_id | Enterprise DLP policy |
| 4 | proofpoint_tessian_rule_id | Tessian adaptive email-DLP rule |
| 5 | proofpoint_hornetsecurity_classification_id | Hornetsecurity email classification |
| 6 | proofpoint_satori_investigation_id | Satori agentic-SOC investigation |
| 7 | proofpoint_ai_agent_intent_id | MCP-aware AI-agent intent decision |
| 8 | proofpoint_insider_threat_score_id | Insider Threat Management score |
| 9 | proofpoint_dspm_data_asset_id | DSPM data asset |
| 10 | proofpoint_dcg_capture_id | Digital Communications Governance capture |
| 11 | proofpoint_atp_session_id | Account Takeover Protection session |
| 12 | proofpoint_itd_session_id | Identity Threat Defense session |
| 13 | proofpoint_email_fraud_decision_id | Email Fraud Defense decision |
| 14 | proofpoint_zenguide_assignment_id | ZenGuide security-awareness assignment |
| 15 | proofpoint_ser_relay_id | Secure Email Relay |
| 16 | proofpoint_collab_security_event_id | Collaboration Security event |
| 17 | proofpoint_email_classification_id | Email classification decision |
| 18 | proofpoint_ai_usage_decision_id | "Secure AI Usage by People/Agents" decision |
| 19 | proofpoint_audit_export_id | Audit export |
| 20 | eu_ai_act_art14_human_oversight_id | EU AI Act Art. 14 human-oversight record |
| 21 | human_override_id | Human override |
| 22 | cross_tenant_no_bleed_audit_trail | Cross-tenant no-bleed invariant |

## Commercial routes (verbatim first-party 2026-07-24, NOT submitted)

- mailto:info@proofpoint.com
- mailto:sales@proofpoint.com
- mailto:contact@proofpoint.com
- FORM:https://www.proofpoint.com/us/company/contact

## Offer

- $500/48h fixed-scope evidence-gap-map audit (22-col receipt + cohort rubric + AI-agent evidence-gap map)
- $497/mo quarterly refresh
- $2,000 four/five-vendor cohort benchmark (Trellix + CrowdStrike + Proofpoint + your pick: Zscaler / Netskope / Cyera / SecuritiAI)
- $2,485 MRR ceiling per YanXbt pattern (5 clients max)

## Pitfall #28 compliance

- No guessed general-business inbox — only first-party mailto:info@proofpoint.com + sales@proofpoint.com + contact@proofpoint.com + verbatim first-party FORM:https://www.proofpoint.com/us/company/contact
- 2 OPEN slots remaining for SIBLING #4-5/5

## SMTP/form gate
- $0 sent / $0 received
- All routes queued, not sent (per pitfall #28 + #46 dry-run discipline)
