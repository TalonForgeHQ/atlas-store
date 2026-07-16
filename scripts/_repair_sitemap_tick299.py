"""Repair the sitemap.xml indent: chunk_166 + chunk_167 blocks have 6-space indent instead of 4-space."""
from pathlib import Path
import re

SITEMAP = Path(r"C:\Users\Potts\projects\atlas-store\sitemap.xml")

text = SITEMAP.read_text(encoding="utf-8")

# Both chunk_166 and chunk_167 blocks need re-indent. Find the damaged region
# (everything from "chunk_166.html</loc>" through the end)
idx_start = text.rfind('chunk_166.html</loc>')
assert idx_start != -1, "chunk_166 marker not found"

old_block = text[idx_start:]
print("--- BEFORE ---")
print(repr(old_block[:500]))

# Normalize: 8 spaces -> 4 spaces (since the lines start with 8 spaces of leading whitespace
# in the over-indented case; the new lines are also over-indented at 6 spaces from old)
# Looking at the actual content: each damaged inner line has 8 leading spaces.
# But the broken patch produced 8 spaces (4+4) because the existing pattern was 4-space.
# We need to normalize back to 4-space indent for inner tags.

# Strategy: take the broken tail, replace 8 leading spaces with 4 (for the chunk_166 block
# inner lines that were incorrectly re-indented), then verify chunk_167 (which is correctly
# 8-space but consistent with the surrounding — no wait, chunk_167 should also be 4-space).

# Actually let's look again - looking at output: chunk_166 inner is 8-space, chunk_167 inner is 8-space.
# Looking at the diff more carefully, the patch added 2 extra leading spaces to chunk_166's inner
# (4 -> 6 -> 8?). Let me just normalize: find each line in the tail that starts with 8+ spaces
# and contains "<lastmod>", "<changefreq>", "<priority>", "<loc>" -- re-indent to 4 spaces.

new_lines = []
for line in old_block.split('\n'):
    # If line is whitespace + inner tag content, normalize to 4-space indent
    stripped = line.lstrip()
    if stripped.startswith(('<lastmod>', '<changefreq>', '<priority>', '<loc>https://talonforgehq.github.io/atlas-store/chunks/')):
        new_lines.append('    ' + stripped)
    elif stripped.startswith('<url>') or stripped.startswith('</url>'):
        new_lines.append('  ' + stripped)
    elif stripped.startswith('</urlset>'):
        new_lines.append(stripped)
    else:
        new_lines.append(line)

new_block = '\n'.join(new_lines)

print("\n--- AFTER ---")
print(new_block[:600])

text = text[:idx_start] + new_block

# Verify XML parses
import xml.etree.ElementTree as ET
try:
    ET.fromstring(text)
    print('\nXML parse OK')
except ET.ParseError as e:
    print(f'\nXML parse FAIL: {e}')
    raise

# Verify balanced tag counts
assert len(re.findall(r"<url>", text)) == len(re.findall(r"</url>", text)), "unbalanced <url>"
print(f"Balanced <url>={len(re.findall(r'<url>', text))} </url>={len(re.findall(r'</url>', text))}")

SITEMAP.write_text(text, encoding="utf-8")
print("OK: sitemap.xml repaired + written")