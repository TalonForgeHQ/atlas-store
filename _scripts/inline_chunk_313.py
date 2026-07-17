import re
import os

REPO = r"C:/Users/Potts/projects/atlas-store"
INDEX = r"C:/Users/Potts/projects/atlas-store/index.html"

with open(INDEX, "r", encoding="utf-8") as f:
    text = f.read()

# baseline
baseline_size = len(text)
baseline_chunk_312 = text.count('id="chunk-312"')
baseline_chunk_313 = text.count('id="chunk-313"')
print(f"baseline size: {baseline_size}")
print(f"baseline chunk-312 count: {baseline_chunk_312}")
print(f"baseline chunk-313 count: {baseline_chunk_313}")

assert baseline_chunk_312 == 1, "expected chunk-312 to exist exactly once"
assert baseline_chunk_313 == 0, "chunk-313 should not exist before insert"

# Summary card for chunk 313 (1-paragraph teaser card shape)
new_card = '''
<!-- chunk_313.html — Agiloft AI-CLM Audit 2026 -->
<article id="chunk-313" data-vertical="ai_contract_intelligence" data-lead="492" data-tick="2026-07-17-fast-exec-agiloft-492" data-cohort="agiloft-kkr-acquired-clm-ai-clm-30-year-bootstrapped-per-clause-lineage-eu-ai-act-art-53-gpai">
  <h2>Agiloft AI-CLM Audit 2026 — Per-Clause + AI-Tagging Lineage, EU AI Act Aug 2 2026 GPAI Documentation, KKR-Scale Evidence Pack</h2>
  <p class="meta">Atlas @ Talon Forge · ai_contract_intelligence cohort sibling #3 (after LinkSquares 490 + ContractWorks 491) · 13-col provenance row · 5 audit gaps · 5+ vendors + 2+ founders cross-walked · <strong>$500 / 48-hour audit</strong> + <strong>$497 / month retainer</strong></p>
  <h3>What this audit covers</h3>
  <p>Agiloft is the 30-year-bootstrapped enterprise-CLM that became a KKR majority-stake platform (May 2024, FTV Capital + JMI Equity follow-on) — the canonical "no-CLM-team-can-afford-to-miss" lane for AI-CLM buyers. This audit delivers the <strong>13-col minimum-provenance-row schema</strong> that maps every Agiloft AI-tagging + AI-clause-extraction + AI-obligation-extraction event to its per-contract source, per-tenant boundary, per-KKR-platform-event, per-FTV-portfolio-event, per-procurement-vendor-DD event, and per-residency-region. Cohort sibling #3 to LinkSquares 490 + ContractWorks 491. Cohort comparison refresh of how each AI-CLM vendor documents the 13-col provenance join-table comes with the audit. <a href="chunks/chunk_313.html">Read the full chunk 313 audit lane.</a></p>
</article>
'''

# anchor on rfind("</html>")
end_html_pos = text.rfind("</html>")
assert end_html_pos != -1, "could not find </html> in index.html"

# insert new card immediately before </html>
new_text = text[:end_html_pos] + new_card + text[end_html_pos:]

# write
with open(INDEX, "w", encoding="utf-8") as f:
    f.write(new_text)

# verify
with open(INDEX, "r", encoding="utf-8") as f:
    text2 = f.read()

# assertions
assert len(text2) == baseline_size + len(new_card), f"size mismatch: {len(text2)} vs expected {baseline_size + len(new_card)}"
assert text2.count('id="chunk-313"') == 1, "chunk-313 not inserted exactly once"
assert text2.count('id="chunk-312"') == 1, "chunk-312 should still be present"
assert text2.endswith("</html>"), "index.html should still end with </html>"
assert "data-tick=\"2026-07-17-fast-exec-agiloft-492\"" in text2, "tick attribute missing"
assert text2.count('<div class="tick-entry"') == 0, "index.html is summary card area, not build-log"

# new card wrapper count
new_card_wrapper = new_card.count('<article id="chunk-313"')
assert new_card_wrapper == 1, f"new card wrapper count != 1: {new_card_wrapper}"

# placeholder anchor count check
anchors = ["chunk_313.html", "13-col", "KKR"]
for a in anchors:
    cnt = text2.count(a)
    print(f"  anchor '{a}' count: {cnt}")
    assert cnt >= 1, f"anchor '{a}' missing from index.html"

print(f"OK — chunk-313 inlined into index.html. New size: {len(text2)} (delta: +{len(text2) - baseline_size})")
