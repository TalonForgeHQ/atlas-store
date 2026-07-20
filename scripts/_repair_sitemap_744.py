"""Repair sitemap.xml indent drift introduced by patch tool. Fix <url>/<loc>/<lastmod>
lines that landed at 10 spaces (canonical) but surrounded by 14-space-or-deeper lines
from sibling cron ticks. Also normalize </urlset> tail to 2 spaces per verified invariant."""
import re
from pathlib import Path

p = Path(r"C:\Users\Potts\projects\atlas-store\sitemap.xml")
raw = p.read_bytes()
t = raw.decode('utf-8')

# Normalize any line with 14+ leading spaces holding <loc> chunk URL → 14 spaces
t2 = re.sub(
    r'^[ \t]{14,}<loc>(https://talonforgehq\.github\.io/atlas-store/chunks/chunk_\d+\.html)</loc>',
    r'              <loc>\1</loc>',
    t,
    flags=re.MULTILINE,
)
t2 = re.sub(
    r'^[ \t]{14,}<lastmod>(\d{4}-\d{2}-\d{2})</lastmod>',
    r'              <lastmod>\1</lastmod>',
    t2,
    flags=re.MULTILINE,
)
# Normalize <url> openers to 10 spaces if at 14+
t2 = re.sub(
    r'^[ \t]{14,}<url>$',
    r'          <url>',
    t2,
    flags=re.MULTILINE,
)
# Normalize </url> closers to 10 spaces if at 14+
t2 = re.sub(
    r'^[ \t]{14,}</url>$',
    r'          </url>',
    t2,
    flags=re.MULTILINE,
)
# Normalize </urlset> tail to 2 spaces (verified invariant for atlas-store post-tick-668)
t2 = re.sub(
    r'^[ \t]{2,}</urlset>$',
    r'  </urlset>',
    t2,
    flags=re.MULTILINE,
)

# Validate parse + tag balance
import xml.etree.ElementTree as ET
ET.fromstring(t2)
url_open = len(re.findall(r"<url>", t2))
url_close = len(re.findall(r"</url>", t2))
assert url_open == url_close, f"unbalanced <url> tags: open={url_open} close={url_close}"

# Tail invariant check
last_line = t2.rstrip().splitlines()[-1]
assert last_line == '  </urlset>', f"sitemap tail wrong: {last_line!r}"

# Write back preserving CRLF
p.write_bytes(t2.encode('utf-8'))
final = p.read_bytes()
crlf = final.count(b'\r\n')
print(f"OK sitemap repaired. bytes={len(final)} <url> open={url_open} close={url_close} CRLF preserved={crlf}")
print(f"tail: {last_line!r}")