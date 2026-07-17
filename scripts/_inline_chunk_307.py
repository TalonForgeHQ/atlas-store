#!/usr/bin/env python3
"""Insert chunk-307 summary card into index.html before </html>.

Uses rfind('</html>') unique anchor (only one closing tag in a well-formed doc).
"""
from pathlib import Path

INDEX = Path(r"C:\Users\Potts\projects\atlas-store\index.html")

new_card = """<section id="chunk-307" class="seo-chunk" data-vertical="ai_research" data-lead="487" data-tick="2026-07-17-fast-exec-usertesting-487" data-cohort="usertesting-thoma-bravo-human-insight-biometric-eu-ai-act-art-53">
<article>
<h2>UserTesting Human Insight Platform and Contributor-Biometric Audit 2026</h2>
<p>Buyer checklist for UserTesting contributor-consent lineage, biometric-data capture (video + screen + facial-expression + voice), EnjoyHQ AI-summary citation grounding, UserZoom quantitative-methods audit, User Interviews 1.4M-panel consent lineage, cross-tenant recording + AI-summary isolation (SOC 2 CC6.1 + GDPR Art. 28 + Schrems II), deletion propagation across all 4 UserTesting products, and Thoma Bravo portfolio cross-product cost-attribution join-table (Calabrio + ConnectWise + NextGen + SolarWinds + Sophos + Barracuda) under EU AI Act Art. 12/14/50/53 evidence + 12-state biometric-privacy-consent (BIPA + Illinois AI Video Interview Act + CA SB 1001 + CO SB 24-205 + TX + NY + 7 others) + Aug 2 2026 GPAI enforcement. <a href="chunks/chunk_307.html">Read the full chunk 307 audit lane.</a></p>
</article>
</section>
"""

text = INDEX.read_text(encoding="utf-8")
anchor = text.rfind("</html>")
assert anchor > 0, "no </html> found"

# Parse-back: verify chunk-306 still present and chunk-307 not yet present
assert 'id="chunk-306"' in text, "chunk-306 missing"
assert 'id="chunk-307"' not in text, "chunk-307 already present"

new_text = text[:anchor] + new_card + text[anchor:]

# Double-check no duplicate wrapper count
assert new_text.count('id="chunk-307"') == 1, "chunk-307 dup"

# Balanced structural check
assert new_text.count("<section id=\"chunk-307\"") == 1
assert new_text.count("</section>\n</html>") >= 1, "no closing structure"

INDEX.write_text(new_text, encoding="utf-8")
print(f"[OK] chunk-307 inserted at byte offset {anchor}")
print(f"[OK] index.html now {len(new_text)} bytes (was {len(text)}; +{len(new_text)-len(text)} expected)")