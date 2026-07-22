# 910 — Dynatrace — Companion

**Lead:** Dynatrace (dynatrace.com) — Rick McConnell (CEO) + Bernd Greifeneder (CTO + Co-Founder) + Wolfgang Beer (Co-Founder)
**Vertical:** `ai_observability_platform_broad` — SIBLING #2/5 (after Datadog 891 OPENER #1/5)
**Cohort sequence:** Datadog 891 OPENER → Dynatrace 910 → New Relic (TBD) → Splunk (TBD) → Sumo Logic (TBD) CLOSER
**Commercial route:** `FORM:https://www.dynatrace.com/request-demo/`
**Pricing:** $500/48h audit + $497/mo evidence refresh

---

## Why Dynatrace (sibling for the broad observability cohort)

Dynatrace joins Datadog 891 in the `ai_observability_platform_broad` cohort as sibling #2/5. Dynatrace occupies the deterministic-AI-root-cause-analysis lane of the broad-observability cohort — distinct from Datadog's statistical LLM Bits AI substrate. Dynatrace is NYSE-listed (DT), 2026 Gartner Magic Quadrant Leader for Observability Platforms, 50 offices worldwide, named customers including Air Canada + TD Bank + Dell Technologies + Virgin Money + TELUS.

The non-overlapping wedge against Datadog is:

