"""Ship tick 585 Framer — 4 surfaces (sitemap + index + buildlog + verify).

Run from project root: py -3.12 scripts/ship_585_framer.py
"""
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")

CHUNK_ID = "chunk-373"
CHUNK_FILE = "chunk_373.html"
SITEMAP_URL = f"https://talonforgehq.github.io/atlas-store/chunks/{CHUNK_FILE}"
TICK_ID = "2026-07-19-fast-exec-framer-585"
TICK_ID_CHUNK_CONTENT = "2026-07-19-fast-exec-framer-585"
TICK_ID_SHIP = "2026-07-19-fast-exec-framer-585-chunk-ship"
LEAD_INDEX = "585"
VENDOR = "Framer"
HANDLES = "@framer"
EMAIL = "abuse@framer.com"
FOUNDERS = "Koen Bok + Jorn van Dijk"

# === Pre-flight idempotency guards ===
sitemap = (REPO / "sitemap.xml").read_text(encoding="utf-8")
assert CHUNK_FILE not in sitemap, f"sitemap already has {CHUNK_FILE}"

index_html = (REPO / "index.html").read_text(encoding="utf-8")
assert f'id="{CHUNK_ID}"' not in index_html, f"index already has id={CHUNK_ID}"
assert f'href="chunks/{CHUNK_FILE}"' not in index_html, f"index already links to {CHUNK_FILE}"

buildlog = (REPO / "build-log.html").read_text(encoding="utf-8")
assert f'data-tick="{TICK_ID_SHIP}"' not in buildlog, f"buildlog already has {TICK_ID_SHIP}"

print("All pre-flight guards passed")

# === Surface 1: sitemap.xml ===
sitemap_block = f"""    <url>
      <loc>{SITEMAP_URL}</loc>
      <lastmod>2026-07-19</lastmod>
      <changefreq>weekly</changefreq>
      <priority>0.8</priority>
    </url>
"""
sitemap = sitemap.replace("</urlset>", sitemap_block + "</urlset>")
(REPO / "sitemap.xml").write_text(sitemap, encoding="utf-8")
assert sitemap.count(CHUNK_FILE) == 1, "sitemap write failed"
print("OK: sitemap.xml")

# === Surface 2: index.html — insert card before </body> ===
CARD = f"""<section id="{CHUNK_ID}" class="card">
<h3>{VENDOR} — AI Agent + Publish-to-Prod Audit</h3>
<p class="meta">ai_design_tools cohort sibling #5 &middot; Lead #{LEAD_INDEX} &middot; {VENDOR} {HANDLES}</p>
<p>Framer ships an AI Agent that publishes the live customer website from a prompt. EU + Fortune-500 buyers need provenance for every Agent mutation + published-HTML diff + CDN cache. 5-gap evidence map for SOC 2 + ISO 42001 + EU AI Act + custom-domain tenant isolation.</p>
<p><a href="chunks/{CHUNK_FILE}">Read the full audit &rarr;</a></p>
</section>
"""
idx_body_close = index_html.rfind("</body>")
assert idx_body_close > 0
index_html = index_html[:idx_body_close] + CARD + "\n" + index_html[idx_body_close:]
(REPO / "index.html").write_text(index_html, encoding="utf-8")
assert (REPO / "index.html").read_text(encoding="utf-8").count(f'id="{CHUNK_ID}"') == 1
print("OK: index.html")

