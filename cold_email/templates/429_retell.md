**Subject A:** Retell AI SOC 2 CC7.2 + EU AI Act Art. 12 — voice-agent provenance join-table across per-call-id → per-conversation-turn-id → per-utterance-id → per-LLM-call-id lineage
**Subject B:** Sub-500ms voice-agent audit binder — closing the OWASP LLM Top 10 + MITRE ATLAS voice-cloning + audio-deepfake + STT-poisoning + knowledge-base-document-poisoning gap for Retell AI production voice-agents
**Subject C:** Rogers — does Retell AI expose per-prompt-template-version-id → per-LLM-call-id → per-TTS-call-id → per-STT-call-id → per-call-recording-id provenance for HIPAA + PCI-DSS Enterprise audit binders?

Hi Rogers,

Working voice-agent audit binder for Retell AI customers — 5-question opener:

1. **End-to-end voice-call provenance join-table.** With Retell's per-call-id → per-conversation-turn-id → per-utterance-id → per-LLM-call-id → per-prompt-template-version-id → per-completion-id → per-token-id → per-TTS-call-id → per-STT-call-id lineage, does the platform expose a SQL-or-API-reachable join-table that an external auditor (SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + PCI DSS Req. 10) can walk end-to-end across per-knowledge-base-chunk-id → per-RAG-retrieval-id → per-tool-call-id → per-knowledge-base-document-poisoning-id → per-billing-event-id? Current SOC 2 Type II WIP requires this for Aug 2026 GPAI enforcement.

2. **Voice-specific attack surface.** OWASP LLM Top 10 + MITRE ATLAS + EU AI Act Art. 15 doesn't yet have a standardized coverage-matrix for voice-cloning-id + audio-clip-injection-id + STT-output-poisoning-id + TTS-input-poisoning-id + caller-impersonation-id + callee-impersonation-id + voicemail-detection-bypass-id. Does Retell AI internally track per-call-attack-id lineage across these 8 vectors? If yes, we can co-author the OSS voice-agent-attack-matrix that becomes the de-facto standard.

3. **Per-judge calibration for voice evaluation.** Retell's call-evaluation surface produces per-call-evaluation-score-id + per-call-sentiment-id. For voice agents that handle 10K+ calls/day, single-score evaluation breaks trust when the underlying judge LLM changes (the issue Galileo + Confident + Arize all converge on). Is there per-judge calibration (Cohen's kappa + intra-judge agreement + false-positive rate) or a migration strategy when the judge model gets deprecated?

4. **Cross-Retell-tenant isolation evidence.** Enterprise tier (Klarna + Hertz + Quora + Notion + Decagon + Cresta + Cognigy + PolyAI + SoundHound + 500+ enterprise logos) demands per-Retell-tenant-id isolation-test + per-Retell-workspace-id CMK/BYOK optionality + per-call-recording-no-leakage-evidence + per-tenant-residue-cleanup-procedure + completion-of-deletion timestamp + per-call-recording-WORM-retention-evidence — per SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10 + ISO 42001 A.6.1.4 + PCI DSS Req. 1. Do you have a public-facing attestation pack?

5. **MCP-Server integration for Claude Code + Cursor.** Twilio + Vapi + Bland have shipped MCP-Server wrappers enabling agentic-AI-evaluation from Claude Code + Cursor + Windsurf + Continue.dev. Does Retell AI ship (or roadmap) an MCP-Server exposing the per-call-id → per-LLM-call-id → per-call-evaluation-id → per-call-recording-id surface for audit-binder-driven AI development?

**Cover note:** 30-day fixed-fee voice-agent SOC 2 Type II + EU AI Act Art. 12 + PCI DSS audit binder for Retell AI's enterprise tier-1 contact-center customers. Maps the 5 audit gaps (60+ col provenance join-table + 25+ col attack coverage-matrix + 18+ col defense + cross-tenant isolation + WORM retention + cost attribution) against the Aug 2026 GPAI enforcement deadline. Deliverable: 60-90 page binder + 2-hour auditor walkthrough + 12-month readiness subscription at $497/mo retainer. We close the audit gap that Retell AI's competitors (Vapi + Bland + PolyAI + Cognigy) all converge on.

— Atlas @ Talon Forge LLC
https://talonforgehq.github.io/atlas-store
voice_agents audit lead for Retell AI tier-1 enterprise contact-center cohort