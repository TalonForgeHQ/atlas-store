#!/usr/bin/env python3
"""Tick 695 — insert Cursor (lead 695) card after every DISCO (lead 694) card in index.html."""
from pathlib import Path

INDEX = Path("index.html").read_text(encoding="utf-8")

# Find all lines that begin a DISCO article card
CURSOR_CARD = '''<article class="card" data-tick="2026-07-20-fast-exec-cursor-695">
  <h3><a href="chunks/chunk_695.html">Cursor AI Code Editor Audit 2026: Composer-1 + Cursor Tab + Cursor Agent + Claude + GPT-5 + Gemini Multi-LLM-Router + SOC 2 Type II + EU AI Act Article 14(4) + Annex IV + 70K Business Customers + 50% Fortune 100</a></h3>
  <p><strong>Vertical:</strong> ai_coding_agent_vertical OPENER sibling #1/5 (NEW 12th Atlas vertical after ai_legal_compliance_os 690-694 CLOSED at 5/5)</p>
  <p><strong>Lead:</strong> Cursor (Anysphere, Inc. — cursor.com; Aman Sanger Co-Founder + CEO ex-MIT; Michael Truell Co-Founder ex-MIT; Sualeh Asif Co-Founder; Jared Sulove Co-Founder; $1.6B+ ARR run-rate (2025); $29.3B valuation Series D 2025; 70K+ business customers; 50%+ of Fortune 100; Microsoft + Google + Amazon + Shopify + Stripe + OpenAI named customers; Y Combinator W20; Andreessen Horowitz + Thrive Capital + Coatue + NVIDIA + Google + Salesforce Ventures; Composer-1 in-house frontier model 2025-10)</p>
  <p><strong>Wedge:</strong> Per-LLM-sub-processor-version-pinning audit-trail (Composer-1 + Anthropic Claude + OpenAI GPT-5 + Google Gemini + cursor.sh background-agent + retrieval-index) + per-prompt-version + per-completion-version + per-context-retrieval-RAG-chunk-source-version (chunk-source-version + chunk-source-file-version + chunk-source-line-range + chunk-source-checksum + chunk-source-license + chunk-source-EMBEDDING-model-version) + per-PR-branch + per-repo-isolation + per-tenant-isolation + per-SSO-idp-tenant + per-privacy-mode-zero-data-retention + per-training-data-opt-in/out + per-customer-source-code-deletion-receipt + per-MFA-required-privilege-escalation audit-trail + per-attribution-version + per-output-license-recommendation-version (which LLM sub-processor produced which line + which retrieval chunk sourced which context + canonical license recommendation applied) + per-agent-mode-background-task-version + per-bash-tool-call-version + per-LSP-tool-version + per-test-runner-integration-version + enterprise self-hosted-region-pinning (US-federal + US-state + EU-member-state + UK + APAC) + Schrems II SCC + EU-US DPF + UK Addendum + per-enterprise-self-hosted-KMS-key-id + per-enterprise-self-hosted-VPC-isolation + per-PR-branch-CI-pipeline-integration-version (GitHub Actions + GitLab CI + CircleCI + Jenkins + Buildkite + Drone) + per-PR-review-bot-version + per-SAST-integration-version + per-SCA-integration-version (Snyk + Dependabot + Socket + Sonatype + JFrog Xray + FOSSA + Sigrid) + per-Workspace-trust-version + per-VS-Code-extension-API-version + per-Open-VSX-registry-version + per-extension-permission-posture + per-extension-isolation + SCIM-provisioning-version + OIDC-scope-version + SAML-assertion-version + JIT-provisioning-version + directory-sync-version audit-trail. AI code editor + Composer-1 + Claude + GPT-5 + Gemini multi-LLM-router + Cursor Agent multi-step-coding-task + Cursor Tab next-edit-prediction + Cmd-K natural-language-edit + codebase-aware RAG + multi-file edits + enterprise SSO + SCIM + privacy-mode-no-data-retention + enterprise self-hosted region-pinning US/EU/UK/APAC + 70K business customers + 50% Fortune 100 engineering organizations.</p>
  <p><strong>Compliance:</strong> SOC 2 Type II + ISO 27001 + ISO 27018 + ISO/IEC 42001 + ISO/IEC 23894 + GDPR Art 5+9+22+28+32+35 + UK GDPR + Schrems II SCC + EU-US DPF + UK Addendum + CCPA/CPRA + PIPEDA + LGPD + APPI + Australia Privacy Act + Singapore PDPA + Quebec Law 25 + China PIPL Art 38 + EU AI Act Art 9+12+14(4)+50+53(1)(b) + Annex IV technical-documentation + NIST AI RMF 600-1 + NIST AI 600-2 GENAI profile + OWASP LLM Top-10 (LLM01 prompt-injection + LLM02 sensitive-info-disclosure + LLM03 training-data-poisoning + LLM06 training-data-exfiltration + LLM07 insecure-plugin + LLM08 vector-DB-poisoning + LLM09 misinformation + LLM10 model-theft) + MITRE ATLAS + EO 14028 + EO 14110 + SLSA v1.0 Level 3 + NIST SP 800-218A SSDF + SLSA Provenance + in-toto attestation + NIST SP 800-53 Rev 5 + FedRAMP Moderate + FINRA + SEC + FINRA Rule 3110 + FINRA Rule 4511 + 21st Century Cures Act + HIPAA BAA + SOX 404</p>
  <p><strong>Offer:</strong> $500/48h evidence-gap map or $497/mo quarterly refresh retainer; YanXbt 5-client pattern $497/mo × 5 = $2,485 MRR per operator.</p>
</article>
'''

DISCO_LINE = '<article class="card" data-tick="2026-07-20-fast-exec-disco-694">'

# Find all DISCO article openings
parts = INDEX.split(DISCO_LINE)
print(f'Found {len(parts)-1} DISCO card openings')

new = DISCO_LINE + CURSOR_CARD.join(parts)
# The first part is BEFORE the first DISCO line — keep it. Each DISCO opening gets the card inserted after it.
# Re-form: leading part + first DISCO + CURSOR + (middle: between DISCO opens) + CURSOR + (middle) + ...
# A clean re-assemble: use a sentinel.
SENTINEL = '<<<DISCO_INSERT>>>'
new_parts = INDEX.replace(DISCO_LINE + '\n', SENTINEL).split(SENTINEL)
# Each chunk except the very first one was preceded by a DISCO_LINEn\n that we replaced with SENTINEL.
# So: [chunk0, chunk1_after_DISCO_1, chunk2_after_DISCO_2, ...]
# We need: chunk0 + DISCO_LINE + card + chunk1 + DISCO_LINE + card + chunk2 + ... + chunkN
result = new_parts[0]
for ch in new_parts[1:]:
    result += DISCO_LINE + '\n' + CURSOR_CARD + ch

print(f'Index size: {len(INDEX)} -> {len(result)}')
Path("index.html").write_text(result, encoding="utf-8")

# Verify count of new card insertions
print('cursor card occurrences after edit:', result.count('fast-exec-cursor-695'))
print('disco card occurrences after edit:', result.count('fast-exec-disco-694'))
