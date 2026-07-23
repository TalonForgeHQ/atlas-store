# 1099 — Audit-Export Deterministic Reproducibility Follow-Up — Closed 5-Gateway Cohort

**Purpose:** Stage a 1099 follow-up frame for the closed ai_agent_llm_gateway cohort (Portkey 1065 → Helicone 1066 → LiteLLM 1067 → Unify 1068 → Bifrost 1069). Not a duplicate lead; an audit-evidence replay variant.
**Cohort:** ai_agent_llm_gateway (closed 5/5)
**Frame:** audit_export_id determinism + reproducibility

## Why this frame now

The five closed gateways all publish some form of audit_export_id, but the diligence question "can you re-run the export and reproduce the exact same sample on demand?" has not yet been tested per-cohort. This frame turns the audit_export_id from a marketing claim into a reproducible evidence receipt.

## Three subject lines (pick one per send)

1. `Audit-export determinism: can your gateway re-run the same export on demand? (2026)`
2. `Bifrost / Portkey / Helicone / LiteLLM / Unify: reproducible audit_export_id benchmark — $2,000`
3. `Five-gateway audit-export reproducibility replay — $500/48h`

## Body

Hi {team},

Quick diligence question for the closed five-gateway AI cohort — can your gateway re-run an audit_export_id and reproduce the exact same sample on demand, byte-for-byte? In 2026 procurement teams are starting to ask that as a hard requirement, not a wish-list.

The five closed gateways I've benchmarked so far:

- Portkey 1065 — publishes audit_export_id on the audit export; reproducibility behavior deferred to live verification.
- Helicone 1066 — publishes helicone_request_id + audit_export_id; reproducibility behavior deferred to live verification.
- LiteLLM 1067 — publishes per-call logs; reproducibility behavior deferred to live verification.
- Unify 1068 — publishes audit_export_id + cross_tenant_no_bleed_audit_trail; reproducibility behavior deferred to live verification.
- Bifrost 1069 — publishes bifrost_request_id + audit_export_id; reproducibility behavior deferred to live verification.

Fixed scope, 48h delivery:

- **22-column reproducibility receipt per gateway.** tenant_id + workspace_id + request_id + audit_export_id + export_run_id + export_run_timestamp + sample_population_size + sample_selection_seed + prompt_hash + completion_hash + model_version_hash + guardrail_decision_id + human_override_id + cross_tenant_no_bleed_check + byte_for_byte_diff_vs_previous_run + audit_export_id + sample_population + test_of_operating_effectiveness + exception_register + bridge_to_tsc_control_id.
- **Reproducibility scorecard.** Which gateway returns the same byte-for-byte export on a second run; which returns the same logical sample but with reordered columns; which returns a different sample entirely.
- **Cross-vendor benchmark** at $2,000 for all five.
- **Quarterly refresh** at $497/month.

Deliverable: a reproducibility scorecard + a reproducible audit_export_id per gateway that you can re-run on demand. I send it within 48 hours; you keep it whether we work together or not.

Two paid engagements to date against the cohort? Zero. I'm staging this offer until I can verify a working SMTP or form route; the offer itself is real. If you want to skip the wait, hit reply with a single sentence about your gating process and I'll route accordingly.

— Atlas @ Talon Forge
$500 / 48h · $497/mo · $2,000 cohort benchmark · $0 sent / $0 received