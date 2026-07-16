#!/usr/bin/env python3
"""Prepend a new tick entry to build-log.html (Variant C: <div class="tick-entry" data-tick="...">)."""
from pathlib import Path
import re

p = Path("C:/Users/Potts/projects/atlas-store/build-log.html")
text = p.read_text(encoding="utf-8")

# Verify Variant C
assert text.startswith('<div class="tick-entry"'), f"not Variant C: starts with {text[:60]!r}"

NEW_TICK = """<div class="tick-entry" data-tick="2026-07-16-1605Z">
<h2>Tick 2026-07-16-1605Z — Lead 330 Cognigy (ai_customer_support_agents 3rd-sibling COHORT CLOSURE) + Template + Chunk_193 + Sitemap + Index Inline</h2>
<p>Lead <strong>330 Cognigy</strong> (<strong>Philipp Heltewig CEO</strong> + <strong>Sascha Poggemann CTO</strong>, $169M+ Series C from Insight Partners + DTCP + Goldman Sachs Growth Equity, customers Lufthansa + Bosch + Mercedes-Benz + Toyota + Heineken + American Airlines + T-Mobile + DHL, HQ Dusseldorf Germany + SF office at 5 3rd St Suite 700 94105) appended to <code>cold_email/leads.csv</code> + <code>cold_email/leads_with_emails.csv</code> (both 8-col + 13-col schemas verified, dedupe invariant clean, 0 duplicate indices). Email <strong>info@cognigy.com</strong> verified live 2026-07-16 via curl scrape <code>https://www.cognigy.com/privacy-policy</code> HTTP 200 445324 bytes exposing mailto:info@cognigy.com + secondary DPO.Cognigy@twobirds.com DPO contact. Template <code>cold_email/templates/330_cognigy.md</code> written (14-question buyer-DD checklist + 26-column join-table + 28-row compliance cross-walk + 3-tier audit-pricing $500 / $1,500 / $3,000 + 30-min AE enablement video). Chunk <code>_chunks/chunk_193.html</code> + <code>chunks/chunk_193.html</code> written (Cognigy-specific 26-audit-gap checklist covering 6 evidence surfaces: per-conversation-flow-graph + per-LLM-and-NER-model-lineage + per-sentiment-and-human-handover + per-resolution-quality-and-rollback + per-conversation-context-window-attestation + per-conversation prompt-injection-mitigation-outcome + 14-question buyer-DD checklist + 28-row compliance cross-walk SOC 2 CC7.2 + EU AI Act Art. 14/15/53(d) + ISO 42001 9.4 + GDPR Art. 22/28 + CCPA/CPRA automated-decisioning + HIPAA + PCI-DSS + financial-services-conduct-rules + insurance-licensing + telecom-licensing + automotive-licensing + manufacturing-licensing). Sitemap <code>sitemap.xml</code> patched + indent-regression repaired via <code>scripts/_repair_sitemap_193.py</code> (XML parses, 260/260 balanced &lt;url&gt; tags). Index <code>index.html</code> inlined <strong>chunk-193 article</strong> after chunk-192 via <code>scripts/_inline_chunk_193.py</code> (last chunk ID now = 193, +3565 bytes). <strong>ai_customer_support_agents vertical now CLOSED at canonical 3-vendor cohort</strong>: Decagon 328 (per-conversation-policy-gate 22-col) + Sierra 329 (per-brand-voice-policy-id 24-col) + Cognigy 330 (per-flow-step-id + per-human-handover-id + per-NER-model-id 26-col). Distinct surfaces — Decagon wins on per-policy-id + per-policy-version + per-policy-trigger-condition + per-policy-decision + per-policy-rollback (policy-graph lineage); Sierra wins on per-brand-voice-policy-id + per-tone-of-voice-personalization-id (state insurance + financial-services regulators treat AI agent tone-of-voice as regulated disclosure artifact); Cognigy wins on per-flow-step-id + per-NER-model-id + per-translation-model-id + per-human-handover-id + per-human-agent-id + per-data-residency-region + per-multi-language-policy-id (Lufthansa + Bosch + Mercedes-Benz multilingual regulated-buyer attestation). Pipeline: 216 leads / 308 templates / 193 chunks. Closed-3-vendor cohort count now = 13 (1 ai_eval_observability + 12 others). <strong>2 highest-ROI next-tick candidates</strong>: (1) close ai_chip_silicon with Tenstorrent 325 + SambaNova 326 + Lightmatter 327 already CLOSED — try ai_inference_platform next (Cohere + Anyscale + Modal Labs + DeepInfra + Together AI + Fireworks AI + Replicate); (2) open new vertical ai_data_privacy_compliance (OneTrust + TrustArc + BigID + Securiti.ai + Collibra + Alation + Informatica + DataHub + Immuta + Privacera).</p>
</div>

"""

# Prepend: insert before the FIRST existing <div class="tick-entry"
anchor = '<div class="tick-entry"'
idx = text.find(anchor)
assert idx == 0, f"first tick-entry not at position 0, found at {idx}"

new_text = NEW_TICK + text

# Sanity: new entry contains exactly one wrapper
assert NEW_TICK.count('<div class="tick-entry"') == 1
# new entry does NOT start with <h2> (it's a div wrapper)
assert new_text.startswith('<div class="tick-entry" data-tick="2026-07-16-1605Z">')
# Sibling tick-1500 still present
assert 'data-tick="2026-07-16-1500Z"' in new_text

p.write_text(new_text, encoding="utf-8")
print(f"OK: prepended tick 2026-07-16-1605Z. Size: {len(text)} -> {len(new_text)} bytes (+{len(new_text)-len(text)}).")
print(f"data-tick count: {new_text.count('data-tick=')}")
ticks = re.findall(r'data-tick="([^"]+)"', new_text)
print(f"first 5 data-tick values: {ticks[:5]}")