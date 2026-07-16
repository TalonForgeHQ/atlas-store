"""Final repair: rewrite the tail of sitemap.xml from chunk_235 onwards to canonical."""
from pathlib import Path
import xml.etree.ElementTree as ET

SITEMAP = Path(r"C:\Users\Potts\projects\atlas-store\sitemap.xml")
text = SITEMAP.read_text(encoding="utf-8")

# Anchor on chunk_235 (the last known-good block)
idx_235 = text.find("chunk_235")
assert idx_235 > 0

# Back up to the start of that <url> opener
search_start = text.rfind("<url>", 0, idx_235)
assert search_start > 0

# Canonical tail: 235 + 236 + 237 + urlset close
tail = (
    "      <url>\n"
    "        <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_235.html</loc>\n"
    "        <lastmod>2026-07-17</lastmod>\n"
    "      </url>\n"
    "      <url>\n"
    "        <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_236.html</loc>\n"
    "        <lastmod>2026-07-17</lastmod>\n"
    "      </url>\n"
    "      <url>\n"
    "        <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_237.html</loc>\n"
    "        <lastmod>2026-07-17</lastmod>\n"
    "      </url>\n"
    "    </urlset>\n"
)
new_text = text[:search_start] + tail

SITEMAP.write_text(new_text, encoding="utf-8")

# Verify
text2 = SITEMAP.read_text(encoding="utf-8")
n_open = text2.count("<url>")
n_close = text2.count("</url>")
print(f"<url>={n_open} </url>={n_close}")
assert n_open == n_close, f"unbalanced: {n_open} vs {n_close}"

# ET parse
root = ET.fromstring(text2)
print(f"OK: sitemap.xml parses, balanced url tags, chunk_235+236+237 present")
print(f"Last 12 lines:")
for ln in text2.split("\n")[-12:]:
    print(repr(ln))