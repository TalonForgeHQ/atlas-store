"""Patch sitemap.xml: replace chunk_237 block with chunk_238 entry."""
from pathlib import Path
import xml.etree.ElementTree as ET

SITEMAP = Path(r"C:\Users\Potts\projects\atlas-store\sitemap.xml")
text = SITEMAP.read_text(encoding="utf-8")

# Anchor: replace the chunk_237 block with chunk_238
old = (
    "      <url>\n"
    "        <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_237.html</loc>\n"
    "        <lastmod>2026-07-17</lastmod>\n"
    "      </url>\n"
    "    </urlset>"
)
new = (
    "      <url>\n"
    "        <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_237.html</loc>\n"
    "        <lastmod>2026-07-17</lastmod>\n"
    "      </url>\n"
    "      <url>\n"
    "        <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_238.html</loc>\n"
    "        <lastmod>2026-07-17</lastmod>\n"
    "      </url>\n"
    "    </urlset>"
)

assert old in text, "chunk_237 block not found in sitemap"
new_text = text.replace(old, new, 1)
SITEMAP.write_text(new_text, encoding="utf-8")

# Verify
text2 = SITEMAP.read_text(encoding="utf-8")
n_open = text2.count("<url>")
n_close = text2.count("</url>")
assert n_open == n_close, f"unbalanced: {n_open} vs {n_close}"
root = ET.fromstring(text2)
assert "chunk_238.html" in text2
print(f"OK: sitemap has chunk_238, balanced {n_open}={n_close}, parses clean")