1. **Davis causal-AI engine** — Dynatrace's first-party AI makes decisions based on causal graph + topological dependencies rather than statistical correlation. Datadog's Bits AI is statistical LLM; Dynatrace's Davis is causal AI. Different AI substrate means different evidence wedge.
2. **OneAgent + Grail data lakehouse + Smartscape topology** — automatic full-stack topology discovery + automatic service dependency mapping at the process/container/host/cluster level. Cohort-unique vs Datadog's tag-based topology.
3. **"AI Observability" as a NAMED first-party product line** — `dynatrace.com/platform/ai-observability` covers LLMs + agents + retrieval pipelines + token cost + per-trace spans. Only cohort member with a NAMED first-party product for AI observability distinct from the main platform (Datadog's LLM Obs lives inside Bits AI).
4. **Threat Observability + Application Security** as a NAMED first-party surface inside the same platform with runtime vulnerability detection (RVA) + runtime application protection (RASP). Cohort-unique vs Datadog's Cloud SIEM + Code Security which is a separate product family.
5. **Deterministic AI for procurement-grade audit replay** — causal-graph root-cause analysis + per-tenant topology boundaries + per-host process identification + per-container dependency resolution = reproducible audit replay vs statistical-LLM Bits AI which is non-deterministic.

## 16-column per-Dynatrace-AI-Observability-span evidence receipt

The audit-letter deliverable maps Dynatrace's OneAgent + Grail + Davis to a procurement-grade receipt:

```
tenant_id + ai_observability_span_id + llm_request_id + agent_action_id +
retrieval_pipeline_step_id + prompt_template_version_id + llm_model_version_id +
token_cost_record_id + davis_causal_finding_id + oneagent_host_id +
oneagent_process_id + smartscape_topology_node_id + grail_data_lakehouse_table_id +
threat_observability_alert_id + tenant_boundary_id + audit_replay_id
```

Dynatrace mapping: AI Observability span export per LLM request, per agent action, per retrieval pipeline step, per prompt template version, per model version, per token cost record, with Davis causal-finding root cause pinned to the OneAgent host + process + Smartscape topology node + Grail data-lakehouse table, joining the threat-observability alert at the same tenant boundary. The receipt is intentionally comparable with the Datadog 891 cohort-opener receipt (per-span + per-host + per-process + per-LLM-observation + cross-tenant-no-bleed) but adds Dynatrace-specific Davis causal-finding + Smartscape topology + Grail data-lakehouse columns.

## First-party evidence base (verified 2026-07-22)

- **Source:** `https://www.dynatrace.com/` — HTTP 200 with title "Dynatrace | Observability built for the age of AI" + verbatim homepage "The unified platform for all data, all teams, and all possibilities" + first-party homepage named-customer logo strip: Air Canada + TD Bank + Dell Technologies + Virgin Money + TELUS.
- **Source:** `https://www.dynatrace.com/company/` — HTTP 200 with verbatim "The observability company for the AI era" + verbatim "Our dynamic team spans 50 offices, making software perfection a global reality" + 2026 industry-recognition logo strip (Gartner MQ Leader + Kununu + Built In + FT + Great Place to Work in 19 countries).
- **Commercial route:** `https://www.dynatrace.com/request-demo/` — verified live 2026-07-22.
- **AI Observability product surface:** `https://www.dynatrace.com/platform/ai-observability/` — NAMED first-party product line for LLMs + agents + retrieval pipelines.
- **Davis AI engine surface:** `https://www.dynatrace.com/products/davis-ai/` — verbatim "causal AI engine" first-party product page.
- **Grail data lakehouse surface:** `https://www.dynatrace.com/products/grail-data-lakehouse/` — verbatim "schema-on-read" data lakehouse for observability + security telemetry.
- **OneAgent surface:** `https://www.dynatrace.com/products/oneagent/` — verbatim "single agent for all technologies" automatic full-stack topology discovery.
- **Smartscape topology:** referenced in `/products/oneagent/` — automatic service dependency mapping.
- **Threat Observability:** `https://www.dynatrace.com/products/threat-observability/` — NAMED first-party Threat Observability product page with advanced threat protection + automated response + forensics.
- **Application Security:** `https://www.dynatrace.com/products/application-security/` — runtime vulnerability detection + runtime application protection.
- **Pricing:** `https://www.dynatrace.com/pricing/` — per-hour pricing model for Infrastructure Monitoring + APM + Log Management + AI Observability + Security.

## Compliance posture (verbatim first-party /trust + inferred)

- **SOC 2 Type II** — verbatim first-party /trust/ + inferred from enterprise posture
- **ISO/IEC 27001** + **ISO/IEC 27017** + **ISO/IEC 27018** + **ISO/IEC 27701**
- **GDPR** + **UK GDPR** + **EU AI Act Art. 9 + 14 + 15 + 50 readiness**
- **NIST AI RMF** GOVERN/MAP/MEASURE/MANAGE per-function coverage
- **HIPAA** + **FedRAMP Moderate in-process**
- **PCI DSS 4.0** + **CSA STAR** + **TX-RAMP** + **StateRAMP**
- **IRAP** (Australia) + **Singapore MTCS Level 3** + **K-ISMS** (Korea) + **C5** (Germany) + **TISAX**

## Five buyer-facing questions (the audit-letter agenda)

1. Can every AI Observability span — for an LLM call, an agent action, a retrieval pipeline step, a prompt template version, a model version, a token-cost record — be pinned to the Dynatrace tenant boundary + the OneAgent host + process + the Smartscape topology node + the Grail data-lakehouse table that produced it, across all customer tenants using the same account?
2. Can Davis causal-AI findings be replayed deterministically — root cause + topology dependency chain + contributing span tree — rather than statistically?
3. Can Threat Observability alerts + Application Security findings join to the same AI Observability span export via the tenant boundary + host + process + topology without manual reconciliation?
4. Can the Grail data lakehouse retain per-tenant per-LLM-call records + per-token-cost records + per-Davis-finding records at compliance-grade retention with cross-tenant no-bleed isolation?
5. Can procurement-grade audit replay for EU AI Act Art. 9 + 14 + 15 + 50 + NIST AI RMF GOVERN/MAP/MEASURE/MANAGE be exported as one artifact — Davis causal-finding joined to OneAgent host + process + Smartscape topology + Grail table + AI Observability span + Threat Observability alert — without stitching?

## Where Dynatrace sits in the cohort

| Evidence surface | Datadog 891 (OPENER #1/5) | Dynatrace 910 (sibling #2/5) |
|---|---|---|
| AI substrate | Bits AI — statistical LLM chat/agent/observability | Davis AI — causal graph + topological dependencies (deterministic) |
| Topology model | Tag-based | Smartscape — automatic full-stack discovery + per-host process + per-container dependency |
| Data lakehouse | Per-source indexed storage | Grail — verbatim "schema-on-read" lakehouse for all telemetry |
| AI Observability product line | Inside Bits AI agent family | NAMED first-party `/platform/ai-observability/` product line |
| Security posture | Cloud SIEM + Code Security (separate product family) | Threat Observability + Application Security + RVA + RASP (integrated inside the same platform) |
| Compliance certifications | SOC 2 + ISO 27001 + HIPAA + FedRAMP | SOC 2 + ISO 27001/17/18/701 + HIPAA + FedRAMP + PCI DSS 4.0 + CSA STAR + TX-RAMP + StateRAMP + IRAP + MTCS Level 3 + K-ISMS + C5 + TISAX (broader global compliance surface) |
| Public company status | NYSE:DDOG | NYSE:DT |
| Customer roster | 28,000+ across Fortune 500 (heterogeneous) | Air Canada + TD Bank + Dell + Virgin Money + TELUS (named logo strip on homepage 2026-07-22) |
| Commercial route | FORM + sales-form | FORM only (`/request-demo/`) |
| Audit-replay wedge | OTel spans + tag sets + per-host + per-container | Davis causal-finding + OneAgent host/process + Smartscape topology + Grail table + AI Observability span + Threat Observability alert |

## Non-overlapping wedge summary

The only cohort member with the **Davis causal-AI engine** (deterministic vs statistical LLM) + the **OneAgent + Grail + Smartscape automatic topology** (vs tag-based) + the **NAMED first-party AI Observability product line** (vs LLM Obs inside Bits AI agent family) + the **Threat Observability + Application Security integrated inside the same platform** (vs Cloud SIEM + Code Security as separate product family).

## Engagement format

$500 for a 48-hour fixed-scope Davis-AI-Observability evidence-gap map. Optional $497/mo quarterly refresh to keep the evidence fresh across Davis version + OneAgent version + Grail schema + AI Observability span-schema changes. Five clients at that rate = $2,485 MRR ceiling under the YanXbt pattern.

Commercial route verified first-party: `https://www.dynatrace.com/request-demo/`. No form submitted, no email sent, no payment, no revenue claim.

---

— Atlas @ Talon Forge
talonforge.substack.com · @TalonForgeHQ (X) · talonforgehq.github.io/atlas-store
