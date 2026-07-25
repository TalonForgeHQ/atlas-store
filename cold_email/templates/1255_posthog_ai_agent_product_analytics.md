# PostHog (Lead 1255) — OPENER #1/5 NEW VERTICAL #67 ai_agent_product_analytics

**Vendor:** PostHog (https://posthog.com)
**Contact route:** https://posthog.com/wizard (form gated, NOT submitted)
**Founder witness:** James Hawkins (Co-founder & CEO, first-party /about page)
**Cohort position:** OPENER #1/5 of NEW VERTICAL #67 ai_agent_product_analytics

## Why this lead is the OPENER

PostHog is the only cohort candidate with a first-party `llm-analytics` product surface
that emits the full `$ai_generation + $ai_input + $ai_output + $ai_latency + $ai_cost`
fields as a single SDK call. That makes it the canonical opener for an AI agent
product analytics cohort that has to ship a 22-field per-generation replay receipt.

## 5-WEDGE non-overlap (vs the cohort's still-pending siblings)

1. First-party LLM Analytics surface (llm-analytics SDK)
2. Developer-first suite (analytics + replay + flags + experiments + heatmaps + surveys + error tracking + warehouse + CDP)
3. Free-tier + $0/mo pay-as-you-go SDK + open-source deployment
4. Heatmaps + Session Replay + CDP adjacent to LLM analytics
5. James Hawkins first-party Co-founder & CEO witness

## 22-field replay schema (one AI generation)

tenant_id + posthog_project_id + distinct_id + session_id + $ai_generation_id +
$ai_input + $ai_output + $ai_input_tokens + $ai_output_tokens + $ai_latency +
$ai_cost + $ai_model_id + $ai_model_revision + $ai_span_id + $ai_tool_call_id +
$ai_tool_call_inputs + $ai_tool_call_outputs + $ai_trace_id + $ai_feedback_id +
cross_tenant_no_bleed_invariant + replay_hash + retention_id

## Outreach angle (NOT submitted)

Subject: PostHog llm-analytics — 22-field per-generation replay receipt

Hi James,

Your llm-analytics SDK already emits `$ai_generation_id + $ai_input + $ai_output +
$ai_latency + $ai_cost` in a single call. The missing piece for AI agent product
teams is the rollout: cost-per-generation rolled up against revenue per user,
tool-call margin attribution, and a `cross_tenant_no_bleed_invariant` so a
multi-tenant deployment can prove isolation.

We map one tenant in 48 hours for $500 and surface the 5 evidence gaps the
on-call engineer does not see today. $497/mo keeps it fresh;
$2,000 buys a five-vendor cohort benchmark.

Three links instead of a calendar:
[Cost-per-generation audit] [Tool-call ROI map] [Five-vendor cohort]

— Atlas @ Talon Forge

## Offer
- $500 / 48 hours — one per-tenant AI generation receipt evidence-gap map
- $497 / month — quarterly refresh across the 22-field LLM analytics boundary
- $2,000 — five-vendor ai_agent_product_analytics cohort benchmark

## Status
- Form gated; $0 sent / $0 received
- [tick-1255-posthog-ai-agent-product-analytics-opener-1-of-5]
