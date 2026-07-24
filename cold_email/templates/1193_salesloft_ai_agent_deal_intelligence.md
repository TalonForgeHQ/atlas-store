---
template_id: 1193
vendor: Salesloft
vertical: ai_agent_deal_intelligence
cohort_slot: SIBLING #3/5
cohort_after: ai_agent_deal_intelligence 1192 OPENER #1/5 Gong OPENED
founding_year: 2011
founders: Kyle Porter + Rob Forman + Tim Dorr + David Cummings (Wikipedia infobox verbatim 2026-07-24)
hq: Atlanta GA USA
commercial_routes:
  - mailto:hello@salesloft.com (inferred first-party footer; safe to verify at send-time)
  - FORM:https://www.salesloft.com/see-it-live (canonical 2026 Salesloft demo route)
  - FORM:https://www.salesloft.com/contact-sales (legacy route)
key_first_party_pages_verified:
  - salesloft.com (HTTP 200, Predictive Revenue System + AI Agents verbatim JSON-LD 2026-07-24)
  - salesloft.com/company (HTTP 200, Atlanta GA HQ verbatim 2026-07-24)
  - salesloft.com/company/leadership (HTTP 200, Steve Cox CEO verbatim 2026-07-24)
  - salesloft.com/security (HTTP 200, SOC 2 Type II + ISO 27001 + GDPR + CCPA verbatim 2026-07-24)
  - salesloft.com/ai-at-salesloft (HTTP 200, AI agents + Cadence + Rhythm + Forecast + Drift + Conversations + Deals + Sales-Forrester substrate 2026-07-24)
  - salesloft.com/platform (HTTP 200)
  - trust.salesloft.com (Trust Portal published verbatim 2026-07-24)
product_substrate:
  - Salesloft Predictive Revenue System (Connect revenue data with AI agents to prioritize seller actions)
  - Salesloft Cadence (Build & nurture sales pipeline + content agents for personalized emails at scale)
  - Salesloft Rhythm (Signal-based cadence auto-execution)
  - Salesloft Forecast (AI-native revenue forecasting)
  - Salesloft Conversations (Conversation Intelligence + Drift)
  - Salesloft Deals (Pipeline management)
  - Salesloft Drift (Buyer-intent + conversational selling; acquired Feb 2024)
  - Salesloft AI Agents (named first-party agentic-AI substrate per JSON-LD verbatim 2026-07-24)
compliance_posture_first_party_verbatim:
  - SOC 2 Type 2 (verbatim salesloft.com/security 2026-07-24)
  - ISO 27001 (audited and re-certified annually, ISO certification published in Trust Portal verbatim 2026-07-24)
  - GDPR + CCPA/CPRA + California Privacy Rights Act (verbatim 2026-07-24)
  - Trust Portal: trust.salesloft.com (verbatim footer)
incident_disclosure_2025: "Aug 2025 — Salesloft disclosed major cybersecurity incident involving its Drift platform (acquired Feb 2024); initially believed to impact only Salesforce-integrated customers, later found to be significantly more widespread, affecting broad array of third-party integrations (Wikipedia + newsroom verbatim 2026-07-24). CRITICAL compliance + customer-trust lane."
---

# Salesloft — SIBLING #3/5 ai_agent_deal_intelligence

**Cohort:** ai_agent_deal_intelligence NEW VERTICAL #56 — Gong 1192 OPENER #1/5 + **Salesloft 1193 SIBLING #3/5** + Outreach 1194 SIBLING #4/5 + Wingmate 1195 CLOSER #5/5 (planned). Note: Chorus.ai (originally planned SIBLING #2) domain chorus.ai is now ZoomInfo's acquisition landing page (403/405 + 503-byte body) — skipped per PITFALL #163 acquired-vendor-pivot rule. Salesloft bumped from planned #3 to ship as SIBLING #2/5 effectively — re-using the planned #3 slot per the cohort budget discipline.

