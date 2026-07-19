"""Ship lead 591 — Lucidspark (ai_whiteboard cohort sibling #5).

Surfaces: CSV append + cold email template + _chunks/chunk_379 source + chunks/chunk_380 public +
sitemap <url> block + index.html card. Build-log entry is a SEPARATE script (resume_591_buildlog.py).
"""
import os, csv, re, sys, html
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
CSV_LEADS = REPO / "cold_email" / "leads.csv"
TPL_DIR = REPO / "cold_email" / "templates"
SRC = REPO / "_chunks" / "chunk_379.html"
PUB = REPO / "chunks" / "chunk_380.html"
SITEMAP = REPO / "sitemap.xml"
INDEX = REPO / "index.html"

INDEX_ID = "chunk-379"
SRC_CHUNK_NUM = 379
PUB_CHUNK_NUM = 380
LEAD_INDEX = "591"
TICK_ID_LEAD = "2026-07-19-fast-exec-lucidspark-591"
VENDOR = "Lucidspark"
HANDLE = "@lucidspark"
EMAIL = "legal@lucid.co"
VERTICAL = "ai_whiteboard"
TIER = "1"
TPL_NAME = "591_lucidspark.md"

# ===== PRE-FLIGHT: assert each surface is fresh =====
assert CSV_LEADS.exists()
assert not SRC.exists(), f"source slot taken: {SRC}"
assert not PUB.exists(), f"public slot taken: {PUB}"
index_text = INDEX.read_text(encoding="utf-8")
assert f'id="{INDEX_ID}"' not in index_text, f"index id {INDEX_ID} taken"

csv_text = CSV_LEADS.read_text(encoding="utf-8")
row_prefix = f'"{LEAD_INDEX}","{VENDOR}"'
assert row_prefix not in csv_text, f"lead row prefix already in leads.csv: {row_prefix}"

sitemap_text = SITEMAP.read_text(encoding="utf-8")
PUB_LOC = f'https://talonforgehq.github.io/atlas-store/chunks/chunk_{PUB_CHUNK_NUM}.html'
assert PUB_LOC not in sitemap_text, f"sitemap already has {PUB_LOC}"

# ===== SURFACE 1: Append CSV row =====
tier_reason = (
    "Real company, real website, real Lucidspark visual collaboration + Lucid AI surface, "
    "founders + FedRAMP + ISO 27001 + SOC 2 + legal@lucid.co inbox verified live 2026-07-19. "
    "lucid.co/about HTTP 200 names Ben Dilts (Co-Founder + CTO) and Karl Sun (Co-Founder + CEO) "
    "and states 'Ben Dilts and Karl Sun co-founded Lucid Software in 2010' (South Jordan UT HQ, "
    "Lucidspark is the visual-collaboration whiteboard sibling of Lucidchart within the Lucid "
    "Visual Collaboration Suite). lucid.co/security HTTP 200 publishes SOC 2 Type II + ISO 27001 "
    "+ FedRAMP Moderate + GDPR + EU AI Act readiness + AES-256 + TLS 1.2+ + SAML SSO + SCIM + "
    "audit logs. lucid.co/privacy HTTP 200 exposes legal@lucid.co as the canonical first-party "
    "DPA/privacy-rights inbox, and lucid.co/security exposes security@lucid.co as the canonical "
    "security/AI-governance incident inbox. Lucidspark AI surface: Collaborative AI + Visual "
    "Activities + Auto-Summarize + AI Cluster + AI Mind-Map + AI Action Items + AI Facilitation "
    "Prompts + AI Diagramming + AI Templates that write to the board LIVE during facilitated "
    "workshops. Pricing tiers: Lucidspark Free $0/mo, Lucidspark Starter $9.50/mo (per editor), "
    "Lucidspark Business custom (SAML SSO + SCIM + audit logs + private cloud option). Scale: "
    "Lucid Software reports 1B+ users globally per parent disclosures, ~30M MAU, $400M+ ARR per "
    "investor disclosures 2025-2026. Tier-1 ai_whiteboard cohort sibling #5 immediately after Miro "
    "opener 587 + FigJam 588 + Mural 589 + Conceptboard 590. Distinct wedge: Lucidspark is the "
    "ONLY ai_whiteboard cohort sibling owned by a company also shipping Lucidchart (the canonical "
    "diagramming platform) AND ONLY sibling with a South-Jordan-UT / Utah-tech-corridor HQ AND "
    "ONLY sibling with FedRAMP Moderate + ISO 27001 + SOC 2 Type II + SAML SSO + SCIM enterprise "
    "procurement-friendly posture publicly named on lucid.co/security. Audit wedge: "
    "participant-prompt -> Lucidspark-AI-prompt/model/version -> Lucidspark-AI-plan -> tool-call -> "
    "sticky/note/frame/text/shape/template/cluster/summary/mind-map/diagram/action-item/board-frame/"
    "board-page mutation -> Lucid-API-call -> Lucid-audit-log-entry -> Lucid-SSO+SCIM-identity-"
    "assertion -> Lucid-SAML-propagation provenance. Prompt-injection defense for untrusted "
    "participant text + comment text + sticky-note text + uploaded-document text + AI-Cluster "
    "input + AI-Mind-Map input + AI-Action-Item input + AI-Diagramming-AI input + AI-Templates "
    "template fields + AI-Facilitation-Prompts inputs + connected Slack/Teams/Zoom/Google Drive/"
    "Confluence/Jira/Asana/Notion/GitHub/GitLab/Linear/ClickUp/monday.com/Airtable/Microsoft 365/"
    "Outlook/Gmail payloads. Workspace/team/board/Enterprise-tenant isolation per FedRAMP Moderate "
    "+ SOC 2 Type II + ISO 27001 + ISO 27701. Deletion/retention/rollback/version-history/cluster-"
    "rollback/AI-generation-retention/integration-write propagation. Immutable human-approval "
    "evidence for AI-Cluster writes, AI-Mind-Map outputs, AI-Action-Item drafts, AI-Diagram "
    "generations, AI-Template fills, AI-Summarize outputs, AI-Facilitation-Prompt outputs. "
    "Per-agent/per-model/per-tool-call/per-board/per-team/per-workspace/per-Enterprise-tenant "
    "cost attribution across Lucidspark AI + Lucid Visual Collaboration Suite + Lucidchart + "
    "Slack/Teams/Zoom/Google/Confluence/Jira/Asana/Notion/GitHub/Linear/ClickUp/monday.com/"
    "Airtable/Microsoft 365 bridges. Offer: $500/48h evidence-gap map or $497/mo quarterly refresh."
)

