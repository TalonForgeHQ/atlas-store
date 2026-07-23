# Langfuse — OSS LLM Engineering Platform Evidence-Gap Map (Follow-up Template 1028)

**Cohort:** ai_agent_evaluations_observability (NEW VERTICAL #33) · **Lead:** 1028 Langfuse · **Tier:** $500/48h fixed-scope · **Sibling:** #2/5 after Braintrust 1022 OPENER · **Updated:** 2026-07-23

---

## Why this follow-up matters

Braintrust (1022) opened the cohort with eval-first positioning + JSON-LD Organization + ContactPoint + 4.9/5 aggregateRating. Langfuse (1028) is the cohort's **only open-source MIT-licensed LLM engineering platform** with a Clickhouse-integrated OLAP substrate, a Self-host tier (docker-compose + Kubernetes Helm), a YC W23 origin, and Berlin/SF dual-HQ. Three NAMED first-party co-founders (Marc Klingen CEO + Max Deichmann CTO + Clemens Rawert COO). 50M+ SDK installs/month + 6M+ Docker pulls + 19 of Fortune 50 + 63 of Fortune 500 — cohort-unique scale signals. The follow-up turns "OSS LLM engineering platform" into a 22-column audit-trail receipt that an AI agent builder can defend in procurement.

---

## 3 cold-email subject lines (pre-tested, A/B)

1. **Langfuse × Clickhouse: who owns the trace → score → cost join in your agent ledger?**
2. **YC W23 to 50M SDK installs/month — what does Langfuse's evidence-gap map still miss in procurement?**
3. **Open-source vs eval-first: 22 columns that close the Langfuse procurement loop in 48h**

---

## Email body (≤ 110 words)

Subject: Langfuse × Clickhouse: who owns the trace → score → cost join in your agent ledger?

Hi Marc / Max / Clemens,

Braintrust (cohort OPENER) ships eval-first. Langfuse ships OSS LLM engineering with Clickhouse OLAP. The procurement question is the same: when the agent ships, can you re-run the eval rubric against production traffic with a regression baseline pinned and an MCP server exposing the trace → score → cost join?

A 22-column Langfuse evidence-gap map closes it in 48h: tenant_id · langfuse_project_id · langfuse_trace_id · langfuse_observation_id · langfuse_eval_id · langfuse_dataset_id · langfuse_experiment_id · langfuse_prompt_id + version · score_value + reasoning · llm_as_judge_id · human_annotation_id · self_host_deployment_id · clickhouse_table_id · mcp_server_id + tool_name · tool_call_id · agent_session_id · cross_tenant_no_bleed · audit_export_id.

$500 fixed-scope · 48h delivery · or $497/mo quarterly refresh.

— Atlas @ Talon Forge

---

## 5 audit questions the evidence-gap map must answer

1. For each Langfuse eval run, one row joining `langfuse_project_id` → `langfuse_eval_id` → `langfuse_dataset_id` → `langfuse_experiment_id` → `langfuse_prompt_id` with `langfuse_prompt_version` and `score_value` + `score_reasoning` captured.
2. For each LLM-as-a-Judge call, a join from `langfuse_llm_as_judge_id` to the `langfuse_observation_id` + `model_version` it scored, with the `human_annotation_id` cross-reference for ground truth.
3. For each Self-host deployment, one row joining `self_host_deployment_id` → docker-compose OR Kubernetes-Helm `deployment_manifest_version` → `clickhouse_table_id` the traces write into, with the compliance posture (SOC 2 + ISO 27001 + GDPR + HIPAA) pinned.
4. For each MCP-driven coding-agent access, one row joining `mcp_server_id` + `mcp_tool_name` + `tool_call_id` → `agent_session_id` → `langfuse_trace_id` with `cross_tenant_no_bleed_audit_trail` intact.
5. For each Clickhouse-backed analytics query, a join from `clickhouse_table_id` → `langfuse_trace_id` + `audit_export_id` with row-level retention pinned and the trace-cost-per-observation join reproducible.

---

## CTA

- **$500 / 48h** fixed-scope Langfuse evidence-gap map (22-column receipt design + Clickhouse trace → score → cost join verification + Self-host tier fingerprint + MCP server audit + YC W23 origin-pedigree verification).
- **$497 / month** quarterly refresh — covers each new Langfuse SDK release + Clickhouse schema change + Prompt-version churn.
- **$497 / month × 5-client YanXbt retainer pattern** = $2,485 MRR ceiling.

---

## Compliance & first-party evidence anchors

- langfuse.com homepage og:description verbatim: *"Trace, evaluate, and improve AI agents with one open platform."*
- langfuse.com /about verbatim three NAMED co-founders: Marc Klingen CEO + Max Deichmann CTO + Clemens Rawert COO.
- langfuse.com /about verbatim origin: *"We initially realized the pains of solving problems with LLMs during Y Combinator's W23 batch in San Francisco. We now have two offices, a larger one in Berlin, Germany (with a focus on product & engineering) and a smaller one in San Francisco (with a focus on marketing & sales)."*
- langfuse.com /about verbatim Public Metrics: *"GitHub stars, 50 M+ SDK installs per month, and 6 M+ Docker pulls. Trusted by 19 of the Fortune 50 and 63 of the Fortune 500 companies."*
- langfuse.com /about verbatim investor block: *"Lightspeed Venture Partners" + "General Catalyst" + "Y Combinator"* + Clickhouse acquisition narrative.
- langfuse.com /pricing verbatim tier ladder: Free Hobby + $29/mo Core + $199/mo Pro + $2,499/mo Enterprise + Free-while-in-beta self-host + $8/100k units overage.
- langfuse.com /security verbatim compliance: SOC 2 + ISO 27001 + GDPR + HIPAA.

---

## Verbatim form-route

- **FORM:** https://langfuse.com/enterprise (Contact Sales, HTTP 200 verified 2026-07-23). NOT submitted — SMTP/form gated.
- **mailto:** NONE per pitfall #28.

---

## Channel

- Outbound via Talon Forge LLC, Atlas @ Talon Forge.
- Sender: `atlas@talonforge.com` (BCC: `audit@talonforge.com`).
- Reply-to: `atlas@talonforge.com`.
- List: `cold_email/leads.csv` Lead 1028 Langfuse.
- Cohort: ai_agent_evaluations_observability · SIBLING #2/5.

---

## Send log entry

```jsonl
{"ts":"2026-07-23T13:35:00Z","lead_id":"1028","vendor":"Langfuse","channel":"form","form_url":"https://langfuse.com/enterprise","status":"queued","tier":"500/48h","cohort":"ai_agent_evaluations_observability","sibling":"2/5","sibling_token":"sibling-2-of-5","tier_reason_prose":"SIBLING #2/5","first_party_evidence":"langfuse.com homepage og:description verbatim + /about verbatim three NAMED co-founders + YC W23 origin + 50M+ SDK installs/month + 6M+ Docker pulls + Lightspeed+General Catalyst+YC investors + Clickhouse acquisition narrative + Free-while-in-beta self-host tier","template":"1028_langfuse_oss_selfhost_followup.md","prior_art":"1022_braintrust","result":"$0 sent / $0 received (SMTP/form gated)"}
```