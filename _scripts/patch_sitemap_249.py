import re
from pathlib import Path

sitemap = Path("C:/Users/Potts/projects/atlas-store/sitemap.xml").read_text(encoding="utf-8")

# Find the chunk_248 block (the last existing entry before </urlset>)
anchor = '<loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_248.html</loc>\n        <lastmod>2026-07-17</lastmod>\n      </url>\n'
assert anchor in sitemap, "chunk_248 anchor not found in sitemap.xml"

new_block = '''<loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_248.html</loc>
        <lastmod>2026-07-17</lastmod>
      </url>

      <url>
        <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_249.html</loc>
        <lastmod>2026-07-17</lastmod>
      </url>
'''

new_sitemap = sitemap.replace(anchor, new_block, 1)
Path("C:/Users/Potts/projects/atlas-store/sitemap.xml").write_text(new_sitemap, encoding="utf-8")
print("OK sitemap patched")

# Verify ET parse + balanced tags
import xml.etree.ElementTree as ET
try:
    root = ET.fromstring(new_sitemap)
    print(f"ET parse OK, root tag: {root.tag}")
except ET.ParseError as e:
    print(f"PARSE ERROR: {e}")

opens = len(re.findall(r'<url>', new_sitemap))
closes = len(re.findall(r'</url>', new_sitemap))
print(f'<url> opens={opens}, closes={closes}, balanced={opens==closes}')
opens = len(re.findall(r'<loc>', new_sitemap))
closes = len(re.findall(r'</loc>', new_sitemap))
print(f'<loc> opens={opens}, closes={closes}, balanced={opens==closes}')
print(f'chunk_249 entries: {new_sitemap.count("chunk_249.html")}')
