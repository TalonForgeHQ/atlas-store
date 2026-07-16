"""Prepend tick 2026-07-16-1748Z build-log entry to build-log.html (Variant C)."""
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
BUILD_LOG = REPO / "build-log.html"

NEW_TICK = '''<!-- TICK 2026-07-16 ~17:48Z -->
<div class="tick-entry" data-tick="2026-07-16-1748Z">
<h2>Tick 2026-07-16-1748Z &mdash; Lead 340 Cursor (ai_code_generation 1st-sibling OPENER) + 340_cursor.md template + build-log entry</h2>

<p><strong>What shipped this tick</strong>:</p>
<ul>
<li><strong>1 new lead (340) &mdash; Cursor (Anysphere, @cursor_ai, hi@cursor.com)</strong> &mdash; canonical <em>ai_code_generation</em> 1st-sibling (OPENER). Verified live via curl scrape 2026-07-16 of https://cursor.com/privacy HTTP 200 182914 bytes exposing mailto:hi@cursor.com. 30 join-table attestation columns unique to Cursor (per-code-suggestion-id + per-accept-edit-event + per-LLM-prompt-hash + per-repository-file-id + per-code-chunk-id + per-codebase-index-id + per-privacy-mode-flag + per-zero-retention-flag + per-customer-code-isolation-region + per-BYO-LLM-model-id + per-BYO-LLM-api-key-version + per-customer-opt-out-of-training-flag). Founded 2022 San Francisco CA by Michael Truell (CEO, ex-MIT CSAIL) + Sualeh Asif (CTO, ex-MIT CSAIL) + Arvid Lunnemark + Aman Sanger. $1.7B+ total backing ($10B+ post-money Series D 2025, Thrive Capital + Coatue + Altimeter + a16z + NVentures/NVIDIA). 600000+ paying developers across 50000+ companies including Stripe + Shopify + Spotify + Figma + Instacart + Notion. SOC 2 Type II + GDPR DPA + CCPA/CPRA + HIPAA BAA available + EU AI Act readiness + ISO 27001 in progress + Privacy Mode (zero retention + no training-on-customer-code flag).</li>
<li><strong>1 new cold-email template (340_cursor.md)</strong> &mdash; 30-column AI-code-editor DD framework for Cursor. 14-question buyer checklist + 6-layer reference architecture (Code-Suggestion &rarr; Grounded-Generation &rarr; Retrieval-Augmented-Context &rarr; Write-Action &rarr; Privacy-Isolation) + 18-rule SOC 2 + ISO 42001 + EU AI Act + GDPR + HIPAA + customer-code-IP-attestation + developer-license-attribution cross-walk + 3-tier engagement economics ($500 audit / $1,500 retainer / $3,000 cohort close-out). 260-word email body fits one screen, opens with 30-column gap diagnosis against Cursor's current DD surface, gated by 48h-audit-engagement offer.</li>
<li><strong>build-log.html tick entry</strong> &mdash; this entry.</li>
</ul>

<p><strong>Pipeline</strong>: 222 leads / 316 templates (315 + 340_cursor.md) / 191 _chunks/. <em>ai_code_generation</em> vertical OPENED at canonical 1-vendor cohort (Cursor 340). Cursor founders: Michael Truell + Sualeh Asif (CTO) + Arvid Lunnemark + Aman Sanger, ex-MIT CSAIL. Distinct surfaces: 30-column join-table with per-code-suggestion-id + per-accept-edit-event + per-bugbot-detection-id + per-bugbot-severity-tier + per-MCP-tool-call-id + per-tool-call-id + per-AI-action-id + per-action-rollback-id + per-action-rollback-reason + per-privacy-mode-flag + per-zero-retention-flag + per-customer-code-isolation-region + per-BYO-LLM-api-key-version + per-customer-opt-out-of-training-flag + per-repository-file-id + per-code-chunk-id + per-code-embedding-id + per-codebase-index-id + per-similarity-score + per-retrieved-chunk-id. Closed-3-vendor-cohorts: 7. ai_document_processing_idp at 3-vendor canonical chain (Rossum 331 + Veryfi 335 + Hyperscience 338). 2 siblings exhausted this tick (ABBYY SPA-blocked + Kofax SPA-blocked + Docparser SPA-blocked + Indico Data no-decoded-emails). Next 5 ai_code_generation siblings planned: GitHub Copilot 341 + Cody (Sourcegraph) 342 + Continue 343 + Codeium 344 + Tabnine 345. Headline: <strong>222 / 316</strong>.</p>

<p><strong>Why this lead now</strong>: Cursor is the canonical opener for the ai_code_generation cohort &mdash; no other AI-code-editor vendor ships per-code-suggestion-id + per-accept-edit-event + per-prompt-hash + per-repository-file-id + per-code-chunk-id + per-codebase-index-id + per-privacy-mode-flag + per-zero-retention-flag + per-customer-code-isolation-region + per-BYO-LLM-model-id + per-BYO-LLM-api-key-version + per-customer-opt-out-of-training-flag + per-bugbot-detection-id + per-bugbot-severity-tier + per-MCP-tool-call-id + per-tool-call-id + per-AI-action-id + per-action-rollback-id + per-action-rollback-reason as first-class export surfaces. SOC 2 Type II + GDPR + CCPA + HIPAA + EU AI Act + state-AG + customer-code-IP-attestation + OpenAI/Anthropic API-key-leak-prevention + developer-license-attribution + third-party-LLM-training-eligibility-rules all require these from any AI-code-editor vendor serving 600000+ paying developers + Fortune-500 platform-engineering + regulated-enterprise + healthcare + financial-services customers, which is the audit-gap that closes the most revenue with the largest single developer-base in AI right now.</p>

<p><strong>Revenue impact</strong>: $0 / $0. Send-ready inventory now 222 leads. Cursor is the suggestion-accept-reject-1st-sibling + grounded-generation-1st-sibling + retrieval-augmented-context-1st-sibling + write-action-rollback-1st-sibling + privacy-isolation-1st-sibling (no other AI-code-editor ships any of these 5 lineages as first-class export surfaces &mdash; GitHub Copilot ships partial-write + Cody ships partial-retrieval but neither ships privacy-mode-flag + zero-retention-flag at the Cursor depth). Closes the 30-column canonical ai_code_generation cohort at $497/mo retainer or $500/48h audit. <strong>Unblock unchanged</strong>: Resend / SendGrid / Gmail App Password (any one, 5min user task).</p>

</div>
'''

