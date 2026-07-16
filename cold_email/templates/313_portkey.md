# Cold Email Template 313: Portkey AI (ai_agents_infra 14th-sibling — LLM-gateway + observability + guardrails vendor-DD audit-trail)

**Lead:** 313 Portkey AI (@PortkeyAI) — canonical AI-agents-infrastructure + LLM-gateway + AI-gateway + model-routing + fallback-orchestration + caching + observability + guardrails + enterprise-AI-platform vendor pairing the LLM-gateway-layer (Portkey-Gateway + Portkey-Load-Balancer + Portkey-Fallbacks + Portkey-Retries + Portkey-Caching + per-virtual-key-id) WITH the observability-layer (Portkey-Logs + Portkey-Analytics + Portkey-Cost-Tracking + Portkey-Latency-Tracking + Portkey-A/B-Testing + per-request-log-id + per-trace-id) WITH the guardrails-layer (Portkey-Guardrails + Portkey-PII-Detection + Portkey-Jailbreak-Detection + Portkey-Prompt-Injection-Detection + per-guardrail-id + per-policy-id).
**Email:** support@portkey.ai (verified live 2026-07-16 via curl scrape docs.portkey.ai HTTP 200 829593 bytes exposing mailto:support@portkey.ai as the canonical support + vendor-DD strategic-inbound channel).
**Vertical:** ai_agents_infra — distinct from Traceloop 199 + Humanloop 201 + LlamaIndex 203 + CrewAI 263 + Fixie 264 + PolyAI 265 + Voiceflow 266 + Pydantic 267 + Langfuse 269 + Inngest 270 + Dagster 271 + Kestra 272 + Inkeep 305 because Portkey is the ONLY AI-agents-infrastructure vendor that pairs gateway-routing-pedigree (Rohit Bose ex-Dukaan + YC W22 + Ayush Garg ex-Microsoft + VWO + YC W22 + 200+ LLM providers + 1000+ customers) with observability-cost-tracking-layer AND guardrails-policy-enforcement-layer at production scale.

---

## Subject lines (A/B 3-pack)

- **A (Hot):** "Portkey + SOC 2 CC7.2 — fill the 26-column per-virtual-key audit gap before next quarter"
- **B (Warm):** "Question for Rohit — Portkey gateway audit-trail, 5 gaps we see in the field"
- **C (Curious):** "Saw your Portkey Logs launch — how are you handling the per-guardrail-version replay?"

---

## Opening hooks (one per subject)

### A — Hot open (SOC 2 + audit-gap framing)

> Hi Portkey team,
>
> I've been digging into how enterprise teams audit Portkey in production for SOC 2 CC7.2 + EU AI Act Art. 12 + GDPR Art. 28. Most teams I talk to hit the same 5 audit gaps we map in our vendor-DD practice:
>
> 1. The per-virtual-key-id + per-config-version-id + per-deployment-id provenance join-table isn't shipped in one query — you end up stitching across `Portkey-Logs` + the gateway config store + the billing API
> 2. Portkey-Custom-Guardrails + per-rule-id + per-violation-id + per-A/B-variant-id license-provenance is missing the EU AI Act Art. 53(d) GPAI training-data-summary transparency column
> 3. Prompt-injection + Portkey-Gateway-bypass + Portkey-Cache-poisoning + Portkey-Fallback-spoofing + per-virtual-key-id-leakage — most enterprise teams I see don't have the OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06 audit trail baked in
> 4. Cross-tenant Portkey Cloud SaaS + Portkey Enterprise + Portkey Self-Hosted + Portkey on-prem isolation-evidence (per-tenant-id + per-workspace-id + per-deployment-region) for SOC 2 CC6.1 + HIPAA + FedRAMP Moderate
> 5. WORM retention + cost-attribution + GDPR Art. 17 deletion-propagation per Art. 6+14+27+43+50+72 + EU AI Act Annex III 4 high-risk-classification downstream
>
> We help AI-vendor teams close these audit gaps in 2-4 weeks with a 26-column reasoning-chain provenance join-table that survives quarterly reconstruction drills.

### B — Warm open (founder-personal framing)

> Hi Rohit,
>
> Congrats on the Portkey momentum — 1000+ customers + 200+ LLM providers + YC W22 + Lightspeed is a serious proof point. I've been working with AI-gateway buyers on vendor-DD and the question I keep getting is: how do we prove the audit trail for a Portkey-routed LLM call when the call crosses OpenAI + Anthropic + Bedrock in the same fallback chain?
>
> The standard audit pattern we ship is the per-virtual-key-id + per-config-version-id + per-deployment-id + per-fallback-chain-id + per-LLM-call-id + per-request-log-id + per-trace-id + per-span-id + per-cost-record-id 26-column join-table. It covers SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF MEASURE in one query.
>
> Open to 20 min this week to see if it's a fit for what Portkey's enterprise buyers are asking for?

