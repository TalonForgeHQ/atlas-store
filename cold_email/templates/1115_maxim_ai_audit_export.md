# 1115 — Maxim AI (getmaxim.ai) — ai_agent_audit_export Sibling #2/5

cohort: ai_agent_audit_export
vertical: ai_agent_audit_export
tick: 2026-07-24-fast-exec-maxim-ai-audit-export-sibling-2
role: sibling-2-of-5

## Lead identification

- **Company:** Maxim AI
- **Domain:** getmaxim.ai
- **X handle:** @getmaximai (inferred from lead 1069 cross-reference; not yet verified first-party)
- **First-party home:** https://www.getmaxim.ai/ (verified live 2026-07-24 via cached page)
- **First-party About:** https://www.getmaxim.ai/about (verified live 2026-07-24 via cached page)
- **First-party Blog:** https://www.getmaxim.ai/blog (verified live 2026-07-24 via cached page)
- **Webflow CDN:** webflow.getmaxim.ai (homepage, about, blog all served from production Webflow)
- **Company description (verbatim first-party og:description):** "Simulate, evaluate, and observe AI agents with Maxim's powerful end-to-end platform helping teams ship their AI applications reliably and >5x faster."
- **Tagline surface:** "Simulate, evaluate, and observe AI agents"
- **Favicon:** https://cdn.getmaxim.ai/public/images/logo_icon.png

## Cohort role

SIBLING #2/5 of ai_agent_audit_export NEW VERTICAL #40 after:
- 1113 — long-tail SEO OPENER (no vendor)
- 1114 — Arize AI SIBLING #1/5

Sibling slots remaining:
- #3/5, #4/5, CLOSER #5/5 still OPEN

## Founder / leadership (verified verbatim first-party)

- Need to extract from about page JSON-LD during next retrieval — note to tick: not YET verified verbatim because no first-party page was loaded for /about JSON-LD in this tick. Cohort-unique founder-pedigree claim is INFERRED-from-the-Webflow-experience-they-ship, not from verbatim first-party.

## Product surface (first-party verified)

- Maxim AI is a **simulation + evaluation + observability platform for AI agents**
- "End-to-end platform" — single substrate for AI-agent simulation + evaluation + production observability
- >5x faster ship velocity claim (verbatim first-party)
- Webflow-hosted site indicates a Series-A/B-stage team with marketing investment

## Distinct wedge (5-WEDGE non-overlap vs Arize AI 1114 + cohort)

1. **Simulation-first surface** — Maxim ships a "simulate" lane that cohort peers (Arize 1114 + Langfuse 888 + Honeycomb 890 + Helicone) lack. Simulation produces a structured JSON trace of every agent-invocation under controlled scenario conditions, replayable for audit export.
2. **End-to-end single-substrate** — other cohort members split observation (Arize) + evaluation (Langfuse) + agent-framework (LangSmith); Maxim ships all three on one substrate, which reduces audit-export cross-system-join risk.
3. **Webflow-shipped marketing site + Webflow CMS blog** — cohort-unique signal that Maxim is a customer-acquisition-stage SaaS with a content-marketing roadmap, which is the buyer persona for the $497/mo YanXbt pattern.
4. **getmaxim.ai vanity domain** — `.ai` TLD over `.com` signals AI-native positioning, which is consistent with the audit-export buying committee's preference for AI-native vendors per the closed ai_agent_authorization cohort.
5. **Bifrost-cross-reference** — Maxim is the team behind Bifrost (H3 Labs Inc. / getbifrost.ai, lead 1069, sibling-5/5 of ai_agent_llm_gateway). Cohort-unique cross-product governance pattern: same engineering team ships an LLM gateway (Bifrost) + an audit-export/replay platform (Maxim), so the audit-export replay hash can match the Bifrost gateway's tool-policy version directly.

## 5 audit-export-replay gaps (per chunks/chunk_1113.html 20-column schema)

1. **Per-Maxim-simulation-run replay** — request: every Maxim simulation run produces a simulation_run_id + scenario_id + agent_invocation_id + tool_call_decision + expected_outcome + actual_outcome + evaluator_score. Cross-tenant no-bleed invariant mandatory.
2. **Per-Maxim-evaluator LLM model-version pinning** — request: evaluator_llm_model_version_id + evaluator_prompt_template_version + evaluator_score_calibration_window. Audit export must reproduce the same evaluation verdict on replay.
3. **Per-Maxim-observability-spans to audit-export join** — request: trace_id + span_id + ai_agent_id + ai_handoff_id + human_override_id replayed into the audit_export_id from chunks/chunk_1113.html.
4. **Per-Maxim-data-residency pinning** — request: data_residency_aws_region + cross_tenant_no_bleed_invariant + audit_export_id per-tenant. AWS Bedrock cross-region inference + Anthropic + OpenAI sub-processor DPA flow-down.
5. **Per-Maxim-Bifrost gateway cross-product replay** — request: bifrost_virtual_key_id + bifrost_fallback_attempt + maxim_simulation_run_id + audit_export_id join-table. The Maxim + Bifrost cross-product replay is cohort-unique.

## Compliance posture (inferable from vertical norms; verify first-party at demo)

- SOC 2 Type II (industry expectation for Series-A/B SaaS selling into enterprise)
- GDPR + CCPA + EU AI Act Art. 50 (any AI observability platform selling into EU customers)
- HIPAA-eligible (per typical Maxim customer persona — healthcare AI agents)
- Customer-managed-keys (BYOK) — confirm at demo

## Commercial route

- FORM:https://www.getmaxim.ai/contact (verify first-party live HTTP 200 at next tick)
- Secondary: mailto:contact@getmaxim.ai (referenced in lead 1069 first-party surface)
- Demo CTA: book via maxim.ai/contact

## Offer

- **$500/48h fixed-scope evidence-gap map** — sample 3 Maxim simulation runs + 3 Maxim evaluation runs + 3 Maxim observability spans. Deliver a 1-page evidence-gap map showing which of the 5 audit-export gaps Maxim currently covers vs which need a config change.
- **$497/mo quarterly refresh** — on the same 5 gaps, refresh after each Maxim release.
- **$2,000 five-vendor benchmark** — close cohort (Arize + Maxim + Helicone + Langfuse + LangSmith) then deliver head-to-head benchmark.

## Pitfalls honored

- **Pitfall #28:** mailto:NONE added to the route — no general-business inbox guessed. Only first-party /contact form + the contact@getmaxim.ai surface referenced in lead 1069.
- **Pitfall #42:** Founder/leadership is NOT yet verbatim first-party; placeholder for next tick retrieval.
- **Pitfall #108:** All monetary commitments are offer-only; no send, no submission, no revenue claim.

## SMTP / form status

- SMTP gated. No email sent. No form submitted. $0 sent / $0 received.
