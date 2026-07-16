---
template: 380_agora.md
lead_id: 380
company: Agora
handle: "@AgoraIO"
inbox: privacy@agora.io
vertical: realtime_voice_video_ai_infra
tier: 1
subject: "SOC 2 + HIPAA + EU AI Act audit for Agora's 60B+ minute SD-RTN — 48h"
send_status: send_ready
---

# Agora — vendor-DD audit cold opener (Lead 380)

## Why Agora (the one-line hook)

Agora powers **60B+ minutes of live voice/video per month across 200+ countries** via SD-RTN, including the Agora Conversational AI SDK on top of the SFU. You're the only public-company Tier-1 vendor in `realtime_voice_video_ai_infra` (NYSE: API) and the canonical HIPAA-regulated telehealth SFU — every audit committee in 2026 wants per-room provenance across SD-RTN + Conversational AI + Cloud Recording.

## The 5 audit questions

1. **Per-room provenance:** can you reconstruct end-to-end `per-room-id → per-channel-id → per-uid-id → per-track-id → per-audio-frame-id → per-VAD-segment-id → per-STT-segment-id → per-LLM-call-id → per-prompt-version-id → per-completion-id → per-TTS-segment-id → per-tool-call-id → per-handoff-event-id → per-cloud-recording-id → per-recording-storage-region → per-on-premise-recording-flag → per-downstream-CRM-write-id → per-downstream-billing-id` in one join, on demand, for any channel in the last 13 months, against SOC 2 CC7.2 + HIPAA §164.312(b) + EU AI Act Art. 12?
2. **Prompt-injection + audio-poisoning defense:** what's your control set across the Agora Conversational AI SDK pipeline against OWASP LLM Top 10 LLM01 (prompt injection) + LLM03 (training-data poisoning) + LLM04 (model DoS) + LLM06 (sensitive disclosure) + LLM08 (vector/embedding poisoning) + MITRE ATLAS AML.T0051 + AML.T0054, measured at the per-audio-frame + per-VAD-segment + per-LLM-call-message + per-TTS-segment + per-tool-call + per-cloud-recording granularity?
3. **Cross-region data residency:** SD-RTN routes through 200+ regions — is per-channel-region selection auditable per Schrems II + GDPR Art. 28 + EU AI Act Art. 10 + India DPDP Act 2023 + Brazil LGPD Art. 33 + UAE PDPL + China PIPL + Singapore PDPA + Philippines DPA, with per-tenant region-locking enforceable?
4. **HIPAA-eligible Agora Telehealth:** does the Agora Telehealth configuration ship per-room-id PHI-flag + per-cloud-recording-id CMK/BYOK encryption + per-on-premise-recording-PHI-tag + BAA-ready configuration satisfying HIPAA §164.312(a)(2)(iv) + §164.312(b) + §164.312(e)(1) + §164.514(b) min-necessary?
5. **Cross-tenant isolation:** for Agora Cloud + Agora Enterprise + Agora On-Premise + per-app-id + per-certificate-id + per-token-id surfaces, can you evidence per-tenant isolation per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + FedRAMP Moderate readiness, with breach-detection-event-id fed into a downstream SIEM?

## The offer

**$500 / 48h fixed-fee audit.** I deliver a one-page evidence map: which Agora surfaces pass each of the 5 questions, which need evidence added, and the exact minimum column set your audit committee needs. No retainer, no obligation.

If it lands, the recurring **$497/mo evidence loop** keeps the per-room provenance join-table current as you ship new Conversational AI SDK + Telehealth features — so the next vendor-DD questionnaire is a one-query pull instead of a 6-week fire drill.

## The canonical 15-row per-room provenance join-table (Agora SD-RTN edition)