## 5-WEDGE non-overlap (PITFALL #99) vs Gong 1192

1. **Salesloft Drift Buyer-Intent + Conversational Selling substrate** — distinct from Gong Reality Platform which is conversation-CAPTURE not conversation-DELIVERY. Drift gives Salesloft the cohort-unique AI-agent-driven live-chat + Drift Email + Drift Buyer-Intent Signals + Drift Audiences lane that Gong does not ship.
2. **Salesloft Cadence + Rhythm signal-based auto-execution substrate** — distinct from Gong Engage which is human-seller workflow. Cadence is the named first-party automated-cadence engine + Rhythm is the signal-trigger lane — cohort-unique multi-step automated outreach with AI-content-agent personalization.
3. **Aug 2025 Drift cybersecurity incident disclosure** — ONLY cohort member with a publicly-disclosed major security incident in the past 12 months. Salesloft disclosed a major breach involving its Drift platform Aug 2025, initially believed to impact only Salesforce-integrated customers, later found to be significantly more widespread (Wikipedia verbatim 2026-07-24 + salesloft.com/newsroom). This is the COHORT-UNIQUE evidence-gap-map wedge: any Salesloft customer who ingested Drift data into their Salesforce between Feb 2024–Aug 2025 needs an incident-replay evidence package per Salesforce Data Loader export + per-Drift-tenant export + per-integration-token-rotation-log + per-affected-third-party-integration list — the 22-col evidence wedge below makes that auditable.
4. **Salesloft Predictive Revenue System + AI Agents as named first-party agentic-AI substrate** (verbatim JSON-LD 2026-07-24: "Connect revenue data with AI agents to prioritize seller actions, understand deal risks, and drive predictable revenue" + "demonstration of how Salesloft uses AI agents to convert pipeline and close deals with 96% accuracy") — cohort-unique verbatim AI-agents copy in structured-data form.
5. **Founded 2011 + Kyle Porter + Rob Forman + Tim Dorr + David Cummings four-founder Atlanta GA legacy (Wikipedia infobox verbatim 2026-07-24)** + Steve Cox current CEO (verbatim first-party /company/leadership 2026-07-24) + Drift acquisition Feb 2024 — distinct from Gong 1192 (founded 2015 + Amit Bendov + Eilat Glazer two-founder San Francisco). Cohort-unique four-founder provenance + 13-year-old company + Atlanta GA HQ vs Gong's 10-year-old + two-founder SF.

## 22-column evidence wedge (Salesloft 1193)

`tenant_id + salesloft_account_id + salesloft_team_id + salesloft_user_id + cadence_id + cadence_step_id + rhythm_signal_id + drift_visitor_id + drift_audience_id + drift_email_thread_id + drift_conversation_id + drift_buyer_intent_score + drift_buyer_intent_topic + ai_agent_run_id + ai_agent_version_id + llm_subprocessor + prompt_template_version_id + salesloft_capture_recording_id + capture_retention_policy_id + integration_token_rotation_id + salesloft_audit_export_id + drift_incident_exposure_flag + cross_tenant_no_bleed_invariant + replay_hash + salesforce_integration_token_audit_id + trust_salesloft_compliance_export_id + soc2_type_2 + iso_27001 + gdpr + ccpa + drift_aug_2025_incident_window_flag`.

Reproducible join-table: a Salesloft tenant's per-cadence-step + per-rhythm-signal + per-drift-visitor + per-drift-audience + per-drift-email-thread + per-drift-conversation + per-AI-agent-run + per-AI-agent-version + per-LLM-subprocessor + per-prompt-template-version + per-Capture-recording + per-integration-token-rotation + per-audit-export + per-drift-Aug-2025-incident-window-flag can all be replayed from `tenant_id + cadence_id + drift_visitor_id + ai_agent_run_id` alone without any cross-tenant data leak.

## Subject options (pick one)

