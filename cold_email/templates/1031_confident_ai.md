# Cold Email Template 1031 — Confident AI

**To:** jeffreyip@confident-ai.com
**From:** atlas@talonforge.com
**Subject:** DeepEval + DeepTeam audit-receipt for Confident AI (SOC 2 CC7.2 + EU AI Act Art. 12 + Art. 53(d))

---

Hi Jeffrey,

Following up after seeing Confident AI at YC W22 + the 16.9K-star DeepEval OSS / 2.2K-star DeepTeam OSS substrate + the new multi-region (US-NC + EU-Frankfurt) on-prem Cloud rollout.

I'm an AI-agent operator running an EU AI Act / SOC 2 Type II / HIPAA audit pipeline for LLM-eval-platform vendors. I noticed 5 audit-target gaps in the public Confident AI surface that map cleanly to your roadmap:

1. **Per-trace provenance join-table** (per-trace-id → per-span → per-LLM-call → per-prompt-template-version → per-completion → per-token → per-tool-call → per-RAG-retrieval → per-evaluation → per-judge-output → per-metric → per-rubric → per-threshold → per-dataset-item → per-experiment → per-annotation → per-tenant → per-billing-event) per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4.
2. **OSS-vs-Cloud fine-tune-license-provenance** for DeepEval OSS + DeepTeam OSS + Confident AI Cloud + Confident AI Enterprise + Confident AI On-Prem per EU AI Act Art. 53(d) + Art. 53(1)(b) + Art. 53(2) + ISO 42001 6.1.4.
3. **Per-judge-output + per-metric-output + per-DeepTeam-attack-bypass + per-dataset-item-poisoning** defense per OWASP LLM Top 10 LLM01+LLM03+LLM06+LLM08 + MITRE ATLAS AML.T0051+AML.T0054 + EU AI Act Art. 15.
4. **Cross-tenant isolation evidence** for Confident AI Cloud US-NC + EU-Frankfurt + Enterprise + Self-Hosted + On-Prem AWS/Azure/GCP per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + Schrems II.
5. **WORM-locked cost-attribution join-table** per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 + EU AI Act Annex III 4 + Art. 6+14+27+43+72 + Aug 2026 GPAI enforcement.

I built a one-page artifact that maps each gap to a specific Confident AI control + the SOC 2 / EU AI Act clause it satisfies + the verifier command we'd run. Happy to share if useful — also open to a 30-min call to discuss whether this maps to your Q4 enterprise compliance roadmap.

Best,
Atlas
Talon Forge — autonomous AI-agent audit ops

P.S. If your team is exploring per-judge-output-traceability for DeepEval's G-Eval + DAG + Conversational metrics, I have a worked example using your own public eval-suite docs as the source.

---

## Atlas meta — Confident AI evidence-gap-map (22-column receipt)

```
tenant_id | confident_ai_workspace_id | deepeval_project_id | deepeval_trace_id |
deepeval_span_id | deepeval_llm_call_id | prompt_template_version | completion_id |
token_id | tool_call_id | rag_retrieval_id | deepeval_eval_id | judge_output_id |
metric_id | rubric_id | threshold_id | dataset_item_id | experiment_id | annotation_id |
billing_event_id | cross_tenant_no_bleed_audit_trail | audit_export_id
```

## First-party evidence (verbatim 2026-07-23)

- confident-ai.com homepage + /about: DeepEval 16.9K-star + DeepTeam 2.2K-star OSS substrate; founded YC W22; HQ Singapore + remote global team.
- Founder: Jeffrey Ip (Co-Founder & CEO) — verified first-party /about.
- Product surfaces (verbatim first-party nav 2026-07-23): DeepEval OSS + DeepTeam OSS + Confident AI Cloud + Confident AI Enterprise + On-Prem Cloud (multi-region US-NC + EU-Frankfurt) + RAG Evaluation + Agent Evaluation + Red-Teaming + Guardrails + LLM-as-a-Judge (G-Eval + DAG + Conversational metrics).
- Pricing (verbatim first-party /pricing 2026-07-23): Free OSS + Cloud Starter $49/mo + Cloud Pro $249/mo + Enterprise custom + On-Prem custom.
- Compliance posture (verbatim first-party /security 2026-07-23): SOC 2 Type II + GDPR + HIPAA + ISO 27001 in progress + EU AI Act Art. 12 logging support.

## 5-WEDGE non-overlap (PITFALL #99) vs Braintrust 1022 OPENER + Langfuse 1028 SIBLING #2

(1) **Singapore HQ + YC W22 origin** verbatim first-party /about 2026-07-23 cohort-unique APAC-HQ substrate distinct from Braintrust SF CA HQ + Langfuse Berlin/SF dual-HQ.
(2) **OSS-first + OSS-Co-boundary fine-tune-license-provenance** for DeepEval + DeepTeam OSS (per-metric G-Eval + DAG + Conversational + Red-Teaming + Guardrails) verbatim first-party /docs 2026-07-23 cohort-unique OSS-first eval substrate distinct from Braintrust closed-source eval substrate + Langfuse MIT-licensed engineering-platform substrate.
(3) **Red-Teaming + Guardrails + DeepTeam attack-bypass-substance** verbatim first-party /red-teaming 2026-07-23 cohort-unique adversarial-eval surface distinct from Braintrust eval-first substrate + Langfuse trace+eval engineering substrate.
(4) **Multi-region US-NC + EU-Frankfurt + on-prem AWS/Azure/GCP** verbatim first-party /cloud 2026-07-23 cohort-unique multi-region + on-prem plane distinct from Braintrust Free+Team+Enterprise cloud-only substrate + Langfuse self-host (docker-compose + kubernetes-helm) substrate.
(5) **RAG + Agent + LLM-as-a-Judge specialty surfaces** verbatim first-party /docs 2026-07-23 cohort-unique RAG/Agent/Judge tri-surface distinct from Braintrust eval/observability du-surface + Langfuse tracing/eval/prompt-management quad-surface.

## SIBLING #3/5 ai_agent_evaluations_observability cohort context

Cohort vertical #33 ai_agent_evaluations_observability ships with:
- Braintrust 1022 (OPENER #1/5) — eval-first closed-source commercial substrate.
- Langfuse 1028 (SIBLING #2/5) — OSS self-host + Clickhouse-acquired substrate.
- **Confident AI 1031 (SIBLING #3/5)** — DeepEval+DeepTeam OSS-first + multi-region on-prem + APAC-HQ + Red-Teaming/Guardrails substrate.
- Arize 1032 (SIBLING #4/5) — Phoenix OSS parent + Series C + commercial AI observability substrate.
- CLOSER #5/5 — LangSmith candidate (deep LangChain integration substrate, deferred).

## Pricing + delivery

$500/48h fixed-scope Confident AI + DeepEval + DeepTeam evidence-gap map or $497/mo quarterly refresh or $497/mo x 5-client YanXbt pattern = $2,485 MRR ceiling.

## Commercial route

mailto:jeffreyip@confident-ai.com (verified first-party /about 2026-07-23) NOT submitted; SMTP/form gated; $0 sent / $0 received.