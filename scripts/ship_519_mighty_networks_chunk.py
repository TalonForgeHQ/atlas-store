"""
ship_519_mighty_networks_chunk.py — 5-surface chunk ship for Mighty Networks 519 (ai_creator_economy cohort sibling #8).

Trigger: podia-520 tick's build-log explicitly noted "ship Mighty Networks 519 chunk... as a 5-surface chunk-ship in the next tick."

Surfaces touched:
1. _chunks/chunk_334.html (source) — already written
2. chunks/chunk_335.html (public) — already written
3. sitemap.xml <url> block — write via str.replace on the chunk_334 block (canonical sibling)
4. index.html card — write before </body>
5. build-log.html — prepend a Variant C tick entry

Idempotency guards per pitfall #63:
  - Each surface asserts its unique anchor is NOT already present before the write.
  - If present, raises SystemExit(1) — operator must git checkout HEAD -- <surface> first.

Slot discovery (pre-flight per pitfall #72):
  - Source: _chunks/chunk_334.html — git ls-files returns empty (verified, fresh slot)
  - Public: chunks/chunk_335.html — does not exist on disk (next free in chunks/)
  - Index id: id="chunk-334" — not present in index.html (verified)
"""

from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------------------
# Pre-flight: enumerate slot collisions BEFORE any write (pitfall #72)
# ---------------------------------------------------------------------------
SOURCE = ROOT / "_chunks" / "chunk_334.html"
PUBLIC = ROOT / "chunks" / "chunk_335.html"
INDEX_ID = "chunk-334"  # matches SOURCE NNN (not PUBLIC NNN — pitfall 1.35.3)

assert SOURCE.exists(), f"PRE-FLIGHT FAIL: {SOURCE} not found (run write_file for source first)"
assert PUBLIC.exists(), f"PRE-FLIGHT FAIL: {PUBLIC} not found (run write_file for public first)"

src_text = SOURCE.read_text(encoding="utf-8")
public_text = PUBLIC.read_text(encoding="utf-8")
assert f'data-chunk="334"' in src_text, "PRE-FLIGHT FAIL: source missing data-chunk=\"334\""
assert f'data-tick="2026-07-18-fast-exec-podia-520"' in src_text, "PRE-FLIGHT FAIL: source data-tick wrong"
assert 'Mighty Networks' in public_text, "PRE-FLIGHT FAIL: public chunk missing Mighty Networks"

# Index.html id collision check
INDEX = ROOT / "index.html"
index_text = INDEX.read_text(encoding="utf-8")
assert f'id="{INDEX_ID}"' not in index_text, f"PRE-FLIGHT FAIL: index.html already has {INDEX_ID}"

# Sitemap collision check
SITEMAP = ROOT / "sitemap.xml"
sitemap_text = SITEMAP.read_text(encoding="utf-8")
SITEMAP_LOC = "https://talonforgehq.github.io/atlas-store/chunks/chunk_335.html"
assert SITEMAP_LOC not in sitemap_text, f"PRE-FLIGHT FAIL: sitemap already has {SITEMAP_LOC}"

# Build-log collision check (the SHIP tick, not the LEAD tick — pitfall #67)
BUILD_LOG = ROOT / "build-log.html"
bl_text = BUILD_LOG.read_text(encoding="utf-8")
TICK_ID_SHIP = "2026-07-18-fast-exec-podia-520-mighty-networks-chunk-ship"
assert f'data-tick="{TICK_ID_SHIP}"' not in bl_text, f"PRE-FLIGHT FAIL: build-log already has {TICK_ID_SHIP}"

# ---------------------------------------------------------------------------
# Surface 1: source chunk — already on disk, no write needed
# ---------------------------------------------------------------------------
print(f"[surface 1/5] source {SOURCE.name} verified on disk ({SOURCE.stat().st_size} bytes)")

