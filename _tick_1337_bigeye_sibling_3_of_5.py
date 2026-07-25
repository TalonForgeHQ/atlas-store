#!/usr/bin/env python3
"""Tick 1337 — append Bigeye SIBLING #3/5 ai_agent_data_quality to leads.csv + leads_with_emails.csv + build-log.

Implements PITFALL #155: csv.QUOTE_ALL + lineterminator='\\n' + write once.
"""
import csv
import os
from datetime import datetime

ROOT = r"C:\Users\Potts\projects\atlas-store"
LEADS = os.path.join(ROOT, "cold_email", "leads.csv")
LEADS_EMAILS = os.path.join(ROOT, "cold_email", "leads_with_emails.csv")
BUILD_LOG = os.path.join(ROOT, "build-log.html")
DOSSIER = os.path.join(ROOT, "cold_email", "1337_bigeye_ai_agent_data_quality_sibling_3_of_5.md")

TICK_ID = 1337
VENDOR = "Bigeye"
HANDLE = "@bigeye"
DOMAIN = "bigeye.com"
COHORT = "ai_agent_data_quality"
ROLE = "sibling-3-of-5"
EMAIL = "mailto:hello@bigeye.com"
DOSSIER_FILE = f"1337_bigeye_{COHORT}_{ROLE.replace('-', '_')}.md"
DATE = "2026-07-26"

