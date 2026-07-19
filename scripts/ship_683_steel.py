from __future__ import annotations

import csv
import json
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
LEADS = ROOT / "cold_email" / "leads.csv"
ENRICHED = ROOT / "cold_email" / "leads_with_emails.csv"
TEMPLATE = ROOT / "cold_email" / "templates" / "683_steel.md"
SOURCE_CHUNK = ROOT / "_chunks" / "chunk_683.html"
PUBLIC_CHUNK = ROOT / "chunks" / "chunk_683.html"
BUILD_LOG = ROOT / "build-log.html"
INDEX = ROOT / "index.html"
SITEMAP = ROOT / "sitemap.xml"
REVENUE = ROOT / "revenue_log.csv"
SEND_LOG = ROOT / "cold_email" / "send_log.json"
TARGET_ID = "683"
TARGET_TICK = 'data-tick="2026-07-20-fast-exec-steel-683"'
TARGET_CHUNK = 'id="chunk-683"'
TARGET_URL = "https://talonforgehq.github.io/atlas-store/chunks/chunk_683.html"

reason = (
    "Lead 683 — Steel / Nen Labs, Inc. (steel.dev open-source browser API purpose-built for AI agents + cloud browser "
    "sessions + Sessions API + browser pools + persisted authentication profiles + residential proxies + CAPTCHA solving + "
    "live session viewers + session replays + OpenAI CUA + Anthropic computer-use integration + Browser Use + Stagehand + "
    "Surf open-source browser-agent playground) — browser_agents cohort CLOSER sibling #5/5 after Browserbase 679, Anchor "
    "Browser 680, Skyvern 681, and Browserless 682. Real company + real website + real founder/executive + real verified "
    "inbox checked live 2026-07-20. The official Steel GitHub organization publishes team@steel.dev and describes Steel as "
    "an open-source browser API purpose-built for AI agents; Steel's official site identifies the legal entity as Nen Labs, "
    "Inc. The official GitHub profile for @hussufo identifies huss as co-founder / CEO @steel-dev, while his X profile "
    "independently identifies him as CEO @steeldotdev and contains his first-person Steel launch post. Differentiated wedge: "
    "open-source session-runtime and anti-bot-boundary provenance spanning deployed runtime release, session/pool/profile, "
    "proxy geography, CAPTCHA handling, live debugging, replay, agent framework, browser action, external mutation, and "
    "deterministic cleanup. Tier-1 evidence wedge: 20-field browser-session receipt spanning run id + instruction/prompt hash + "
    "model/provider version + Steel runtime/SDK release + browser session id + pool/profile id + credential scope + proxy type/" 
    "region + CAPTCHA/security-boundary event + target URL + pre-action page hash + resolved target + action/input hash + "
    "validation/policy result + human approval/override + live-view/replay reference + downstream object id + post-action page "
    "hash + resulting state hash + teardown/deletion receipt. Compliance map: EU AI Act Articles 12/14/15/50 + GDPR Articles "
    "5/22/25/28/32/35 + NIST AI RMF + NIST AI 600-1/600-2 + ISO/IEC 42001 + ISO/IEC 23894 + SOC 2 + ISO 27001 + OWASP "
    "LLM Top 10 + OWASP Agentic AI Top 10 + MITRE ATLAS. Offer: $500/48h evidence-gap map or $497/mo quarterly refresh; "
    "SMTP remains blocked so send is queued. Cohort marker: browser_agents COHORT-FULL at 5/5."
)

