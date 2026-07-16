#!/usr/bin/env python3
"""Inline chunk-193 summary section into index.html after chunk-192 closing."""
from pathlib import Path

p = Path("C:/Users/Potts/projects/atlas-store/index.html")
text = p.read_text(encoding="utf-8")

# Locate chunk-192's closing </article>
idx_start = text.find('id="chunk-192"')
assert idx_start > 0, "chunk-192 not found"
idx_end = text.find("</article>", idx_start)
assert idx_end > 0, "chunk-192 closing </article> not found"
# Look at what immediately follows the closing </article>
after = text[idx_end + len("</article>"): idx_end + len("</article>") + 20]
print(f"after chunk-192 closing: {repr(after)}")

# Anchor: chunk-192 closing </article> + triple-newline + </body> + newline
anchor = "</article>\n\n\n</body>\n</html>\n"
assert text.count(anchor) == 1, f"anchor count = {text.count(anchor)}"

chunk193_inline = """<article class="chunk-inline" id="chunk-193">
<h2>Cognigy Conversational-AI 26-Column Audit Checklist — SOC 2 + EU AI Act + ISO 42001 + Per-Flow-Step-Id + Per-Human-Handover-Id Attestation (2026)</h2>
<p>The <strong>ai_customer_support_agents</strong> cohort <strong>CLOSES</strong> with its canonical <strong>3rd-sibling Cognigy 330</strong> (Philipp Heltewig + Sascha Poggemann, $169M+ Series C from Insight Partners + DTCP + Goldman Sachs Growth Equity, customers Lufthansa + Bosch + Mercedes-Benz + Toyota + Heineken + American Airlines + T-Mobile + DHL) — a <strong>Cognigy-specific 26-audit-gap checklist</strong> covering 6 evidence surfaces: (1) per-conversation-flow-graph (per-flow-id + per-flow-version + per-flow-step-id + per-intent-id + per-intent-version + per-entity-id + per-slot-id + per-context-window-id), (2) per-LLM-and-NER-model-lineage (per-LLM-model-id + per-LLM-prompt-hash + per-prompt-template-version + per-prompt-injection-detection-signal-id + per-NER-model-id + per-NER-confidence-score + per-translation-model-id), (3) per-sentiment-and-human-handover (per-sentiment-score + per-handover-id + per-handover-tier + per-human-agent-id + per-regulatory-licensing-attestation + per-AI-action-id + per-action-type + per-action-rollback-id), (4) per-resolution-quality-and-rollback (per-resolution-quality-score + per-PII-redaction-policy-id + per-retention-policy-id + per-WORM-export-target + per-cross-system-join-id), (5) per-conversation-context-window-attestation (per-encryption-key-id + per-PII-detection-id + per-multi-language-policy-id + per-data-residency-region + per-human-review-flag), AND (6) per-conversation prompt-injection-mitigation-outcome — the <strong>per-flow-step-id + per-human-handover-id + per-human-agent-id surfaces</strong> are what distinguish Cognigy from Decagon and Sierra in regulated-industry diligence because Lufthansa ground-ops + Bosch field-service + Mercedes-Benz dealer-network all require per-human-agent attribution for any AI-initiated conversation. Reply to <code>info@cognigy.com</code> with which of the 6 surfaces is most acute (most Cognigy-stage companies say "per-flow-step-id-attestation" or "per-human-handover-id-attribution" or "per-NER-model-id-multilingual-lineage" or "per-data-residency-region-Schrems-II-assessment"). <strong>Full 26-audit-gap map + 14-question buyer self-scoring checklist + 3-tier audit-pricing ($500 / $1,500 / $3,000) + 3-vendor ai_customer_support_agents cohort comparison (Decagon 22/26 + Sierra 18/26 + Cognigy 26/26) + 6-layer reference architecture + 17-framework compliance cross-walk (SOC 2 CC6.1/CC6.7/CC7.2/CC7.4/CC8.1 + EU AI Act Art. 9/12/14/15/53(d)/73 + ISO 42001 §6.1.2/§8.5.6/§9.4 + NIST AI 600-1 + OWASP LLM Top 10 + GDPR + CCPA/CPRA + HIPAA + PCI-DSS + financial-services-conduct-rules + insurance-licensing + telecom-licensing + automotive-licensing + manufacturing-licensing)</strong> lives at <a href="chunks/chunk_193.html">chunks/chunk_193.html</a>. The 26-column join-table maps Cognigy's flow-graph + intent-graph + entity-graph + context-window + LLM-model + NER-model + translation-model + sentiment-score + prompt-template-version + prompt-injection-detection + human-handover + AI-action + resolution-quality + rollback to every SOC 2 CC7.2 + EU AI Act Art. 14/15/53(d) + ISO 42001 9.4 + GDPR Art. 22/28 + CCPA/CPRA automated-decisioning + HIPAA + PCI-DSS row in a regulated-buyer DDQ — pre-mapped, pre-vetted, evidence-ready for Lufthansa ground-ops + Bosch field-service + Mercedes-Benz dealer-network procurement teams.</p>
</article>

</body>
</html>
"""

new_text = text.replace(anchor, chunk193_inline, 1)

assert 'id="chunk-193"' in new_text
assert 'id="chunk-192"' in new_text
assert new_text.count('id="chunk-193"') == 1
assert new_text.endswith("</html>\n")

p.write_text(new_text, encoding="utf-8")
print(f"OK: chunk-193 inlined. Size: {len(text)} -> {len(new_text)} bytes (+{len(new_text)-len(text)}).")
print(f"chunk_inline articles total: {new_text.count('class=' + chr(34) + 'chunk-inline' + chr(34))}")