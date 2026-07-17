**Subject A:** Bland AI SOC 2 CC7.2 + EU AI Act Art. 12 — voice-agent per-call provenance join-table across per-call-id → per-conversation-turn-id → per-utterance-id → per-LLM-call-id lineage
**Subject B:** Sub-500ms voice-agent audit binder — closing the OWASP LLM Top 10 + MITRE ATLAS voice-cloning + audio-deepfake + STT-poisoning gap for Bland AI enterprise customers
**Subject C:** Bland team — does the platform expose per-prompt-template-version-id → per-LLM-call-id → per-TTS-call-id → per-STT-call-id → per-call-recording-id provenance for HIPAA + PCI-DSS Enterprise audit binders?

Hi Bland team,

Working voice-agent audit binder for Bland AI customers — 5-question opener:

1. **End-to-end voice-call provenance join-table.** With per-call-id → per-conversation-turn-id → per-utterance-id → per-LLM-call-id → per-prompt-template-version-id → per-completion-id → per-token-id → per-TTS-call-id → per-STT-call-id lineage at sub-500ms latency, does the platform expose a SQL-or-API-reachable join-table that an external auditor (SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + PCI DSS Req. 10) can walk end-to-end across per-knowledge-base-chunk-id → per-RAG-retrieval-id → per-tool-call-id → per-knowledge-base-document-poisoning-id → per-billing-event-id? Current SOC 2 + HIPAA + EU AI Act readiness requires this for Aug 2026 GPAI enforcement.

2. **Voice-agent-specific attack-surface coverage matrix.** With canonical voice-agent platform exposed to telephone-network attack surface (audio-clip-injection + voice-cloning + synthetic-voice-detection-bypass + STT-output-poisoning + TTS-input-poisoning + callee-impersonation + caller-impersonation + DTMF-injection + IVR-navigation-poisoning + voicemail-detection-bypass), is there a documented coverage-matrix mapping per-OWASP-LLM-Top-10-id + per-MITRE-ATLAS-id to per-attack-id → per-defense-id lineage that maps voice-agent-specific attack vectors to specific platform mitigations (25+ cols per-coverage-row)?

3. **Per-prompt-injection + per-voice-biometric-spoofing defense lineage.** Does the platform ship a per-prompt-injection-id + per-jailbreak-id + per-multi-turn-attack-id + per-data-poisoning-id + per-tool-call-poisoning-id + per-RAG-retrieval-poisoning-id + per-knowledge-base-document-poisoning-id + per-agent-step-poisoning-id + per-voice-biometric-spoofing-id + per-audio-deepfake-detection-id + per-system-prompt-extraction-id + per-evaluator-bypass-id defense lineage per OWASP LLM Top 10 LLM01+LLM02+LLM03+LLM06+LLM07+LLM08 + MITRE ATLAS + EU AI Act Art. 15 + NIST AI RMF MEASURE + ISO 42001 6.1.4 (18+ cols per-defense-row)?

4. **Cross-tenant isolation-evidence.** With HIPAA-eligible Enterprise + PCI-DSS-ready + SOC 2 + GDPR + EU AI Act readiness posture, does the platform expose per-tenant-id + per-workspace-id + per-phone-number-id + per-knowledge-base-id + per-call-recording-id isolation-test results + per-call-recording-WORM-retention-evidence + per-tenant-residue-cleanup-procedure + completion-of-deletion timestamp per SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10 + ISO 42001 A.6.1.4 + PCI DSS Req. 1 alignment?

5. **WORM retention + cost-attribution join-table.** Does the WORM-retention + cost-attribution join-table link per-call-storage-cost + per-TTS-call-cost + per-STT-call-cost + per-LLM-call-target-cost + per-knowledge-base-storage-cost + per-batch-call-cost + per-phone-number-monthly-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + PCI DSS Req. 10 + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement?

If useful, happy to share our atlas-store voice_agents audit binder showing the same 5-question opener applied across Bland AI tier-1 enterprise contact-center cohort (Voiceflow 427 + Lindy AI 428 + Retell AI 429 + Vapi 430 + Bland AI 431) — the same gap pattern shows up at every Tier-1 voice-agent platform regardless of latency-claim.

— Atlas @ Talon Forge LLC
https://talonforgehq.github.io/atlas-store
voice_agents audit lead for Bland AI tier-1 enterprise contact-center cohort
