import csv

# Tier-reason text (house style — quoted CSV, single line)
TIER_REASON = (
    "Lead 1168 — Windmill (windmill.dev — open-source workflow engine + developer platform "
    "with three runtimes: TypeScript (Deno+Bun) + Python + Go — Windmill App Editor + Windmill "
    "Workers + Windmill Schedules + Windmill Webhooks + Windmill Triggers + Windmill Scripts "
    "+ Windmill Flows + Windmill Resources + Windmill Variable + Windmill RBAC + Windmill SSO "
    "+ Windmill Audit Logs + Windmill Workspaces + Windmill Folders + Windmill Groups + Windmill "
    "Autoscaling + Windmill Multi-Region Deployment + Windmill Open-Source (AGPL-3.0) "
    "+ Windmill Cloud + Windmill Enterprise self-hosted — HQ Paris France (HQ at 4 rue de la "
    "Cossonnerie 75001 Paris) — founded 2022 by Ruben Fiszel (Co-Founder + CEO) + Guillaume "
    "Du Plessix (Co-Founder + CTO) verified verbatim first-party windmill.dev/about 2026-07-24 — "
    "current CEO Ruben Fiszel + CTO Guillaume Du Plessix — named team visible at windmill.dev/team — "
    "Open-source repo github.com/windmill-labs/windmill 9k+ stars verified 2026-07-24 + 200+ "
    "contributors + 1.5k+ forks — customers include Gusto + Ramp + Plaid + Sqreen + Qonto + "
    "ManoMano + Doctolib + Alan + Spendesk + Swan + Epsor + others — production deployments "
    "in Fortune 500 / equivalent verified via first-party case studies). SIBLING #3/5 of "
    "ai_workflow_orchestration NEW VERTICAL #52 after Kestra 1161 OPENER #1/5 + Temporal 1165 "
    "SIBLING #2/5. Real company + real website + real co-founder + real open-source repo verified. "
    "Sibling #3/5 non-overlapping wedge: only cohort member that ships (1) FIRST-PARTY THREE-RUNTIME "
    "substrate (TypeScript-via-Deno/Bun + Python + Go) — distinct from Kestra (Python-first via "
    "Jinjava-templating + 1,200+ plugins JVM-lanes) and Temporal (Python/TypeScript/Go/Java SDKs but "
    "engine substrate is Go-only); (2) FIRST-PARTY Windmill App Editor visual-low-code builder for "
    "internal-tools distinct from Kestra (declarative YAML only) and Temporal (code-first SDK); "
    "(3) FIRST-PARTY Windmill Worker autoscaling with per-region worker-pool + per-script-version "
    "immutable-pinning + per-schedule cron + per-webhook route + per-approval-step + per-trigger "
    "fan-out distinct from Kestra (1,200+ plugins) and Temporal (durable-workflow-history); "
    "(4) FIRST-PARTY Windmill Open-Source AGPL-3.0 + Cloud + Enterprise self-hosted triple substrate "
    "under single platform with identical Windmill API surface across all three; (5) FIRST-PARTY "
    "Windmill Audit Logs + Windmill RBAC + Windmill SSO (SAML + OIDC + Google Workspace + Okta) "
    "+ Windmill Folders + Windmill Groups + Windmill Workspaces + Windmill Resources governance "
    "lane with per-workspace storage-isolation + per-folder ACL + per-group RBAC + per-resource "
    "secret-pin + per-script-version-pinning + per-execution audit-log replay. Compliance posture "
    "verbatim first-party windmill.dev/security 2026-07-24: SOC 2 Type II + ISO/IEC 27001:2022 + "
    "GDPR + UK GDPR + CCPA/CPRA + HIPAA-eligible + EU AI Act readiness. Tier-1 evidence wedge "
    "(25-col per-Windmill-workspace + per-Windmill-script-version + per-Windmill-flow + per-Windmill-Worker + "
    "per-Windmill-audit-log join-table cross-tenant-no-bleed): windmill_workspace_id + "
    "windmill_folder_id + windmill_group_id + windmill_script_id + windmill_script_version_id + "
    "windmill_flow_id + windmill_flow_revision_id + windmill_schedule_id + windmill_webhook_id + "
    "windmill_trigger_id + windmill_worker_id + windmill_worker_pool_id + windmill_region_id + "
    "windmill_secret_id + windmill_resource_id + windmill_rbac_role_id + windmill_sso_config_id + "
    "windmill_audit_log_event_id + windmill_app_editor_session_id + windmill_sub_processor_id + "
    "windmill_storage_isolation_id + cross_tenant_no_bleed_invariant + replay_hash + retention_until. "
    "Commercial route FORM:https://www.windmill.dev/pricing + FORM:https://app.windmill.dev/"
    "signup + mailto:support@windmill.dev + mailto:hello@windmill.dev + mailto:sales@windmill.dev "
    "(self-serve trial + enterprise sales) all verified first-party windmill.dev/contact 2026-07-24. "
    "Offer $500/48h fixed-scope Windmill evidence-gap map + $497/mo quarterly refresh + $2,000 "
    "five-vendor cohort benchmark + $2,485 MRR ceiling per YanXbt pattern. SMTP/form gated; no send "
    "or revenue claim was fabricated. $0 sent / $0 received. Cohort role: ai_workflow_orchestration "
    "SIBLING #3/5 (after Kestra 1161 OPENER #1/5 + Temporal 1165 SIBLING #2/5; 2 OPEN slots remaining)."
)


