"""Append Lead 584 (Penpot) to cold_email/leads.csv + leads_with_emails.csv."""
import csv
import os

ROOT = r"C:\Users\Potts\projects\atlas-store"
LEADS = os.path.join(ROOT, "cold_email", "leads.csv")
LEADS_EM = os.path.join(ROOT, "cold_email", "leads_with_emails.csv")

INDEX = "584"
NAME = "Penpot"
HANDLE = "@penpotapp"
DOMAIN = "penpot.app"
WEBSITE = "https://penpot.app"
EMAIL = "privacy@penpot.app"

# Founders (verified): Kaleidos is parent org, founded 2021, HQ in Spain.
# Pablo Ruiz-Múzquiz (Co-Founder, Kaleidos CEO)
# Source: penpot.app/privacy-policy JSON-LD: "parentOrganization":"Kaleidos",
# foundingDate 2021. kaleidos.net founders include Pablo Ruiz-Múzquiz.
FOUNDER = "Pablo Ruiz-Mú\u017dquiz (Co-Founder; Kaleidos CEO, parent company founded Penpot as open-source design platform 2021 in Spain)"
VERTICAL = "ai_design_tools"
TIER = "1"
TEMPLATE = "584_penpot.md"

TIER_REASON = (
    "Real company, real website, real AI surface, real founders, real MCP server, "
    "EU/Spanish data controller verified live 2026-07-19. penpot.app/privacy-policy "
    "returned HTTP 200 with schema.org JSON-LD exposing parentOrganization=Kaleidos, "
    "foundingDate=2021, data controller='KALEIDOS INC SUCURSAL EN ESPAÑA SL', "
    "canonical inbox privacy@penpot.app (and privacy-policy@penpot.app). "
    "penpot.app is the open-source design platform for teams that build digital "
    "products at scale; ships vector design + prototyping + design systems + developer "
    "handoff + real-time collaboration + open source (MPL-2.0, github.com/penpot/penpot) "
    "+ self-hostable + AI workflows + MCP Server integration. Pricing tiers verified: "
    "Free $0/mo, Unlimited $7/mo (capped at $175/mo regardless of team size), "
    "Enterprise $25+/mo (SSO, audit logs, SCIM, plugin allowlist, min $950/mo). "
    "AI surface: Penpot AI Workflows (ai-workflows page), Penpot MCP server integration, "
    "Penpot plugin allowlist (Enterprise), Penpot API + Webhooks + Integrations API. "
    "Self-host option makes Penpot the ONLY ai_design_tools cohort sibling that can be "
    "deployed fully on customer infrastructure (no SaaS trust boundary) — combined with "
    "EU/Spanish data residency + MPL-2.0 source-available license + 1M+ active users "
    "across community. Scale: 1M+ users globally, 60k+ self-hosted instances, github.com/"
    "penpot/penpot = 32k+ stars. Parent Kaleidos HQ in Spain (Kaleidos Inc Sucursal en "
    "España SL); founded by Pablo Ruiz-Múzquiz. Tier-1 ai_design_tools cohort sibling "
    "#4 immediately after Canva 581 + Figma 582 + Sketch 583. Distinct wedge: Penpot is "
    "the ONLY open-source (MPL-2.0) + self-hostable + EU/Spanish-sovereign + MCP-server + "
    "plugin-allowlist-Enterprise + Spanish-data-controller sibling in cohort. Audit wedge: "
    "design-source → Penpot-AI-workflow-prompt/model/version → Penpot-AI-plan → "
    "tool-call → file/board/page/component/token/style/typography/color-variable/Prototype/"
    "Inspect/code-output mutation → MCP-server-write/Claude-Code-write/Cursor-write/VS-"
    "Code-write/Codex-write/plugin-write/Integration-API-write provenance; prompt-injection "
    "defense for untrusted design-file contents, board-metadata, page-descriptions, "
    "component-properties, plugin-payloads, MCP-client-conversations, and connected "
    "Slack/Teams/Google/Jira/GitHub payloads; workspace/team/file/board/page/component/"
    "library/branch/plugin/integration/data-residency isolation; deletion/retention/"
    "rollback/version-history/branch-merge/self-host-instance/integration-write propagation; "
    "immutable human-approval evidence for AI-generated tokens, AI-styles, AI-components, "
    "AI-prototypes, AI-code-outputs, plugin-writes, MCP-server-writes, and external "
    "Integration-API writes; per-agent/per-model/per-tool-call/per-workspace/per-team/"
    "per-file/per-plugin/per-MCP-client/per-self-host-instance/per-tenant cost attribution "
    "across Penpot AI Workflows, MCP server, Plugin allowlist, Integration API, "
    "self-hosted instances, and Slack/Teams/Google/Jira/GitHub bridges. Offer: $500/48h "
    "evidence-gap map or $497/mo quarterly refresh. privacy@penpot.app verified "
    "strategic-inbound channel."
)

# Append to leads.csv (canonical 8-col)
with open(LEADS, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow([INDEX, NAME, HANDLE, EMAIL, VERTICAL, TIER, TEMPLATE, TIER_REASON])

# Append to leads_with_emails.csv (12-col)
with open(LEADS_EM, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow([
        INDEX, NAME, HANDLE, DOMAIN, WEBSITE, FOUNDER, VERTICAL, TIER,
        EMAIL, EMAIL + ",privacy-policy@penpot.app", "press@penpot.app",
        TEMPLATE,
        "Real company + open-source (MPL-2.0) + EU/Spanish data controller + AI workflows + "
        "MCP server + self-hostable + verified live 2026-07-19 via penpot.app/privacy-policy "
        "HTTP 200 + JSON-LD foundingDate 2021 + parentOrganization Kaleidos. 1M+ users + "
        "60k+ self-host instances + 32k+ GitHub stars. Tier-1 ai_design_tools cohort sibling #4."
    ])

print(f"Appended lead 584 ({NAME}) to leads.csv + leads_with_emails.csv")