# Cold Email Template 379 — Helicone (ai_observability, Tier-1 VERTEX)

**To:** contact@helicone.ai (verified live 2026-07-16 via https://www.helicone.ai/privacy)
**From:** Atlas (Talon Forge LLC)
**Subject:** 60+ column join-table for Helicone Observability audit-targets

---

Hi Helicone team,

Five quick questions — answer in one line each and I'll send the full audit-package back:

1. **Per-LLM-call-id lineage** — does your observability layer carry the request → response → cost → cache → eval → feedback chain as a single joinable record, or do customers have to correlate across Helicone Observability + Evals + Prompts + Cache + Gateway separately?

2. **Per-prompt-template-version-id provenance** — when a customer A/B tests v3 vs v7 of a prompt template and one drifts, can you reconstruct which LLM calls (per-LLM-call-id) ran against which exact prompt-version-commit-id at the time of the call?

3. **Per-cache-hit-miss-flag + per-cache-similarity-threshold-id join** — when a cache hit saves cost on a RAG retrieval, do you preserve the embedding-id + similarity-threshold-id + cache-key-id so audits can prove the hit was semantically-equivalent and not a false-cache that bypassed safety?

4. **Per-eval-result-id + per-eval-runner-id attribution** — when an LLM-as-judge grader scores an eval-test-case-id, do you preserve the grader-llm-id + eval-run-id + scoring-method-id so customers can defend eval claims against vendor-DD auditors?

5. **Per-LLM-call-prompt-injection-detection-signal-id + per-RAG-corpus-document-chunk-id poisoning defense** — when you flag a request as OWASP-LLM01-prompt-injection, do you preserve the chunk-id + tool-call-id + assistant-id chain for forensic reconstruction?

If any of those are on your roadmap but not shipped, I have a 60+ column join-table spec that closes the gap — happy to send the full schema if useful.

— Atlas
Talon Forge LLC
helicone-audit-targets@atlas-store.local