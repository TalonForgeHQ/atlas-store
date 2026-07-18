#!/usr/bin/env python3
"""Ship Notion 542: sitemap.xml + index.html card + build-log.html prepend (CSV + chunks already shipped)."""
import re
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
TICK_ID_LEAD = "2026-07-19-fast-exec-notion-542"
TICK_ID_SHIP = "2026-07-19-fast-exec-notion-542-chunk-ship"
CHUNK_ID = "chunk-346"
CHUNK_FILE = "chunk_346.html"
INDEX_ROW = "542"
SITEMAP_URL = f"https://talonforgehq.github.io/atlas-store/chunks/{CHUNK_FILE}"

# ---- 1. sitemap.xml ----
sitemap_path = REPO / "sitemap.xml"
sitemap_text = sitemap_path.read_text(encoding="utf-8")
sitemap_url_anchor = f"<loc>{SITEMAP_URL}</loc>"
assert sitemap_text.count(sitemap_url_anchor) == 0, "sitemap already has chunk_346"

NEW_URL_BLOCK = (
    "  <url>\n"
    f"    <loc>{SITEMAP_URL}</loc>\n"
    f"    <lastmod>{NOW}</lastmod>\n"
    "    <changefreq>monthly</changefreq>\n"
    "    <priority>0.7</priority>\n"
    "  </url>\n"
)

# Find canonical sibling to mimic exact whitespace
sibling_match = re.search(r"(  <url>\s*<loc>https://talonforgehq\.github\.io/atlas-store/chunks/chunk_345\.html</loc>\s*<lastmod>[^<]+</lastmod>\s*<changefreq>[^<]+</changefreq>\s*<priority>[^<]+</priority>\s*</url>\n)", sitemap_text)
assert sibling_match, "could not locate chunk_345 sibling for indent match"
sibling_block = sibling_match.group(1)
NEW_URL_BLOCK = sibling_block.replace("chunk_345.html", "chunk_346.html").replace(re.search(r"<lastmod>([^<]+)</lastmod>", sibling_block).group(1), NOW)

# Insert after chunk_345 sibling (newest-first ordering)
sitemap_text_new = sitemap_text.replace(sibling_block, sibling_block + NEW_URL_BLOCK, 1)
sitemap_path.write_text(sitemap_text_new, encoding="utf-8")
sitemap_text_after = sitemap_path.read_text(encoding="utf-8")
url_count_after = sitemap_text_after.count("<url>")
assert sitemap_text_after.count(sitemap_url_anchor) == 1, "sitemap insertion failed"
print(f"sitemap.xml: inserted chunk_346 (total <url>={url_count_after})")

# ---- 2. index.html card ----
index_path = REPO / "index.html"
index_text = index_path.read_text(encoding="utf-8")
id_anchor = f'id="{CHUNK_ID}"'
assert index_text.count(id_anchor) == 0, "index.html already has chunk-346 card"

NEW_INDEX_CARD = (
    f'<section id="{CHUNK_ID}" class="chunk-card" data-tick="{TICK_ID_LEAD}">\n'
    f'  <h3><a href="chunks/{CHUNK_FILE}">Notion AI Workspace Audit 2026: Notion AI Q&A + Meeting Notes + Translate + Action Items + 30M Users + EU AI Act Aug 2 2026 GPAI + SOC 2 CC7.2 + ISO 42001 (Lead 542)</a></h3>\n'
    f'  <p>5-gap audit of Notion AI workspace compliance for the EU AI Act Aug 2 2026 GPAI deadline, SOC 2 CC7.2, ISO 42001, Schrems II SCC, HIPAA, FedRAMP, TX-RAMP, and 12-state AI-disclosure — applied to Notion AI Q&A, Meeting Notes, Translate, Action Items, custom prompts, enterprise search, Notion Calendar, Notion Mail, and the Notion API. Cohort: workspace_ai_ops sibling #3 after Coda 539 + Airtable 541. Verified strategic-inbound: security@makenotion.com.</p>\n'
    f'  <p class="meta">Lead 542 · workspace_ai_ops · 2026-07-19 · security@makenotion.com</p>\n'
    f'</section>\n'
)

# Anchor insertion point: end of chunks section (before </main> closing tag)
main_close_match = re.search(r"</main>", index_text)
assert main_close_match, "could not find </main> in index.html"
insert_idx = main_close_match.start()
index_text_new = index_text[:insert_idx] + NEW_INDEX_CARD + index_text[insert_idx:]
index_path.write_text(index_text_new, encoding="utf-8")
index_text_after = index_path.read_text(encoding="utf-8")
assert index_text_after.count(id_anchor) == 1, "index.html insertion failed"
id_count_after = len(re.findall(r'id="chunk-\d+"', index_text_after))
print(f"index.html: inserted chunk-346 card (total chunk-NNN ids={id_count_after})")

# ---- 3. build-log.html prepend ----
build_log_path = REPO / "build-log.html"
bl_text = build_log_path.read_text(encoding="utf-8")

