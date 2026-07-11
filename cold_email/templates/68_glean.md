# Glean — Cross-Tenant Permission Leakage in Workplace Search

**To:** partners@glean.com (Arvind Jain, CEO)
**From:** Atlas @ Talon Forge

---

Hi Glean team — when employees query Glean with natural language ("show me the compensation plan for the EMEA sales team"), the retrieval layer has to enforce ACLs across Slack, Drive, Notion, and Salesforce in a single hop. One misrouted embedding lookup and an intern in Austin sees the VP's comp memo. We just shipped a $500 / 48h "cross-tenant ACL audit" for enterprise AI search: we run 150 natural-language queries against your staging tenant, test boundary cases (shared channels, externally-shared Docs, partial-permission folders), and deliver a one-page ranked list of the 5 most likely leakage paths. Worth a 15-min call?