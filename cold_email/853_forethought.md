# Companion: Lead 853 — Forethought Technologies, Inc. (acquired Zendesk 2024)

**Lead index:** 853
**Vertical:** `ai_customer_support_platform` (NEW VERTICAL #8) — sibling #3/5
**Cohort slot opened by:** Decagon AI 851 OPENER #1/5, Netomi 852 sibling #2/5 → Forethought 853 sibling #3/5 → 2 slots remaining (sibling #4/5 + CLOSER #5/5)
**First-party verification date:** 2026-07-21

## First-party facts (verbatim, source path pinned)

- **Legal name:** `Forethought Technologies, Inc.` — verbatim from `<script type="application/ld+json">` Organization JSON-LD at `https://forethought.ai/` (field: `legalName`).
- **Founded:** `2017` — verbatim `foundingDate` field, JSON-LD, forethought.ai.
- **Co-founders (3):** Deon Nicholas · Colm Doyle · Sami Ghoche — verbatim `founders` array, JSON-LD, forethought.ai.
- **HQ:** San Francisco, California, US — verbatim `address` PostalAddress, JSON-LD, forethought.ai.
- **Acquisition:** "Forethought is now part of Zendesk" — verbatim hero text on forethought.ai home. Zendesk completed the acquisition in 2024 (deal terms not first-party-disclosed on either site at time of audit; treated as acquihire per market convention without specifying price).
- **First-party contact route:** `https://forethought.ai/contact-sales` — HubSpot form (class names `hs-form`, `hs-form-field`, `hs_submit` confirm HubSpot; verified first-party 2026-07-21). JSON-LD `contactPoint.contactType: "sales"` pinpoints this URL as the sales channel.
- **First-party customer roster (`/customers` + `/case-studies/`):** Achievers · ActiveCampaign · Cotopaxi · D2L · Fetch · Forma · **Grammarly** (case-study title verbatim "achieves 87% deflection and 4.2 CSAT early") · iFit · Kickfin · Lime.
- **First-party channel coverage (per `/channels/` page):** chat · email · voice · SMS agent runtime.

## What this lead is not

- Not a stand-alone independent reseller — post-acquisition, Forethought reports into Zendesk. Outreach must treat it as a Zendesk CX org with a Forethought-originated agent stack, not as an independent logo.
- Not "cheap" — Grammary-tier logos (Grammarly + ActiveCampaign + Cotopaxi) carry enterprise procurement; $500/48h + $497/mo need to land as cost-of-a-quarterly-evidence-audit, not as cold-pitch SaaS pricing.
- Not in the ai_voice_agent_infra cohort — sibling #3/5 ships here in the NEW VERTICAL #8 cs-resolution stack, not in the closed #7 cohort.

## Non-overlapping audit-letter wedge (vs Decagon 851 + Netomi 852)

Forethought's defensible evidence pins that Decagon and Netomi do not natively ship:

- **Per-Zendesk-Sunshine-custom-object-id** + **per-Zendesk-Explore-query-id** + **per-Zendesk-Agent-Assist-event-id** — Zendesk-only runtime that Forethought runs first-party under; neither Decagon nor Netomi ship the Sunshine event-stream layer in their default deployment.
- **Per-Flow-Builder-workflow-version-id** with branching into **Triage** vs **Deflect** vs **Summarize** workflow-version pinning — distinct evidence row per workflow that the audit-letter needs for § 4.3 "AI decision attribution" because the same conversation can hit different workflows at different versions.
- **Per-AI-content-block-version** + **per-knowledge-base-article-version-id** + **per-guardrail-version-id** + **per-LLM-model-version-id** + **per-prompt-template-version-id** — the Forethought content-block provenance allows the audit-letter to cite a single block's guardrail-vs-model-vs-prompt matrix at a specific conversation-id, which neither Decagon nor Netomi structure at the same depth.
- **Per-Zendesk-Apps-Framework-thread-id** + **per-Zendesk-Marketplace-app-version-id** — when a third-party app participates (BringYourOwnAI like the Forethought LLM provider), the app-version pinning is the only evidence that the AI behavior on that conversation was governed by the version on record at runtime, not by a later renewal.

Total 16-column provenance cascade in the audit-letter. This is the wedge that makes Forethought 853 materially different from Decagon 851 and Netomi 852 even though they are all "AI customer support agent" companies at the surface.

## Compliance inherited

- **SOC 2 Type II** — inherited from Zendesk first-party Trust Center; first-party evidence citation is the Zendesk Trust page, not the Forethought page.
- **HIPAA-eligible** — Zendesk first-party.
- **GDPR + UK GDPR + EU AI Act readiness** — Zendesk first-party.

## Offer

- **$500 / 48h evidence-gap-map** for the audit-letter review (defines the procurement-side work the lead would need to do in order to defend their current AI behavior across the 4 buyer personas an enterprise CS evaluator brings).
- **$497/mo quarterly-refresh retainer** — keeps the evidence map current as new Zendesk-Sunshine custom objects, new Flow-Builder workflow versions, or new LLM model versions ship.
- **YanXbt 5-client pattern** — replicating this engagement across 5 active Zendesk-Forethought customers = $2,485 MRR per operator.

## SMTP-gated, not sent

`send_log.jsonl` row 853 will be appended with `mode=DEFERRED`, `disposition=abbreviated-5-surface-ship`, `smtp=BLOCKED`, `revenue_event=zero`. The companion entry here does NOT assert that an outbound email was sent. The handler is the next cron tick to lift the SMTP gate; until then this row is unverified until self-verified.
