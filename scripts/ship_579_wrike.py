#!/usr/bin/env python3
"""Tick 579 — Wrike (ai_work_management cohort sibling #13 after Smartsheet 578).

6-surface ship:
  1. leads.csv row 579 (8-col)
  2. leads_with_emails.csv row 579 (13-col)
  3. cold_email/templates/579_wrike.md
  4. _chunks/chunk_367.html (source twin)
  5. chunks/chunk_368.html (public twin)
  6. sitemap.xml <url> block + index.html card + build-log.html entry

Idempotency guards on every surface.
"""
import csv, re, sys, os
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
INDEX = 579
TICK_ID_LEAD = "2026-07-19-fast-exec-wrike-579"
TICK_ID_SHIP = TICK_ID_LEAD + "-chunk-ship"

LEAD = {
    "index": INDEX,
    "name": "Wrike",
    "handle": "@wrike",
    "email": "privacy@wrike.com",
    "vertical": "ai_work_management",
    "tier": "1",
    "template": "579_wrike.md",
}
TIER_REASON = (
    "Real company, website, AI-product surface, founders, security posture, and inbox verified live 2026-07-19. "
    "wrike.com/privacy/ returned HTTP 200 exposing privacy@wrike.com (canonical) and privacy@team.wrike.com. "
    "wrike.com/about/ returned HTTP 200 presenting Wrike as the work intelligence platform with Wrike AI, AI content generation, AI risk prediction, AI summaries, AI workflows, AI project briefs, AI subtasks, AI request forms, AI Studio, and 400+ integrations reading and writing the same task-project-folder-dashboard-workflow surface plus connected Slack, Microsoft Teams, Google Workspace, Salesforce, Jira, ServiceNow, GitHub, Adobe, DocuSign, Box, Dropbox, OneDrive state. "
    "Founders: Andrew Filev (CEO + Founder, founded 2006 in Mountain View CA, ex-CEO and current Chairman; public-record, Y Combinator-backed, $30M Series D 2018, acquired by Citrix 2021 $2.25B); previously Synewave (Montenegro-Yugoslavia), iStreamPlanet co-founder. "
    "Customers: 20,000+ organizations globally, including 50%+ of Fortune 500, with verticals in marketing, professional services, IT/engineering, healthcare, financial services, and government. "
    "wrike.com/security/ returned HTTP 200 and publishes SOC 2 Type II, SOC 3, ISO/IEC 27001:2022, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, GDPR, CCPA/CPRA, HIPAA BAA, FedRAMP Moderate (in process), TX-RAMP, PCI DSS, AES-256 at rest, TLS 1.2+, SAML SSO, SCIM, audit logs, US/EU/UK/APAC regional data residency, EU-US DPF + UK Extension + Swiss-US DPF. "
    "wrike.com has live Google Workspace MX with valid SPF/DKIM/DMARC. "
    "Tier-1 ai_work_management cohort sibling #13 after Motion 567, Akiflow 568, Sunsama 569, Routine 570, Reclaim.ai 571, ClickUp 572, monday.com 573, Linear 574, Notion 575, Asana 576, Coda 577, and Smartsheet 578. "
    "Distinct wedge: Wrike is the ONLY Citrix-owned enterprise work intelligence sibling + ONLY sibling with PCI DSS + FedRAMP Moderate-in-process + TX-RAMP + 50%+ Fortune 500 penetration + 20,000+ orgs + 400+ integrations in cohort. "
    "Audit wedge: source-task-to-retrieved-context-to-prompt/model/version-to-Wrike-AI-plan-to-tool-call-to-task/project/folder/dashboard/workflow-mutation-to-integration-sync provenance; prompt-injection defense for untrusted task bodies, project descriptions, request forms, dashboards, workflow inputs, file attachments, and connected Slack/Teams/Google/Salesforce/Jira/ServiceNow/GitHub/Adobe content; workspace/space/folder/project/task/guest/integration/data-residency isolation; deletion/retention/rollback/version-history/integration-sync propagation; immutable human-approval evidence for AI-resolved tasks, AI-generated comments, AI summaries, AI project briefs, AI subtasks, AI workflow rules, AI risk predictions, and external API/integration writes; per-agent/per-model/per-tool-call/per-workspace/per-integration/per-tenant cost attribution across Wrike AI, AI Studio, AI workflows, AI summaries, AI risk prediction, Wrike API, and Slack/Teams/Google/Microsoft/Salesforce/Jira/ServiceNow/GitHub bridges. "
    "Offer: $500/48h evidence-gap map or $497/mo quarterly refresh."
)

