"""One-shot sitemap repair + chunk_174 insertion."""
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
sitemap = REPO / "sitemap.xml"
text = sitemap.read_text(encoding="utf-8")

# 1. Repair the orphan chunk_100 block to canonical 6/6/6/4 indentation.
old_orphan = """    <url>
      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_100.html</loc>
      <lastmod>2026-07-16</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
      
    </urlset>"""
new_orphan = """    <url>
      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_100.html</loc>
      <lastmod>2026-07-16</lastmod>
      <changefreq>monthly</changefreq>
      <priority>0.8</priority>
    </url>
    <url>
      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_174.html</loc>
      <lastmod>2026-07-16</lastmod>
      <changefreq>monthly</changefreq>
      <priority>0.8</priority>
    </url>
  </urlset>"""

assert old_orphan in text, "old_orphan block not found — sitemap shape changed"
text2 = text.replace(old_orphan, new_orphan, 1)

# Verify
import re
opens = len(re.findall(r"<url>", text2))
closes = len(re.findall(r"</url>", text2))
print(f"After repair: <url>={opens}, </url>={closes}")
assert opens == closes, f"unbalanced tags: {opens} vs {closes}"

# XML well-formed check
import xml.etree.ElementTree as ET
try:
    ET.fromstring(text2)
    print("sitemap parses cleanly with ET.fromstring()")
except ET.ParseError as e:
    print(f"PARSE ERROR: {e}")
    raise

# Write
sitemap.write_text(text2, encoding="utf-8")
print(f"Wrote {sitemap} ({len(text2)} bytes, was {len(text)})")
print("OK sitemap repaired + chunk_174 inserted.")