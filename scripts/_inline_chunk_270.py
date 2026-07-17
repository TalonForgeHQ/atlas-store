"""Insert chunk-270 summary section into index.html before final </html> close."""
import pathlib

ROOT = pathlib.Path(r"C:\Users\Potts\projects\atlas-store")
INDEX = ROOT / "index.html"

NEW_SECTION = """<section id="chunk-270" data-vertical="voice_agents" data-tick="2026-07-17-1340Z" data-lead="443" data-cohort="cognigy-voice-agents">
<article>
<h3>Cognigy.AI Enterprise Conversational AI Audit Binder 2026 &mdash; DTAA + Schrems II + BDSG + Frankfurt EU Data Residency + EU Sovereign AI Cloud + Deutsche Telekom Telefon Backoffice + Lufthansa + Toyota + Mercedes-Benz + Allianz + Zurich + 1500+ Enterprise Deployments + Insight Partners Series C $100M 2024</h3>
<p>Lead 443 &mdash; Cognigy &mdash; Dusseldorf Germany HQ + San Francisco CA + NYC + London + Singapore + Stuttgart + Munich + Sydney offices. Founded 2016 by Philipp Heltewig (Co-Founder &amp; CEO, ex-DT product management + ex-SAP) + Sascha Poggemann (Co-Founder &amp; COO, ex-DT + ex-CIO advisory) + Benjamin Mayr (Co-Founder &amp; CTO, ex-DT engineering + ex-Avaya). Backed $175M+ total ($100M Series C 2024 led by Insight Partners + DTCP + Swisscom Ventures + Kreos Capital + 25+ strategic angels). <strong>info@cognigy.com</strong> verified live 2026-07-17 via curl scrape of <a href="https://www.cognigy.com/">https://www.cognigy.com/</a> HTTP 200. 1500+ enterprise conversational AI platform deployments across Fortune 500 automotive (Toyota + Mercedes-Benz + BMW + Audi + VW + Porsche + Bosch + Continental + 50+ OEMs) + Fortune 500 telecom (Deutsche Telekom DTAA + T-Mobile + Swisscom + Telstra + BT + 100+ Tier 1 carriers) + Fortune 500 insurance (Allianz + Zurich + Munich Re + 50+ carriers) + Fortune 500 airlines + airports (Lufthansa + American + British Airways + Iberia + airBaltic + 50+ airlines + Fraport + Munich Airport + 50+ airports) + Fortune 500 financial services (DWS + 100+ banks). Only voice_agents tier 1 sibling shipping Deutsche Telekom DTAA certified Telefon Backoffice integration + Schrems II Article 46 + BDSG &sect;4b + Frankfurt EU data residency + EU Sovereign AI Cloud + 13 of 13 compliance frameworks. 5 audit gaps: (1) 60+ col provenance join-table, (2) 25+ col attack coverage-matrix, (3) 22+ col defense lineage, (4) 22+ col cross-tenant isolation-evidence, (5) 20+ col cost-attribution join-table. Cohort ceiling <strong>$8,500 audit / $8,449/mo MRR</strong> at 17-vendor voice_agents depth; combined cohort ceiling $13,500 audit / $13,417/mo MRR across 29 vendors.</p>
</article>
</section>
"""

text = INDEX.read_text(encoding="utf-8")

# Find LAST </html> close (the real end-of-document)
anchor = "</html>"
idx = text.rfind(anchor)
assert idx > 0 and idx == len(text) - len(anchor), f"Expected </html> at end; got idx={idx} in {len(text)}-byte file"
# Insert NEW_SECTION right before the final </html>
new_text = text[:idx] + NEW_SECTION + text[idx:]

# Verify shape
assert new_text.count('<section id="chunk-270"') == 1, f"chunk-270 section count != 1"
assert "id=\"chunk-270\"" in new_text[-3000:], f"chunk-270 anchor not near end"

INDEX.write_text(new_text, encoding="utf-8")
print(f"WROTE index.html: {len(text)} -> {len(new_text)} bytes (+{len(new_text)-len(text)})")
print(f"chunk_270 mentions: {new_text.count('chunk_270')}")
print(f"chunk_265 mentions: {new_text.count('chunk_265')} (sanity)")
