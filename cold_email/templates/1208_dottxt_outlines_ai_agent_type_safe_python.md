# .txt / Outlines — AI-agent structured-output evidence gap map

## Subject options
1. **.txt × Outlines: can every constrained decode be replayed?**
2. **A 22-column receipt for JSON Schema, CFG and function-call outputs**
3. **From token mask to agent action: an audit-ready .txt map**

## 3-line first touch
Hi Rémi — .txt's first-party site makes a crisp promise: **“Your schema is a contract. We enforce it.”** It also names Outlines (65M+ downloads), `api.dottxt.ai`, vLLM/SGLang/TensorRT-LLM drop-ins, `dotjson`, `dotgrammar`, and `dotlambda`.

I mapped the evidence gap between that constrained-generation layer and the downstream agent action: can one tenant replay the schema revision, grammar, tokenizer, token mask, function-call contract, latency and final validation result without crossing tenant boundaries?

I can deliver the fixed-scope map in 48h for **$500**, then keep it current for **$497/mo**; the five-vendor Pydantic + Instructor + LMQL + .txt/Outlines + Guidance benchmark is **$2,000**.

## Five audit-replay questions
1. Which `schema_revision_id` and `tokenizer_revision` governed each constrained decode?
2. Can the same `token_mask_hash` be reproduced for the exact model and inference server revision?
3. How are `dotjson`, `dotgrammar`, and `dotlambda` revisions tied to the final agent tool call?
4. What proves that a valid structured output remained semantically safe after it reached the downstream tool?
5. Can an auditor export one tenant's full replay without any cross-tenant data bleed?

## 22-column evidence receipt
`tenant_id + dottxt_workspace_id + outlines_program_id + schema_revision_id + regex_constraint_id + grammar_revision_id + dotjson_revision_id + dotgrammar_revision_id + dotlambda_revision_id + inference_server + model_id + tokenizer_revision + token_mask_hash + constrained_decode_id + function_call_schema_id + validation_result_id + latency_ms + cost_usd + audit_export_id + retention_policy_version + cross_tenant_no_bleed_invariant + replay_hash`

## Why this is not the same audit as the other cohort members
- **Pydantic:** post-call Python schema validation and agent runtime.
- **Instructor:** patched client response plus retry on `ValidationError`.
- **LMQL:** declarative DSL plus parser-guided decoding and compile target.
- **.txt / Outlines:** hosted constrained-decoding API, inference-server drop-ins, JSON Schema + CFG + function-call libraries.
- **Guidance (queued closer):** token-level interleaving of generation and control flow.

## Offer ladder
- **$500 / 48h:** fixed-scope evidence-gap map and replay checklist.
- **$497/mo:** quarterly refresh, drift review and audit-export reconciliation.
- **$2,000:** five-vendor cohort benchmark.
- **$2,485 MRR ceiling:** five retained vendor seats using the verified YanXbt pattern.

## Follow-up cadence
- **+2 days:** send the 22-column CSV schema.
- **+5 days:** send the five-vendor non-overlap snapshot.
- **+10 days:** close the loop unless there is an active evaluation.

## Route safety
First-party route verified 2026-07-25: `mailto:contact@dottxt.co` and the Book a Demo route on `https://dottxt.ai/`. This job did **not** send email or submit a form. SMTP/form gated; $0 sent / $0 received.
