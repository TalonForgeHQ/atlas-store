#!/usr/bin/env python3
"""Insert chunk_646 url block into sitemap.xml with 4-space outer + 6-space inner indent.
Pitfall #93 — probe last sibling indent first."""
import re
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
SITEMAP = REPO / "sitemap.xml"

NEW_URL = """    <url>
      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_646.html</loc>
      <lastmod>2026-07-19</lastmod>
      <changefreq>monthly</changefreq>
      <priority>0.8</priority>
  </url>
"""

# Pre-flight: idempotency guard
text = SITEMAP.read_text(encoding="utf-8")
chunk_646_marker = "chunk_646.html"
assert text.count(chunk_646_marker) == 0, "chunk_646 already in sitemap.xml"

# Probe last sibling indent (pitfall #93) — find last <url> block
matches = list(re.finditer(r"<url>", text))
assert matches, "no <url> blocks in sitemap.xml"
last_url_idx = matches[-1].start()
# Get last <loc> line to determine indent era
last_loc = re.search(r"<loc>[^<]+</loc>", text[last_url_idx:])
assert last_loc, "last url has no <loc>"
# Count leading whitespace before this <loc>
loc_match = re.search(r"(\n)([ \t]*)<loc>", text[last_url_idx:])
assert loc_match, "no <loc> found near last url"
indent = loc_match.group(2)
NEW_LOC_INDENT = indent

# Insert new block before </urlset>
close = text.rfind("</urlset>")
assert close > 0, "no </urlset> in sitemap.xml"
new_block = "    <url>\n      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_646.html</loc>\n      <lastmod>2026-07-19</lastmod>\n      <changefreq>monthly</changefreq>\n      <priority>0.8</priority>\n  </url>\n"
new_text = text[:close] + new_block + text[close:]

# Verify balanced url tags
url_open = new_text.count("<url>")
url_close = new_text.count("</url>")
assert url_open == url_close, f"unbalanced <url>/</url>: {url_open} open / {url_close} close"
assert new_text.count("chunk_646.html") == 1, "chunk_646 marker count != 1 after insert"

# Verify XML well-formed
import xml.etree.ElementTree as ET
ET.fromstring(new_text)
print(f"[OK] sitemap.xml: chunk_646 block inserted (urls={url_open}, indent_match={repr(indent)})")

SITEMAP.write_text(new_text, encoding="utf-8")