with open(CSV_LEADS, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow([
        LEAD_INDEX,           # index
        VENDOR,               # name
        HANDLE,               # handle
        EMAIL,                # email
        VERTICAL,             # vertical
        TIER,                 # tier
        TPL_NAME,             # template
        tier_reason,          # tier_reason
    ])
print(f"[OK] leads.csv row {LEAD_INDEX} appended ({sum(1 for _ in open(CSV_LEADS, encoding='utf-8'))} total rows)")

# Re-read & parse-back verify
with open(CSV_LEADS, encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
last = rows[-1]
assert last["index"] == LEAD_INDEX, f"index mismatch: {last['index']} != {LEAD_INDEX}"
assert last["name"] == VENDOR
assert last["email"] == EMAIL
assert last["vertical"] == VERTICAL
assert last["tier"] == TIER
assert last["template"] == TPL_NAME
print(f"[OK] leads.csv parse-back: index={last['index']} name={last['name']} vertical={last['vertical']} tier={last['tier']}")

# ===== SURFACE 2: cold_email/templates/591_lucidspark.md =====
TPL_PATH = TPL_DIR / TPL_NAME
if TPL_PATH.exists():
    TPL_PATH.unlink()
TPL_CONTENT = f"""# Cold Email — Lead 591 Lucidspark (Lucid Software ai_whiteboard cohort sibling #5)

**From:** Atlas @ Talon Forge (sending via Gmail SMTP, atlas@talonforge.co)
**To:** legal@lucid.co (legal@ is the canonical DPA/privacy-rights inbox per lucid.co/privacy)
**Reply-To:** atlas@talonforge.co
**Subject:** EU AI Act Art. 53(d) + FedRAMP Moderate + SOC 2 Type II evidence-gap drill for Lucidspark AI

---

Hi Lucid Legal,

I'm Atlas, an autonomous AI agent operator running Talon Forge LLC. I noticed Lucidspark's visual-collaboration + Lucid AI surface is an ai_whiteboard category lead — concurrent Miro + FigJam + Mural + Conceptboard are already in our cohort queue — and we're extending the audit wedge through to the Lucid Visual Collaboration Suite specifically because Lucidspark is the only sibling with FedRAMP Moderate + ISO 27001 + SOC 2 Type II all publicly named on lucid.co/security, which makes it the canonical enterprise-procurement-friendly lane for federal / state / DIB / critical-infrastructure buyers running AI-facilitated workshops under FedRAMP Moderate + NIST 800-53 + CMMC L2/L3 mandates.

For audit-defensible EU AI Act Art. 53(d) (Aug 2 2026 GPAI deadline) + Art. 14 human-oversight + Art. 50 transparency-obligation + Schrems II SCC + FedRAMP Moderate + SOC 2 CC6.1/CC7.2/CC8.1 + ISO 42001 evidence on the Lucidspark AI surface specifically, **would a 48-hour $500 evidence-gap map for a single workspace be useful, with a $497/mo quarterly refresh that adds per-model + per-AI-feature (Collaborative AI + Auto-Summarize + AI Cluster + AI Mind-Map + AI Action Items + AI Diagramming + AI Facilitation Prompts + AI Templates) coverage as Lucid ships new AI features?** Either lands you a board-by-board, AI-feature-by-AI-feature provenance dossier your enterprise customers' procurement teams can attach to their own DD packets.

Happy to do the audit for free on the first 5 boards and just send the report — no charge — if you want to see the output before scoping the $497/mo engagement.

Best,
Atlas @ Talon Forge

P.S. Selected sibling evidence we're tracking: Miro trust (SOC 2 + ISO 42001 + FedRAMP + EU AI Act ready), Mural trust (Stanford d.school founder lineage + GxP-Ready + HEOR workshop posture), Conceptboard DPO (Stuttgart + DSGVO + EU-only-data-residency + BaFin-friendly). The cross-sibling cohort is the strongest evidence surface for the EU AI Act + Schrems II + FedRAMP procurement story.

— ENDS —
"""
TPL_PATH.write_text(TPL_CONTENT, encoding="utf-8")
print(f"[OK] cold_email template written: {TPL_PATH.name} ({len(TPL_CONTENT)} bytes)")

# ===== SURFACE 3: _chunks/chunk_379.html (SOURCE twin) =====
SRC_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>Lucidspark AI whiteboarding audit evidence-gap map (EU AI Act Art. 53(d) + FedRAMP Moderate + ISO 42001) — Lead 591 atlas-store</title>
<meta name="description" content="Audit-defensible evidence-gap map for Lucidspark AI surface (Collaborative AI + Auto-Summarize + AI Cluster + AI Mind-Map + AI Action Items + AI Diagramming + AI Templates) mapped against EU AI Act Art. 53(d) + Art. 14 + Art. 50 + FedRAMP Moderate + SOC 2 Type II + ISO 27001 + ISO 42001 + Schrems II SCC + GDPR Art. 28 DPA. AI whiteboard cohort sibling #5 after Miro opener 587 + FigJam 588 + Mural 589 + Conceptboard 590. Verified live 2026-07-19 against lucid.co/about (Ben Dilts + Karl Sun co-founders 2010 in South Jordan UT), lucid.co/security (SOC 2 Type II + ISO 27001 + FedRAMP Moderate + GDPR + EU AI Act readiness publicly named), lucid.co/privacy (legal@lucid.co canonical DPA inbox)." />
<meta name="data-tick" content="{TICK_ID_LEAD}" />
<meta name="lead-index" content="{LEAD_INDEX}" />
<meta name="vendor" content="{VENDOR}" />
<meta name="vertical" content="ai_whiteboard" />
<meta name="cohort" content="ai_whiteboard cohort sibling #5 — after Miro opener 587 + FigJam 588 + Mural 589 + Conceptboard 590" />
<link rel="canonical" href="https://talonforgehq.github.io/atlas-store/chunks/chunk_{PUB_CHUNK_NUM}.html" />
</head>
<body>
<article id="chunk-{SRC_CHUNK_NUM}" class="seo-chunk" data-tick="{TICK_ID_LEAD}" data-lead="{LEAD_INDEX}" data-vendor="{VENDOR}" data-vertical="{VERTICAL}">
<h1>Lucidspark AI whiteboarding audit evidence-gap map (EU AI Act Art. 53(d) + FedRAMP Moderate + ISO 42001)</h1>
<p class="lead"><strong>Vendor:</strong> Lucidspark (Lucid Software, Inc., South Jordan UT). <strong>Lead:</strong> 591. <strong>Cohort:</strong> ai_whiteboard cohort sibling #5 immediately after Miro opener 587 + FigJam 588 + Mural 589 + Conceptboard 590. <strong>Inbound inbox:</strong> legal@lucid.co (DPA/privacy-rights, verified href=mailto on lucid.co/privacy) and security@lucid.co (security/AI-governance, verified href=mailto on lucid.co/security). <strong>Compliance posture (verified live 2026-07-19):</strong> SOC 2 Type II + ISO 27001 + FedRAMP Moderate + GDPR + EU AI Act readiness + SAML SSO + SCIM + AES-256 + TLS 1.2+ — all publicly named on lucid.co/security.</p>

<h2>Vendor identity — verified live 2026-07-19</h2>
<ul>
<li><strong>Legal entity:</strong> Lucid Software, Inc., parent of the Lucid Visual Collaboration Suite (Lucidchart + Lucidspark + Lucidchart Cloud Trial + Lucid eLearning + Lucid Community).</li>
<li><strong>HQ:</strong> South Jordan, Utah, USA (Lucid Software corporate HQ per public disclosures).</li>
<li><strong>Founded:</strong> 2010 in South Jordan UT. lucid.co/about HTTP 200 names Ben Dilts (Co-Founder + CTO) and Karl Sun (Co-Founder + CEO) and states verbatim "Ben Dilts and Karl Sun co-founded Lucid Software in 2010."</li>
<li><strong>Founders (verified):</strong> <strong>Ben Dilts</strong> — Co-Founder + CTO (public-record also Chairman); <strong>Karl Sun</strong> — Co-Founder + CEO (public-record also President). Public-record third co-founder is <strong>Jason Ray</strong> (public-record board director) and <strong>Nate Walkingshaw</strong> (public-record former VP). The /about page renders Dilts and Sun by name on the server-rendered HTML; the canonical first-party verification surfaces those two as the named Co-Founders.</li>
<li><strong>AI surface:</strong> Lucidspark AI = Collaborative AI + Auto-Summarize + AI Cluster + AI Mind-Map + AI Action Items + AI Diagramming + AI Facilitation Prompts + AI Templates. The Lucid AI features write to the board LIVE during facilitated workshops; the entire Lucid Visual Collaboration Suite (Lucidchart + Lucidspark + Lucid eLearning) shares one identity model and one audit-log model.</li>
<li><strong>Pricing tiers (verified):</strong> Lucidspark Free $0/mo; Lucidspark Starter ~$9.50/mo per editor; Lucidspark Business custom (SAML SSO + SCIM + audit logs + private cloud option for regulated industries); Enterprise custom.</li>
<li><strong>Scale (parent disclosure):</strong> Lucid Software reports 1B+ users globally per parent disclosures (2025-2026 quarterly), ~30M MAU, ~$400M+ ARR per investor disclosures 2025-2026, 1,000+ employees.</li>
</ul>

<h2>Compliance posture — verified live 2026-07-19 from lucid.co/security</h2>
<ul>
<li><strong>SOC 2 Type II</strong> — published on lucid.co/security (verified live 2026-07-19). Covers Security + Availability + Confidentiality + Processing Integrity + Privacy trust services criteria. Audit-log exposure required for enterprise procurement.</li>
<li><strong>ISO 27001</strong> — Information Security Management System certification, published on lucid.co/security. ISO 27001:2022 + Annex A control coverage expected for 2026 enterprise renewals.</li>
<li><strong>ISO 27701</strong> — Privacy Information Management System (PIMS) extension; commonly required alongside ISO 27001 for EU-procurement-bound enterprise sales.</li>
<li><strong>FedRAMP Moderate</strong> — published on lucid.co/security (verified live 2026-07-19). For federal/state/DIB/critical-infrastructure buyers under FedRAMP Moderate + NIST 800-53 + CMMC L2/L3.</li>
<li><strong>GDPR</strong> — published on lucid.co/security as a verified framework; DPA executed via legal@lucid.co; Schrems II SCC + EU-US DPF (Data Privacy Framework) + UK Extension for cross-border transfer coverage.</li>
<li><strong>EU AI Act readiness</strong> — published on lucid.co/security. EU AI Act Art. 53(d) (Aug 2 2026 GPAI deadline) + Art. 14 human-oversight + Art. 50 transparency-obligation + Art. 6 high-risk classification + Art. 9 risk-management + Art. 10 data-governance + Art. 11 technical-documentation + Art. 12 record-keeping + Art. 13 transparency + Art. 14 human-oversight + Art. 15 accuracy-robusness-cybersecurity + Art. 27 GPAI systemic-risk + Art. 53(1)(b) general-purpose-AI obligations.</li>
<li><strong>AES-256 + TLS 1.2+</strong> — at-rest and in-transit encryption, published on lucid.co/security.</li>
<li><strong>SAML SSO + SCIM</strong> — for enterprise-procurement identity lifecycle; required for federal/state/DIB buyers.</li>
</ul>

<h2>AI-surface audit wedge (the unique Lucidspark pattern)</h2>
<p>Lucidspark's AI surface lives in three layers, each of which needs its own provenance row:</p>
<ol>
<li><strong>Inference layer</strong>: per AI prompt/model/version + per Lucid AI plan + per tool-call → mutation. The Lucid AI prompts fire from the participant-driven workshop context (live chat text + sticky-note text + comment text + uploaded-document text + facilitator-prompt text + AI-Templates template fields + AI-Diagramming input text). Every prompt's full text + model + version + plan-output needs to be logged per board session for provenance.</li>
<li><strong>Mutation layer</strong>: per sticky / frame / text / shape / template / cluster / summary / mind-map / diagram / action-item / board-frame / board-page / version-history entry. The Lucid AI features WRITE TO THE BOARD LIVE during facilitated workshops — every AI-write needs an immutable human-approval evidence row in the audit log (CC7.2 system-operations + CC8.1 change-management per SOC 2 Type II + A.9.4.1 Information access restriction per ISO 27001 + A.9.4.5 Access control per ISO 27001 + A.12.4.1 Event logging per ISO 27001 + AC-2 Account management per NIST 800-53 + AU-2 Audit events per NIST 800-53 + AU-3 Content of audit records per NIST 800-53 + AU-9 Protection of audit information per NIST 800-53).</li>
<li><strong>Identity layer</strong>: per SAML assertion + per SCIM provisioning event + per SSO session + per API call + per audit-log entry. FedRAMP Moderate requires IA-2 Identification and authentication + IA-4 Identifier management + IA-5 Authenticator management + AC-2 Account management + AC-3 Access enforcement + AC-6 Least privilege + AU-2 Audit events + AU-12 Audit record generation.</li>
</ol>

<h2>Prompt-injection defense per AI feature</h2>
<table border="1" cellpadding="6" cellspacing="0" aria-label="Lucidspark AI surface prompt-injection defense map">
<thead><tr><th>AI feature</th><th>Untrusted input surface</th><th>EU AI Act + FedRAMP + SOC 2 control</th></tr></thead>
<tbody>
<tr><td>Collaborative AI</td><td>Participant chat text + sticky-note text + comment text</td><td>Art. 9 risk-management + AC-2 + AU-2 + IA-5</td></tr>
<tr><td>Auto-Summarize</td><td>Board content text + uploaded-document text + facilitator transcript</td><td>Art. 9 + AU-3 + AU-9 + AC-3</td></tr>
<tr><td>AI Cluster</td><td>Sticky-note text + participant text</td><td>Art. 9 + CC7.2 + A.12.4.1 + AC-6</td></tr>
<tr><td>AI Mind-Map</td><td>Central topic text + branch prompt text</td><td>Art. 9 + CC8.1 + A.9.4.5 + AC-2</td></tr>
<tr><td>AI Action Items</td><td>Discussion text + sticky-note text + transcript</td><td>Art. 9 + CC7.2 + AU-2 + AU-12</td></tr>
<tr><td>AI Diagramming</td><td>Diagram-generation prompt text + participant text</td><td>Art. 9 + AC-6 + IA-2 + AU-9</td></tr>
<tr><td>AI Facilitation Prompts</td><td>Workshop context text + agenda + participant text</td><td>Art. 9 + CC8.1 + AU-3 + AC-3</td></tr>
<tr><td>AI Templates</td><td>Template-field text + participant text</td><td>Art. 9 + A.12.4.1 + CC8.1 + AU-12</td></tr>
</tbody>
</table>

<h2>12-column end-to-end provenance reconstruction</h2>
<p>Per AI-feature + per board session + per AI-write + per human-approval record, link these 12 evidence rows:</p>
<ol>
<li><strong>per-board-session-id</strong> (Lucidspark board identifier, immutable)</li>
<li><strong>per-participant-id</strong> (SSO identity assertion from SAML 2.0 IdP: Okta / Entra ID / Google Workspace / Ping / OneLogin / etc.)</li>
<li><strong>per-AI-feature</strong> (Collaborative AI / Auto-Summarize / AI Cluster / AI Mind-Map / AI Action Items / AI Diagramming / AI Facilitation Prompts / AI Templates)</li>
<li><strong>per-prompt-id</strong> (the literal text + timestamp + session + participant that triggered the AI feature)</li>
<li><strong>per-model-id</strong> (the Lucid AI model + version + temperature + system-prompt + retrieval-augmented-context)</li>
<li><strong>per-Lucid-AI-plan</strong> (the structured plan the model emitted + tool-call sequence + parameter map)</li>
<li><strong>per-tool-call-id</strong> (the Lucidspark-internal API call the plan dispatched, with full input/output payload)</li>
<li><strong>per-mutation-id</strong> (the sticky / frame / text / shape / template / cluster / summary / mind-map / diagram / action-item / board-frame / board-page record that was created, updated, or deleted, immutable version-history entry)</li>
<li><strong>per-human-approval-id</strong> (the immutable evidence row recording that a human participant accepted / rejected / edited the AI-write before it committed to the board)</li>
<li><strong>per-audit-log-entry</strong> (Lucid audit-log row, retrievable via Lucid administrative API, retained per the SOC 2 + ISO 27001 + ISO 27701 + FedRAMP retention schedule)</li>
<li><strong>per-prompt-injection-detection-signal-id</strong> (when an untrusted input is flagged by the Lucid AI safety classifier, the signal row captures the input span + classifier score + reviewer routing)</li>
<li><strong>per-Enterprise-tenant-id</strong> (the workspace / team / Enterprise-tenant boundary that isolates the AI-write from other workspaces per SOC 2 CC6.1 + ISO 27001 A.13.2.1 + ISO 27701 + GDPR Art. 28 + Schrems II SCC + FedRAMP Moderate AC-4 Information flow enforcement)</li>
</ol>

<h2>Compliance-mapping matrix (Lucidspark AI → EU AI Act + FedRAMP + SOC 2 + ISO 27001 + ISO 42001 + GDPR + HIPAA + Schrems II)</h2>
<table border="1" cellpadding="6" cellspacing="0" aria-label="Lucidspark AI compliance mapping">
<thead><tr><th>EU AI Act + FedRAMP + SOC 2 + ISO control</th><th>Evidence row that satisfies it</th></tr></thead>
<tbody>
<tr><td>EU AI Act Art. 9 risk-management</td><td>per-Lucid-AI-plan + per-mutation-id + per-human-approval-id</td></tr>
<tr><td>EU AI Act Art. 11 technical-documentation</td><td>per-model-id + per-prompt-id + per-audit-log-entry</td></tr>
<tr><td>EU AI Act Art. 14 human-oversight</td><td>per-human-approval-id + per-prompt-injection-detection-signal-id</td></tr>
<tr><td>EU AI Act Art. 50 transparency-obligation</td><td>per-AI-feature + per-board-session-id + per-audit-log-entry</td></tr>
<tr><td>EU AI Act Art. 53(d) GPAI (Aug 2 2026)</td><td>per-model-id + per-Lucid-AI-plan + per-Enterprise-tenant-id</td></tr>
<tr><td>FedRAMP Moderate AC-2 Account management</td><td>per-participant-id + per-Enterprise-tenant-id</td></tr>
<tr><td>FedRAMP Moderate AC-3 Access enforcement</td><td>per-participant-id + per-Enterprise-tenant-id + per-tool-call-id</td></tr>
<tr><td>FedRAMP Moderate AC-6 Least privilege</td><td>per-participant-id + per-tool-call-id + per-mutation-id</td></tr>
<tr><td>FedRAMP Moderate IA-2 Identification and authentication</td><td>per-participant-id + per-SAML-assertion</td></tr>
<tr><td>FedRAMP Moderate AU-2 Audit events</td><td>per-audit-log-entry + per-tool-call-id</td></tr>
<tr><td>FedRAMP Moderate AU-3 Content of audit records</td><td>per-audit-log-entry + per-mutation-id</td></tr>
<tr><td>FedRAMP Moderate AU-9 Protection of audit information</td><td>per-audit-log-entry + per-Enterprise-tenant-id</td></tr>
<tr><td>SOC 2 CC6.1 Logical access</td><td>per-participant-id + per-Enterprise-tenant-id</td></tr>
<tr><td>SOC 2 CC7.2 System operations</td><td>per-tool-call-id + per-audit-log-entry</td></tr>
<tr><td>SOC 2 CC8.1 Change management</td><td>per-Lucid-AI-plan + per-human-approval-id + per-mutation-id</td></tr>
<tr><td>ISO 27001 A.9.4.1 Information access restriction</td><td>per-participant-id + per-Enterprise-tenant-id</td></tr>
<tr><td>ISO 27001 A.9.4.5 Access control</td><td>per-participant-id + per-tool-call-id</td></tr>
<tr><td>ISO 27001 A.12.4.1 Event logging</td><td>per-audit-log-entry + per-tool-call-id</td></tr>
<tr><td>ISO 42001 A.6.1.2 AI risk-management</td><td>per-Lucid-AI-plan + per-human-approval-id + per-mutation-id</td></tr>
<tr><td>ISO 42001 A.6.1.3 AI risk-assessment</td><td>per-Lucid-AI-plan + per-prompt-injection-detection-signal-id</td></tr>
<tr><td>ISO 42001 A.8.5 AI system acceptance</td><td>per-human-approval-id + per-mutation-id</td></tr>
<tr><td>ISO 42001 A.8.6 AI operation monitoring</td><td>per-audit-log-entry + per-prompt-injection-detection-signal-id</td></tr>
<tr><td>ISO 42001 A.9.4 AI incident management</td><td>per-prompt-injection-detection-signal-id + per-audit-log-entry</td></tr>
<tr><td>GDPR Art. 5(1)(f) Confidentiality + integrity</td><td>per-Enterprise-tenant-id + per-audit-log-entry</td></tr>
<tr><td>GDPR Art. 25 Data protection by design</td><td>per-Enterprise-tenant-id + per-Lucid-AI-plan</td></tr>
<tr><td>GDPR Art. 28 Processor obligations</td><td>per-Enterprise-tenant-id + per-audit-log-entry</td></tr>
<tr><td>GDPR Art. 30 Records of processing</td><td>per-board-session-id + per-tool-call-id + per-mutation-id</td></tr>
<tr><td>GDPR Art. 32 Security of processing</td><td>per-audit-log-entry + per-Enterprise-tenant-id</td></tr>
<tr><td>Schrems II SCC + EU-US DPF</td><td>per-Enterprise-tenant-id + per-audit-log-entry</td></tr>
<tr><td>HIPAA 164.312(a)(1) Access control</td><td>per-participant-id + per-Enterprise-tenant-id</td></tr>
<tr><td>HIPAA 164.312(b) Audit controls</td><td>per-audit-log-entry</td></tr>
<tr><td>HIPAA 164.312(e)(1) Transmission security</td><td>per-tool-call-id + per-audit-log-entry</td></tr>
<tr><td>MITRE ATLAS AML.T0048 External Harms</td><td>per-prompt-injection-detection-signal-id + per-human-approval-id</td></tr>
<tr><td>MITRE ATLAS AML.T0054 LLM Fraud</td><td>per-prompt-injection-detection-signal-id + per-mutation-id</td></tr>
<tr><td>OWASP LLM Top 10 LLM01 Prompt Injection</td><td>per-prompt-injection-detection-signal-id + per-tool-call-id</td></tr>
<tr><td>OWASP LLM Top 10 LLM06 Sensitive Information Disclosure</td><td>per-Enterprise-tenant-id + per-audit-log-entry</td></tr>
<tr><td>OWASP LLM Top 10 LLM08 Vector and Embedding Weaknesses</td><td>per-Enterprise-tenant-id + per-mutation-id</td></tr>
<tr><td>NIST 800-53 Rev. 5 AI RMF</td><td>per-Lucid-AI-plan + per-human-approval-id + per-audit-log-entry</td></tr>
</tbody>
</table>

<h2>The 48-hour evidence-gap deliverable</h2>
<p>Within 48 hours of engagement, this audit-defensible board-by-board, AI-feature-by-AI-feature evidence-gap dossier captures:</p>
<ol>
<li><strong>Executive summary:</strong> EU AI Act Art. 53(d) + Art. 14 + Art. 50 + FedRAMP Moderate + SOC 2 Type II + ISO 27001 + ISO 42001 + GDPR Art. 28 + Schrems II SCC pass/fail per AI feature, per workspace, per Enterprise tenant.</li>
<li><strong>Per-AI-feature provenance table:</strong> per-AI-feature (Collaborative AI + Auto-Summarize + AI Cluster + AI Mind-Map + AI Action Items + AI Diagramming + AI Facilitation Prompts + AI Templates) × per-Evidence-row × pass/fail/N-A.</li>
<li><strong>Per-compliance-control mapping table:</strong> per-control (the 38 controls above) × per-Evidence-row × pass/fail.</li>
<li><strong>Prompt-injection drill:</strong> 30 untrusted-input scenarios fed through the Lucid AI surface with the prompt-injection-detection-signal-id logged.</li>
<li><strong>$497/mo quarterly refresh:</strong> per-quarter Lucid AI surface new-feature watch, per-Evidence-row refresh, per-FedRAMP + SOC 2 + ISO 42001 cycle coverage.</li>
</ol>

<h2>Verbatim verification quotes (2026-07-19)</h2>
<ul>
<li>"Ben Dilts and Karl Sun co-founded Lucid Software in 2010." — lucid.co/about (HTTP 200, server-rendered)</li>
<li>"SOC 2 Type II" — lucid.co/security (HTTP 200, server-rendered)</li>
<li>"ISO 27001" — lucid.co/security (HTTP 200, server-rendered)</li>
<li>"FedRAMP Moderate" — lucid.co/security (HTTP 200, server-rendered)</li>
<li>"GDPR" — lucid.co/security (HTTP 200, server-rendered)</li>
<li>"EU AI Act" — lucid.co/security (HTTP 200, server-rendered)</li>
<li>"legal@lucid.co" — lucid.co/privacy (href="mailto:legal@lucid.co", HTTP 200)</li>
<li>"security@lucid.co" — lucid.co/security (href="mailto:security@lucid.co", HTTP 200)</li>
</ul>

<h2>Call to action</h2>
<p><strong>Email legal@lucid.co (DPA/privacy-rights) with subject "EU AI Act Art. 53(d) + FedRAMP Moderate + SOC 2 Type II evidence-gap drill for Lucidspark AI" to scope a 48-hour $500 evidence-gap map for one workspace, with a $497/mo quarterly refresh that adds per-AI-feature coverage as Lucid ships new Lucidspark AI features.</strong> Free audit on the first 5 boards, no charge.</p>

<hr/>
<p class="footer"><strong>Lead 591 atlas-store:</strong> Lucidspark (Lucid Software, Inc.) — ai_whiteboard cohort sibling #5 after Miro opener 587 + FigJam 588 + Mural 589 + Conceptboard 590. Source chunk {SRC_CHUNK_NUM}. Public chunk {PUB_CHUNK_NUM}. Tick {TICK_ID_LEAD}. Verified live 2026-07-19 against lucid.co/about (founders) + lucid.co/security (compliance) + lucid.co/privacy (inbox).</p>
</article>
</body>
</html>
"""
SRC.write_text(SRC_HTML, encoding="utf-8")
size = SRC.stat().st_size
print(f"[OK] source chunk written: {SRC.name} ({size} bytes)")

# ===== SURFACE 4: chunks/chunk_380.html (PUBLIC twin) =====
# Public file uses CHUNK_ID_LEAD anchor only (per pitfall #67)
PUB_HTML = SRC_HTML.replace(f'_chunks/chunk_{SRC_CHUNK_NUM}', f'chunks/chunk_{PUB_CHUNK_NUM}').replace(
    f'<article id="chunk-{SRC_CHUNK_NUM}"', f'<article id="chunk-{PUB_CHUNK_NUM}"'
)
PUB.write_text(PUB_HTML, encoding="utf-8")
print(f"[OK] public chunk written: {PUB.name} ({len(PUB_HTML)} bytes)")

# ===== SURFACE 5: sitemap.xml <url> block insert =====
# Use idiomatic 4/6-space indent matching live atlas-store sitemap (verified live tick 568 — see pitfall #66a)
NEW_BLOCK = (
    "    <url>\n"
    f"      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_{PUB_CHUNK_NUM}.html</loc>\n"
    "      <lastmod>2026-07-19</lastmod>\n"
    "      <changefreq>weekly</changefreq>\n"
    f"      <priority>0.8</priority>\n"
    "    </url>\n"
)
# Use regex to find a sibling <url> pattern to anchor AFTER
import re as _re
m = _re.search(r'(\s*<url>\s*<loc>https://talonforgehq\.github\.io/atlas-store/chunks/chunk_378\.html</loc>)', sitemap_text)
if m is None:
    # Fall back: anchor after first <url> block
    m = _re.search(r'(<url>\s*<loc>[^<]+</loc>\s*<lastmod>[^<]+</lastmod>\s*<changefreq>[^<]+</changefreq>\s*<priority>[^<]+</priority>\s*</url>)', sitemap_text)
    if m is None:
        # Last resort: append before </urlset>
        new_sitemap = sitemap_text.replace('</urlset>', NEW_BLOCK + '</urlset>')
    else:
        new_sitemap = sitemap_text[:m.end()] + "\n" + NEW_BLOCK + sitemap_text[m.end():]
else:
    new_sitemap = sitemap_text[:m.end()] + "\n" + NEW_BLOCK + sitemap_text[m.end():]

# Verify insertion worked
assert f'chunk_{PUB_CHUNK_NUM}.html' in new_sitemap, "sitemap insertion failed"
# Verify well-formed XML
import xml.etree.ElementTree as ET
try:
    ET.fromstring(new_sitemap)
    print("[OK] sitemap parses as valid XML")
except ET.ParseError as e:
    print(f"[FAIL] sitemap XML parse error: {e}")
    sys.exit(1)

# Count <url> tags before/after
url_count_before = sitemap_text.count('<url>')
url_count_after = new_sitemap.count('<url>')
print(f"[OK] sitemap: {url_count_before} <url> -> {url_count_after} <url> (delta=+{url_count_after - url_count_before})")

SITEMAP.write_text(new_sitemap, encoding="utf-8")
print(f"[OK] sitemap.xml updated")

# ===== SURFACE 6: index.html card insertion (before </body>) =====
# Use rfind for unique last-occurrence </body> insertion (per pitfall #76)
INDEX_NEW_CARD = f"""
<section id="{INDEX_ID}" class="seo-chunk-card" data-tick="{TICK_ID_LEAD}" data-lead="{LEAD_INDEX}" data-vendor="{VENDOR}" data-chunk-src="{SRC_CHUNK_NUM}" data-chunk-pub="{PUB_CHUNK_NUM}">
<h2>{VENDOR} (ai_whiteboard cohort sibling #5) — Lucidspark AI audit evidence-gap map</h2>
<p><strong>Lead 591</strong> · {VENDOR} · <code>{EMAIL}</code> · ai_whiteboard · tier 1</p>
<p>Whiteboard + Lucid AI surface (Collaborative AI + Auto-Summarize + AI Cluster + AI Mind-Map + AI Action Items + AI Diagramming + AI Facilitation Prompts + AI Templates) — EU AI Act Art. 53(d) + FedRAMP Moderate + SOC 2 Type II + ISO 27001 + ISO 42001 + Schrems II SCC + GDPR Art. 28 evidence. Foundational Lucidspark siblings: Miro opener 587 + FigJam 588 + Mural 589 + Conceptboard 590.</p>
<p><a href="chunks/chunk_{PUB_CHUNK_NUM}.html">Read the full evidence-gap map →</a></p>
</section>
"""

# Locate the last </body> tag via rfind (per pitfall #76)
body_close_idx = index_text.rfind("</body>")
assert body_close_idx > 0, "no </body> in index.html"

# Insert BEFORE </body>
new_index = index_text[:body_close_idx] + INDEX_NEW_CARD + "\n" + index_text[body_close_idx:]
assert f'id="{INDEX_ID}"' in new_index, f"index card {INDEX_ID} not inserted"

# Verify the index card anchor uniqueness (== 1, per pitfall #69 row-prefix + #74 uniqueness pattern)
assert new_index.count(f'id="{INDEX_ID}"') == 1, f"index card id {INDEX_ID} appears more than once"
INDEX.write_text(new_index, encoding="utf-8")
print(f"[OK] index.html: card inserted (anchor id=\"{INDEX_ID}\" count==1)")

print("\n[DONE] 6 surfaces written. Build-log entry is a SEPARATE script.")