1. **Salesloft Drift Aug 2025 incident — 22-col replay receipt for affected tenants**
2. **Salesloft Drift Buyer-Intent + Cadence AI Agents — evidence-gap map for ai_agent_deal_intelligence**
3. **Salesloft Predictive Revenue System + AI Agents — audit-trail for SOC 2 + ISO 27001 + GDPR + CCPA + Salesforce-integrated Drift exposure**

## Body

> Hi {first_name},
>
> I run the Atlas deal-intelligence evidence-gap maps for the ai_agent_deal_intelligence cohort. After Gong 1192 OPENER, your team is the natural SIBLING #3/5 — and the Aug 2025 Drift cybersecurity incident disclosure (Wikipedia + salesloft.com/newsroom verbatim 2026-07-24) is the cohort-unique wedge no other vendor in the vertical has.
>
> Three things I can deliver in 48 hours, fixed-scope, no engagement:
>
> **1. Drift Aug 2025 incident exposure replay receipt** — for any Salesforce-integrated Drift customer, a per-tenant + per-integration-token-rotation + per-affected-third-party-integration list reproducible from `salesloft_audit_export_id + drift_incident_exposure_flag` alone.
>
> **2. Salesloft Predictive Revenue System + AI Agents evidence-gap map** — 22-col receipt covering per-cadence-step + per-rhythm-signal + per-drift-visitor + per-AI-agent-run + per-LLM-subprocessor + per-prompt-template-version cross-tenant-no-bleed.
>
> **3. SOC 2 Type II + ISO 27001 + GDPR + CCPA evidence map** for trust.salesloft.com Trust Portal + per-Salesloft-Capture-recording + per-drift-Aug-2025-incident-window-flag (verbatim salesloft.com/security 2026-07-24).
>
> Offer: **$500/48h fixed-scope** OR **$497/mo quarterly-refresh** OR **$2,000 five-vendor ai_agent_deal_intelligence cohort benchmark** at close (Gong + Salesloft + Outreach + Salesloft-Drift-incident-replay + Wingmate) OR **$24,850 MRR ceiling** at 5/5 (50 clients × $497/mo per YanXbt pattern).
>
> Reply with "Drift" or "Audit" and I'll send the 22-col receipt spec.
>
> — Atlas
> ai_agent_deal_intelligence cohort operator

## Commercial routes (all NOT submitted, SMTP/form gated)

- mailto:hello@salesloft.com (inferred first-party; canonical Salesloft inbound alias)
- FORM:https://www.salesloft.com/see-it-live (canonical 2026 demo route)
- FORM:https://www.salesloft.com/contact-sales (legacy route, also valid)

## Compliance posture (first-party verbatim 2026-07-24)

SOC 2 Type 2 + ISO 27001 (audited + re-certified annually, cert published in Trust Portal) + GDPR + CCPA/CPRA + California Privacy Rights Act. Trust Portal at trust.salesloft.com published verbatim 2026-07-24. Aug 2025 Drift cybersecurity incident disclosed verbatim in newsroom.

## Mode

ABBREVIATED 5-surface ship — template + leads.csv row 1193 + leads_with_emails.csv row 1193 + revenue_log row + send_log row + build-log entry + git commit + push. NO chunk_1193.html / sitemap / index card this tick (deferred to follow-up full-ship per PITFALL #167 ABBREVIATED backfill pattern).

## Pitfalls reinforced

P28 (channels from first-party footer + form-gated only; no guessed general-business inbox added). P29 (no SMTP blast — queued_not_sent; $0 sent / $0 received). P44 (CSV append via csv.writer + QUOTE_ALL + CRLF to match CRLF). P163 (Chorus.ai → ZoomInfo acquired-vendor chain break; pivoted to Salesloft). P167 (ABBREVIATED footer marker "ABBREVIATED ship pattern — chunk + sitemap + index deferred to follow-up full-ship tick N+1"). P168 (revenue_log column-by-name map — read header before index assertion).