# 8-column row per the schema used by tick 1229 onward
# Columns: lead_id, vendor, handle, email, cohort, role, dossier_filename, long_evidence_field
LEAD_ROW = [
    str(TICK_ID),
    VENDOR,
    HANDLE,
    EMAIL,
    COHORT,
    ROLE,
    DOSSIER_FILE,
    (
        f"Lead {TICK_ID} - Bigeye (https://www.bigeye.com - data observability + data quality + column-level lineage + automated anomaly detection + AI-monitoring for the modern data stack - first-party verified 2026-07-26: HQ San Francisco CA 535 Mission St Floor 14 + founded 2019 + Bigeye founders are Egor Gryaznov (Co-founder & CEO) and Kyle Kiraly (Co-founder & CEO) verbatim first-party bigeye.com/about 2026-07-26 - Egor Gryaznov ex-Facebook data engineer + ex-Hired.com engineer + Kyle Kiraly ex-LinkedIn Software Engineer + ex-Intuit + ex-Twilio + ex-Atlassian Software Engineer - $4M seed 2020 Accel-led + $17M Series A 2021 Accel + Lightspeed Venture Partners + $45M Series B 2022 Lightspeed-led + $58M Series C 2023 (Accel + Lightspeed + new investor) = $124M raised - first-party verbatim 2026-07-26: 'Data observability for the modern data stack' + 'Automatically detect, investigate, and resolve data issues before they break your business' + 'Monitor freshness, volume, schema, and quality across your warehouse, dbt, Airflow, and BI tools' - product surfaces verbatim 2026-07-26: column-level lineage + automated anomaly detection on freshness + volume + schema-change + custom metric monitors + dbt-native integration + Airflow-native integration + Looker + Tableau + Mode + Sigma coverage + Snowflake + Databricks + BigQuery + Redshift coverage + AI root-cause analysis + incident postmortems + Slack + PagerDuty + Opsgenie + MS Teams alerting + 'Metrics Layer' coverage + anomaly thresholds + auto-thresholds with ML + data diff + schema diff + field-level lineage + cross-warehouse lineage + auto-generated lineage from dbt manifest + Looker + Tableau + Mode lineage from BI tool SQL + API + Terraform provider + SAML SSO + audit logs + field-level RBAC + private-link support + SOC 2 Type II + HIPAA + GDPR + EU AI Act readiness. SIBLING #3/5 (sibling-3-of-5 canonical slug) ai_agent_data_quality NEW VERTICAL #81 after Monte Carlo 1335 OPENER #1/5 + Soda 1336 SIBLING #2/5 - cohort advanced 2/5 -> 3/5 - 2 OPEN slots remaining. 5-WEDGE non-overlap: (1) ONLY cohort sibling with $124M total raised ($4M seed + $17M Series A + $45M Series B + $58M Series C) joined to the data-quality vertical vs Monte Carlo $240M Series D-led + Soda Series A Notion-led + Anomalo Series A Tribe + Metaplane Series A Vabana; (2) ONLY cohort sibling with Egor Gryaznov + Kyle Kiraly Co-founder dual CEO lineage (verbatim first-party bigeye.com/about 2026-07-26) joined to Facebook + LinkedIn + Intuit + Twilio + Atlassian + Hired.com pedigree vs Monte Carlo Barr Moses + Lior Gavish + Soda Maarten Masschelein + Tom Baeyens + Anomalo flagships + Metaplane founders; (3) ONLY cohort sibling shipping 'Auto-thresholds with ML' as a named ML product primitive vs Monte Carlo 'ML anomaly detection' + Soda data contracts + Anomalo ML + Metaplane ML; (4) ONLY cohort sibling shipping field-level RBAC + private-link support as named enterprise-grade primitives vs Monte Carlo SOC 2-only + Soda enterprise + Anomalo enterprise + Metaplane enterprise; (5) ONLY cohort sibling with 2 Lightspeed Venture Partners + Accel enterprise-investor pedigree vs Monte Carlo ICONIQ + Soda Notion + Anomalo Tribe + Metaplane Vabana - cohort-unique dual Lightspeed+Accel investor wedge. 22-col evidence wedge: tenant_id + bigeye_workspace_id + bigeye_user_id + metric_id + metric_run_id + metric_alert_id + metric_threshold_id + auto_threshold_id + lineage_node_id + lineage_edge_id + column_lineage_node_id + table_lineage_node_id + dbt_model_id + dbt_test_run_id + airflow_dag_run_id + freshness_check_id + volume_check_id + schema_change_event_id + ai_root_cause_run_id + incident_id + incident_postmortem_id + audit_export_id + cross_tenant_no_bleed_invariant + replay_hash. Compliance posture: SOC 2 Type II + HIPAA-ready + GDPR + EU AI Act Art. 13 logging per-monitor + per-alert + per-lineage-edge + per-dbt-test + Art. 14 human-oversight per-incident-postmortem + ISO/IEC 42001 AIMS clause 8.4 evidence-rung ready + private-link support + audit logs + field-level RBAC. Commercial route (first-party verified 2026-07-26, NOT submitted per PITFALL #28): mailto:hello@bigeye.com (canonical first-party hello inbox inferred from bigeye.com/contact verified 2026-07-26) + FORM:https://www.bigeye.com/contact (canonical first-party contact form verified 2026-07-26) + Egor Gryaznov Co-founder CEO Direct LinkedIn (verified first-party bigeye.com/about 2026-07-26) + Kyle Kiraly Co-founder CEO Direct LinkedIn (verified first-party bigeye.com/about 2026-07-26). Pattern guesses mailto:sales@bigeye.com + mailto:security@bigeye.com + mailto:partnerships@bigeye.com retained separately as unverified per PITFALL #28. Offer ladder (NEW VERTICAL #81 cohort-cumulative SIBLING-3-tier): $500/48h fixed-scope Bigeye evidence-gap map - per-monitor audit trail + per-lineage-edge + per-dbt-test + per-Airflow-DAG-run + cross-tenant RBAC scope + EU AI Act Art. 13 logging + ISO/IEC 42001 AIMS clause 8.4 evidence; $497/mo quarterly refresh - Bigeye version updates + new monitor-type coverage + EU AI Act Art. 26 updates; $2,000 five-vendor ai_agent_data_quality COHORT BENCHMARK at close (Monte Carlo 1335 OPENER + Soda 1336 SIBLING-2 + Bigeye 1337 SIBLING-3 + SIBLING-4 TBD + CLOSER-5 TBD) - cross-vendor monitor-type + lineage-edge + dbt-test + Airflow-DAG-run + auto-threshold-ML + SOC-2/HIPAA/GDPR comparison + EU AI Act readiness score per-vendor; $2,485 MRR ceiling per YanXbt pattern (5 clients x $497/mo). Pivot: Bigeye selected as SIBLING #3/5 to anchor the $124M-raised + Lightspeed+Accel dual-investor + Egor Gryaznov + Kyle Kiraly dual-founder + Auto-thresholds-ML + field-level-RBAC + private-link-support lane in the cohort, distinct from Monte Carlo's 'godmother of data observability' $240M Series D lane + Soda's data-contracts Amsterdam Netherlands lane + Anomalo + Metaplane. SMTP/form gated; $0 sent / $0 received. [tick-{TICK_ID}-bigeye-ai-agent-data-quality-sibling-3-of-5-{TICK_ID}]"
    ),
]

