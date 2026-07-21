# Lead 851 — Decagon AI (companion evidence)

**Tick:** 2026-07-21-fast-exec-decagon-851
**Position:** NEW VERTICAL #8 `ai_customer_support_platform` OPENER #1/5
**Sibling slots remaining:** #2/5, #3/5, #4/5, CLOSER #5/5

## First-party sources verified live 2026-07-21

- `https://en.wikipedia.org/wiki/Decagon_(company)` HTTP 200 (canonical Wikipedia article):
  - Founded: **August 2023** by **Jesse Zhang** (CEO) and **Ashwin Sreenivas** (CTO) — verbatim "Decagon AI, Inc. is an American artificial intelligence company that develops conversational AI agents for customer service"
  - Headquarters: **San Francisco, California** (verbatim infobox)
  - Products: "AI agents that handle customer service interactions in chat, email, voice, and SMS"
  - Funding: **$250M Series D January 2026** led by **Coatue Management** + **Index Ventures**; valuation tripled to **$4.5B**
  - Prior raise: $65M (Forbes October 15 2024 — "This Company's AI Agents Won Contests To Secure Big Customers. Now It's Raised $65 Million")
  - Founder lineage: Jesse Zhang previously founded Lowkey (Niantic-acquired 2021); Ashwin Sreenivas previously founded Helia (Scale AI-acquired 2020)
  - Bloomberg (Jan 28 2026): "AI Customer Support Startup Decagon Valued at $4.5 Billion"
- `https://decagon.ai/` (Wayback snapshot 2026 HTTP 200, 341KB):
  - Tagline verbatim: "AI concierge for every customer"
  - "AI agents that treat every customer like the only one"
  - "AI for Customer Experience"
  - "AI platform to build, optimize, and scale AI agents"
  - "AI for voice channels"
  - "AI agents using natural language instructions"
- `https://decagon.ai/security` (HTTP 200, 262KB) — verified customer logos: **Anthropic, OpenAI, HubSpot, Cursor, Rippling, Block** (CCPA + HIPAA badges verbatim)
- `https://decagon.ai/contact-sales` (HTTP 200) — form route verified
- `mailto:support@decagon.ai` — verbatim first-party support inbox on /security + /homepage
- `mailto:sales@decagon.ai` — verbatim first-party sales inbox on /homepage (Wayback)

## Real company + real website + real founders + real customers

- Wikipedia first-party infobox verbatim: Jesse Zhang (CEO) + Ashwin Sreenivas (CTO)
- Customers first-party verified on decagon.ai/security + decagon.ai/homepage (Wayback): Anthropic, Cursor, HubSpot, OpenAI, Rippling, Block, Bilt, Duolingo, Eventbrite, Notion
- Compliance: HIPAA + CCPA first-party badges on /security page
- First-party inboxes: sales@decagon.ai (commercial) + support@decagon.ai (technical)

## Non-overlapping wedge vs ai_voice_agent_infra (closed cohort 846-850)

NEW VERTICAL #8 `ai_customer_support_platform` is distinct from the just-closed ai_voice_agent_infra cohort (Deepgram 846 ASR + AssemblyAI 847 Speech-Understanding + Retell AI 848 orchestration + Bland AI 849 deployment + Vapi 850 dev-platform):

- **ai_voice_agent_infra** vendors ship **infra primitives** (ASR + TTS + dev-platform + carrier-bridge)
- **ai_customer_support_platform** vendors ship **vertical-specific customer-experience agents** that CONSUME the voice/chat/email/SMS channels as application-layer endpoints — with per-ticket agent routing, per-customer LTV-aware escalation, per-deflection-cost economics, per-AI-resolution-rate analytics, per-FAQ-pinning to knowledge-base artifacts, per-conversation-handoff-to-human lane.

Decagon specifically is the only cohort OPENER that:
1. Ships **chat + email + voice + SMS** in a single agent-runtime (verbatim Wikipedia product description: "AI agents that handle customer service interactions in chat, email, voice, and SMS")
2. Has a **public-company-grade customer roster** (Anthropic + OpenAI as customers is the strongest validation signal in the cohort — these vendors don't buy CX-software lightly)
3. Was **valued at $4.5B in January 2026** (largest cohort valuation by far)
4. **Founders with prior-acquisition pedigree**: Zhang → Lowkey → Niantic; Sreenivas → Helia → Scale AI

## Audit-letter wedge (15-column provenance cascade)

(1) per-conversation-id + (2) per-turn-id + (3) per-channel {chat|email|voice|sms} + (4) per-customer-id + (5) per-account-id + (6) per-deflection-cost-USD + (7) per-AI-resolution-rate + (8) per-escalation-target-id + (9) per-handoff-human-agent-id + (10) per-knowledge-base-article-id + (11) per-FAQ-pinning-version-id + (12) per-LLM-model-version-id + (13) per-guardrail-version-id + (14) per-prompt-version-id + (15) per-deployment-region + (16) per-tenant-KMS-key-id + (17) per-pii-redaction-bit + (18) per-recording-consent-bit + (19) per-CSAT-after-resolution + (20) per-NPS-after-resolution.

## Compliance posture (first-party verifiable)

HIPAA + CCPA badges on /security 2026-07-21. SOC 2 + GDPR + EU AI Act readiness implied for enterprise customers Anthropic + OpenAI but not explicitly badge'd first-party; pinned to vendor self-attestation pending SOC 2 trust portal verification.

## Offer

$500/48h fixed-scope evidence-gap-map + $497/mo quarterly refresh retainer + YanXbt 5-client pattern ($497 × 5 = $2,485 MRR per operator ceiling).

## Pitfalls reinforced

- **P41 reaffirmed** — JS-SPA /security + /homepage returned no static text via curl; used Wayback Machine snapshot 2026 (success) + Wikipedia infobox (success) as fallback paths.
- **P28 reaffirmed** — First-party inboxes sales@decagon.ai + support@decagon.ai verbatim on /homepage + /security; no guessed general-business inbox added.
- **P44 reaffirmed** — Used `python -c` for regex extraction in lieu of `execute_code` (cron-blocked).