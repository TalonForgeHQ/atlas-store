# Cold Email Template — Lead 539 — Coda

**To:** hello@coda.io (canonical strategic-inbound)
**Company:** Coda
**Founded:** 2014
**HQ:** San Francisco, CA
**Founders:** Shishir Mehrotra (Co-Founder + CEO, ex-CEO Vevo, ex-VP Product YouTube) + Alex Chen (Co-Founder)
**Stage:** Late-stage growth (100K+ team customer base)
**Vertical:** workspace_ai_ops
**Tier:** 1 (canonical workspace-AI canvas + AI Brain + AI column + Packs)

---

## Subject line options (A/B test)
- A: `Shishir — one question about Coda AI Brain audit evidence`
- B: `Coda AI: 13-column provenance join-table for SOC 2 + EU AI Act`

## Body

Hi Shishir (or Alex) —

I'm reaching out because Coda sits in the daily workflow of 100K+ teams and the AI Brain + AI column + AI chat features now route LLM calls into documents ops + product + HR teams must audit. I'm a buyer-side audit consultant — I write fixed-fee $500 / 48-hour AI-vendor audit reports that help procurement + security + legal teams close the SOC 2 + EU AI Act + ISO 42001 + GDPR Art. 22 evidence gap.

**Three things I've found in similar workspace-AI vendors that I'd want Coda to have evidence for:**

1. **Per-AI-action 13-column provenance join-table** — `doc_id → workspace_id → ai_feature_type (AI Brain / AI column / AI chat) → prompt_template_id → retrieval_chunk_id → doc_chunk_id → pack_call_id → model_version_id → ai_output_id → coda_tenant_id → residency_region_id → audit_log_entry_id → procurement_vendor_DD_event_id`. Without this join, a buyer cannot answer a GDPR Art. 22 right-to-explanation request when an HR candidate pipeline runs through a Coda AI column.

2. **Pack-credential rotation + per-Pack-API-key-scope manifest** — every Coda Pack (Slack, Jira, Gmail, Salesforce, Stripe, NetSuite) carries an OAuth credential that lives in Coda's infra. The buyer needs an auditable log of credential rotation frequency, per-Pack-API-key-scope (read vs. write), and cross-workspace credential isolation — this is the SOC 2 CC6.1 evidence a regulated buyer will ask for during vendor-DD.

3. **AI-output ↔ doc-state-change cryptographic binding + 7-year WORM retention** — when a Coda AI column writes a value back to the doc, that write is a regulated artifact if the doc carries financial close data, HR candidate scoring, or customer PII. The buyer needs a per-AI-output ↔ per-doc-state-change cryptographic binding manifest + SEC 17a-4 / SOX 404 / GDPR Art. 30 WORM retention proof.

**What I do:** I run a 48-hour fixed-fee $500 audit that produces a buyer-ready PDF + an evidence binder mapping your AI actions to the SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 §9.4 + GDPR Art. 22 + Schrems II SCC requirements. No retainer, no hourly billing. The deliverable is a verifiable evidence manifest your auditor, your CISO, or your regulator can review.

**Why I'm reaching out specifically:** If Coda is in vendor-DD cycles for Fortune 500 buyers in 2026, the AI-action provenance gap is the question that will surface first. I'd like to show you what a great answer looks like — and I'd rather you have that answer before a Fortune 500 CISO asks for it.

Would you (or the right person on the AI infra / security / trust team) be open to a 15-minute call next week? I'll bring a sample audit binder for a peer workspace-AI vendor so you can see exactly what the deliverable looks like.

Best,
Atlas
Talon Forge LLC — buyer-side AI audit + compliance
talonforgehq.com | $500 / 48-hour fixed-fee audits

P.S. I'm independent — I don't resell Coda, I don't take referral fees from Coda, and the audit binder is yours to keep regardless of whether we ever work together again.
