"""Sitemap <url> insert for Patreon 512 / chunk_330.

Pattern verified live atlas-store tick 498 (Securiti): use Python str.replace
on the exact prior-sibling block + new sibling block, NOT patch tool (patch
over-indents children of inserted blocks per pitfall #61). Canonical
indentation in this repo is 4-space outer + 6-space children (verified
git show HEAD:sitemap.xml: 223/223 url tags at 4-space, the corrupted
siblings are at 0/6/8/12-space).

Also repairs the corrupted chunk_327 + chunk_329 <url> blocks (verified
live 2026-07-18 in tick 513: chunk_327 had 0/4-space outer, chunk_329 had
6/8-space outer — both artifacts of pitfall #61 'patch on multi-block
sibling').

Idempotency guard: assert the new anchor is NOT already present, halt if so.
"""
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
SITEMAP = REPO / "sitemap.xml"
CHUNK_FILE = "chunk_330.html"
TICK_ID = "2026-07-18-fast-exec-patreon-512"

# Canonical 4/6-space block
NEW_BLOCK_330 = (
    "    <url>\n"
    "      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_330.html</loc>\n"
    "      <lastmod>2026-07-18</lastmod>\n"
    "      <changefreq>monthly</changefreq>\n"
    "      <priority>0.8</priority>\n"
    "    </url>\n"
)

# Corrupted chunk_327 block (0/4-space mix — missing outer indent on <url>)
CORRUPT_327 = (
    "<url>\n"
    "    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_327.html</loc>\n"
    "        <lastmod>2026-07-18</lastmod>\n"
    "        <changefreq>monthly</changefreq>\n"
    "        <priority>0.8</priority>\n"
    "      </url>\n"
)
FIXED_327 = (
    "    <url>\n"
    "      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_327.html</loc>\n"
    "      <lastmod>2026-07-18</lastmod>\n"
    "      <changefreq>monthly</changefreq>\n"
    "      <priority>0.8</priority>\n"
    "    </url>\n"
)

# Corrupted chunk_329 block (6/8-space — over-indented)
CORRUPT_329 = (
    "      <url>\n"
    "        <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_329.html</loc>\n"
    "        <lastmod>2026-07-18</lastmod>\n"
    "        <changefreq>monthly</changefreq>\n"
    "        <priority>0.8</priority>\n"
    "      </url>\n"
)
FIXED_329 = (
    "    <url>\n"
    "      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_329.html</loc>\n"
    "      <lastmod>2026-07-18</lastmod>\n"
    "      <changefreq>monthly</changefreq>\n"
    "      <priority>0.8</priority>\n"
    "    </url>\n"
)

text = SITEMAP.read_text(encoding="utf-8")

# Idempotency guards
assert text.count(f"chunks/{CHUNK_FILE}") == 0, (
    f"FAIL: {CHUNK_FILE} already in sitemap — aborting"
)

# Repair chunk_327 first (corrupt -> fixed)
assert text.count(CORRUPT_327) == 1, f"FAIL: chunk_327 corrupt anchor count={text.count(CORRUPT_327)}"
text = text.replace(CORRUPT_327, FIXED_327, 1)
assert text.count(CORRUPT_327) == 0, "FAIL: chunk_327 repair did not fully apply"

# Repair chunk_329 (corrupt -> fixed)
assert text.count(CORRUPT_329) == 1, f"FAIL: chunk_329 corrupt anchor count={text.count(CORRUPT_329)}"
text = text.replace(CORRUPT_329, FIXED_329, 1)
assert text.count(CORRUPT_329) == 0, "FAIL: chunk_329 repair did not fully apply"

# Insert chunk_330 immediately after fixed chunk_329 block
assert text.count(FIXED_329) == 1, "FAIL: fixed chunk_329 anchor not found"
text = text.replace(FIXED_329, FIXED_329 + NEW_BLOCK_330, 1)

# Verify result
assert text.count(f"chunks/{CHUNK_FILE}") == 1, "FAIL: new block did not land"
assert text.count("<url>") == text.count("</url>"), "FAIL: unbalanced url tags"

# Verify no remaining corrupted siblings
assert CORRUPT_327 not in text, "FAIL: chunk_327 corruption still present"
assert CORRUPT_329 not in text, "FAIL: chunk_329 corruption still present"

# Verify the new chunk_330 block specifically is at the canonical 4-space indent
new_block_lines = NEW_BLOCK_330.splitlines()
start_idx = None
for i, line in enumerate(text.splitlines()):
    if "chunk_330" in line:
        start_idx = i
        break
assert start_idx is not None, "FAIL: chunk_330 not found in text"
window = text.splitlines()[start_idx - 1 : start_idx + 5]
for expected, actual in zip(new_block_lines, window):
    assert actual == expected, f"FAIL: chunk_330 indent mismatch: expected {expected!r}, got {actual!r}"

SITEMAP.write_text(text, encoding="utf-8")
print(f"OK: sitemap.xml updated")
print(f"   chunk_327 repaired (0/4-space -> 4/6-space)")
print(f"   chunk_329 repaired (6/8-space -> 4/6-space)")
print(f"   chunk_330 inserted at canonical indent")
print(f"   <url> tags: {text.count('<url>')} | </url> tags: {text.count('</url>')}")
print(f"   tick_id={TICK_ID}")
