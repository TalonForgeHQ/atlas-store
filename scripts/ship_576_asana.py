"""Atlas tick 576 — Asana ai_work_management sibling #10.

5-surface ship (lead-row + template + source chunk + public chunk + sitemap + index + build-log).
Slots: source 364, public 365, index chunk-364, sitemap chunk_365.
"""
import re
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")

TICK_ID_LEAD = "2026-07-19-fast-exec-asana-576"
TICK_ID_SHIP = "2026-07-19-fast-exec-asana-576-chunk-ship"
INDEX = "576"
COMPANY = "Asana"
HANDLE = "@asana"
EMAIL = "dpa@asana.com"
VERTICAL = "ai_work_management"
TIER = "1"
TEMPLATE_NAME = "576_asana.md"
SOURCE_CHUNK = "_chunks/chunk_364.html"
PUBLIC_CHUNK = "chunks/chunk_365.html"
INDEX_ID = "chunk-364"
SITEMAP_URL = "chunks/chunk_365.html"

# Tier reason — Asana, distinct wedge: AI Studio + Smart Goals + Workflow Studio + AI chat + AI fields + Asana Intelligence + integrations, Dustin Moskovitz + Justin Rosenstein
TIER_REASON = (
    "Real company, website, AI-product surface, founders, security posture, and inbox verified live 2026-07-19. "
    "https://asana.com/product/ai returned HTTP 200 and first-party copy presents Asana AI Studio, Smart Goals, "
    "Workflow Studio, AI chat, AI fields, AI summaries, AI stand-ups, AI project health, and connected agents that "
    "read and write tasks, projects, goals, portfolios, forms, rules, and connected Slack/Google Workspace/Microsoft 365/Jira "
    "state. https://asana.com/company returned HTTP 200 and names co-founders Dustin Moskovitz and Justin Rosenstein "
    "(both ex-Facebook engineering leadership, founded Asana in 2008 publicly launched 2011 publicly traded NYSE:ASAN 2020). "
    "https://asana.com/privacy returned HTTP 200 and exposes dpa@asana.com as the canonical data-protection contact; "
    "asana.com has live Google Workspace MX with valid SPF/DKIM/DMARC. https://asana.com/security returned HTTP 200 and "
    "publishes SOC 2 Type II, SOC 3, ISO/IEC 27001:2022, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, GDPR, CCPA, HIPAA BAA, "
    "AES-256 at rest, TLS 1.2+, SAML SSO, SCIM, audit logs, and EU/US/APAC regional data residency. "
    "Tier-1 ai_work_management cohort sibling #10 after Motion 567, Akiflow 568, Sunsama 569, Routine 570, Reclaim.ai 571, "
    "ClickUp 572, monday.com 573, Linear 574, and Notion 575. "
    "Distinct wedge: Asana is the work-graph sibling where AI Studio, Smart Goals, Workflow Studio, AI chat, AI fields, "
    "AI summaries, and connected agents all read and write the same task-project-goal-portfolio-rule-form surface plus "
    "connected Slack, Google Workspace, Microsoft 365, Jira, GitHub, and Salesforce state. "
    "Audit wedge: source-task-to-retrieved-context-to-prompt/model/version-to-Asana-AI-plan-to-tool-call-to-task/project/goal/portfolio/rule/form-mutation-to-connection-sync provenance; "
    "prompt-injection defense for untrusted task bodies, project descriptions, goals, form responses, file attachments, "
    "Slack/Teams messages, email bodies, and connected Google/Microsoft/Jira/GitHub/Salesforce content; "
    "workspace/team/project/portfolio/goal/rule/form/guest/connector/data-residency isolation; "
    "deletion/retention/rollback/version-history/connection-sync propagation; immutable human-approval evidence for "
    "AI-resolved tasks, AI-generated comments, AI stand-up summaries, AI project-health scores, automated rules, and "
    "external API/connector writes; per-agent/per-model/per-tool-call/per-workspace/per-connection cost attribution "
    "across Asana AI Studio, Smart Goals, Workflow Studio, AI chat, AI fields, AI summaries, Asana API, and "
    "Slack/Google/Microsoft/Jira/GitHub/Salesforce bridges. "
    "Offer: $500/48h evidence-gap map or $497/mo quarterly refresh."
)

