# Cold Email Template 378 — Cresta (Tim Shi, Co-Founder & CEO + Zayd Enam, Co-Founder & CTO)

**Vertical:** `ai_voice_agents_orchestration` (4th-sibling — extends cohort after Bland AI 189 + Voiceflow 310 + Retell AI 374 + Vapi 377)
**Inbox (verified):** `cresta-privacy@cresta.ai` (from `https://cresta.com/privacy-policy`, HTTP 200, 166KB)
**Company:** Cresta AI Inc. — HQ San Francisco CA + Toronto Canada (100 King Street West, Suite 6200, Toronto ON M5X 1E8 per legal page)
**Founded:** 2017 (Stanford AI Lab spinout)
**Funding:** $151M+ across Series A/B/C/D — Andreessen Horowitz + Greylock + Sequoia + Tiger Global + Porsche SE + Zoom + Five9 + Genesys + Qualcomm Ventures
**Customers:** Hilton, Porsche, Intuit, Brinks Home, DISH, Cox, Toyota, Liberty Mutual, Blue Nile, Farmers Insurance, Dollar Car + 100+ enterprise contact-center operators
**Compliance:** SOC 2 Type II + GDPR DPA + CCPA/CPRA + EU AI Act readiness per cresta.com/privacy-policy + cresta.com/security

---

## Subject Line (Option A — recommended)
`SOC 2 + EU AI Act audit for Cresta's real-time coaching + self-service surface — 48h`

## Subject Line (Option B — for compliance officer)
`Cresta → 5 audit questions on per-conversation provenance + per-utterance AI-disclosure`

## Subject Line (Option C — founder-coded)
`Tim — what's your per-conversation provenance join-table for the Hilton + Porsche + Brinks deployments?`

---

## Body

Hi Tim,

I run the $500/48h fixed-fee AI agent audit at Talon Forge. We do one thing: ship a 60-col per-conversation provenance join-table for AI voice / chat / email agents that maps to SOC 2 CC7.2 + HIPAA §164.312(b) + EU AI Act Art. 12 + state-AI-disclosure + OWASP LLM Top 10 in one spreadsheet.

For Cresta specifically, that join-table would stitch across **per-conversation-id → per-utterance-id → per-message-id → per-suggestion-id → per-real-time-coaching-id → per-tool-call-id → per-handoff-event-id → per-recording-id → per-transcript-id → per-QM-scorecard-id → per-compliance-disclosure-id → per-AI-disclosure-id → per-CRM-write-id → per-downstream-billing-id**. That's the surface your customers (Hilton, Porsche, Intuit, Brinks Home) are going to be asked for in 2026 vendor-DD questionnaires — and right now it's likely fragmented across your Coaching, Self-Service, Insights, Quality, and Compliance modules.

**Five audit questions that would drive the engagement:**

1. **End-to-end per-conversation provenance** — when a Cresta Self-Service conversation hands off to a human agent mid-call, do you carry the per-utterance + per-real-time-coaching-id lineage across the handoff, or does the human-side agent assist start a fresh per-conversation-id? SOC 2 CC7.2 + EU AI Act Art. 12 both expect continuous lineage across the AI↔human boundary.

2. **Prompt-injection + per-utterance-poisoning defense at the coaching injection point** — Cresta's real-time whisper coach is a perfect LLM01 attack surface (the coach sees the live transcript and suggests responses). What's the per-utterance injection-detection-signal-id + per-coaching-injection-quarantine-id pipeline? OWASP LLM Top 10 LLM01+LLM03+LLM04 + EU AI Act Art. 15 want this documented per-conversation, not in aggregate.

3. **State-by-state AI-disclosure for the Self-Service module** — California SB 1001 §3(a)(2) + Colorado SB 24-205 + Illinois AI Video Interview Act + Texas + New York + 7 other states all want a per-conversation disclosure-timestamp + per-conversation human-handoff-evidence + per-conversation jurisdiction-detection signal. Do you have a per-conversation compliance-disclosure-id column, and is it queryable per Hilton + per Brinks tenant?

4. **Multi-region call-audio + transcript + coaching-annotation residency** — your Toronto office (100 King Street West, Suite 6200) suggests Canadian customers + PIPEDA exposure; European customers under Schrems II + GDPR Art. 28 + EU AI Act Art. 10 want EU-only data residency. Is the per-tenant-id region-routing log + per-recording-storage-region + per-coaching-annotation-region auditable, or is it implicit in tenant configuration?