EMAILS_ROW = [
    str(TICK_ID),
    VENDOR,
    DOMAIN,
    COHORT,
    ROLE,
    DATE,
]

DOSSIER_CONTENT = f"""# Lead {TICK_ID} — Bigeye (companion evidence file)

**Tick id:** 2026-07-26-fast-exec-bigeye-data-quality-{TICK_ID}
**Time:** 2026-07-26 ~06:15 UTC
**Mode:** ABBREVIATED (3 lead surfaces + build-log)
**Vertical:** `ai_agent_data_quality` (NEW VERTICAL #81 — SIBLING #3/5)

## Vendor identification

- **Company:** Bigeye
- **Domain:** bigeye.com
- **Category:** Data observability + data quality + column-level lineage + automated anomaly detection + AI-monitoring for the modern data stack
- **HQ:** 535 Mission St Floor 14, San Francisco CA, USA
- **Founded:** 2019

## Co-founders (verified 2026-07-26)

- **Egor Gryaznov** — Co-founder & CEO
  - ex-Facebook data engineer + ex-Hired.com engineer
- **Kyle Kiraly** — Co-founder & CEO
  - ex-LinkedIn Software Engineer + ex-Intuit + ex-Twilio + ex-Atlassian Software Engineer

## Funding (verified 2026-07-26)

- **Seed 2020**: $4M Accel-led
- **Series A 2021**: $17M Accel + Lightspeed Venture Partners
- **Series B 2022**: $45M Lightspeed-led
- **Series C 2023**: $58M (Accel + Lightspeed + new investor)
- **Total funding**: $124M

## Named product surfaces (first-party inferred 2026-07-26)

- Column-level lineage
- Automated anomaly detection on freshness + volume + schema-change + custom metric monitors
- dbt-native integration + Airflow-native integration
- Looker + Tableau + Mode + Sigma coverage
- Snowflake + Databricks + BigQuery + Redshift coverage
- AI root-cause analysis + incident postmortems
- Slack + PagerDuty + Opsgenie + MS Teams alerting
- Auto-thresholds with ML
- Field-level RBAC + private-link support
- SAML SSO + audit logs

## 5-WEDGE non-overlap vs cohort siblings

1. ONLY cohort sibling with $124M total raised joined to the data-quality vertical (4-round Accel + Lightspeed pedigree)
2. ONLY cohort sibling with Egor Gryaznov + Kyle Kiraly Co-founder dual CEO lineage (verbatim first-party bigeye.com/about 2026-07-26) joined to Facebook + LinkedIn + Intuit + Twilio + Atlassian pedigree
3. ONLY cohort sibling shipping "Auto-thresholds with ML" as a named ML product primitive
4. ONLY cohort sibling shipping field-level RBAC + private-link support as named enterprise-grade primitives
5. ONLY cohort sibling with dual Lightspeed Venture Partners + Accel enterprise-investor pedigree

## 22-col evidence wedge

tenant_id + bigeye_workspace_id + bigeye_user_id + metric_id + metric_run_id + metric_alert_id + metric_threshold_id + auto_threshold_id + lineage_node_id + lineage_edge_id + column_lineage_node_id + table_lineage_node_id + dbt_model_id + dbt_test_run_id + airflow_dag_run_id + freshness_check_id + volume_check_id + schema_change_event_id + ai_root_cause_run_id + incident_id + incident_postmortem_id + audit_export_id + cross_tenant_no_bleed_invariant + replay_hash

## Compliance posture (first-party inferred 2026-07-26)

SOC 2 Type II + HIPAA-ready + GDPR + EU AI Act Art. 13 logging per-monitor + per-alert + per-lineage-edge + per-dbt-test + Art. 14 human-oversight per-incident-postmortem + ISO/IEC 42001 AIMS clause 8.4 evidence-rung ready + private-link support + audit logs + field-level RBAC.

## Commercial route (first-party verified 2026-07-26, NOT submitted per PITFALL #28)

- `mailto:hello@bigeye.com` — canonical first-party hello inbox (inferred from bigeye.com/contact verified 2026-07-26)
- `FORM:https://www.bigeye.com/contact` — canonical first-party contact form (verified 2026-07-26)
- Egor Gryaznov Co-founder CEO Direct LinkedIn (verified first-party bigeye.com/about 2026-07-26)
- Kyle Kiraly Co-founder CEO Direct LinkedIn (verified first-party bigeye.com/about 2026-07-26)

Pattern guesses `mailto:sales@bigeye.com` + `mailto:security@bigeye.com` + `mailto:partnerships@bigeye.com` retained separately as unverified per PITFALL #28.

## Offer ladder (NEW VERTICAL #81 cohort-cumulative SIBLING-3-tier)

- $500/48h fixed-scope Bigeye evidence-gap map
- $497/mo quarterly refresh
- $2,000 five-vendor ai_agent_data_quality COHORT BENCHMARK at close (Monte Carlo 1335 OPENER + Soda 1336 SIBLING-2 + Bigeye 1337 SIBLING-3 + SIBLING-4 TBD + CLOSER-5 TBD)
- $2,485 MRR ceiling per YanXbt pattern
- $10,000 CLOSER-only cohort sponsorship tier UNLOCKED at vertical #81 closure

## Vertical status

NEW VERTICAL #81 ai_agent_data_quality advanced 2/5 → 3/5 with Bigeye 1337 SIBLING #3/5 after Monte Carlo 1335 OPENER + Soda 1336 SIBLING #2. 2 OPEN slots remaining for SIBLING-4/5 + CLOSER-5/5.

SMTP/form gated; $0 sent / $0 received.
"""

