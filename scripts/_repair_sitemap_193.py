#!/usr/bin/env python3
"""Repair sitemap.xml indent regression from patch-then-indent-fix DOUBLE-BREAK."""
from pathlib import Path

p = Path("C:/Users/Potts/projects/atlas-store/sitemap.xml")
text = p.read_text(encoding="utf-8")

# Target the bad block and replace with canonical 12-space indent
bad = """            <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_192.html</loc>
                        <lastmod>2026-07-16</lastmod>
                        <changefreq>monthly</changefreq>
                        <priority>0.8</priority>
                      </url>
                      <url>
                        <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_193.html</loc>
                        <lastmod>2026-07-16</lastmod>
                        <changefreq>monthly</changefreq>
                        <priority>0.8</priority>
                      </url>
                    </urlset>"""

good = """            <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_192.html</loc>
            <lastmod>2026-07-16</lastmod>
            <changefreq>monthly</changefreq>
            <priority>0.8</priority>
          </url>
          <url>
            <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_193.html</loc>
            <lastmod>2026-07-16</lastmod>
            <changefreq>monthly</changefreq>
            <priority>0.8</priority>
          </url>
        </urlset>"""

assert bad in text, "bad block not found"
text = text.replace(bad, good)
p.write_text(text, encoding="utf-8")

# Verify
import xml.etree.ElementTree as ET, re
try:
    ET.fromstring(text)
    print("OK: sitemap parses")
except ET.ParseError as e:
    print("FAIL:", e)
    raise
opens = len(re.findall(r"<url>", text))
closes = len(re.findall(r"</url>", text))
print(f"<url> open/close: {opens}/{closes} balanced: {opens == closes}")
print(f"chunk_192 mentions: {text.count('chunk_192')}")
print(f"chunk_193 mentions: {text.count('chunk_193')}")
print(f"last 12 lines:")
for line in text.splitlines()[-12:]:
    print(line)