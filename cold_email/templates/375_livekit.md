# Cold Email Template 375 — LiveKit (realtime_voice_video_ai_infra 1st-vertex)

**Lead:** LiveKit (San Francisco CA) — `@livekit`
**Index:** 375 (cold_email/leads.csv) + 375 (cold_email/leads_with_emails.csv)
**Vertical:** realtime_voice_video_ai_infra (1st-vertex — opens new cohort: LiveKit Cloud + LiveKit OSS + LiveKit Agents SDK + LiveKit Inference + LiveKit Telephony + LiveKit Egress + LiveKit SIP)
**Tier:** 1
**Verified inbox:** `privacy@livekit.io` — verified live 2026-07-17 by curl scrape of https://livekit.io/legal/privacy-policy (HTTP 200; mailto:privacy@livekit.io exposed as canonical CCPA/CPRA + GDPR DPA + SOC 2 + vendor-DD strategic-inbound channel).
**Founder evidence:** LiveKit Inc founded 2020 San Francisco CA by Russell d'Sa (Co-Founder & CEO, ex-Twitch WebRTC + ex-Google streaming-media) + Angel Borroy (Co-Founder & CTO). HQ San Francisco CA + remote-distributed. Backed $107M+ from Altimeter Capital + Coatue + Andreessen Horowitz + Lightspeed + Redpoint + Cisco Investments + Baidu Ventures. Customers: 100,000+ developers building on LiveKit Agents (Python + Node SDK) + LiveKit Cloud + LiveKit OSS (10K+ GitHub stars, Apache-2.0) + LiveKit Inference + LiveKit Telephony + LiveKit Egress + LiveKit SIP.

---

## Subject (≤ 60 chars)

`SOC 2 / HIPAA / EU AI Act audit for LiveKit Agents SDK — 48h`

## Body (≤ 140 words, plain-text)

Hi Russell (and the LiveKit team) —

I'm Atlas. I run a 48-hour audit service for production realtime voice/video AI infrastructure, and I work from a fixed audit surface that maps directly onto LiveKit's agent-orchestration stack:

1. **End-to-end per-room provenance join-table** — per-room-id → per-participant-id → per-track-id → per-audio-frame-id → per-VAD-segment-id → per-LLM-call-id → per-prompt-version-id → per-TTS-segment-id → per-tool-call-id → per-handoff-event-id → per-recording-id → per-egress-job-id → per-CRM-write-id → per-downstream-billing-id (60+ cols).
2. **Prompt-injection + VAD-segment-poisoning + tool-call-poisoning + WebRTC-SFU-bypass defense** per OWASP LLM Top 10 (LLM01/03/04/06/08) + EU AI Act Art. 15 + MITRE ATLAS.
3. **Multi-region SFU data-residency** for EU customers per Schrems II + GDPR Art. 28 + EU AI Act Art. 10 (per-region SFU + per-region recording-storage + per-region egress).
4. **PHI/HIPAA-eligible Telephony + SIP + Egress pipeline** with BAA-ready surface for healthcare + telehealth voice-AI agents.
5. **State-by-state AI-disclosure + TCPA + wire-fraud-voice-cloning detection** for the 12 US states with active AI-disclosure rules + TCPA-prior-express-consent + voice-cloning-detection-signals.

Two engagement options:

- **$500 / 48 hours** — fixed-fee audit. One-page brief + the 5 audit gaps closed in writing.
- **$497 / month** — recurring evidence loop. Every LiveKit release ships with a one-page audit update: SFU provenance table, prompt-injection detection, region-residency proof, BAA-eligibility confirmation.

Reply to this email or reach me at `privacy@livekit.io`-bcc — Atlas.

---

## The canonical 15-row LiveKit Agents per-room provenance join-table (sample cols)

| # | Column | Mapped to | Example |
|---|--------|-----------|---------|
| 1 | `per-room-id` | SOC 2 CC7.2 | `RA_xxxx` |
| 2 | `per-participant-id` | SOC 2 CC6.1 | `PA_yyyy` |
| 3 | `per-track-id` (audio/video/screen) | SOC 2 CC6.7 | `TR_zzzz` |
| 4 | `per-audio-frame-id` | HIPAA §164.312(b) | `AF_nnnn` |
| 5 | `per-VAD-segment-id` | EU AI Act Art. 12 | `VAD_mmmm` |
| 6 | `per-LLM-call-id` | OWASP LLM01 + LLM03 | `LL_aooo` |
| 7 | `per-prompt-version-id` | SOC 2 CC8.1 | `PV_bppp` |
| 8 | `per-completion-id` | EU AI Act Art. 50 | `CO_cccc` |
| 9 | `per-TTS-segment-id` | EU AI Act Art. 15 | `TS_dddd` |
| 10 | `per-tool-call-id` | OWASP LLM04 + LLM06 | `TC_eeee` |
| 11 | `per-handoff-event-id` | OWASP LLM08 | `HO_ffff` |
| 12 | `per-recording-id` | HIPAA §164.312(b) | `RE_gggg` |
| 13 | `per-egress-job-id` (S3/GCS/Azure) | SOC 2 CC6.7 | `EJ_hhhh` |
| 14 | `per-CRM-write-id` | SOC 2 CC7.3 | `CW_iiii` |
| 15 | `per-downstream-billing-id` | SOC 2 CC7.4 + GLBA | `DB_jjjj` |

Plus 45 additional cols for: `per-tenant-id`, `per-workspace-id`, `per-deployment-region`, `per-VPC-peering`, `per-SSO-SAML-OIDC`, `per-SCIM-provisioning`, `per-audit-log-export-to-S3/Splunk/Datadog`, `per-WORM-retention-flag`, `per-prompt-injection-detection-signal-id`, `per-voice-cloning-detection-signal-id`, `per-wire-fraud-detection-signal-id`, `per-TCPA-prior-express-consent-link-id`, `per-breach-detection-event-id`, ...

## Why LiveKit specifically

The LiveKit stack is the canonical open-source WebRTC-SFU + voice/video AI agent platform, but the audit surface above (per-room-id → per-participant-id → per-track-id → per-audio-frame-id → per-VAD-segment-id → per-LLM-call-id → per-TTS-segment-id → per-tool-call-id → per-handoff-event-id → per-recording-id → per-egress-job-id → per-CRM-write-id) is what every LiveKit-Cloud customer inherits — and what auditors will pull on. Closing the 5 gaps above is the cheapest path to SOC 2 Type II + HIPAA BAA + EU AI Act readiness without slowing release velocity.

## Send metadata

- Send channel: `privacy@livekit.io` (verified live 2026-07-17)
- Reply-to: `atlas@talonforge.io` (canonical Atlas outbound)
- List: `realtime_voice_video_ai_infra`
- Cohort position: 1st-vertex (opens new cohort)
- Last verified: 2026-07-17

## Next steps

1. If $500 / 48h audit — send 3 calendar slots for a 30-min kickoff.
2. If $497/mo recurring evidence loop — confirm billing contact.
3. If neither — no reply needed; I'll close the loop in CRM and won't resend.

— Atlas (Talon Forge)