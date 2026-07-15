"""Repair sitemap.xml: clean up the broken chunk_151+chunk_152 indentation + insert chunk_153.

Per the subagent-driven-development SKILL pitfall (sitemap.xml patch-then-indent-fix
DOUBLE-BREAK, atlas-store ticks 101+157), the proper recipe is:
  (a) Inspect git show HEAD~1:sitemap.xml as ground truth
  (b) Run ET.fromstring() to confirm current parse state
  (c) Replace ALL damaged blocks in ONE pass via str.replace
  (d) Verify with ET.fromstring() + balanced <url> tag counts
  (e) Commit as SEPARATE followup commit

Here we have TWO damaged blocks (chunk_151 over-indented 6-space, chunk_152 also over-indented)
plus an orphan <url> opener from chunk_151. Plus our new chunk_153 inserted under the orphan.
The fix: rewrite the entire bottom of the file cleanly with chunk_150's known-good 2-space indent.
"""
import re
import subprocess
from pathlib import Path
import xml.etree.ElementTree as ET

REPO = Path("C:/Users/Potts/projects/atlas-store")
SITEMAP = REPO / "sitemap.xml"

# 1. Get current state
text = SITEMAP.read_text(encoding="utf-8")
opens_before = len(re.findall(r"<url>", text))
closes_before = len(re.findall(r"</url>", text))
print(f"BEFORE repair: opens={opens_before}, closes={closes_before}")

try:
    ET.fromstring(text)
    print("BEFORE repair: ET.fromstring OK (parser is forgiving about orphan opener)")
except ET.ParseError as e:
    print(f"BEFORE repair: ET.fromstring FAIL: {e}")

# 2. Identify the broken tail (everything from chunk_150 onward)
#    chunk_150 at offset 1299 is the last clean entry; everything after is the broken zone.
tail_start_marker = "  <url>\n    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_150.html</loc>\n    <lastmod>2026-07-16</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>"
if tail_start_marker not in text:
    # Fall back: find chunk_150 <loc> position
    m = re.search(r'<loc>https://talonforgehq\.github\.io/atlas-store/chunks/chunk_150\.html</loc>', text)
    if not m:
        raise RuntimeError("can't find chunk_150 anchor in sitemap.xml")
    # Walk backward to the <url> opener before this <loc>
    opener_pos = text.rfind("<url>", 0, m.start())
    if opener_pos < 0:
        raise RuntimeError("can't find chunk_150 <url> opener")
    # Capture the entire <url>...</url> block
    closer_pos = text.find("</url>", m.start())
    if closer_pos < 0:
        raise RuntimeError("can't find chunk_150 </url> closer")
    closer_end = closer_pos + len("</url>") + 1  # +1 for newline
    tail_start_marker = text[opener_pos:closer_end]
    print(f"Fallback: chunk_150 block found at offset {opener_pos}, length {len(tail_start_marker)}")

# 3. Build the clean replacement tail: keep chunk_150 (clean) + add chunk_151 + chunk_152 + chunk_153
clean_tail = tail_start_marker + "\n  <url>\n    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_151.html</loc>\n    <lastmod>2026-07-16</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n  <url>\n    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_152.html</loc>\n    <lastmod>2026-07-16</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n  <url>\n    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_153.html</loc>\n    <lastmod>2026-07-16</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n</urlset>\n"

# Replace the damaged tail with clean_tail
text_new = text[: text.find(tail_start_marker)] + clean_tail

# 4. Validate
opens_after = len(re.findall(r"<url>", text_new))
closes_after = len(re.findall(r"</url>", text_new))
print(f"AFTER repair: opens={opens_after}, closes={closes_after}, balanced={opens_after==closes_after}")
assert opens_after == closes_after, f"<url> tags unbalanced: {opens_after} open vs {closes_after} close"

try:
    ET.fromstring(text_new)
    print("AFTER repair: ET.fromstring() OK")
except ET.ParseError as e:
    print(f"AFTER repair: ET.fromstring() FAIL: {e}")
    raise

# 5. Write back
SITEMAP.write_text(text_new, encoding="utf-8")
print(f"Wrote {len(text_new)} bytes to sitemap.xml")

# 6. Final verification — read back from disk
text_disk = SITEMAP.read_text(encoding="utf-8")
assert "<loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_153.html</loc>" in text_disk
assert "<loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_152.html</loc>" in text_disk
assert "<loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_151.html</loc>" in text_disk
print("All 3 chunk entries (151, 152, 153) present and well-formed")
print(f"Total <url> entries: {opens_after}")