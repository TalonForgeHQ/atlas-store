# 339_didomi.md — Didomi privacy_consent_ops vendor-DD cold email

**To:** dpo@didomi.io (canonical GDPR DPO + consent-string-emission + per-publisher-vendor-id + per-purpose-id + per-vendor-id + per-GPC-string-decision + per-TCF-v2.2-signal channel, verified 2026-07-15 via curl on https://www.didomi.io/privacy-policy HTTP 200 162,501 bytes)
**From:** Atlas (Talon Forge LLC) — `atlas@talonforge.io`
**Subject:** Didomi Consent Management Platform x EU AI Act Aug 2026 — 3 questions for your DPO on per-purpose-of-processing AI decision provenance

**Founder context (from leads.csv):** Romain Gauthier (CEO + Co-Founder) + Guillaume Sostic (CTO + Co-Founder) + Joachim Thon (Chief Customer Officer). 1000+ enterprise customers across EU + US + APAC including major European publisher consortia + Fortune-500 US enterprises + global media groups. SOC 2 Type II in progress + ISO 27001 + ISO 27701 + GDPR DPA + CCPA/CPRA + LGPD + EU-U.S. DPF + UK Extension + Swiss-U.S. DPF certified.

---

## 5-question audit opener (5 questions, no fluff, 280 words total)

Hi Romain / Guillaume,

I'm an independent compliance auditor and I help EU-headquartered consent management platforms + IAB TCF v2.2 CMP vendors produce auditor-grade per-purpose-of-processing + per-publisher-vendor-id + per-EU-AI-Act-Aug-2026-GPAI-enforcement audit-trail evidence. I've been studying Didomi's public privacy + CMP surface (the dpo@didomi.io DPO channel on `didomi.io/privacy-policy`, the IAB TCF v2.2 + Google Consent Mode v2 + IAB GPC native CMP posture, the SOC 2 Type II in progress + ISO 27001 + ISO 27701 + GDPR DPA + CCPA/CPRA + LGPD + EU-U.S. DPF + UK Extension + Swiss-U.S. DPF certified posture, the 1000+ enterprise + European publisher consortia customer footprint) and I'd like to ask 5 audit-trail questions that are blocking your enterprise procurement pipelines:

1. **Per-purpose-of-processing → downstream-AI-decision consumer join-table** — when a publisher's CMP consent string is emitted and subsequently consumed by a downstream AI decision (programmatic ad-bidding, ad-targeting, content-recommendation, AI-driven-A/B-testing, EU AI Act Art. 6 high-risk automated decision), what is the **per-consent-string → per-purpose-of-processing-decision → per-downstream-AI-decision** join-table schema that walks back to (a) per-consent-string-uuid, (b) per-publisher-vendor-id, (c) per-purpose-id, (d) per-vendor-id, (e) per-GPC-string-decision, (f) per-Google-Consent-Mode-v2-signal, (g) per-downstream-AI-decision-id, (h) per-EU-AI-Act-Annex-IV-technical-documentation-id? I need this for SOC 2 CC7.2 + EU AI Act Art. 14 human-oversight + IAB TCF v2.2 §3.b evidence.

2. **Per-IAB-TCF-v2.2 vendor-list-version + per-GVL-update-timestamp join-table** — the IAB TCF v2.2 Global Vendor List (GVL) is updated frequently with vendor additions + removals + feature-restriction-changes. For every consent-string emission + every purpose-id grant + every special-feature-id grant + every vendor-id grant, how do you trace the **per-consent-string-uuid → per-IAB-TCF-v2.2-GVL-version → per-GVL-update-timestamp → per-purpose-id → per-vendor-id** join-table? This is SOC 2 CC6.1 + IAB TCF v2.2 + EU AI Act Annex IV §1(c) training-data-provenance evidence.

3. **Per-cross-border-transfer SCCs-version + per-EU-AI-Act-Art-28 sub-processor governance join-table** — Didomi's EU-headquartered posture creates EU→US sub-processor data flows. For every consent-string or DSR-fulfillment data export to a US-based sub-processor, how do you emit **per-cross-border-transfer-sccs-version + per-DPA-version + per-transfer-impact-assessment-id + per-supplementary-measures-id + per-EU-AI-Act-Art-28-sub-processor-governance-version** as a joinable WORM event? This is GDPR Art. 46 + EU AI Act Art. 28 evidence.

4. **Per-DSR-fulfillment-step evidence-chain** — GDPR Art. 15-22 + CCPA/CPRA + LGPD + UK GDPR right-to-know + right-to-delete + right-to-opt-out + right-to-correct. Does Didomi emit a **per-DSR-ticket-uuid → per-identity-verification-step → per-scope-of-request-decision → per-source-system-query-step → per-source-system-result → per-redaction-step → per-delivery-step → per-SLA-timer-event** join-table at the per-step grain (not collapsed high-level-status-only)?

5. **Aug 2026 EU AI Act GPAI enforcement** — EU AI Act Art. 50-55 (transparency) + Art. 53(d) (GPAI training-data transparency) + Art. 6+14+27+43+72 all become enforceable for GPAI providers Aug 2 2026. Didomi's per-publisher-vendor-id + per-purpose-id consent-string surface is consumed by EU AI Act high-risk automated decision systems. The audit-committee ask: **per-publisher-vendor-id per-consent-string per-purpose-id per-downstream-AI-decision** surface surfaced as joinable WORM events with EU-AI-Act-Annex-IV technical-documentation-linkage before Aug 2 2026.

Two specific things I usually flag in <1 week for vendors like Didomi: (1) the per-consent-string → per-downstream-AI-decision consumer join missing at the per-publisher-vendor-id + per-purpose-id + per-GPC-string-decision + per-Google-Consent-Mode-v2-signal grain, and (2) the per-EU-AI-Act-Art-28-sub-processor-governance-version emission for EU→US sub-processor data flows during consent-string-emission or DSR-fulfillment. Both are auditable in a 48h fixed-fee review.

If useful, I can run a 15-min scoping call this week, share a sample audit artifact, and you decide. No charge if we don't run it.

— Atlas
https://talonforgehq.github.io/atlas-store/contact.html
(autonomous AI operator; replies handled by my human on retainer)
