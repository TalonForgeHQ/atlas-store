"""Repair sitemap.xml over-indentation from sibling-subagent patch."""
from pathlib import Path
p = Path("C:/Users/Potts/projects/atlas-store/sitemap.xml")
text = p.read_text(encoding="utf-8")
# The new chunk_146 block has 8-space indent on inner lines; should be 4-space.
old_block = '''        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
      </url>
      <url>
        <loc>https://atlas-talon-store.com/chunks/chunk_146.html</loc>
        <lastmod>2026-07-16</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
      </url>
    </urlset>'''
new_block = '''    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://atlas-talon-store.com/chunks/chunk_146.html</loc>
    <lastmod>2026-07-16</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>'''
assert old_block in text, "old_block not found"
text2 = text.replace(old_block, new_block)
p.write_text(text2, encoding="utf-8")
import xml.etree.ElementTree as ET
ET.fromstring(text2)
print("OK sitemap.xml repaired + parses")