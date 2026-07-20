# Modal serverless AI sandbox evidence replay — Lead 753

**Company:** Modal Labs, Inc.
**Website:** https://modal.com/
**Route:** `mailto:security@modal.com` (first-party Enterprise / HIPAA BAA / SOC 2 / PCI / GDPR contact on /docs/guide/security); alt `mailto:support@modal.com` (first-party support line on /company)
**Executive:** Erik Bernhardsson, Co-founder + former CTO and current Chief Executive Officer; Akshat Bubna, Co-founder + CTO
**Vertical:** `ai_agent_sandbox_infrastructure` cycle-1 sibling #3/5
**Offer:** $500 fixed-scope 48-hour evidence-gap map or $497/month quarterly refresh
**Status:** TEMPLATE ONLY — no email, form submission, delivery, reply, payment, or revenue is claimed

---

## Subject options

1. `Modal sandbox receipts — five checks for serverless AI agent compute`
2. `Can a Modal customer replay every sandbox, snapshot, image, and volume change?`
3. `A 48-hour evidence map for Modal's serverless AI compute runtime`

## Open

Hi Erik (cc Akshat and the Modal team) — I mapped Modal's current first-party serverless AI infrastructure surface against the receipts an enterprise buyer needs before letting agents run untrusted CPU or GPU code in Modal Sandboxes, Inference endpoints, and Training jobs.

The public story is clear: bring-your-own code, run CPU/GPU/data-intensive compute at scale, scale from zero to thousands of CPUs or GPUs in a few lines of code, with $30/month free compute, the modal Python SDK, the `modal run` CLI, the Sandboxes product page, automated health checks, readiness probes (TCP port / file / any shell condition), detailed logging and metrics, Memory Snapshots, Filesystem and Directory Snapshots, Images, Volumes v1 (out of HIPAA scope) and the HIPAA-Compliant Volumes v2, custom container runtimes, custom schedulers, and Custom container image builders. SOC 2 Type 2 has been completed (audit announcement at /blog/soc2type2 with the SOC 2 Type 2 report behind trust.modal.com). HIPAA Business Associate Agreements are available on the Enterprise plan via security@modal.com. A PCI section is published on the security page.

The narrower audit question is whether one Modal customer can reconstruct a material agent run after the sandbox ID, image, snapshot, runtime, region, file mutations, secrets, tools, people, and downstream systems have changed.

## Five-question evidence replay

1. **Sandbox identity and image lineage:** Can each sandbox export the sandbox ID, image or Docker input, snapshot version (Filesystem and Directory Snapshot, Memory Snapshot), runtime and SDK versions, region, tenant, and Customer-Managed Compute or customer-key-scope identity into one immutable receipt?
2. **Execution and filesystem provenance:** Can a reviewer trace one agent instruction through process execution, code run, file mutation, Image rebuild, Volume attach, Function call input/output hash, Modal Inference endpoint call, exit state, and resulting filesystem state?
3. **Persistent state and volume boundary:** Modal publishes Volumes v1 (out-of-HIPAA scope) and HIPAA-Compliant Volumes v2. Can every Volume mount, read, write, snapshot, restore, and detach event preserve volume identity, tenant scope, HIPAA-or-non-HIPAA classification, and a before/after hash?
4. **Readiness, health, and human intervention:** Modal publishes automated health checks, readiness probes (TCP port / file / any shell condition), detailed logging and metrics, observability dashboards, and modal Sandbox dashboard control plane. Can autonomous actions be separated from human operator intervention and tied to the resulting state they changed?
5. **Retention, deletion, and shared-responsibility replay:** Modal's shared-responsibility model says customers own backups, recovery, availability, and security measures. Can a customer reproduce a run, verify rollback, export sandbox, process, volume, log, backup, and deletion-cascade completion, and prove what did not survive teardown?

## Deliverable

Within 48 hours I return:

- a one-page red / amber / green evidence-gap map;
- the five highest-priority missing receipts;
- a sample serverless-sandbox run schema;
- a Trust Center publication checklist; and
- an updated EU AI Act Article 14 human-oversight record template.

## Engagement options

- **$500 fixed-scope, 48 hours** — one-shot evidence-gap map.
- **$497 per month, quarterly refresh** — refresh after material snapshot, runtime, region, image, volume, sandbox, API, or compliance changes.

## Cohort non-overlap

E2B 751 owns the full-computer agent-cloud lane with sandbox image, credential/egress, replay, and teardown receipts. Daytona 752 adds stateful execution, reproducible snapshots, persistent volumes, customer-managed compute, programmatic process/file/Git/LSP control, and multi-OS computer-use oversight. Modal 753 owns the serverless, scale-to-zero CPU/GPU compute, Python-decorator (`@app.function()`) + `modal run` CLI, Memory Snapshots + Filesystem Snapshots + HIPAA-Compliant Volumes v2, automated health checks + readiness probes, Inference endpoints + Training jobs, modal Sandbox dashboard observability, and the $466M-raised / SOC 2 Type 2 / HIPAA BAA / GDPR DPA / UK GDPR / PCI enterprise posture wedge.

## Evidence boundary

Modal's first-party homepage, /company page, /products/sandboxes page, /docs/guide/security page, /blog/soc2type2 page, trust.modal.com Security Portal, /legal/privacy-policy, /legal/terms, and /products/* pages support the company, founder, product, location, compliance, and route statements above. This template does not claim a Modal partnership, certification audit result, customer outcome, email, form submission, delivery, payment, or revenue. The commercial route is the first-party security@modal.com address published on the canonical /docs/guide/security page (and trust.modal.com for SOC 2 Type 2 report access); no email was sent.

— Atlas @ Talon Forge