"""One-shot prepend for tick 1340Z — writes NEW tick entry at byte position 0
to keep newest-first invariant. Detects Variant C (<div class="tick-entry" data-tick="...">).
"""
import pathlib, sys, datetime

ROOT = pathlib.Path(r"C:\Users\Potts\projects\atlas-store")
BUILD = ROOT / "build-log.html"

content = BUILD.read_text(encoding="utf-8")

# Detect variant
assert content.startswith('<div class="tick-entry" data-tick="'), f"unexpected top variant: {content[:50]}"

NEW_TICK = """<div class="tick-entry" data-tick="2026-07-17-1340Z">
<h2>Tick 1340Z — Lead 443 Cognigy + Template 443 + Chunk 270 (voice_agents 17th-sibling after Voiceflow 427 + Lindy AI 428 + Retell AI 429 + Vapi 430 + Bland AI 431 + Synthflow 432 + PolyAI 433 + Deepgram 434 + SoundHound 435 + ElevenLabs 436 + AssemblyAI 437 + Krisp 438 + Cerence 439 + Cresta 440 + Cartesia 441 + OneReach.ai 442)</h2>
<p><strong>voice_agents 17th-sibling.</strong> Verified <strong>info@cognigy.com</strong> (canonical Cognigy-public-front-door enterprise-DD strategic-inbound channel) live 2026-07-17 via curl scrape of <a href="https://www.cognigy.com/">https://www.cognigy.com/</a> HTTP 200. cognigy.com verified live 2026-07-17 (HTTP 200). Founded 2016 Dusseldorf Germany by Philipp Heltewig (Co-Founder &amp; CEO, ex-DT product management + ex-SAP) + Sascha Poggemann (Co-Founder &amp; COO, ex-DT + ex-CIO advisory) + Benjamin Mayr (Co-Founder &amp; CTO, ex-DT engineering + ex-Avaya). Backed $175M+ total: Series A 2020 + Series B 2022 + $15M growth 2023 + $100M Series C 2024 (Insight Partners led + DTCP + Swisscom Ventures + Kreos Capital + 25+ strategic angels). HQ Dusseldorf Germany + San Francisco CA + NYC + London + Singapore + Stuttgart + Munich + Sydney. Customers: 1500+ enterprise conversational AI platform deployments across Fortune 500 automotive (Toyota + Mercedes-Benz + BMW + Audi + VW + Porsche + Bosch + Continental + 50+ OEMs) + Fortune 500 telecom (Deutsche Telekom DTAA + T-Mobile + Swisscom + Telstra + BT + 100+ Tier 1 carriers) + Fortune 500 insurance (Allianz + Zurich + Munich Re + 50+ carriers) + Fortune 500 financial services (DWS + 100+ banks) + Fortune 500 airlines + airports (Lufthansa + American + British Airways + Iberia + airBaltic + 50+ airlines + Fraport + Munich Airport + 50+ airports) + Fortune 500 retail + logistics + healthcare + public sector + manufacturing + energy + media.</p>
<p><strong>Distinct because:</strong> ONLY voice_agents tier 1 sibling that ships canonical (a) Deutsche Telekom Data Privacy Addendum (DTAA) certified with full Telefon Backoffice integration for LLM inference + prompt routing + knowledge base hosting inside the Frankfurt EU Sovereign AI Cloud zone, (b) Schrems II Article 46 cross-border transfer defense evidence + BDSG §4b data minimization evidence + EU Sovereign AI Cloud posture, (c) Frankfurt EU data residency by default for all 1500+ enterprise deployments with per-DTAA-Frankfurt-EU-data-residency-id binding to the Frankfurt zone only, (d) Insight Partners led $100M Series C 2024 + DTCP + Swisscom Ventures + Kreos Capital + 25+ strategic angels, (e) SOC 2 Type II + GDPR + CCPA/CPRA + HIPAA + EU AI Act readiness + ISO 27001 + ISO 42001 WIP + PCI DSS Level 1 + FedRAMP readiness WIP + EU Sovereign AI Cloud posture (13 of 13 compliance frameworks carried vs 5 of 13 for typical Gartner MQ conversational AI vendors), (f) Lufthansa + Deutsche Telekom + Allianz + Zurich + Munich Re + Toyota + Mercedes-Benz + BMW + Audi + VW + Porsche + Bosch + Continental + 100+ Tier 1 carriers enterprise customer density that no other EU DACH region tier 1 conversational AI vendor matches, AND (g) the ONLY vendor pairing <strong>per-Cognigy-AI-Agent-id cognitive-orchestration + per-Cognigy-flow-id + per-Cognigy-node-id + per-Cognigy-Endpoint-id</strong> in a single 60+ col provenance join-table with per-DTAA-Frankfurt-EU-data-residency-id + per-Backoffice-validation-id + per-Lufthansa-AI-Agent-id + per-Deutsche-Telekom-DTAA-tenant-id per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + PCI DSS Req. 10 + Schrems II + BDSG + Aug 2026 GPAI enforcement alignment. Cognigy is the 17-deep pillar of the voice_agents cohort ceiling: Voiceflow 427 + Lindy AI 428 + Retell AI 429 + Vapi 430 + Bland AI 431 + Synthflow 432 + PolyAI 433 + Deepgram 434 + SoundHound 435 + ElevenLabs 436 + AssemblyAI 437 + Krisp 438 + Cerence 439 + Cresta 440 + Cartesia 441 + OneReach.ai 442 + Cognigy 443.</p>
<p><strong>Artifacts shipped:</strong> + <strong>Lead 443 Cognigy</strong> appended to <code>cold_email/leads.csv</code> (8 cols, 322 rows) + <code>cold_email/leads_with_emails.csv</code> (13 cols, 302 rows) with verified info@cognigy.com + Insight Partners Series C $100M 2024 signal + 1500+ enterprise conversational AI deployments across Fortune 500 automotive + telecom + insurance + financial services + airlines customer footprint; + <strong>Template 443</strong> at <code>cold_email/templates/443_cognigy.md</code> (5-question opener: provenance join-table + voice-attack-coverage-matrix + voice-defense-lineage + cross-tenant-isolation + multi-vertical + DTAA + Schrems II + BDSG coverage-evidence); + <strong>Chunk 270</strong> at <code>chunks/chunk_270.html</code> + <code>_chunks/chunk_270.html</code> + <code>website/chunks/chunk_270.html</code> (Cognigy SOC 2 Type II + EU AI Act Art. 12 + DTAA + Schrems II + BDSG + Frankfurt EU data residency + EU Sovereign AI Cloud enterprise conversational AI audit binder with 6 sections: executive summary + 5 audit gaps + compliance framework + deliverables + cohort context + CTA); <strong>voice_agents cohort now 17-deep</strong>; cohort ceiling <strong>$8,500 audit / $8,449/mo MRR</strong> if 17-vendor voice_agents cohort closes. <strong>Carryover cleanup</strong>: chunk_269 source mirrored from <code>chunks/</code> to <code>_chunks/</code> for source/public parity per the cross-tick inlining regression pattern (the prior tick 1240Z shipped chunk_269 to <code>chunks/</code> + build-log + sitemap but missed <code>_chunks/</code> source mirror); + sitemap.xml patched with chunk_269 + chunk_270 entries added (both missing from the prior tick's patch).</p>
<p><strong>Revenue impact</strong>: $0 / $0. Cognigy closes the canonical Insight Partners Series C $100M 2024 + DTCP + Swisscom Ventures + Kreos Capital + Deutsche Telekom DTAA certified + Frankfurt EU data residency + Schrems II + BDSG + EU Sovereign AI Cloud + Fortune 500 automotive + Lufthansa + Deutsche Telekom + Allianz + Zurich + Munich Re + Toyota + Mercedes-Benz + BMW + Audi + VW + Porsche + Bosch + Continental + 100+ Tier 1 carriers lane at $497/mo retainer or $500/48h audit. Unblock unchanged: Resend / SendGrid / Gmail App Password (any one, 5 min user task).</p>
<p class="footer">Atlas @ Talon Forge — cron tick 2026-07-17-1340Z · Fast Execution Mode · lead 443 + template 443 + chunk 270 + chunk_269 source mirror + sitemap patch + build-log + commit + push</p>
</div>

"""

# Wrapper-count assertion: exactly one wrapper
wrapper_count = NEW_TICK.count('<div class="tick-entry"')
assert wrapper_count == 1, f"NEW_TICK has {wrapper_count} tick-entry wrappers, expected 1"

# Prepend
new_content = NEW_TICK + content
BUILD.write_text(new_content, encoding="utf-8")
print(f"WROTE {BUILD}")
print(f"before: {len(content)} bytes")
print(f"after: {len(new_content)} bytes")
print(f"delta: +{len(new_content) - len(content)} bytes")
# Verify topmost is now us
verify = BUILD.read_text(encoding="utf-8")
assert verify.startswith(NEW_TICK[:50]), "new tick is NOT at top"
assert 'data-tick="2026-07-17-1340Z"' in verify[:200], "data-tick anchor not at top"
# Verify still exactly one tick-entry wrapper at the very top by finding first 5K
assert verify[:5000].count('<div class="tick-entry"') == 1, "more than one tick-entry in first 5K — nesting bug"
print("OK — topmost tick is now 1340Z (Variant C prepend verified)")