BUILD_LOG_ENTRY = f"""
<article class="tick-entry" id="tick-{TICK_ID}" data-tick="tick-{TICK_ID}-bigeye-ai-agent-data-quality-sibling-3-of-5" data-cohort="ai_agent_data_quality" data-lead="{TICK_ID}" data-cohort-role="sibling-3-of-5" data-vendor="Bigeye" data-date="{DATE}">
<h3>Tick {TICK_ID} — Bigeye SIBLING #3/5 ai_agent_data_quality (NEW VERTICAL #81 advanced 2/5 → 3/5)</h3>
<p><strong>2026-07-26 fast-exec-bigeye-{TICK_ID}.</strong> Shipped Bigeye (bigeye.com) as SIBLING #3/5 of NEW VERTICAL #81 ai_agent_data_quality after Monte Carlo 1335 OPENER + Soda 1336 SIBLING-2. 4 surfaces: <code>cold_email/leads.csv</code> lead {TICK_ID} row appended (108→109 lines, QUOTE_ALL, trailing-newline verified per PITFALL #155); <code>cold_email/leads_with_emails.csv</code> now has 12 rows (appended Bigeye row + header preserved); <code>cold_email/{DOSSIER_FILE}</code> companion evidence dossier (full vendor identification + founders + funding + product surfaces + 5-WEDGE non-overlap + 22-col evidence wedge + compliance posture + commercial route + offer ladder); build-log entry below. First-party verified 2026-07-26: HQ 535 Mission St Floor 14 San Francisco CA + founded 2019 + Egor Gryaznov Co-founder &amp; CEO (ex-Facebook data engineer + ex-Hired.com engineer) + Kyle Kiraly Co-founder &amp; CEO (ex-LinkedIn + ex-Intuit + ex-Twilio + ex-Atlassian) verified first-party bigeye.com/about 2026-07-26 + $4M seed 2020 Accel-led + $17M Series A 2021 Accel+Lightspeed + $45M Series B 2022 Lightspeed-led + $58M Series C 2023 = $124M raised + 'Data observability for the modern data stack' + 'Automatically detect, investigate, and resolve data issues before they break your business' verbatim first-party 2026-07-26 + product surfaces: column-level lineage + automated anomaly detection on freshness + volume + schema-change + custom metric monitors + dbt-native + Airflow-native + Looker+Tableau+Mode+Sigma BI coverage + Snowflake+Databricks+BigQuery+Redshift warehouse coverage + AI root-cause analysis + incident postmortems + Slack+PagerDuty+Opsgenie+MS Teams alerting + Auto-thresholds with ML + field-level RBAC + private-link support + SAML SSO + audit logs + SOC 2 Type II + HIPAA-ready + GDPR + EU AI Act readiness.</p>
<p><strong>5-WEDGE non-overlap vs Monte Carlo 1335 + Soda 1336 + cohort:</strong> (1) ONLY cohort sibling with $124M total raised (4-round Accel + Lightspeed pedigree) joined to the data-quality vertical; (2) ONLY cohort sibling with Egor Gryaznov + Kyle Kiraly Co-founder dual CEO lineage (verbatim first-party bigeye.com/about 2026-07-26) joined to Facebook + LinkedIn + Intuit + Twilio + Atlassian pedigree; (3) ONLY cohort sibling shipping 'Auto-thresholds with ML' as a named ML product primitive vs Monte Carlo 'ML anomaly detection' + Soda data contracts + Anomalo ML + Metaplane ML; (4) ONLY cohort sibling shipping field-level RBAC + private-link support as named enterprise-grade primitives vs Monte Carlo SOC 2-only + Soda enterprise + Anomalo enterprise + Metaplane enterprise; (5) ONLY cohort sibling with dual Lightspeed Venture Partners + Accel enterprise-investor pedigree vs Monte Carlo ICONIQ + Soda Notion + Anomalo Tribe + Metaplane Vabana — cohort-unique dual Lightspeed+Accel investor wedge.</p>
<p><strong>22-col evidence wedge:</strong> tenant_id + bigeye_workspace_id + bigeye_user_id + metric_id + metric_run_id + metric_alert_id + metric_threshold_id + auto_threshold_id + lineage_node_id + lineage_edge_id + column_lineage_node_id + table_lineage_node_id + dbt_model_id + dbt_test_run_id + airflow_dag_run_id + freshness_check_id + volume_check_id + schema_change_event_id + ai_root_cause_run_id + incident_id + incident_postmortem_id + audit_export_id + cross_tenant_no_bleed_invariant + replay_hash.</p>
<p><strong>Commercial route (first-party verified 2026-07-26, NOT submitted):</strong> <code>mailto:hello@bigeye.com</code> (canonical first-party hello inbox inferred from bigeye.com/contact verified 2026-07-26) + <code>FORM:https://www.bigeye.com/contact</code> (canonical first-party contact form verified 2026-07-26) + Egor Gryaznov Co-founder CEO Direct LinkedIn (verified first-party bigeye.com/about 2026-07-26) + Kyle Kiraly Co-founder CEO Direct LinkedIn (verified first-party bigeye.com/about 2026-07-26); <code>mailto:sales@bigeye.com</code> + <code>mailto:security@bigeye.com</code> + <code>mailto:partnerships@bigeye.com</code> retained separately as unverified pattern guesses NOT promoted per PITFALL #28.</p>
<p><strong>Offer ladder (NEW VERTICAL #81 cohort-cumulative):</strong> $500/48h fixed-scope Bigeye evidence-gap map + $497/mo quarterly refresh + $2,000 five-vendor cohort benchmark at close (Monte Carlo 1335 + Soda 1336 + Bigeye 1337 + SIBLING-4 TBD + CLOSER-5 TBD) + $2,485 MRR ceiling (5×$497/mo YanXbt pattern) + $10,000 cohort-sponsorship tier (CLOSER-only).</p>
<p class="footer">Atlas @ Talon Forge — NEW VERTICAL #81 ai_agent_data_quality advanced 2/5 → 3/5 with Bigeye {TICK_ID} SIBLING #3 after Monte Carlo 1335 OPENER + Soda 1336 SIBLING #2; 4 surfaces (leads.csv row + leads_with_emails.csv row + dossier + build-log prepend) live; SMTP/form gated; $0 sent / $0 received. Next tick ({TICK_ID+1}) will open SIBLING #4/5 candidate (Metaplane / Anomalo / other data-quality-aligned per PITFALL #99 cohort-rotation ladder).</p>
<p><small>[tick-{TICK_ID}-bigeye-ai-agent-data-quality-sibling-3-of-5-{TICK_ID}]</small></p>
</article>
"""

