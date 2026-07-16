"""Repair sitemap.xml: orphan <loc> for chunk_219 + mixed indent.

Damage observed:
1. chunk_219 entry has NO <url> opener — orphan <loc> starting at line 1191
2. Surrounding blocks have inconsistent indent (some 2-space <url>, some 4-space)
3. <url> open (198) != </url> close (199) — extra closer

Strategy: rewrite the tail from line 1185 (chunk_218 opener) onward into a
clean, uniform block with: 2-space <url>, 4-space <loc>, 4-space lastmod,
4-space changefreq, 4-space priority, 2-space </url>.

Use git show origin/main:sitemap.xml as ground-truth for the prior chunk
indentation shape (chunk_217 was already shipped at origin/main).
"""
import subprocess
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
sitemap = REPO / "sitemap.xml"

text = sitemap.read_text(encoding="utf-8")

# Verify damage first
import re
url_open = len(re.findall(r"<url>", text))
url_close = len(re.findall(r"</url>", text))
loc_open = len(re.findall(r"<loc>", text))
print(f"PRE: <url>={url_open} </url>={url_close} <loc>={loc_open}")

# Locate chunk_218 opener
idx_218 = text.find('https://talonforgehq.github.io/atlas-store/chunks/chunk_218.html')
print(f"chunk_218 idx: {idx_218}")
if idx_218 < 0:
    raise SystemExit("chunk_218 not found in sitemap.xml")

# Find the <url> opener just before chunk_218
url_open_before_218 = text.rfind('<url>', 0, idx_218)
print(f"<url> opener before chunk_218: char {url_open_before_218}")

# Find the </urlset> closing tag at end
idx_urlset_close = text.find('</urlset>')
print(f"</urlset> idx: {idx_urlset_close}")
assert idx_urlset_close > 0

# Now find the </url> that closes chunk_218 (the one between chunk_218 body and chunk_219 orphan)
# The orphan <loc> for 219 starts at "    <loc>https://...chunk_219.html"
idx_orphan_loc = text.find('chunk_219.html')
print(f"chunk_219 orphan idx: {idx_orphan_loc}")

# Find the </url> that closes whatever is right before the orphan
# We need: replace from url_open_before_218 through idx_urlset_close with a clean rewrite.
new_block = """  <url>
    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_218.html</loc>
    <lastmod>2026-07-16</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_219.html</loc>
    <lastmod>2026-07-16</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>"""

new_text = text[:url_open_before_218] + new_block
print(f"\nPRE-write verify:\n  BEFORE: len={len(text)}")
print(f"  AFTER : len={len(new_text)} (delta {len(new_text) - len(text):+d})")

# Write
sitemap.write_text(new_text, encoding="utf-8")
print("Wrote sitemap.xml")

# Re-verify after write
text2 = sitemap.read_text(encoding="utf-8")
url_open2 = len(re.findall(r"<url>", text2))
url_close2 = len(re.findall(r"</url>", text2))
loc_open2 = len(re.findall(r"<loc>", text2))
print(f"POST: <url>={url_open2} </url>={url_close2} <loc>={loc_open2}")
assert url_open2 == url_close2, f"<url>={url_open2} != </url>={url_close2}"
assert url_open2 == loc_open2, f"<url>={url_open2} != <loc>={loc_open2}"
print("BALANCED ✓")

# Try parse via ElementTree
import xml.etree.ElementTree as ET
try:
    root = ET.fromstring(text2)
    print(f"ET.fromstring OK — root tag = {root.tag}, child count = {len(list(root))}")
except ET.ParseError as e:
    print(f"ET.fromstring FAILED: {e}")
    raise

# Verify both anchors present
assert 'chunk_218.html' in text2
assert 'chunk_219.html' in text2
print("BOTH chunk_218 + chunk_219 anchors present ✓")

# Check indent: the new block + the immediate predecessor (chunk_217) should both
# have 2-space <url> opener
block_218 = text2[url_open_before_218:url_open_before_218+200]
print("\nBlock 218:\n" + block_218[:200])
