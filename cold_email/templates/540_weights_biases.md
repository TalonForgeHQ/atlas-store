# Lead 540 — Weights & Biases (W&B)

**Vendor:** Weights & Biases / W&B (acquired by CoreWeave 2025)
**Domain:** wandb.ai
**Cohort:** Tier-1 ai_observability cohort sibling #2 (after Arize AI 538)
**Canonical inbox:** privacy@coreweave.com (verified live 2026-07-19 via curl /site/privacy)
**Tier reason:** Largest MLOps + LLM-observability install base in industry (1M+ practitioners); frontier-AI lab customers (OpenAI, Anthropic, Meta, Google DeepMind, Mistral, Cohere); Fortune 500 enterprise-AI teams across finance + healthcare + biotech + autonomous-vehicles + robotics + regulated industries. Post-acquisition the canonical strategic-inbound channel is CoreWeave enterprise-procurement-vendor-DD (privacy@coreweave.com) rather than the legacy wandb.com support@ inbox.

## Engagement

- **Fixed-fee 48-hour audit:** $500 (deliverable: 5-gap AI governance audit report)
- **Monthly retainer:** $497/mo (deliverable: ongoing W&B Inference + Weave + Traces + Prompts audit-trail monitoring, monthly EU AI Act + Schrems II + SOC 2 evidence package)
- **Procurement-vendor-DD package:** $1,500 (deliverable: full enterprise procurement vendor-DD packet for CoreWeave enterprise-procurement channel, includes SOC 2 + ISO 27001 + ISO 27701 + ISO 42001 + GDPR DPA + Schrems II SCC + EU AI Act Art. 12 + EU AI Act Art. 53(d) GPAI + HIPAA + FedRAMP-Ready + 12-state AI-disclosure evidence bundle)

## 5-gap audit framework

1. **End-to-end 13-col provenance join-table** — per-run-id → per-experiment-id → per-artifact-id → per-model-registry-id → per-launch-sweep-id → per-trace-id → per-prompt-id → per-weave-eval-id → per-workspace-id → per-team-id → per-procurement-vendor-DD-event-id → per-audit-log-entry-id → per-residency-region-id. Per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + ISO 27701 + GDPR Art. 30 + Schrems II SCC + 12-state AI-disclosure + EU AI Act Aug 2 2026 GPAI Art. 53(d) + Art. 14 human-oversight + Art. 50 transparency-obligation + CoreWeave enterprise-procurement-vendor-DD.

2. **Training-corpus + experiment-tracking + launch-sweep + artifact-versioning + trace + prompt + weave-eval + workspace-corpus license-provenance** — per EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary + ISO 42001 6.1.4 + Schrems-II-cross-border + EU-US-DPF + HIPAA + FedRAMP + SEC 17a-4 cross-border provenance.

3. **Prompt-injection + W&B-Inference-poisoning + W&B-Weave-poisoning + trace-poisoning + prompt-poisoning + experiment-poisoning + artifact-poisoning + workspace-tenant-prompt-injection + launch-sweep-prompt-injection defense** — per OWASP LLM Top 10 LLM01+LLM03+LLM06+LLM08 + MITRE ATLAS + EU AI Act Art. 14 + Art. 50 + 12-state AI-disclosure + Schrems II + HIPAA + FedRAMP.

4. **Cross-W&B-workspace isolation + per-tenant-KMS + CMK/BYOK + per-workspace-Inference-endpoint + per-Weave-trace-pool-isolation + cross-border-data-residency + CoreWeave-GPU-cloud-isolation** — per SOC 2 CC6.1 + GDPR Art. 28 + Schrems II SCC + EU-US DPF + FTC Safeguards Rule + ISO 27701 + HIPAA + FedRAMP + CoreWeave enterprise-procurement-vendor-DD.

5. **WORM retention + cost-attribution join-table** — per-run-cost + per-experiment-cost + per-artifact-cost + per-model-registry-version-cost + per-launch-sweep-cost + per-trace-cost + per-prompt-cost + per-weave-eval-cost + per-workspace-cost + per-team-cost + per-CoreWeave-GPU-cloud-cost + per-procurement-vendor-DD-event-cost. Per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + Schrems-II-recordkeeping + HIPAA-6-year + GDPR Art. 30 + FedRAMP-recordkeeping + CoreWeave-GPU-cloud-recordkeeping.

## Cold email — 3-paragraph opener

**Subject:** AI governance gap analysis for W&B Inference + Weave (48-hour audit)

Hi Lukas,

W&B Inference and Weave now sit at the frontier of LLM observability — 1M+ ML practitioners, OpenAI + Anthropic + Meta + DeepMind in production traces. The Aug 2 2026 EU AI Act GPAI documentation deadline (Art. 53(d) training-data transparency + Art. 53(1)(b) copyright summary) makes W&B's per-run → per-trace → per-prompt → per-weave-eval join-table the canonical evidence artifact — but only if it's audit-ready. The CoreWeave acquisition adds a procurement-vendor-DD layer (privacy@coreweave.com) that Fortune 500 enterprise-AI teams will start asking about this quarter.

I run a 48-hour, fixed-fee AI-governance audit ($500) that maps your W&B Inference + Weave + Traces + Prompts + Tools audit-trail surface against SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + Schrems II SCC + 12-state AI-disclosure + HIPAA + FedRAMP-Ready. Deliverable is a 5-gap audit report with the 13-col provenance join-table schema wired into your existing W&B workspace structure.

For W&B specifically, the gaps that move the needle: (1) per-run → per-trace → per-prompt lineage that's audit-ready by Aug 2, (2) cross-W&B-workspace isolation + CMK/BYOK evidence for Fortune 500 procurement teams, (3) CoreWeave-GPU-cloud tenant-isolation evidence for the post-acquisition procurement channel. If any of these are gaps, I close them as a $497/mo retainer with a monthly evidence-package deliverable.

Worth a 20-minute call next week? I'm free Tue 2-4pm PT or Thu 10am-12pm PT.

Best,
Atlas
Talon Forge LLC · ai-governance audit + retainer

---

**Inbox-verify budget used:** 2 probes (wandb.ai → privacy@coreweave.com verified via /site/privacy mailto:).
**Cohort progression:** ai_observability 2/2 anchored (Arize AI 538 + W&B 540). Next sibling candidates: Honeycomb (observability adjacent), LangSmith, Langfuse, Maxim AI, Comet ML, Patronus, Galileo (already separately anchored in other cohorts).
**Verification:** Lead row 540 in `cold_email/leads.csv` (8-col row, csv.writer QUOTE_ALL).