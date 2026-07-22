# 890 — Honeycomb (AI Agent Observability + OpenTelemetry)
**Lead tier:** 1 — ai_llm_observability sibling #3/5
**Cohort sequence:** Langfuse 888 OPENER → Arize AI 889 → **Honeycomb 890** → Maxim AI 891 → LangSmith 892 CLOSER
**Commercial route:** FORM:https://www.honeycomb.io/get-a-demo
**Offer:** $500/48h audit + $497/mo evidence refresh

---

## Variant A — humans-and-agents production-evidence angle

**Subject:** Honeycomb's humans + agents mission: one replayable trace receipt

Charity, Christine —

Honeycomb's first-party mission now explicitly covers engineering teams of humans and agents. That creates a new procurement question beyond ordinary distributed tracing: can one production incident be replayed across the human action, agent timeline, model generation, retrieval span, tool call, evaluator result, and tenant boundary without reconstructing evidence by hand?

We build that as an 18-column per-LLM-trace receipt: trace + span + generation + model version + prompt version + evaluator version + tenant-scoping proof.

For Honeycomb, the wedge is unusually clean because the operational context already lives in OpenTelemetry-native traces. The missing artifact is often the buyer-facing evidence map that joins Agent Timeline + LLM Observability + MCP/tool calls to the security-review packet.

Would a $500, 48-hour sample evidence map be useful for the team running AI Agent Observability procurement conversations?

— Atlas

---

## Variant B — OpenTelemetry migration angle

**Subject:** OTel → agent timeline: the evidence gap buyers will ask about

Charity, Christine —

Teams adopting Honeycomb already have service, environment, trace, and span context. When they add AI agents, buyers start asking for four additional joins: model version, prompt version, tool-call/retrieval lineage, and the human or automated oversight decision that followed the result.

We package those joins as a replayable evidence receipt rather than another dashboard:

`tenant_id → llm_trace_id → llm_span_id → llm_generation_id → model_version → prompt_version → eval_run_id → eval_judge_version → tenant_boundary → no_bleed_proof`

Honeycomb is the strongest operational-debugging member in our five-vendor LLM-observability cohort because OpenTelemetry, Agent Timeline, MCP, and Private Cloud sit on one first-party platform surface.

Can I send the one-page cohort map comparing Honeycomb's OTel-native receipt against Langfuse 888 and Arize AI 889?

— Atlas

---

## Variant C — enterprise customer proof angle

**Subject:** Slack / Intercom / Dropbox proof → a 48h AI-agent audit map

Charity, Christine —

Honeycomb's first-party About page puts Slack, Intercom, and Dropbox beside an explicit humans-and-agents mission. For enterprise buyers, the gap is no longer whether the platform can trace production systems. It is whether the procurement packet can replay an agent decision across model, prompt, tool, retrieval, evaluator, and tenant-scoping versions.

Atlas turns that into a 48-hour audit-grade evidence map for $500, then a $497/mo refresh as instrumentation and agent stacks change.

The deliverable is concrete: an 18-column per-LLM-trace receipt, OpenTelemetry attribute map, WORM-export checklist, and cross-tenant-no-bleed test matrix mapped to Honeycomb's Agent Timeline + LLM Observability surfaces.

Who owns the AI Agent Observability evidence story for enterprise security reviews?

— Atlas

---

## Pre-send checklist (verified 2026-07-22)

- [x] First-party company verification: Honeycomb About Us HTTP 200, server-rendered.
- [x] Founder verification: Charity Majors CTO / Co-founder; Christine Yen identified in first-party founder-story text.
- [x] Product verification: AI Agent Observability + Agent Timeline + LLM Observability + Agentic Intelligence + MCP + OpenTelemetry + Private Cloud.
- [x] Customer proof: Slack + Intercom + Dropbox on first-party About surface.
- [x] Commercial route: `FORM:https://www.honeycomb.io/get-a-demo` discovered twice in rendered About HTML.
- [x] No guessed general-business inbox; FORM-only per pitfall #28.
- [x] Cohort state: sibling #3/5 after Langfuse 888 + Arize AI 889.
- [x] No fabricated send, form submission, payment, or revenue.

## Send gates

1. SMTP/form action remains gated; this artifact is queued, not sent.
2. Use the first-party demo form only; do not route commercial outreach to support or security contacts.
3. If submitted later, preserve the exact subject/body variant, UTC timestamp, and response receipt.
