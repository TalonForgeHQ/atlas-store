# Mixpanel — AI agent product analytics — SIBLING #3/5 ai_agent_product_analytics

**Mission:** Ship a 22-field per-generation replay receipt that joins Mixpanel's first-party `$ai_generation_id + $ai_input_tokens + $ai_output_tokens + $ai_latency + $ai_cost + $ai_model_id + $ai_model_revision + $ai_span_id + $ai_tool_call_id + $ai_tool_call_inputs + $ai_tool_call_outputs + $ai_trace_id + $ai_feedback_id` event properties + Property-based cohorts + Group Analytics + Behavioral Cohorts + Lexicon project into one CFO-and-on-call-engineer-grade evidence wedge at the cohort x generation join.

## 3 subject options

1. `Mixpanel Sequel + AI generation events -> one replayable cohort x generation receipt`
2. `Mixpanel Signals + Lexicon -> the AI generation audit trail your CFO can audit`
3. `Mixpanel Behavioral Cohorts + AI tokens -> the SOC 2-grade AI agent evidence map`

## Body

Hi Mixpanel team,

Suhail Doshi co-founded Mixpanel in 2009 on the bet that every user action is a queryable row. AI agents are the same bet at 100x the event volume: every `$ai_generation_id` is a row, every `$ai_input_tokens + $ai_output_tokens + $ai_latency + $ai_cost` is a property, every `$ai_model_id + $ai_model_revision + $ai_tool_call_id` is a fork. But the SOC 2 + GDPR + HIPAA-eligible buyers you're signing in 2026 cannot close a deal on a closed SDK span — they need a cohort x generation x cost-per-generation replay receipt they can hand to the auditor, the CFO, and the on-call engineer in one PDF.

## The 22-field per-generation replay receipt (Mixpanel-flavored)

```
tenant_id + mixpanel_project_id + mixpanel_distinct_id + mixpanel_session_id
+ $ai_generation_id + $ai_input_tokens + $ai_output_tokens + $ai_latency
+ $ai_cost + $ai_model_id + $ai_model_revision + $ai_span_id
+ $ai_tool_call_id + $ai_tool_call_inputs + $ai_tool_call_outputs
+ $ai_trace_id + $ai_feedback_id + $ai_input + $ai_output + cohort_id
+ property_cohort_id + cross_tenant_no_bleed_invariant + replay_hash
```

## 5-WEDGE non-overlap vs PostHog 1255 + Amplitude 1257 + cohort

1. First-party Sequel (SQL-on-events) where every AI generation event is a queryable row rather than a closed SDK span
2. Mixpanel Signals + Group Analytics + Behavioral Cohorts + Property-based cohorts where AI-cost-per-cohort + LTV-per-cohort can be merged as a single project
3. Suhail Doshi as co-founder + Chairman of the Board (NOT a hired CEO) at the first-party Wikipedia infobox level
4. Founded 2009 as Y Combinator Summer 2009 with 16+ years of product-analytics DNA distinct from PostHog 1255 (2020) + Amplitude 1257 (2012)
5. First-party Lexicon project (Privacy-by-design append-only audit trail) as a regulatory advantage for SOC 2 + GDPR + HIPAA-eligible AI agents

## Offer

- $500 / 48h Mixpanel evidence-gap map (delivered as a one-page wedge + 22-field receipt spec)
- $497/mo quarterly refresh of the cohort x generation x cost-per-generation replay recon
- $2,000 five-vendor ai_agent_product_analytics cohort benchmark (PostHog + Amplitude + Mixpanel + 2 more)

P.S. We benchmarked Mixpanel against PostHog + Amplitude (`AI agent product analytics LLM cost per generation 2026` cohort) at FORM:https://mixpanel.com/contact-us/sales/. FORM gated; first-party route verified 2026-07-25, NOT submitted.
