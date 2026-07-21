# Anomalo — Lead 840 follow-up template

**Tick id:** 2026-07-21-fast-exec-anomalo-840
**Cohort:** `ai_data_context_observability` CLOSER #5/5
**Sanctioned commercial route:** https://www.anomalo.com/request-a-demo/ (first-party Request a Demo page, HTTP 200 verified 2026-07-21; `/demo` redirects to the same route)

## Five-question audit-letter mapping (per cohort convention)

1. **What model/version produced the anomaly?** — Anomalo AI anomaly-detection model + version + trained-on-customer-table-snapshot + unsupervised-threshold-tuning-window
2. **What dataset / table / column / field identity is the issue scoped to?** — `dataset_id` + `table_id` + `column_id` + `external_system_of_record` + `tenant_id` + `data_warehouse_id`
3. **What validation rule / data-quality issue fires?** — `validation_rule_id` + `validation_rule_version` + `dq_issue_id` + `dq_issue_severity` + `dq_issue_status` (open/triaged/owner_assigned/in_remediation/closed)
4. **What lineage edge / governance policy / tenant context applies?** — `lineage_edge_id` + `lineage_run_id` + `governance_policy_id` + `policy_version` + `owner_id` + `remediation_sla_seconds`
5. **What exportable control evidence + exception / rollback path?** — `control_evidence_id` + `control_framework` (SOC 2 + GDPR Art 5/25/32/35 + EU AI Act Art 14(4)) + `exception_id` + `rollback_event_id` + `evidence_artifact_storage_path` + `export_timestamp`

## Offer framing

- $500 / 48h fixed-scope **evidence-gap map** — the 5-question audit letter joined to Anomalo's first-party surface
- $497 / mo quarterly refresh — running the audit letter against new Anomalo releases
- $497 × 5-client YanXbt pattern — retainer engine (documentation only; no send, no claim)

## Non-overlapping wedge (why Anomalo closes the cohort, not duplicates it)

- **vs DataHub 836** — DataHub is OSS Apache-2.0 metadata-catalog + AI-context lineage (open-source-metadata-native)
- **vs Acceldata 837** — Acceldata is data-pipeline reliability + remediation (pipeline-reliability-native)
- **vs Monte Carlo Data 838** — Monte Carlo is field-level lineage + automated RCA + AI-monitoring (field-level-lineage-native)
- **vs Bigeye 839** — Bigeye is Enterprise AI Trust + runtime-enforcement + sensitivity scanning (Enterprise-AI-Trust-native)
- **Anomalo 840** — AI-based unknown-unknowns detection + unstructured-data monitoring + automated data-lineage + table-observability (AI-quality-monitoring-native)

## Channels and constraints

- **No guessed inbox added.** First-party Request a Demo form is the sanctioned commercial channel.
- **No form submission made.** SMTP, contact-form submission, payment, delivery, and revenue all remain $0.
- **Build-log entry:** appended to `build-log.html` for tick 2026-07-21-fast-exec-anomalo-840.
- **Revenue_log entry:** audit-only line, $0 sent / $0 received.

## Suggested subject line (not sent, not fabricated)

`Anomalo: 5-question audit letter for AI-based unknown-unknowns quality monitoring (gap-map)` — for reference only; the bot does NOT send until SMTP is unlocked.

---

*Cron tick 2026-07-21-fast-exec-anomalo-840 · template only · SMTP remains gated*
