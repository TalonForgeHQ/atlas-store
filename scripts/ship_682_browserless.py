from __future__ import annotations

import csv
import json
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
LEADS = ROOT / "cold_email" / "leads.csv"
ENRICHED = ROOT / "cold_email" / "leads_with_emails.csv"
BUILD_LOG = ROOT / "build-log.html"
INDEX = ROOT / "index.html"
SITEMAP = ROOT / "sitemap.xml"
REVENUE = ROOT / "revenue_log.csv"
SEND_LOG = ROOT / "cold_email" / "send_log.json"

reason = (
    "Lead 682 — Browserless / browserless.io, Inc. (browserless.io managed and self-hosted browser infrastructure + "
    "BrowserQL + Browsers as a Service APIs + MCP & AI Browser Agent + persistent browser sessions + proxies + "
    "browser automation + screenshots/PDFs/testing) — browser_agents cohort sibling #4/5 after Browserbase 679, "
    "Anchor Browser 680, and Skyvern 681. Real company + real website + real founder + real verified inbox checked "
    "live 2026-07-20. Browserless's official About page identifies Joel Griffith as Founder & CEO and publishes his "
    "first-person account of starting Browserless after operating browser-backed PDF infrastructure. "
    "support@browserless.io is published on the official Contact page, Privacy Policy, Terms of Service, and docs. "
    "Differentiated wedge: browser-infrastructure provenance and Cloud-versus-Self-Hosted responsibility parity across "
    "BrowserQL, BaaS APIs, MCP, persistent sessions, proxy/region routing, authenticated state, external web mutations, "
    "and deterministic teardown. Tier-1 evidence wedge: 18-field browser-infrastructure receipt spanning session id + "
    "BrowserQL/MCP/API instruction version + browser/runtime image + tenant identity + credential scope + proxy/region + "
    "target URL + pre-action page hash + resolved target + action/input hash + CAPTCHA/security-boundary event + "
    "policy/validation result + human approval/override + replay artifact + downstream object id + post-action page hash + "
    "resulting state hash + teardown/deletion receipt. Compliance map: EU AI Act Articles 12/14/15/50 + GDPR Articles "
    "5/22/25/28/32/35 + NIST AI RMF + NIST AI 600-1/600-2 + ISO/IEC 42001 + ISO/IEC 23894 + SOC 2 + ISO 27001 + "
    "OWASP LLM Top 10 + OWASP Agentic AI Top 10 + MITRE ATLAS. Offer: $500/48h evidence-gap map or $497/mo "
    "quarterly refresh; SMTP remains blocked so send is queued. Cohort marker: browser_agents sibling #4/5."
)


def append_dict(path: Path, row: dict[str, str]) -> None:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        assert fields is not None
        rows = list(reader)
    assert "682" not in {r[fields[0]] for r in rows}, f"duplicate lead 682 in {path}"
    assert list(row) == fields, (list(row), fields)
    with path.open("a", encoding="utf-8", newline="") as f:
        csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_ALL).writerow(row)


append_dict(LEADS, {
    "index": "682", "name": "Browserless", "handle": "@browserless",
    "email": "support@browserless.io", "vertical": "browser_agents", "tier": "1",
    "template": "682_browserless.md", "tier_reason": reason,
})
append_dict(ENRICHED, {
    "lead_index": "682", "company": "Browserless", "handle": "@browserless",
    "domain": "browserless.io", "website": "https://www.browserless.io/",
    "founder": "Joel Griffith (Founder & CEO)", "vertical": "browser_agents", "tier": "1",
    "best_email": "support@browserless.io", "emails_found": "support@browserless.io",
    "guessed_emails": "", "source_template": "682_browserless.md", "tier_reason": reason,
})