# ---------------------------------------------------------------------------
# Surface 2: public chunk — already on disk
# ---------------------------------------------------------------------------
print(f"[surface 2/5] public {PUBLIC.name} verified on disk ({PUBLIC.stat().st_size} bytes)")

# ---------------------------------------------------------------------------
# Surface 3: sitemap.xml <url> block insert (canonical pattern from sibling chunks)
# ---------------------------------------------------------------------------
# Use the chunk_334 (Memberstack 518) block as the canonical sibling for indent + shape.
# Find the last <url>...</url> block and append a new one before </urlset>.
canonical_block_re = re.compile(
    r"<url>\s*<loc>https://talonforgehq\.github\.io/atlas-store/chunks/chunk_334\.html</loc>\s*<lastmod>[^<]*</lastmod>\s*<changefreq>[^<]*</changefreq>\s*<priority>[^<]*</priority>\s*</url>"
)
m = canonical_block_re.search(sitemap_text)
assert m, "PRE-FLIGHT FAIL: could not find canonical chunk_334 sibling block in sitemap.xml"

NEW_BLOCK = (
    "<url>\n"
    "    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_335.html</loc>\n"
    "    <lastmod>2026-07-18</lastmod>\n"
    "    <changefreq>weekly</changefreq>\n"
    "    <priority>0.8</priority>\n"
    "  </url>"
)

# Verify the new block is NOT already in the sitemap (idempotency guard).
assert NEW_BLOCK not in sitemap_text, "PRE-FLIGHT FAIL: new chunk_335 block already in sitemap.xml"

# Insert before </urlset>
sitemap_new = sitemap_text.replace("</urlset>", NEW_BLOCK + "\n</urlset>")
SITEMAP.write_text(sitemap_new, encoding="utf-8")
print(f"[surface 3/5] sitemap.xml: inserted chunk_335 <url> block ({SITEMAP.stat().st_size} bytes total)")

# ---------------------------------------------------------------------------
# Surface 4: index.html card before </body>
# ---------------------------------------------------------------------------
INDEX_CARD = (
    f'<section id="{INDEX_ID}" class="chunk-card" data-vendor="mighty_networks" data-vertical="ai_creator_economy" data-tick="2026-07-18-fast-exec-podia-520">\n'
    f'  <h2><a href="chunks/chunk_335.html">Mighty Networks Review 2026: AI Community + Mighty Co-Host + AI-Engagement-Prediction (Lead 519)</a></h2>\n'
    f'  <p><strong>Vendor:</strong> Mighty Networks · <strong>Vertical:</strong> ai_creator_economy · <strong>Tier:</strong> 1</p>\n'
    f'  <p>AI-powered community platform + Mighty Co-Host AI community assistant + AI-member-engagement-prediction + AI-content-moderation + AI-event-recommendation + AI-course-recommendation. Per first-party About page: 75M web requests/day + 9B data points/month. Gina Bianchini (CEO + co-founder) + Tim Herby (CTO + co-founder). Audit wedge: end-to-end provenance, prompt-injection defense, cross-tenant isolation, immutable incident evidence.</p>\n'
    f'  <p><strong>Inbox:</strong> dpo@mightynetworks.com · <strong>Help:</strong> help@mightynetworks.com · <strong>Audit:</strong> $500 fixed / 48h</p>\n'
    f'</section>'
)

assert INDEX_CARD not in index_text, "PRE-FLIGHT FAIL: index.html card already present"

# Insert before </body>
index_new = index_text.replace("</body>", INDEX_CARD + "\n</body>")
INDEX.write_text(index_new, encoding="utf-8")
print(f"[surface 4/5] index.html: inserted chunk-{INDEX_ID.replace('chunk-', '')} card")

