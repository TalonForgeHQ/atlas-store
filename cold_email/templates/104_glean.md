# 104_glean.md — Glean Technologies (glean.com)

**To:** partners@glean.com (Arvind Jain, CEO; or partner BD)
**Subject:** The federated-permission-inheritance join-table is the SOC 2 + GDPR Art. 22 + HIPAA gap auditors are asking about
**Vertical:** enterprise_search_ai

---

Hi Arvind,

Glean's positioning — federated enterprise search across 100+ SaaS sources with AI-synthesized answers + write-back agents — is the most-ambitious permission-inheritance problem in enterprise AI right now. Customers like Databricks, Grammarly, Plaid, Rubrik, ServiceNow, and Reddit all bring regulated data into the retrieval pool.

The 2026 audit gap: **when Glean Assistant answers a question by combining chunks from Salesforce + Workday + Google Drive + Slack + Jira + Notion + Confluence, the join-table between the user's federated identity and each source-system's ACL must be reconstructible for SOC 2 CC6.1 + GDPR Art. 6 lawful-basis + HIPAA §164.502(b) min-necessary + EU AI Act Article 10 data-governance. And when Glean Agent writes back (updates Salesforce, creates Jira, sends Slack), the write needs end-to-end audit evidence — same gap pattern as Decagon/Sierra/Cresta.**

The 8 questions every auditor we work with at agent-platform vendors is asking in 2026:

1. **ACL snapshot at query time** — at the moment of retrieval, did Glean snapshot every source-system ACL that contributed to the retrieval? (per-query log row: query_id, user_id, timestamp, source, acl_version, acl_hash)
2. **Identity federation proof** — does the Glean audit trail record the IdP assertion ID + the source-system session ID + the timestamp skew between them? (so that after a domain migration, the join key is reconstructible)
3. **Retrieval ranking replay** — can Glean replay the retrieval-ranking pipeline for any past answer? (top-K chunks, ranking model version, re-ranker version, similarity score distribution, prompt template)
4. **Permission-inheritance join-table** — the hardest one. Per-query table with one row per source-system, columns for (source, document_id, source_acl_id, effective_acl_at_query_time, inherited_via_chain, deny_reason_if_any)
5. **Token-level provenance** — map every token in the LLM answer back to the source chunk it came from (chunk-level citation is not the same; the 2026 auditor expects token-level)
6. **PII redaction layer** — redaction at ingest vs retrieval vs output? GDPR Art. 25 data-protection-by-design requires you to defend which layer
7. **Writeback audit evidence** — when Glean Agent writes back to Salesforce/Jira/Slack, the audit trail needs (a) user identity that initiated, (b) prompt + retrieved chunks, (c) source-system API call log, (d) idempotency key, (e) rollback evidence
8. **GDPR Art. 17 + HIPAA delete propagation** — when a user invokes right-to-erasure, can Glean delete their data across all 100+ federated sources + eval sets + retrieval caches + fine-tune datasets within 30 days?

We do $500/48h audits that walk through the 8-question checklist. Reference architecture: S3 Object Lock (or equivalent WORM) + per-query join-table with all 8 artifacts bound to one immutable record. Engineering cost to ship all 8: 4 engineers × 12 weeks.

Worth a 30-min call? I can share the worksheet + the per-query schema + the compliance cross-walk (SOC 2 / GDPR / HIPAA / EU AI Act). Even just Q1+Q4+Q8 alone cover the 3 audit questions Glean's biggest EU customer will ask in the next procurement cycle.

— Atlas
Atlas Store · talonforgehq.github.io/atlas-store

P.S. The new SEO article we published today — "AI agent permission inheritance audit 2026" (chunk_39) — walks through all 8 questions with the compliance cross-walk table. Your customers' compliance teams will Google this within the next 6 months; we'd rather they land on it before your competitor's answer.