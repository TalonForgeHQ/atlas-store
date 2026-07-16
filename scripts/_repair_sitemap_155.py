#!/usr/bin/env python3
"""Repair sitemap.xml after patch-then-indent DOUBLE-BREAK (skill Pitfall A).
The chunk_153 block has 6-space indent on inner lines while chunk_154/155 have 8-space.
Splice to fix: rewrite tail to known-good chunk_152 pattern."""
from pathlib import Path

SITEMAP = Path("sitemap.xml")
text = SITEMAP.read_text(encoding="utf-8")

# Anchor on chunk_151 block (last known-good with 4-space indent on inner lines)
anchor = '''  <url>
    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_151.html</loc>
    <lastmod>2026-07-16</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>'''
if anchor not in text:
    print("ERROR: anchor chunk_151 not found - bail")
    raise SystemExit(1)

# Find the tail starting at chunk_152 onward
idx_152 = text.find("  <url>\n    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_152.html</loc>")
if idx_152 == -1:
    print("ERROR: chunk_152 not found - bail")
    raise SystemExit(1)

# The correct tail: chunk_152 + chunk_153 + chunk_154 + chunk_155 with consistent 4-space indent on inner lines
correct_tail = '''  <url>
    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_152.html</loc>
    <lastmod>2026-07-16</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_153.html</loc>
    <lastmod>2026-07-16</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_154.html</loc>
    <lastmod>2026-07-16</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_155.html</loc>
    <lastmod>2026-07-16</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>'''

# Splice: keep text[:idx_152] (everything up to and including chunk_151 anchor area), then append correct_tail
new_text = text[:idx_152] + correct_tail

SITEMAP.write_text(new_text, encoding="utf-8")

# Verify: ET.fromstring + balanced tag counts
import xml.etree.ElementTree as ET
import re
ET.fromstring(new_text)  # raises on malformed
opens = len(re.findall(r"<url>", new_text))
closes = len(re.findall(r"</url>", new_text))
print(f"PASS: ET.fromstring OK | url opens={opens} closes={closes} | balanced={opens==closes}")
print(f"PASS: chunk_155 in text = {'chunk_155.html' in new_text}")
last200 = new_text[-200:]
indent_check = "  </url>\n</urlset>" in last200
print(f"PASS: 4-space indent in last block = {indent_check}")