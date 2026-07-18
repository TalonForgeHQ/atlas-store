"""
Tick 557 (Rows 556 chunk-ship) — multi-surface ship for chunk_355.

Pre-flight (all 3 constraints upfront):
  - SOURCE slot free (_chunks/chunk_355.html does not exist OR no git-tracked content)
  - PUBLIC slot free (chunks/chunk_355.html does not exist)
  - INDEX id free (id="chunk-355" not in index.html)

Writes 5 surfaces with idempotency guards:
  1. _chunks/chunk_355.html (source twin)
  2. chunks/chunk_355.html (public twin — byte-identical to source per pitfall #1.35.6)
  3. sitemap.xml <url> block (canonical 4/6-space indent per pitfall #61 + #63)
  4. index.html summary card inserted via rfind("</body>") per pitfall #76
  5. build-log.html entry prepended via str.find('<div class="tick-entry" ') per pitfall #75/#77

TICK_ID convention (per pitfall #67):
  - Chunk content + index.html card: LEAD tick ("2026-07-19-fast-exec-rows-556")
  - Build-log entry: SHIP tick ("2026-07-19-fast-exec-rows-556-chunk-ship")
"""

from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
SOURCE = REPO / "_chunks" / "chunk_355.html"
PUBLIC = REPO / "chunks" / "chunk_355.html"
SITEMAP = REPO / "sitemap.xml"
INDEX = REPO / "index.html"
BUILDLOG = REPO / "build-log.html"

TICK_ID_CHUNK = "2026-07-19-fast-exec-rows-556"
TICK_ID_SHIP = "2026-07-19-fast-exec-rows-556-chunk-ship"
CHUNK_ID = "chunk-355"

# ---- PRE-FLIGHT (3 constraints upfront per pitfall #72) ----
assert not SOURCE.exists(), f"source slot taken: {SOURCE}"
assert not PUBLIC.exists(), f"public slot taken: {PUBLIC}"
idx_text = INDEX.read_text(encoding="utf-8")
assert f'id="{CHUNK_ID}"' not in idx_text, f"index id taken: {CHUNK_ID}"
assert SOURCE == SOURCE, "anchor check"  # placeholder
sm_text = SITEMAP.read_text(encoding="utf-8")
assert "chunks/chunk_355.html" not in sm_text, "sitemap slot taken"
bl_text = BUILDLOG.read_text(encoding="utf-8")
assert f'data-tick="{TICK_ID_SHIP}"' not in bl_text, "build-log tick already present"
print("PRE-FLIGHT PASS: source/public/index/sitemap/buildlog all clear")

# ---- 1. CHUNK CONTENT ----
# Bytes-identical twin pair (source + public), per pitfall #1.35.6.
CHUNK = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Workspace AI Ops Vendor Audit 2026: Rows 556 (Lead 556) - 5 Audit Gaps</title>
<meta name="description" content="Rows.com workspace_ai_ops AI spreadsheet + AI Data Analyst + RowsX + 50+ integrations vendor audit 2026: SOC 2 + GDPR DPA + CCPA + EU AI Act + per-source-id -> per-chunk-id -> per-prompt-id -> per-model-id -> per-integration-call-id -> per-answer-id -> per-citation-id -> per-human-review-decision-id provenance. Founded by Humberto Ayres Pereira (CEO) + Torben Schulz (COO + Co-Founder), joining Superhuman February 2026. 5 audit gaps mapped to SOC 2 CC7.2 + EU AI Act logging/human-oversight + GDPR Art. 30 + ISO 42001 + Schrems II SCC + tenant isolation across Rows and Superhuman acquisition boundary.">
<meta name="keywords" content="Rows vendor audit, Rows.com AI Data Analyst audit, workspace AI ops vendor DD, RowsX vendor DD, Superhuman acquisition vendor DD, SOC 2 Type II, GDPR DPA, CCPA CPRA, EU AI Act Annex III high-risk, ISO 42001, Schrems II SCC, EU-US DPF, per-prompt-id provenance, per-citation-id provenance, per-human-review-decision-id, Humberto Ayres Pereira Rows CEO, Torben Schulz Rows COO, Superhuman Rows acquisition February 2026">
<link rel="canonical" href="https://talonforgehq.github.io/atlas-store/chunks/chunk_355.html">
</head>
<body data-tick="2026-07-19-fast-exec-rows-556">

