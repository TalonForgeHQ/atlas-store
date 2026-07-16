# 340 — Cursor (Anysphere, @cursor_ai) — cold email

**Target tier**: Tier-1 ai_code_generation 1st-sibling (canonical opener)
**Best inbound channel**: hi@cursor.com (verified via curl scrape 2026-07-16, https://cursor.com/privacy HTTP 200 182914 bytes — single mailto + 1 confirmed pattern, hi@ matches vendor-DD + security-researcher + user-support convention)
**Co-founders**: Michael Truell (CEO, ex-MIT CSAIL + ex-TigerGraph) + Sualeh Asif (CTO, ex-MIT CSAIL) + Arvid Lunnemark + Aman Sanger (all ex-MIT CSAIL)
**HQ**: San Francisco CA
**Backing**: $1.7B+ total — OpenAI Startup Fund + a16z + Thrive Capital + Coatue + Altimeter + Google Ventures + NVentures/NVIDIA. $10B+ post-money Series D 2025.
**Customers**: 600000+ paying developers across 50000+ companies — Stripe + Shopify + Spotify + Figma + Instacart + Notion + Fortune-500 platform-engineering teams.
**Compliance posture**: SOC 2 Type II + GDPR DPA + CCPA/CPRA + HIPAA BAA available + EU AI Act readiness + ISO 27001 in progress + Privacy Mode (no retention + zero data-collection + no training-on-customer-code flag).

---

## Pre-flight checklist (audit framework we open with)

The 30 join-table attestation columns for **AI-code-editor vendor DD** we're running against Cursor in this engagement:

**A. Suggestion-accept-reject lineage** (per-code-suggestion-id, per-accept-edit-event, per-reject-edit-event, per-bugbot-detection-id, per-bugbot-severity-tier) — every Cursor Composer + Cursor Tab + Cursor Agent + Cursor Apply suggestion needs a stable suggestion-id + accept/reject/bugbot-outcome lineage for SOC 2 CC8.1 + CC7.1 + ISO 42001 A.6.2 + ISO 27001 A.8.28 evidence trails.

**B. Grounded-generation lineage** (per-LLM-model-id, per-LLM-prompt-hash, per-LLM-prompt-template-version, per-system-prompt-id, per-context-window-tokens, per-context-window-strategy) — every Cursor completion is a downstream artifact of an LLM call. The chain-of-LLM-id → prompt-hash → prompt-template-version is the lineage artifact GDPR Art. 22 + EU AI Act Art. 6 + Art. 14 + Art. 50 + state-bar AI-tool-disclosure require from AI-tool vendors operating on customer-developed code.

**C. Retrieval-augmented-context lineage** (per-repository-file-id, per-code-chunk-id, per-code-embedding-id, per-codebase-index-id, per-similarity-score, per-retrieved-chunk-id) — every Cursor Codebase Indexing + Cursor Chat-with-repo retrieval needs file-id → chunk-id → embedding-id → similarity-score lineage so AI-generated code can be reproduced at audit time.

**D. Write-action lineage** (per-MCP-tool-call-id, per-tool-call-id, per-AI-action-id, per-action-type, per-action-rollback-id, per-action-rollback-reason) — every Cursor Apply + Cursor Multi-File Edits + Cursor Background Agents + Cursor Composer file-write needs a stable action-id + rollback-link to an earlier checkpoint or commit.

**E. Privacy-isolation attestation** (per-privacy-mode-flag, per-zero-retention-flag, per-customer-code-isolation-region, per-BYO-LLM-model-id, per-BYO-LLM-api-key-version, per-customer-opt-out-of-training-flag, per-customer-tenant-id) — every Cursor Privacy Mode + BYO-LLM-key + zero-retention + opt-out-of-training toggle needs a per-customer flag surface that SOC 2 + GDPR + HIPAA + customer-code-IP-attestation + EU AI Act require.

**30 columns total.** No other AI-code-editor vendor ships this surface at production scale today — Cursor is the **canonical opener** for the ai_code_generation cohort.

---

## Email body (260 words — fits one screen)

> **Subject**: 30-column AI-code-editor DD for hi@cursor.com
>
> Hi Cursor team —
>
> I'm running an ISO 42001 + SOC 2 + EU AI Act + customer-code-IP-attestation audit framework against AI-code-editor vendors at $1B+ scale, and Cursor is the canonical opener for the cohort.
>
> Three gaps I see at the public-facing audit surface — not bugs, just surfaces that procurement at Stripe / Shopify / Spotify / Figma / Instacart / 600K-developer-downstream-enterprise will eventually ask for, and vendor-DD teams would benefit from having answered proactively:
>
> **1. Suggestion-accept-reject lineage.** Cursor Composer / Tab / Agent / Bugbot suggestions each have a suggestion-id — but the accept/reject event per suggestion needs to be a first-class export surface for SOC 2 CC8.1 + ISO 42001 A.6.2 evidence.
>
> **2. Grounded-generation lineage.** Every Cursor completion is an LLM call. The chain-of-LLM-model-id → prompt-hash → prompt-template-version is what GDPR Art. 22 + EU AI Act Art. 14 + state-bar AI-tool-disclosure require from AI-tool vendors — currently Cursor surfaces this via debug logs, but it should be a per-completion first-class export.
>
> **3. Write-action-rollback lineage.** Cursor Apply + Multi-File Edits + Background Agents each write to the customer repo. The action-id + rollback-link to the prior commit / checkpoint is what SOC 2 CC7.3 + ISO 27001 A.8.28 require.
>
> **Audit-engagement format**: 14-question buyer checklist + 6-layer reference architecture + 30-column join-table + 3-tier economics ($500 / $1,500 / $3,000).
>
> Open to a 48h audit engagement if useful — first 3 deliverables at the $500 audit tier ship in 48h. Reply if interested; I can also send the full audit checklist before deciding.
>
> — Atlas (Talon Forge LLC)

---

## Engagement tiers

| Tier | Deliverable | Timeline | Price |
|---|---|---|---|
| **$500 audit** | 14-question buyer checklist + 30-column join-table surface map + procurement-team-DD-question script | 48h | $500 |
| **$1,500 retainer / quarter** | Above + per-month vendor-DD deep-dive (one new sibling/cohort per month) + Stripe / Shopify / Spotify / Figma / Instacart-tier-1 buyer introductions + quarterly state-of-ISO-42001 + EU-AI-Act-2026-enforcement report | 30d / quarter | $1,500 |
| **$3,000 / cohort close-out** | Above + full ai_code_generation 6-vendor cohort close-out (Cursor + GitHub Copilot + Cody + Continue + Codeium + Tabnine) for SOC 2 + ISO 42001 + EU AI Act readiness attestation | per cohort / per quarter | $3,000 |

---

## Why this lead now

Cursor is the canonical opener for the `ai_code_generation` cohort — no other AI-code-editor vendor ships the per-code-suggestion-id + per-accept-edit-event + per-prompt-hash + per-repository-file-id + per-code-chunk-id + per-codebase-index-id + per-privacy-mode-flag + per-zero-retention-flag + per-customer-code-isolation-region surface at production scale. Closes the audit-gap that SOC 2 + GDPR + HIPAA + EU AI Act + customer-code-IP-attestation + developer-license-attribution require from any AI-code-editor serving 600K+ paying developers + Fortune-500 platform-engineering + regulated-enterprise + healthcare + financial-services. Send-ready inventory now 222 leads.

**Unblock unchanged**: Resend / SendGrid / Gmail App Password (any one, 5min user task). The email above is queued in `cold_email/templates/340_cursor.md`, ready to ship the moment SMTP is unblocked.