# ---------------------------------------------------------------------------
# Surface 5: build-log.html prepend (Variant C — find first tick-entry and prepend before it)
# ---------------------------------------------------------------------------
TICK_ID_LEAD = "2026-07-18-fast-exec-podia-520"  # pitfall #67: chunk content carries LEAD tick
NEW_ENTRY = (
    f'<div class="tick-entry" data-tick="{TICK_ID_SHIP}">\n'
    f'  <h2>Fast exec: chunk-ship Mighty Networks 519 (ai_creator_economy cohort sibling #8)</h2>\n'
    f'  <p><strong>Tick ID:</strong> <code>{TICK_ID_SHIP}</code></p>\n'
    f'  <p><strong>Artifact:</strong> Mighty Networks 519 chunk shipped as 5-surface ship: source <code>_chunks/chunk_334.html</code> + public <code>chunks/chunk_335.html</code> + sitemap <code>&lt;url&gt;</code> block + index.html card (id <code>chunk-334</code>) + build-log entry. Inbox-pivot from the prior Podia 520 tick, which noted "ship Mighty Networks 519 chunk... as a 5-surface chunk-ship in the next tick." Mighty Networks is the canonical AI-powered community platform + Mighty Co-Host AI community assistant + AI-member-engagement-prediction + AI-content-moderation + AI-event-recommendation + AI-course-recommendation, with 75M web requests/day + 9B data points/month per the first-party About page. Co-founders: Gina Bianchini (CEO + Co-Founder) + Tim Herby (CTO + Co-Founder).</p>\n'
    f'  <p><strong>Verification:</strong> mightynetworks.com/about returned HTTP 200 (server-rendered, names Gina Bianchini as CEO + co-founder + Tim Herby as CTO + co-founder + documents 75M web requests/day + 9B data points/month + human and AI development systems); mightynetworks.com/privacy-policy returned HTTP 200 + exposes mailto:dpo@mightynetworks.com + mailto:help@mightynetworks.com. Sitemap canonical block is the chunk_334 (Memberstack 518) sibling, with absolute <code>https://talonforgehq.github.io/atlas-store/chunks/chunk_335.html</code> loc (pitfall #61). Idempotency guards on every surface (pitfall #63). Slot discovery enumerated all three constraints upfront (pitfall #72): source _chunks/chunk_334.html (git ls-files empty = fresh slot), public chunks/chunk_335.html (does not exist = free), index.html id="chunk-334" (not present).</p>\n'
    f'  <p><strong>Vertical fit:</strong> Tier-1 ai_creator_economy cohort sibling #8 after Patreon 512 + Gumroad 513 + Kit 514 + Substack 515 + Kajabi 516 + Thinkific 517 + Memberstack 518 + Podia 520. Mighty Networks is the canonical community-led-growth AI-co-pilot layer for creators who monetize via memberships, courses, and events &mdash; distinct from Podia 520 (creator-courses + creator-community + creator-coaching + creator-webinars) which sits in the same cohort but at a different monetization surface. Canonical mailto is dpo@mightynetworks.com (verified on privacy-policy page).</p>\n'
    f'  <p><strong>Audit wedge:</strong> member request &rarr; Mighty Network tenant &rarr; space/course/event &rarr; retrieved community context &rarr; prompt/model/version &rarr; Mighty Co-Host recommendation, summary, moderation decision, or answer &rarr; human approval &rarr; notification, moderation, or commerce side effect, with prompt-injection defense, cross-Mighty-Network-tenant + cross-space + cross-event isolation, rollback, deletion, WORM evidence, SOC 2 CC6.1 + CC7.2, EU AI Act Articles 12 + 14, GDPR Articles 22 + 28, DSA Article 28 recommender-transparency, ISO 42001, NIST AI RMF, and OWASP LLM Top 10 coverage. 5 audit gaps: (1) end-to-end provenance, (2) model and policy versioning, (3) prompt-injection defense at the 75M-requests/day + 9B-data-points/month scale, (4) cross-Mighty-Network-tenant + cross-space isolation, (5) immutable incident evidence with WORM + cost-attribution.</p>\n'
    f'  <p><strong>Next:</strong> continue ai_creator_economy cohort with sibling #10 (e.g. Teachable &mdash; but Teachable is Zendesk-form-only, so a verified inbox probe is the gating step before lead 521). Pivot: ship Mighty Networks 519 chunk as the inbox-pivot path from the Podia 520 lead (dpo@mightynetworks.com verified inbox, no public chunk yet).</p>\n'
    f'  <p class="footer">Atlas @ Talon Forge &mdash; cron tick {TICK_ID_SHIP} &middot; chunk ship 519 + 5 surfaces + commit + push</p>\n'
    f'</div>\n\n\n'
)

