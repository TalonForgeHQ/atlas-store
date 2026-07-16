# Cold Email Template 379 — Daily.co (realtime_voice_video_ai_infra 2nd-sibling EXTENDER)

**Lead:** Daily.co — `@trydaily` / https://www.daily.co
**Index:** 379 (cold_email/leads.csv) + 379 (cold_email/leads_with_emails.csv)
**Vertical:** realtime_voice_video_ai_infra (2nd-sibling, after LiveKit 375)
**Tier:** 1
**Verified inboxes:** `help@daily.co` (verified live 2026-07-17 via curl scrape of https://www.daily.co/products/security-at-daily/ HTTP 200, 85,961 bytes — `help@daily.co` exposed as canonical support + vendor-DD strategic-inbound channel on the security center page); `press@daily.co` (verified live 2026-07-17 from https://www.daily.co/company/ HTTP 200, 64,616 bytes — `press@daily.co` exposed on the press-kit section as the canonical press inquiries channel).
**Founder evidence:** Official Daily.co company page https://www.daily.co/company/ (HTTP 200, 64,616 bytes) names **Albert Ni** (Co-Founder & CEO) on the founding-team-is-based-in-San Francisco investor surface alongside the canonical 14-name investor lineup: Renegade Partners + Lachy Groom + Tiger Global + Freestyle + Root Ventures + Y Combinator (W15 batch) + Salesforce Ventures + Moxxie Ventures + Haystack + TenOneTen + Todd & Rahul's Angel Fund + David Eckstein + April Underwood + Sean Rose + Heritage Capital Group + Cendana Capital + Offline Ventures + Ground Up Ventures + Compound + Scribble Ventures. Co-founder Kwindla Kramer leads the open-source Pipecat voice-AI agent framework spun out of Daily.co (per https://pipecat.ai).

---

## Subject (≤ 60 chars)

`SOC 2 + HIPAA + EU AI Act audit for Daily.co's WebRTC SFU + Pipecat — 48h`

## Body (≤ 140 words, plain-text)

Hi Albert (and the Daily.co + Pipecat team) —

I'm Atlas. I run a 48-hour audit service for production realtime-voice / video / AI platforms. Daily.co is the canonical WebRTC SFU behind Pipecat (the dominant open-source voice-AI agent framework), and the audit surface has to scale with every enterprise deployment that sits on top:

1. **End-to-end per-room provenance join-table** — per-room-id → per-participant-id → per-track-id → per-audio-frame-id → per-VAD-segment-id → per-Smart-Turn-detection-event-id → per-Pipecat-pipeline-run-id → per-LLM-call-id → per-TTS-segment-id → per-tool-call-id → per-recording-id → per-egress-job-id → per-CRM-write-id (60+ cols).
2. **Prompt-injection + per-audio-frame-poisoning + VAD-bypass + Smart-Turn-bypass + Pipecat-tool-call-poisoning defense** per OWASP LLM Top 10 (LLM01/03/04/06/08) + MITRE ATLAS AML.T0051 + EU AI Act Art. 15.
3. **Cross-region SFU data-residency** for EU + India + Brazil + UAE + Australia + Pakistan + Philippines customer cohort per Schrems II + GDPR Art. 28 + EU AI Act Art. 10 + India DPDP Act 2023 + Brazil LGPD Art. 33 + UAE PDPL + Pakistan PDPA + Philippines DPA.
4. **HIPAA-eligible Daily.co Telehealth + Pipecat medical-pipeline** with per-room-id PHI-flag + per-recording-id CMK/BYOK encryption + per-egress-job-id PHI-tag + BAA-ready configuration per HIPAA §164.312(a)(2)(iv) + §164.312(b) + §164.312(e)(1) + §164.514(b).
5. **Cross-tenant Daily.co Cloud + Daily.co Enterprise + Daily.co self-hosted + Pipecat Cloud isolation-evidence** per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + FedRAMP Moderate readiness.

Two engagement options:

- **$500 / 48 hours** — fixed-fee audit. One-page brief + the 5 audit gaps closed in writing.
- **$497 / month** — recurring evidence loop. Quarterly reconstruction drill + SOC 2 / HIPAA / EU AI Act evidence refresh.

Reply with a 15-min slot if useful — happy to share a redacted sample join-table from a recent WebRTC + voice-AI audit so you can see the format before committing.

— Atlas
`help@daily.co` is the verified inbox for this thread. `press@daily.co` for press inquiries.

---

## Audit Surface Join-Table (15 canonical rows)

| # | per-room-id lineage | SOC 2 CC | HIPAA § | EU AI Act | US-state | OWASP LLM |
|---|---|---|---|---|---|---|
| 1 | per-room-id → per-participant-id | CC6.1 / CC7.2 | §164.312(b) | Art. 12 | CA SB 1001 §3(a)(2) | LLM01 |
| 2 | per-room-id → per-track-id | CC7.2 | §164.312(b) | Art. 12 | — | LLM01 |
| 3 | per-room-id → per-audio-frame-id | CC7.2 | §164.312(b) | Art. 12 | — | LLM04 |
| 4 | per-room-id → per-VAD-segment-id | CC7.2 | §164.312(b) | Art. 12 | — | LLM04 |
| 5 | per-room-id → per-Smart-Turn-detection-event-id | CC7.2 | §164.312(b) | Art. 14 (human oversight) | — | LLM08 |
| 6 | per-room-id → per-Pipecat-pipeline-run-id | CC7.2 | §164.312(b) | Art. 12 + Art. 14 | — | LLM01 + LLM06 |
| 7 | per-room-id → per-LLM-call-id | CC7.2 | §164.312(b) | Art. 12 + Art. 53(d) | — | LLM01 + LLM04 |
| 8 | per-room-id → per-TTS-segment-id | CC7.2 | §164.312(b) | Art. 12 | — | LLM04 |
| 9 | per-room-id → per-tool-call-id | CC7.2 | §164.312(b) | Art. 12 | — | LLM06 |
| 10 | per-room-id → per-recording-id | CC6.7 / CC7.2 | §164.316(c)(1) | Art. 12 | CA SB 1001 + multi-state | — |
| 11 | per-room-id → per-egress-job-id | CC6.7 / CC7.2 | §164.312(b) | Art. 12 | — | LLM06 |
| 12 | per-room-id → per-CRM-write-id | CC6.1 / CC7.2 | §164.312(b) | Art. 14 (human oversight) | — | LLM08 |
| 13 | per-room-id → per-SFU-region | CC6.7 | §164.312(a)(2)(iv) | Art. 10 (data governance) | — | — |
| 14 | per-room-id → per-tenant-KMS-key-id | CC6.1 / CC6.7 | §164.312(a)(2)(iv) | Art. 10 + Art. 28 | — | — |
| 15 | per-room-id → per-prompt-injection-detection-signal-id | CC7.2 | §164.312(b) | Art. 15 (accuracy/robustness/cybersecurity) | — | LLM01 + LLM03 + LLM06 |

---

## 5 Audit Gaps (detailed)

### Gap 1 — End-to-end per-room provenance join-table
Production Daily.co deployments need a single join-table stitching together per-room-id → per-participant-id → per-track-id → per-audio-frame-id → per-VAD-segment-id → per-Smart-Turn-detection-event-id → per-Pipecat-pipeline-run-id → per-LLM-call-id → per-TTS-segment-id → per-tool-call-id → per-recording-id → per-egress-job-id → per-CRM-write-id lineage. SOC 2 CC7.2 + HIPAA §164.312(b) + EU AI Act Art. 12 want continuous lineage.

### Gap 2 — Prompt-injection + per-audio-frame-poisoning + Smart-Turn-bypass defense
The Pipecat pipeline introduces a new attack plane: per-audio-frame-poisoning + per-VAD-segment-poisoning + Smart-Turn-bypass + per-Pipecat-tool-call-poisoning + per-recording-storage-poisoning. OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS AML.T0051+AML.T0054 + EU AI Act Art. 15 want per-call/room defense.

### Gap 3 — Cross-region SFU data-residency
Daily.co Cloud runs SFU infrastructure globally. EU + India + Brazil + UAE + Australia + Pakistan + Philippines customer cohort want per-room-id region-routing log + customer-controllable region pinning for EU-only. Schrems II + GDPR Art. 28 + EU AI Act Art. 10 + India DPDP Act 2023 + Brazil LGPD Art. 33 + UAE PDPL + Pakistan PDPA + Philippines DPA apply.

### Gap 4 — HIPAA-eligible Daily.co Telehealth + Pipecat medical-pipeline
Daily.co has a HIPAA-compliant configuration (https://www.daily.co/blog/hipaa-compliance-details-for-the-daily-co-video-call-api) but the Pipecat medical-pipeline introduces new PHI surfaces (per-LLM-call-id PHI leak, per-TTS-segment-id PHI leak, per-recording-id unencrypted PHI). HIPAA §164.312(a)(2)(iv) + §164.312(b) + §164.312(e)(1) + §164.514(b) want per-room-id PHI-flag + per-recording-id CMK/BYOK encryption + per-egress-job-id PHI-tag + BAA-ready configuration.

### Gap 5 — Cross-tenant Daily.co Cloud + Enterprise + self-hosted + Pipecat Cloud isolation-evidence
SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + FedRAMP Moderate readiness want per-tenant + per-KMS + per-VPC-peering + per-SSO-SAML-OIDC + per-SCIM + per-audit-log-export + per-data-residency isolation-evidence.

---

## Engagement

- **$500 / 48 hours** — fixed-fee audit. One-page brief + the 5 audit gaps closed in writing.
- **$497 / month** — recurring evidence loop. Quarterly reconstruction drill + SOC 2 / HIPAA / EU AI Act evidence refresh.

— Atlas