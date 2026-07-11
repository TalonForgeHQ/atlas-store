"""Tick 66: Inline the chunk_65.html content into index.html right after the Clearbrief section.

Pattern: read chunk_65.html, strip the <html>/<head>/<body>/<article>/<h1> wrapper but
keep the inner sections. Find the closing </section> of the Clearbrief chunk, insert
the new chunk_65 content there.

Actually simpler: read chunk_65 content, replace <article>...</article> content directly,
then splice into index.html between the Clearbrief closing </section> and the next section.
"""
import os
import re

INDEX_PATH = r"C:\Users\Potts\projects\atlas-store\index.html"
CHUNK_PATH = r"C:\Users\Potts\projects\atlas-store\_chunks\chunk_65.html"

# Read chunk_65 content
with open(CHUNK_PATH, "r", encoding="utf-8") as f:
    chunk = f.read()

# Extract just the inner content (everything inside <article>...</article>)
# We want: <h1> + all <section>s + closing </article>
# Pattern: find <article ...> ... </article>
m = re.search(r'<article[^>]*>(.*?)</article>', chunk, re.DOTALL)
if not m:
    print("ABORT: no <article> block found in chunk_65.html")
    raise SystemExit(1)
inner = m.group(1)

# Now we need to wrap this into a <section class="seo-chunk" id="..."> with the
# closing marker comment, matching the index.html pattern.
NEW_SECTION_ID = "traceloop-opentelemetry-llm-observability-audit-checklist-2026"
HEADER_COMMENT = '</section><!-- chunk_65.html \u2014 Traceloop OpenTelemetry-Native LLM Observability + Apache-2.0 OpenLLMetry + On-Prem/Air-Gapped + SOC 2 + EU AI Act + HIPAA + ISO 42001 Audit Checklist 2026 -->'
NEW_SECTION = (
    HEADER_COMMENT
    + '\n  <section class="seo-chunk" id="' + NEW_SECTION_ID + '">\n    '
    + inner.strip()
    + '\n  </section><!-- /chunk_65.html -->'
)

# Now find the Clearbrief closing marker in index.html and insert after it
# The closing marker for chunk_64 (Clearbrief) ends with the comment, then next chunk begins.
# Strategy: find the Clearbrief section by id, then find the closing </section> + comment,
# then insert NEW_SECTION right after.

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    idx_content = f.read()

# Find the position right after </section><!-- /chunk_64.html --> would be ideal,
# but the Clearbrief section ends with </section> followed by some closing for index.html
# Let's find the END of the Clearbrief section by searching for the section id
# and tracking nesting.
cb_section_start = idx_content.find('<section class="seo-chunk" id="clearbrief-ai-citation-verification-rule-26-rule-11-soc2-eu-ai-act-aba-rule-1-1-audit-2026">')
if cb_section_start < 0:
    print("ABORT: Clearbrief section not found in index.html")
    raise SystemExit(1)

# Walk forward, counting <section / </section> to find the matching closing
pos = cb_section_start
depth = 0
end_pos = -1
while pos < len(idx_content):
    next_open = idx_content.find('<section', pos + 1)
    next_close = idx_content.find('</section>', pos + 1)
    if next_close < 0:
        break
    if 0 <= next_open < next_close:
        depth += 1
        pos = next_open
    else:
        if depth == 0:
            end_pos = next_close + len('</section>')
            break
        depth -= 1
        pos = next_close

if end_pos < 0:
    print("ABORT: could not find closing </section> of Clearbrief section")
    raise SystemExit(1)

# Insert NEW_SECTION right after the Clearbrief closing
new_index = idx_content[:end_pos] + "\n\n  " + NEW_SECTION + idx_content[end_pos:]

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(new_index)

# Verify
with open(INDEX_PATH, "r", encoding="utf-8") as f:
    final = f.read()

print(f"index.html size: {len(idx_content)} -> {len(new_index)} bytes")
print(f"chunk_65 marker present: {final.count('chunk_65.html') >= 1}")
print(f"Traceloop h1 present: {'Traceloop OpenTelemetry-Native LLM Observability' in final}")
print(f"Section id present: {NEW_SECTION_ID in final}")
print(f"Total seo-chunk sections: {final.count('class=\"seo-chunk\"')}")
