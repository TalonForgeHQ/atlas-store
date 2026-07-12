import sys, re
from pathlib import Path

SITEMAP = r"C:\Users\Potts\projects\atlas-store\sitemap.xml"
text = Path(SITEMAP).read_text(encoding="utf-8")

# The closing pattern (lines from chunk_95 through </urlset>)
# Need to insert chunk_96 + chunk_97 before </urlset>, preserving indentation style of chunk_95
old_block = '''    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_95.html</loc>
    <lastmod>2026-07-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>'''

new_block = '''    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_95.html</loc>
    <lastmod>2026-07-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_96.html</loc>
    <lastmod>2026-07-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_97.html</loc>
    <lastmod>2026-07-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>'''

assert old_block in text, "old_block not found"
assert text.count("chunk_96") == 0, "chunk_96 already present"
assert text.count("chunk_97") == 0, "chunk_97 already present"

text = text.replace(old_block, new_block, 1)

Path(SITEMAP).write_text(text, encoding="utf-8")

# Verify well-formed XML + count
import xml.etree.ElementTree as ET
tree = ET.fromstring(text)
ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
urls = tree.findall("s:url/s:loc", ns)
print(f"OK: sitemap.xml well-formed, {len(urls)} URLs")
print(f"  chunk_96 present: {sum(1 for u in urls if 'chunk_96' in u.text)}")
print(f"  chunk_97 present: {sum(1 for u in urls if 'chunk_97' in u.text)}")