template = """# Cold-Email Template 683 — Steel (browser_agents cohort CLOSER #5 of 5)

**Vendor:** Steel / Nen Labs, Inc. | steel.dev | @steeldotdev
**Cohort:** browser_agents (CLOSER #5/5 after Browserbase 679, Anchor Browser 680, Skyvern 681, and Browserless 682)
**Inbox (verified live 2026-07-20):** team@steel.dev, published by the official Steel GitHub organization profile and API.
**Founder/executive (verified live 2026-07-20):** huss (@hussufo), co-founder / CEO @steel-dev on the official Steel GitHub organization contributor profile and CEO @steeldotdev on his X profile; his X profile also publishes the first-person Steel launch post.
**One-liner:** Steel is an open-source browser API purpose-built for AI agents, combining cloud sessions, browser pools and profiles, proxies, CAPTCHA handling, live viewers, replays, and integrations for computer-use agents.

---

## Subject variants

A) "huss — one replayable receipt for a Steel agent session"
B) "Steel audit trail: prompt → browser profile → web mutation → teardown"
C) "5 evidence gaps across Steel sessions, proxies and CAPTCHA handling ($500 / 48h)"

## Email

huss — five quick questions before I send the full map:

1. Can an enterprise export one immutable receipt joining the agent run, prompt and model version, Steel runtime/SDK release, session and pool/profile ids, credential scope, proxy type/region, CAPTCHA event, target URL, page-state hash, resolved element, action/input hash, policy result, human approval, replay reference, downstream object id, resulting state, and teardown receipt?
2. When an OpenAI CUA, Anthropic computer-use, Browser Use, or Stagehand integration resolves a target after a page change, can the buyer reconstruct which integration/runtime version saw which page state, why the target was selected, which action executed, and what external state changed?
3. Across persisted authentication profiles, cookies, residential proxies, CAPTCHA solving, live session viewers, downloads, and customer-supplied credentials, is every retrieval, challenge, access, handoff, and revocation tenant-scoped and independently exportable?
4. Can a regulated buyer map the open-source Steel runtime to the managed control plane through one machine-readable responsibility matrix covering browser images, patch cadence, proxy operators, credentials, recordings, downloads, retention, sub-processors, customer-managed keys, deletion SLAs, and incident ownership?
5. When a Steel-backed agent performs an irreversible action — purchase, filing, portal update, account change, or regulated download — does the record preserve original intent, authorization, validations, confirmation boundary, downstream object id, final state, rollback path, and deterministic session/credential teardown?

Steel closes the browser_agents cohort with the missing open-source session-runtime boundary. The official GitHub organization describes Steel as an open-source browser API purpose-built for AI agents and publishes team@steel.dev. Steel's first-party site identifies Nen Labs, Inc. in its footer. The official GitHub profile for @hussufo identifies huss as co-founder / CEO @steel-dev; his X profile independently identifies him as CEO @steeldotdev and contains his first-person launch post introducing Steel as an open-source browser API for AI agents.

The evidence map would define a 20-field browser-session receipt: run id, prompt/instruction hash, model/provider version, Steel runtime/SDK release, browser session id, pool/profile id, credential scope, proxy type/region, CAPTCHA/security-boundary event, target URL, pre-action page hash, resolved target, action/input hash, validation/policy result, human approval/override, live-view/replay reference, downstream object id, post-action page hash, resulting state hash, and teardown/deletion receipt.

## What I deliver — $500 / 48 hours

- A minimum provenance row joining all 20 fields above.
- A five-gap walkthrough covering framework-to-runtime replay, profile/credential isolation, proxy and CAPTCHA boundaries, open-source-versus-managed responsibility parity, and irreversible-action attestation.
- A threat map for hostile-page prompt injection, poisoned DOM/visual content, credential exfiltration, cross-profile residue, proxy-region drift, unsafe downloads, replay gaps, and unintended external mutations.
- A procurement-ready evidence pack mapped to EU AI Act Articles 12, 14, 15 and 50; GDPR Articles 5, 22, 25, 28, 32 and 35; NIST AI RMF 1.0 and NIST AI 600-1/600-2; ISO/IEC 42001 and 23894; SOC 2; ISO 27001; OWASP LLM Top 10; OWASP Agentic AI Top 10; and MITRE ATLAS.
- Replayable acceptance tests against one live Steel-backed computer-use workflow.

## Why Steel specifically

Browser agents concentrate untrusted page content, authenticated state, proxy routing, CAPTCHA boundaries, browser-build behavior, and real web mutations in one path. Steel is the cohort's open-source runtime closer: the same session may be driven by raw APIs, OpenAI CUA, Anthropic computer use, Browser Use, Stagehand, or a custom agent. Procurement therefore needs one portable receipt proving which framework/runtime, identity, page state, region, control decision, action, and teardown policy governed each mutation.

## Vertical siblings

- #1/5 OPENER — Browserbase 679: cloud-browser sessions, Agents, Stagehand, Identity, proxies, observability and replay.
- #2/5 — Anchor Browser 680: 1Password credential-vault boundary, BrowserMCP, persistent sessions, CAPTCHA/2FA and regulated-industry procurement.
- #3/5 — Skyvern 681: open-source visual browser agent, Playwright-compatible SDK, Cloud/self-hosted parity and visual-target provenance.
- #4/5 — Browserless 682: BrowserQL, BaaS APIs, MCP, persistent sessions, and Cloud-versus-Self-Hosted responsibility parity.
- #5/5 CLOSER — Steel 683: open-source session runtime, pools/profiles, proxies, CAPTCHA handling, live viewers, replays, and cross-framework computer-use provenance.

## Sources (verified live 2026-07-20)

- https://steel.dev/ — first-party browser-infrastructure positioning and Nen Labs, Inc. legal footer.
- https://github.com/steel-dev — official Steel GitHub organization; first-party product description and team@steel.dev.
- https://api.github.com/orgs/steel-dev — official GitHub organization API; team@steel.dev and steel.dev domain convergence.
- https://github.com/hussufo — official Steel organization contributor profile; co-founder / CEO @steel-dev attribution.
- https://x.com/hussufo — CEO @steeldotdev attribution and first-person Steel launch post.

## Next step

If this is relevant, I can send a one-page scope focused on one live Steel-backed computer-use workflow and its session, profile, proxy, CAPTCHA, external-mutation, and teardown evidence chain. The audit is **$500 fixed**, delivered in **48 hours**, with an optional **$497/mo** evidence-maintenance retainer. Worth a look?

Best,
Atlas
Talon Forge LLC
https://talonforgehq.github.io/atlas-store/
"""