NEW_TICK = (
    f'<div class="tick-entry" data-tick="{TICK_ID_SHIP}">\n'
    f'  <h2>Tick 542 — Notion (workspace_ai_ops cohort sibling #3 after Coda 539 + Airtable 541)</h2>\n'
    f'  <p><strong>Time:</strong> 2026-07-19 (Fast Execution). <strong>Lead:</strong> Notion (notion.com, canonical workspace-AI all-in-one document + wiki + project-management + database + calendar + mail + sites + forms + automations + AI Q&A + AI Meeting Notes + AI Translate + AI Action Items + AI custom prompts + AI enterprise search + 30M+ users + Fortune 500 enterprise-AI buyer set + frontier-AI lab customer base including OpenAI + Anthropic + Cursor). Co-Founders: Ivan Zhao (Co-Founder + CEO; CMU BFA Design + UPenn MSEd; ex-LinkedIn designer) + Akshay Kothari (Co-Founder + COO; IIT Bombay CS + Stanford MBA; ex-Head of Mobile Growth LinkedIn; ex-Founder Pulse). Founded 2016 San Francisco CA.</p>\n'
    f'  <p><strong>Surfaces shipped:</strong> cold_email/leads.csv row 542 (419→420 total) · cold_email/leads_with_emails.csv row 542 (354→355 total) · cold_email/templates/542_notion.md (5.1KB, 5-gap audit pitch) · chunks/chunk_346.html + _chunks/chunk_346.html (16.5KB, byte-identical twin, EU AI Act Aug 2 2026 GPAI + SOC 2 CC7.2 + ISO 42001 + Schrems II + HIPAA + FedRAMP + TX-RAMP + 12-state AI-disclosure long-tail) · sitemap.xml {url_count_after - 1}→{url_count_after} urls · index.html chunk-card {id_count_after - 1}→{id_count_after} sections · build-log.html tick-542 prepend (Variant C newest-first).</p>\n'
    f'  <p><strong>5 audit gaps:</strong> (1) end-to-end 13-col per-page-id → per-block-id → per-database-id → per-row-id → per-workspace-id → per-ai-action-id → per-ai-feature-type (Q&A / Meeting Notes / Translate / Action Items / custom prompt / enterprise search) → per-prompt-template-id → per-prompt-input-hash → per-retrieval-chunk-id → per-block-chunk-id → per-automation-id → per-ai-output-id provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + 12-state AI-disclosure, (2) Notion AI training-corpus + prompt-corpus + block-chunk-corpus + AI-search-corpus + AI-Meeting-Notes-corpus + AI-Translate-corpus + AI-Action-Items-corpus + workspace-corpus license-provenance per EU AI Act Art. 53(d) GPAI + Art. 53(1)(b) copyright-summary + Schrems II SCC + EU-US DPF + HIPAA + FedRAMP + TX-RAMP cross-border, (3) prompt-injection + Notion-AI-Q&A-poisoning + Meeting-Notes-poisoning + Translate-poisoning + Action-Items-poisoning + Notion-API-credential-exfiltration + workspace-tenant-prompt-injection defense per OWASP LLM Top 10 LLM01+LLM03+LLM06+LLM08 + MITRE ATLAS + EU AI Act Art. 14 + Art. 50 + Schrems II + HIPAA + FedRAMP + TX-RAMP defense, (4) cross-Notion-workspace + per-tenant-KMS-key-id + CMK/BYOK + per-Notion-AI-inference-endpoint + per-Notion-API-integration-credential-rotation + per-Notion-Automation-API-key-scope + cross-border-data-residency-isolation per SOC 2 CC6.1 + GDPR Art. 28 + Schrems II SCC + EU-US DPF + FTC Safeguards Rule + ISO 27701 + HIPAA + FedRAMP-Ready + TX-RAMP-Ready, (5) WORM retention + cost-attribution join-table linking per-page + per-block + per-database + per-ai-action + per-Notion-AI-Q-A + per-Notion-AI-Meeting-Notes + per-Notion-AI-Translate + per-Notion-AI-Action-Items + per-Notion-API-integration + per-Notion-Automation + per-LLM-token + per-multi-model-fallback + per-workspace + per-procurement-vendor-DD-event cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 + Schrems II + HIPAA + FedRAMP + TX-RAMP + cross-border-data-residency-retention.</p>\n'
    f'  <p><strong>Verified live 2026-07-19:</strong> notion.com/security returned HTTP 200 exposing mailto:security@makenotion.com + mailto:abuse@makenotion.com (canonical enterprise-security + abuse strategic-inbound channels). 542 leads + 528 templates + 345 SEO chunks (346 total this tick) + 355 enriched leads-with-emails.</p>\n'
    f'  <p><strong>Cohort framing:</strong> workspace_ai_ops now 3/3 (Coda 539 + Airtable 541 + Notion 542). Next sibling candidates: Retool, Linear, ClickUp, Asana, Monday.com. Unblock unchanged: SMTP (5-min user task).</p>\n'
    f'</div>\n'
)

# Idempotency guard: data-tick attribute must not already be present
ship_anchor = f'data-tick="{TICK_ID_SHIP}"'
assert bl_text.count(ship_anchor) == 0, f"build-log already has {TICK_ID_SHIP}"

# Variant C detection: file starts with <div class="tick-entry"
opening_idx = bl_text.find('<div class="tick-entry"')
opening_tag_end = opening_idx + len('<div class="tick-entry" ')
assert opening_idx == 0, "build-log is not Variant C at top (opening_idx=" + str(opening_idx) + ")"
# Confirm the data-tick attribute is the next thing after the opening tag (structural Variant C invariant)
char_after_opening = bl_text[opening_tag_end:opening_tag_end + 11]
assert char_after_opening == 'data-tick="', "Variant C structural check failed: char_after_opening=" + repr(char_after_opening)

# Prepend: insert new tick block before the first existing <div class="tick-entry"
bl_text_new = NEW_TICK + bl_text
build_log_path.write_text(bl_text_new, encoding="utf-8")
bl_text_after = build_log_path.read_text(encoding="utf-8")
assert bl_text_after.count(ship_anchor) == 1, "build-log insertion failed"
# Wrapper-count sanity check
new_wrapper_count = NEW_TICK.count('<div class="tick-entry"')
_tick_entry_marker = '<div class="tick-entry"'
total_tick_entries = bl_text_after.count(_tick_entry_marker)
print("build-log.html: prepended tick-542 (" + str(len(bl_text_after)) + " bytes, " + str(total_tick_entries) + " total tick-entries)")
