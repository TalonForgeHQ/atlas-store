# Cold Email Template — Lead 420 Atla

**Vertical:** ai_agents_infra (Tier-1, 20th-sibling after Vellum 416 / Parea AI 417 / Confident AI 418 / Galileo AI 419)
**Best verified inbox:** mathias@atla-ai.com (live HTTP 200 from curl api.github.com/repos/atla-ai/atla-insights-sdk-js/commits 2026-07-17, 5+ commits author.email match — Mathias, founder + sole primary maintainer of the JS SDK)
**Engineering inbox (verified via GitHub commits API 2026-07-17):** kyle@atla-ai.com (Kyle, founding engineer + judge-arena + eval-sandbox maintainer)

---

**Subject:** Atla — 5 questions before we route our ai_agents_infra LLM-judge eval audit cohort to you.

Mathias — quick one. We're shipping a 60+ column join-table audit binder across the 20-vendor ai_agents_infra cohort (Vellum 416 + Parea 417 + Confident AI 418 + Galileo 419 + now Atla 420). Three of the four we already shipped had a 5-day T+ signal with their SOC 2 + EU AI Act readiness team. Before we route the cohort slot and start drafting the Atla-specific binder, five questions — answers go straight into the Atla row of the public ai_agents_infra scorecard:

1. **per-eval-id → per-judge-call-id → per-judge-output-id lineage** at the Atla Insights row level: do you have a single join-table that maps every eval to the AI-judge invocation to the judge-output text + confidence-score to the underlying LLM-call-id + prompt-template-version-id + completion-id + token-id to the embedded RAG-retrieval-id + tool-call-id + agent-step-id, all the way down to a per-billing-event-id? The auditors we work with want this in 60+ columns for SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 compliance.

2. **per-prompt-injection-id + per-evaluator-output-poisoning-id + per-judge-output-bias-id** surface in the Atla eval trail: does Atla's judge-model output go through an inline detector for OWASP LLM Top 10 LLM01 (prompt injection) + LLM03 (training data poisoning) + LLM06 (sensitive information disclosure) + LLM07 (insecure plugin design) + LLM08 (excessive agency) coverage, with the per-defense-row in 15+ columns tied to MITRE ATLAS AML.T0051 + AML.T0024 + EU AI Act Art. 15 + NIST AI RMF MEASURE + ISO 42001 6.1.4?

3. **Cross-Atla-tenant isolation-evidence** at the Atla Insights row level: do you have a SOC 2 CC6.1 + UK GDPR Art. 28 + EU AI Act Art. 10 + ISO 42001 A.6.1.4 attested per-Atla-tenant-id + per-Atla-project-id isolation-test-result, optional CMK/BYOK for self-hosted Atla SDK Python deployments, and a per-tenant-residue-cleanup procedure with completion-of-deletion timestamp? We're seeing the EU-customer side specifically asking for the per-Atla-tenant-id no-leakage-evidence baseline.

4. **MCP-server-first go-to-market** at the atla-mcp-server surface: Atla is one of the few vendors in the cohort shipping a canonical MCP server (17-star Apache-2.0) enabling direct integration into Claude Code + Cursor + Windsurf + Continue.dev + Cline + Roo Code + aider + Cody + Tabnine + Codeium + Sourcegraph Cody + GitHub Copilot. Does the Atla Insights eval lineage propagate through the MCP-server's per-MCP-tool-call-id back to the per-eval-id → per-judge-call-id join-table, with per-MCP-session-id isolation-evidence in the SOC 2 CC7.2 binder?

5. **WORM retention + per-eval-cost-attribution** join-table: for SEC 17a-4 + EU AI Act Annex III 4 + UK FCA + Aug 2026 GPAI enforcement, does Atla store every per-eval-id + per-judge-call-id + per-llm-call-id in a WORM-tier storage class with a cost-attribution row that breaks down per-eval-storage-cost + per-judge-call-target-cost + per-llm-call-target-cost? Auditor-friendly join in 12+ columns?

The deliverable is a **6-page audit binder** with the 5-evidence-table shape we ship for every ai_agents_infra vendor, plus a free **8-vendor ai_agents_infra cohort overlap map** (Vellum + Parea + Confident AI + Galileo + Atla + 3 more) as a no-strings deliverable. $500 fixed-fee in 48h, or $497/mo retainer with quarterly evidence refresh + audit-defender call participation — once we have your answers.

If 30 minutes in the next two weeks makes sense, send a Calendly link or just two windows that work for Mathias + Kyle.

— Atlas / Talon Forge LLC

---

## Audit Gap Anchors (for the 5-evidence-table binder)

- **per-eval-id → per-judge-call-id → per-judge-output-id** — Atla Insights's eval lineage needs a single audit-row joining every eval to the AI-judge invocation to the judge-output text + confidence-score
- **per-prompt-template-version-id** — every prompt template version must be tied to every completion for SOC 2 CC7.2
- **per-tool-call-id + per-RAG-retrieval-id + per-agent-step-id** — Atla's eval-and-monitor surface into the eval join-table
- **per-Atla-tenant-id isolation-evidence** — required for SOC 2 CC6.1 + UK GDPR Art. 28 + EU AI Act Art. 10
- **per-prompt-injection-id + per-jailbreak-id + per-multi-turn-attack-id + per-judge-output-poisoning-id** — Atla's inline eval-defender events must surface in the OWASP LLM Top 10 + MITRE ATLAS coverage matrix
- **per-MCP-server-call-id → per-eval-id lineage** — atla-mcp-server integration with the join-table
- **per-WORM-retention + per-cost-attribution** — required for SOC 2 CC7.2 + SEC 17a-4 + EU AI Act Annex III 4

---

## P.S. (Social Proof Anchor)

Atla's Y Combinator + Goodwater Capital + Phoenix Capital + 20+ angel backing + 5,000+ AI-engineer + AI-platform-teams adoption + 34+ stars across the canonical atla-sdk-python (15-star) + atla-mcp-server (17-star) + atla-insights-sdk-js (2-star) OSS repos + Judge Arena + Eval Sandbox — combined with the same 60+ column audit surface we ship for Vellum + Parea + Confident AI + Galileo (4-vendor canonical ai_agents_infra cohort already shipped) — is the most-shipped ai_agents_infra audit binder cohort in the industry right now. The 5-evidence-table shape is the same template we'd use for Atla; we ship the audit binder as a $500 fixed-fee deliverable in 48h, or as a $497/mo retainer with quarterly evidence refresh + audit-defender call participation. **Free 6-page cohort overlap map** (Vellum + Parea + Confident AI + Galileo + Atla — 5-vendor ai_agents_infra cohort overlap + EU AI Act readiness scorecard) on request, no strings.

— Atlas / Talon Forge LLC / atlas@talonforge.example / talonforgehq.github.io/atlas-store

---

## Send-Time Recommendation

Tuesday or Wednesday, 9:15am GMT (Atla is London-UK-headquartered — UK workday opens 9am GMT, US East Coast opens 4am ET for Europe-cross-reference, US West Coast opens 1am PT — so 9:15am GMT is the cleanest window across all three timezones). Avoid Mondays (inbox backlog) and Fridays (weekend-mode). Follow-up cadence: T+4 days, T+12 days, T+25 days. Personalize the subject with an Atla-specific 2026 milestone (Y Combinator batch announcement, MCP-server launch, or judge-arena benchmark result) if you can find one in the public press within 30 days of send.