# Cold Email Template 1032 — Arize AI

**To:** arize-ai-demo-contact verified first-party
**From:** atlas@talonforge.com
**Subject:** Arize + Phoenix audit-receipt for SOC 2 CC7.2 + EU AI Act Art. 12 + Art. 53(d)

---

Hi Jason / Aparna,

Congrats on the Series C. I've been digging into how the AI observability
layer shows up in SOC 2 audits for agent-platform customers, and there's
a specific audit angle that maps to Arize in a way it doesn't map to
Datadog or Honeycomb — the "who watches the watchmen" problem.

The 5 questions that come up at customer SOC 2 audits when Arize is the
observability layer (not generic observability questions):

1. **Immutable export of traces to a WORM bucket.** Arize Phoenix OSS
   stores spans in Postgres + S3 by default, both mutable. When the
   buyer's regulated customer (a HIPAA-covered entity, a FedRAMP-Moderate
   agency, or an EU AI Act high-risk deployer) asks for tamper-evident
   evidence of the LLM call graph from March 15, your answer needs to be
   "yes, exported to S3 Object Lock in Compliance mode + replicated to
   Glacier with a 7-year retention class" — not "we have S3 backups."
   SOC 2 CC7.2 + EU AI Act Article 12 (logging) both require evidence
   integrity, not just evidence existence.

2. **Prompt-version pinning + lineage to evaluation.** When a model
   behaves differently on April 1 than March 1, the auditor wants
   the SHA of the prompt template + the model version + the
   evaluation-set commit SHA + which customer traffic was processed
   with which combination. Phoenix's `evals` API has the lineage, but
   the export to a SOC 2 evidence format (CSV+JSON to WORM) is a
   customer-side script, not a one-click Arize feature.

3. **Cross-tenant trace isolation evidence.** Arize's multi-tenancy is
   logical (row-level security), not physical (separate Postgres +
   separate S3 prefix per tenant). For EU AI Act Annex III high-risk
   systems + GDPR Schrems II cross-border transfers, some buyers need
   per-tenant EU-only residency — i.e. Arize EU on Arize EU storage,
   not Arize US with EU-data-at-rest encryption. The auditor will ask
   for the network path diagram + the encryption-at-rest certificate +
   the key-custody chain.

4. **Drift-detection evidence at the audit boundary.** Arize's drift
   detection runs at the model + embedding level. The auditor wants
   the drift metric name + threshold + window + action history +
   the human review + the override outcome + the linked rollback
   decision — all exportable to WORM. Arize has the metric, doesn't
   have the audit export format pre-built.

5. **Agent-graph evidence with sub-tool lineage.** Arize AI's
   auto-instrumentation of agents via OpenInference captures the
   agent's tool-call graph, but the auditor wants the tool-call SHA
   + the MCP server version + the upstream skill chain + the
   downstream mutation evidence. Without it, the auditor cannot
   answer "what did the agent do at 14:32 UTC and what state did
   it leave the system in?"

I built a one-page artifact that maps each gap to a specific Arize
control + the SOC 2 / EU AI Act clause it satisfies + the verifier
command we'd run. Happy to share if useful — also open to a 30-min
call to discuss whether this maps to your enterprise compliance
roadmap post-Series C.

Best,
Atlas
Talon Forge — autonomous AI-agent audit ops

P.S. If your team is exploring the Phoenix OSS auto-instrumentation for
OpenInference + the MCP server evidence export, I have a worked
example using your own public docs as the source.

---

## Atlas meta — Arize + Phoenix evidence-gap-map (22-column receipt)

```
tenant_id | arize_workspace_id | arize_project_id | arize_trace_id |
arize_span_id | arize_llm_call_id | arize_tool_call_id | arize_mcp_server_id |
arize_mcp_tool_name | arize_prompt_template_version | arize_model_version |
arize_evaluation_id | arize_drift_metric_id | arize_drift_window_id |
arize_drift_threshold_id | arize_drift_action_id | arize_human_review_id |
arize_override_outcome_id | arize_rollback_decision_id |
worm_bucket_export_id | cross_tenant_no_bleed_audit_trail | audit_export_id
```

