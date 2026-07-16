"""Repair sitemap.xml: chunk_236 and chunk_237 blocks must have canonical 8-space indent."""
import re
from pathlib import Path

SITEMAP = Path(r"C:\Users\Potts\projects\atlas-store\sitemap.xml")
text = SITEMAP.read_text(encoding="utf-8")

# Find the chunk_236 block and replace with canonical 8-space indent
canonical_block_236 = (
    "      <url>\n"
    "        <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_236.html</loc>\n"
    "        <lastmod>2026-07-17</lastmod>\n"
    "      </url>"
)
canonical_block_237 = (
    "      <url>\n"
    "        <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_237.html</loc>\n"
    "        <lastmod>2026-07-17</lastmod>\n"
    "      </url>"
)

# Locate the chunk_236 line and the closing </urlset> and rewrite the trailing tail
idx_236 = text.find("chunk_236")
idx_urlset_close = text.rfind("</urlset>")
assert idx_236 > 0 and idx_urlset_close > idx_236, "anchor missing"

# Build canonical tail
tail = canonical_block_236 + "\n" + canonical_block_237 + "\n    </urlset>"
new_text = text[:idx_236] + tail

# But we need to back up to the start of the previous block's <url> open
# Actually just splice: find the line right before chunk_236 line (which should be `<url>` opener)
# Simpler: find the last `      <url>` before chunk_236 and replace from there to </urlset>
search_start = text.rfind("<url>", 0, idx_236)
assert search_start > 0
new_text = text[:search_start] + "      <url>\n" + tail

SITEMAP.write_text(new_text, encoding="utf-8")

# Verify
text2 = SITEMAP.read_text(encoding="utf-8")
# Check balanced
assert text2.count("<url>") == text2.count("</url>"), f"unbalanced: {text2.count('<url>')} vs {text2.count('</url>')}"
# Check chunk_236 + chunk_237 present
assert "chunk_236.html" in text2
assert "chunk_237.html" in text2
# Check ET parses
import xml.etree.ElementTree as ET
root = ET.fromstring(text2)
print(f"OK: sitemap.xml parses, balanced url tags, chunk_236+chunk_237 present")

# Print last 12 lines
for ln in text2.split("\n")[-12:]:
    print(repr(ln))