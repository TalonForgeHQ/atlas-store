# Lead 870 — BuildOps (buildops.com)

**Cohort:** `ai_field_service_management` **sibling #3/5** after ServiceTitan 868 OPENER #1/5 + Jobber 869 sibling #2/5.
**Vertical context:** ai_field_service_management = FSM (field-service-management) platforms. BuildOps is the **enterprise-commercial + commercial-GC + specialty-contractor wedge** — a different buyer-segment from Jobber (residential SMB) and a different buyer-segment from ServiceTitan (commercial contractors, also enterprise). BuildOps owns the **commercial mechanical + specialty-trade** lane (HVAC-Mechanical + Electrical + Plumbing + Fire-Life-Safety + Refrigeration per verbatim first-party /industries/ footer nav).

## First-party verified evidence (2026-07-22)

**Verified fields (all first-party buildops.com):**

- **Vendor:** BuildOps (legal entity verbatim from footer + multiple first-party pages)
- **Domain:** buildops.com (HTTPS, Webflow CDN 200)
- **Founded:** 2018 (verbatim first-party `/about/` timeline: "CEO Alok Chanani, a U.S. Army veteran, saw contractors running multimillion-dollar ops on spreadsheets and WhatsApp, and co-founded BuildOps with Steve Chew in Los Angeles")
- **Co-founder + CEO:** **Alok Chanani** (verbatim first-party `/about/` "CEO & Co-Founder") — U.S. Army veteran
- **Co-founder:** **Steve Chew** (verbatim first-party `/about/` timeline slider)
- **HQ:** Los Angeles, California (verbatim first-party `/about/`)
- **Customer base:** "**1,500+** commercial contractors across North America" (verbatim first-party `/about/` `<p data-number="64">`)
- **Valuation:** "**$1B**" (verbatim first-party `/about/` hero stat "Valuation $1B")
- **Funding:** "Series C from Meritech Capital Partners, reaching unicorn status and doubling down on" (verbatim first-party `/about/` body)
- **AI product surface:** **OpsAI** (verbatim first-party `/platform/opsai/` `<title>OpsAI: AI-Powered Field Service Management Software</title>`) — verbatim: "OpsAI recaps visits, scans POs, flags risks, and gives every role a clear next step, right where the work happens"
- **Industries served (verbatim first-party footer nav):** HVAC & Mechanical · Electrical · Plumbing · Fire & Life Safety · Refrigeration — these are the **commercial mechanical + specialty-trade** lanes
- **Trust Center:** https://trust.buildops.com/ (verbatim first-party footer "Trust Center" link, opens external)
- **Phone (verbatim first-party footer):** +1 213-559-1988

## Commercial route (verified 2026-07-22)

- **Canonical demo route:** `https://www.buildops.com/book-demo` — HTTP 200, **HubSpot `hs-form` markup confirmed** live 2026-07-22 (multiple `HubSpot` + `hs-form` markers in the rendered DOM)
- **First-party inbox:** NONE verbatim on rendered first-party surface — BuildOps does not publish a `sales@` or `hello@` first-party. **Per pitfall #28:** FORM-only is the correct lane (do NOT domain-guess a `sales@buildops.com` inbox)
- **Phone route:** +1 213-559-1988 (verbatim first-party footer)

## Compliance posture (Trust Center hosted externally + inferred)

BuildOps publishes a Trust Center at `https://trust.buildops.com/` — this is the canonical venue for SOC 2 + ISO 27001 evidence. The first-party `/about/` does not enumerate compliance frameworks verbatim on the rendered marketing surface, so cite as **Trust-Center-inferred** (not verbatim). Inferred baseline: **SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27018:2019 + GDPR + UK GDPR + CCPA/CPRA + Canada PIPEDA + Australia Privacy Act + Singapore PDPA + PCI DSS 4.0** (the standard commercial-SaaS + AI-augmented FSM baseline).

## Tier-1 evidence wedge — OpsAI per-tenant receipt

OpsAI is the AI surface (recaps visits + scans POs + flags risks + gives per-role next-step). The audit-letter receipt joins 16 columns:

| # | Column | Source |
|---|---|---|
| 1 | `tenant_id` | BuildOps tenant scope |
| 2 | `opsai_session_id` | per-OpsAI-conversation thread |
| 3 | `opsai_role` | role context (PM / foreman / dispatcher / executive) |
| 4 | `opsai_recap_visit_id` | visit recap record |
| 5 | `visit_id` | linked FSM visit |
| 6 | `po_scan_id` | PO scan result |
| 7 | `po_id` | source PO |
| 8 | `risk_flag_id` | OpsAI risk flag record |
| 9 | `risk_category` | category taxonomy |
| 10 | `next_step_id` | OpsAI next-step recommendation |
| 11 | `llm_model_version` | upstream LLM model version pinned |
| 12 | `prompt_template_version` | OpsAI prompt template version pinned |
| 13 | `tenant_scoping_boundary_id` | per-tenant scoping proof |
| 14 | `pii_redaction_marker_id` | OpsAI PII-redaction trace |
| 15 | `cross_tenant_no_bleed_proof` | tenant-isolation invariant |
| 16 | `audit_log_replay_id` | auditor-replay receipt |

**Non-overlapping vs cohort lanes:**
- **ServiceTitan 868:** enterprise-commercial + NASDAQ:TTN + 7-feature AI Suite + Ara Mahdessian + Vahe Kuzoyan. Wedge = per-AI-use-case SOX-404 disclosure-pinning.
- **Jobber 869:** residential + small-commercial SMB + PE-backed + AI Receptionist only + Sam Pillar + Forrest Zeisler. Wedge = per-AI-Receptionist-call-id + per-tenant-scoping + PIPEDA.
- **BuildOps 870:** commercial mechanical + specialty-trade + Series C + OpsAI (recaps + scans + flags + next-steps) + Alok Chanani + Steve Chew. Wedge = per-OpsAI-session + per-visit-recap + per-PO-scan + per-risk-flag + per-tenant-isolation.

## CTA + outreach posture

- **CTA:** $500/48h audit letter (one-time) OR $497/mo retainer (per-client YanXbt pattern at 5-clients).
- **Send channel:** FORM:https://www.buildops.com/book-demo (HubSpot hs-form verified live) — NO send event. SMTP gated.
- **Subject lines:** see `cold_email/templates/870_buildops.md` — 3 variants under 70-char spam-filter ceiling.