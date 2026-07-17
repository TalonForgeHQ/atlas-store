"""
Append chunk_283 <url> block to sitemap.xml.
Anchor: `</urlset>` is unique in the file.
Pattern: replace `          </urlset>` with `<new block>\n          </urlset>`.
"""
from pathlib import Path

SITEMAP = Path("C:/Users/Potts/projects/atlas-store/sitemap.xml")
text = SITEMAP.read_text(encoding="utf-8")

NEW_BLOCK = """          <url>
              <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_283.html</loc>
              <lastmod>2026-07-17</lastmod>
          </url>
"""

# Read raw bytes for CRLF-correct splice
data = SITEMAP.read_bytes()
old = b'</url>\r\n          </urlset>'
new = b'</url>\r\n' + NEW_BLOCK.encode('utf-8') + b'          </urlset>'

if b'chunk_283.html' in data:
    print("chunk_283 already in sitemap.xml — skipping")
else:
    count = data.count(old)
    assert count == 1, f"old anchor pattern expected exactly once, found {count}"
    data2 = data.replace(old, new, 1)
    SITEMAP.write_bytes(data2)
    print(f"Inserted chunk_283 url block (CRLF-preserved, +{len(data2)-len(data)} bytes)")

# Verify
import xml.etree.ElementTree as ET
text3 = SITEMAP.read_text(encoding="utf-8")
ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
tree = ET.fromstring(text3)
locs = [u.find(f"{ns}loc").text for u in tree.findall(f"{ns}url")]
assert any('chunk_283' in l for l in locs), "chunk_283 not in parsed locs"
print(f"OK: sitemap parses clean, {len(locs)} locs, chunk_283 present")
print(f"  last 3 locs: {locs[-3:]}")