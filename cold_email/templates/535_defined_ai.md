# Cold Email — Defined.ai (Lead 535)

**To:** contact@defined.ai
**From:** Talon Forge / Atlas
**Subject line A:** Defined.ai marketplace provenance — Aug 2 EU AI Act GPAI evidence gap audit
**Subject line B:** Daniela — quick question on the 3-party contributor→Defined.ai→buyer audit chain

---

## Opener (3-line)

Hi Daniela — I run Talon Forge, an independent AI governance + AI vendor-DD consultancy that ships 48-hour audit deliverables to enterprise AI buyers. After Defined.ai's pivot from data-labeling-services to a marketplace model in 2024, the contributor→Defined.ai→buyer provenance chain is the single most underdocumented control surface in the AI data layer. We help teams like yours prove the marketplace license terms, contributor payouts, and buyer-side license restrictions hold up under EU AI Act Art. 53(d) GPAI, ISO 42001, and Schrems II SCC scrutiny.

## Provenance row (13-col)

| col | value |
|---|---|
| marketplace_listing_id | per-listing identifier published on defined.ai marketplace |
| dataset_version_id | hash-pinned dataset version (semver, immutable per release) |
| defined_ai_license_id | license-template-version applied to this listing |
| defined_ai_diana_prompt_id | Diana chatbot prompt trace, opt-in per session |
| byod_explorer_query_id | BYOD explorer query log, per-buyer session |
| defined_ai_contributor_id | verified contributor identity + payout rail |
| defined_ai_buyer_id | verified buyer identity + accepted license |
| defined_ai_tenant_id | tenant workspace + region of processing |
| procurement_vendor_dd_event_id | join row to buyer's vendor-DD system |
| audit_log_entry_id | append-only audit row, WORM retention |
| residency_region_id | EU / US / APAC / LATAM hosting region |
| defined_ai_contributor_payout_id | royalty event, payable per license terms |
| defined_ai_license_royalty_id | royalty calculation result, auditable |

## 5 audit gaps

1. **3-party provenance chain** — contributor → Defined.ai → buyer. Each leg must be auditable per-license, per-buyer, per-residency (SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + ISO 27701 + GDPR Art. 30 + Schrems II SCC + Daniela-Braga-Congressional-testimony).
2. **Training-data transparency** — marketplace dataset license provenance + Diana chatbot corpus + BYOD explorer index + professional-services annotation corpus + RLHF / safety-eval / multimodal / NLP / speech / vision / ethical-AI / fairness data (EU AI Act Art. 53(d) GPAI + Art. 53(1)(b) copyright-summary + ISO 42001 6.1.4 + Schrems II + EU-US DPF).
3. **Hostile-input defense** — Diana chatbot poisoning, BYOD explorer poisoning, marketplace listing poisoning, license-royalty bypass, buyer-license-restriction bypass, contributor-payout bypass, Daniela-Braga counter-messaging (OWASP LLM Top 10 LLM01/03/06/08 + MITRE ATLAS + EU AI Act Art. 14 human-oversight + Art. 50 + 12-state AI disclosure + Schrems II cross-border).
4. **Tenant + contributor + buyer + cross-region isolation** — per-tenant KMS keys (CMK/BYOK), per-tenant AI inference + training endpoints, cross-border data-residency isolation (SOC 2 CC6.1 + GDPR Art. 28 + Schrems II SCC + EU-US DPF + ISO 27701).
5. **WORM retention + cost attribution** — per-listing, per-Diana-prompt, per-BYOD-query, per-contributor-payout, per-license-royalty cost, full per-tenant cost join-table (SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + Schrems II + GDPR Art. 30).

## Regulatory hooks

EU AI Act Aug 2 2026 GPAI enforcement (Art. 53(d) + 53(1)(b)) · SOC 2 Type II · ISO 27001 · ISO 27701 · GDPR DPA + Schrems II SCC + EU-US DPF · CCPA/CPRA · HIPAA · 12-state AI disclosure · Daniela Braga US Congressional testimony recordkeeping · White House AI working-group recordkeeping · SEC 17a-4 WORM.

## CTA

Reply with a 20-minute slot next week and I'll send back a one-page marketplace-provenance control map with the 5 gaps above mapped to your current SOC 2 + EU AI Act evidence stack. No charge for the map — we charge $500 if you want the full 48-hour audit deliverable.

— Atlas, Talon Forge LLC