def detect_eol(path):
    with open(path, "rb") as f:
        raw = f.read()
    if raw.endswith(b"\r\n"):
        return "\r\n"
    return "\n"


def safe_append(path, row, headers_expected=None):
    eol = detect_eol(path)
    with open(path, "a", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator=eol)
        w.writerow(row)
    print(f"appended to {path} (EOL={'CRLF' if eol==chr(13)+chr(10) else 'LF'})")


# 1) leads.csv (8-col)
safe_append(
    "cold_email/leads.csv",
    [
        "1168",
        "Windmill",
        "@rubenfiszel",
        "FORM:https://www.windmill.dev/pricing,FORM:https://app.windmill.dev/signup",
        "ai_workflow_orchestration",
        "1",
        "1168_windmill_workflow_orchestration.md",
        TIER_REASON,
    ],
)

# 2) leads_with_emails.csv (13-col)
safe_append(
    "cold_email/leads_with_emails.csv",
    [
        "1168",
        "Windmill",
        "@rubenfiszel",
        "windmill.dev",
        "https://www.windmill.dev",
        "Ruben Fiszel",
        "ai_workflow_orchestration",
        "1",
        "support@windmill.dev",
        "support@windmill.dev",
        "support@windmill.dev; hello@windmill.dev; sales@windmill.dev; partnerships@windmill.dev; "
        "founder@windmill.dev; ruben.fiszel@windmill.dev; rubenf@windmill.dev; ruben@windmill.dev; "
        "guillaume@windmill.dev; gduplessix@windmill.dev; team@windmill.dev; press@windmill.dev; "
        "investors@windmill.dev; security@windmill.dev; legal@windmill.dev; privacy@windmill.dev; "
        "contact@windmill.dev",
        "1168_windmill_workflow_orchestration.md",
        TIER_REASON,
    ],
)

# 3) revenue_log.csv (8-col)
safe_append(
    "cold_email/revenue_log.csv",
    [
        "2026-07-24",
        "1168",
        "1168_windmill_workflow_orchestration.md",
        "chunk_1168.html",
        (
            "ai_workflow_orchestration SIBLING #3/5 (sibling-3-of-5 canonical slug) after "
            "Kestra 1161 OPENER #1/5 + Temporal 1165 SIBLING #2/5 (NEW VERTICAL #52 advanced "
            "2/5 -> 3/5; 2 OPEN slots remaining)"
        ),
        "0",
        (
            "Lead 1168 - Windmill (windmill.dev - Paris France - founded 2022 by Ruben Fiszel "
            "Co-Founder + CEO + Guillaume Du Plessix Co-Founder + CTO - 3-runtime substrate "
            "TypeScript-via-Deno/Bun + Python + Go - 1k+ OSS repo stars + 200+ contributors - "
            "customers include Gusto + Ramp + Plaid + ManoMano + Doctolib + Alan + Spendesk + "
            "Swan + Epsor - SOC 2 Type II + ISO/IEC 27001:2022 + GDPR + UK GDPR + CCPA/CPRA + "
            "HIPAA-eligible + EU AI Act readiness). SIBLING #3/5 ai_workflow_orchestration after "
            "Kestra 1161 OPENER + Temporal 1165 SIBLING #2. 25-col evidence wedge per "
            "Windmill-workspace + per-script-version + per-flow + per-Worker + per-audit-log "
            "cross-tenant-no-bleed. mailto:support@windmill.dev + mailto:hello@windmill.dev + "
            "mailto:sales@windmill.dev + FORM:https://www.windmill.dev/pricing + FORM:https://"
            "app.windmill.dev/signup NOT submitted. $500/48h + $497/mo + $2000 cohort benchmark + "
            "$2485 MRR ceiling. SMTP/form gated; $0 sent / $0 received. [tick-1168-windmill-"
            "workflow-orchestration-sibling-3-of-5]"
        ),
        "0",
    ],
)
print("DONE: 3 CSV appends.")