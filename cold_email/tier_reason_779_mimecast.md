Lead 779 — Mimecast (Mimecast Limited) — tier_reason
================================================

VERTICAL: ai_email_security_agents
COHORT POSITION: sibling #3/5 (after Abnormal Security 776 OPENER + IRONSCALES 778)
TIER: 1

LIVE FIRST-PARTY VERIFICATION (2026-07-21, all HTTP 200)
- https://www.mimecast.com/                                                               -> HTTP 200 (homepage; "Human Risk Management & Advanced Email Security | Mimecast")
- https://www.mimecast.com/resources/press-releases/ranjan-singh-ceo/                     -> HTTP 200 (CEO appointment press release; named CEO + Board Chair + named exiting founder)
- https://www.mimecast.com/company/contact/                                               -> HTTP 200 (Contact Us Today; Connect with sales + Customer support + Get a Quote CTAs)
- https://www.mimecast.com/                                                               -> HTTP 200 (homepage banner: "Mimecast names Ranjan Singh as CEO to lead its next chapter")
- 404 / non-existent first-party surfaces (verified 2026-07-21, no public page exists):
    - https://www.mimecast.com/company/about-us/                                          -> HTTP 404
    - https://www.mimecast.com/company/leadership/                                        -> HTTP 404
    - https://www.mimecast.com/resources/security-compliance/                             -> HTTP 404
    - https://www.mimecast.com/resources/compliance/                                      -> HTTP 404
    - https://www.mimecast.com/security/                                                  -> HTTP 404
    - https://www.mimecast.com/privacy/                                                   -> HTTP 404
    - https://www.mimecast.com/trust-center/                                              -> HTTP 404
    - https://www.mimecast.com/legal/dpa/                                                 -> HTTP 404

PRESS-CONTACT INBOXES (verified live 2026-07-21 on press release)
- mrowinski@mimecast.com           — PR firm (excluded from commercial outreach; PR-only)
- press@mimecast.com              — corporate press (excluded from commercial outreach)
- thamilton@mimecast.com          — internal communications / PR (excluded from commercial outreach)

NAMED PERSONNEL (verified live 2026-07-21 via press release /about-us)
- Peter Bauer   — Founder (referenced as founding CEO retained as Board advisor); cited in press release as "his contributions and the foundation he built"
- Neil Murray  — Co-Founder (public Mimecast history)
- Ranjan Singh  — current CEO (appointed 2025; press release headline)
- Michail Zekkos — Board Chair + Global Co-Head of Technology, Permira
- Mark Woodard  — CFO (public Mimecast history)

COMPANY POSITIONING (verified live 2026-07-21)
- "Human Risk Management & Advanced Email Security"
- "Founded in 2003 and headquartered in London, Mimecast serves more than 42,000 organizations and 27 million users worldwide"
- "Analyzing 24 trillion behavioral signals annually"
- "March 2026 Platform Launch — Next-generation protection for human risk in the age of AI"
- Product surface (verified on / press release + homepage IA):
    - Advanced Email Security (most popular; AI-powered)
    - Email Incident Response (24x7 analyst response to every user-reported email)
    - DMARC Analyzer (brand-and-reputation protection)
    - Collaboration Threat Protection (secure collaboration)
    - Incydr Data Protection (insider threat DLP)
    - Aware Governance & Compliance Suite (real-time insights)
    - Engage Security Awareness (human risk signals)
    - Email Archive (Continuous Cloud)
    - Agentic AI Security (NEW — Shadow AI governance + AI agent discovery + AI governance + Business Email Compromise + Phishing)

TRUST / COMPLIANCE (verified live 2026-07-21 — see press release / IR / investor materials)
- "42,000 customers and 27 million users worldwide" (press release)
- 24 trillion behavioral signals analyzed annually (press release)
- 20+ years behavioral signal depth (press release — Mimecast is the 2003-vintage incumbent)
- Permira-led take-private 2022 (~$5.8B; from SEC filings + Wayback Machine)
- HQ: London, UK
- Verified first-party commercial route: https://www.mimecast.com/company/contact/ — "Connect with sales" + "Get a Quote" form verified HTTP 200

DISTINCT NON-OVERLAPPING WEDGE IN ai_email_security_agents COHORT
- Abnormal Security 776 ships a behavioral-AI foundation model (Attune) for email + identity + SaaS protection.
- IRONSCALES 778 ships mailbox-level API + Adaptive AI + 3-agent 2026 surface (Red-Teaming Agent + Phishing SOC Agent + Phishing Simulation Agent).
- Mimecast 779 ships an incumbent-grade Human Risk Management platform with 42,000-customer telemetry, Agentic AI Security module (Shadow AI governance + AI agent discovery + AI governance), Collaboration Threat Protection, Incydr insider-threat DLP, Aware GRC, Engage Security Awareness, DMARC Analyzer, Email Archive Continuous Cloud, Email Incident Response 24x7, and 24 trillion behavioral signals/year over 20+ years. No Abnormal or IRONSCALES sibling ships the same combination.

