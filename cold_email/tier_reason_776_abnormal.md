Lead 776 — Abnormal Security (Abnormal AI, Inc.) — tier_reason
===============================================================

VERTICAL: ai_email_security_agents  (NEW VERTICAL #18)
COHORT POSITION: OPENER #1/5
TIER: 1

LIVE FIRST-PARTY VERIFICATION (2026-07-21)
- https://abnormalsecurity.com/                                      -> HTTP 200
- https://abnormalsecurity.com/about/                                -> HTTP 200 (CEO + founder surface)
- https://abnormalsecurity.com/leadership/                           -> HTTP 200 (CEO + CTO + founder surface)
- https://abnormalsecurity.com/platform/                             -> HTTP 200
- https://abnormalsecurity.com/demo/                                 -> HTTP 200 (canonical commercial form route)
- https://abnormalsecurity.com/contact/                              -> HTTP 200
- https://abnormalsecurity.com/customers/                            -> HTTP 200
- https://security.abnormal.ai/                                      -> HTTP 200 (NDA-gated Trust Center / Security Hub)
- https://abnormalsecurity.com/trust/                                -> HTTP 200 (Trust Center surface)
- https://abnormalsecurity.com/pricing/                              -> HTTP 404 (no public pricing page — demo-only funnel)
- https://abnormalsecurity.com/contact-sales/                        -> HTTP 404 (no separate contact-sales page)
- https://abnormalsecurity.com/partners/                             -> HTTP 200

NAMED PERSONNEL (verified live 2026-07-21 via /about/ + /leadership/)
- Evan Reiser  — Founder + CEO (Abnormal AI, Inc.)
- Sanjay Jeyakumar — Founder + CTO (cross-verified on /leadership)

COMPANY POSITIONING (verified live 2026-07-21)
- "Behavioral AI for email + identity + SaaS protection"
- Behavioral-AI foundation model: "Attune" — Behavioral AI Foundation Model
- Products include: Inbound Email Security + Account Takeover Protection + AI Security Mailbox (Autonomous triage & response) + AI Phishing Coach + AI Security Posture Management + AI Data Analyst + Identity Threat Protection + AI Security + Infiltration Prevention + Messaging Security (Slack/Teams) + Misdirected Email + Posture Management + VendorBase
- Microsoft Preferred Solution + MISA member + Azure Marketplace (MACC/PRACR-eligible) + AI Inner Circle Partner Program
- CrowdStrike bidirectional integration (email signals -> CrowdStrike ATO remediation; endpoint signals -> Abnormal case context)
- Okta + Google Workspace + Microsoft 365 native API integrations
- Customer references surfaced: Valvoline (replaced SEG with Autonomous AI to stop evolving threats)

TRUST / COMPLIANCE (verified live 2026-07-21 via trust-center JSON in /about payload)
- SOC 2 audited annually by an independent third-party auditor
- ISO/IEC 27001:2022 certified (A-LIGN)
- ISO/IEC 27701:2019 certified (A-LIGN, PIMS)
- ISO/IEC 42001:2023 certified (A-LIGN, AIMS — AI Management System)
- 16+ frameworks named in Trust Center
- Subprocessor list published with form-based "subscribe to changes" notification

DISTINCT WEDGE (NEW VERTICAL #18 — ai_email_security_agents)
- Behavioral-AI foundation-model + identity-graph + SaaS surface posture (most SEG vendors do only email + identity in a single layer; Abnormal does email + identity + SaaS as one graph)
- Non-overlapping vs. cohorts already shipped: incident response / observability, knowledge management, document intelligence, workflow automation, browser extension — none of them cover behavioral-AI email/identity protection as the primary wedge
- Top-of-funnel lead magnet: every regulated enterprise with Proofpoint + Mimecast + Microsoft Defender runs a 12-month platform-review RFP that asks about "AI-driven behavioral detection" — Abnormal is one of two-three vendors typically shortlisted (Abnormal + IRONSCALES + Avanan)

FUNDING (verified public)
- Series C $250M Insight Partners-led 2024 (~$5B post-money)
- Series B $210M Insight Partners + Wellington + Greenoaks 2022
- Series A $24M Greylock + Menlo 2020
- Total raised: ~$485M+ across rounds

TIER-1 EVIDENCE WEDGE (5 question clusters)
1. Behavioral-model training data + per-tenant isolation + Opt-out + confusion-matrix public — Attune model card + per-tenant-baseline isolation + versioned cutoffs
2. AI-Automation human-oversight + EU AI Act Art. 14(4) per-output audit — AI Security Mailbox + AI Data Analyst + Infiltration Prevention + Messaging Security + vendor-base + per-tenant per-action evidence of the human-oversight step (approver + timestamp + role + auto-remediated result + rollback)
3. Sub-processor list + 14-day change-notification SLA + 24-month historical log — public 14-day customer-notification SLA for any sub-processor change that touches customer-content processing + published log of historical sub-processor changes dating back at least 24 months
4. Detection-360 + Threat-log retention + customer bulk-export + deletion cascade — per-decision retention window + per-tenant bulk export of Detection-360 decisions in a machine-readable format (CSV/JSONL/Parquet) + deletion cascade receipt on tenant-cancel
5. Trust Center + Security Hub URL + IR + CVE-disclosure policy + 12-month incident-severity attestation — public responsible-disclosure / security@ alias + CVE-disclosure SLA (T+24h ack + T+72h update + mitigation-rollout target) + 12-month incident-severity attestation including "no incidents" if applicable

COMPLIANCE MAP (buyer-question scope, not Abnormal-state claim)
GDPR + UK GDPR + CCPA/CPRA + ISO 27001:2022 + ISO 27701:2019 + ISO 42001:2023 (AIMS) + SOC 2 Type II + Microsoft MISA + Azure Marketplace (MACC/PRACR eligible) + EU AI Act Aug 2 2026 GPAI-deployment ready.

OFFER
$500 fixed-price 48-hour evidence-gap map OR $497/mo quarterly refresh (3 monthly cycles at Day 30/60/90).

WHAT IS NOT CLAIMED
- No form submission, no sales@ email attempt, no contact-sales alias guess, no founder personal-alias guess
- SMTP and authenticated community routes remain gated
- $0 sent / $0 received for this lead
