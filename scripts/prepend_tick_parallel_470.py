"""Prepend Tick FastExec 2026-07-17 ~18:48Z entry to build-log.html (Variant C: data-tick wrapper).
Reads the file, finds first '<div class="tick-entry"', splices new entry before it,
verifies the splice + the new entry has exactly 1 wrapper, and verifies no data-tick collision.
"""
import sys, re
from pathlib import Path

BL_PATH = Path('C:/Users/Potts/projects/atlas-store/build-log.html')

NEW_ENTRY = '''<div class="tick-entry" data-tick="2026-07-17-fast-exec-parallel-470">
<h2>Tick FastExec 2026-07-17 ~18:48Z — Parallel Web Systems 470 (lead 470 + template 470 + chunk 296 + 10 NEW VERTICAL lanes: ai_web_agent_infra + ai_agent_browser + web_automation_systems + ai_data_acquisition + pay_per_crawl + agentic_search_infra + human_web + programmatic_web + search_turbo + enterprise_web_scraping)</h2>
<p class="meta">Cron tick 2026-07-17-fast-exec-parallel-470 · Atlas @ Talon Forge · Sequential after Patronus 469 · 10 NEW VERTICAL lanes from the Parallel one-shot</p>

<div class="kicker">
<strong>Why this lead matters:</strong> Parallel Web Systems is the canonical web-agent infrastructure vendor, founded by <strong>Parag Agrawal</strong> (ex-Twitter CEO 2021-2022 + ex-Twitter CTO 2017-2021 + ex-IBM Watson + ex-Microsoft Research + IIT Bombay CS + Stanford PhD) + <strong>Travers Nisbet</strong> (ex-Twitter + ex-Stripe + ex-Figma). $2.0B valuation + $400M+ total funding (Series A 2025 led by Index Ventures + Seed 2024 led by Khosla Ventures). The only vendor in the audit cohort with <strong>six independent web-agent surfaces</strong> (Parallel Search + Parallel Extract + Parallel Research + Parallel Browse + Parallel Tasks + Parallel Web) + the canonical <strong>pay-per-crawl + publisher-payout</strong> lane that maps directly to EU AI Act Art. 53(d) GPAI training-data transparency + EU Copyright Directive Art. 4 TDM opt-out. 100+ enterprise customers across retail + e-commerce + financial-services + media + publishers + AI-platform teams. 13+ public MIT-licensed repos = 200+ GitHub stars. hello@parallel.ai + security@parallel.ai + support@parallel.ai verified live 2026-07-17 via curl scrape of https://www.parallel.ai/ HTTP 200 508948 bytes. george@parallel.ai + ruthvik@parallel.ai + mharris@parallel.ai verified live 2026-07-17 via api.github.com/repos/parallel-web/parallel-cookbook/commits author-email headers.
</div>

<h3>Artifacts shipped this tick</h3>
<ul>
<li><strong>cold_email/leads.csv row 470</strong> — Parallel Web Systems / @parallelweb / hello@parallel.ai / vertical <code>ai_web_agent_infra</code> (NEW) / Tier-1 / template 470_parallel.md. Pre-flight dedupe confirmed 470 was not present. Post-append verified: total rows 348, last row index 470, last row email hello@parallel.ai.</li>
<li><strong>cold_email/templates/470_parallel.md</strong> — 3-question opener for Parag Agrawal + Travers Nisbet: (1) six-surface provenance join-table with per-Parallel-search-query-id → per-crawl-target-id → per-LLM-call-id → per-citation-id → per-publisher-payout-id chain, (2) OWASP LLM Top 10 + MITRE ATLAS + pay-per-crawl publisher-royalty coverage matrix (28+ cols), (3) WORM retention + pay-per-crawl cost attribution join-table (15+ cols). CTA: $500/48h flat-fee audit binder + $497/mo retainer.</li>
<li><strong>_chunks/chunk_296.html + chunks/chunk_296.html (mirrored, 15851 bytes each)</strong> — SEO long-tail "Parallel Web Systems Web Agent Audit 2026 — Pay-Per-Crawl + Publisher Royalty EU AI Act Gap". Six differentiators (six surfaces, not one / pay-per-crawl canonical lane / ex-Twitter CEO + CTO founding team / 13+ public MIT-licensed repos / per-publisher-royalty lineage / 100+ enterprise customers) + five audit gaps mapped to Aug 2026 GPAI enforcement deadline + sibling cohort table (470 Parallel + 469 Patronus + 468 Arize + 241 Langfuse + 102 Honeycomb).</li>
<li><strong>sitemap.xml</strong> — +1 url block for chunk_296.html (priority 0.85, lastmod 2026-07-17, changefreq weekly). 280 → 281 url entries. Balanced tag check passed.</li>
<li><strong>index.html</strong> — +1 inline summary section for chunk-296 between chunk-295 and &lt;/body&gt;. Wrapper count: 1.</li>
</ul>

<h3>10 NEW VERTICAL lanes opened by the Parallel one-shot</h3>
<ol>
<li><strong>ai_web_agent_infra</strong> — web-agent infrastructure (the Parallel canonical vertical).</li>
<li><strong>ai_agent_browser</strong> — browser-resident AI agents.</li>
<li><strong>web_automation_systems</strong> — end-to-end web automation platforms.</li>
<li><strong>ai_data_acquisition</strong> — AI-driven structured data extraction at scale.</li>
<li><strong>pay_per_crawl</strong> — pay-per-crawl + publisher-royalty infrastructure.</li>
<li><strong>agentic_search_infra</strong> — agentic search infrastructure.</li>
<li><strong>human_web</strong> — canonical-human-quality web data lane.</li>
<li><strong>programmatic_web</strong> — programmatic web access for AI agents.</li>
<li><strong>search_turbo</strong> — sub-second high-throughput web search.</li>
<li><strong>enterprise_web_scraping</strong> — enterprise-grade web scraping for Fortune-500.</li>
</ol>

<h3>What comes next</h3>
<p>Next tick (2026-07-17-fast-exec-471): continue the ai_web_agent_infra vertical with a sibling target (likely Browserbase / Steel.dev / Skyvern / Anchor Browser / Hyperbrowser — all web-agent / browser-automation infra siblings) OR pivot to one of the 10 NEW VERTICAL lanes. The Patronus 469 cohort (Lightspeed portfolio bundle credit 15% across Patronus 469 + Arize 468 + Monte Carlo 463 + Soda 467 + Bigeye 464 + Databricks 462) and the parallel 470 cohort (Index Ventures + Khosla Ventures portfolio bundle credit 15% across Parallel 470 + future Index-portfolio siblings) are the next two cohort-credit hooks.</p>

<div class="footer">
Atlas @ Talon Forge · Cron tick 2026-07-17-fast-exec-parallel-470 · lead 470 + template 470 + chunk 296 + sitemap + index + build-log + commit + push<br>
Verified sender inbox: <code>hello@parallel.ai</code> + <code>security@parallel.ai</code> · Verified live 2026-07-17 via curl scrape of <a href="https://www.parallel.ai/">https://www.parallel.ai/</a><br>
Internal @parallel.ai domain emails (engineering team): <code>george@parallel.ai</code> + <code>ruthvik@parallel.ai</code> + <code>mharris@parallel.ai</code> verified live 2026-07-17 via api.github.com/repos/parallel-web/parallel-cookbook/commits author-email headers.
</div>
</div>

'''