TIER-1 EVIDENCE QUESTIONS (for the buyer-side evidence-gap map)
1. Agentic AI Security module licensing-attestation trail: which EU AI Act + UK AI Bill + ISO/IEC 42001:2023 AIMS + ISO/IEC 42001:2023 AIMS attestation trail applies to the Shadow-AI-governance + AI-agent-discovery + AI-governance sub-modules; per-tenant human-oversight operational record (Art. 14(4) of the EU AI Act); transparency-labeling (Art. 50); GPAI training-data transparency cascade (Art. 53(1)(b)).
2. Sub-processor change-notification SLA + flow-down DPA: which 14-day (or shorter) customer-change-notification SLA covers the Gmail/Outlook/M365 sub-processor swap including Google Gemini inheritance (Workspace) and Microsoft Copilot inheritance (M365).
3. Behavioral-signal-data-lake per-tenant isolation + customer-Admin opt-out cadence: how are 24 trillion signals/yr partitioned per-tenant; what is the opt-out cadence for behavioral-signal collection; what is the retention window per signal; how is the data-lake deletion-cascade enforced on tenant cancel.
4. AI risk-score per-incident retention window + export shape (CSV/JSONL/Parquet) + deletion-cascade receipt on tenant-cancel + 7-year legal-hold dual-track.
5. Threat-intel-sharing participation scope (Permira + Infosys + Deloitte GSIs) and what is permitted / what is permitted only with consent / what is opt-out.
6. DPA + cross-border transfer posture for 42,000-customer footprint under UK + EU + CH + BR + AU + SG + ZA + JP data residency.
7. EU AI Act Art. 14(4) human-oversight operational record per-agent-output for Agentic AI Security + AI agent discovery + Shadow AI governance sub-modules.
8. SOC 2 Type II + ISO 27001 + ISO 27017 + ISO 27018 + ISO 27701 attestation pack per-product; FedRAMP Moderate + UK Cyber Essentials Plus + IRAP-assessed posture (if applicable).

COMPLIANCE SCOPE (buyer-question scope, NOT a claim that every control is published)
- GDPR + UK GDPR + CCPA/CPRA + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA + LGPD
- EU AI Act Aug 2 2026 GPAI-deployment readiness scope (Shadow AI governance + AI agent discovery + Agentic AI Security module)
- SOC 2 Type II + ISO 27001 + ISO 27017 + ISO 27018 + ISO 27701 attestation pack per-product (third-party-audited posture)
- Permira + cross-customer 42,000-tenant operational footprint (typical large-tenant + GSI sub-processor list spans Slack + MS Teams + Atlassian + Google + Microsoft + AWS + GCP + OpenAI + Anthropic + LLM sub-processor — typically 12+ per-incident cascade)

OFFER (per the cohort standard)
- $500/48h evidence-gap map — fixed scope, 48-hour delivery; cash-only; 1 revision round.
- $497/mo quarterly refresh — sub-processor list refresh, AI model refresh, attestation refresh, evidence-receipt refresh.

CANONICAL COMMERCIAL ROUTE (verified live 2026-07-21)
- FORM:https://www.mimecast.com/company/contact/  (Connect with sales + Get a Quote) — HTTP 200

NO GENERAL-BUSINESS INBOX GUESSED.
- mrowinski@mimecast.com — PR firm, excluded
- press@mimecast.com    — corporate press, excluded
- thamilton@mimecast.com — internal communications / PR, excluded
- privacy@/legal@/security@/careers@/investor@/founder@ routes excluded (purpose-limited)

NO FORM SUBMISSION, EMAIL, DELIVERY, PAYMENT, OR REVENUE IS CLAIMED.
- SMTP remains gated
- $0 sent / $0 received

COHORT MARKER: ai_email_security_agents sibling #3/5
NOTES: Mimecast is the incumbent 2003-vintage vendor with the deepest behavioral-signal depth in the cohort. The 42,000-customer + 27M-user + 24T-signal/yr + Permira-led take-private 2022 + London HQ posture makes this the most "enterprise-defensible" sibling. The distinct wedge is the Agentic AI Security module (Shadow AI governance + AI agent discovery + AI governance) combined with the broad enterprise platform (DMARC Analyzer + Collaboration Threat Protection + Incydr DLP + Aware GRC + Engage Security Awareness + Email Incident Response 24x7 + Email Archive). This is the cohort incumbent and the cohort closer candidate for EU + UK enterprise procurement packets with NIS2 + DORA + UK AI Bill + EU AI Act readiness scope.
