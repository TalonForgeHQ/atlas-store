from __future__ import annotations

import csv
import json
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(r"C:\Users\Potts\projects\atlas-store")
IDX = "741"
TICK = "2026-07-20-revenue-loop-eightfold-741-seo"
CHUNK = ROOT / "chunks/chunk_741.html"
CHUNK_URL = "https://talonforgehq.github.io/atlas-store/chunks/chunk_741.html"
ROUTE = "FORM:https://eightfold.ai/request-demo/"


def already_complete() -> bool:
    try:
        with (ROOT / "revenue_log.csv").open(encoding="utf-8-sig", newline="") as fh:
            revenue_rows = list(csv.reader(fh))
        send_rows = json.loads((ROOT / "send_log.json").read_text(encoding="utf-8"))
        revenue_hits = [r for r in revenue_rows if len(r) >= 7 and r[0] == "2026-07-20" and r[1] == IDX]
        send_hits = [x for x in send_rows if isinstance(x, dict) and str(x.get("lead_index")) == IDX]
        return (
            CHUNK.is_file()
            and (ROOT / "sitemap.xml").read_text(encoding="utf-8").count(CHUNK_URL) == 1
            and (ROOT / "index.html").read_text(encoding="utf-8").count('id="chunk-741"') == 1
            and (ROOT / "build-log.html").read_text(encoding="utf-8").count(f'data-tick="{TICK}"') == 1
            and len(revenue_hits) == 1
            and len(send_hits) == 1
            and send_hits[0].get("status") == "form_route_not_submitted"
            and send_hits[0].get("smtp_eligible") is False
            and "Fetcher (planned)" not in (ROOT / "chunks/chunk_740.html").read_text(encoding="utf-8")
        )
    except (FileNotFoundError, csv.Error, json.JSONDecodeError, IndexError, TypeError):
        return False


if already_complete():
    print("SKIP 741 SEO: all completion anchors already present (idempotent no-op)")
    raise SystemExit(0)

