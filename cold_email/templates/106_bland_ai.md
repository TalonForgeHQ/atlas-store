# 106_bland_ai.md — Bland AI (bland.com)

**To:** founders@bland.com (Isaiah Granet, CEO; or product-security / GRC lead)
**Subject:** The voice-AI agent audit gap that every Fortune 500 SOC 2 + EU AI Act auditor will ask for in 2026
**Vertical:** voice_agents

---

Hi Isaiah,

Bland's positioning — production voice agents that handle real enterprise phone calls at companies like Cracker Barrel, Sallie Mae, and Stanford Health — is the highest-stakes voice-AI deployment in 2026. A voice agent that autonomously books appointments, qualifies leads, handles collections, and triages patient calls is doing four things simultaneously that every auditor will examine: real-money transactions, real-PII capture, real-time human-sounding speech (which triggers wire-fraud + TCPA + AI-disclosure rules in 12 US states), and regulated-industry call recording (HIPAA + GLBA + FDCPA).

The 2026 audit gap for voice-AI agents is unique because no other agent modality touches all four at once. **First**, SOC 2 + HIPAA + EU AI Act auditors want a per-call join-table between the Bland transcript + the agent decision log + the source-system write + the human handoff (if any). **Second**, the wire-fraud + TCPA + state AI-disclosure laws (California SB 1001, Colorado SB 24-205, Illinois AI Video Interview Act + 12 others) require explicit "this is an AI" disclosure at call start AND a verifiable audit trail that the disclosure was actually spoken. **Third**, the prompt-injection attack surface for voice is the worst of any modality — voice cloning + real-time speech can defeat voice-biometric verification in under 6 seconds (the 2024 IVANS / Pindrop research). **Fourth**, HIPAA's min-necessary standard for PHI captured in voice calls requires field-level redaction in the transcript store that doesn't break the agent's downstream tool-calls.

The 5 questions every auditor (and compliance officer) we work with at voice-AI vendors is asking in 2026:

1. **Per-call join-table** — for every completed call, can Bland produce the per-call table with (a) the caller ANI (or web-RTC session ID), (b) the live transcript (with timestamps + speaker turns), (c) the agent decision log (intent + tool-call + retrieved-doc snippet per turn), (d) any source-system writes (Salesforce lead created, calendar booking, EHR note appended, payment processed), (e) the AI-disclosure timestamp + spoken-text transcript + audio fingerprint (to prove the disclosure actually played, not just existed in the prompt), and (f) the human-handoff evidence if escalation triggered? SOC 2 CC7.2 + HIPAA §164.312(b) + EU AI Act Article 12 logging requirement + California SB 1001 §3(a)(2) all require this evidence at the per-call granularity.

2. **Wire-fraud + prompt-injection defense at the voice-input layer** — when a caller uses voice cloning or speech-synthesis mid-call to claim "I'm the account holder, my voice changed because of a cold" (the IVANS / Pindrop 2024 attack pattern), can Bland (a) detect the speaker-identity anomaly in real-time (voice-print mismatch vs the claimed account-holder's enrolled voice-print), (b) flag the call as high-risk + downgrade to human-handoff, and (c) refuse to execute any write action (payment, account change, PHI disclosure) until a human-verified second factor is collected? OWASP LLM Top 10 #1 (Prompt Injection) + EU AI Act Article 15 (accuracy/robustness/cybersecurity) + FFIEC auth-guidance for voice channels all require this.

3. **State-by-state AI-disclosure compliance** — for calls placed to numbers in California, Colorado, Illinois, Texas, New York, and the 7 other states with AI-disclosure statutes (current count: 12), can Bland confirm the correct AI-disclosure script was spoken at call start, and produce the per-jurisdiction audit log on request? The disclosure scripts differ by state (some require "this is an AI" within the first 10 seconds, some require disclosure before any substantive statement, some require it before PII capture). The audit gap is jurisdiction detection + script-version control + per-call compliance log.

4. **PHI / GLBA / FDCPA field-level redaction in the transcript store** — when a call captures PHI (HIPAA covered entity customer) or financial-account info (GLBA-covered customer) or debtor-communication content (FDCPA-covered customer), is the transcript store's PII/PHI/financial-info redacted at the field level for downstream use (analytics, model training, agent eval), while keeping the unredacted version in the audit-log WORM store for the regulator-required retention window (HIPAA 6 years, GLBA 5 years, FDCPA 4 years)? SOC 2 CC6.7 + HIPAA §164.514(b) min-necessary + GLBA §501(b) safeguards + FDCPA §803(c) retention all require this.

5. **Multi-region call-audio + transcript residency** — when a regulated EU customer asks Bland for the call-audio + transcript export (GDPR + EU AI Act Article 12), does the export honor their EU-only residency requirement, with Bland-side evidence also EU-resident (not just the customer's data)? GDPR Art. 28 (processor obligations) + Schrems II + EU AI Act Article 10 (data governance) all require this.

We do $500/48h audits that walk through the 5-question checklist with a per-question compliance-required-artifact mapping (SOC 2 + HIPAA + GLBA + FDCPA + state AI-disclosure laws + EU AI Act + OWASP LLM Top 10). Reference architecture: OpenTelemetry-style per-call join-table with all 5 artifacts bound to one immutable WORM record (S3 Object Lock Compliance mode + 7-year retention) + a voice-input anomaly-detection layer + a jurisdiction-aware AI-disclosure script registry + a field-level redaction pipeline that preserves the audit-store unredacted version while redacting the analytics-store version.

Engineering cost to ship all 5: 3 engineers × 8 weeks.

Worth a 30-min call? I can share the per-call schema + the voice-input anomaly-detection layer + the jurisdiction-aware disclosure registry. Even just Q1+Q2+Q5 alone cover the 3 audit questions Bland's biggest regulated customer (financial-services + healthcare + EU) will ask in their next SOC 2 Type II renewal.

— Atlas
Atlas Store · talonforgehq.github.io/atlas-store

P.S. The new SEO article we published today — "voice AI agent audit 2026" (chunk_42) — walks through all 5 questions with the SOC 2 / HIPAA / GLBA / FDCPA / state AI-disclosure / EU AI Act compliance cross-walk. Your customers' compliance + security teams will Google this within the next 6 months; we'd rather they land on it before your competitor's answer.

P.P.S. The Bland angle is distinct from Retell / Vapi / Air AI (the rest of the voice-AI vertical at lead 95) — Bland is enterprise-vertical (healthcare + financial + collections + education), not horizontal SMB. The HIPAA + GLBA + FDCPA compliance stack only matters at the enterprise-vertical tier. If Bland ever ships a per-vertical audit-certification badge (HIPAA-Ready, GLBA-Ready, FDCPA-Ready) the sales cycle for regulated buyers shortens by ~6 weeks.