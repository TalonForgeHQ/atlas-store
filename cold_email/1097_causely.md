# Lead 1097 — Causely (SIBLING #4/5 ai_agent_operations) — causal-model-to-remediation evidence-gap map

**Vertical:** ai_agent_operations SIBLING #4/5 after Resolve AI 1094 OPENER + incident.io 1095 SIBLING #2 + Rootly 1096 SIBLING #3

**First-party evidence retrieved 2026-07-23:**
- `causely.ai/` — title: “Causely: Causal Intelligence for AI Agents”; description says Causely gives AI agents a live causal model so they can identify root cause, assess blast radius, and resolve incidents without human intervention.
- `causely.ai/company` — founder Shmuel Kliger, Ph.D.; co-founders Christine Miller, Endre Sara, Ph.D., and Enlin Xu; CEO Yotam Yemini. The page says Causely was incorporated in 2022 after the founding team’s Turbonomic/IBM experience.
- `causely.ai/security` — no sensitive data or PII is stored or processed; symptom data is encrypted in transit and at rest; SOC 2 compliance; hybrid mediation layer plus on-premise/air-gapped deployment.
- `causely.ai/pricing` — free 30-day trial; Professional Edition $2,000/month; Enterprise custom plans including on-prem and air-gapped requirements.
- `causely.ai/demo` — first-party demo form with work-email field; no form submitted.

## 5-WEDGE non-overlap rubric

1. **Live causal model as the primary substrate.** Causely starts from a continuously updated causal model and topology snapshot, unlike Resolve AI’s Kubernetes investigate-run, incident.io’s schedule/page chain, or Rootly’s Slack workflow.
2. **Deterministic causal inference.** The evidence row preserves causal graph edges and root-cause confidence rather than relying only on an LLM narrative.
3. **Root-cause + blast-radius pair.** Causely explicitly joins a root-cause decision to a blast-radius assessment before remediation.
4. **Prevention after remediation.** The receipt ends with a prevention-policy/version record, extending the replay from incident response into recurrence prevention.
5. **Hybrid, on-prem, and air-gapped control plane.** Local mediation keeps sensitive data within the customer environment; the security page states no sensitive data or PII is stored or processed.

## 20-column per-Causely receipt

`tenant_id + causely_workspace_id + incident_id + topology_snapshot_id + causal_model_version + symptom_id + anomaly_id + service_id + causal_graph_edge_set_hash + root_cause_id + root_cause_confidence + blast_radius_assessment_id + remediation_action_id + remediation_execution_id + prevention_policy_id + human_override_id + deployment_mode + token_spend_usd + latency_ms + audit_export_id`

**Commercial route:** `FORM:https://www.causely.ai/demo` — verified first-party demo page with work-email field; not submitted.

**Offer:** $500/48h fixed-scope causal-model-to-remediation evidence-gap map OR $497/mo quarterly refresh OR $2,000 five-vendor ai_agent_operations benchmark.

**Verification:** mailto:NONE; SMTP/form gated; `$0 sent / $0 received`.