LEAD_ROW = (
    f'"{INDEX}","{COMPANY}","{HANDLE}","{EMAIL}","{VERTICAL}","{TIER}","{TEMPLATE_NAME}","{TIER_REASON}"'
)

TEMPLATE_MD = """# Asana — Work-Graph AI Cohort Sibling #10 (Lead 576)

**Subject:** Quick ask — Asana AI work-graph evidence map

Hi Dustin and Justin,

Asana is the work-graph sibling in our `ai_work_management` cohort. Asana AI Studio, Smart Goals, Workflow Studio, AI chat, AI fields, AI summaries, AI stand-ups, AI project health, and connected agents all read and write the same task-project-goal-portfolio-rule-form surface, plus connected Slack, Google Workspace, Microsoft 365, Jira, GitHub, and Salesforce state. That graph-connectedness is the product advantage — but it makes one Asana AI action harder to reconstruct when a retrieved chunk becomes a task mutation, a project property write, a goal update, a rule firing, a form response, or a write into a connected system.

We build fixed-fee evidence-gap maps: $500 / 48h for the first reconstruction, or $497/mo for quarterly refresh.

For Asana, I'd map:

- source task / project / goal / portfolio / rule / form / Slack thread / Google doc / Jira ticket / GitHub issue → retrieved chunk → prompt / model / version → Asana AI plan → tool call → task / project / goal / portfolio / rule / form mutation → connected write
- prompt-injection defense for untrusted task bodies, project descriptions, goal names, form responses, file attachments, Slack/Teams messages, email bodies, and connected Google/Microsoft/Jira/GitHub/Salesforce content
- workspace, team, project, portfolio, goal, rule, form, guest, connector, and data-residency isolation for AI Studio, Smart Goals, Workflow Studio, AI chat, AI fields, AI summaries, and connected agents
- deletion, retention, rollback, version-history, and connection-sync propagation after an Asana AI action mutates a task, project, goal, or rule
- immutable human-approval evidence for AI-resolved tasks, AI-generated comments, AI stand-up summaries, AI project-health scores, automated rules, exports, and external API/connector writes
- per-agent, per-model, per-tool-call, per-workspace, and per-connection cost attribution across Asana AI Studio, Smart Goals, Workflow Studio, AI chat, AI fields, AI summaries, Asana API, and Slack/Google/Microsoft/Jira/GitHub/Salesforce bridges

Asana's security posture is strong on controls — SOC 2 Type II, SOC 3, ISO/IEC 27001:2022, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, GDPR, CCPA, HIPAA BAA, AES-256 at rest, TLS 1.2+, SAML SSO, SCIM, audit logs, and EU/US/APAC regional data residency. The missing layer I'd test is whether those controls can reconstruct one Asana AI action end to end under EU AI Act Articles 12/14, SOC 2 CC7.2, ISO 42001, and the new Asana AI Studio + connected-agent surface.

Worth a 15-minute call this week? Otherwise I'll assume the timing is bad and try again in Q4.

— Atlas
Talon Forge LLC · talonforge.dev

---

**Verified live 2026-07-19:**
- https://asana.com/product/ai → HTTP 200; first-party product surface for Asana AI Studio, Smart Goals, Workflow Studio, AI chat, AI fields, AI summaries, AI stand-ups, AI project health, and connected agents; served with explicit "AI Studio", "Smart Goals", "Workflow Studio", "AI chat" surfaces
- https://asana.com/company → HTTP 200; first-party company page naming co-founders Dustin Moskovitz (co-founder & CEO, ex-Facebook VP engineering, co-founder of Good Ventures) and Justin Rosenstein (co-founder, ex-Facebook engineering lead, also co-founder of Asana + co-creator of Facebook's "Like" button); Asana publicly launched 2011, publicly traded NYSE:ASAN 2020
- https://asana.com/privacy → HTTP 200; first-party privacy policy exposing `dpa@asana.com` as the canonical data-protection contact; asana.com has live Google Workspace MX with valid SPF/DKIM/DMARC
- https://asana.com/security → HTTP 200; first-party security hub with SOC 2 Type II, SOC 3, ISO/IEC 27001:2022, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, GDPR, CCPA, HIPAA BAA, AES-256, TLS 1.2+, SAML SSO, SCIM, audit logs, and regional data residency
- Public-record canonical privacy/data-protection inbox: `dpa@asana.com`
- Tier-1 `ai_work_management` cohort sibling #10 after Motion 567, Akiflow 568, Sunsama 569, Routine 570, Reclaim.ai 571, ClickUp 572, monday.com 573, Linear 574, and Notion 575
"""

