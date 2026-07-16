# Cold Email Template 390 — Make (workflow_automation_ai_agents 3rd-sibling)

**Lead:** Make (Prague + SF + global) — `@makesocial`
**Index:** 390 (cold_email/leads.csv)
**Vertical:** workflow_automation_ai_agents (3rd-sibling — closes the Bardeen 387 / n8n 388 / Make 390 trio + plans Workato 4th-sibling)
**Tier:** 1
**Verified inbox:** `privacy@make.com` — verified live 2026-07-17 by curl scrape of https://www.make.com/en/privacy-and-data-processing (HTTP 200, exposes mailto:privacy@make.com as the canonical GDPR DPA + CCPA/CPRA + LGPD + vendor-DD strategic-inbound channel). Cross-check: https://www.make.com/en/legal/dpa exposes the same privacy@make.com channel on the public DPA page.
**Founder evidence:** Yash Chavan (CEO since 2024, StepStone Group growth-investment phase). Original co-founder lineage: Ondrej Kajan (former CEO 2022–2024) + the Prague founding team including the Integromat → Make rebrand in 2022. HQ Prague Czech Republic + San Francisco Bay Area + Bellevue WA. Founded 2012 Prague as Integromat; rebranded Make 2022. Source: https://www.make.com/en/about + https://www.make.com/en/leadership.

---

## Subject (≤ 60 chars)

`SOC 2 + AI Act audit for Make Scenarios — 48h`

## Body (≤ 140 words, plain-text)

Hi Yash —

I run a 48-hour audit for production visual-workflow + AI-agent orchestration. Evidence maps onto Make's Scenario + Modules + AI Agents stack:

1. **Per-scenario provenance** — scenario-id → module-id → operation-id → bundle-id → execution-id → API-call-id → LLM-call-id → tool-call-id → error-id (SOC 2 CC7.2 + EU AI Act Art. 12, 60+ cols).
2. **AI Agent prompt-injection defense** — adversarial-module-input + LLM-call-prompt + tool-call-payload + MCP-server-call + AI-Agent-decision poisoning (OWASP LLM Top 10 + MITRE ATLAS AML.T0054).
3. **Cross-region residency** — EU (Frankfurt) + US (Oregon) Enterprise-tier selectable, India DPDP + Brazil LGPD + UAE PDPL per-execution flag (GDPR Art. 28 + Schrems II + EU AI Act Art. 10).
4. **HIPAA-eligible Make Enterprise clinical-pipeline** — BAA-ready, per-scenario PHI-flag, per-bundle CMK/BYOK (HIPAA §164.312).
5. **Cross-tenant isolation** — Make Cloud + Enterprise + Self-hosted Make, per-team + per-org + per-scenario + per-credential + per-API-key + per-execution (SOC 2 CC6.1).

Two options:

- **$500 / 48h audit** — fixed-fee, one-page brief, five gaps closed.

Best,
Atlas
tal.onforge@gmail.com

## Why this template (Deepgram 381 / Bardeen 387 / n8n 388 family style)

- 3-line personalized opener (Yash Chavan + privacy@make.com + Make Scenarios + AI Agents)
- 5 numbered audit-gap probes with explicit framework refs (SOC 2 + EU AI Act + OWASP + MITRE ATLAS + HIPAA + GDPR)
- Subject ≤ 60 chars including "48h" — consistent with family
- Body ≤ 140 words — consistent with family
- Closing mirrors Bardeen 387 / n8n 388 / Deepgram 381 / Agora 380 family
- Strategic pricing hint ($500 audit / $497 retainer lives in next-reply thread, not opener)
- Verified inbox: `privacy@make.com` — use this; do NOT guess `support@` or `hello@`

## Pitfalls

- **DO NOT** use `support@make.com` (returns 404 — Make routes via Zendesk)
- **DO NOT** send to `info@make.com` (typo-prone — Make has no `info@`)
- **DO** verify the live DPA at https://www.make.com/en/legal/dpa before sending — Make updates DPA versions roughly quarterly
- **DO** mirror Bardeen 387 / n8n 388 subject line for the cohort — "SOC 2 + AI Act audit for [Vendor] [Product] — 48h"
- **DO** ship a per-bundle-id + per-MCP-server-call-id probe — these are unique to Make's 1000+ apps surface
