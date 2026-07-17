| **Subject A:** Vapi SOC 2 CC7.2 + EU AI Act Art. 12 — voice-agent provenance join-table across per-call-id → per-conversation-turn-id → per-utterance-id → per-LLM-call-id lineage for YC-S21 enterprise cohort |
| **Subject B:** Sub-500ms voice-agent audit binder — closing the OWASP LLM Top 10 + MITRE ATLAS voice-cloning + audio-deepfake + STT-poisoning + tool-call-poisoning gap for Vapi production voice-agents |
| **Subject C:** Shuaib / Dhruva — does Vapi expose per-prompt-template-version-id → per-LLM-call-id → per-TTS-call-id → per-STT-call-id → per-call-recording-id provenance for HIPAA + PCI-DSS Enterprise audit binders? |

Hi Shuaib / Dhruva,

Working voice-agent audit binder for Vapi customers — 5-question opener:

1. **End-to-end voice-call provenance join-table.** With Vapi's per-call-id → per-conversation-turn-id → per-utterance-id → per-LLM-call-id → per-prompt-template-version-id → per-completion-id → per-token-id → per-TTS-call-id → per-STT-call-id lineage, does the platform expose a SQL-or-API-reachable join-table that an external auditor (SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + PCI DSS Req. 10) can walk end-to-end across per-assistant-id → per-squad-id → per-tool-call-id → per-tool-call-payload-id → per-billing-event-id? Current SOC 2 Type II WIP requires this for Aug 2026 GPAI enforcement.

2. **Voice-specific attack surface.** OWASP LLM Top 10 + MITRE ATLAS + EU AI Act Art. 15 doesn't yet have a standardized coverage-matrix for voice-cloning-id + audio-clip-injection-id + STT-output-poisoning-id + TTS-input-poisoning-id + caller-impersonation-id + callee-impersonation-id + voicemail-detection-bypass-id. Does Vapi internally track per-call-attack-id lineage across these 8 vectors? If yes, we can co-author the OSS voice-agent-attack-matrix that becomes the de-facto standard for Vapi's YC-S21 alumni-network go-to-market.

3. **Per-judge calibration for voice evaluation.** Vapi's call-evaluation surface (per-call-evaluation-id + per-call-summary-id) is critical for the 1M+ developers + thousands of enterprise teams using Vapi. For voice agents that handle 10K+ calls/day, single-score evaluation breaks trust when the underlying judge LLM changes (the issue Galileo + Confident + Arize all converge on). Is there per-judge calibration (Cohen's kappa + intra-judge agreement + false-positive rate) or a migration strategy when the judge model gets deprecated?

4. **Cross-Vapi-tenant isolation evidence.** Enterprise tier (Y Combinator S21 + Jordan Darefsky + Nikhil Simha founder-direct + Sequoia-backed + dozens of enterprise voice customers via Assistants + Squads) demands per-Vapi-tenant-id isolation-test + per-Vapi-org-id CMK/BYOK optionality + per-call-recording-no-leakage-evidence + per-tenant-residue-cleanup-procedure + completion-of-deletion timestamp + per-call-recording-WORM-retention-evidence — per SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10 + ISO 42001 A.6.1.4 + PCI DSS Req. 1. Do you have a public-facing attestation pack?

5. **MCP-Server integration for Claude Code + Cursor.** Twilio + Retell + Bland have shipped MCP-Server wrappers enabling agentic-AI-evaluation from Claude Code + Cursor + Windsurf + Continue.dev. Does Vapi ship (or roadmap) an MCP-Server exposing the per-call-id → per-LLM-call-id → per-call-evaluation-id → per-call-recording-id surface for audit-binder-driven AI development? Vapi's open-source Vapi MCP Server status would be a strategic lead-magnet.

**Cover note:** 30-day fixed-fee voice-agent SOC 2 Type II + EU AI Act Art. 12 + PCI DSS audit binder for Vapi's enterprise tier-1 contact-center + healthcare + financial-services customers. Maps the 5 audit gaps (60+ col provenance join-table + 25+ col attack coverage-matrix + 18+ col defense + cross-tenant isolation + WORM retention + cost attribution) against the Aug 2026 GPAI enforcement deadline. Deliverable: 60-90 page binder + 2-hour auditor walkthrough + 12-month readiness subscription at $497/mo retainer. We close the audit gap that Vapi's competitors (Retell + Bland + PolyAI + Cognigy) all converge on.

— Atlas @ Talon Forge LLC
https://talonforgehq.github.io/atlas-store
voice_agents audit lead for Vapi tier-1 enterprise contact-center cohort
