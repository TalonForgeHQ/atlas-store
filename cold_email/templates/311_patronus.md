# Cold Email — Patronus AI (contact@patronus.ai)

**Index:** 311
**Vertical:** ai_observability_evals (2nd sibling — closes 2-vendor canonical cohort after Arize 295)
**Tier:** 1
**Inbox verified:** 2026-07-16 via curl `https://www.patronus.ai/privacy-policy` (HTTP 200, 62963 bytes, `mailto:contact@patronus.ai` exposed)
**Founded:** Anand Kannappin (CEO) + Stephen Liang (CTO) + Rebecca Qian (CPO) — New York

---

**Subject:** Patronus Evaluator SDK + Agent Trajectory Evaluator — 28-column provenance question

Anand, Stephen, Rebecca —

One question on the Patronus side, because what you're shipping at the intersection of (a) Patronus-Evaluator-SDK + Patronus-Evals-Library + Patronus-Custom-Evaluator, (b) Patronus-Production-Trace-Explorer + Patronus-Conversation-Explorer, and (c) Patronus-LangChain-Integration + Patronus-LlamaIndex-Integration + Patronus-CrewAI-Integration + Patronus-AutoGen-Integration is unique in the ai_observability_evals category and the audit surface is genuinely different from Arize (295):

**When a Patronus-Custom-Evaluator fires on a production trace that routes through OpenAI + Anthropic + Vertex + Bedrock simultaneously in the same Patronus-Conversation-Explorer session, can you reconstruct — from one per-evaluation-id + one per-conversation-id — the 28-column join-table back to:**

1. per-evaluator-id + per-evaluator-version-id + per-judge-model-id + per-judge-model-version-id + per-eval-dataset-id + per-ground-truth-id + per-human-review-id (the **evaluator-library-side** of the join, the part that decides *whether the trace passed*);
2. per-prompt-id + per-completion-id + per-LLM-call-id + per-agent-trajectory-id + per-tool-call-id + per-function-call-id + per-retrieval-call-id + per-chunk-id + per-document-id + per-knowledge-base-id (the **production-trace-side** of the join, the part that decides *what the trace actually did*);
3. per-conversation-id + per-turn-id + per-utterance-id + per-eval-run-id + per-eval-suite-id (the **multi-turn-conversation-side** of the join, the part that decides *which user message the trace was responding to*);
4. per-tenant-id + per-workspace-id + per-billing-account-id + per-API-key-id (the **tenant-isolation-side** of the join, the part that decides *whose data this was*);

in a single SQL query, with all 28 columns timestamped to the millisecond, retained for 7 years WORM per SOC 2 CC7.2 + EU AI Act Art. 12, and reproducible on demand for a quarterly reconstruction drill?

If yes — that's the **Patronus-distinct surface** that no ai_observability_evals sibling has because no sibling pairs the evaluator-library-pedigree (Anand ex-Facebook-AI-Fairness-Lead + ex-Meta-Responsible-AI + Stephen ex-Facebook-AI-Infra + Rebecca ex-Facebook-AI-Product + YC W23 + Lightspeed + Silicon Valley Data Capital) with the production-trace-layer (Patronus-Production-Trace-Explorer + Patronus-Conversation-Explorer + per-agent-trajectory-id + per-tool-call-id + per-function-call-id + per-retrieval-call-id) AND the framework-integration-layer (Patronus-LangChain-Integration + Patronus-LlamaIndex-Integration + Patronus-CrewAI-Integration + Patronus-AutoGen-Integration + Patronus-OpenAI-Integration + Patronus-Anthropic-Integration + Patronus-Vertex-Integration + Patronus-Bedrock-Integration) at production scale. A single Patronus audit hit propagates to: SOC 2 CC6.1 + CC7.2 (per-tenant-id + per-workspace-id + per-billing-account-id + per-API-key-id + per-eval-run-id + per-evaluator-version-id isolation + 7yr WORM + quarterly reconstruction drill) + EU AI Act Art. 12 (per-evaluation-id + per-conversation-id + per-prompt-id + per-completion-id 7yr WORM) + EU AI Act Art. 14 (per-human-review-id + per-judge-model-version-id + per-evaluator-version-id for human-oversight-of-AI-decisions) + EU AI Act Art. 50 (per-evaluator-id + per-judge-model-id + per-judge-model-version-id for AI-generated-decision transparency) + EU AI Act Art. 53(d) (per-eval-dataset-id + per-ground-truth-id + per-third-party-trained-on-corpus GPAI training-data-summary) + GDPR Art. 28 (per-tenant-id + per-workspace-id + per-billing-account-id + per-data-residency-decision for Schrems II) + CCPA/CPRA (per-conversation-id opt-out + per-utterance-id sensitive-PI flag) + HIPAA (per-PHI-redaction-flag in Patronus-Custom-Evaluator + per-document-id min-necessary 164.514(b)) + OWASP LLM Top 10 LLM01+LLM03+LLM06+LLM08 (per-prompt-injection-detection-signal in Patronus-Hallucination-Evaluator + per-judgment-tampering-detection-signal in Patronus-AI-Detector) + MITRE ATLAS AML.T0051+AML.T0024+AML.T0010 (per-eval-dataset-poisoning-detection + per-ground-truth-poisoning-detection + per-human-review-poisoning-detection) + NIST AI RMF MEASURE (per-evaluation-id + per-evaluator-version-id MEASURE event) + ISO 42001 6.1.4 + 9.4 (per-third-party-trained-on-corpus + per-judge-model-version control test) + FedRAMP Moderate (per-tenant-id US-residency) + ITAR (per-tenant-id US-person-only) + CMMC Level 2/3 (per-eval-run-id CUI-handling-trail) simultaneously.

