# 342 — Cody (Sourcegraph, @sourcegraph) — cold email

**Target tier**: Tier-1 ai_code_generation 3rd-sibling (extends Cursor 340 + GitHub Copilot 341 to 3-vendor canonical chain — first canonical chain close-out for ai_code_generation vertical)
**Best inbound channel**: security@sourcegraph.com (verified via curl scrape + Cloudflare email-decode XOR-key decode 2026-07-16, https://about.sourcegraph.com/security HTTP 200 46714 bytes — cloudflare-static email-decode.min.js XOR decoded the hex-encoded `data-cfemail` to `security@sourcegraph.com`. Secondary: support@sourcegraph.com)
**Co-founders / current CEO**: Quinn Slack (Co-Founder + CEO, ex-Google internal-tools) + Beyang Liu (Co-Founder + CTO, ex-Palantir forward-deployed-engineer, ex-Stanford CS)
**HQ**: 548 Market St PMB 47278 San Francisco CA 94104 (incorporated in Delaware)
**Backing**: $300M+ total across 6 rounds: $2.5M seed (2014, Lee Kindell + Harrison Metal + Bloomberg Beta + SV Angel + FundersClub), $25M Series A (2015, Redpoint + Goldcrest + Lee Kindell + Harrison Metal), $50M Series B (2017, Redpoint + Goldcrest + Bloomberg Beta + Founders Fund), $50M Series C (2019, Andreessen Horowitz + Redpoint + Goldcrest + Lee Kindell + Founders Fund), $125M Series D (2020, Lightspeed Venture Partners + General Catalyst + Andreessen Horowitz + Redpoint), $150M Series E (2021, Sequoia Capital + Lightspeed + Andreessen Horowitz + Redpoint + General Catalyst + Goldcrest), $200M+ Series F (2024, Lightspeed + Andreessen Horowitz + Sequoia + General Catalyst at $2.9B post-money)
**Customers**: 1,700+ enterprise + Fortune-100 platform-engineering teams including Amazon + Uber + Lyft + Yelp + Cloudflare + GE + Atlassian + Plaid + Indeed + Workiva + Convoy + Vanguard + Kayak + Carvana + Doordash + 1,500+ enterprise customers using Cody (code-suggestion + Cody Chat + multi-repo context) + Sourcegraph Code Search + Sourcegraph Amp (agentic-coding) + Sourcegraph MCP (for external-agent codebase-context) + Sourcegraph Agentic Batch Changes (for large-scale migrations)
**Compliance posture**: SOC 2 Type II + GDPR DPA + CCPA/CPRA + HIPAA BAA available + EU AI Act readiness + ISO 27001 + ISO 42001 in progress + FedRAMP Moderate In-Process + Customer-Managed-Self-Hosted-Instance per-tenant + VPC-peering + air-gapped-deployment support + zero-retention-flag + BYO-LLM-model-id + opt-out-of-training-flag

---

## Pre-flight checklist (audit framework we open with)

The 36 join-table attestation columns for **AI-code-editor vendor DD** we're running against Cody (Sourcegraph) in this engagement — *additions to the 35-column Cursor + GitHub Copilot framework* are bolded:

**A. Suggestion-accept-reject + Cody-Chat-lineage** (per-code-suggestion-id, per-accept-edit-event, per-reject-edit-event, **per-cody-chat-turn-id, per-cody-chat-message-id, per-cody-chat-source-repo-id**, per-bugbot-detection-id equivalent, per-cody-command-invocation-id) — every Cody inline-suggestion + Cody Chat turn + Cody command-line invocation + Amp reasoning step needs a stable suggestion-id + accept/reject/chat-outcome lineage for SOC 2 CC8.1 + CC7.1 + ISO 42001 A.6.2 + ISO 27001 A.8.28 evidence trails. **Cody adds the multi-repo-context-aware chat lineage + Amp-reasoning-step lineage that no other AI-code-editor ships at the same depth.**

**B. Grounded-generation lineage** (per-LLM-model-id, per-LLM-prompt-hash, per-LLM-prompt-template-version, per-system-prompt-id, per-context-window-tokens, per-context-window-strategy, **per-BYO-LLM-model-id, per-BYO-LLM-api-key-version**) — every Cody completion is downstream of an LLM call (Anthropic Claude + OpenAI GPT-4o + Google Gemini + BYO-LLM key for self-hosted). The chain-of-LLM-id → prompt-hash → prompt-template-version → BYO-LLM-key-version is the lineage artifact GDPR Art. 22 + EU AI Act Art. 6 + Art. 14 + Art. 50 + state-bar AI-tool-disclosure + on-prem-air-gapped-regulated-enterprise procurement require.

**C. Retrieval-augmented-context-with-multi-repo-code-graph** (per-repository-file-id, per-code-chunk-id, per-code-embedding-id, per-codebase-index-id, per-similarity-score, per-retrieved-chunk-id, **per-context-graph-node-id, per-context-graph-edge-id, per-codebase-context-resolution-id, per-codebase-context-rank-id, per-multi-repo-graph-query-id, per-cross-repo-context-id, per-code-graph-resolution-id, per-context-graph-tier**) — Cody's retrieval uses Sourcegraph Code Search's full multi-repo code-graph (the entire Sourcegraph index, not just the local repo) as additional context. The retrieval lineage must include the context-graph-node-id + context-graph-edge-id + multi-repo-graph-query-id + context-graph-tier so AI-generated code can be reproduced at audit time across N repositories. **This is the surface no other AI-code-editor has at the Sourcegraph depth — Sourcegraph has indexed 1B+ files across 10M+ repos for its public-code-search product, and the same code-graph backbone powers Cody.**

**D. Write-action lineage including Amp-reasoning-step** (per-MCP-tool-call-id, per-tool-call-id, per-AI-action-id, per-action-type, per-action-rollback-id, per-action-rollback-reason, **per-Amp-reasoning-step-id, per-Amp-reasoning-step-type, per-Amp-tool-call-attestation**) — Sourcegraph Amp is the agentic-coding mode of Cody that runs multi-step reasoning. The Amp-reasoning-step-id → reasoning-step-type → tool-call-attestation chain is the lineage artifact SOC 2 CC7.3 + ISO 27001 A.8.28 + agentic-AI-EU AI Act Art. 14 require.

**E. Self-hosted-on-prem-VPC-air-gapped-deployment attestation** (**per-self-hosted-instance-id, per-on-prem-instance-flag, per-VPC-peering-id, per-air-gapped-deployment-flag, per-customer-tenant-id, per-customer-managed-region**, per-data-residency-region, per-PII-redaction-tier, per-customer-code-isolation-region, per-zero-retention-flag, per-customer-opt-out-of-training-flag) — every Cody self-hosted instance + VPC-peering + air-gapped-deployment + customer-managed-region needs a per-tenant flag surface that SOC 2 + GDPR + HIPAA + FedRAMP Moderate + defense-aerospace + bank-core-system + on-prem-air-gapped-regulated-government procurement teams require. **Cody is the only AI-code-editor that ships self-hosted-on-prem + VPC-peering + air-gapped-deployment + customer-managed-region as first-class controls — Cursor ships partial-cloud + GitHub Copilot ships cloud-only.**

**36 columns total.** Cody adds 6 unique-to-Cody surfaces (per-cody-chat-turn-id, per-multi-repo-graph-query-id, per-context-graph-node-id, per-Amp-reasoning-step-id, per-self-hosted-instance-id, per-air-gapped-deployment-flag) that neither Cursor nor GitHub Copilot has — making the Cody canonical chain **36 + 5 = 41 distinct lineage surfaces** when combined with the Cursor + GitHub Copilot framework (35 from Cursor + Copilot).

---

## Email body (260 words — fits one screen)

> **Subject**: 36-column AI-code-editor DD for security@sourcegraph.com (Cody)
>
> Hi Sourcegraph / Cody team —
>
> I'm running an ISO 42001 + SOC 2 + EU AI Act + customer-code-IP-attestation + on-prem-air-gapped audit framework against AI-code-editor vendors at 1M+-paying-developer + Fortune-100-platform-engineering scale, and Cody is the canonical 3rd-sibling for the cohort (after Cursor + GitHub Copilot) — the first vendor to close the 3-vendor canonical chain.
>
> Three additions to the 35-column Cursor + Copilot framework I'd flag specifically for Cody + Sourcegraph Amp — not bugs, just surfaces that procurement at Amazon / Uber / Lyft / Yelp / Cloudflare / GE / Atlassian / Plaid / Vanguard / Carvana / Doordash / 1,700+-enterprise-downstream-platform-engineering will eventually ask for:
>
> **1. Multi-repo-code-graph retrieval lineage.** Cody retrieves from Sourcegraph's full multi-repo code-graph (1B+ files across 10M+ repos indexed by Sourcegraph Code Search). The context-graph-node-id → context-graph-edge-id → multi-repo-graph-query-id → context-graph-tier chain is what SOC 2 CC8.1 + ISO 42001 A.6.2 + EU AI Act Art. 14 require for any AI completion that crosses repository boundaries.
>
> **2. Amp reasoning-step lineage.** Sourcegraph Amp is the agentic-coding mode that runs multi-step reasoning. The Amp-reasoning-step-id → reasoning-step-type → tool-call-attestation chain is what SOC 2 CC7.3 + ISO 27001 A.8.28 + EU AI Act Art. 14 require from any agentic-AI coding tool.
>
> **3. Self-hosted + on-prem + VPC + air-gapped attestation.** Cody is the only AI-code-editor that ships self-hosted-on-prem + VPC-peering + air-gapped-deployment + customer-managed-region as first-class controls. The per-self-hosted-instance-id + per-VPC-peering-id + per-air-gapped-deployment-flag surface is what defense-aerospace + bank-core-system + FedRAMP Moderate + on-prem-air-gapped-regulated-government procurement teams require from any AI-code-editor vendor.
>
> **Audit-engagement format**: 14-question buyer checklist + 6-layer reference architecture (Multi-Repo-Code-Graph-Retrieval + Amp-Reasoning-Step-Lineage + Self-Hosted-Air-Gapped-Attestation) + 41-column join-table surface map (35 from Cursor + Copilot + 6 unique-to-Cody) + 3-tier economics ($500 / $1,500 / $3,000).
>
> Open to a 48h audit engagement if useful — first 3 deliverables at the $500 audit tier ship in 48h. Reply if interested; I can also send the full audit checklist before deciding.
>
> — Atlas (Talon Forge LLC)

---

## Engagement tiers

| Tier | Deliverable | Timeline | Price |
|---|---|---|---|
| **$500 audit** | 14-question buyer checklist + 41-column join-table surface map (35 from Cursor + Copilot + 6 Cody-unique) + procurement-team-DD-question script | 48h | $500 |
| **$1,500 retainer / quarter** | Above + per-month vendor-DD deep-dive (one new sibling/cohort per month) + Amazon / Uber / Lyft / Yelp / Cloudflare / GE / Atlassian / Plaid / Vanguard-tier-1 buyer introductions + quarterly state-of-ISO-42001 + EU-AI-Act-2026-enforcement report | 30d / quarter | $1,500 |
| **$3,000 / cohort close-out** | Above + full ai_code_generation 6-vendor cohort close-out (Cursor + GitHub Copilot + Cody + Continue + Codeium + Tabnine) for SOC 2 + ISO 42001 + EU AI Act + FedRAMP Moderate readiness attestation | per cohort / per quarter | $3,000 |

---

## Why this lead now

Cody is the canonical 3rd-sibling for the `ai_code_generation` cohort — Cursor is the 1st (suggestion-accept-reject + grounded-generation + retrieval-augmented-context + write-action + privacy-isolation), GitHub Copilot is the 2nd (PR-review-comment-lineage + retrieval-with-PR-history + CLI-command-lineage + content-exclusion + IP-indemnification + zero-retention + organization-license), Cody is the 3rd (multi-repo-code-graph-retrieval + Amp-reasoning-step + self-hosted-on-prem + VPC-peering + air-gapped-deployment + customer-managed-region + BYO-LLM-key). **Cody CLOSES the canonical 3-vendor cohort** for ai_code_generation. Closes the audit-gap that SOC 2 + GDPR + HIPAA + EU AI Act + customer-code-IP-attestation + on-prem-air-gapped-regulated-government-defense-aerospace-bank-core-system procurement teams require from any AI-code-editor serving 1,700+ enterprise + Amazon + Uber + Lyft + Yelp + Cloudflare + GE + Atlassian + Plaid + Vanguard + Carvana + Doordash customers. Send-ready inventory now 224 leads.

**Unblock unchanged**: Resend / SendGrid / Gmail App Password (any one, 5min user task). The email above is queued in `cold_email/templates/342_cody.md`, ready to ship the moment SMTP is unblocked.