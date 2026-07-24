# Argo Workflows — Kubernetes-native workflow engine (CLOSER #5/5)

**Vertical:** ai_workflow_orchestration
**Cohort slot:** CLOSER #5/5 after Kestra 1161 (OPENER #1/5) + Temporal 1165 (SIBLING #2/5) + Windmill 1168 (SIBLING #3/5) + Prefect 1169 (SIBLING #4/5); cohort now CLOSED 5/5
**First-party route:** FORM:https://github.com/argoproj/argo-workflows/issues/new/choose + mailto:cncf-argo-workflows-maintainers@lists.cncf.io
**Offer:** $500 / 48h fixed-scope audit · $497/mo refresh · $2,000 five-vendor cohort benchmark · $2,485 MRR ceiling

## Subject options

1. A 20-column receipt for Argo WorkflowTemplate + CronWorkflow + WorkflowTaskSet + DAG + Step + Parameter + Artifact
2. Map your Argo workflow audit trail in 48 hours
3. CNCF Graduated + Kubernetes CRD substrate — buyer-ready control matrix

## Email

Hi Argo maintainers —

Argo Workflows exposes five Kubernetes CustomResourceDefinitions — Workflow + WorkflowTemplate + CronWorkflow + ClusterWorkflowTemplate + WorkflowTaskSet — under the argoproj.io API group, with DAG + Step + Parameter + Artifact as first-class CRD field types. Enterprise buyers still ask the same narrower evidence question: can one exported record explain which WorkflowTemplate version triggered a Workflow, which DAG/Step fan-out handled it, which Kubernetes Pod + ServiceAccount executed it, which Artifact (S3/GCS/OSS/HTTP/Git) was the per-step input/output, and which retry-strategy pinned it?

I can map that evidence gap in 48 hours for $500, or maintain it quarterly for $497/month. The output is a buyer-ready control matrix — not an Argo replacement — and it will benchmark Argo against the now-CLOSED five-vendor workflow-orchestration cohort (Kestra + Temporal + Windmill + Prefect + Argo Workflows).

Worth sending the five-question scope?

— Atlas

## Personalization evidence

- First-party `argoproj.github.io/argo-workflows` (verbatim title "Argo Workflows - The workflow engine for Kubernetes", extracted 2026-07-24).
- First-party GitHub REST API (`api.github.com/repos/argoproj/argo-workflows`, extracted 2026-07-24): 16,844 stars, 3,576 forks, Apache-2.0 license, description "Workflow Engine for Kubernetes".
- CNCF Graduated project status (verbatim from the argoproj/argo-workflows README: "CNCF graduated project").
- Apache-2.0 license is the substrate license — Argo is OSS infrastructure, not multi-tenant SaaS.
- Sister projects under the same argoproj.io governance: Argo CD (declarative GitOps continuous delivery) + Argo Rollouts (progressive delivery + canary + blue-green) + Argo Events (event-driven workflow triggers from webhooks + S3 + SNS + Kafka + NATS + GCP PubSub + Azure EventGrid + GitHub + GitLab + Slack + Stripe + Bitbucket + EMR + File + Resource + Calendar).

## 20-col evidence wedge

| Column | Source | Confidence |
|---|---|---|
| `argo_workflow_id` | argoproj.github.io CRD docs | high |
| `argo_workflow_template_id` | argoproj.github.io CRD docs | high |
| `argo_workflow_template_version` | argoproj.github.io CRD docs | high |
| `argo_cron_workflow_id` | argoproj.github.io CRD docs | high |
| `argo_cluster_workflow_template_id` | argoproj.github.io CRD docs | high |
| `argo_workflow_task_set_id` | argoproj.github.io CRD docs | high |
| `argo_task_id` | argoproj.github.io CRD docs | high |
| `argo_task_type` (Container / Script / Resource / DAG / Step / Suspend / HTTP) | argoproj.github.io CRD docs | high |
| `argo_pod_id` | argoproj.github.io CRD docs | high |
| `argo_pod_service_account` | argoproj.github.io CRD docs | high |
| `argo_pod_node_selector` | argoproj.github.io CRD docs | high |
| `argo_pod_resource_quota` | argoproj.github.io CRD docs | high |
| `argo_step_id` | argoproj.github.io CRD docs | high |
| `argo_dag_id` | argoproj.github.io CRD docs | high |
| `argo_parameter_input_name` | argoproj.github.io CRD docs | high |
| `argo_parameter_output_name` | argoproj.github.io CRD docs | high |
| `argo_artifact_id` (S3 / GCS / OSS / HTTP / Git) | argoproj.github.io CRD docs | high |
| `argo_artifact_retention_policy` | argoproj.github.io CRD docs | high |
| `argo_retry_strategy_id` | argoproj.github.io CRD docs | high |
| `cross_tenant_no_bleed_invariant` | argoproj.github.io CRD docs | high |

## Source URLs (verified live 2026-07-24)

- https://argoproj.github.io/argo-workflows/
- https://github.com/argoproj/argo-workflows
- https://github.com/argoproj/argo-workflows/blob/main/README.md
- https://github.com/argoproj/argo-workflows/blob/main/GOVERNANCE.md
- https://argo-workflows.readthedocs.io/en/latest/
- https://api.github.com/repos/argoproj/argo-workflows