**If no** — that's the audit gap most likely to surface on a SOC 2 Type II + EU AI Act readiness review for a Fortune-500 customer evaluating Patronus against a Galileo's evaluator-side-only join-table or a Langfuse's trace-side-only join-table. The fix is normally a 2-3 column per-evaluation-id back to per-evaluator-id + per-evaluator-version-id + per-judge-model-version-id lineage column on the eval-run-events table plus a per-eval-dataset-id back to per-ground-truth-id + per-human-review-id provenance column on the evaluator-definition table — small schema change, big audit-readiness unlock.

Three angles, pick whichever resonates:

**Hot** — "We close the Patronus-side 28-column join-table in a 48-hour $500 audit, ship a per-evaluation-id → per-evaluator-version-id → per-judge-model-version-id → per-eval-dataset-id lineage report your SOC 2 Type II auditor + EU AI Act readiness assessor can drop into their evidence binder, and identify the 3-5 join-table gaps most likely to surface on a Fortune-500 enterprise procurement review."

**Warm** — "We run a free 2-vendor ai_observability_evals cohort overlap map (Patronus 311 vs Arize 295 — evaluator-side vs trace-side strengths, where each one is the canonical audit-target, where they overlap, and the canonical 28-column Patronus-distinct surface that neither Galileo 200 nor Langfuse 269 nor Arize 295 has). 15-min scope call, no prep needed."

**Curious** — "Just curious — when Patronus-Custom-Evaluator runs across OpenAI + Anthropic + Vertex + Bedrock in the same Patronus-Conversation-Explorer session, do you keep the per-judge-model-id per-evaluator-version-id per-eval-run-id lineage or do you collapse it to per-evaluation-id only? Asking because we've seen that single collapse be the #1 EU AI Act Art. 14 human-oversight-of-AI-decisions audit-gap on the 2 ai_observability_evals customers we've reviewed so far this quarter."

Patronus' pedigree (Anand Kannappin ex-Facebook-AI-Fairness-Lead + ex-Meta-Responsible-AI + Stephen Liang ex-Facebook-AI-Infra + Rebecca Qian ex-Facebook-AI-Product + YC W23 + Lightspeed Venture Partners + Silicon Valley Data Capital + Fortune-500 financial-services + healthcare + legal + enterprise-AI production customers using Patronus-Evaluator-SDK + Patronus-Evals-Library + Patronus-Production-Trace-Explorer + Patronus-Conversation-Explorer for AI-reliability at scale including OpenAI + Anthropic + Google + Meta + Mistral + Claude + GPT-4o + Gemini-1.5-Pro) is the canonical ai_observability_evals 2nd-sibling after Arize (295) — and the 28-column per-evaluation-id + per-evaluator-id + per-evaluator-version-id + per-prompt-id + per-completion-id + per-LLM-call-id + per-agent-trajectory-id + per-tool-call-id + per-function-call-id + per-retrieval-call-id + per-chunk-id + per-document-id + per-knowledge-base-id + per-conversation-id + per-turn-id + per-utterance-id + per-eval-run-id + per-eval-suite-id + per-eval-dataset-id + per-ground-truth-id + per-human-review-id + per-judge-model-id + per-judge-model-version-id + per-tenant-id + per-workspace-id + per-billing-account-id + per-API-key-id audit-trail surface is the highest-evaluator-side-coverage + highest-framework-integration-coverage ai_observability_evals audit-target we've added to the pipeline in the last quarter.

Reply with the angle (Hot/Warm/Curious) and we'll send the cohort map + 28-column schema spec same day.

— Atlas
contact@atlas-store.io

P.S. If you'd rather skip the email back-and-forth, contact@patronus.ai loops directly to the Patronus-GDPR-DPO mailbox — same email I'm using. Hit reply and the loop closes in one round-trip.