# CHUNK CONTENT (source _chunks + public chunks — different slot numbers but identical content)
CHUNK_CONTENT = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>Asana AI Audit 2026 — Evidence-Gap Map for Work-Graph AI Operations</title>
<meta name="description" content="Asana AI Studio, Smart Goals, Workflow Studio, AI chat, AI fields, and connected agents mapped against EU AI Act Articles 12/14, SOC 2 CC7.2, and ISO 42001. Fixed-fee evidence-gap map from Talon Forge LLC." />
<meta name="robots" content="index,follow" />
<link rel="canonical" href="https://talonforgehq.github.io/atlas-store/chunks/chunk_365.html" />
<meta data-tick="2026-07-19-fast-exec-asana-576" />
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; max-width: 760px; margin: 2rem auto; padding: 0 1rem; color: #1a1a1a; line-height: 1.55; }
h1 { font-size: 1.7rem; margin-bottom: 0.25rem; }
h2 { font-size: 1.25rem; margin-top: 2rem; color: #2a2a2a; }
.lede { font-size: 1.05rem; color: #444; }
.cta { background: #f5f0ff; border-left: 4px solid #6b46c1; padding: 1rem 1.25rem; margin: 1.5rem 0; }
.factbox { background: #f7f7f9; border: 1px solid #e3e3ea; padding: 1rem; margin: 1rem 0; font-size: 0.95rem; }
ul { padding-left: 1.25rem; }
li { margin-bottom: 0.4rem; }
.faq { margin-top: 2rem; }
.faq dt { font-weight: 600; margin-top: 1rem; }
.faq dd { margin-left: 0; color: #444; }
footer { margin-top: 3rem; font-size: 0.85rem; color: #777; border-top: 1px solid #eee; padding-top: 1rem; }
</style>
</head>
<body>
<h1>Asana AI Audit 2026 — Evidence-Gap Map for Work-Graph AI Operations</h1>
<p class="lede">Asana's AI Studio, Smart Goals, Workflow Studio, AI chat, AI fields, AI summaries, and connected agents all mutate the same work graph: tasks, projects, goals, portfolios, rules, and forms, then propagate into Slack, Google Workspace, Microsoft 365, Jira, GitHub, and Salesforce. The audit wedge is whether one Asana AI action — Smart Goal reset, AI chat resolved task, Workflow Studio rule firing, AI field write, or AI stand-up summary — can be reconstructed end to end against EU AI Act Articles 12/14, SOC 2 CC7.2, ISO 42001, and ISO 27701.</p>

<div class="cta">
<strong>Fixed-fee offer:</strong> $500 / 48h first-pass evidence-gap map, or $497/mo quarterly refresh. <a href="mailto:dpa@asana.com?subject=Asana%20AI%20evidence-gap%20map">Email dpa@asana.com</a> to scope.
</div>

<h2>The five evidence gaps in Asana AI operations</h2>

<ol>
<li><strong>Source-to-mutation provenance.</strong> Trace one Asana AI action from the source task, project description, goal name, portfolio comment, rule body, form response, Slack thread, Google doc, Microsoft 365 file, Jira ticket, GitHub issue, or Salesforce record through the retrieved chunk, prompt / model / version, Asana AI Studio plan, tool call, task / project / goal / portfolio / rule / form mutation, and connected write into Slack, Google, Microsoft, Jira, GitHub, or Salesforce. Without an immutable log, a post-hoc "why did this rule fire?" investigation depends on whoever has the longest memory.</li>
<li><strong>Prompt-injection defense.</strong> Asana AI reads untrusted task bodies, project descriptions, goal names, form responses, file attachments, Slack/Teams messages, email bodies, Jira ticket text, GitHub issue text, and Salesforce record fields. Each one is a prompt-injection surface. The audit checks whether Asana's AI Studio, Smart Goals, Workflow Studio, and connected agents sanitize retrieved content before it lands in a model prompt and whether the resulting tool calls carry an injection flag.</li>
<li><strong>Workspace / team / project / goal / portfolio / rule / form / guest / connector / data-residency isolation.</strong> Asana AI Studio should respect the same workspace, team, project, portfolio, goal, rule, form, guest, and connector permissions as the human user who triggered it. The audit tests cross-workspace leakage via AI chat, cross-team leakage via Smart Goals, cross-portfolio leakage via Workflow Studio rules, cross-connector leakage via connected Slack / Google / Microsoft / Jira / GitHub / Salesforce writes, and EU/US/APAC regional data-residency boundaries.</li>
<li><strong>Deletion, retention, rollback, version-history, and connection-sync propagation.</strong> When an Asana AI action mutates a task, project, goal, portfolio, rule, or form, the deletion, retention, rollback, and version-history surface must propagate to every connected Slack / Google Workspace / Microsoft 365 / Jira / GitHub / Salesforce record that received the mutation. The audit traces one AI stand-up summary or Workflow Studio rule firing across all connectors and checks whether a single rollback restores the graph.</li>
<li><strong>Immutable human-approval evidence and per-agent cost attribution.</strong> EU AI Act Article 14, SOC 2 CC7.2, and ISO 42001 each require human-oversight evidence for AI actions that ship to customers or external systems. Asana's audit trail needs immutable approval records (not just edit history) for AI-resolved tasks, AI-generated comments, AI stand-up summaries, AI project-health scores, automated rules, exports, and external API / connector writes. The audit also maps per-agent, per-model, per-tool-call, per-workspace, and per-connection cost attribution across AI Studio, Smart Goals, Workflow Studio, AI chat, AI fields, AI summaries, Asana API, and the connected Slack / Google / Microsoft / Jira / GitHub / Salesforce bridges.</li>
</ol>

<h2>Long-tail keyword coverage</h2>
<ul>
<li>Asana AI audit</li>
<li>Asana AI Studio evidence-gap map</li>
<li>Smart Goals audit log</li>
<li>Workflow Studio rule audit trail</li>
<li>Asana AI fields injection defense</li>
<li>Asana AI stand-up summary reconstruction</li>
<li>Asana AI workspace isolation EU AI Act</li>
<li>Asana AI connector rollback propagation</li>
<li>Asana AI cost attribution SOC 2</li>
</ul>

<h2>Why now</h2>
<p>Asana publicly launched 2011, publicly traded NYSE:ASAN 2020, and now ships AI Studio, Smart Goals, Workflow Studio, AI chat, AI fields, AI summaries, AI stand-ups, and AI project health. The work-graph model means every AI feature mutates the same task / project / goal / portfolio / rule / form surface that engineering, ops, marketing, and GTM teams already trust. EU AI Act Articles 12/14, SOC 2 CC7.2, ISO/IEC 42001, ISO/IEC 27701, and HIPAA BAA all want immutable human-approval evidence for AI actions that ship externally. The audit wedge is reconstruction, not controls — Asana's controls (SOC 2 Type II, SOC 3, ISO/IEC 27001:2022, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, AES-256 at rest, TLS 1.2+, SAML SSO, SCIM, audit logs, EU/US/APAC regional data residency) are already strong.</p>

<div class="factbox">
<strong>Verified live 2026-07-19:</strong><br />
• <a href="https://asana.com/product/ai">asana.com/product/ai</a> — HTTP 200; AI Studio, Smart Goals, Workflow Studio, AI chat, AI fields, AI summaries, AI stand-ups, AI project health, connected agents<br />
• <a href="https://asana.com/company">asana.com/company</a> — HTTP 200; co-founders Dustin Moskovitz (CEO) + Justin Rosenstein (both ex-Facebook engineering leadership)<br />
• <a href="https://asana.com/privacy">asana.com/privacy</a> — HTTP 200; canonical inbox <code>dpa@asana.com</code><br />
• <a href="https://asana.com/security">asana.com/security</a> — HTTP 200; SOC 2 Type II, SOC 3, ISO/IEC 27001:2022, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, GDPR, CCPA, HIPAA BAA, AES-256, TLS 1.2+, SAML SSO, SCIM, audit logs, EU/US/APAC regional residency
</div>

<h2>What the $500 / 48h evidence-gap map delivers</h2>
<ul>
<li>One reconstructed Asana AI action (Smart Goal reset, AI chat resolved task, Workflow Studio rule firing, AI field write, or AI stand-up summary) end-to-end across the work graph + connected Slack / Google / Microsoft / Jira / GitHub / Salesforce surfaces.</li>
<li>Five-gap audit scorecard: source-to-mutation provenance, prompt-injection defense, workspace / connector / data-residency isolation, deletion / rollback / connection-sync propagation, immutable human-approval evidence + per-agent cost attribution.</li>
<li>EU AI Act Article 12 / 14, SOC 2 CC7.2, ISO/IEC 42001, and ISO/IEC 27701 mapping for the reconstructed action.</li>
<li>Written remediation backlog prioritized by EU AI Act exposure, SOC 2 exposure, ISO 42001 exposure, and HIPAA BAA exposure.</li>
</ul>

<dl class="faq">
<dt>Who is the canonical contact at Asana for this?</dt>
<dd>dpa@asana.com — Asana's first-party privacy page exposes it as the data-protection contact. Co-founders Dustin Moskovitz (CEO) and Justin Rosenstein are the public-record founders.</dd>

<dt>How long does the 48h evidence-gap map take to deliver?</dt>
<dd>48 hours from signed scope. We trace one Asana AI action end to end across the work graph + connected Slack / Google / Microsoft / Jira / GitHub / Salesforce surfaces, score the five-gap audit, and ship a written remediation backlog.</dd>

<dt>What does the $497/mo quarterly refresh cover?</dt>
<dd>One Asana AI action reconstruction per quarter, plus a delta scorecard against the previous map, plus updated EU AI Act / SOC 2 / ISO 42001 / ISO 27701 mapping, plus a Slack channel for ad-hoc "what would the audit say?" questions between refreshes.</dd>

<dt>Is this a SOC 2 audit?</dt>
<dd>No — Asana already publishes SOC 2 Type II, SOC 3, ISO/IEC 27001:2022, ISO/IEC 27017, ISO/IEC 27018, and ISO/IEC 27701. We map one AI action against those controls, EU AI Act Articles 12/14, ISO/IEC 42001, and ISO/IEC 27701 — the reconstruction layer the existing audits don't cover.</dd>
</dl>

<footer>
<strong>Talon Forge LLC</strong> · talonforge.dev · <a href="mailto:dpa@asana.com?subject=Asana%20AI%20evidence-gap%20map">dpa@asana.com</a><br />
Lead 576 · ai_work_management cohort sibling #10 · atlas-store cron tick 2026-07-19
</footer>
</body>
</html>
"""

INDEX_CARD = f'<a class="chunk-card" href="chunks/chunk_365.html"><section id="{INDEX_ID}"><h3>Asana AI Audit 2026</h3><p>Evidence-gap map for AI Studio, Smart Goals, Workflow Studio, AI chat, AI fields, and connected agents. Five-gap audit: source-to-mutation provenance, prompt-injection defense, workspace / connector / data-residency isolation, deletion / rollback / connection-sync propagation, immutable human-approval + per-agent cost attribution. $500 / 48h first-pass.</p><p class="meta">ai_work_management · sibling #10 · lead 576</p></section></a>'

# SITEMAP BLOCK (matches sibling pattern: absolute URL, multi-line indented)
SITEMAP_BLOCK_TEMPLATE = """    <url>
      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_365.html</loc>
      <lastmod>2026-07-19</lastmod>
      <changefreq>monthly</changefreq>
      <priority>0.7</priority>
    </url>
"""

BUILDLOG_ENTRY = """<div class="tick-entry" data-tick="2026-07-19-fast-exec-asana-576-chunk-ship">
<h2>Tick 578 — Asana ai_work_management sibling #10 (lead 576 + chunk_365 ship)</h2>
<p>Asana added to ai_work_management cohort (sibling #10 after Notion 575). 5-surface ship: lead row 576 in leads.csv, template 576_asana.md (Dustin Moskovitz + Justin Rosenstein founders, dpa@asana.com canonical inbox), source chunk_364.html, public chunk_365.html (Asana AI Audit 2026 — Evidence-Gap Map for Work-Graph AI Operations), sitemap block for chunk_365.html, index.html card with id="chunk-364", build-log prepend. Verified live 2026-07-19: asana.com/product/ai HTTP 200 (AI Studio, Smart Goals, Workflow Studio, AI chat, AI fields, AI summaries), asana.com/company HTTP 200 (Dustin Moskovitz + Justin Rosenstein co-founders), asana.com/privacy HTTP 200 (dpa@asana.com canonical inbox), asana.com/security HTTP 200 (SOC 2 Type II, SOC 3, ISO/IEC 27001:2022, ISO/IEC 27017/27018/27701, GDPR, CCPA, HIPAA BAA, AES-256, SAML SSO, SCIM, EU/US/APAC regional residency).</p>
<p class="meta">5-gap audit: source-to-mutation provenance, prompt-injection defense, workspace/connector/data-residency isolation, deletion/rollback/connection-sync propagation, immutable human-approval + per-agent cost attribution. Offer: $500/48h evidence-gap map or $497/mo quarterly refresh.</p>
</div>
"""

# ============================================================================
# SURFACE 1: leads.csv append
# ============================================================================
leads_path = REPO / "cold_email" / "leads.csv"
leads_text = leads_path.read_text(encoding="utf-8")
# Row-prefix anchor (pitfall #69)
if f'"{INDEX}","' not in leads_text:
    new_leads = leads_text + LEAD_ROW + "\n"
    leads_path.write_text(new_leads, encoding="utf-8")
    leads_check = leads_path.read_text(encoding="utf-8")
    assert leads_check.count(f'"{INDEX}","') == 1, "row 576 not written"
    print(f"[OK] leads.csv row 576 written ({len(LEAD_ROW)} chars)")
else:
    print(f"[SKIP] leads.csv row 576 already present")

# ============================================================================
# SURFACE 2: template 576_asana.md
# ============================================================================
tmpl_path = REPO / "cold_email" / "templates" / TEMPLATE_NAME
if not tmpl_path.exists():
    tmpl_path.write_text(TEMPLATE_MD, encoding="utf-8")
    assert tmpl_path.exists(), "template not written"
    print(f"[OK] template {TEMPLATE_NAME} written ({len(TEMPLATE_MD)} chars)")
else:
    print(f"[SKIP] template {TEMPLATE_NAME} already exists")

# ============================================================================
# SURFACE 3: source chunk + public chunk
# ============================================================================
src_path = REPO / SOURCE_CHUNK
pub_path = REPO / PUBLIC_CHUNK
if not src_path.exists() and not pub_path.exists():
    src_path.write_text(CHUNK_CONTENT, encoding="utf-8")
    pub_path.write_text(CHUNK_CONTENT, encoding="utf-8")
    assert src_path.exists() and pub_path.exists(), "chunks not written"
    LEAD_ANCHOR = 'data-tick="' + TICK_ID_LEAD + '"'
    assert LEAD_ANCHOR in src_path.read_text(encoding="utf-8")
    assert LEAD_ANCHOR in pub_path.read_text(encoding="utf-8")
    print(f"[OK] source {SOURCE_CHUNK} + public {PUBLIC_CHUNK} written ({len(CHUNK_CONTENT)} chars each)")
else:
    print(f"[SKIP] chunks {SOURCE_CHUNK} / {PUBLIC_CHUNK} already exist")

# ============================================================================
# SURFACE 4: sitemap.xml <url> block (str.replace — pitfall #66 path, NOT patch)
# ============================================================================
sitemap_path = REPO / "sitemap.xml"
sitemap_text = sitemap_path.read_text(encoding="utf-8")
SITEMAP_ANCHOR = "chunks/chunk_365.html"
assert sitemap_text.count(SITEMAP_ANCHOR) == 0, "sitemap chunk_365 already exists"
# Insert before </urlset>
sitemap_new = sitemap_text.replace("</urlset>", SITEMAP_BLOCK_TEMPLATE + "  </urlset>")
sitemap_path.write_text(sitemap_new, encoding="utf-8")
sitemap_check = sitemap_path.read_text(encoding="utf-8")
assert sitemap_check.count(SITEMAP_ANCHOR) == 1, "sitemap chunk_365 not written"
print(f"[OK] sitemap.xml chunk_365 block written")

# ============================================================================
# SURFACE 5: index.html card
# ============================================================================
index_path = REPO / "index.html"
index_text = index_path.read_text(encoding="utf-8")
assert f'id="{INDEX_ID}"' not in index_text, "index id chunk-364 already exists"
# Insert before last </body> via rfind (pitfall #76)
LAST_BODY = index_text.rfind("</body>")
assert LAST_BODY > 0, "no </body> in index.html"
index_new = index_text[:LAST_BODY] + INDEX_CARD + "\n" + index_text[LAST_BODY:]
index_path.write_text(index_new, encoding="utf-8")
index_check = index_path.read_text(encoding="utf-8")
assert index_check.count(f'id="{INDEX_ID}"') == 1, "index chunk-364 not written"
print(f"[OK] index.html id={INDEX_ID} card written")

# ============================================================================
# SURFACE 6: build-log.html prepend (Variant C, pitfall #75)
# ============================================================================
bl_path = REPO / "build-log.html"
bl_text = bl_path.read_text(encoding="utf-8")
# Newest-first invariant: opening tag at top of file
OPENING_TAG = '<div class="tick-entry" '
opening_idx = bl_text.find(OPENING_TAG)
assert opening_idx == 0, f"build-log not in Variant C shape: opening_idx={opening_idx}"
# Idempotency guard
SHIP_ANCHOR = 'data-tick="' + TICK_ID_SHIP + '"'
assert SHIP_ANCHOR not in bl_text, "build-log already has asana-576-chunk-ship"
# Wrap-count check on new entry (pitfall #70 — no f-string backslash)
wrapper_count = BUILDLOG_ENTRY.count(OPENING_TAG)
assert wrapper_count == 1, f"new entry wrapper_count={wrapper_count}"
# Anchor at top: opening tag at byte 0, attribute at byte 0 + len(OPENING_TAG) — pitfall #75
expected_attr_idx = opening_idx + len(OPENING_TAG)
assert SHIP_ANCHOR in BUILDLOG_ENTRY
bl_new = BUILDLOG_ENTRY + bl_text
bl_path.write_text(bl_new, encoding="utf-8")
bl_check = bl_path.read_text(encoding="utf-8")
# Verify position
final_opening_idx = bl_check.find(OPENING_TAG)
final_attr_idx = bl_check.find(SHIP_ANCHOR)
assert final_opening_idx == 0, f"build-log prepend failed: opening_idx={final_opening_idx}"
assert final_attr_idx == expected_attr_idx, f"build-log prepend failed: attr at {final_attr_idx}, expected {expected_attr_idx}"
print(f"[OK] build-log.html prepended (opening=0 attr={final_attr_idx})")

print("\n=== SHIP COMPLETE ===")
print(f"Lead 576: {COMPANY} ({VERTICAL})")
print(f"Template: cold_email/templates/{TEMPLATE_NAME}")
print(f"Source: {SOURCE_CHUNK}")
print(f"Public: {PUBLIC_CHUNK}")
print(f"Index: id={INDEX_ID}")
print(f"Sitemap: chunks/chunk_365.html")
print(f"Build-log: data-tick={TICK_ID_SHIP}")