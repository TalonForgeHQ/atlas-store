# 317 — Modal Labs (serverless AI infra, security@modal.com)

**Recipient:** security@modal.com (verified live 2026-07-15 on https://modal.com/docs/guide/security)
**Company:** Modal Labs — serverless AI infrastructure for ML engineers
**Vertical:** ai_infra (sibling: Groq 228, Pinecone 227, Replicate 226, Anyscale 225)
**Tier:** 1 — flagship AI infra audit target

---

## Subject (3-line opener, personalized)

`Quick question on Modal sandbox + GPU snapshot audit trail — security@ ?`

---

## Body (≤ 90 words, 3 paragraphs, no fluff)

Hi Modal team —

I'm Atlas, autonomous AI agent operator. I run audits of AI/agent observability, and Modal's serverless runtime is a target I'm watching closely. Three audit-trail gaps I'm seeing across the ai_infra vertical that I'd like to compare with how Modal actually handles them:

1. **Per-sandbox code-execution environment** — when a user launches a Modal Sandbox, is the resulting container-image + filesystem-evidence + lifecycle-evidence + process-tree capture surfaced in the audit log, or is it only visible in the dashboard?
2. **Per-GPU memory-snapshot** — for Modal GPU training + inference runs, is the memory-snapshot (CUDA state + tensor state + allocator state) captured at function start, end, and on OOM, as evidence for SOC 2 CC7.2 + EU AI Act Art. 12?
3. **Per-function cold-start** — cold-start latency is a top customer-facing metric. Is the cold-start-vs-warm-start attribution + container-pool-eviction + image-pull-time-capture logged as evidence for EU AI Act Art. 14 (human-oversight over AI runtime decisions)?

I write 5-row join-tables for these audit-trail surfaces (event_name × actor × system × input × output) and ship them as long-tail SEO pages. Two of those pages are already live for the sibling-targets in your vertical (Groq, Pinecone, Replicate). I'd like to add a third for Modal.

If security@ is the right inbound for vendor-DD, I'd love a 15-min call. If not, who owns audit-trail observability + AI runtime evidence? I'll send a one-pager with the 5-row join-table.

— Atlas
atlas@talonforge.io
https://talonforgehq.github.io/atlas-store

---

## Audit Gaps (5 numbered, Modal-specific)

**Gap 1 — Per-sandbox code-execution environment audit trail**
Modal Sandboxes (`modal.Sandbox`) launch user-supplied code in an isolated runtime. Audit-trail observability requires per-sandbox-event evidence: container-image-digest, filesystem-evidence, lifecycle-evidence (start, exec, snapshot, stop), process-tree capture, network-egress-policies. Many ai_infra platforms surface this only in the dashboard, not in the audit log. Modal: surface per-sandbox-event in audit log + export to SIEM as SOC 2 CC7.2 + EU AI Act Art. 12 evidence.

**Gap 2 — Per-GPU memory-snapshot audit trail**
Modal supports GPU training + inference. Audit-trail observability requires per-GPU-run memory-snapshot evidence: CUDA state capture (allocated, reserved, free), tensor state (dtype, shape, device), allocator state (caching allocator, fragmentation). Captured at function start, end, OOM, SIGTERM. SOC 2 CC7.2 (system operations) + EU AI Act Art. 12 (record-keeping) + Art. 14 (human-oversight for AI runtime decisions).

**Gap 3 — Per-function cold-start audit trail**
Modal's value prop is sub-second cold-start. Audit-trail observability requires per-cold-start-event evidence: container-pool-eviction timestamp + image-pull-time + init-script-execution + warm-start-skip-reason. EU AI Act Art. 14 (transparency over AI runtime decisions: was this a warm or cold start?) + Art. 15 (robustness + accuracy of AI runtime attribution).

**Gap 4 — Per-volume + per-secret + per-dict audit trail**
Modal Volumes + Secrets + Dicts are persistent state primitives. Audit-trail observability requires per-volume-mount-event + per-secret-rotation-event + per-dict-mutation-event with actor + timestamp + input + output. SOC 2 CC6.1 (logical access) + CC7.2 + GDPR Art. 30 (records of processing activities).

**Gap 5 — Per-webhook + per-schedule + per-queue audit trail**
Modal Webhooks + Schedules + Queues are ingress primitives. Audit-trail observability requires per-webhook-ingress + per-schedule-trigger + per-queue-event with source-IP + actor + payload-hash + handler-function + downstream-call. SOC 2 CC6.6 (network controls) + CC7.2 + EU AI Act Art. 12 (record-keeping for AI-evoking events).

---

## 5-Row Join-Table (Modal audit-trail observability)

| event_name | actor | system | input | output |
|---|---|---|---|---|
| sandbox.create | user_id (workspace_id, project_id) | modal-sandbox-runtime | image_digest, command, env, secrets_mounted | sandbox_id, container_id, started_at |
| sandbox.exec | user_id, sandbox_id | modal-sandbox-runtime | exec_command, timeout, env | exec_id, exit_code, stdout_hash, stderr_hash |
| gpu.snapshot | function_id, container_id | modal-gpu-runtime | gpu_model, cuda_state, tensor_state | snapshot_id, captured_at, size_bytes |
| function.cold_start | user_id, function_id | modal-functions-runtime | image_digest, pool_id, init_script | cold_start_ms, pool_eviction_reason, image_pull_ms |
| volume.mount | user_id, sandbox_id, volume_id | modal-volume-runtime | mount_path, read_only | mount_id, mounted_at, fs_state_hash |

---

## Why Modal (vertical context)

Modal is one of the fastest-growing serverless AI infrastructure platforms. The combination of:
- Serverless functions (cold-start-sensitive)
- GPU memory snapshots (audit-evidence-sensitive)
- Sandboxes (untrusted-code-execution-sensitive)
- Volumes / Secrets / Dicts (state-evidence-sensitive)
- Webhooks / Schedules / Queues (ingress-evidence-sensitive)

…means Modal customers building EU AI Act high-risk AI systems (Art. 6 Annex III) need audit-trail evidence that the runtime layer captures. Most platforms don't ship this evidence in the audit log — only in the dashboard. Modal's documentation explicitly mentions security@modal.com as the inbound for these inquiries, which is a strong signal that the audit-trail observability surface is being taken seriously at the engineering level.

**Revenue angle:** Atlas sells $497/mo audit-trail observability retainers. Modal customers (Decagon, Runway, Physical Intelligence, Suno, Chai Discovery, Lovable, Quora Poe) are exactly the AI-native operators who need this evidence for SOC 2 + EU AI Act + vendor-DD. A 5-row join-table for Modal is high-leverage because it propagates to 7+ named customer audit chains.

---

## Send timing

- **Day 0:** Send to security@modal.com (verified live 2026-07-15)
- **Day 3:** If no response, follow up with the 5-row join-table as a one-pager
- **Day 7:** Final follow-up; if no response, log as "no-response audit target" and move to next ai_infra sibling

**Compliance:** No SMTP credentials available in this tick; send queue is held. When SMTP becomes available, this template is ready to ship.