CHUNK_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Eightfold AI Talent Intelligence Procurement Audit Checklist (2026)</title>
<meta name="description" content="Five evidence gaps for Eightfold AI talent intelligence and recruiting: candidate and requisition versions, inferred skills and ranking, employment-AI fairness review, recruiter override, hiring-outcome feedback, and retention or deletion receipts.">
<link rel="canonical" href="https://talonforgehq.github.io/atlas-store/chunks/chunk_741.html">
<meta name="robots" content="index,follow">
<style>
:root{--ink:#182129;--muted:#5b6670;--accent:#3157a4;--line:#dbe3ef;--panel:#f3f6fc}
*{box-sizing:border-box}
body{font-family:Inter,system-ui,sans-serif;max-width:900px;margin:40px auto;padding:0 22px;color:var(--ink);line-height:1.65}
h1{font-size:2rem;line-height:1.2}h2{margin-top:2rem;border-bottom:1px solid var(--line);padding-bottom:.4rem}
.lede{border-left:4px solid var(--accent);padding:12px 16px;background:var(--panel)}
.meta{color:var(--muted);font-size:.92rem}.gap{border:1px solid var(--line);border-radius:8px;padding:16px;margin:14px 0}.cta{background:var(--panel);border:1px solid var(--line);padding:18px;border-radius:8px}code{background:#edf1f7;padding:2px 5px;border-radius:4px}
</style>
</head>
<body data-tick="2026-07-20-revenue-loop-eightfold-741-seo" data-cohort="ai_hr_workflow_agents" data-lead="741">
<h1>Eightfold AI Talent Intelligence: Five Evidence Gaps Recruiting Buyers Will Test</h1>
<p class="lede"><strong>Eightfold AI</strong> publishes a full-stack, agentic Talent Intelligence Platform at <a href="https://eightfold.ai/">eightfold.ai</a>. Its first-party product pages say the platform combines enterprise data, market trends, and real-time work signals to model skills, capabilities, aspirations, and work, while the Talent Acquisition suite uses multi-modal LLMs and Eightfold agents to evaluate more candidates in less time. The procurement question is concrete: can one export reconstruct how a candidate moved from source evidence and a requisition version through inferred skills, an agent or model version, a ranking and explanation, recruiter review, and final action?</p>
<p class="meta">Atlas Lead 741 · ai_hr_workflow_agents cycle-1 sibling #2/5 after Textio 740 · Ashutosh Garg CEO &amp; Co-Founder + Varun Kacholia CTO &amp; Co-Founder · first-party route <code>FORM:https://eightfold.ai/request-demo/</code>.</p>
<h2>Why Eightfold owns the candidate-decision provenance wedge</h2>
<p>Textio 740 owns the language layer before recruiting or employee text is published. Eightfold 741 owns the next control point: candidate sourcing and rediscovery, profile and requisition versions, inferred skills and potential, match or ranking, explanation, recruiter review or override, and hiring outcome. That distinction matters because employment-AI buyers need more than a final score. They need the source span, rule or model version, constraint set, reviewer decision, and reproducible correction path behind every material recommendation.</p>
<p>This checklist does not claim that a specific control is missing. It states the evidence joins an enterprise buyer should test against Eightfold's published Talent Intelligence and Talent Acquisition surfaces.</p>
<h2>The five audit gaps</h2>
<section class="gap"><h3>Gap 1 — Candidate Source and Profile Version to Inferred Skill to Match</h3>
<p>For one candidate, can the customer export the source record, profile version, extracted or inferred skill, inference timestamp, confidence, model or agent version, target role, and resulting match or ranking?</p>
<p>The record should separate observed evidence from inferred potential, identify stale or superseded source data, and show whether a recruiter accepted, edited, or rejected the inference.</p></section>
<section class="gap"><h3>Gap 2 — Requisition and Policy Constraints to Candidate Set and Explanation</h3>
<p>Can the customer replay the job or requisition version, role and location constraints, eligibility or policy rules, candidate-set version, explanation, confidence, and exclusion reason that existed when an Eightfold agent produced a recommendation?</p>
<p>Without this join, a buyer cannot determine whether a changed requirement, stale policy, or regional rule silently altered the evaluated candidate pool.</p></section>
<section class="gap"><h3>Gap 3 — Candidate Segment and Accommodation Handling to Fairness Review</h3>
<p>Can an authorized reviewer join the applicable candidate segment, fairness test, accommodation handling, ranking outcome, reviewer identity, review timestamp, and override or disposition reason while minimizing unnecessary personal data?</p>
<p>This is the operational evidence behind employment-AI impact assessment, bias-audit, notice, appeal, and human-oversight obligations. Aggregate fairness reporting is useful, but it does not replace a protected, access-controlled per-decision review trail.</p></section>
<section class="gap"><h3>Gap 4 — Agent Recommendation to Recruiter Action to Hiring Outcome</h3>
<p>Can a customer link the recommendation and explanation to recruiter review, interview invitation, talent rediscovery, disposition, offer, or hire outcome, then record any correction signal without turning outcome feedback into an unexplained feedback loop?</p>
<p>The export should preserve the original recommendation, downstream action, reviewer intervention, outcome timestamp, feedback eligibility, and the model or policy version that later consumed the correction.</p></section>
<section class="gap"><h3>Gap 5 — Access, Retention, Deletion, and Change to Affected Rankings</h3>
<p>Can a tenant prove who accessed candidate data, which retention policy applied, when an export or deletion request completed, which derived profiles or rankings were affected, and whether downstream copies, embeddings, backups, and audit records received a completion receipt?</p>
<p>When a model, policy, or data source changes, the buyer should also be able to identify affected recommendations, rerun or invalidate them, document remediation, and preserve the legally required audit trail.</p></section>
<h2>Minimum export fields</h2>
<ul>
<li>Candidate source ID, source span, profile version, observed versus inferred skill, confidence, model or agent version, and match or ranking ID.</li>
<li>Requisition version, role/location/eligibility constraints, candidate-set version, exclusion reason, explanation, and confidence.</li>
<li>Fairness-test version, authorized segment definition, accommodation handling, reviewer identity, override or disposition reason, and review timestamp.</li>
<li>Recommendation ID, recruiter action, interview or rediscovery event, offer or hire outcome, correction signal, and downstream-use eligibility.</li>
<li>Tenant, role, region, access event, retention policy version, export or deletion request, downstream completion receipt, and affected-ranking reconstruction.</li>
</ul>
<h2>Compliance and procurement map</h2>
<p>Title VII · ADA · ADEA · EEOC Uniform Guidelines on Employee Selection Procedures · OFCCP · NYC Local Law 144 · Illinois AI Video Interview Act · Colorado AI Act · California employment-automation and privacy obligations · GDPR Arts. 5, 9, 15, 17, 22, 28, 32 and 35 · UK GDPR · EU AI Act risk management, logging, data governance, human oversight, accuracy, transparency and Annex IV documentation · CCPA/CPRA · SOC 2 · ISO 27001 · ISO/IEC 42001 · ISO/IEC 23894 · NIST AI RMF.</p>
<h2>Cohort position</h2>
<table border="1" cellpadding="6" cellspacing="0"><thead><tr><th>Slot</th><th>Vendor</th><th>Evidence primitive</th></tr></thead><tbody>
<tr><td>740 OPENER</td><td>Textio</td><td>Workplace-language suggestion, review, publication, and retention provenance.</td></tr>
<tr><td><strong>741</strong></td><td><strong>Eightfold AI</strong></td><td><strong>Candidate profile, inferred skill or potential, ranking, recruiter override, outcome, and deletion provenance.</strong></td></tr>
<tr><td>Planned #3</td><td>Interview-intelligence vendor</td><td>Interview recording, transcript, rubric, score, reviewer, and appeal evidence.</td></tr>
<tr><td>Planned #4</td><td>Employee-service agent</td><td>Employee request, policy retrieval, action, handoff, and resolution evidence.</td></tr>
<tr><td>Planned #5</td><td>Workforce-planning system</td><td>Skills graph, headcount scenario, compensation, approval, and system-of-record write-back.</td></tr>
</tbody></table>
<section class="cta"><h2>Atlas 48-Hour Evidence-Gap Map</h2>
<p>Atlas delivers a source-indexed map of the missing or unproven event IDs, version pins, source spans, explanations, reviewer decisions, exceptions, overrides, retention receipts, and remediation records for one de-identified recruiting workflow. <strong>Offer: $500 fixed in 48 hours or $497/month for quarterly refreshes.</strong></p>
<p>Long-tail keyword cluster: <em>Eightfold AI procurement audit</em>, <em>Eightfold candidate ranking evidence</em>, <em>Eightfold talent intelligence model version</em>, <em>Eightfold inferred skills audit trail</em>, <em>Eightfold recruiting agent human oversight</em>, <em>Eightfold NYC Local Law 144 evidence</em>, <em>Eightfold EU AI Act employment AI audit</em>, <em>Eightfold recruiter override provenance</em>, <em>Eightfold candidate deletion receipt</em>.</p>
</section>
<h2>First-party route and evidence</h2>
<p>The first-party Leadership page identifies <strong>Ashutosh Garg</strong> as CEO and Co-Founder and <strong>Varun Kacholia</strong> as CTO and Co-Founder. Product evidence: <a href="https://eightfold.ai/products/">Eightfold products</a> and <a href="https://eightfold.ai/products/talent-acquisition/">Talent Acquisition</a>. Commercial route: <a href="https://eightfold.ai/request-demo/">Request a live demo</a>. No suitable general-business inbox was published, so the lead uses the <code>FORM:</code> transport sentinel. SMTP must skip it. No form submission, send, or revenue is claimed.</p>
<p class="meta">Atlas @ Talon Forge · cron tick 2026-07-20-revenue-loop-eightfold-741-seo · public SEO + sitemap + index + revenue ledger + non-sendable form-route audit record · ai_hr_workflow_agents sibling #2/5.</p>
</body>
</html>
'''

INDEX_CARD = '''\n<article id="chunk-741" class="seo-chunk" data-tick="2026-07-20-revenue-loop-eightfold-741-seo" data-cohort="ai_hr_workflow_agents" data-lead="741">
<h2><a href="chunks/chunk_741.html">Eightfold AI Talent Intelligence — Candidate Profile + Inferred Skill/Potential + Agent Ranking + Recruiter Override + Hiring Outcome + Retention/Deletion Evidence Checklist</a></h2>
<p><strong>Lead 741 · ai_hr_workflow_agents sibling #2/5 after Textio 740.</strong> A five-gap procurement checklist for Eightfold AI's published Talent Intelligence and Talent Acquisition surfaces: candidate source/profile/version to inferred skill and ranking; requisition and policy constraints to candidate set and explanation; fairness/accommodation review to recruiter override; recommendation to interview, rediscovery, offer or hire outcome; and access, retention, export, deletion and model-change receipts. First-party leadership evidence identifies Ashutosh Garg as CEO &amp; Co-Founder and Varun Kacholia as CTO &amp; Co-Founder. Route-safe commercial path: <code>FORM:https://eightfold.ai/request-demo/</code>; SMTP must skip it and no form submission, send, or revenue is claimed.</p>
</article>\n'''

BUILD_ENTRY = '''<div class="tick-entry" data-tick="2026-07-20-revenue-loop-eightfold-741-seo">
<h2>2026-07-20 — revenue-loop Eightfold AI 741 SEO/distribution backfill</h2>
<p><strong>Artifact:</strong> shipped <code>chunks/chunk_741.html</code>, registered its canonical URL in <code>sitemap.xml</code>, added the <code>chunk-741</code> card to <code>index.html</code>, and recorded truthful zero-revenue and non-sendable form-route audit entries. The buyer-facing checklist covers candidate/profile versions, inferred skills and potential, ranking/explanation, fairness review, recruiter override, hiring outcomes, retention, deletion, and model-change reconstruction.</p>
<p><strong>Progress:</strong> completed the public SEO/distribution surfaces deferred by the immediately preceding Lead 741 ship. <code>ai_hr_workflow_agents</code> remains at sibling #2/5 after Textio 740; the Textio public chunk's stale planned table was synchronized so Eightfold now occupies 741 rather than a future placeholder. Offer remains $500/48h or $497/month.</p>
<p><strong>Pivot:</strong> SMTP credentials are still absent and Eightfold publishes a demo form rather than a suitable general-business inbox. The send log therefore records <code>status=form_route_not_submitted</code> and <code>smtp_eligible=false</code>; no queueing, form submission, email, delivery, payment, or revenue is claimed.</p>
<p class="footer">Atlas @ Talon Forge — cron tick 2026-07-20-revenue-loop-eightfold-741-seo · chunk + sitemap + index + revenue ledger + route audit + build-log + verification · ai_hr_workflow_agents sibling #2/5</p>
</div>
'''


def require_absent(path: Path, anchor: str) -> None:
    if path.exists():
        assert anchor not in path.read_text(encoding="utf-8"), (path, anchor)


require_absent(CHUNK, 'data-lead="741"')
for path, anchor in (
    (ROOT / "sitemap.xml", CHUNK_URL),
    (ROOT / "index.html", 'id="chunk-741"'),
    (ROOT / "build-log.html", f'data-tick="{TICK}"'),
):
    assert anchor not in path.read_text(encoding="utf-8"), (path, anchor)

with (ROOT / "revenue_log.csv").open(encoding="utf-8-sig", newline="") as fh:
    revenue_before = list(csv.reader(fh))
assert not any(r and r[0] == "2026-07-20" and len(r) > 1 and r[1] == IDX for r in revenue_before)

send_path = ROOT / "send_log.json"
send_data = json.loads(send_path.read_text(encoding="utf-8"))
assert not any(isinstance(item, dict) and str(item.get("lead_index")) == IDX for item in send_data)

CHUNK.write_text(CHUNK_HTML, encoding="utf-8", newline="\n")

sitemap_path = ROOT / "sitemap.xml"
sitemap = sitemap_path.read_text(encoding="utf-8")
close = sitemap.rfind("</urlset>")
assert close >= 0
sitemap_block = (
    "<url>\n"
    f"  <loc>{CHUNK_URL}</loc>\n"
    "  <lastmod>2026-07-20</lastmod>\n"
    "  <changefreq>monthly</changefreq>\n"
    "  <priority>0.8</priority>\n"
    "</url>\n"
)
sitemap_path.write_text(sitemap[:close] + sitemap_block + sitemap[close:], encoding="utf-8", newline="")

index_path = ROOT / "index.html"
index = index_path.read_text(encoding="utf-8")
anchor = 'id="chunk-740"'
start = index.find("<article", index.find(anchor) - 100)
assert start >= 0
end = index.find("</article>", start)
assert end >= 0
insert_at = end + len("</article>")
index = index[:insert_at] + INDEX_CARD + index[insert_at:]
index = index.replace(
    '<p><strong>Lead 740 · ai_hr_workflow_agents cycle-1 cohort OPENER sibling #1/5 (before Fetcher 741 + Eightfold 742 + Lattice 743 + Workday 744).</strong>',
    '<p><strong>Lead 740 · ai_hr_workflow_agents cycle-1 cohort OPENER sibling #1/5 (before Eightfold 741 plus planned interview-intelligence, employee-service, and workforce-planning siblings).</strong>',
    1,
)
index_path.write_text(index, encoding="utf-8", newline="")

textio_path = ROOT / "chunks/chunk_740.html"
textio = textio_path.read_text(encoding="utf-8")
textio = textio.replace(
    '<tr><td>741</td><td>Fetcher (planned)</td><td>Sourcing-agent + candidate-ranking + outbound-sequencing evidence</td></tr>\n<tr><td>742</td><td>Eightfold (planned)</td><td>Talent-intelligence + skills-graph + internal-mobility evidence</td></tr>\n<tr><td>743</td><td>Lattice (planned)</td><td>Performance + engagement + compensation-cycle evidence</td></tr>\n<tr><td>744</td><td>Workday (planned CLOSER)</td><td>HCM-system-of-record + tenant isolation + cross-product HR-OS evidence</td></tr>',
    '<tr><td><strong>741</strong></td><td><strong>Eightfold AI</strong></td><td><strong>Candidate profile + inferred skill/potential + ranking + recruiter override + hiring-outcome provenance</strong></td></tr>\n<tr><td>Planned #3</td><td>Interview-intelligence vendor</td><td>Interview recording + transcript + rubric + score + reviewer + appeal evidence</td></tr>\n<tr><td>Planned #4</td><td>Employee-service agent</td><td>Employee request + policy retrieval + action + handoff + resolution evidence</td></tr>\n<tr><td>Planned #5</td><td>Workforce-planning system</td><td>Skills graph + headcount scenario + compensation + approval + system-of-record write-back</td></tr>',
    1,
)
textio = textio.replace(
    '$2,000 fixed</strong> — five-vendor cohort map (Textio 740 + planned Fetcher 741 + planned Eightfold 742 + planned Lattice 743 + planned Workday 744).',
    '$2,000 fixed</strong> — five-vendor cohort map (Textio 740 + Eightfold AI 741 + three planned non-overlapping HR-workflow siblings).',
    1,
)
assert "Fetcher (planned)" not in textio and "Eightfold (planned)" not in textio
textio_path.write_text(textio, encoding="utf-8", newline="\n")

with (ROOT / "revenue_log.csv").open("a", encoding="utf-8", newline="") as fh:
    csv.writer(fh, lineterminator="\n").writerow([
        "2026-07-20",
        IDX,
        "741_eightfold_talent_acquisition_followup.md",
        "chunk_741.html",
        "ai_hr_workflow_agents sibling #2/5 after Textio 740 OPENER",
        "0",
        "Eightfold AI SEO/distribution backfill: candidate/profile-version to inferred-skill and agent-ranking evidence, recruiter review/override, hiring-outcome feedback, retention/deletion reconstruction; first-party leadership names Ashutosh Garg and Varun Kacholia; FORM:https://eightfold.ai/request-demo/ is non-SMTP and was not submitted; no send, payment, or revenue claimed.",
    ])

send_data.append({
    "tick": TICK,
    "lead_index": 741,
    "vendor": "Eightfold AI",
    "route": ROUTE,
    "vertical": "ai_hr_workflow_agents",
    "tier": 1,
    "template": "cold_email/templates/741_eightfold_talent_acquisition_followup.md",
    "chunk": "chunks/chunk_741.html",
    "cohort": "ai_hr_workflow_agents sibling #2/5 after Textio 740 OPENER",
    "recorded_at": "2026-07-20T20:40:00Z",
    "status": "form_route_not_submitted",
    "smtp_eligible": False,
    "queued": False,
    "sent": False,
    "revenue": 0,
    "note": "First-party Request a live demo form retained as a route-safe commercial option. It was not submitted. SMTP must skip FORM: sentinels. No email, delivery, payment, or revenue claimed.",
})
send_path.write_text(json.dumps(send_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")

build_path = ROOT / "build-log.html"
build_path.write_text(BUILD_ENTRY + build_path.read_text(encoding="utf-8"), encoding="utf-8", newline="")

ET.fromstring(sitemap_path.read_bytes())
assert sitemap_path.read_text(encoding="utf-8").count(CHUNK_URL) == 1
assert index_path.read_text(encoding="utf-8").count('id="chunk-741"') == 1
assert build_path.read_text(encoding="utf-8").count(f'data-tick="{TICK}"') == 1
with (ROOT / "revenue_log.csv").open(encoding="utf-8-sig", newline="") as fh:
    revenue_after = list(csv.reader(fh))
assert len(revenue_after) == len(revenue_before) + 1 and revenue_after[-1][1] == IDX and revenue_after[-1][5] == "0"
print("SHIP 741 SEO OK: chunk + sitemap + index + Textio cohort sync + revenue zero + non-sendable form audit + build-log")
