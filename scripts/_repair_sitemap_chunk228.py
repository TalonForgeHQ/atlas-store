"""Repair sitemap.xml tail after the patch over-indent.
Strategy: rewrite the tail from a known-good 6-space indent anchor (chunk_224 block)
back to </urlset>."""
import re
from pathlib import Path

SITEMAP = Path(r"C:\Users\Potts\projects\atlas-store\sitemap.xml")
text = SITEMAP.read_text(encoding="utf-8")

# Anchor: the known-good chunk_224 block (6-space indented <url>, 8-space <loc>, 6-space closer).
anchor = """      <url>
        <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_224.html</loc>
        <lastmod>2026-07-17</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
      </url>
"""

assert text.count(anchor) == 1, f"anchor must be unique, found {text.count(anchor)} matches"
tail_start = text.find(anchor) + len(anchor)

new_tail = """      <url>
        <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_227.html</loc>
        <lastmod>2026-07-17</lastmod>
      </url>
      <url>
        <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_228.html</loc>
        <lastmod>2026-07-17</lastmod>
      </url>
</urlset>
"""

fixed = text[:tail_start] + new_tail
SITEMAP.write_text(fixed, encoding="utf-8")

# Verify balanced tags + parse + count
import xml.etree.ElementTree as ET
ET.fromstring(fixed)  # raises ParseError on malformed XML
opens = len(re.findall(r"<url>", fixed))
closes = len(re.findall(r"</url>", fixed))
urlset_closes = len(re.findall(r"</urlset>", fixed))
print(f"OK sitemap repaired: <url>={opens}, </url>={closes}, </urlset>={urlset_closes}")
assert opens == closes, f"unbalanced: opens={opens} closes={closes}"
assert urlset_closes == 1
# Verify chunk_228 present
assert "chunk_228" in fixed
assert "chunk_227" in fixed
print(f"chunk_228 + chunk_227 present, {len(fixed)} bytes total")