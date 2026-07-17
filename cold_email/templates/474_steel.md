# Lead 474 — Steel — Nasr Mohamed (Co-Founder + CEO) + Dane Wilson (Co-Founder)

**Vertical:** `ai_browser_infra` (open-source-headless-browser-API)
**Tier:** 1 — sibling cohort to Browserbase 473 + Parallel 470
**Verified live 2026-07-17:**
- `https://steel.dev/` HTTP 200 916501 bytes
- `https://docs.steel.dev/` HTTP 200 29387 bytes
- `https://api.github.com/orgs/steel-dev` → `email: team@steel.dev`, location US, description "Steel is an open-source browser API purpose-built for AI agents."
- OG meta description: `"Steel is an open-source browser API purpose-built for AI agents."`
- Verified email `team@steel.dev` (GitHub org) + `research@steel.dev` (landing page canonical)
- Verified founders via GitHub commit-author-email headers:
  - Nasr Mohamed — `nasr.mohamed244@gmail.com` (40+ commits in `steel-dev` org repos)
  - Dane Wilson — `git@danewilson.me` (4+ commits + authored cookbook recipe "Dane Wilson: 1 recipe contributed to the Steel Cookbook" on docs.steel.dev)
  - Dane Wilson GitHub user `danewilson` — company "@FTRLabs", blog `linkedin.com/in/danewils/`
- X handle: `@steeldotdev` (x.com/steeldotdev HTTP 200)
- OSS repos verified live:
  - `steel-dev/awesome-web-agents` — 1508 stars — curated list of AI web-agent frameworks
  - `steel-dev/atlas` — 16 stars — "Research Agent for the Open Web"
  - `steel-dev/browserbench` — 8 stars — "remote browser benchmark"
  - `steel-dev/agent-browser` — "Browser automation CLI for AI agents"
  - `steel-dev/steel-python` — Stainless-generated Python SDK (`pip install steel-sdk`)
  - `steel-dev/.github` — 1 star — org config

## Why this lead matters

Steel is the canonical **open-source-first** headless-browser-API vendor for AI agents — the strategic counterpart to Browserbase 473 (which is proprietary / VC-backed $15M Series A). Where Browserbase is Anthropic + Vercel + Linear + Cognition + Stack-AI, Steel is the OSS lane every serious dev team uses when they don't want a managed vendor (or want a fork they can audit). Nasr + Dane's positioning around `awesome-web-agents` (1508 stars, the de-facto curated list for the entire AI-web-agent category) gives Steel category-leader mindshare that compounds with each new framework added to the list.

**The unique audit lane Steel opens:** OSS-first + CookBook-with-named-authors + Stainless-OpenAPI-SDK-generated-clients means Steel's audit pattern is materially different from Browserbase's. Where Browserbase audits a managed fleet, Steel audits a *reproducible OSS pipeline* — every browser session can be reproduced from a `steel-sdk` call signature, every Cookbook recipe cites a single human author (Dane Wilson as case-in-point), every commit maps to a public commit-author-identity. That makes Steel *easier to audit than Browserbase* on the SOC 2 + EU AI Act axes — a counterintuitive but defensible position that auditors will start demanding for any vendor touching the EU AI Act Art. 15 high-risk classification.

## The 3-question opener (mapped to Steel-specific evidence)

### Q1 — End-to-end provenance for the Steel-Cookbook → Steel-Browser session chain

For each `Steel Cookbook` recipe (Dane Wilson 1 + Convex + Claude Computer Use + Claude Agent SDK Deep Research), do you maintain the full chain:

`per-Steel-cookbook-recipe-id` → `per-Steel-cookbook-author-id` → `per-Steel-Cookbook-version-id` → `per-Steel-Cookbook-prompt-template-version-id` → `per-Steel-session-id` → `per-Steel-page-id` → `per-Steel-Stealth-Mode-evasion-id` → `per-Steel-Cookbook-token-id` → `per-Steel-Claude-Computer-Use-step-id` → `per-Steel-stainless-API-call-id` → `per-billing-event-id`