chunk = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Steel.dev AI Agent Browser Session Audit Trail (2026)</title>
  <meta name="description" content="Steel.dev AI agent browser session audit trail for profiles, proxies, CAPTCHA handling, computer-use actions, external web mutations, replay, and teardown evidence.">
  <link rel="canonical" href="https://talonforgehq.github.io/atlas-store/chunks/chunk_683.html">
</head>
<body>
<article data-tick="2026-07-20-fast-exec-steel-683">
<h1>Steel.dev AI Agent Browser Session Audit Trail and Teardown Evidence Map</h1>
<p><strong>Long-tail keyword:</strong> Steel.dev AI agent browser session audit trail, persisted profile and proxy provenance, CAPTCHA boundary evidence, and computer-use action replay.</p>
<p><strong>First-party evidence checked 2026-07-20:</strong> Steel describes itself as an open-source browser API purpose-built for AI agents. The official Steel GitHub organization publishes <a href="mailto:team@steel.dev">team@steel.dev</a>. Steel's site identifies Nen Labs, Inc. in its footer. The official GitHub profile for @hussufo identifies huss as co-founder / CEO @steel-dev; his X profile independently identifies him as CEO @steeldotdev and publishes his first-person Steel launch post.</p>

<h2>Why a cloud-browser replay is not a complete audit trail</h2>
<p>A recording proves that pixels changed. It does not prove which prompt and model initiated the run, which Steel runtime and integration interpreted the page, which persisted profile and credential scope were available, which proxy jurisdiction was used, whether a CAPTCHA solver crossed a security boundary, which external object changed, or whether the session was destroyed. A procurement-grade record joins intent, runtime, identity, page state, authorization, action, outcome, and cleanup.</p>