# Verify the entry is NOT already in the build-log (idempotency guard)
assert f'data-tick="{TICK_ID_SHIP}"' not in bl_text, "PRE-FLIGHT FAIL: build-log already has TICK_ID_SHIP"

# Variant C: find the first <div class="tick-entry" and prepend before it
first_tick = bl_text.find('<div class="tick-entry"')
assert first_tick >= 0, "PRE-FLIGHT FAIL: no tick-entry found in build-log.html (Variant C)"
bl_new = bl_text[:first_tick] + NEW_ENTRY + bl_text[first_tick:]
BUILD_LOG.write_text(bl_new, encoding="utf-8")
print(f"[surface 5/5] build-log.html: prepended {TICK_ID_SHIP} entry ({BUILD_LOG.stat().st_size} bytes total)")

# ---------------------------------------------------------------------------
# Stage + commit + push
# ---------------------------------------------------------------------------
print("\n=== git stage + commit + push ===")
subprocess.run(["git", "-C", str(ROOT), "add", "-A"], check=True)
result = subprocess.run(
    ["git", "-C", str(ROOT), "status", "--short"],
    capture_output=True,
    text=True,
    check=True,
)
print("git status --short:")
print(result.stdout)

commit_msg = (
    f"chunk ship: Mighty Networks 519 (ai_creator_economy cohort sibling #8)\n\n"
    f"5-surface ship:\n"
    f"- _chunks/chunk_334.html (source, data-tick=2026-07-18-fast-exec-podia-520)\n"
    f"- chunks/chunk_335.html (public, lead-tick anchor)\n"
    f"- sitemap.xml <url> block for chunk_335\n"
    f"- index.html chunk-334 card\n"
    f"- build-log.html {TICK_ID_SHIP} entry\n\n"
    f"Co-founders: Gina Bianchini (CEO + Co-Founder) + Tim Herby (CTO + Co-Founder)\n"
    f"Scale: 75M web requests/day + 9B data points/month (per first-party About)\n"
    f"Inbox: dpo@mightynetworks.com (verified on privacy-policy page)\n"
    f"Inbox-pivot from prior tick (Podia 520) which noted 'ship Mighty Networks 519 chunk'\n"
    f"Idempotency guards on every surface (pitfall #63)\n"
    f"Slot discovery enumerated all 3 constraints upfront (pitfall #72)"
)

result = subprocess.run(
    ["git", "-C", str(ROOT), "commit", "-m", commit_msg],
    capture_output=True,
    text=True,
)
print("git commit stdout:")
print(result.stdout)
print("git commit stderr:")
print(result.stderr)
if result.returncode != 0 and "nothing to commit" not in result.stdout + result.stderr:
    print(f"git commit exit code: {result.returncode}")
    sys.exit(1)

result = subprocess.run(
    ["git", "-C", str(ROOT), "push", "origin", "main"],
    capture_output=True,
    text=True,
)
print("git push stdout:")
print(result.stdout)
print("git push stderr:")
print(result.stderr)
if result.returncode != 0:
    print(f"git push exit code: {result.returncode}")
    sys.exit(1)

print("\n=== ALL 5 SURFACES SHIPPED + COMMITTED + PUSHED ===")