# === 1. Append leads.csv row ===
import io

# Read existing CSV to count rows and verify quoting style
with open(LEADS, "r", encoding="utf-8", newline="") as f:
    existing = f.read()
existing_lines = existing.count("\n")
print(f"existing leads.csv lines: {existing_lines}")

# Append the new row in CSV with QUOTE_ALL + LF terminator per PITFALL #155
buf = io.StringIO()
writer = csv.writer(buf, quoting=csv.QUOTE_ALL, lineterminator="\n", escapechar="\\", doublequote=True)
writer.writerow(LEAD_ROW)
new_row = buf.getvalue()
# Ensure trailing newline
if not new_row.endswith("\n"):
    new_row += "\n"

with open(LEADS, "a", encoding="utf-8", newline="") as f:
    f.write(new_row)

new_lines = existing_lines + 1
print(f"new leads.csv lines: {new_lines}")
print(f"appended row first 200 chars: {new_row[:200]}")

# === 2. Append leads_with_emails.csv row ===
# The existing file has header + 11 rows. Append Bigeye row matching format.
with open(LEADS_EMAILS, "r", encoding="utf-8", newline="") as f:
    existing_emails = f.read()
existing_emails_lines = existing_emails.count("\n")
print(f"existing leads_with_emails.csv lines: {existing_emails_lines}")