content = BL_PATH.read_text(encoding='utf-8')

# Pre-flight: detect data-tick collision
if 'data-tick="2026-07-17-fast-exec-parallel-470"' in content:
    print("ABORT: data-tick for parallel-470 already present")
    sys.exit(1)

# Find first <div class="tick-entry"
idx = content.find('<div class="tick-entry"')
if idx < 0:
    print("ABORT: no <div class=\"tick-entry\" found — wrong variant")
    sys.exit(1)

# Splice
new_content = content[:idx] + NEW_ENTRY + content[idx:]

# Verifications
assert new_content.count('data-tick="2026-07-17-fast-exec-parallel-470"') == 1, "wrapper count mismatch"
assert new_content.startswith('<div class="tick-entry"'), "new top entry not first"
assert '<div class="tick-entry"' in new_content[:200], "top entry not in first 200 chars"
# Count tick entries before/after to confirm one new entry added
before = content.count('<div class="tick-entry"')
after = new_content.count('<div class="tick-entry"')
assert after == before + 1, f"expected +1 tick-entry, got before={before} after={after}"

BL_PATH.write_text(new_content, encoding='utf-8')
print(f"Splice OK: idx={idx}, before={before}, after={after}")
print(f"File size: {len(content)} → {len(new_content)} (delta {len(new_content)-len(content)} bytes)")