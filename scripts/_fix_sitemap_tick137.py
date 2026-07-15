"""Fix sitemap.xml indent for chunk_120 + chunk_121 blocks (6-space -> 4-space)."""
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
sitemap = REPO / "sitemap.xml"
text = sitemap.read_text(encoding="utf-8")

# The two over-indented blocks
broken_block = """  <url>
      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_120.html</loc>
      <lastmod>2026-07-15</lastmod>
      <changefreq>monthly</changefreq>
      <priority>0.8</priority>
    </url>
    <url>
      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_121.html</loc>
      <lastmod>2026-07-15</lastmod>
      <changefreq>monthly</changefreq>
      <priority>0.8</priority>
    </url>
  </urlset>"""

fixed_block = """  <url>
    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_120.html</loc>
    <lastmod>2026-07-15</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_121.html</loc>
    <lastmod>2026-07-15</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>"""

assert broken_block in text, "broken block not found in sitemap.xml"
text = text.replace(broken_block, fixed_block)
sitemap.write_text(text, encoding="utf-8")
print("sitemap.xml indent fixed")

# Verify XML validity and count URLs
import xml.etree.ElementTree as ET
tree = ET.fromstring(text)
url_count = sum(1 for _ in tree.iter('{*}url'))
chunk_121_count = text.count("chunk_121.html")
print(f"Valid XML, {url_count} <url> elements, chunk_121 occurrences: {chunk_121_count}")
# Verify the indent of the chunk_120 + chunk_121 lines
lines = text.splitlines()
for ln in lines:
    if 'chunk_120.html' in ln or 'chunk_121.html' in ln:
        print(f"  {ln}")