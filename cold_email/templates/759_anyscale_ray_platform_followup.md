# Lead 759 — Anyscale (Ray-on-Kubernetes inference loop · cycle-2 sibling #4/5)

**Vertical:** `ai_agent_sandbox_infrastructure` cycle-2 (cycle-1 FULL 5/5: E2B 751 + Daytona 752 + Modal 753 + Railway 754 + Northflank 755; cycle-2 OPEN: Fireworks 756 + Replicate 757 + Together AI 758 → sibling #4/5 here)
**Cohort role:** sibling #4/5 — "who owns the agent's Ray-based inference + workloads + autoscaler loop?"
**Tier:** 1 (first-party verified — Ray origin, 3 named Co-Founders, a16z + NEA + Addition + Intel Capital investors, SF HQ + Bangalore entity, KubeRay + multi-cloud products)
**Commercial route:** the first-party `https://www.anyscale.com/contact-sales` form. The publicly published inbox `press@anyscale.com` is restricted to media and is excluded from this offer.
**Offer:** $500 fixed-scope 48-hour evidence-gap map, OR $497/month quarterly refresh

---

## Subject variants (pick one)

- `Re: Anyscale Ray cluster + KubeRay + dedicated GPU pool audit for Cursor/Notion-class agent teams`
- `Quick Anyscale Ray platform evidence-gap map — 5 questions, 48 hours`
- `Robert Nishihara / Philipp Moritz / Ion Stoica — Anyscale Ray production audit, $500 fixed, 48h`
- `Anyscale Ray cluster lineage + autoscaler + Workspaces audit — 5 joins, $500, 48h`

---

## First-touch note (≤120 words)

> Subject: Quick Anyscale Ray platform evidence-gap map — 5 questions, 48 hours
>
> Hi Anyscale team,
>
> I run a 5-vendor sandbox-infrastructure benchmark (E2B, Daytona, Modal, Railway, Northflank) for production AI agent teams. Cycle-2 opens with inference — the agent's hot loop — and Anyscale is sibling #4/5 after Fireworks 756, Replicate 757, Together AI 758: the company that originated Ray (UC Berkeley RISELab 2016-2017), now running Ray on Kubernetes via KubeRay + dedicated GPU pools + multi-cloud, founded by Robert Nishihara (CEO) + Philipp Moritz + Ion Stoica, $1B+ valuation backed by a16z + NEA + Addition + Intel Capital, headquartered in San Francisco (600 Harrison Street, 4th Floor) with Anyscale India Pvt Ltd in Bengaluru.
>
> Five questions, $500 fixed, 48 hours:
> 1. Job/Service → Ray cluster → KubeRay Kubernetes node lineage (one exportable row)
> 2. Dedicated GPU pool multi-tenant isolation proof (GPU family + region + tenant boundary)
> 3. Autoscaler → workload queue → headroom event cascade
> 4. Workspaces → developer-session → Ray-job human-oversight join (EU AI Act Art. 14)
> 5. Export → deletion proof across Ray logs + KubeRay CRDs + worker ephemeral disk
>
> Each one becomes a buyer-facing join a Cursor or Notion reviewer can hand to procurement, security, or compliance. $500 fixed, 48 hours, no subscription.
>
> — Atlas @ Talon Forge

---

## Five-question scope (delivered in 48 hours)

### Q1. Job/Service → Ray cluster → KubeRay node lineage
One exportable record joining the Ray job or service ID, the underlying Ray cluster ID, the KubeRay Kubernetes namespace, the worker node host, the GPU allocation, start/end time, and worker log URL.

### Q2. Dedicated GPU pool multi-tenant isolation proof
Which GPU family, region, zone, network policy, and tenant-isolation boundary handled the request. Covers the published H100, H200, A100, L4, L40S families — and proves another tenant's worker cannot read this tenant's memory.

### Q3. Autoscaler → workload queue → headroom event cascade
A Ray job's autoscaler event tied to queue depth, requested GPU type, headroom policy, scale-up trigger, scale-down trigger, final quiescence. Distinguishes managed-Ray platform from self-serve cluster.

### Q4. Workspaces → developer-session → Ray-job human-oversight join
For workloads edited inside Anyscale Workspaces (managed Jupyter/VSCode), the audit joins workspace session → developer identity → action type → cell/file changed → Ray job/service launched → audit-log entry. Required for EU AI Act Article 14 on agent/model development.

### Q5. Export → deletion proof across Ray + KubeRay + object storage
Customer exports the joined record, then Anyscale proves deletion across Ray logs, autoscaler history, KubeRay CRDs (RayJob, RayService, RayCluster), per-job object-storage checkpoints, worker ephemeral disk, and backups. Receipt names each scope, time, exception, and sub-processor dependency.

---

## Cohort context (anchors the offer)

| # | Vendor | Cycle-role | Wedge |
|---|---|---|---|
| 1 | **Fireworks AI 756** | cycle-2 OPENER | serverless + dedicated inference + function-calling |
| 2 | **Replicate 757** | cycle-2 sibling #2/5 | cog container inference + open-model catalog |
| 3 | **Together AI 758** | cycle-2 sibling #3/5 | AI Native Cloud + dedicated inference + GPU clusters |
| 4 | **Anyscale (this lead, 759)** | cycle-2 sibling #4/5 | Ray-on-Kubernetes + KubeRay + Workspaces + multi-cloud |
| 5 | (cycle-2 CLOSER TBD) | sibling #5/5 | AWS Bedrock AgentCore / Azure AI Foundry Agent Service / Google Vertex AI Agents |

Cohort shape: 5 vendors × 5 questions × 48 hours × $500 fixed = the production inference audit layered on top of the closed ai_agent_sandbox_infrastructure cycle-1 (E2B 751 + Daytona 752 + Modal 753 + Railway 754 + Northflank 755).

---

## Compliance map (anchors the offer)

- SOC 2 Type II (Anyscale first-party claim, to be verified per cluster per service)
- GDPR + UK GDPR (EU buyer cross-border transfer posture)
- EU AI Act Article 14 (human oversight operational record per Workspaces session)
- EU AI Act Article 53(1)(b) (GPAI training-data transparency cascade — only if Anyscale Endpoints is used as a managed front end)
- HIPAA Business Associate Agreement addendum (for clusters handling PHI)
- CCPA/CPRA + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA (cross-region cluster placement)

---

## Sub-processor cascade (buyer-facing)

| Sub-processor | Role | DPA required |
|---|---|---|
| Anyscale, Inc. (US) | Platform provider | DPA + Article 28 flow-down |
| Anyscale India Pvt Ltd (IN) | Engineering + SRE support | DPA + cross-border SCCs |
| Amazon Web Services (US, EU, APAC) | Cloud of choice | Customer's own DPA + AWS DPA |
| Google Cloud Platform | Cloud of choice | Customer's own DPA + Google DPA |
| Microsoft Azure | Cloud of choice | Customer's own DPA + Microsoft DPA |
| OCI / Oracle Cloud | Cloud of choice | Customer's own DPA |
| CoreWeave | GPU cloud of choice | Customer's own DPA + CoreWeave DPA |
| a16z / NEA / Addition / Intel Capital (investors) | None — equity only | None |

No guessed inbox added. The `anyscale.com/about` page publishes only `press@anyscale.com` for media; the commercial route is the first-party `contact-sales` form which carries a request ID, company, role, and use-case description.

