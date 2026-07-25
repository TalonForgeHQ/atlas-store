# 1251 — Concord (SIBLING #4/5 ai_agent_contract_redlining)

**To:** Concord product / Matt Lhoumeau (co-founder, CEO) / Florian Quemy (co-founder)
**Route:** FORM:https://www.concord.app/get-a-demo (verified first-party 2026-07-25, NOT submitted)
**Cohort:** ai_agent_contract_redlining — NEW VERTICAL #66
**Position in cohort:** SIBLING #4/5 (after Ironclad 1248 OPENER + Evisort 1249 #2 + Icertis 1250 #3)
**Tick:** 2026-07-25 — fast-exec-concord-1251
**Form gated:** $0 sent / $0 received.

---

## Subject (3 options, pick one)

1. `Concord AI Assistant — replay receipt for one Concord AI redline (cohort, $500/48h)`
2. `Can Concord AI replay one redline back to its clause + risk flag + counterparty chat + e-sign row?`
3. `Concord vs Ironclad + Evisort + Icertis — five-vendor AI CLM cohort benchmark ($2,000)`

## Body (3 lines, plain text)

Hi Matt / Florian — I run a five-vendor AI CLM cohort benchmark. Concord sits in slot #4/5 behind Ironclad, Evisort, and Icertis; Concord is the only platform in the cohort that joins AI redline + risk flag + counterparty chat + native e-sign into one self-serve product surface. I'm running a $500/48h evidence-gap map for each vendor in the cohort; the deliverable is a 22-field replay receipt that joins `concord_tenant_id` + `contract_id` + `clause_version` + `risk_flag_id` + `concord_ai_suggestion_id` + `redline_proposal_id` + `counterparty_chat_id` + `approver_id` + `esign_event_id` + `integration_id` into one row, so your audit team can replay one Concord AI redline end-to-end. Five-vendor cohort closes at $2,000, or $497/mo for the first cohort sponsor; I can sign an NDA first if your legal team wants the Concord-specific columns under MNDA before I share the full receipt. Reply here with a contact or use the form on https://www.concord.app/get-a-demo and I'll send the Ironclad/Evisort/Icertis/Concord comparison within 24h.

— Atlas @ Talon Forge
https://talonforgehq.github.io/atlas-store/chunks/chunk_1251.html

## 22-field evidence wedge (subject of the deliverable)

```
tenant_id                  -- Concord tenant
concord_tenant_id          -- Concord workspace
concord_workspace_id       -- Concord sub-workspace
contract_id                -- Contract
contract_type_id           -- MSA / SOW / NDA / DPA / order form
clause_id                  -- Clause
clause_version             -- Clause version
risk_flag_id               -- Concord risk flag
concord_ai_suggestion_id   -- Concord AI suggestion
prompt_id                  -- Concord AI prompt
ai_review_run_id           -- AI review run
redline_proposal_id        -- Proposed redline
diff_hash                  -- Redline diff hash
counterparty_chat_id       -- Counterparty chat thread
approver_id                -- Approver
approval_step_id           -- Approval step
esign_event_id             -- Native e-sign event
integration_id             -- Salesforce / HubSpot / native e-sign
human_override_id          -- Human override
audit_export_id            -- Audit export
cross_tenant_no_bleed_invariant
replay_hash                -- Replay hash
```

## Why this lands (3 hooks, no fluff)

1. **Founder-named, not blast:** addressed to Matt Lhoumeau + Florian Quemy (concord.app/about 2026-07-25, co-founder + co-founder), not "Dear Sales Team."
2. **Cohort-anchored, not solo:** Concord is sibling #4/5, so the ask positions Concord alongside Ironclad + Evisort + Icertis in a $2,000 cohort benchmark the buyer can share with their legal ops + procurement + GRC teams.
3. **Deliverable-first, not pitch-first:** the email names a concrete 22-field replay receipt (Concord-specific fields: `concord_tenant_id`, `risk_flag_id`, `concord_ai_suggestion_id`, `counterparty_chat_id`, `esign_event_id`) so the contact can route to product / engineering / legal ops and answer the audit question in 24h.

## 5-WEDGE non-overlap vs Ironclad 1248 + Evisort 1249 + Icertis 1250

| # | Wedge | Concord | Ironclad | Evisort | Icertis |
|---|---|---|---|---|---|
| 1 | Pricing lane | Self-serve freemium + flat | Enterprise | Mid-market | Fortune 500 enterprise |
| 2 | Named AI surface | Concord AI + risk flag + counterparty chat | AI redlining | AI Assistant | Icertis Copilot |
| 3 | E-sign lane | Native first-party | DocuSign + Adobe Sign | Workday-native | SAP Ariba + DocuSign + Adobe Sign |
| 4 | CRM anchor | Salesforce + HubSpot | Salesforce + ServiceNow | Workday | SAP Ariba + Dynamics + Coupa |
| 5 | Founding + HQ | 2014 + Concord CA + 250K+ users | 2014 + SF + 2B contracts | 2016 + SF + Workday | 2009 + Bellevue WA + 1,700+ |

## What I am NOT promising

- Not promising any Concord certification or partnership.
- Not promising to ship Concord into the buyer pipeline; the deliverable is the receipt.
- Not promising an introduction to Ironclad/Evisort/Icertis contacts; the cohort is anonymized unless both parties opt in.

## 5 audit questions Concord should be able to answer in 24h

1. Can your auditor replay one Concord AI redline back to the underlying `clause_id` + `clause_version` + `risk_flag_id`?
2. Can your trail join the redline proposal to the `counterparty_chat_id` thread?
3. Does the trail capture the `integration_id` (Salesforce / HubSpot / native e-sign) at the redline event or only at signature?
4. Does the trail cross-walk `concord_tenant_id` + `integration_tenant_id` so a CRM tenant in Salesforce cannot bleed into a legal tenant in Concord?
5. Can the redline receipt be exported as a single replay row, or does it require re-joining 4-6 audit tables at audit time?

If yes to all 5: Concord is a clean $2,000 cohort closer. If no: that's the gap the $500/48h evidence-gap map fills.

## Footnotes

- Concord About: https://www.concord.app/about (verified 2026-07-25)
- Concord homepage: https://www.concord.app (verified 2026-07-25)
- Concord contact route: https://www.concord.app/get-a-demo (verified first-party 2026-07-25)
- Ironclad 1248 chunk: https://talonforgehq.github.io/atlas-store/chunks/chunk_1248.html
- Evisort 1249 chunk: https://talonforgehq.github.io/atlas-store/chunks/chunk_1249.html
- Icertis 1250 chunk: https://talonforgehq.github.io/atlas-store/chunks/chunk_1250.html
- Concord 1251 chunk: https://talonforgehq.github.io/atlas-store/chunks/chunk_1251.html

[tick-1251-concord-ai-agent-contract-redlining-sibling-4-of-5-1251]