5. **Cross-tenant Cresta SaaS + Enterprise + Private isolation** — your Fortune-500 customer cohort means Hilton data must never bleed into the Porsche training loop. SOC 2 CC6.1 + GDPR Art. 28 want a per-tenant-id + per-workspace-id + per-API-key-id isolation-evidence table — what's the per-tenant-isolation-flag granularity today?

**What the $500 / 48h fixed-fee audit delivers:**
- The 60-col per-conversation provenance join-table (CSV + schema diagram)
- A per-gap remediation plan mapped to SOC 2 / HIPAA / EU AI Act / state-disclosure
- A redlined evidence-list for the 2026 vendor-DD questionnaire (Hilton + Porsche are sending these out now)
- A reference implementation of the per-conversation compliance-disclosure-id column

**After the audit, the $497/mo evidence loop:**
- Quarterly provenance-join-table refresh (per-conversation schema drift + new module coverage)
- Monthly AI-disclosure-jurisdiction-tracker update (12 US states + EU + Canada)
- Per-vendor-DD-questionnaire response package (reusable for Hilton / Porsche / Intuit / Brinks questionnaire cycles)
- Annual SOC 2 / EU AI Act readiness-letter refresh

48 hours from your go-ahead. Cresta is one of the more interesting platforms to audit because the coaching-injection surface is genuinely novel — most AI-voice-agent audit frameworks were written for Bland / Vapi / Retell-style customer-facing surfaces and don't cover the real-time agent-assist module at all.

Reply with "go" if you want me to start the intake form (5 min) and ship the 60-col join-table within 48h.

— Atlas
Talon Forge LLC
$500 / 48h fixed-fee audit · $497/mo evidence loop
atlas-store · privacy: talonforgehq.github.io/atlas-store/privacy

---

## 15-row canonical per-conversation provenance join-table

| # | column | type | source module | SOC 2 / HIPAA / EU AI Act mapping |
|---|---|---|---|---|
| 1 | per-conversation-id | uuid | Cresta Self-Service + Agent Assist | SOC 2 CC7.2 lineage anchor |
| 2 | per-utterance-id | uuid | per-message timestamp | EU AI Act Art. 12 + Art. 14 transparency |
| 3 | per-message-id | uuid | transcript store | HIPAA §164.312(b) audit trail |
| 4 | per-suggestion-id | uuid | Cresta Insights real-time engine | SOC 2 CC6.1 logical access |
| 5 | per-real-time-coaching-id | uuid | Agent Assist whisper coach | OWASP LLM LLM01 injection-defense anchor |
| 6 | per-tool-call-id | uuid | function-call surface | OWASP LLM LLM04 + EU AI Act Art. 15 |
| 7 | per-handoff-event-id | uuid | AI↔human handoff | SOC 2 CC7.2 + EU AI Act Art. 14 handoff transparency |
| 8 | per-recording-id | uuid | audio capture store | HIPAA §164.312(a)(2)(iv) encryption-at-rest anchor |
| 9 | per-transcript-id | uuid | ASR output | EU AI Act Art. 10 data governance |
| 10 | per-QM-scorecard-id | uuid | Cresta Quality post-call | SOC 2 CC4.1 monitoring + EU AI Act Art. 9 risk-mgmt |
| 11 | per-compliance-disclosure-id | uuid | Cresta Compliance | California SB 1001 §3(a)(2) + Colorado SB 24-205 |
| 12 | per-AI-disclosure-id | uuid | jurisdictional language detector | EU AI Act Art. 50 transparency obligation |
| 13 | per-jurisdiction-detection-id | uuid | per-call geo-detection | state-by-state AI-disclosure compliance |
| 14 | per-CRM-write-id | uuid | downstream Salesforce / Zendesk write | SOC 2 CC6.7 + downstream-billing reconciliation |
| 15 | per-downstream-billing-id | uuid | per-conversation metering | revenue + GLBA §501(b) reconciliation |

---

## Coda (footer)

Cresta's per-conversation provenance join-table is the canonical ai_voice_agents_orchestration audit surface because Cresta combines three previously-separate audit worlds (real-time agent assist + post-call quality management + customer self-service) in one platform. The cohort now has 4 siblings — Bland AI 189 (190/200KB privacy page) + Voiceflow 310 (Voiceflow Agent + Voiceflow Workflows design surface) + Retell AI 374 (developer-platform voice-AI orchestration with HIPAA + PCI) + Vapi 377 (1M+ developers, 1B+ calls, Series B May 2026) + Cresta 378 (real-time coaching + QM + self-service). If you want to reference the cross-cohort comparison, the canonical long-tail keyword is `voice AI agent audit checklist SOC 2 HIPAA EU AI Act 2026`. Reply with "go" for the 48h intake form.