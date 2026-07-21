# Lead 769 — Slab (5-Question Audit Letter)

**Recipient:** Slab, Inc. (canonical commercial route: https://slab.com/contact-sales/ — verified live 2026-07-21)
**Route:** FORM:https://slab.com/contact-sales/ (verified HTTP 200 live 2026-07-21; server-rendered; no general-business inbox published; press@slab.com and security@slab.com are press/responsible-disclosure only and excluded)
**Subject:** Slab unified-search evidence map — per-connector ACL cascade + sub-processor DPA (48h, $500 fixed)

---

Hi Slab team,

I built a 5-question evidence-gap audit for Slab's unified-search-first knowledge base — covering the verified-topic-hierarchy, the unified-search answer provenance across the integration catalog (Google Drive + Slack + GitHub + Asana + Airtable + Okta), the per-connector ACL cascade, the SOC 2 Type 2 + GDPR + ISO 27001 per-tenant evidence packet, and the 8-12 sub-processor cascade. The EU AI Act Art. 14 enforcement window opens August 2 2026, and a unified-search-first knowledge base has a specific per-connector ACL-cascade + LLM-sub-processor surface that is non-overlapping with browser-resident copilots, Slack/Teams Q&A bots, or self-maintaining KB agents — so the audit template is different from a Guru, Tettra, or Slite audit.

**5 questions I would answer in your $500 fixed-scope 48-hour evidence-gap map:**

1. **Unified-search answer provenance across connected sources** — For each unified-search answer served to a Slab user, do you capture (a) the user identity + workspace + tenant, (b) the search query, (c) which Google Drive file IDs + which Slack channel/message IDs + which GitHub commit SHAs + which Asana task IDs + which Airtable record IDs produced the answer (per your Integrations catalog at slab.com), (d) per-connector ACL enforcement (Drive file ACL + Slack channel ACL + GitHub repo ACL + Asana project ACL + Airtable base ACL + Okta group membership), (e) LLM sub-processor invoked if LLM-augmented re-ranking is enabled (OpenAI vs. Anthropic vs. self-hosted), (f) retention window per source, and (g) region routing per connector? Is this audit trail exportable as a single artifact for procurement review?

2. **Verified topic-hierarchy + freshness state per KB article** — Slab's verified-topic-hierarchy is one of the distinct wedges vs Confluence/Notion (per your Compare pages at slab.com). For each KB article in the hierarchy, do you capture (a) who verified the article (user identity + role), (b) when verification occurred (timestamp + retention), (c) what changed in the article since verification (diff hash), (d) what downstream search-result cache invalidations fired when the article changed, (e) how long the verification badge is honored before re-verification is required (90 days? 180 days? configurable?), and (f) what happens to search answers pointing at unverified topics (suppressed? flagged? down-ranked?)? Where is this freshness state persisted (your Postgres + your cache + your search index)?

3. **Permissions cascade across integrations** — A unified-search answer that pulls from 6+ connectors must respect every ACL on every connector simultaneously or it is a data-leak. Do you publish (a) Google Workspace OAuth scopes per Drive file (least-privilege per-file vs. broad tenant-wide scope), (b) Slack channel ACL propagation (which channels the user is in; whether private-channel content can be returned via search), (c) GitHub repo + branch ACL (whether private-repo code can appear in unified-search results), (d) Asana workspace + project ACL, (e) Airtable base + table ACL, and (f) Okta group-membership-driven role assignment (which roles can see which connector content)? How is the per-connector ACL reconciled at query time, and what is the test surface that proves a user who lacks Drive access to file X cannot see file X's content even if another connector returned a reference to file X?

4. **SOC 2 Type 2 + GDPR + ISO 27001 evidence packet per-tenant** — Slab's first-party security page (slab.com/security, verified 2024) publishes SOC 3 + SOC 2 Type 2 + GDPR + ISO 27001 certifications on the Google Cloud Platform. For an enterprise procurement review, do you provide (a) the most-recent annual SOC 2 Type 2 report excerpt scoped to the customer's tenant, (b) the GDPR Art. 28 sub-processor list scoped to the tenant's connectors (i.e. which of Stripe + Google Cloud Platform + Google Workspace OAuth + Slack + GitHub + Asana + Airtable + Okta + OpenAI/Anthropic are active for THIS tenant), (c) the ISO 27001 Statement of Applicability mapping to the customer's data classification, and (d) an EU AI Act Art. 14 human-oversight operational record if the customer's tenant uses LLM-augmented unified-search? How is this evidence packet refreshed when a connector is added or removed?

5. **Sub-processor cascade DPA + 14-day change-notification SLA** — Slab's per-answer sub-processor cascade for a customer using the full integration catalog runs Stripe (billing) + Google Cloud Platform (hosting) + Google Workspace OAuth (Drive) + Slack + GitHub + Asana + Airtable + Okta + OpenAI/Anthropic (if LLM-augmented) — totaling 8-12 sub-processors in the per-answer cascade. Do you maintain a current sub-processor list with flow-down DPA, and does your DPA with each include a 14-day change-notification SLA per GDPR Art. 28(2)? Specifically, do you publish a list of LLM sub-processors used for unified-search re-ranking (OpenAI vs. Anthropic vs. both), and do you have a customer-facing change-notification mechanism for connector additions (e.g. when Slab adds Notion as a connector, are existing customers notified within 14 days)?

**What you get for $500 / 48h:** a written 8-12 page evidence-gap map with each of the 5 questions answered (current state + gap + remediation ETA + dollar/effort estimate), plus a redlined Slab sub-processor list + a per-connector ACL reconciliation matrix you can hand to procurement.

**What you get for $497 / month:** quarterly refresh — every 90 days we re-run the 5-question audit, capture the delta (new connector + new LLM sub-processor + new region + new verification state), and emit a refreshed evidence packet you can hand to the next EU enterprise buyer.

Reply with a yes/no on the 48h engagement (or use the Contact Sales form at https://slab.com/contact-sales/ and reference "Atlas / Talon Forge audit") and I'll send a Stripe payment link.

— Atlas / Talon Forge
atlas@talonforge.com

---

**Cohort marker:** ai_enterprise_knowledge_agents sibling #4/5 after Guru 766 OPENER + Tettra 767 + Slite 768.
**Hard rules followed:** real company + real website + real first-party cited (slab.com/contact-sales/ HTTP 200 live 2026-07-21, slab.com/security 2024 snapshot, slab.com/about 2021 snapshot, slab.com/press 2021 snapshot, TechCrunch 2018-02-06); no form submission; press/security/careers/support/founder/investor routes excluded; offer $500/48h or $497/mo; no email sent, no delivery, no payment, no revenue claimed.
