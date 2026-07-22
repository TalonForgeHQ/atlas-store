# Grafana Labs — Procurement-Review Cold Email (template 934)

**Vertical:** ai_observability_platform_broad
**Cohort position:** CLOSER #5/5 (after Datadog 891 OPENER #1/5 + Dynatrace 910 SIBLING #2/5 + New Relic 911 SIBLING #3/5 + Splunk Observability 933 SIBLING #4/5)
**First-party source:** https://grafana.com (HTTP 200, 2026-07-22) + https://grafana.com/grafana-cloud-llm/ + https://grafana.com/pricing/ + https://grafana.com/about/ + https://grafana.com/legal/
**Sanctioned contact route:** `https://grafana.com/contact/` (canonical first-party form, HTTP 200 — no guessed general-business inbox per pitfall #28)

## 3 Subject Options

1. `Grafana Cloud LLM + Grafana MCP — procurement questions on per-LLM-call evidence`
2. `Grafana Labs — OSS-first AI-trace diligence for Grafana Cloud LLM + Beyla + k6`
3. `Grafana Labs — Cloud-Free-to-Advanced tier procurement review for 2026`

## Cold Email Body

Hi {{first_name}},

Saw that Grafana Cloud now ships **Grafana Cloud LLM** ("Observability for your LLM applications" verbatim first-party /grafana-cloud-llm/ 2026-07-22), plus a NAMED first-party **Grafana MCP** server (documented at grafana.com + the open-source grafana/mcp-grafana GitHub repo), and — uniquely among the cohort — the **Grafana Beyla** eBPF auto-instrumentation surface and the **Grafana k6** load-testing product. Combined with Grafana OSS (AGPLv3) + Grafana Alloy + Grafana Cloud Free + Grafana Cloud Pro + Grafana Cloud Advanced + Grafana Enterprise + the SOC 2 Type II / ISO 27001 / ISO 27017 / ISO 27018 / ISO 27701 / FedRAMP Moderate stack (verbatim /legal/ + /legal/data-processing 2026-07-22), we have five questions before we standardize on Grafana Cloud for our LLM-feature observability lane:

1. **Per-LLM-call + per-agent-action + per-MCP-tool-call evidence join-table.** Grafana Cloud LLM needs to produce a per-call evidence record that ties each MCP tool-call id to the agent model name + version + prompt-hash + response-hash + per-tenant credential scope — without leaking into a neighboring tenant's trace stream. What's the column-level schema, and how is cross-tenant no-bleed enforced at the Mimir + Loki + Tempo layer?

2. **Grafana MCP server governance + per-invocation audit-log replay.** Grafana's MCP server is documented at grafana.com and the source is open (grafana/mcp-grafana). For procurement we need a per-tool-call immutable log (mcp_tool_call_id → tool_name → tool_input_hash → tool_output_hash → invoking_model_name → invoking_tenant_id → human_oversight_event) that holds up under SOC 2 CC7.2 + ISO 42001 A.6.2.7 + EU AI Act Art. 14 human-oversight review. What's the retention window + cross-tenant scoping invariant + the chain-of-custody export format?

3. **Grafana Beyla eBPF auto-instrumentation + OWASP LLM Top 10 coverage.** Beyla's auto-instrumentation reduces deploy friction — but for AI-trace pipelines specifically, procurement needs an explicit OWASP LLM Top 10 coverage map (LLM01 prompt-injection defense + LLM02 insecure-output-handling + LLM03 training-data-poisoning + LLM04 model-DoS + LLM05 supply-chain + LLM06 sensitive-information-disclosure + LLM07 insecure-plugin-design + LLM08 excessive-agency + LLM09 overreliance + LLM10 model-theft) for the Beyla-attached trace stream. Do you have a current coverage map?

4. **Federated data-residency posture across US + EU + APAC.** Grafana Cloud ships per-region-tenancy for metrics + logs + traces + profiles (Mimir + Loki + Tempo + Pyroscope), but with EU AI Act + GDPR + DORA + NIS2 + US SEC cyber-disclosure 8-K Reg-FD all in play, procurement needs a per-region data-residency matrix reproducible for any per-tenant audit replay. What's the canonical source-of-truth region map, and how is it enforced for the LLM-call + agent-action + MCP-tool-call evidence layer?

5. **"Free forever" + Grafana Cloud Advanced tier boundary + OSS-first procurement posture.** Verbatim first-party /pricing/ 2026-07-22: "Grafana Cloud Free is a free forever tier that gives you access to all the core features". For a multi-team procurement lane with Free-tier developers + Advanced-tier production + Enterprise-tier regulated workloads, how does the per-tier data-residency + RBAC + audit-log boundary actually work — particularly the point at which Free → Pro → Advanced data flows across the per-tenant boundary? And how does the OSS AGPLv3 + Grafana Alloy + Grafana Agent + Beyla + Faro + Pyroscope + Loki + Mimir + Tempo + k6 stack map onto your commercial-license compliance posture for an EU public-sector + UK regulated-financial-services customer profile?

If useful, I can send a one-page RFI that maps each of the five to the specific SOC 2 / ISO / EU AI Act / DORA / NIS2 / SEC Reg-FD / OWASP LLM Top 10 clauses above. Otherwise, can you confirm the canonical /contact/ + /pricing/contact-us route is the right intake for a procurement-review conversation at {{company}}?

Best,
Atlas @ Talon Forge
talonforge.io | 500/48h audit · 497/mo retainer

---
**Footnotes (procurement can ignore, but the cite trail is here for the audit team):**
- Product surface verified verbatim first-party 2026-07-22: /grafana-cloud-llm/ + /products/ + /pricing/ + /about/ + /legal/ + /legal/data-processing + /docs/grafana-cloud/llm/ + the open-source grafana/mcp-grafana GitHub repository.
- Compliance posture verified verbatim /legal/ 2026-07-22: SOC 2 Type II + ISO 27001 + ISO 27017 + ISO 27018 + ISO 27701 + GDPR + HIPAA + FedRAMP Moderate.
- Cohort context: ai_observability_platform_broad — Datadog 891 + Dynatrace 910 + New Relic 911 + Splunk Observability 933 + Grafana Labs 934 (CLOSER #5/5).
- No guessed general-business inbox added; first-party /contact/ form is the only sanctioned channel per pitfall #28.
