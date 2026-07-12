from pathlib import Path

path = Path("C:/Users/Potts/projects/atlas-store/sitemap.xml")
text = path.read_text(encoding="utf-8")

# Bad block (over-indented chunk_106 + new chunk_107)
BAD = """                                    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_106.html</loc>
                                    <lastmod>2026-07-12</lastmod>
                                    <changefreq>monthly</changefreq>
                                    <priority>0.8</priority>
                                </url>
                                <url>
                                    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_107.html</loc>
                                    <lastmod>2026-07-12</lastmod>
                                    <changefreq>monthly</changefreq>
                                    <priority>0.8</priority>
                                </url>
                            </urlset>"""

# Good block (proper 20-space indent matching chunk_105)
GOOD = """                    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_106.html</loc>
                    <lastmod>2026-07-12</lastmod>
                    <changefreq>monthly</changefreq>
                    <priority>0.8</priority>
                </url>
                <url>
                    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_107.html</loc>
                    <lastmod>2026-07-12</lastmod>
                    <changefreq>monthly</changefreq>
                    <priority>0.8</priority>
                </url>
            </urlset>"""

assert BAD in text, "BAD block not found in sitemap.xml"
text = text.replace(BAD, GOOD)
path.write_text(text, encoding="utf-8")
print("OK: sitemap.xml indentation fixed")

# Verify
lines = path.read_text(encoding="utf-8").splitlines()
url_locs = [(i, l) for i, l in enumerate(lines) if "<loc>" in l and "chunk_10" in l]
for i, l in url_locs:
    # find leading spaces
    indent = len(l) - len(l.lstrip())
    print(f"  line {i}: indent={indent} | {l.strip()[:60]}")
# All chunk_10x blocks should be same indent
indents = set(indent for i, (indent, l) in enumerate(url_locs))
assert len(indents) == 1, f"Mixed indents: {indents}"
print(f"OK: all chunk_10x <loc> lines at indent={indents.pop()}")