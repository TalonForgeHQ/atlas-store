"""Repair sitemap.xml indent drift via regex — fix any <url> block whose <loc>/<lastmod> lines
have 20+ leading spaces (orphan from patch tool over-indent)."""
import re
from pathlib import Path

p = Path(r"C:\Users\Potts\projects\atlas-store\sitemap.xml")
raw = p.read_bytes()
t = raw.decode('utf-8')

# Normalize: replace any leading whitespace + <loc>https://talonforgehq.../chunks/chunk_NNN.html</loc>
# that's on a line with 20+ leading spaces back to 14 spaces (the canonical indent inside <url>).
# Similarly for <lastmod>2026-07-17</lastmod> with 20+ leading spaces.
# This pattern ONLY fires if the indentation is over-indented (>14 spaces), so legitimate
# well-formed lines (10 spaces for <url>, 14 for inner) are untouched.

# Match over-indented <loc> blocks inside <url>
t2 = re.sub(
    r'^[ \t]{20,}<loc>(https://talonforgehq\.github\.io/atlas-store/chunks/chunk_\d+\.html)</loc>',
    r'              <loc>\1</loc>',
    t,
    flags=re.MULTILINE,
)
t2 = re.sub(
    r'^[ \t]{20,}<lastmod>(\d{4}-\d{2}-\d{2})</lastmod>',
    r'              <lastmod>\1</lastmod>',
    t2,
    flags=re.MULTILINE,
)
# Normalize <url> over-indented openers (should be 10 spaces; restore if >14)
t2 = re.sub(
    r'^[ \t]{20,}<url>$',
    r'          <url>',
    t2,
    flags=re.MULTILINE,
)
# Normalize </url> over-indented closers (should be 10 spaces; restore if >14)
t2 = re.sub(
    r'^[ \t]{20,}</url>$',
    r'          </url>',
    t2,
    flags=re.MULTILINE,
)
# Normalize </urlset> (should be 6 spaces; restore if >10)
t2 = re.sub(
    r'^[ \t]{10,}</urlset>$',
    r'      </urlset>',
    t2,
    flags=re.MULTILINE,
)

# Verify the tail now looks canonical
tail = t2[-700:]
print('tail after repair:')
print(tail)

# Validate parse + tag balance
import xml.etree.ElementTree as ET
ET.fromstring(t2)
url_open = len(re.findall(r"<url>", t2))
url_close = len(re.findall(r"</url>", t2))
assert url_open == url_close, f"unbalanced <url> tags: open={url_open} close={url_close}"

p.write_text(t2, encoding='utf-8', newline='')  # preserve original CRLF? actually \r\n was kept by read + decode

# Re-check CRLF preserved
final = p.read_bytes()
assert final.count(b'\r\n') > 1000, "CRLF lost"
crlf_count = final.count(b'\r\n')
print(f"OK sitemap repaired. bytes={len(final)} <url> open={url_open} close={url_close} CRLF preserved={crlf_count}")