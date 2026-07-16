#!/usr/bin/env python3
"""Repair sitemap.xml: normalize the trailing block after patch over-indented."""
from pathlib import Path
p = Path("C:/Users/Potts/projects/atlas-store/sitemap.xml")
text = p.read_text(encoding="utf-8")

# Locate the prior chunk_239 sibling block and replace the entire damaged tail
# with a canonical 6-space-indent <url> block + 4-space-indent </urlset>
needle = '<url>\n        <loc>https://talonforgehq.github.io/atlas-store/chunks/confident_ai_deepeval_audit_observability.html</loc>\n        <lastmod>2026-07-17</lastmod>\n      </url>'
canonical_tail = '''<url>
        <loc>https://talonforgehq.github.io/atlas-store/chunks/confident_ai_deepeval_audit_observability.html</loc>
        <lastmod>2026-07-17</lastmod>
      </url>
      <url>
        <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_239.html</loc>
        <lastmod>2026-07-17</lastmod>
      </url>
      <url>
        <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_240.html</loc>
        <lastmod>2026-07-17</lastmod>
      </url>
    </urlset>'''

idx = text.find(needle)
assert idx > -1, "needle (confident_ai_deepeval) not found"
# Locate the </urlset> after the needle
end_idx = text.find("</urlset>", idx)
assert end_idx > -1, "no </urlset> after needle"
end_idx_full = end_idx + len("</urlset>")
new_text = text[:idx] + canonical_tail
p.write_text(new_text, encoding="utf-8")
print("sitemap.xml repaired")

# Verify
import re
import xml.etree.ElementTree as ET
final = p.read_text(encoding="utf-8")
print("len after:", len(final))
print("<url> count:", len(re.findall(r"<url>", final)))
print("</url> count:", len(re.findall(r"</url>", final)))
ET.fromstring(final)
print("PARSE OK")

# Verify chunk_240 is present
assert "chunk_240.html" in final, "chunk_240 missing"
print("chunk_240 confirmed in sitemap")