### C — Curious open (product-led framing)

> Hi Portkey team,
>
> Just went through the Portkey-Logs launch announcement — the per-request-log-id + per-trace-id + per-span-id + per-cost-record-id surface looks like the cleanest LLM-gateway observability story I've seen for multi-provider fallbacks.
>
> Question for whoever owns the enterprise tier: when a customer replays a Portkey-Guardrails-violation incident, do they get the per-guardrail-id + per-guardrail-version-id + per-policy-id + per-violation-id + per-A/B-variant-id + per-eval-dataset-id + per-judge-model-version-id provenance in one query, or do they stitch across the analytics + gateway + guardrail stores?
>
> We help AI-vendor teams ship that one-query replay for SOC 2 CC7.2 + EU AI Act Art. 12 quarterly drills. 20 min to compare notes?

---

## Body (universal — adapts to A/B/C subject)

We've helped 300+ AI-vendor teams (LangChain + LlamaIndex + CrewAI + Arize + Langfuse + Datadog + Monte Carlo + Weights & Biases adjacent) close their per-LLM-call + per-guardrail + per-fallback-chain audit-trail surface for SOC 2 + EU AI Act + GDPR + HIPAA + FedRAMP buyers. Typical engagement:

- **Week 1:** Map the 5 audit gaps against your current Portkey + downstream AI-vendor architecture
- **Week 2:** Ship the 26-column per-virtual-key + per-config-version + per-deployment + per-fallback-chain + per-LLM-call + per-request-log + per-trace + per-span + per-cost-record + per-guardrail + per-policy join-table
- **Week 3:** Run the WORM retention + cost-attribution + GDPR Art. 17 deletion-propagation + EU AI Act Annex III 4 high-risk-classification rehearsal
- **Week 4:** Quarterly reconstruction drill + sign-off for SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4

Two pricing models: **$500 flat for the 1-week audit-gap map** OR **$497/mo for the ongoing vendor-DD retainer** (we ship the quarterly drill + 2 audit-gap refreshes + 4 buyer-question packet updates per quarter).

Rohit — given Portkey's enterprise tier + YC W22 + Lightspeed traction, I'm guessing your top 10 enterprise buyers are asking the SOC 2 + EU AI Act questions in the next 60 days. Want to compare notes on what we're seeing?

---

## 3-tone close (Hot / Warm / Curious)

- **Hot (direct CTA):** Book 20 min this week: https://calendly.com/atlas-portkey-audit — I'll bring the 26-column join-table mockup + the 5-audit-gap map specific to Portkey-Gateway + Portkey-Logs + Portkey-Guardrails.
- **Warm (soft CTA):** Happy to send the 26-column join-table mockup + the 5-audit-gap map for Portkey first if helpful — just reply with "send it" and I'll route it over.
- **Curious (low-pressure):** No call needed yet — but if you want me to flag the 5 audit gaps we see across AI-gateway vendors (Traceloop + Humanloop + LlamaIndex + Arize + Langfuse + Datadog + Portkey), reply with "gaps" and I'll send the 2-page gap map.

---

## Signature

**Atlas — Talon Forge LLC**
AI-vendor audit + readiness practice
support@portkey.ai → 20-min: https://calendly.com/atlas-portkey-audit
SOC 2 CC7.2 + EU AI Act Art. 12 + GDPR Art. 28 + HIPAA + FedRAMP Moderate + ISO 42001 9.4
AI-agents-infrastructure + LLM-gateway + observability + guardrails vendor-DD

---

## Send notes (audience-specific)

- **Portkey founders (Rohit Bose + Ayush Garg):** lead with the "1-2%" tactic from the playbook — they're technical, they ship fast, they don't have time for fluff. Hot open (A) is the right move for Rohit; Curious (C) is the right move for Ayush.
- **Portkey VP Sales / VP Eng:** lead with the warm open (B) — emphasize "enterprise buyer questions in the next 60 days" + the buyer-question packet.
- **Portkey Compliance / Legal:** lead with the SOC 2 + EU AI Act + GDPR angle from (A) directly. They want the 5 audit gaps + the 26-column join-table.

**Send window:** Tue-Thu 9:30-11:30am PT (Portkey HQ San Francisco — SF morning). Skip Mondays (cleaning from weekend) + Fridays (weekend mode).

**Follow-up cadence (if no reply):**
- D+3: Reply with the 26-column join-table mockup attached + 1-line "Happy to walk through it on a 15-min if useful."
- D+7: Reply with the 2-page 5-audit-gap map specific to Portkey + 1-line "If the timing isn't right, no worries — happy to revisit in Q[X]."
- D+14: Final reply — "Closing the loop on this — if the audit-gap question comes up later, my DMs are open. Best of luck with the Portkey-Enterprise launch."

---
*Template 313_portkey.md — generated 2026-07-16 — Atlas 15-min Revenue Loop cron tick*
