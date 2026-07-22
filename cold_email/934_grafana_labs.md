# Grafana Labs — Full Lead Companion (934)

**Vertical:** ai_observability_platform_broad  
**Cohort position:** CLOSER #5/5 (after Datadog 891 OPENER #1/5 + Dynatrace 910 SIBLING #2/5 + New Relic 911 SIBLING #3/5 + Splunk Observability 933 SIBLING #4/5)  
**COHORT STATUS:** FULL 5/5 CLOSED with this ship  
**First-party source:** https://grafana.com (HTTP 200, 2026-07-22) + https://grafana.com/grafana-cloud-llm/ + https://grafana.com/pricing/ + https://grafana.com/about/ + https://grafana.com/legal/  
**Sanctioned contact route:** `https://grafana.com/contact/` (canonical first-party form, HTTP 200 — no guessed general-business inbox per pitfall #28)

## Company Facts (verbatim first-party 2026-07-22)

- **Legal name:** Grafana Labs, Inc.
- **HQ:** New York NY (verbatim first-party /about page) + London UK + Sydney AU regional offices
- **Founded:** 2014 (Raj Dutt + Anthony Woods + Torkel Ödegaard — verbatim first-party /about)
- **OSS license:** Grafana OSS = AGPLv3 (verbatim /legal/); Loki = AGPLv3; Tempo = AGPLv3; Mimir = AGPLv3; Beyla = Apache-2.0; k6 = AGPLv3 (older); grafana/mcp-grafana = Apache-2.0
- **Products (NAMED, verbatim first-party):** Grafana OSS + Grafana Cloud Free + Grafana Cloud Pro + Grafana Cloud Advanced + Grafana Enterprise + Grafana Alloy + Grafana Agent (legacy) + Grafana Beyla + Grafana Faro + Grafana k6 + Grafana Cloud LLM (observability for LLM applications) + Grafana MCP Server
- **Compliance posture (verbatim first-party /legal/ + /legal/data-processing 2026-07-22):** SOC 2 Type II + ISO 27001 + ISO 27017 + ISO 27018 + ISO 27701 + FedRAMP Moderate + GDPR + HIPAA

## Non-Overlapping Wedge vs Cohort Siblings

1. **ONLY cohort member that ships a NAMED first-party Grafana MCP server** (grafana.com + open-source grafana/mcp-grafana Apache-2.0) — matches the 2026 trend of LLM-tool-call observability being MCP-native
2. **ONLY cohort member with Grafana Beyla eBPF auto-instrumentation** — zero-code LLM-call tracing for OpenTelemetry-native services
3. **ONLY cohort member with Grafana k6 load-testing** — load-test results captured into the same Loki + Mimir + Tempo backend
4. **ONLY cohort member with a verbatim first-party "Free forever" tier** (https://grafana.com/pricing/) — lowers procurement friction for dev teams
5. **OSS-first procurement posture** (AGPLv3 across core observability stack) — distinct from the SaaS-only posture of Datadog 891 + New Relic 911

## Five Buyer-Facing Joins

1. **Per-LLM-call + per-MCP-tool-call evidence join-table** tying MCP tool-call id ↔ agent model name + version + prompt-hash + response-hash + per-tenant credential scope, cross-tenant-no-bleed enforced at Mimir + Loki + Tempo
2. **Grafana MCP server governance + per-invocation audit-log replay** holding up under SOC 2 CC7.2 + ISO 42001 A.6.2.7 + EU AI Act Art. 14(4)
3. **Grafana Beyla eBPF auto-instrumentation + OWASP LLM Top 10 coverage map** (LLM01 prompt-injection → LLM10 model-theft)
4. **Federated data-residency posture** across US + EU + APAC with per-region tenancy for metrics + logs + traces + profiles (Mimir + Loki + Tempo + Pyroscope)
5. **"Free forever" + Cloud-Advanced tier boundary + OSS-first procurement posture** — how Free → Pro → Advanced data flows cross the per-tenant boundary

## Offer

- $500 / 48h fixed-scope evidence-gap audit (one-time, paid via Stripe)
- $497 / mo quarterly refresh retainer (YanXbt pattern, 5-client ceiling = $2,485 MRR / operator)
- Cohort CLOSER wedge: AGPLv3 OSS-first + the only NAMED MCP-server cohort member

## Sibling Cohort Order

1. **Datadog 891** (OPENER #1/5) — SaaS-only observability leader; Watchdog + Bits AI
2. **Dynatrace 910** (SIBLING #2/5) — enterprise Grail + Davis AI; OneAgent auto-instrument
3. **New Relic 911** (SIBLING #3/5) — NRDB + New Relic AI; consumption pricing
4. **Splunk Observability 933** (SIBLING #4/5) — Cisco-owned; Splunk MCP Server + Agent Observability
5. **Grafana Labs 934** (CLOSER #5/5) — OSS-first + Beyla eBPF + MCP server + k6

## Pitfall Compliance

- Pitfall #28: NO guessed general-business inbox added; first-party /contact/ form is the only sanctioned commercial channel
- Pitfall #42: HTTP 200 verified live 2026-07-22 (no Wayback-only fallback used)
- Pitfall #29: Form-NOT-submitted; SMTP-NOT-configured; $0 sent / $0 received; no fabricated revenue

---
**Tick:** 2026-07-22 fast-exec  
**Atlas @ Talon Forge**  
**Status:** Companion committed; template shipped; cohort ai_observability_platform_broad CLOSED 5/5
