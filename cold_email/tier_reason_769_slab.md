# Lead 769 — Slab (Tier-Reason, ai_enterprise_knowledge_agents sibling #4/5)

**Vertical:** `ai_enterprise_knowledge_agents`
**Cohort position:** sibling #4/5 — after Guru 766 (OPENER #1/5), Tettra 767 (sibling #2/5), Slite 768 (sibling #3/5)
**Tier:** 1
**Route:** FORM:https://slab.com/contact-sales/ (HTTP 200 verified live 2026-07-21; server-rendered, no Wayback needed)
**Handle:** @SlabHQ
**Press contact (excluded from commercial outreach):** press@slab.com
**Responsible-disclosure (excluded):** security@slab.com

## First-party verification (cited)

- **slab.com/contact-sales/** — HTTP 200, server-rendered (335KB), footer ©2026 Slab Inc. Live verified 2026-07-21. The page names the canonical commercial entry point and the three jobs-to-be-done ("Create content that looks good by default. Make it easy for teammates to browse and discover. Learn about unified search, pulling your answers into one.") plus the Vevo testimonial from Scott Anderson, SVP Engineering and Product.
- **slab.com/security** — Wayback 2024 snapshot (252KB, server-rendered). SOC 3 + SOC 2 Type 2 + GDPR + ISO 27001; AES-128/256 at rest; SSL/TLS A+ from Qualys; bcrypt; Stripe PCI-compliant billing; annual third-party pen-tests; security@slab.com published as responsible-disclosure contact.
- **slab.com/about** — Wayback 2021-06-23 snapshot (281KB, server-rendered). Investors named with image-alts linking to matrixpartners.com + crv.com + NEA.com ("Our Investors" section).
- **TechCrunch 2018-02-06** — "Slab raises $2.2M to build tools for an internal employee information nexus" (referenced on first-party Press page).
- **slab.com/press** — Wayback 2021-04-12 snapshot (253KB). press@slab.com published as canonical press contact.

## Non-overlapping clauses vs siblings

- vs **Guru 766 (verified-wiki + browser/Slack/Teams delivery)**: Slab's verification is article-level with a freshness state, while Guru's is card-level with browser/Slack/Teams as the *delivery surface* (not the *retrieval surface*). Slab's unified-search traverses 6+ first-party connectors (Drive, Slack, GitHub, Asana, Airtable, Okta) and must reconcile per-connector ACL, while Guru's browser-extension surfaces Guru cards authored in Guru.
- vs **Tettra 767 (Slack/Teams-Q&A-bot + expert-verification escalation + structured wiki write-back)**: Slab's primary surface is unified search across the integration catalog (not a question→bot→expert flow). Tettra's escalation is expert-driven; Slab's verification is article-driven. Slab does not have a write-back-to-wiki primitive the way Tettra does.
- vs **Slite 768 (self-maintaining KB + MCP server + cross-workspace isolation + Super 2025 multi-product)**: Slab has no agentic self-maintenance primitive (no Slite Agent equivalent), no MCP server surface, no cross-workspace isolation in the same sense (Slab's isolation is per-tenant within one workspace, not across workspaces inside one tenant). Slite's distinct wedge is agent + MCP; Slab's distinct wedge is unified search + per-connector ACL cascade.

## Tier-1 evidence wedge (5 questions for the audit)

1. **Unified-search answer provenance across connected sources** — for each unified-search answer, which Google Drive file IDs + which Slack channel/message IDs + which GitHub commit SHAs + which Asana task IDs + which Airtable record IDs produced the answer; per-tenant ACL enforcement at each connector; retention window per source; region routing per connector; citation set attached.
2. **Verified topic-hierarchy + freshness state per KB article** — who verified the article, when, what changed since verification, what cache invalidations fired, how long the verification badge is honored before re-verification is required, what happens to search answers pointing at unverified topics.
3. **Permissions cascade across integrations** — Google Workspace OAuth scopes per Drive file, Slack channel ACL propagation, GitHub repo + branch ACL, Asana workspace + project ACL, Airtable base + table ACL, Okta group-membership-driven role assignment; the unified-search result must respect every ACL on every connector simultaneously.
4. **SOC 2 Type 2 + GDPR + ISO 27001 evidence packet per-tenant** — annual SOC 2 Type 2 report excerpt scoped to the customer's tenant, GDPR Art. 28 sub-processor list scoped to the tenant's connectors, ISO 27001 SoA mapping to the customer's data classification, EU AI Act Art. 14 human-oversight operational record if LLM sub-processor is used.
5. **Sub-processor cascade DPA + 14-day change-notification SLA** — Stripe (billing) + Google Cloud Platform (hosting) + Google Workspace OAuth (Drive) + Slack + GitHub + Asana + Airtable + Okta + OpenAI/Anthropic (if LLM-augmented) — 8-12 sub-processors per answer.

## Why tier 1

- Real company, real website, real first-party verified trust signals, real named enterprise customer (Vevo).
- Three top-tier investors (Matrix + CRV + NEA) verified via first-party About page snapshot.
- Compliance posture is mature (SOC 3 + SOC 2 Type 2 + GDPR + ISO 27001) and self-published.
- Canonical commercial route is FORM:https://slab.com/contact-sales/ (server-rendered, HTTP 200, no JS required, no Wayback needed for the route itself).
- The audit wedge is non-overlapping with the three siblings and addresses a distinct buyer-facing join: unified-search ACL cascade across 6+ connectors.

## Excluded routes (do NOT use as commercial entry)

- press@slab.com — published press contact only.
- security@slab.com — published responsible-disclosure contact only.
- careers@slab.com / jobs@slab.com — hiring only.
- support@slab.com — customer support only.
- /pricing — public pricing page; no transactional entry.
- /about — public About page; not a commercial route.

## Offer staged (do not send without explicit Atlas approval)

- $500 fixed / 48-hour evidence-gap map (8-12 page written deliverable).
- $497 / month quarterly refresh (every 90 days, re-run the 5-question audit, emit refreshed evidence packet).

## Hard rules followed

- Real company + real website + real first-party cited.
- No form submission, no email sent, no delivery, no payment, no revenue claimed.
- press / security / careers / support / founder / investor routes excluded.
- Canonical commercial route is FORM (slab.com/contact-sales/), not email.
