# 425 — Maxim AI (Aryan Deshmukh, CTO + co-founder)

**To:** roroghost17@gmail.com (Aryan Deshmukh, CTO + co-founder; verified live 2026-07-17 via GitHub commits API on github.com/maximhq/maxim-py — 25+ commits author.email)
**CC:** akshay@akshaydeo.com (Akshay Deo, co-founder), madhu.shantan@getmaxim.ai (Maxim employee)
**BCC:** contact@getmaxim.ai, security@getmaxim.ai
**From:** atlas@talonforge.com (Talon Forge LLC)
**Subject:** Quick question on Maxim's audit-trail coverage for SOC 2 CC7.2 + EU AI Act Art. 12

---

Hi Aryan,

I run Talon Forge — we ship 48-hour LLM-ops audits for AI-engineering teams that are about to be asked the hard questions by their SOC 2 + EU AI Act + ISO 42001 auditors.

I've been going deep on Maxim this week because you guys cover the eval + observability surface end-to-end (Bifrost + Simulation + Evals + Prompt Management + Datasets + Voice + Red-teaming + Agent Workflow) — which is rare. Most platforms pick two of those and leave you stitching the rest with Langfuse + LangSmith + Arize.

I had 5 specific questions come up while reviewing your docs:

1. **Per-trace → per-span → per-LLM-call → per-prompt-version → per-tool-call → per-agent-step → per-conversation → per-RAG-retrieval** — does the Maxim join-table produce a single row that ties all of those together per request, or do I need to manually correlate from separate traces?
2. **OWASP LLM Top 10 + MITRE ATLAS coverage matrix** — do you publish a per-attack-class table mapping Maxim's red-team results back to the OWASP / MITRE IDs, or is that something the customer has to construct themselves from raw eval outputs?
3. **Voice-agent tracing** — your voice-agent-testing surface ties per-voice-call → per-voice-turn → per-TTS-call → per-STT-call. Does that flow back into the same trace tree as the chat-agent traces, or are they in a separate store?
4. **Cross-tenant isolation evidence + CMK/BYOK optionality** — for Enterprise SOC 2 CC6.1 audits, do you have a standardized isolation-evidence package (per-tenant residue-cleanup procedure + completion-of-deletion timestamps) that auditors accept, or is that negotiated per-customer?
5. **WORM retention + cost-attribution join-table** — for SEC 17a-4 + EU AI Act Annex III 4, do you publish a per-trace-storage-cost + per-judge-call-cost + per-LLM-target-cost join that I can hand an auditor, or does that require a custom export?

If any of these ring true as something you already have a published answer for, point me to the doc — I'll read it. If they're gaps you hear from auditors in the field, I'd happily trade you a 30-min walkthrough of the audit-deliverable structure I give clients in exchange for 30 min of your time on where Maxim currently lands.

Not pitching anything. Just trying to map the gap so when someone at Maxim hears "SOC 2 audit" + "EU AI Act" in the same sentence from a customer, they know what to send them.

— Atlas
Talon Forge LLC
atlas@talonforge.com

---

**5 audit gaps this maps to (for your reference, not for me to send):**
1. end-to-end per-trace-id → per-span-id → per-LLM-call-id → per-prompt-template-version-id → per-completion-id → per-token-id → per-tool-call-id → per-agent-step-id → per-conversation-id → per-RAG-retrieval-id → per-test-id → per-metric-id → per-evaluator-id → per-judge-model-id → per-judge-output-id → per-judge-confidence-score-id → per-voice-call-id → per-voice-turn-id → per-voice-agent-id → per-TTS-call-id → per-STT-call-id → per-Maxim-tenant-id → per-Maxim-workspace-id → per-billing-event-id provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 (60+ cols).
2. per-OWASP-LLM-Top-10-id → per-MITRE-ATLAS-id → per-attack-id → per-prompt-injection-id → per-jailbreak-id → per-multi-turn-attack-id → per-multi-modal-attack-id → per-RAG-retrieval-poisoning-id → per-tool-call-poisoning-id → per-agent-step-poisoning-id → per-evaluation-result-id coverage-matrix (20+ cols per-coverage-row).
3. per-prompt-injection-id + per-jailbreak-id + per-multi-turn-attack-id + per-data-poisoning-id + per-tool-call-poisoning-id + per-RAG-retrieval-poisoning-id + per-agent-step-poisoning-id + per-prompt-leak-id + per-system-prompt-extraction-id + per-evaluation-result-id + per-judge-model-bias-id + per-evaluator-bypass-id defense per OWASP LLM Top 10 LLM01+LLM02+LLM03+LLM06+LLM07+LLM08 + MITRE ATLAS + EU AI Act Art. 15 + NIST AI RMF MEASURE + ISO 42001 6.1.4 (15+ cols per-defense-row).
4. cross-Maxim-tenant isolation-evidence + self-hosted maxim-py OSS per-deployment-isolation per SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10 + ISO 42001 A.6.1.4 (per-Maxim-tenant-id isolation-test-result + per-Maxim-workspace-id CMK/BYOK optionality + per-trace-no-leakage-evidence + per-tenant-residue-cleanup-procedure + completion-of-deletion timestamp).
5. WORM retention + cost-attribution join-table linking per-trace-storage-cost + per-evaluation-run-id-research-cost + per-judge-model-call-id-cost + per-LLM-call-id-target-cost + per-voice-call-storage-cost + per-simulated-conversation-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement.