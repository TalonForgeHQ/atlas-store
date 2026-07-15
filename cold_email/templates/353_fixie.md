# Cold Email Template 353 — Fixie / Ultravox (ai_agents_infra, Tier 1)

**To:** privacy@fixie.ai
**From:** Atlas (Talon Forge LLC) — atlas@talonforge.com
**Subject line A:** Fixie / Ultravox + Atlas — turn every realtime voice call into a reconstructable audit record

---

## Open (3 sentences)

Hi Zach — Fixie's move from the original voice-agent framework into the Ultravox speech-to-speech foundation model + Ultravox Realtime + Ultravox Studio + Fixie Agent Cloud is the moment when the voice-AI stack stops being "a clever demo" and becomes a regulated production surface that enterprise procurement will audit. The failure mode we keep seeing in realtime voice deployments is not "the model hallucinated"; it is that nobody can reconstruct the per-call speech frames, turn-takeaways, interruption-handling events, tool calls, customer-voice fine-tune lineage, region routing, and downstream state changes after the call ends. Atlas is the AI-governance + audit-target layer that turns those events into a joinable evidence trail without replacing the Fixie / Ultravox stack.

## 3 audit-target questions

1. **Per-call speech-frame + turn-takeaway provenance** — for each Ultravox Realtime call, do you retain a joinable record containing call-id, tenant-id, speech-frame-id, turn-takeaway-id, interruption-handling-event-id, VAD-endpoint-event-id, TTS-segment-id, model-provider, pinned-model-version, prompt-hash, region-routing-decision, and WebRTC-network-quality-state? Or is the evidence split between Ultravox dashboards, LLM-provider logs, and WebRTC monitoring so an auditor cannot replay one production call end to end?

2. **Tool-call and customer-voice fine-tune lineage** — when an Ultravox agent invokes a tool, makes an LLM decision, runs an interruption-handling event, or fine-tunes on a customer-uploaded voice sample, can you prove the policy version evaluated before the action, the exact arguments sent, the returned-data hash, the customer-voice-sample hash, the approval gate, the cost-attribution, and the downstream CRM / contact-center write id? This is the difference between "Fixie logged a call" and a reconstruction-ready record for SOC 2 CC7.2, NIST AI RMF, ISO 42001, EU AI Act Article 14 human oversight, and the EU AI Act Annex III 4 high-risk-classification surface that realtime voice agents fall into under the Aug 2026 GPAI enforcement deadline.

3. **Cross-tenant and fine-tune corpus isolation** — for Fixie Agent Cloud + Ultravox Realtime deployments that include customer-uploaded voice samples and fine-tune corpora, can the evidence package demonstrate tenant-id, deployment-id, fine-tune-corpus-version, retrieval-filter decision, secrets boundary, model-region, subprocessor route, customer-voice-sample lineage, and cross-tenant isolation for every realtime call? Or does the audit trail stop at the call audio while the per-tenant fine-tune corpus, voice-sample license-provenance, and tenant boundary remain implicit?

## Closes (3 variants)

**A — direct ask:**
If those three evidence surfaces are already instrumented or on the roadmap, we'd like 30 minutes with the Fixie / Ultravox security / platform team to map Atlas onto the gaps and quote a 14-day $497/mo retainer for the first production realtime-voice audit run. Reply with a 30-minute window and we will return a concrete field-level gap map.

**B — value-first:**
We've pre-built a free schema for per-call speech-frame provenance, interruption-handling events, customer-voice fine-tune lineage, and cross-tenant realtime isolation. Reply `template` and I'll send the CSV fields plus a reconstruction-drill runbook your team can adapt to Ultravox Realtime + Fixie Voice Agents + Fixie Agent Cloud.

**C — social proof:**
Atlas is already mapped against AI infrastructure, compliance automation, property-tech, privacy-ops, and legal-ops vendors where the same question appears in enterprise RFPs: can the operator reconstruct the AI decision and every downstream state change? Fixie / Ultravox is a strong next install because realtime voice is the highest-stakes production AI surface — interruption, hallucination, and downstream CRM corruption all happen in the same call. Reply with a 30-minute window.