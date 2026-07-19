"""Resume ship 591 — ONLY insert index.html card.

The main ship (ship_591_lucidspark_sitemap.py) wrote 5 of 6 surfaces (CSV + template + source + public + sitemap)
and tripped on the index.html surface because index.html uses </html> as its closing tag, NOT </body>.
This script inserts the chunk_379 card BEFORE </html> (using rfind for unique last-occurrence).

Idempotency guard: if the anchor `id="chunk-379"` is already in index.html, exit 0.
"""
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
INDEX = REPO / "index.html"
INDEX_ID = "chunk-591-card"  # Use a distinct id since chunk-379 number is already used for source slot
# Actually use chunk-379 — but check carefully
INDEX_ID = "chunk-379"
LEAD_INDEX = "591"
TICK_ID_LEAD = "2026-07-19-fast-exec-lucidspark-591"
VENDOR = "Lucidspark"
EMAIL = "legal@lucid.co"
SRC_CHUNK_NUM = 379
PUB_CHUNK_NUM = 380

INDEX_NEW_CARD = f"""
<section id="{INDEX_ID}" class="seo-chunk-card" data-tick="{TICK_ID_LEAD}" data-lead="{LEAD_INDEX}" data-vendor="{VENDOR}" data-chunk-src="{SRC_CHUNK_NUM}" data-chunk-pub="{PUB_CHUNK_NUM}">
<h2>{VENDOR} (ai_whiteboard cohort sibling #5) — Lucidspark AI audit evidence-gap map</h2>
<p><strong>Lead 591</strong> · {VENDOR} · <code>{EMAIL}</code> · ai_whiteboard · tier 1</p>
<p>Whiteboard + Lucid AI surface (Collaborative AI + Auto-Summarize + AI Cluster + AI Mind-Map + AI Action Items + AI Diagramming + AI Facilitation Prompts + AI Templates) — EU AI Act Art. 53(d) + FedRAMP Moderate + SOC 2 Type II + ISO 27001 + ISO 42001 + Schrems II SCC + GDPR Art. 28 evidence. Foundational Lucidspark siblings: Miro opener 587 + FigJam 588 + Mural 589 + Conceptboard 590.</p>
<p><a href="chunks/chunk_{PUB_CHUNK_NUM}.html">Read the full evidence-gap map →</a></p>
</section>
"""

# Idempotency guard
text = INDEX.read_text(encoding="utf-8")
if f'id="{INDEX_ID}"' in text:
    print(f"[SKIP] id=\"{INDEX_ID}\" already in index.html — surface 6 already wrote.")
    raise SystemExit(0)

# Find last </html> and insert BEFORE it (rfind for unique last-occurrence)
html_close_idx = text.rfind("</html>")
assert html_close_idx > 0, "no </html> in index.html"

new_index = text[:html_close_idx] + INDEX_NEW_CARD + "\n" + text[html_close_idx:]
# Verify uniqueness
assert new_index.count(f'id="{INDEX_ID}"') == 1, f"id {INDEX_ID} appears more than once"
INDEX.write_text(new_index, encoding="utf-8")
print(f"[OK] index.html: chunk-{INDEX_ID} card inserted before </html>")
