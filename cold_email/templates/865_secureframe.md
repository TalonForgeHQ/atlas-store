# Secureframe — outbound cold email template

**Lead:** 865 — Secureframe, Inc. (secureframe.com)
**Contact route:** FORM:https://secureframe.com/request-demo
**Subject variants:** A/B/C below
**Offer:** $500 / 48h fixed-scope evidence-gap map · $497/mo quarterly refresh · $497/mo × 5 YanXbt cohort

---

## Subject A (lead-with-product — evidence-gap map)

> A 21-column Secureframe-Comply + Defense evidence-gap map you can hand to your C3PAO

Hi {{first_name}},

Most SOC 2 + ISO 27001 evidence maps we audit collapse under CMMC 2.0 because the
per-control-uid + per-framework-version pinning doesn't extend across Secureframe
Comply → Secureframe Defense. The result: auditors spend 60+ hours reproducing
the evidence trail instead of trusting the timestamp ledger.

For Secureframe specifically that means a 21-column receipt joining
control_uid + framework_version + evidence_collection_timestamp +
automation_run_id + auditor_acknowledgment_id + policy_version_id +
cmmc_level + cui_scope_isolation_state + fedramp_20x_piid_package_state +
defense_navigator_milestone + ssp_version_id + poam_version_id +
c3pao_acknowledgment_id + nist_800_171a_objective_id +
secureframe_ai_model_version + secureframe_ai_response_id — produced
in 48h, exportable as a single CSV + Markdown bundle, reproducible by an
external C3PAO without re-running the Secureframe-AI co-pilot.

— Shrav, this is the layer that closes the DoD-prime → mid-market
   compliance loop most teams don't realize is missing until audit week.

Two ways to engage:
1. $500 / 48h fixed-scope evidence-gap map (one audit-ready bundle).
2. $497/mo quarterly refresh (per-framework-version-bump + per-new-control-uid
   + per-C3PAO-acknowledgment-id re-validation).

— Atlas @ Talon Forge
   Secureframe cohort #3/5 after Vanta (862) + Scrut (864).
   No SMTP claim — this is an inbound FORM pickup, not an outbound blast.

---

## Subject B (lead-with-founder pedigree)

> Shrav — the KPCB-board-C3PAO-readiness receipt most Secureframe customers miss

Hi {{first_name}},

Secureframe ships the only cohort-grade compliance platform with a first-party
CMMC 2.0 Defense product surface (Defense Navigator + Managed CUI Enclave +
SSP & POA&M Management). The wedge is small and most C3PAOs don't surface it
in their readiness checklist.

What we hand back in 48h:
- A 21-column evidence-gap map joining per-control-uid + per-CMMAC-level +
  per-CUI-scope-isolation + per-FedRAMP-20x-PIID-package-state +
  per-Defense-Navigator-Milestone + per-C3PAO-acknowledgment-id.
- A C3PAO-ready CSV + Markdown bundle.
- A reproducible replay (one command, no Secureframe credentials).

Two ways to engage:
1. $500 / 48h fixed-scope.
2. $497/mo quarterly refresh.

— Atlas @ Talon Forge
   ai_security_compliance_attestation sibling #3/5 (after Vanta 862 + Scrut 864).

---

## Subject C (lead-with-economics)

> The $497/mo Secureframe evidence-refresh retainer that closes the audit-letter math

Hi {{first_name}},

Most Secureframe customers pay for Comply + Defense + AI + Federal but the
evidence ledger is fragmented across three control surfaces. The result is a
~$25K/year hidden audit-prep tax — auditors reproducing what should already be
reproducible from the Secureframe API.

What we ship in 48h:
- A 21-column evidence-gap map (one exportable CSV + Markdown bundle).
- A $497/mo quarterly retainer that pins per-framework-version + per-new-
  control-uid + per-C3PAO-acknowledgment-id so the next audit costs hours,
  not weeks.

— Atlas @ Talon Forge
   No SMTP claim. Form pickup only.

---

## Pitfalls reinforced

- P28: FORM-only correct — no general-business inbox published on first-party
  rendered surface; commercial route is the JSON-LD-Sales contactPoint URL.
- P41: /about page is Cloudflare-challenged (2026-07-21); Wayback fallback
  used for verbatim /about facts (2020 founded, 200+ employees, $79M
  funding, Kleiner Perkins + Gradient + Accomplice + Base10 + BoxGroup +
  Chapter One + Village Global + Liquid 2).
- P43: JSON-LD Organization schema on the homepage is server-rendered,
  no JS hydration needed — grep the inline script block.
- P31: no customer-name brag (do not list "Anthropic uses X") — pivot to
  the audit-letter math instead.
- P44: cat-heredoc + write_file for cron-safe lead row append (no execute_code).