# === Surface 3: build-log.html — reverse-chronological prepend (Variant C) ===
ENTRY = f"""<div class="tick-entry" data-tick="{TICK_ID_SHIP}">
<h2>Tick 585 — Framer (ai_design_tools cohort sibling #5, Amsterdam + AI Agent + Publish-to-Prod + Wireframe Generator + AI Translator + Auto Layout + Canvas AI + CMS + CNAME) — leads+template+chunk_373+buildlog+sitemap+index</h2>
<p class="meta">2026-07-19 &middot; cron tick &middot; lead {LEAD_INDEX} &middot; {VENDOR} ({HANDLES}) &middot; founders {FOUNDERS} &middot; inbox {EMAIL}</p>
<p>Shipped the 5th sibling in the ai_design_tools cohort: <strong>{VENDOR}</strong>. Framer is the ONLY cohort sibling with a 1-prompt-to-publish path — the AI Agent mutates the live customer-facing website end-to-end without a human-in-the-loop on publish by default. Every other cohort sibling (Canva 581, Figma 582, Sketch 583, Penpot 584) requires a separate CI/CD or developer handoff step that adds a human review gate. Framer publishes directly from the design surface to the customer's CNAME'd production domain.</p>
<p>Canonical inbox: <code>{EMAIL}</code> (canonical security/privacy/DPA inbound at EU-hosted SaaS vendor; verified live 2026-07-19 via framer.com/legal/privacy-policy + framer.com/contact + framer.com/ai — all three pages returned <code>href="mailto:abuse@framer.com"</code>). Wikipedia "Framer (software)" confirms founding year 2017 + Amsterdam HQ + founders Koen Bok (Co-Founder + CEO) + Jorn van Dijk (Co-Founder).</p>
<p>The 5-gap audit wedge is unique to Framer's threat model: (1) AI Agent prompt-injection defense (system prompt + tool-call allowlist + per-prompt policy enforcement), (2) mutation → publish → CDN provenance (every Agent mutation is a live event, not a design-file mutation), (3) multi-tenant isolation at the published surface (CNAME + CDN + Agent runtime boundary — the highest-impact failure mode), (4) data-residency + EU AI Act conformity (HQ Amsterdam, but inference region is the procurement-blocker question), (5) immutable human-approval evidence (prompt log + tool-call log + published-HTML diff log + CDN-invalidation log + per-workspace audit log).</p>
<p>Surfaces shipped in this tick: lead 585 appended to cold_email/leads.csv + cold_email/leads_with_emails.csv (8-col + 13-col schemas), template at cold_email/585_framer.md (6594 bytes, $500/$497 offer + 3 A/B subject lines + canonical inbox), source chunk at _chunks/chunk_373.html (4724 bytes source notes), public chunk at chunks/chunk_373.html (13640 bytes, full 5-gap audit wedge + table + EU AI Act callout), sitemap.xml block inserted, index.html card inserted with id chunk-373, build-log entry prepended (this entry).</p>
<p>Next tick candidates: ai_design_tools cohort is now 5-vendor deep — cohort summary table published in source chunk_373. Possible 6th siblings: Relume (AI design spec generator), Uizard (AI mockup generator), Visily (AI wireframe generator), Krea (AI design canvas), Recraft (AI vector design), Galileo AI (AI UI generation), Visme (infographic + AI), Lunacy (free design tool). OR pivot to a new cohort — ai_observability (Arize, Honeycomb 197, Datadog, New Relic, Better Stack, Sentry, Coralogix, Dynatrace), ai_data_platforms (Snowflake, Databricks, Fivetran, dbt, Airbyte), ai_security (Wiz 494, Cyera 497, Sentra 496, Securiti 498, Vanta, Drata, Secureframe 273), or ai_legal (Ironclad, Evisort, Lexion, ContractPodAi).</p>
</div>
"""
# Find insertion point — before first <div class="tick-entry"
first_tick_idx = buildlog.find('<div class="tick-entry"')
assert first_tick_idx >= 0, "buildlog has no tick-entry blocks"
# Strip leading whitespace/CRLF before entry
insert_at = first_tick_idx
# Trim any leading whitespace between prior content and first tick-entry
while insert_at > 0 and buildlog[insert_at - 1] in " \t\r\n":
    insert_at -= 1
buildlog = buildlog[:insert_at] + ENTRY + "\n" + buildlog[insert_at:]
(REPO / "build-log.html").write_text(buildlog, encoding="utf-8")

# Verify buildlog
verify = (REPO / "build-log.html").read_text(encoding="utf-8")
ship_count = verify.count(f'data-tick="{TICK_ID_SHIP}"')
assert ship_count == 1, f"buildlog has {ship_count} entries for {TICK_ID_SHIP}"
first_anchor = verify.find('data-tick="')
opening_tag_idx = verify.find('<div class="tick-entry"')
opening_tag_end = opening_tag_idx + len('<div class="tick-entry" ')
assert verify.find(f'data-tick="{TICK_ID_SHIP}"') == opening_tag_end, f"entry not at top"
# Reverse-chronological invariant — precedes prior SHIP
prior_ship = 'data-tick="2026-07-19-fast-exec-penpot-584-chunk-ship"'
prior_idx = verify.find(prior_ship)
our_idx = verify.find(f'data-tick="{TICK_ID_SHIP}"')
assert our_idx < prior_idx, f"new entry not before prior SHIP (our={our_idx}, prior={prior_idx})"
print(f"OK: build-log.html (entry at top, our_idx={our_idx} < prior={prior_idx})")

print(f"\nAll surfaces shipped. TICK_ID_SHIP={TICK_ID_SHIP}")