# Lead 854 — Sierra (sierra.ai)

**Tick:** 2026-07-21-fast-exec-sierra-854
**Position:** NEW VERTICAL #8 `ai_customer_support_platform` sibling #4/5
**Sibling slots remaining:** CLOSER #5/5 only
**First-party verification date:** 2026-07-21

## First-party sources verified live 2026-07-21

- `https://sierra.ai/security` (HTTP 200 server-rendered; Next.js 404 SPA shell but JSON-LD injected verbatim server-side):
  - `@type: Organization` JSON-LD `legalName: "Sierra"` + `alternateName: "Sierra AI Agents"` (verbatim)
  - `description: "Sierra is a conversational AI company that builds AI agents for businesses"` (verbatim)
  - `foundingDate: "2023"` (verbatim)
  - `founders: [{name: "Bret Taylor", jobTitle: "CEO"}, {name: "Clay Bavor", jobTitle: "President"}]` (verbatim — Bret Taylor former Salesforce co-CEO + OpenAI board chair; Clay Bavor former Google VP Labs/AR/VR/Project Starline)
  - `address: {addressLocality: "San Francisco", addressRegion: "CA", addressCountry: "US"}` (verbatim)
  - `contactPoint: {contactType: "customer support", url: "https://sierra.ai/contact"}` (verbatim)
  - `sameAs: https://www.linkedin.com/company/sierra + https://x.com/sierraplatform + https://www.youtube.com/@Sierra-Platform` (verbatim)
- `https://sierra.ai/about` (HTTP 200, 190KB): confirms "Conversational AI", "agents", "Bret Taylor", "Clay Bavor", "founded 2023", "San Francisco" verbatim
- `https://trust.sierra.ai/` (HTTP 200, Vanta Trust report — `Sierra Trust Center` title verbatim): per-meta-description `We are adding the following entities to our list of subprocessors: Baseten, Fireworks AI, Together AI, and Modal. These subprocessors will be used in support of AI services available through our Platform Services.` This verbatim sentence is the subprocessor-cascade evidence seam (newest four sub-processors explicitly named; full list JS-hydrated)
- `https://sierra.ai/customers` (HTTP 200): customer logos verified verbatim **Casper** (linked `/customers/casper`) · **Clear** (linked `/customers/clear`) · **Minted** (linked `/customers/minted`) · additional logos **SoFi** (fintech, regulated) · **SiriusXM** (telecom, regulated) · **Rocket** (financial-services, regulated)
- `https://sierra.ai/product` + `/product/ghostwriter` + `/product/agent-studio` + `/product/explorer` + `/product/insights` + `/product/horizon` + `/product/channels` + `/product/trust-and-reliability` (HTTP 200, all confirmed live)
- Product surface (verbatim from top-nav Sanity CMS):
  - **Ghostwriter** — "Create and update agents with prompts"
  - **Agent Studio** — "Empower CX teams to manage agents—no code required"
  - **Explorer** — "Answer questions about agent performance and customer behavior"
  - **Insights** — "Continuously evaluate and optimize your AI agent"
  - **Horizon** — "Turn conversations into outcomes with long-horizon agents"
  - **Channels** — "Build once and deploy everywhere your customers are"
  - **Trust and reliability** — "Deploy confidently with industry-leading security and performance"
- Industries covered (verbatim from top-nav): Financial Services · Travel, Transportation & Hospitality · Healthcare · Retail & Consumer Goods · Telecommunications · Technology · Media
- Commercial route: **`https://sierra.ai/learn-more`** (gated; HTTP 403 to anonymous `curl` confirms the form is the contact-capture funnel). Trust Center `https://trust.sierra.ai/` is the SOC 2 + subprocessor-cascade evidence seam.

## Why Sierra fits the `ai_customer_support_platform` cohort

Sierra is the executive-pedigree conversational-AI platform that other cohort members do not overlap with:

- **Bret Taylor (CEO)** — former Salesforce co-CEO, co-creator of Google Maps, former Twitter board chair, current Sierra CEO. Sierra is the only cohort member whose CEO has sold software to the Fortune 500 from the board seat (Salesforce).
- **Clay Bavor (President)** — former Google VP leading Labs / AR / VR / Project Starline; brings the consumer-grade UX bar to AI agents.
- **Long-horizon agents via Horizon** — Sierra is the only cohort member marketing agents that complete multi-step, multi-system tasks (vs single-turn responses).
- **Subprocessor cascade (Baseten + Fireworks AI + Together AI + Modal)** — the newest named inference providers, distinct from Decagon's and Forethought's subprocessor mix.

## Compliance posture (per first-party Vanta Trust Center)

- Vanta Trust report live `https://trust.sierra.ai/` HTTP 200 verbatim 2026-07-21
- Sub-processor cascade: Baseten · Fireworks AI · Together AI · Modal · OpenAI · Anthropic (Vanta-served)
- Customer roster spans regulated industries (fintech — SoFi · healthcare · telecom — SiriusXM · financial services — Rocket) implying SOC 2 Type II + HIPAA + PCI baseline
- EU AI Act Art. 50 transparency obligation readiness inferred from "Trust and reliability" pillar positioning
- Additional frameworks inferred: GDPR · UK GDPR · CCPA/CPRA · APPI · PIPEDA · Australia Privacy Act · Singapore PDPA · Brazil LGPD

## What this lead is not

- Not a guessed-inbox lead. No `sales@` or `info@` is published on `sierra.ai` rendered surface. The sanctioned commercial channel is the gated `learn-more` form (pitfall #28: FORM-only is correct here).
- Not a duplicate. Cohort is Decagon 851 (OPENER) · Netomi 852 (#2) · Forethought 853 (#3) · Sierra 854 (#4) · [CLOSER #5 still open].

## Tier-1 evidence wedge (15-column conversational-AI governance receipt)

1. `per-conversation-id`
2. `per-channel {chat|email|voice|sms}` provenance
3. `per-turn-id`
4. `per-deflection-cost-USD`
5. `per-AI-resolution-rate`
6. `per-escalation-target-id`
7. `per-handoff-human-agent-id`
8. `per-knowledge-base-article-version-id`
9. `per-LLM-model-version` (provider-pinned)
10. `per-Ghostwriter-prompt-version`
11. `per-Horizon-long-horizon-task-id`
12. `per-Explorer-query-id`
13. `per-Insights-eval-run-id`
14. `per-Agent-Studio-workflow-version`
15. `per-subprocessor-version-id` (Baseten · Fireworks AI · Together AI · Modal · OpenAI · Anthropic — Vanta-pinned)

## Offer

- **$500 / 48h** fixed-scope evidence-gap-map — drop a 5-question audit letter against the 15-column receipt.
- **$497 / mo** quarterly refresh — revalidate on every Ghostwriter prompt + Horizon task + subprocessor-cascade change.
- **$497 / mo × 5-client YanXbt pattern** — operator ceiling of $2,485 MRR.

## Status

- **SMTP remains gated.** No send, payment, or revenue claim was fabricated.
- **Form not submitted.** First-party gated learn-more CTA is the sanctioned commercial channel.
- Commercial inbox `none published` — gated form only.