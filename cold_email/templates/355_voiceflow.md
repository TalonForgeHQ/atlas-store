# Cold Email Template 355 — Voiceflow (ai_agents_infra)

**To:** support@voiceflow.com
**From:** Potts (Talon Forge LLC)
**Subject:** Quick question on Voiceflow's per-flow audit trail + EU AI Act Art. 12 readiness
**Length:** ~340 words

---

Hi Voiceflow team,

I'm reaching out because I'm seeing enterprise procurement teams ask three specific questions about Voiceflow Canvas + Knowledge + Integrations that I think your platform may already have answers for — but the docs don't surface them clearly, so deals are stalling in legal review.

The three questions I'm hearing most often from SOC 2 + EU AI Act + ISO 42001 audit teams evaluating your workspace:

1. **End-to-end per-flow provenance.** When an enterprise-customer agent makes a Voiceflow Canvas decision (turn selection + NLU classification + Webhook call + handoff to human), can you produce a single signed audit-log row that joins per-flow-canvas-version + per-knowledge-document-id + per-conversation-turn-id + per-integration-credential-rotation-id + per-NLU-classifier-training-run-id + per-Webhook-API-call-id + per-handoff-to-human-event-id + per-A/B-experiment-variant-id, signed and WORM-retained for 7 years per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4? Or is that audit trail still a join across 3-4 separate Voiceflow product surfaces?

2. **Voiceflow-hosted AI-training corpus + per-customer-uploaded Knowledge Document license-provenance per EU AI Act Art. 53(d) GPAI training-data transparency.** When you train or fine-tune any internal model on customer-uploaded Knowledge Documents or conversation transcripts, can you produce the per-corpus-hash + per-license-spdx-id + per-cross-border-transfer-sccs-version + per-gdpr-dpa-signed-version chain on demand? The Aug 2026 GPAI enforcement date is 4 weeks out and most enterprise procurement teams won't sign without this.

3. **Cross-workspace Voiceflow Canvas + Knowledge + Integrations + Workflows isolation evidence per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10.** When a Voiceflow Enterprise customer runs 50-200 workspaces for 50-200 brands / BUs / geographies, can you produce the per-workspace-id-hash + per-flow-isolation-flag + per-knowledge-document-isolation-flag + per-conversation-transcript-isolation-flag + per-Webhook-credential-isolation-flag + per-tenant-KMS-key-id chain on demand? CMK/BYOK on Voiceflow Canvas + Knowledge?

If the answers are "yes, here's the audit-log query" — I'd love a 30-min technical call with the Voiceflow platform + compliance lead. If the answers are "in progress" or "on the roadmap," I'm building a 2-week audit-trail readiness sprint specifically for ai_agents_infra platforms and would be a strong fit to ship it before the next EU AI Act + SOC 2 audit cycle.

Happy to share the procurement-question checklist I've compiled from 30+ enterprise ai_agents_infra RFPs.

Best,
Potts
Talon Forge LLC
https://talonforge.com

P.S. Also: voiceflow.com/privacy exposes support@voiceflow.com — thanks for making the privacy/DPA channel discoverable. Most ai_agents_infra vendors bury it behind a 4-form-funnel.