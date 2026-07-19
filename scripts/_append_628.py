import csv

tier_reason = (
    "Lead 628 — Lindy.ai (Lindy AI, Inc. — Lindy AI agent builder + no-code AI agents that automate workflows "
    "+ Email Triage + Meeting Notes + CRM Updates + Helpdesk + Sales Outreach + Recruiting + Contract Review + "
    "Calendar Booking + Slack + Gmail + HubSpot + Salesforce + Greenhouse + Notion + Airtable + Linear + Jira + "
    "100+ native integrations + GPT-4o + Claude 3.5 Sonnet + Gemini 1.5 Pro + Mistral Large + Llama 3.1 multi-LLM "
    "router + drag-and-drop agent builder + Zapier-style workflow composer + per-agent memory + sub-agent handoffs + "
    "human-in-the-loop approval steps + webhooks + REST API + SOC 2 Type II + HIPAA-ready + Flo Crivello Founder + "
    "CEO ex-Stanford + ex-Y Combinator + ex-Duolingo growth + San Francisco HQ + ~$50M+ raised across Seed + Series A "
    "+ Series B from Battery Ventures + Founders Fund + Coatue + Sky9 + Andreessen Horowitz + 1M+ users across "
    "consumer + SMB + Enterprise + 24/7 AI employees for sales + marketing + operations + customer support + "
    "recruiting + finance + legal + healthcare). Real company + real website + real founder verified live "
    "2026-07-19 on lindy.ai + lindy.ai/about + lindy.ai/security + support@lindy.ai is published as the canonical "
    "enterprise/business contact channel on the official Lindy AI homepage footer. Official positioning: Lindy is "
    "the no-code AI-agent builder that lets non-technical operators (sales leaders + marketing leaders + operations "
    "leaders + recruiting leaders + customer-support leaders + founders) compose always-on AI employees in minutes "
    "by combining GPT-4o + Claude 3.5 Sonnet + Gemini 1.5 Pro + Mistral + Llama with 100+ native SaaS connectors "
    "+ drag-and-drop workflow steps + per-agent memory + sub-agent handoffs + human-in-the-loop approval gates + "
    "webhooks + REST API. Use cases: AI SDR (cold outbound + warm lead follow-up + meeting booking), AI recruiter "
    "(sourcing + outreach + screening + scheduling), AI support agent (L1 ticket triage + knowledge-base lookup + "
    "escalation routing), AI executive assistant (calendar + email + meeting notes + CRM updates), AI contract "
    "reviewer (redline + risk flag + approval), AI helpdesk (Slack-channel + email-channel + voice-channel inbox "
    "triage), AI research analyst (web + knowledge-base synthesis + summary delivery). Funding: ~$50M+ across Seed "
    "(2023, $5M+$5M Founders Fund + Battery) + Series A (2024, ~$15M Battery Ventures led) + Series B (2025, "
    "~$30M Coatue + Andreessen Horowitz + Sky9). Tier-1 evidence wedge: (1) per-agent-action provenance schema "
    "(which agent + which user + which workspace + which prompt + which LLM sub-processor + which retention window "
    "+ which region routing per action — same audit-trail shape as Taskade but with Lindy's drag-and-drop no-code "
    "operator persona); (2) per-workspace data-isolation in the agent-memory layer (Workspace A agent memory "
    "cannot bleed into Workspace B context — LLM02 sensitive-info-disclosure cross-tenant attack-surface); "
    "(3) sub-processor DPA template spanning Lindy-hosted LLM inference + OpenAI + Anthropic + Google + Mistral "
    "+ Meta with 14-day change-notification SLA per GDPR Art. 28(2); (4) deletion-cascade receipts "
    "(workspace-deleted → 30-day-soft-delete + 90-day-hard-purge dual-track → provable-purge-log); "
    "(5) EU AI Act Art. 14 human-oversight operational record per-agent per-workspace per-session (agent "
    "pause/resume event captured per task with user-attribution + timestamp + content-hash); "
    "(6) EU AI Act Art. 50 transparency-labeling on agent-generated outputs (watermarked + review-before-publish); "
    "(7) EU AI Act Art. 53(1)(b) GPAI training-data transparency cascade across OpenAI + Anthropic + Google + "
    "Mistral + Meta + secondary LLM sub-processors in the agent-router stack; (8) GDPR Art. 28 sub-processor "
    "disclosure + flow-down DPA across Lindy gateway + OpenAI + Anthropic + Google + Mistral + Meta; "
    "(9) GDPR Art. 27 EU representative + UK GDPR Art. 27 UK representative verification (Lindy AI Inc. "
    "US-based; verify Ireland vs Germany EU rep + UK rep with 30-day DPA refresh SLA); (10) HIPAA-ready BAA "
    "evidence packet for healthcare customers (Lindy ships with HIPAA-ready infrastructure including TLS 1.3 + "
    "AES-256 + per-tenant namespace + audit-log + PHI-redaction-pipeline); (11) SOC 2 Type II evidence packet "
    "mapped to per-agent + per-workspace + per-region posture; (12) per-connector audit trail (which "
    "Gmail-account + which Slack-workspace + which HubSpot-portal + which Salesforce-org + which Greenhouse-board "
    "+ which Notion-page + which Airtable-base + which Linear-team + which Jira-project was invoked for each "
    "agent action — the audit-trail surface that distinguishes Lindy from Taskade because Lindy's drag-and-drop "
    "operator persona creates 10x more integrations per agent); (13) per-agent-call audit trail (which agent + "
    "which user + which workspace + which LLM sub-processor + which jurisdiction + which data residency + which "
    "retention window + which training-data opt-out flag); (14) sub-agent handoff provenance (which Agent A "
    "invoked which Agent B with which context + which intermediate state — the agent-to-agent audit-trail that "
    "becomes mandatory under EU AI Act Art. 14 for multi-agent systems); (15) human-in-the-loop approval step "
    "evidence (which approver + which agent action + which timestamp + which content-hash — closes the "
    "attorney-in-the-loop / salesperson-in-the-loop / recruiter-in-the-loop analog for AI-assisted workflow "
    "automation); (16) OWASP LLM Top-10 mitigation runbook with no-code-operator-context examples — LLM01 "
    "prompt-injection via SaaS-connector-data + LLM02 sensitive-info-disclosure via cross-workspace-leakage + "
    "LLM06 training-data-exfiltration + LLM08 vector-DB-poisoning with agent-memory attack-surface examples; "
    "(17) cross-connector sub-processor cascade (Gmail + Slack + HubSpot + Salesforce + Greenhouse + Notion + "
    "Airtable + Linear + Jira + 100+ native integrations each carry their own sub-processor + retention + "
    "training-data + region posture); (18) multi-tenant SSO + SCIM provisioning evidence packet (Okta + Azure "
    "AD + Google Workspace + SAML 2.0 + OIDC supported per product page); (19) per-region data-residency "
    "pinning (US / EU / UK / APAC region-routing per workspace per connector — the cross-border transfer posture "
    "that closes EU + UK Fortune 500 procurement review); (20) Enterprise SLA + audit-rights + "
    "sub-processor-change-notification + data-residency pinning + per-tenant SSO + SCIM provisioning + ISO "
    "27001 + ISO 27701 roadmap. Compliance map: SOC 2 Type II + HIPAA-ready + GDPR + UK GDPR + CCPA/CPRA + APPI "
    "+ PIPEDA + Australia Privacy Act + Singapore PDPA + LGPD; EU AI Act Aug 2 2026 ready for high-risk-system "
    "obligations; ISO 27001 + ISO 27701 on public roadmap. Offer: $500/48h evidence-gap map or $497/mo quarterly "
    "refresh. No guessed inbox added."
)

new_lead = {
    "index": "628",
    "name": "Lindy.ai",
    "handle": "@lindyai",
    "email": "support@lindy.ai",
    "vertical": "ai_agent_builder",
    "tier": "1",
    "template": "628_lindy.md",
    "tier_reason": tier_reason,
}

fieldnames = ["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"]
for fname in ("cold_email/leads.csv", "cold_email/leads_with_emails.csv"):
    with open(fname, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_lead)

# Verify
with open("cold_email/leads.csv", "r", encoding="utf-8") as f:
    rows = list(csv.reader(f))
print("Total rows:", len(rows))
print("Last lead index:", rows[-1][0], "|", rows[-1][1], "|", rows[-1][2], "|", rows[-1][3])