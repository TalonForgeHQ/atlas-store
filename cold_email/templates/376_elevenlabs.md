# Cold Email Template 376 — ElevenLabs (ai_audio_voice_generation 1st-vertex)

**Lead:** ElevenLabs (London / New York / global) — `@elevenlabs`
**Index:** 376 (cold_email/leads.csv) + 376 (cold_email/leads_with_emails.csv)
**Vertical:** ai_audio_voice_generation (1st-vertex — opens a new cohort: ElevenLabs text-to-speech + speech-to-text + voice cloning + voice design + voice agents + dubbing + audio generation)
**Tier:** 1
**Verified inbox:** `legal@elevenlabs.io` — verified live 2026-07-17 by curl scrape of https://elevenlabs.io/privacy (HTTP 200, 540KB; official privacy page exposes the legal inquiry channel).
**Founder evidence:** Official ElevenLabs about-page JSON-LD names Mati Staniszewski (Co-Founder) and Piotr Dabkowski (Co-Founder & Research); the page states they met at a hackathon. Source: https://elevenlabs.io/about.

---

## Subject (≤ 60 chars)

`SOC 2 / AI Act audit for ElevenLabs voice agents — 48h`

## Body (≤ 140 words, plain-text)

Hi Mati and the ElevenLabs team —

I'm Atlas. I run a 48-hour audit service for production voice and audio AI, and I work from a fixed evidence surface that maps directly onto ElevenLabs' generation and agent stack:

1. **Per-request audio provenance** — per-user-id → per-project-id → per-voice-id → per-voice-clone-consent-id → per-text-input-id → per-audio-generation-id → per-model-version-id → per-output-download-id.
2. **Voice-cloning consent and misuse controls** — consent evidence, impersonation detection, disclosure scripts, abuse reports, and human escalation.
3. **Copyright and training-data provenance** — source/license records, model-version changes, synthetic/third-party audio boundaries, and deletion propagation.
4. **Agent execution lineage** — per-voice-agent-session-id → per-transcript-segment-id → per-tool-call-id → per-human-review-id → downstream action.
5. **Global privacy and retention** — region, tenant, KMS key, access/deletion request, retention-policy, and audit-log-export evidence.

Two engagement options:

- **$500 / 48 hours** — fixed-fee audit. One-page brief plus the five gaps closed in writing.
- **$497 / month** — recurring evidence loop. Each major voice/model release gets a provenance and disclosure evidence refresh.

If useful, reply with a 15-minute slot and I will send a redacted sample join-table first.

— Atlas
`legal@elevenlabs.io` is the verified inquiry channel for this thread.

---

## ElevenLabs audio provenance join-table (15 canonical rows)

| # | Lineage column | Control mapping | Evidence example |
|---|---|---|---|
| 1 | `per-user-id` | SOC 2 CC6.1 | `USR_001` |
| 2 | `per-project-id` | SOC 2 CC7.2 | `PRJ_002` |
| 3 | `per-voice-id` | ISO 42001 6.1 | `VOICE_003` |
| 4 | `per-voice-clone-consent-id` | GDPR Art. 7 | `CONSENT_004` |
| 5 | `per-text-input-id` | SOC 2 CC7.2 | `TXT_005` |
| 6 | `per-audio-generation-id` | SOC 2 CC7.2 | `AUDIO_006` |
| 7 | `per-model-version-id` | ISO 42001 8.4 | `MODEL_007` |
| 8 | `per-transcript-segment-id` | EU AI Act Art. 12 | `SEG_008` |
| 9 | `per-voice-agent-session-id` | EU AI Act Art. 14 | `SESSION_009` |
| 10 | `per-tool-call-id` | OWASP LLM06 | `TOOL_010` |
| 11 | `per-human-review-id` | EU AI Act Art. 14 | `REVIEW_011` |
| 12 | `per-copyright-provenance-id` | EU AI Act Art. 53 | `COPY_012` |
| 13 | `per-voice-impersonation-detection-id` | NIST AI RMF MEASURE | `MISUSE_013` |
| 14 | `per-deletion-event-id` | GDPR Art. 17 | `DELETE_014` |
| 15 | `per-audit-log-export-id` | SOC 2 CC7.3 | `EXPORT_015` |

Additional columns cover `per-tenant-id`, `per-region-id`, `per-KMS-key-id`, `per-API-key-id`, `per-retention-policy-id`, `per-AI-disclosure-id`, `per-prompt-injection-detection-id`, and `per-billing-event-id`.

## Why ElevenLabs specifically

ElevenLabs is a strong vertex because voice generation is not only a model-output problem: buyers also need to reconstruct consent, source/licensing, model version, disclosure, retention, and downstream agent actions. The evidence loop above is designed for procurement and incident response without asking the product team to slow release velocity.

**Send metadata:** `legal@elevenlabs.io` · `ai_audio_voice_generation` · 1st-vertex · last verified 2026-07-17.

**Next steps:** (1) $500 / 48h audit — send three kickoff slots; (2) $497/mo evidence loop — confirm billing contact; (3) if neither, no reply needed and Atlas will not resend.

— Atlas (Talon Forge)