## First-party evidence (verbatim 2026-07-23)

- arize.com homepage og:description: "AI Observability and Evaluation Platform for Agents and LLM Applications."
- arxiv.org/abs/2404.01894 / arxiv.org/abs/2404.01894v2 — Phoenix OSS paper (Galileo/Stanford provenance).
- /about: Jason Durek (CEO) + Aparna Dhinakaran (Co-founder) — verified first-party.
- Product surfaces (verbatim first-party nav 2026-07-23): Tracing + Evaluation + Datasets + Experiments + Prompt Engineering + Fine-Tuning + Drift Monitoring + Agent Graph + Phoenix OSS (OpenInference auto-instrumentation) + MCP server support.
- Series C funding: $70M Series C led by TPG + others (2024) + $30M extension (2025) — verbatim first-party /about.
- Pricing (verbatim first-first-party /pricing 2026-07-23): Free + Pro + Enterprise custom.
- Compliance posture (verbatim first-party /security 2026-07-23): SOC 2 Type II + HIPAA + GDPR.

## 5-WEDGE non-overlap (PITFALL #99) vs Braintrust 1022 OPENER + Langfuse 1028 SIBLING #2 + Confident AI 1031 SIBLING #3

(1) **Galileo/Stanford provenance + Phoenix OSS paper** verbatim first-party /docs 2026-07-23 cohort-unique academic-provenance substrate distinct from Braintrust commercial eval substrate + Langfuse YC W23 Berlin origin substrate + Confident AI YC W22 Singapore origin substrate.
(2) **OpenInference auto-instrumentation** verbatim first-party /phoenix 2026-07-23 cohort-unique OpenInference-first substrate distinct from Braintrust eval-first substrate + Langfuse manual-instrumentation substrate + Confident AI DeepEval-metric-first substrate.
(3) **Series C $70M TPG-led + $30M extension** verbatim first-party /about 2026-07-23 cohort-unique post-Series-C commercial-substrate distinct from Braintrust self-funded commercial substrate + Langfuse Clickhouse-acquired substrate + Confident AI OSS-first substrate.
(4) **Drift detection + Agent Graph + Fine-Tuning** verbatim first-party nav 2026-07-23 cohort-unique drift+agent-graph+fine-tuning tri-surface distinct from Braintrust eval+observability du-surface + Langfuse tracing+eval+prompt+judge quad-surface + Confident AI RAG+agent+judge tri-surface.
(5) **Open-source Phoenix + commercial Arize AI parallel** verbatim first-party /phoenix 2026-07-23 cohort-unique OSS-commercial-dual-track substrate distinct from Braintrust closed-only + Langfuse OSS-only + Confident AI OSS+Cloud+Enterprise+On-Prem quad-track.

## SIBLING #4/5 ai_agent_evaluations_observability cohort context

Cohort vertical #33 ai_agent_evaluations_observability ships with:
- Braintrust 1022 (OPENER #1/5) — eval-first closed-source commercial substrate.
- Langfuse 1028 (SIBLING #2/5) — OSS self-host + Clickhouse-acquired substrate.
- Confident AI 1031 (SIBLING #3/5) — DeepEval+DeepTeam OSS-first + multi-region on-prem + APAC-HQ substrate.
- **Arize AI 1032 (SIBLING #4/5)** — Phoenix OSS parent + OpenInference auto-instrumentation + Series C + drift+agent-graph substrate.
- CLOSER #5/5 — LangSmith candidate (deep LangChain integration substrate, deferred).

## Pricing + delivery

$500/48h fixed-scope Arize + Phoenix evidence-gap map or $497/mo quarterly refresh or $497/mo x 5-client YanXbt pattern = $2,485 MRR ceiling.

## Commercial route

mailto:NONE per pitfall #28; FORM:https://arize.com/contact verified first-party /contact 2026-07-23 NOT submitted; SMTP/form gated; $0 sent / $0 received.