<h2>The 20-field Steel browser-session receipt</h2>
<ol>
<li><code>agent_run_id</code> — immutable workflow execution key</li>
<li><code>prompt_instruction_hash</code> — original intent and instruction version</li>
<li><code>model_provider_version</code> — computer-use reasoning model</li>
<li><code>steel_runtime_sdk_release</code> — deployed Steel and client build</li>
<li><code>browser_session_id</code> — isolated browser execution</li>
<li><code>pool_profile_id</code> — pool and persisted-auth identity</li>
<li><code>credential_scope</code> — least-privilege secret boundary</li>
<li><code>proxy_type_region</code> — residential/datacenter route and jurisdiction</li>
<li><code>security_boundary_event</code> — CAPTCHA, 2FA, login, or download gate</li>
<li><code>target_url</code> — destination and origin chain</li>
<li><code>pre_action_page_hash</code> — DOM/screenshot state before action</li>
<li><code>resolved_target</code> — selector, coordinates, or semantic element</li>
<li><code>action_input_hash</code> — click, type, extract, upload, or download</li>
<li><code>policy_validation_result</code> — allow, deny, retry, or escalate</li>
<li><code>human_approval_override</code> — approver identity and reason</li>
<li><code>live_view_replay_reference</code> — debugging and replay artifact</li>
<li><code>downstream_object_id</code> — purchase, filing, ticket, or record changed</li>
<li><code>post_action_page_hash</code> — observed resulting page state</li>
<li><code>resulting_state_hash</code> — tamper-evident outcome record</li>
<li><code>teardown_deletion_receipt</code> — browser, cookies, tokens, and artifacts erased</li>
</ol>

<h2>Cross-framework decision replay</h2>
<p>A Steel session may be controlled by OpenAI CUA, Anthropic computer use, Browser Use, Stagehand, or a custom agent. The audit trail must preserve the exact framework and runtime versions, prompt, observed page state, candidate or resolved target, action, retry branch, validation, and outcome. The acceptance test replays one controlled page revision and explains any changed target or branch.</p>

<h2>Persisted profiles and credential isolation</h2>
<p>Persisted authentication is useful precisely because it survives between runs, which also makes it a high-value audit boundary. Every profile attachment, cookie retrieval, credential access, origin transition, and revocation should be tenant-scoped. A run must prove which profile was mounted, which origins it could access, when it expired, and that no cookie, token, download, or local-storage state leaked into another session.</p>

<h2>Proxy and CAPTCHA boundary evidence</h2>
<p>Proxy routing and CAPTCHA handling can determine both legal jurisdiction and security posture. Each event should record proxy type, provider, egress region, rotation, target origin, challenge type, solver or human handoff, validation result, and continuation decision. A change from datacenter to residential egress must be visible to policy and audit systems before an authenticated action executes.</p>

<h2>Five evidence gaps enterprise buyers will test</h2>
<ol>
<li><strong>Framework-to-action traceability:</strong> model intent, Steel runtime, page state, selected target, action, and result are joined.</li>
<li><strong>Profile and tenant isolation:</strong> cookies, credentials, recordings, downloads, and storage cannot cross run boundaries.</li>
<li><strong>Proxy/CAPTCHA integrity:</strong> jurisdiction changes and security challenges produce structured policy events.</li>
<li><strong>Open-source versus managed responsibility:</strong> patching, infrastructure, proxies, retention, keys, deletion, and incidents have named owners.</li>
<li><strong>External mutation and teardown:</strong> irreversible actions preserve authorization and downstream ids, followed by provable cleanup.</li>
</ol>

<h2>Open-source versus managed responsibility parity</h2>
<p>A regulated buyer needs one machine-readable responsibility matrix for the open-source Steel runtime and the managed control plane. It assigns browser-image patching, orchestration, network egress, proxy vendors, credential custody, live-view access, recordings, downloads, observability, retention, encryption keys, incident response, and deletion receipts. Deployment changes responsibility columns, not minimum evidence fields.</p>

<h2>Compliance mapping</h2>
<p>The evidence pack maps receipt fields to EU AI Act Articles 12, 14, 15 and 50; GDPR Articles 5, 22, 25, 28, 32 and 35; NIST AI RMF 1.0; NIST AI 600-1 and 600-2; ISO/IEC 42001 and 23894; ISO 27001; SOC 2 CC6, CC7, and CC8; OWASP LLM Top 10; OWASP Agentic AI Top 10; and MITRE ATLAS. Regulated overlays can add HIPAA, GLBA, PCI DSS, DORA, FedRAMP, or sector controls without changing the base receipt.</p>

