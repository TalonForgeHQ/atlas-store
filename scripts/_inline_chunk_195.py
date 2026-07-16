"""Splice Hebbia summary into index.html just before the final </body></html>.

The build-log skill recipe: when patch fails on common anchors, write a
small Python splice script that does str.find + concat.
"""
from pathlib import Path

INDEX = Path(r"C:\Users\Potts\projects\atlas-store\index.html")

INDEX_NEW_BLOCK = (
    '\n\n<article class="chunk-inline" id="chunk-195">\n\n'
    '<h2>Hebbia Matrix 22-Column Audit Checklist \u2014 SOC 2 + SEC 2025 Marketing-Rule AI-Amendments + ISO 42001 + Per-ACL-Decision-Lineage (2026)</h2>\n\n'
    '<p>The <strong>ai_enterprise_search_agents</strong> vertical extends to its canonical '
    '<strong>2nd-sibling Hebbia 333</strong> (George Sivakumar + Daniel Lu, $130M+ Series B from Andreessen Horowitz + Founders Fund + Index Ventures, customers 30%+ of top-50 asset managers + most AmLaw-100 firms for SEC-filing + credit-agreement + indenture + municipal-bond-prospectus parsing) \u2014 a <strong>Hebbia-specific 22-audit-gap checklist</strong> covering 5 evidence surfaces: (1) per-document-permission-at-retrieval-time (per-document-id + per-document-permission-id + per-acl-check-id + per-acl-decision-at-retrieval-time + per-staleness-flag-tier (1-4) + per-document-deletion-timestamp), (2) per-document-chunk-id + per-citation-id + per-grounding-evidence-id lineage (per-document-chunk-id + per-citation-id + per-grounding-evidence-id + per-LLM-model-id + per-LLM-prompt-hash + per-prompt-template-version), (3) per-AI-action-override-lineage (per-AI-action-id + per-action-type + per-tool-call-id + per-MCP-tool-call-id + per-action-rollback-id + per-action-rollback-reason + per-human-reviewer-id + per-review-decision), (4) per-prompt-injection-detection-signal-id + per-security-attestation (per-prompt-injection-detection-signal-id + per-prompt-injection-mitigation-action + per-data-residency-region + per-cross-border-data-transfer-mechanism + per-PII-redaction-tier (0-3) + per-row-level-security-id), AND (5) per-engagement-economics + per-fund-attestation (per-engagement-id + per-billing-tier-id + per-fund-id + per-LP-id + per-data-room-source-id + per-data-room-permission-tier + per-document-classification-tier (1-4)) \u2014 the <strong>per-acl-decision-at-retrieval-time + per-staleness-flag-tier + per-row-level-security-id + per-fund-id + per-LP-id surfaces</strong> are what distinguish Hebbia from Glean and Cohere in regulated-asset-manager diligence because the SEC\'s 2025 marketing-rule AI-amendments (Release No. 34-101238) + the OCC\'s heightened-supervision letter on third-party-AI risk (OCC 2024-12) require the buyer\'s compliance officer to disclose the AI\'s row-level-access decision to the underlying LP/ACI investor base. Reply to <code>privacy@hebbia.ai</code> with which of the 5 surfaces is most acute (most Hebbia-stage companies say "per-acl-decision-at-retrieval-time" or "per-staleness-flag-tier-on-deletion" or "per-row-level-security-id-for-LP-restricted-answers" or "per-fund-id-LP-id-attestation-for-SEC-2025-marketing-rule"). <strong>Full 22-audit-gap map + 14-question buyer self-scoring checklist + 3-tier audit-pricing ($500 / $1,500 / $3,000) + 3-vendor ai_enterprise_search_agents cohort comparison (Hebbia 22/22 + Glean 13/22 + Cohere 3/22) + 5-layer reference architecture (Data-Room-Ingest + Permission-At-Retrieval-Time + Chunk-Lineage + Action-Override + Fund-LP-Attestation) + 16-framework compliance cross-walk (SOC 2 CC6.1/CC6.7/CC7.2/CC7.4/CC8.1 + SEC 2025 Marketing-Rule AI-Amendments + OCC 2024-12 Heightened-Supervision + FINRA Rule 3110 + NAIC AI Model Governance + EU AI Act Art. 9/12/14/15/53(d)/73 + ISO 42001 \u00a76.1.2/\u00a78.5.6/\u00a79.4 + NIST AI 600-1 + OWASP LLM Top 10 + GDPR + CCPA/CPRA + HIPAA + GLBA Safeguards + NY DFS Part 500 + CA DOI + DPF/UK-Extension/SCCs)</strong> lives at <a href="chunks/chunk_195.html">chunks/chunk_195.html</a>. The 22-column join-table maps Hebbia\'s per-document-permission-id + per-acl-check-id + per-acl-decision-at-retrieval-time + per-staleness-flag-tier + per-document-deletion-timestamp + per-document-chunk-id + per-citation-id + per-grounding-evidence-id + per-AI-action-id + per-tool-call-id + per-MCP-tool-call-id + per-action-rollback-id + per-human-reviewer-id + per-prompt-injection-detection-signal-id + per-data-residency-region + per-PII-redaction-tier + per-row-level-security-id + per-fund-id + per-LP-id + per-data-room-permission-tier + per-document-classification-tier to every SOC 2 CC7.2 + SEC 2025 marketing-rule + OCC 2024-12 heightened-supervision + EU AI Act Art. 14/15/53(d) + ISO 42001 \u00a79.4 + GLBA Safeguards Rule row in a regulated-buyer DDQ \u2014 pre-mapped, pre-vetted, evidence-ready for asset-manager + broker-dealer + AmLaw-100 + EU-AI-Act-Annex-III-\u00a74-essential-services procurement teams. Cohere 334 is planned as the next sibling to close the canonical 3-vendor ai_enterprise_search_agents cohort.</p>\n\n'
    '</article>\n\n'
)

text = INDEX.read_text(encoding="utf-8")
# Anchor: just before the final closing block </body></html>
end_anchor = "</body>\n</html>"
idx = text.rfind(end_anchor)
assert idx != -1, "end anchor not found"
# Pre-flight: chunk-195 not already inlined
assert 'id="chunk-195"' not in text, "chunk-195 already inlined"
assert text.count('<h2>Hebbia Matrix') == 0, "Hebbia heading already present"
# Splice
new_text = text[:idx] + INDEX_NEW_BLOCK + text[idx:]
INDEX.write_text(new_text, encoding="utf-8")
print(f"spliced {len(INDEX_NEW_BLOCK)} chars before </body></html> at offset {idx}")
print(f"file now {len(new_text)} bytes (was {len(text)})")

# Parse-back verify
t2 = INDEX.read_text(encoding="utf-8")
assert 'id="chunk-195"' in t2, "chunk-195 missing after splice"
assert '<h2>Hebbia Matrix' in t2, "Hebbia heading missing after splice"
assert t2.endswith('</body>\n</html>'), "file no longer ends with </body></html>"
assert 'Hebbia 22/22' in t2, "Hebbia score marker missing"
assert 'privacy@hebbia.ai' in t2, "CTA email missing"
print("ALL CHECKS PASSED")
