# Cold Email Template 357 — Gong (privacy@gong.io)

**To:** privacy@gong.io (verified live 2026-07-16 via curl on https://www.gong.io/privacy-policy/)
**From:** Atlas (Talon Forge LLC — Atlas Store)
**Subject:** question for Gong's data-governance team — per-call provenance at AI-act scale

---

Hi Gong team —

Quick question on how you handle audit-trail provenance across the Gong Revenue AI Platform now that EU AI Act Article 12 risk-management + Article 14 human-oversight + Article 17 deletion-propagation are in force, especially for Gong Calls + Gong Engage + Gong Forecast + Gong AI Insights + Gong Protect (MiFID II + FINRA 4511 + FCA recordkeeping).

The 5 audit-trail gaps we keep seeing across Tier-1 conversation-intelligence platforms:

1. **Per-conversation-call + per-speaker-utterance + per-LLM-extraction-model-run + per-prompt-version provenance join-table** at the per-call + per-transcript + per-deal + per-rep + per-region granularity SOC 2 CC7.2 + EU AI Act Art. 12 demand when a customer asks "show every model run + every prompt + every output that touched this deal-risk-score." Most platforms capture calls and scores separately; the join key is reconstructible in an incident but not in a 30-day auditor window.

2. **WORM retention + MiFID II + FINRA 4511 + FCA CONRED recordkeeping flags per Gong Protect storage object** — auditors want a single query that proves a 7-year WORM hold is active on a specific Gong conversation + Gong Protect recording + Gong AI Insights extraction-record by ID + region, with the per-customer controlled Opt-Out-Of-AI-Training + per-no-train-zone + per-tenant KMS CMK/BYOK flag baked in. Platforms that store the flag in a separate metadata table leave a 1-row gap that's enough for an Art. 28 processor-adequacy finding.

3. **Gong call-corpus + Gong meeting-corpus + Gong email-corpus + Gong-support-ticket-corpus + Gong-deal-record-corpus + Gong-engagement-corpus + Gong-forecast-snapshot license-provenance per EU AI Act Article 53(d) GPAI training-data transparency + Article 53(1)(b) copyright-summary + Article 53(2) publicly-available-summary** — covering per-corpus-hash + per-license-SPDX-id (apache-2.0 / MIT / OpenRAIL / custom) + per-cross-border-transfer-sccs-version + per-gdpr-dpa-signed-version + per-Common-Crawl-inheritance-flag. Auditors in Q3 2026 are starting to ask which corpora are sourced where.

4. **Per-tenant KMS CMK/BYOK + per-cross-border-transfer-sccs-version + per-tenant-data-residency-region + per-no-train-zone-flag + per-customer-controlled-Opt-Out-Of-AI-Training-flag cross-tenant isolation evidence per SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10** — covering per-workspace-id-hash + per-call-isolation-flag + per-Insights-extraction-isolation-flag + per-engagement-cadence-isolation-flag + per-cross-border-transfer-data-flow-country-chain. Auditors increasingly demand cross-workspace leakage drills — "show me that workspace A's Gong Calls can never reach workspace B's Gong AI extraction pipeline."

5. **Prompt-injection + Gong-call-transcript-poisoning + Gong-engagement-cadence-poisoning + Gong-Insights-extraction-poisoning + Gong-Data-Extract-ingestion-poisoning + Gong-Protect-WORM-bypass defense per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + NIST AI RMF MEASURE + ISO 42001 6.1.4** — covering per-call-id + per-transcript-segment-id + per-Insights-extraction-id + per-engagement-cadence-step-id + per-WORM-record-id + per-no-train-zone-flag + per-defense-version + per-incident-link. Auditors want the row-level audit-log of the defense, not the policy.

If any of these is on the Gong data-governance roadmap for the next 2 quarters, happy to compare notes on what we've seen work — we audit a few Tier-1 conversation-intelligence + revenue-AI platforms per month and there's a real pattern forming.

— Atlas
Talon Forge LLC — Atlas Store
https://atlas-store.example (request audit-report sample)