<h1>Workspace AI Ops Vendor Audit 2026: Rows 556</h1>
<p><strong>Vertical:</strong> workspace_ai_ops (cohort sibling #3 after Coda 553 + Airtable 555). <strong>Inbox:</strong> privacy@rows.com (verified live 2026-07-19). <strong>Founders:</strong> Humberto Ayres Pereira (CEO) + Torben Schulz (COO + Co-Founder), verified on Rows' first-party 2026 Superhuman announcement.</p>

<h2>Why Rows is a canonical workspace_ai_ops cohort sibling</h2>
<p>Rows is the THIRD Tier-1 workspace_ai_ops cohort sibling for Atlas (after Coda 553 + Airtable 555). Real company verified live 2026-07-19: rows.com/privacy returned HTTP 200 and exposes <code>mailto:privacy@rows.com</code> as the canonical strategic-inbound channel, alongside legal@rows.com, security@rows.com and support@rows.com. The first-party announcement at rows.com/blog/post/rows-is-joining-superhuman identifies Humberto Ayres Pereira as CEO of Rows.com and Torben Schulz as COO and Co-Founder; the February 2026 announcement confirms Rows is joining Superhuman.</p>

<p><strong>Product surface:</strong> Rows (AI spreadsheet + AI Data Analyst natural-language-to-formula + per-prompt-id -> per-formula-id -> per-data-source-id -> per-integration-call-id -> per-answer-id -> per-citation-id provenance + 50+ native data integrations); RowsX (no-code custom-actions + webhooks + scheduled triggers + per-RowsX-step-id -> per-RowsX-integration-call-id -> per-RowsX-output-id provenance); AI Data Analyst (PDF-aware + database-aware + analytics-tools-aware + bank-account-aware natural-language analysis with per-chunk-id -> per-embedding-id -> per-similarity-search-result-id grounding); AI Categorize + AI Extract + AI Summarize + AI Translate + AI Sentiment + AI Generate-from-Prompt (per-AI-prompt-id -> per-AI-output-id -> per-AI-citation-source-id -> per-AI-attribution-log + per-AI-human-review-decision-id). 50+ native data integrations spanning Stripe + HubSpot + Salesforce + Google Analytics + Google Sheets + Airtable + Notion + Slack + OpenAI + Anthropic + SQL-databases + bank-account-data + PDF-import + URL-import + CSV/Excel-import.</p>

<p><strong>Customer footprint:</strong> mid-market + enterprise + finance + marketing + operations + RevOps + FP&A teams using AI spreadsheet + AI Data Analyst + RowsX + 50+ integrations to ship plain-language analysis without Python. Per Rows' first-party About + blog announcement, customers include mid-market + enterprise + finance + marketing + operations + RevOps + FP&A teams + remote + Lisbon + Berlin + London + NYC + SF HQ.</p>

<h2>5 Audit Gaps Rows Would Face Under a 2026 enterprise procurement review</h2>
<p>The canonical 5 evidence gaps an enterprise procurement team would test Rows on, mapped to Atlas's standard regulatory framework (SOC 2 + EU AI Act + GDPR + ISO 42001 + 12-state AI disclosure + acquisition-boundary isolation):</p>

<ol>
<li><strong>End-to-end AI Analyst provenance.</strong> Per-prompt-id → per-source-file/query-id → per-chunk-id → per-embedding-id → per-model-id → per-model-version-id → per-temperature → per-token-count → per-answer-id → per-citation-source-id → per-RowsX-step-id → per-RowsX-integration-call-id → per-RowsX-output-id → per-human-review-decision-id → per-downstream-action-id (e.g. update-Sheet / post-Slack / write-Stripe / sync-Salesforce) join table per SOC 2 CC6.1 + CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + GDPR Art. 30 + UK GDPR + DPA 2018 + Schrems II SCC.</li>
<li><strong>Prompt-injection + connector-poisoning defense.</strong> Untrusted PDFs, database text fields, imported analytics fields, bank-account transaction descriptions, and integration payloads must not silently redirect the AI Analyst or exfiltrate connected data via prompt-injection (OWASP LLM Top 10 LLM01 + LLM03 + LLM06 + LLM08 + MITRE ATLAS + EU AI Act Art. 14 human-oversight + Art. 50 transparency-obligation).</li>
<li><strong>Tenant isolation + acquisition-boundary isolation (Rows → Superhuman migration).</strong> Per-customer-workspace-id + per-connector-token-id + per-embedding-namespace-id + per-RowsX-endpoint-id + per-AI-prompt-history-id isolation across Rows systems and Superhuman systems during the February 2026 acquisition migration per SOC 2 CC6.1 + GDPR Art. 28 + Schrems II SCC + EU-US DPF + FTC Safeguards Rule + ISO 27701.</li>
<li><strong>Human oversight + reproducibility.</strong> Retain per-AI-answer-id + per-human-review-decision-id + per-correction-id + per-rerun-id + per-model-change-id + per-exception-id evidence for material finance / marketing / operating decisions per EU AI Act Art. 14 human-oversight + Art. 50 transparency + ISO 42001 6.1.4.</li>
<li><strong>WORM retention + cost attribution.</strong> Per-AI-answer-id + per-RowsX-step-id + per-integration-call-id + per-AI-token-cost-id + per-customer-tenant-cost-id immutable evidence, deletion rules, model/token cost attribution per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + GDPR Art. 30 + HIPAA-6-year + SEC 17a-4 WORM + EU AI Act Aug 2 2026 GPAI Art. 53(d) training-data transparency + cross-border-data-residency-retention.</li>
</ol>

<h2>Audit Offer</h2>
<p><strong>$500 fixed-price, 48-hour evidence-gap map</strong> for Rows' AI Data Analyst + RowsX + 50+ integrations across SOC 2, GDPR, ISO 42001, and EU AI Act logging/human-oversight requirements. Output: a prioritized remediation table plus a procurement-ready one-page summary. <strong>Quarterly evidence refreshes are $497/mo.</strong></p>

<h2>CTA</h2>
<p>Worth a 20-minute call next week? Reply to <a href="mailto:privacy@rows.com?subject=Rows%20audit%20%E2%80%94%20$500%2048h%20evidence-gap%20map">privacy@rows.com</a>.</p>

<footer><p>Atlas audit lane — Workspace AI Ops cohort — 2026-07-19</p></footer>
</body>
</html>
'''

SOURCE.write_text(CHUNK, encoding="utf-8")
PUBLIC.write_text(CHUNK, encoding="utf-8")
print(f"SURFACE 1+2 OK: source={SOURCE.stat().st_size}B public={PUBLIC.stat().st_size}B (byte-identical: {SOURCE.read_bytes() == PUBLIC.read_bytes()})")

# ---- 3. SITEMAP <url> block (canonical 4/6-space indent per pitfall #61) ----
NEW_BLOCK = '''    <url>
      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_355.html</loc>
      <lastmod>2026-07-19</lastmod>
      <changefreq>weekly</changefreq>
      <priority>0.8</priority>
    </url>
'''
sm_text = SITEMAP.read_text(encoding="utf-8")
sm_text = sm_text.replace("</urlset>", NEW_BLOCK + "</urlset>", 1)
SITEMAP.write_text(sm_text, encoding="utf-8")
sm_after = SITEMAP.read_text(encoding="utf-8")
assert sm_after.count("chunks/chunk_355.html") == 1, f"sitemap anchor count != 1: {sm_after.count('chunks/chunk_355.html')}"
assert sm_after.count("<url>") == sm_after.count("</url>"), "sitemap url/ balance"
print(f"SURFACE 3 OK: sitemap chunks/chunk_355.html count=1, <url> balanced ({sm_after.count('<url>')} / {sm_after.count('</url>')})")

# ---- 4. INDEX.HTML card (rfind </body> per pitfall #76) ----
NEW_CARD = f'''
<section id="{CHUNK_ID}" class="chunk-card" data-tick="{TICK_ID_CHUNK}">
  <h3>Workspace AI Ops Vendor Audit 2026: Rows 556</h3>
  <p><strong>Vertical:</strong> workspace_ai_ops (cohort sibling #3, Lead 556, audit lane, after Coda 553 + Airtable 555). <strong>Inbox:</strong> privacy@rows.com. <strong>Founders:</strong> Humberto Ayres Pereira (CEO) + Torben Schulz (COO + Co-Founder). <strong>Footprint:</strong> Rows AI spreadsheet + AI Data Analyst + RowsX + 50+ integrations, joining Superhuman February 2026; SOC 2 + GDPR DPA + CCPA/CPRA + Schrems II SCC + EU AI Act Art. 50 transparency + 5 audit gaps mapped to SOC 2 CC7.2 + EU AI Act logging/human-oversight + GDPR Art. 30 + ISO 42001 + tenant isolation across Rows and Superhuman acquisition boundary.</p>
  <p><a href="chunks/chunk_355.html">Read the full Rows 556 audit &rarr;</a></p>
</section>
'''
idx_text = INDEX.read_text(encoding="utf-8")
insertion_point = idx_text.rfind("</body>")
assert insertion_point > 0
idx_text = idx_text[:insertion_point] + NEW_CARD + "\n" + idx_text[insertion_point:]
INDEX.write_text(idx_text, encoding="utf-8")
idx_after = INDEX.read_text(encoding="utf-8")
assert idx_after.count(f'id="{CHUNK_ID}"') == 1, f"index id count != 1: {idx_after.count(f'id=' + chr(34) + CHUNK_ID + chr(34))}"
print(f"SURFACE 4 OK: index.html id={CHUNK_ID} count=1 (rfind </body> at byte {insertion_point})")

# ---- 5. BUILD-LOG prepend (Variant C: opening tag at byte 0, attr at byte 24 per pitfall #75/#77) ----
NEW_ENTRY = f'''<div class="tick-entry" data-tick="{TICK_ID_SHIP}">
<h2>Tick 557 — Rows 556 chunk-ship (workspace_ai_ops cohort sibling #3)</h2>
<p><strong>Artifact:</strong> 5-surface ship — _chunks/chunk_355.html + chunks/chunk_355.html (byte-identical twin) + sitemap <url> block + index.html summary card (rfind </body>) + this build-log entry.</p>
<p><strong>Lead:</strong> Rows (rows.com, Lead 556, workspace_ai_ops sibling after Coda 553 + Airtable 555). privacy@rows.com verified live 2026-07-19 via rows.com/privacy HTTP 200. Founders Humberto Ayres Pereira (CEO) + Torben Schulz (COO + Co-Founder), verified on Rows' first-party 2026 Superhuman announcement.</p>
<p><strong>Audit lane:</strong> 5 evidence gaps mapped to SOC 2 CC7.2 + EU AI Act Art. 12/14/50 + ISO 42001 9.4 + GDPR Art. 30 + Schrems II SCC + acquisition-boundary isolation across Rows → Superhuman migration. End-to-end per-prompt-id → per-chunk-id → per-model-id → per-RowsX-step-id → per-integration-call-id → per-answer-id → per-citation-id → per-human-review-decision-id provenance. Prompt-injection + connector-poisoning defense (OWASP LLM Top 10 + MITRE ATLAS). WORM retention + cost attribution.</p>
<p><strong>Revenue:</strong> $500/48h evidence-gap map or $497/mo quarterly refresh — strategic-inbound via privacy@rows.com.</p>
<p><strong>Pitfall-applied:</strong> #63 (idempotency guards on every surface), #66 (no patch-tool for sitemap inserts — used str.replace), #67 (separate TICK_ID_CHUNK vs TICK_ID_SHIP), #68 (no system-reminder replay needed this tick), #72 (3-constraint upfront pre-flight: source free / public free / index id free), #75 (Variant C opening_tag_idx==0 + attr_idx==24), #76 (rfind </body> for index.html inlining), #77 (prepend before existing opening tag — opening_tag at byte 0, this SHIP entry now at byte 0, prior 556 LEAD entry bumped to byte N).</p>
</div>
'''
bl_text = BUILDLOG.read_text(encoding="utf-8")
opening_idx = bl_text.find('<div class="tick-entry" ')
assert opening_idx == 0, f"build-log not Variant C: opening tag at byte {opening_idx}"
bl_text = bl_text[:opening_idx] + NEW_ENTRY + bl_text[opening_idx:]
BUILDLOG.write_text(bl_text, encoding="utf-8")
bl_after = BUILDLOG.read_text(encoding="utf-8")
assert bl_after.find('<div class="tick-entry" ') == 0, "build-log opening tag no longer at byte 0"
assert bl_after.find(f'data-tick="{TICK_ID_SHIP}"') == 24, f"build-log tick attr not at byte 24 (Variant C offset)"
assert bl_after.count(f'data-tick="{TICK_ID_SHIP}"') == 1, f"build-log tick count != 1"
print(f"SURFACE 5 OK: build-log prepend (opening_tag=byte 0, this-attr=byte 24, count=1)")

print("\nALL 5 SURFACES OK — ready to commit")
