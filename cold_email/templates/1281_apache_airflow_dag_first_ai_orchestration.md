# Apache Airflow — DAG-First AI Data Pipeline Orchestration — Evidence-Gap Map

**Tick:** 1281
**Cohort:** NEW VERTICAL #70 ai_agent_data_pipeline (SIBLING #4/5)
**Vendor:** Apache Airflow (airflow.apache.org + astronomer.io commercial layer)
**Date:** 2026-07-25

## Subject

Airflow evidence-gap map for SOC 2 + HIPAA + EU AI Act audit readiness — 48h fixed-scope

## Body

Hi Astronomer / Apache Airflow team,

I reviewed the first-party airflow.apache.org surfaces (DAG-first orchestration, Apache-2.0 OSS, CNCF Incubator 2019, KubernetesExecutor, 350+ providers) and the Astronomer Trust Center (SOC 2 Type II for Astro). I'm putting together a cohort comparison for ai_agent_data_pipeline — Dagster + Mage.ai + Prefect + Airflow + a CLOSER.

For Airflow specifically, an enterprise buyer evaluating the substrate for AI-pipeline authoring (Bedrock / Vertex AI / Azure OpenAI operators) wants to see evidence on:

1. **Pod-per-task isolation** — KubernetesExecutor tenant boundaries, per-pod IAM, sidecar injection, namespace-level RBAC.
2. **LLM-call DAG replay** — per-task-instance XCom + log + Bedrock invocation + Vertex AI endpoint + Azure OpenAI deployment audit trail.
3. **Cross-tenant no-bleed invariant** — Astronomer Astro deployment-level isolation, per-deployment RBAC, SCIM provisioning logs.
4. **EU AI Act Art. 13 logging** — log retention, deletion, residency, automated per-task-instance export.
5. **ISO/IEC 42001 AIMS clause 8.4 evidence** — Airflow + Astronomer provider-level AI management system coverage.

I can deliver a 48h fixed-scope Airflow evidence-gap map (per-DAG + per-task-instance + per-Kubernetes-Pod + per-Bedrock-prompt + per-Astronomer-deployment + per-XCom + per-pool + per-SLA-miss + cross-tenant RBAC + EU AI Act Art. 13 logging + ISO/IEC 42001 AIMS clause 8.4 evidence) for $500, with $497/mo quarterly refresh and a $2,000 five-vendor ai_agent_data_pipeline cohort benchmark at close (Dagster + Mage.ai + Prefect + Airflow + CLOSER).

If this lands, please send the canonical sales inbox at the Astronomer contact form or share the right route.

Thanks,
Atlas
TalonForgeHQ

## Route

- Primary: FORM:https://www.astronomer.io/contact (canonical first-party sales widget, verified 2026-07-25)
- Backup: mailto:hello@astronomer.io (pattern guess, retained separately per PITFALL #28)
- Direct: Maxime Beauchemin Creator Direct LinkedIn (verified first-party airflow.apache.org/community 2026-07-25)
- SMTP/form gated; $0 sent / $0 received
- Pattern-guess mailto:security@astronomer.io NOT promoted (security disclosure lane)

— Atlas @ TalonForgeHQ
[tick-1281-apache-airflow-dag-first-ai-orchestration]
