# Cold Email Template 397 — Helicone (llm_observability, Tier-1, 2nd-sibling)

**To:** contact@helicone.ai
**From:** josh@talonforge.ai
**Subject:** Helicone's OpenAI-compatible proxy → SOC 2 audit trail question

---

Hi Cole,

Helicone's one-line drop-in proxy is the cleanest LLM observability surface we've audited in 2026 — every request, every token, every cost line written through the existing OpenAI SDK path with zero code change.

One audit question:

**Does the per-request log persist end-to-end through every model-routing fallback in your proxy chain?** When a request hits GPT-4o, falls back to Claude Sonnet on rate-limit, then caches the response — does your trace join-table carry the same `request_id` across all three hops with per-hop cost + latency + token-usage + cache-hit-metric, or does the fallback re-issue a fresh `request_id` that breaks lineage at the observability layer?

We're seeing this exact pattern fail SOC 2 CC7.2 (system operations monitoring) at observability vendors we audit — the trace looks complete in the dashboard, but the join-table breaks at the fallback boundary, which means the auditor can't follow one logical request from user prompt to cached response.

For Helicone specifically, this matters because the proxy is positioned as the **single observability surface** for the entire LLM stack. If the trace breaks at the fallback, every downstream compliance claim inherits the gap.

The 5 audit questions that usually surface for an OpenAI-compatible observability proxy:

1. Does the `request_id` survive per-model-routing-fallback + per-cache-key + per-cache-hit + per-cache-miss + per-retry + per-streaming-chunk?
2. Does the trace include the upstream OpenAI/Anthropic response headers (`x-request-id`, `x-ratelimit-remaining`) or only the body you proxy back?
3. Is there a per-tenant-key-id → per-request-id → per-model-call-id → per-token-id → per-cache-key-id provenance table, or only flat request logs?
4. Does the prompt-versioning system carry per-version-id → per-deployment-id → per-rollback-id lineage, or just timestamp the version switches?
5. Does the custom-properties threading (user/session/conversation) survive model swaps, or reset on fallback?

If you can point me at the trace schema + a sample multi-hop request showing per-hop lineage, I'll send back a written gap analysis by Friday — no charge, no follow-up sales call.

Best,
Josh @ Talon Forge
helicone.ai audit-target inquiry · contact@helicone.ai

---

**Word count:** ~270
**Pattern:** vendor-DD opener (audit-question framing, not sales pitch) + 5 numbered questions + value-first close (free gap analysis)
**Channel:** strategic-inbound cold email
**Vertical:** llm_observability
**Cohort:** 2nd-sibling after Arize 396 (VERTEX)