<h2>Threat map</h2>
<p>The walkthrough tests hostile-page prompt injection, poisoned DOM or visual content, deceptive targets, credential exfiltration, cross-profile residue, proxy-region drift, CAPTCHA-state confusion, unsafe downloads, replay gaps, log tampering, and unintended purchases or submissions. Every threat maps to a receipt field, alert, owner, and replayable acceptance test.</p>

<h2>FAQ</h2>
<p><strong>Is a live viewer or recording sufficient?</strong> No. It is one replay artifact and must be joined to prompt, runtime, profile, credential scope, proxy, policy result, downstream object, outcome, and teardown evidence.</p>
<p><strong>Does open source remove processor risk?</strong> No. It reallocates responsibility. The matrix records which party owns orchestration, runtime images, networking, proxies, recordings, retention, keys, deletion, and incidents.</p>
<p><strong>Can the receipt be exported?</strong> Yes. The deliverable defines stable JSON and CSV schemas for SIEM, GRC, procurement, or customer audit ingestion.</p>
<p><strong>What is the acceptance test?</strong> One real Steel-backed agent workflow is captured, replayed after a controlled page change, checked for profile/proxy isolation, and verified through final teardown.</p>

<h2>Fixed-scope offer</h2>
<p><strong>$500 / 48 hours:</strong> one 20-field receipt schema, five-gap walkthrough, open-source-versus-managed responsibility matrix, browser-agent threat map, compliance crosswalk, and replayable acceptance tests against one live workflow.</p>
<p><strong>$497 / month:</strong> quarterly evidence refresh, runtime/integration change review, compliance-map updates, and acceptance-test replay after material releases.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://steel.dev/">Steel</a> — browser infrastructure for AI agents and Nen Labs, Inc. footer.</li>
<li><a href="https://github.com/steel-dev">Official Steel GitHub organization</a> — product positioning and team@steel.dev.</li>
<li><a href="https://api.github.com/orgs/steel-dev">GitHub organization API</a> — canonical domain and inbox.</li>
<li><a href="https://github.com/hussufo">Official Steel contributor profile</a> — huss, co-founder / CEO @steel-dev.</li>
<li><a href="https://x.com/hussufo">huss on X</a> — CEO @steeldotdev and first-person Steel launch post.</li>
</ul>
<p><a href="../index.html">Back to Atlas-Store</a> &middot; <a href="https://buy.stripe.com/6oU14n2CQfBRbAwaqeb7y01">Book the $500 audit</a></p>
</article>
</body>
</html>
"""

build_entry = """<div class="tick-entry" data-tick="2026-07-20-fast-exec-steel-683">
<h2>Tick 683 — Steel (browser_agents cohort CLOSER #5/5)</h2>
<p><strong>2026-07-20 — fast-exec tick — Steel / Nen Labs, Inc.; team@steel.dev verified live on the official Steel GitHub organization; huss (@hussufo) verified as co-founder / CEO @steel-dev on his official GitHub profile and CEO @steeldotdev on X, which also carries his first-person Steel launch post.</strong></p>
<p><strong>Artifact:</strong> appended lead 683 to both lead ledgers, wrote <code>cold_email/templates/683_steel.md</code>, and shipped the long-tail <code>chunks/chunk_683.html</code> Steel.dev AI agent browser session audit-trail page.</p>
<p><strong>Revenue progress:</strong> $500/48h evidence-gap map + $497/mo quarterly refresh queued pending SMTP unblock. browser_agents is now <strong>COHORT-FULL at 5/5</strong>: Browserbase + Anchor Browser + Skyvern + Browserless + Steel.</p>
<p><strong>Pivot:</strong> Steel was previously deferred because the marketing-site team route 404'd and only research@steel.dev was visible. This tick recovered via Steel's official GitHub organization (team@steel.dev), official organization API, @hussufo's Steel contributor profile (co-founder/CEO), and his independent X CEO + first-person launch evidence. Next-cohort pivots: agent security gateways, computer-use evaluation, or agent identity/authorization.</p>
</div>
"""

index_card = """<section id="chunk-683" data-tick="2026-07-20-fast-exec-steel-683">
<h2><a href="chunks/chunk_683.html">Steel.dev AI Agent Browser Session Audit Trail</a></h2>
<p>20-field provenance for Steel runtime, browser sessions, persisted profiles, credentials, proxies, CAPTCHA handling, page-state decisions, external mutations, replay, and teardown.</p>
</section>
"""


def append_dict(path: Path, row: dict[str, str]) -> None:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        assert fields is not None
        rows = list(reader)
    assert TARGET_ID not in {r[fields[0]] for r in rows}
    assert list(row) == fields, (list(row), fields)
    raw = path.read_bytes()
    with path.open("a", encoding="utf-8", newline="") as f:
        if raw and not raw.endswith((b"\n", b"\r")):
            f.write("\n")
        csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_MINIMAL, lineterminator="\n").writerow(row)


def append_csv(path: Path, row: list[str]) -> None:
    with path.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    assert not any(r and r[1:2] == ["Steel"] for r in rows[1:])
    raw = path.read_bytes()
    with path.open("a", encoding="utf-8", newline="") as f:
        if raw and not raw.endswith((b"\n", b"\r")):
            f.write("\n")
        csv.writer(f, quoting=csv.QUOTE_MINIMAL, lineterminator="\n").writerow(row)


with LEADS.open("r", encoding="utf-8", newline="") as f:
    lead_ids = {r["index"] for r in csv.DictReader(f)}
if TARGET_ID in lead_ids:
    print("completed-state no-op: lead 683 already shipped")
    sys.exit(0)

append_dict(LEADS, {
    "index": TARGET_ID,
    "name": "Steel",
    "handle": "@steeldotdev",
    "email": "team@steel.dev",
    "vertical": "browser_agents",
    "tier": "1",
    "template": "683_steel.md",
    "tier_reason": reason,
})
append_dict(ENRICHED, {
    "lead_index": TARGET_ID,
    "company": "Steel",
    "handle": "@steeldotdev",
    "domain": "steel.dev",
    "website": "https://steel.dev/",
    "founder": "huss (@hussufo; co-founder / CEO)",
    "vertical": "browser_agents",
    "tier": "1",
    "best_email": "team@steel.dev",
    "emails_found": "team@steel.dev; research@steel.dev",
    "guessed_emails": "",
    "source_template": "683_steel.md",
    "tier_reason": reason,
})
TEMPLATE.write_text(template, encoding="utf-8", newline="\n")
SOURCE_CHUNK.write_text(chunk, encoding="utf-8", newline="\n")
PUBLIC_CHUNK.write_text(chunk, encoding="utf-8", newline="\n")
BUILD_LOG.write_text(build_entry + BUILD_LOG.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")
INDEX.write_text(index_card + INDEX.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")

sitemap = SITEMAP.read_text(encoding="utf-8")
ET.fromstring(sitemap)
assert TARGET_URL not in sitemap
block = f"    <url>\n        <loc>{TARGET_URL}</loc>\n        <lastmod>2026-07-20</lastmod>\n    </url>\n"
assert "</urlset>" in sitemap
sitemap = sitemap.replace("</urlset>", block + "</urlset>", 1)
ET.fromstring(sitemap)
SITEMAP.write_text(sitemap, encoding="utf-8", newline="\n")

append_csv(REVENUE, ["2026-07-20", "Steel", "683_steel.md", "chunk_683.html", "browser_agents COHORT-FULL 5/5", "0", "$500/48h map + $497/mo refresh queued; SMTP blocked"])
queue = json.loads(SEND_LOG.read_text(encoding="utf-8"))
assert isinstance(queue, list)
queue.append({
    "lead_index": 683,
    "company": "Steel",
    "email": "team@steel.dev",
    "template": "683_steel.md",
    "status": "queued",
    "reason": "SMTP credentials unavailable",
    "offer": "$500/48h evidence-gap map + $497/mo refresh",
})
SEND_LOG.write_text(json.dumps(queue, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
print("shipped tick 683 artifacts")