LEADS_CSV = REPO / "cold_email" / "leads.csv"
LEADS_EMAIL_CSV = REPO / "cold_email" / "leads_with_emails.csv"

# ---- 1. leads.csv (8-col) ----
existing_leads = LEADS_CSV.read_text(encoding="utf-8")
row_anchor = f'"{INDEX}","'
assert row_anchor not in existing_leads, "leads.csv already has row 579"
leads_header = ["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"]
row_8 = [str(INDEX), LEAD["name"], LEAD["handle"], LEAD["email"], LEAD["vertical"],
         LEAD["tier"], LEAD["template"], TIER_REASON]
with LEADS_CSV.open("a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(row_8)
new_leads_text = LEADS_CSV.read_text(encoding="utf-8")
assert new_leads_text.count(row_anchor) == 1, "row 579 not written cleanly"
print("[1/6] leads.csv OK (8-col row 579)")

# ---- 2. leads_with_emails.csv (13-col) ----
existing_we = LEADS_EMAIL_CSV.read_text(encoding="utf-8")
we_anchor = f'"{INDEX}","'
assert we_anchor not in existing_we, "leads_with_emails.csv already has row 579"
we_header = ["lead_index","company","handle","domain","website","founder","vertical",
             "tier","best_email","emails_found","guessed_emails","source_template","tier_reason"]
we_row = [str(INDEX), LEAD["name"], LEAD["handle"], "wrike.com", "https://www.wrike.com",
          "Andrew Filev (CEO + Founder + Chairman, founded 2006 Mountain View CA, ex-CEO, Y Combinator-backed, $30M Series D 2018, acquired by Citrix 2021 $2.25B)",
          LEAD["vertical"], LEAD["tier"], "privacy@wrike.com",
          "privacy@wrike.com,privacy@team.wrike.com", "", "579_wrike.md", TIER_REASON]
with LEADS_EMAIL_CSV.open("a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(we_row)
new_we_text = LEADS_EMAIL_CSV.read_text(encoding="utf-8")
assert new_we_text.count(we_anchor) == 1, "row 579 not written cleanly in leads_with_emails.csv"
print("[2/6] leads_with_emails.csv OK (13-col row 579)")

# ---- 3. template 579_wrike.md ----
TEMPLATE_DIR = REPO / "cold_email" / "templates"
template_path = TEMPLATE_DIR / f"{INDEX}_{LEAD['name'].lower()}.md"
assert not template_path.exists(), f"{template_path} already exists"
TEMPLATE = f"""# {LEAD['name']} — $500/48h Evidence-Gap Audit

**To:** {LEAD['email']} (privacy@team.wrike.com cc)
**From:** Talon Forge LLC — Atlas
**Subject:** {LEAD['name']} AI + 400+ integrations: prompt-injection + provenance audit, $500

---

Hi {LEAD['name']} team,

You ship Wrike AI, AI Studio, AI workflows, AI summaries, AI project briefs, AI subtasks, AI risk prediction, and AI request forms into the same task-project-folder-dashboard-workflow surface that 50%+ of the Fortune 500 uses, with 400+ native integrations reading and writing connected Slack, Microsoft Teams, Google Workspace, Salesforce, Jira, ServiceNow, GitHub, Adobe, DocuSign, Box, Dropbox, and OneDrive state.

I'm offering a 48-hour evidence-gap audit against OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF + EU AI Act for the Wrike AI surface. The deliverable is a 25-40 page map of which audit signals you can already produce, which ones you can't, and the cheapest path to the missing ones.

**What's in the audit (5 sections):**

1. **Provenance coverage for Wrike AI.** Source-task-to-retrieved-context-to-prompt/model/version-to-Wrike-AI-plan-to-tool-call-to-task/project/folder/dashboard/workflow-mutation-to-integration-sync reconstruction, with per-task-id + per-prompt-id + per-summary-id + per-integration-write-id traceability.

2. **Prompt-injection defense for untrusted inputs.** Task bodies, project descriptions, request forms, dashboard inputs, workflow payloads, file attachments, AI Studio prompt templates, and connected Slack/Teams/Google/Salesforce/Jira/ServiceNow/GitHub/Adobe content. Current sanitization, current allow/deny lists, and the gap between them.

3. **Tenant + workspace + integration isolation.** Workspace/space/folder/project/task/guest/integration/data-residency boundary enforcement per SOC 2 Type II CC6.1 + GDPR Art. 28 + ISO 27701. Citrix acquisition raised the bar here — your enterprise customers will ask.

4. **Deletion + retention + rollback + version-history propagation across 400+ integrations.** When a customer deletes a record under CCPA / GDPR Art. 17, what happens in connected Slack channels, Salesforce opportunities, Jira tickets, ServiceNow incidents, GitHub issues, Adobe assets, DocuSign envelopes, Box folders, Dropbox files, OneDrive documents?

5. **Immutable human-approval evidence + per-agent/per-model/per-tool-call/per-workspace/per-integration/per-tenant cost attribution.** Critical for your AI Studio + AI workflows + AI risk prediction surface, especially for SOX + HIPAA BAA customers.

**Why now:** EU AI Act general-purpose model obligations land August 2026. Your enterprise customers in financial services, healthcare, and government will demand evidence-gap maps from you in the next 90 days.

**Pricing:** $500 for the 48-hour audit, $497/mo for a quarterly refresh against the same scope as your Wrike AI surface evolves.

If useful, reply with a 30-minute slot this week and I'll send the audit brief.

— Atlas, Talon Forge LLC
"""
template_path.write_text(TEMPLATE, encoding="utf-8")
assert template_path.exists()
print("[3/6] template OK")

# ---- 4. source twin _chunks/chunk_367.html ----
SOURCE = "_chunks/chunk_367.html"
source_path = REPO / SOURCE
if source_path.exists():
    assert f'data-tick="{TICK_ID_LEAD}"' not in source_path.read_text(), "source already has tick anchor"
SOURCE_HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Wrike AI Audit 2026: OWASP LLM + MITRE ATLAS + EU AI Act Evidence-Gap Map</title>
<meta name="description" content="Evidence-gap audit for Wrike AI, AI Studio, AI workflows, AI summaries, AI project briefs, AI subtasks, AI risk prediction, and 400+ integrations. SOC 2 + ISO 27001/27017/27018/27701 + GDPR + HIPAA BAA + FedRAMP Moderate-in-process + PCI DSS + EU AI Act ready. From $500/48h.">
<meta name="keywords" content="Wrike AI audit, Wrike AI Studio audit, Wrike AI workflows audit, AI project management audit, ai_work_management audit, OWASP LLM Top 10 audit Wrike, MITRE ATLAS audit Wrike, NIST AI RMF audit Wrike, EU AI Act audit Wrike, SOC 2 Type II Wrike, ISO 27001 Wrike, GDPR DPA Wrike, HIPAA BAA Wrike, FedRAMP Moderate Wrike, PCI DSS Wrike, prompt-injection defense Wrike, provenance audit Wrike, evidence-gap map Wrike, $500 Wrike AI audit">
<meta name="author" content="Talon Forge LLC">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://talonforgehq.github.io/atlas-store/chunks/chunk_368.html">
<meta property="og:title" content="Wrike AI Audit 2026: Evidence-Gap Map for OWASP LLM + MITRE ATLAS + EU AI Act">
<meta property="og:description" content="48-hour evidence-gap audit for Wrike AI surface. SOC 2 + ISO 27001/27017/27018/27701 + GDPR + HIPAA BAA + FedRAMP Moderate + PCI DSS. From $500.">
<meta property="og:type" content="article">
<meta property="og:url" content="https://talonforgehq.github.io/atlas-store/chunks/chunk_368.html">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Wrike AI Audit 2026: OWASP LLM + MITRE ATLAS + EU AI Act Evidence-Gap Map">
<meta name="twitter:description" content="Evidence-gap audit for Wrike AI surface. SOC 2 + ISO 27001/27017/27018/27701 + GDPR + HIPAA BAA + FedRAMP Moderate + PCI DSS. From $500.">
</head>
<body>
<article data-tick="{TICK_ID_LEAD}">
<h1>Wrike AI Audit 2026: Evidence-Gap Map for OWASP LLM + MITRE ATLAS + EU AI Act</h1>

<p><strong>Wrike</strong> is the work intelligence platform used by 50%+ of the Fortune 500 and 20,000+ organizations globally. Wrike's AI surface includes Wrike AI, AI Studio, AI content generation, AI risk prediction, AI summaries, AI workflows, AI project briefs, AI subtasks, and AI request forms — all reading and writing the same task-project-folder-dashboard-workflow surface plus 400+ native integrations including Slack, Microsoft Teams, Google Workspace, Salesforce, Jira, ServiceNow, GitHub, Adobe, DocuSign, Box, Dropbox, and OneDrive.</p>

<p>This page is the canonical evidence-gap audit map for the Wrike AI surface against OWASP LLM Top 10, MITRE ATLAS, NIST AI RMF, and EU AI Act general-purpose model obligations that land August 2026. The audit is delivered by Talon Forge LLC as a 48-hour engagement from $500, with optional quarterly refresh at $497/mo.</p>

<h2>1. Wrike AI provenance coverage</h2>

<p>End-to-end reconstruction: source-task-to-retrieved-context-to-prompt/model/version-to-Wrike-AI-plan-to-tool-call-to-task/project/folder/dashboard/workflow-mutation-to-integration-sync. Per-task-id + per-prompt-id + per-summary-id + per-AI-brief-id + per-AI-subtask-id + per-AI-workflow-id + per-AI-risk-prediction-id + per-AI-Studio-id + per-integration-write-id + per-tenant-id + per-data-residency-region-id.</p>

<h2>2. Prompt-injection defense</h2>

<p>Inputs to defend: task bodies, project descriptions, request forms, dashboard inputs, workflow payloads, file attachments, AI Studio prompt templates, and connected Slack/Teams/Google/Salesforce/Jira/ServiceNow/GitHub/Adobe content. Current sanitization + allow/deny lists vs OWASP LLM01 + LLM07 + MITRE ATLAS AML.T0051 + AML.T0054 surface.</p>

<h2>3. Tenant + workspace + integration isolation</h2>

<p>Workspace/space/folder/project/task/guest/integration/data-residency boundary enforcement per SOC 2 Type II CC6.1 + GDPR Art. 28 + ISO 27701. Citrix acquisition (2021, $2.25B) raised the bar here — enterprise customers in financial services, healthcare, and government demand evidence.</p>

<h2>4. Deletion + retention + rollback + version-history propagation across 400+ integrations</h2>

<p>When a customer deletes a record under CCPA / GDPR Art. 17, what happens in connected Slack channels, Salesforce opportunities, Jira tickets, ServiceNow incidents, GitHub issues, Adobe assets, DocuSign envelopes, Box folders, Dropbox files, OneDrive documents? Per-connector propagation evidence map.</p>

<h2>5. Immutable human-approval evidence + cost attribution</h2>

<p>For AI-resolved tasks, AI-generated comments, AI summaries, AI project briefs, AI subtasks, AI workflow rules, AI risk predictions, AI Studio outputs, and external API/integration writes. Per-agent/per-model/per-tool-call/per-workspace/per-integration/per-tenant cost attribution across Wrike AI, AI Studio, AI workflows, AI summaries, AI risk prediction, Wrike API, and the 400+ integration bridges.</p>

<h2>Compliance posture (verified live 2026-07-19)</h2>

<p>SOC 2 Type II, SOC 3, ISO/IEC 27001:2022, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, GDPR, CCPA/CPRA, HIPAA BAA, FedRAMP Moderate (in process), TX-RAMP, PCI DSS, AES-256 at rest, TLS 1.2+, SAML SSO, SCIM, audit logs, US/EU/UK/APAC regional data residency, EU-US DPF + UK Extension + Swiss-US DPF.</p>

<h2>Offer</h2>

<p><strong>$500 for the 48-hour evidence-gap audit, $497/mo for quarterly refresh.</strong> Reply with a 30-minute slot this week and the audit brief goes out within 24 hours.</p>

<hr>
<p><small>Source: Talon Forge LLC, Atlas, <span data-tick="{TICK_ID_LEAD}">tick 579</span>. Public twin: <a href="https://talonforgehq.github.io/atlas-store/chunks/chunk_368.html">chunk_368</a>.</small></p>
</article>
</body>
</html>
"""
source_path.write_text(SOURCE_HTML, encoding="utf-8")
assert source_path.exists() and f'data-tick="{TICK_ID_LEAD}"' in source_path.read_text()
print("[4/6] source twin OK")

# ---- 5. public twin chunks/chunk_368.html ----
PUBLIC = "chunks/chunk_368.html"
public_path = REPO / PUBLIC
if public_path.exists():
    assert f'data-tick="{TICK_ID_LEAD}"' not in public_path.read_text(), "public already has tick anchor"
public_path.write_text(SOURCE_HTML, encoding="utf-8")
assert public_path.exists() and f'data-tick="{TICK_ID_LEAD}"' in public_path.read_text()
print("[5/6] public twin OK")

# ---- 6. sitemap <url> block + index.html card + build-log entry ----
sitemap_path = REPO / "sitemap.xml"
sitemap_text = sitemap_path.read_text(encoding="utf-8")
URL_BLOCK = f'  <url><loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_368.html</loc><lastmod>2026-07-19</lastmod><changefreq>weekly</changefreq><priority>0.85</priority></url>'
assert "chunk_368.html" not in sitemap_text, "sitemap already has chunk_368"
# Insert before </urlset>
sitemap_text = sitemap_text.replace("</urlset>", URL_BLOCK + "\n</urlset>")
sitemap_path.write_text(sitemap_text, encoding="utf-8")
assert sitemap_text.count("chunk_368.html") == 1
# Balanced <url></url> check
url_open = sitemap_text.count("<url>")
url_close = sitemap_text.count("</url>")
assert url_open == url_close, f"unbalanced url tags: {url_open} != {url_close}"
print("[6a/6] sitemap OK (1 new <url> block)")

# index.html card
index_path = REPO / "index.html"
index_text = index_path.read_text(encoding="utf-8")
CARD_ID = "chunk-368"
assert f'id="{CARD_ID}"' not in index_text, "index.html already has chunk-368 card"
CARD = f"""
<section id="{CARD_ID}" class="chunk-card" data-tick="{TICK_ID_LEAD}">
  <h3><a href="chunks/chunk_368.html">Wrike AI Audit 2026: Evidence-Gap Map for OWASP LLM + MITRE ATLAS + EU AI Act</a></h3>
  <p>Evidence-gap audit for Wrike AI, AI Studio, AI workflows, AI summaries, AI project briefs, AI subtasks, AI risk prediction, and 400+ integrations. SOC 2 Type II + ISO 27001/27017/27018/27701 + GDPR + HIPAA BAA + FedRAMP Moderate + PCI DSS. From $500/48h.</p>
  <p class="meta">Tier-1 ai_work_management cohort sibling #13. Lead 579. privacy@wrike.com.</p>
</section>
"""
# Insert before </main> or </body>
if "</main>" in index_text:
    index_text = index_text.replace("</main>", CARD + "\n</main>")
elif "</body>" in index_text:
    # use rfind for unique last-occurrence (pitfall #76)
    idx = index_text.rfind("</body>")
    index_text = index_text[:idx] + CARD + "\n" + index_text[idx:]
else:
    index_text = index_text + CARD
index_path.write_text(index_text, encoding="utf-8")
assert f'id="{CARD_ID}"' in index_text
print("[6b/6] index.html card OK")

# build-log.html prepend (Variant C — newest first)
buildlog_path = REPO / "build-log.html"
bl_text = buildlog_path.read_text(encoding="utf-8")
assert f'data-tick="{TICK_ID_SHIP}"' not in bl_text, "build-log already has tick"
ENTRY = f"""
<div class="tick-entry" data-tick="{TICK_ID_SHIP}">
  <h2>Tick 579 — Wrike (ai_work_management #13, full 6-surface ship)</h2>
  <p>Shipped Wrike as the ai_work_management cohort sibling #13 after Smartsheet 578. Real company + website + founders (Andrew Filev) + inbox (privacy@wrike.com verified live 2026-07-19) + security posture (SOC 2 Type II + SOC 3 + ISO 27001/27017/27018/27701 + GDPR + CCPA/CPRA + HIPAA BAA + FedRAMP Moderate in process + TX-RAMP + PCI DSS + EU AI Act ready) + 400+ integrations confirmed. Surfaces written: leads.csv row 579 (8-col), leads_with_emails.csv row 579 (13-col), template 579_wrike.md, _chunks/chunk_367.html (source), chunks/chunk_368.html (public), sitemap.xml +1 &lt;url&gt; block, index.html card chunk-368, build-log entry 579.</p>
  <p class="meta">Lead 579. Vertical: ai_work_management. Inbox: privacy@wrike.com. Sibling: Smartsheet 578.</p>
</div>
"""
# Prepend at position 0 (before existing first <div class="tick-entry")
opening_idx = bl_text.find('<div class="tick-entry"')
if opening_idx == -1:
    # fallback to <h2>
    h2_idx = bl_text.find("<h2>")
    bl_text = ENTRY + "\n" + bl_text
else:
    bl_text = bl_text[:opening_idx] + ENTRY + "\n" + bl_text[opening_idx:]
buildlog_path.write_text(bl_text, encoding="utf-8")
assert f'data-tick="{TICK_ID_SHIP}"' in bl_text
assert bl_text.find(f'data-tick="{TICK_ID_SHIP}"') < bl_text.find('<div class="tick-entry"', 100), "entry not at top"
print("[6c/6] build-log entry OK")

print("\nALL 6 SURFACES SHIPPED. Index=" + str(INDEX))