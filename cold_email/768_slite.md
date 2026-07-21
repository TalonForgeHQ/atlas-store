# Lead 768 — Slite (Evidence Note)

**Company:** Slite, Inc.
**Website:** https://slite.com (live, HTTP 200, 2026-07-21)
**Founded:** 2017 (per slite.com/about "We founded Slite in 2017")
**Headquarters:** Delaware (©2026 Slite, Inc.) — remote-first, multi-locale EN/FR/ES/DE/NL/JA
**Backers:** Spark Capital + eFounders + Index Ventures + Y Combinator (verified live on slite.com/about)
**CEO:** Christophe Pasquier (Co-founder & CEO — verified live 2026-07-21 on slite.com/about as "Christophe Pasquier, Slite CEO" and in vike_pageContext structured data with `position:"CEO"`)
**CTO:** Pierre Renaudin (verified live 2026-07-21 in vike_pageContext structured data with `position:"CTO"`)
**COO:** Fadeelah Al-Horaibi (verified live 2026-07-21 in vike_pageContext structured data with `position:"COO"`)

## First-party verification (live 2026-07-21, curl + Mozilla/5.0 Chrome/130.0 UA)

| URL | HTTP | Source |
|---|---|---|
| https://slite.com/ | 200 | homepage; footer identifies ©2026 Slite, Inc. + support@slite.com + LinkedIn + X @SliteHQ |
| https://slite.com/about | 200 | "We founded Slite in 2017"; "In 2025, we went multi product and built its cousin, Super"; CEO quote "Christophe Pasquier, Slite CEO"; Backed by Spark Capital + eFounders + Index Ventures + Y Combinator |
| https://slite.com/book-demo | 200 | first-party Book Demo form route (commercial) |
| https://slite.com/privacy | 200 | privacy notice |
| https://slite.com/security | 200 | security posture page |
| https://slite.com/legal | 200 | legal information page |

## Product surface (current, 2026)

- **Slite (original KB):** self-maintaining knowledge base with AI Search + Ask Slite + Slite Agent + MCP server + Integrations catalog
- **Super (2025 launch):** multi-product cousin for the AI era — teams' ultimate AI search on all their tools + agents able to tap on their collective knowledge
- **Comparisons:** /compare/alternative-to-notion, /compare/alternative-to-confluence, /compare/alternative-to-guru, /compare/alternative-to-google-docs, /compare/alternative-to-slab (Slite publishes direct comparisons to 5 alternatives)
- **Ratings:** 4.7/5 on G2 Crowd + 4.7/5 on Capterra + 4.9/5 on Product Hunt (first-party verified on slite.com footer)
- **MCP:** dedicated /mcp page + slite.com/integrations (catalog)

## Routes used vs. excluded

- **Used:** FORM:https://slite.com/book-demo (first-party Book Demo route, HTTP 200 verified)
- **Excluded as support-only:** support@slite.com (footer + Cookie/legal pages; not a commercial inbox)
- **Excluded:** privacy@slite.com / legal@slite.com / security@slite.com (these are documented-policy routes, not commercial)
- **Excluded:** press / careers / investor / founder direct-mail routes (no first-party verified general-business inbox)

## Wedge (5 buyer-facing joins)

1. Slite Agent self-maintenance provenance + write-back ledger
2. AI Search answer provenance across MCP-connected sources
3. Cross-workspace data-isolation audit (workspace-A vs. workspace-B)
4. MCP server surface audit (per-tool OAuth + per-tenant authorization + retention + region)
5. Sub-processor cascade DPA + 14-day change-notification SLA across Slite gateway + OpenAI + Anthropic + per-MCP-integration sub-processor

## Compliance map (current, 2026)

- GDPR + UK GDPR + CCPA/CPRA + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA + LGPD (verified via slite.com/privacy)
- EU AI Act Article 14 (human-oversight) + Article 50 (transparency-labeling) + Article 53(1)(b) (GPAI cascade) — Aug 2 2026 enforcement window
- SOC 2 verification pending (slite.com/security published; report under NDA per standard procurement flow)
- SAML SSO + SCIM + audit-logs + IP-allowlist Enterprise-tier security review packet
- 5,000+ product/ops/engineering/support/HR teams using Slite per the homepage hero

## Offer

$500 fixed-scope 48-hour evidence-gap map or $497/month quarterly refresh. No email sent, no form submitted, no delivery, no payment, no revenue claimed.

## COHORT marker

ai_enterprise_knowledge_agents sibling #3/5 after Guru 766 OPENER + Tettra 767.

## Non-overlap clauses (vs. earlier siblings)

- **Non-overlapping with Guru 766:** Guru's wedge is verified-knowledge control plane + browser/web/Slack/Teams delivery + verification-state freshness; Slite's wedge is self-maintenance + AI Search + MCP + Super multi-product 2025 surface + cross-workspace isolation (Guru does not ship MCP, does not publish a multi-product cousin, does not position around AI Search across all MCP-connected tools)
- **Non-overlapping with Tettra 767:** Tettra's wedge is Slack/Teams-native Q&A bot + expert-verification escalation + structured wiki write-back; Slite's wedge is in-app KB-resident self-maintenance + AI Search + MCP server (Tettra does not ship MCP, does not ship self-maintenance, does not ship Super-style AI search across all connected tools)
- **Non-overlapping with Notion AI (different lead):** Notion's wedge is block-based collaborative editor + AI inline assist; Slite is a dedicated self-maintaining KB with Agent + MCP + Super multi-product
- **Non-overlapping with Confluence (different lead):** Confluence's wedge is Atlassian-suite-bundled page + Atlassian Intelligence; Slite is KB-first + MCP-first + agent-self-maintenance-first
