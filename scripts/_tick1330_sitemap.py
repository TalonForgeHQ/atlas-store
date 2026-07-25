"""Tick 1330 — append chunk-1327 and chunk-1329 to sitemap.xml so both new cards have SEO entries."""
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the </urlset> close tag and insert before it
close_tag = '</urlset>'
pos = content.rfind(close_tag)
if pos == -1:
    raise SystemExit('NO_URLSET_FOUND')

insertions = (
    '<url><loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_1327.html</loc>'
    '<lastmod>2026-07-26</lastmod><changefreq>weekly</changefreq><priority>0.85</priority></url>'
    '<url><loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_1329.html</loc>'
    '<lastmod>2026-07-26</lastmod><changefreq>weekly</changefreq><priority>0.85</priority></url>'
)

new_content = content[:pos] + insertions + content[pos:]
with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('OK sitemap.xml updated; new size:', len(new_content))