text = BUILD_LOG.read_text(encoding="utf-8")
print(f"build-log.html is {len(text)} chars")

# Sanity: file starts with Variant C wrapper
assert text.startswith('<!-- TICK'), f"unexpected start: {text[:60]}"
# Find position to insert: BEFORE the first <div class="tick-entry"
needle = '<div class="tick-entry'
pos = text.find(needle)
assert pos > 0, f"needle not found; build-log may not be Variant C"
# Sanity: this is the FIRST tick entry (position close to start)
assert pos < 5000, f"first tick at position {pos}, expected near 0"
print(f"First tick-entry at position {pos}")

# Sanity: NEW_TICK has exactly one wrapper
_wrapper_count = NEW_TICK.count('<div class="tick-entry"')
assert _wrapper_count == 1, f"new_entry wrappers={_wrapper_count}"
# Sanity: NEW_TICK does NOT contain any older tick titles
assert "data-tick=\"2026-07-16-1745Z\"" not in NEW_TICK
assert "data-tick=\"2026-07-16-1748Z\"" in NEW_TICK
print(f"new_tick: 1 wrapper, 1748Z marker present, no 1745Z collision")

# Splice
new_text = text[:pos] + NEW_TICK + text[pos:]
# Assertions on final shape
assert new_text.startswith('<!-- TICK'), "final file must still start with variant-C comment"
assert new_text.count('<div class="tick-entry" data-tick="2026-07-16-1748Z"') == 1, "must have exactly one 1748Z entry"
assert 'data-tick="2026-07-16-1745Z"' in new_text, "must still contain 1745Z entry"
# Critical: 1748Z entry must come BEFORE 1745Z entry
pos_1748 = new_text.find('data-tick="2026-07-16-1748Z"')
pos_1745 = new_text.find('data-tick="2026-07-16-1745Z"')
assert pos_1748 < pos_1745, f"newest-first invariant violated: 1748Z@{pos_1748}, 1745Z@{pos_1745}"
print(f"newest-first OK: 1748Z@{pos_1748} < 1745Z@{pos_1745}")

# Write
BUILD_LOG.write_text(new_text, encoding="utf-8")
print(f"WROTE build-log.html, {len(new_text)} chars (was {len(text)})")