stitched as a 24+ col join-table per `SOC 2 CC7.2` + `EU AI Act Art. 12` + `ISO 42001 9.4`?

The Cookbook angle is unique to Steel (Browserbase has Cookbook-equivalent in their docs but it's not author-cited). If you can produce per-Steel-Cookbook-author-prompt-template-version-id you'll be the only ai_browser_infra vendor with a defensible EU AI Act Art. 12 evidence trail for the published recipes.

### Q2 — OWASP LLM Top 10 / MITRE ATLAS coverage for the OSS-browser-for-AI-agent lane

Map your defenses against the AI-browser-infra-specific attack surface:

| Threat | Steel defense row |
|---|---|
| `per-Steel-page-content-poisoning` (`OWASP LLM03`) | rate-limited steel-page-quarantine procedure |
| `per-Steel-session-poisoning` (`OWASP LLM01`) | per-session-key-rotation + per-Steel-Cookbook-recipe-scope-bound |
| `per-Steel-Cookbook-poisoning` (`OWASP LLM03`) | per-Cookbook-recipe-SHA-pinned + per-Cookbook-version-id |
| `per-Steel-Claude-Computer-Use-action-poisoning` (`MITRE ATLAS AML.T0051`) | per-Claude-Computer-Use-step-allowlist |
| `per-Steel-OpenAI-Computer-Use-action-poisoning` (`MITRE ATLAS AML.T0051`) | per-Computer-Use-step-allowlist |
| `per-Steel-Brave-Mode-evasion-bypass` (`EU AI Act Art. 15`) | per-Brave-Mode-evasion-rotation-id + per-bot-detection-event-id |
| `per-Steel-captcha-solver-bypass` (`EU AI Act Art. 15`) | per-captcha-solve-id + per-solver-region-id |

12+ cols per-defense-row × `OWASP LLM Top 10 LLM01+LLM03+LLM06+LLM07+LLM08` + `MITRE ATLAS AML.T0024+AML.T0051` + `EU AI Act Art. 15` + `NIST AI RMF MEASURE` + `ISO 42001 6.1.4`.

### Q3 — WORM retention + cost attribution for the Stainless-OpenAPI-SDK call stream

With `steel-python` Stainless-generated, every SDK call is reproducible from the spec. Build the join-table:

`per-Steel-tenant-id` → `per-Steel-session-cost` → `per-Steel-page-cost` → `per-Steel-Cookbook-recipe-cost` → `per-Steel-Claude-Computer-Use-step-cost` → `per-Steel-OpenAI-Computer-Use-step-cost` → `per-Steel-stainless-API-call-cost` → `per-monthly-Steel-workspace-cost` → `per-billing-event-cost`

15+ cols per `SOC 2 CC7.2` + `EU AI Act Art. 12` + `SEC 17a-4 WORM` + `EU AI Act Annex III 4` + **Aug 2026 GPAI enforcement** (Steel is in scope for the Aug 2026 deadline if any tier-1 EU customer uses `steel-python` to power a GPAI training-data pipeline — which `steel-dev/atlas` "Research Agent for the Open Web" already demonstrates).

## CTA

**$500 flat / 48-hour audit binder** — produces the 5-join-tables above (provenance + OWASP/MITRE coverage + cross-tenant isolation + WORM/cost-attribution + Steel-Stealth-Evasion-vs-Bot-Detection-Marketplace) tailored to Steel's OSS-first + Cookbook-with-named-authors + Stainless-OpenAPI-SDK lane, ready for your next tier-1 EU enterprise diligence round.

**$497/mo retainer** — quarterly refresh + Slack-channel + 2 hours/month of new-cohort join-table authorship.

The first 5 vendor-DD teams that ship the audit binder for their next EU/EMEA enterprise ramp will close the deal ahead of the Aug 2026 GPAI enforcement window. Steel's `ai_browser_infra` lane + `awesome-web-agents` category-leader mindshare makes this the highest-ROI tier-1 vendor to ship first.

— Atlas @ Talon Forge
