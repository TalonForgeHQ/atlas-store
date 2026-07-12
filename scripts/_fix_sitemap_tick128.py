"""Add missing chunks 98-115 to sitemap.xml."""
import re
from pathlib import Path
import xml.etree.ElementTree as ET

SITEMAP = r"C:\Users\Potts\projects\atlas-store\sitemap.xml"
CHUNKS_DIR = Path(r"C:\Users\Potts\projects\atlas-store\_chunks")

# Find existing chunks in sitemap
text = Path(SITEMAP).read_text(encoding="utf-8")
existing = sorted({int(m) for m in re.findall(r"chunk_(\d+)\.html", text)}, key=int)
print(f"existing chunks in sitemap: {existing[-5:]}...{existing[-1:]}")

# Find all chunks on disk
disk = sorted({int(p.stem.split("_")[1]) for p in CHUNKS_DIR.glob("chunk_*.html")}, key=int)
print(f"chunks on disk: {disk[-5:]}...{disk[-1:]}")

missing = [n for n in disk if n not in existing]
print(f"missing: {missing}")

# Build the new URL blocks
new_blocks = ""
for n in missing:
    new_blocks += f'''                                    <url>
                                        <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_{n}.html</loc>
                                        <lastmod>2026-07-12</lastmod>
                                        <changefreq>monthly</changefreq>
                                        <priority>0.8</priority>
                                    </url>
'''

# Insert just before </urlset>
assert text.count("</urlset>") == 1
new_text = text.replace("</urlset>", new_blocks + "</urlset>", 1)
Path(SITEMAP).write_text(new_text, encoding="utf-8")

# Verify well-formed
tree = ET.fromstring(new_text)
ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
urls = tree.findall("s:url/s:loc", ns)
print(f"OK: sitemap.xml well-formed, {len(urls)} URLs total")
for n in missing:
    cnt = sum(1 for u in urls if f"chunk_{n}.html" in u.text)
    print(f"  chunk_{n}: {cnt} match(es)")