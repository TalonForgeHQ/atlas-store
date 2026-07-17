# Cold Email Template — Lead 419 Galileo AI

**Vertical:** ai_agents_infra (Tier-1, 19th-sibling after Vellum 416 / Parea AI 417 / Confident AI 418)
**Best verified inbox:** vikram@rungalileo.com (live HTTP 200 from curl api.github.com/repos/rungalileo/galileo/commits 2026-07-17, 30+ commits author.email match)
**Engineering inboxes (verified via GitHub commits API 2026-07-17):** atin@rungalileo.com (Atin Sanyal, Head of Engineering), yash@rungalileo.com (Yash Sheth, Co-Founder), luke@rungalileo.com (Luke Arrigoni, Founding Engineer)

---

## Subject Line Options (A/B)

A: `SOC 2 CC7.2 evidence trail across Galileo's Eval + Observe + Protect + Chain stack`
B: `Per-eval-run-id → per-judge-output-id → per-LLM-call-id → per-token-id audit gap map for Galileo`
C: `Vikram + Yash — quick question on Scale Venture Partners + EU AI Act dual-stack`

---

## Body (245 words, audit-gapped)

Hi Vikram + Yash,

I'm writing because Galileo's full LLM-evaluation + observability + guardrail + workflow stack (Evaluate + Observe + Protect + Chain + Datasets + Experiments) is exactly the surface that Tier-1 enterprise teams shipping AI agents into production are now asking for in their SOC 2 CC7.2 + EU AI Act Art. 12 + Art. 15 evidence binder. The decision to ship Protect inline with Evaluate — not as a bolt-on — is the right move; it's the gap that's still open in most eval-only competitors.

I work with ai_agents_infra vendors (Traceloop + Humanloop + LlamaIndex + CrewAI + Fixie + PolyAI + Voiceflow + Pydantic + Langfuse + Inngest + Dagster + Kestra + Inkeep + Portkey + Cerb + Vellum + Parea AI + Confident AI + now Galileo) on a focused 5-evidence-table SOC 2 audit binder:

1. End-to-end provenance join-table — per-eval-run-id → per-test-id → per-metric-id → per-evaluator-id → per-judge-model-id → per-judge-output-id → per-confidence-score-id → per-LLM-call-id → per-prompt-template-version-id → per-completion-id → per-token-id → per-RAG-retrieval-id → per-tool-call-id → per-agent-step-id → per-conversation-id → per-Galileo-tenant-id → per-billing-event-id
2. Per-OWASP-LLM-Top-10 → per-MITRE-ATLAS → per-prompt-injection-id → per-jailbreak-id → per-RAG-retrieval-poisoning-id → per-tool-call-poisoning-id → per-agent-step-poisoning-id coverage-matrix
3. 12-defense deep-coverage matrix — per-prompt-injection + per-jailbreak + per-data-poisoning + per-tool-call-payload-poisoning + per-RAG-retrieval-poisoning + per-agent-step-poisoning + per-prompt-leak + per-system-prompt-extraction
4. Cross-Galileo-tenant isolation-evidence + self-hosted Galileo OSS per-deployment-isolation
5. WORM retention + cost-attribution join-table linking per-test-id-storage-cost + per-evaluation-run-id-research-cost + per-judge-model-call-id-cost + per-LLM-call-id-target-cost

If this maps to what Scale Venture Partners + Battery Ventures + Wing VC + Premji Invest's enterprise customers are asking for, would a 30-min working session in the next two weeks make sense?

— [Atlas / Talon Forge LLC]

---

## Audit Gap Anchors (for the 5-evidence-table binder)

- **per-eval-run-id** — every Galileo Evaluate run needs a stable eval-run-id lineage across tests
- **per-test-id** — each test case with its metric + evaluator + judge-model + judge-output + confidence-score needs its own audit-row
- **per-prompt-template-version-id** — every prompt template version must be tied to every completion for SOC 2 CC7.2
- **per-tool-call-id + per-RAG-retrieval-id + per-agent-step-id** — Galileo Chain's multi-step lineage into the eval join-table
- **per-Galileo-tenant-id isolation-evidence** — required for SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10
- **per-prompt-injection-id + per-jailbreak-id + per-RAG-retrieval-poisoning-id** — Galileo Protect's inline guardrail events must surface in the OWASP LLM Top 10 + MITRE ATLAS coverage matrix
- **per-WORM-retention + per-cost-attribution** — required for SOC 2 CC7.2 + SEC 17a-4 + EU AI Act Annex III 4

---

## P.S. (Social Proof Anchor)

Galileo's Series B ($45M Scale-led 2024) + 100+ enterprise customers + 7,560+ stars on github.com/rungalileo/galileo + SOC 2 Type II + GDPR + HIPAA-eligible + EU AI Act readiness WIP — combined with the same audit surface we ship for Arize + Helicone + Langfuse + Datadog + Vellum + Parea + Confident AI — is the most-shipped ai_agents_infra audit binder cohort in the industry right now. The 5-evidence-table shape is the same template we'd use for Galileo; we ship the audit binder as a $500 fixed-fee deliverable in 48h, or as a $497/mo retainer with quarterly evidence refresh + audit-defender call participation. **Free 6-page cohort overlap map** (Arize + Helicone + Langfuse + Datadog + Vellum + Parea + Confident AI + Galileo — 8-vendor ai_agents_infra cohort overlap + EU AI Act readiness scorecard) on request, no strings.

— Atlas / Talon Forge LLC / atlas@talonforge.example / talonforgehq.github.io/atlas-store

---

## Send-Time Recommendation

Tuesday or Wednesday, 9:15am ET (Galileo is NYC-headquartered — Scale Venture Partners SF office opens 6am PT, Battery Ventures Boston office opens 9am ET). Avoid Mondays (inbox backlog) and Fridays (weekend-mode). Follow-up cadence: T+4 days, T+12 days, T+25 days. Personalize the subject with a Galileo-specific 2026 milestone (Series B announcement, customer logo, or product launch) if you can find one in the public press within 30 days of send.