entry = """<div class="tick-entry" data-tick="2026-07-20-fast-exec-browserless-682">
<h2>Tick 682 — Browserless (browser_agents cohort sibling #4/5)</h2>
<p><strong>2026-07-20 — fast-exec tick — Browserless / browserless.io, Inc.; support@browserless.io verified live on the official Contact, Privacy, Terms, and docs surfaces; Joel Griffith verified as Founder &amp; CEO on the official About page.</strong></p>
<p><strong>Artifact:</strong> appended lead 682 to both lead ledgers, wrote <code>cold_email/templates/682_browserless.md</code>, and shipped the 86-line <code>chunks/chunk_682.html</code> long-tail SEO page. Browserless advances browser_agents to 4/5 with BrowserQL, Browsers as a Service APIs, MCP &amp; AI Browser Agent, persistent browser sessions, and Self-Hosted responsibility parity.</p>
<p><strong>Evidence wedge:</strong> one 18-field browser-infrastructure receipt joining session, query/instruction, runtime image, tenant, credential scope, proxy/region, target URL, before/after page hashes, resolved target, action, security boundary, policy/human approval, replay artifact, downstream object, resulting state, and teardown/deletion proof.</p>
<p><strong>Revenue progress:</strong> $500/48h evidence-gap map + $497/mo quarterly refresh queued pending SMTP unblock. browser_agents is OPEN at 4/5; one non-overlapping secure computer-use/runtime sibling remains before closure.</p>
<p><strong>Pivot:</strong> Hyperbrowser was probed first but its guessed About and Privacy routes returned 404 and no canonical public inbox. The tick pivoted to Browserless, whose official About, Contact, Privacy, Terms, and docs surfaces exposed the founder and inbox directly.</p>
</div>
"""
text = BUILD_LOG.read_text(encoding="utf-8")
assert 'data-tick="2026-07-20-fast-exec-browserless-682"' not in text
BUILD_LOG.write_text(entry + text, encoding="utf-8")

card = """
<section id="chunk-682" class="card" data-tick="2026-07-20-fast-exec-browserless-682">
  <h2>Browserless BrowserQL AI Agent Audit Trail (2026)</h2>
  <p><strong>Long-tail keyword:</strong> Browserless BrowserQL AI agent audit trail, MCP browser session provenance, and cloud-versus-self-hosted browser automation compliance.</p>
  <p><strong>Wedge:</strong> an 18-field browser-infrastructure receipt linking query, session, runtime image, credential scope, proxy region, page-state interpretation, action, external mutation, and teardown across Browserless Cloud and Self-Hosted.</p>
  <p><a href="chunks/chunk_682.html">Read the Browserless evidence map &rarr;</a></p>
  <p class="meta">Lead 682 &middot; browser_agents cohort sibling #4/5 &middot; <a href="mailto:support@browserless.io">support@browserless.io</a></p>
</section>
"""
text = INDEX.read_text(encoding="utf-8")
assert 'id="chunk-682"' not in text
anchor = '<section id="chunk-680"'
pos = text.find(anchor)
assert pos >= 0
INDEX.write_text(text[:pos] + card + text[pos:], encoding="utf-8")

sitemap = SITEMAP.read_text(encoding="utf-8")
url = "https://talonforgehq.github.io/atlas-store/chunks/chunk_682.html"
assert url not in sitemap
block = f"""  <url>
    <loc>{url}</loc>
    <lastmod>2026-07-20</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
"""
assert sitemap.endswith("</urlset>")
SITEMAP.write_text(sitemap[:-len("</urlset>")] + block + "</urlset>", encoding="utf-8")
ET.parse(SITEMAP)

with REVENUE.open("a", encoding="utf-8", newline="") as f:
    csv.writer(f).writerow([
        "2026-07-20", "682", "682_browserless.md", "chunk_682", "browser_agents", "0",
        "Browserless sibling #4/5; Joel Griffith + support inbox verified first-party; BrowserQL/MCP/Self-Hosted 18-field receipt; $500/48h audit + $497/mo refresh queued; SMTP blocked",
    ])

queue = json.loads(SEND_LOG.read_text(encoding="utf-8"))
assert not any(str(x.get("lead_index", x.get("lead_id", ""))) == "682" for x in queue)
queue.append({
    "lead_index": 682, "name": "Browserless", "vertical": "browser_agents",
    "template": "cold_email/templates/682_browserless.md", "best_email": "support@browserless.io",
    "send_status": "queued_pending_smtp_unblock", "queued_at": "2026-07-20T04:10:00Z",
})
SEND_LOG.write_text(json.dumps(queue, indent=2) + "\n", encoding="utf-8")

print("shipped lead/template/chunk/sitemap/index/build-log/revenue/send-log for 682")