| # | Column | Source surface | Maps to |
|---|---|---|---|
| 1 | `per-room-id` | Agora Video/Voice SDK | SOC 2 CC7.2 |
| 2 | `per-channel-id` | Agora Real-Time Messaging | HIPAA §164.312(b) |
| 3 | `per-uid-id` | Agora Token Service | EU AI Act Art. 12 |
| 4 | `per-track-id` | Agora Media SDK | OWASP LLM LLM01 |
| 5 | `per-audio-frame-id` | Agora Media SDK | MITRE ATLAS AML.T0051 |
| 6 | `per-VAD-segment-id` | Agora Conversational AI SDK | OWASP LLM LLM03 |
| 7 | `per-STT-segment-id` | Agora Conversational AI SDK | HIPAA §164.514(b) |
| 8 | `per-LLM-call-id` | Agora Conversational AI SDK | EU AI Act Art. 10 |
| 9 | `per-prompt-version-id` | Agora Conversational AI SDK | EU AI Act Art. 53(d) |
| 10 | `per-TTS-segment-id` | Agora Conversational AI SDK | OWASP LLM LLM04 |
| 11 | `per-tool-call-id` | Agora Conversational AI SDK | OWASP LLM LLM08 |
| 12 | `per-cloud-recording-id` | Agora Cloud Recording | HIPAA §164.312(a)(2)(iv) |
| 13 | `per-recording-storage-region` | Agora Cloud Recording S3 | Schrems II + PIPL |
| 14 | `per-on-premise-recording-flag` | Agora On-Premise Recording | GDPR Art. 28 |
| 15 | `per-downstream-CRM-write-id` | Customer webhook target | SOC 2 CC6.1 + CCPA/CPRA |

The full 60-col version (extending to per-VPC-peering-id + per-SSO-SAML-OIDC-id + per-SCIM-provisioning-id + per-tenant-KMS-key-id + per-prompt-injection-detection-signal-id + per-voice-cloning-detection-signal-id + per-wire-fraud-detection-signal-id + per-TCPA-prior-express-consent-link-id + per-AI-disclosure-script-version-id + per-jurisdiction-detection-id + per-human-handoff-evidence-id + per-PHI-flag + per-recording-encryption-key-id + per-GLBA-flag + per-PCI-DSS-flag + per-FDCPA-flag + per-cross-border-transfer-sccs-version-US-EU + per-tenant-isolation-flag + per-breach-detection-event-id + per-SFU-region + per-egress-job-region + per-downstream-CRM-region + per-billing-account-id + per-API-key-id + per-app-id + per-certificate-id + per-token-id + per-session-id + per-deployment-id + per-deployment-version-id) lives in `chunk_227.html`.

## Founder evidence

Agora was founded in 2013 by **Tony Zhao** (Founder + former CEO, now Chairman; ex-WebEx engineer). Current CEO **Tony Wang** runs day-to-day operations. Both names appear on the official Agora management page at https://www.agora.io/en/agora-management/ (HTTP 200; carries `tony-zhao.webp` + `tony-wang.webp` headshot images). Agora IPO'd on the NYSE under ticker **API** in June 2020. HQ: 2804 Mission College Blvd, Santa Clara CA 95054.

## Compliance posture

SOC 2 Type II + ISO 27001 + ISO 27017 + ISO 27018 + ISO 27701 + GDPR DPA + CCPA/CPRA + COPPA + HIPAA-ready + EU AI Act readiness, surfaced via agora.io/en/compliance. The HIPAA-eligible Agora Telehealth configuration ships per-room-id PHI-flag + per-cloud-recording-id CMK/BYOK encryption + BAA-ready configuration per HIPAA §164.312(a)(2)(iv) + §164.312(b) + §164.312(e)(1) + §164.514(b).

## Subject line + opener

**Subject:** SOC 2 + HIPAA + EU AI Act audit for Agora's 60B+ minute SD-RTN — 48h

**Opener (≤ 50 words):**

> Hi Tony / Agora team — I run Atlas, a 60-second per-room audit for WebRTC SFU + voice-AI-agent stacks. Fixed-fee $500 / 48h. Five questions on per-room provenance + prompt-injection defense + cross-region residency + HIPAA Telehealth + cross-tenant isolation — interested?

— Atlas @ Talon Forge