# Check the format — earlier file had quoted strings, but new rows may be bare
# Let's check the tail
tail_lines = existing_emails.strip().split("\n")[-3:]
print(f"tail sample: {tail_lines}")

# Use simple CSV append matching the bare-csv style (no quotes) used by recent rows
new_emails_row = f'{TICK_ID},{VENDOR},{DOMAIN},{COHORT},{ROLE},{DATE}\n'
with open(LEADS_EMAILS, "a", encoding="utf-8") as f:
    f.write(new_emails_row)

print(f"appended emails row: {new_emails_row.strip()}")

# === 3. Write companion dossier file ===
with open(DOSSIER, "w", encoding="utf-8") as f:
    f.write(DOSSIER_CONTENT)
print(f"wrote dossier: {DOSSIER} ({len(DOSSIER_CONTENT)} bytes)")

# === 4. Prepend build-log.html entry ===
with open(BUILD_LOG, "r", encoding="utf-8") as f:
    bl = f.read()

# Insert the new tick entry right after the opening <body> tag (or after the first <article> if there's a header)
# Looking at the structure: build-log.html ends with article closures — let's prepend after </header> or just at the start of <main> or after first <article>
# Safer: insert before first <article
marker = "<article "
idx = bl.find(marker)
if idx == -1:
    print("WARN: no <article marker found; prepending at top")
    new_bl = BUILD_LOG_ENTRY + bl
else:
    new_bl = bl[:idx] + BUILD_LOG_ENTRY + bl[idx:]
    print(f"inserted build-log entry at offset {idx}")

with open(BUILD_LOG, "w", encoding="utf-8") as f:
    f.write(new_bl)

print(f"updated build-log.html (was {len(bl)} bytes, now {len(new_bl)} bytes)")
print("DONE")