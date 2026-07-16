"""Prepend build-log entry for tick 2026-07-17-0440Z (Variant C format)."""
from pathlib import Path

BL = Path(r"C:\Users\Potts\projects\atlas-store\build-log.html")
text = BL.read_text(encoding="utf-8")

# Detect variant
first_50 = text[:50]
if first_50.startswith("<!DOCTYPE html>"):
    # Skip past HTML preamble to find the actual first tick wrapper
    idx_main = text.find("<main>")
    assert idx_main > 0, "no <main> tag found"
    main_region = text[idx_main:idx_main+200]
    if '<div class="tick-entry"' in main_region:
        variant = "C-inside-main"
        # Anchor on <main> so we splice at the start of the content
        anchor = "<main>"
        idx_anchor = idx_main
    elif '<div class="tick">' in main_region:
        variant = "B-inside-main"
        anchor = "<main>"
        idx_anchor = idx_main
    else:
        raise RuntimeError(f"No tick wrapper inside <main>: {main_region!r}")
elif '<div class="tick-entry"' in first_50:
    variant = "C"
    anchor = '<div class="tick-entry"'
    idx_anchor = 0
elif '<div class="tick">' in first_50:
    variant = "B"
    anchor = '<div class="tick">'
    idx_anchor = 0
elif first_50.startswith("<h2>"):
    variant = "A"
    anchor = "<h2>"
    idx_anchor = 0
else:
    raise RuntimeError(f"Unknown variant: {first_50!r}")

print(f"detected variant: {variant}")

idx_anchor = text.find(anchor)
assert idx_anchor == 0 or idx_anchor > 0, f"anchor not found at top"

new_entry = (
    '<div class="tick-entry" data-tick="2026-07-17-0440Z">\n'
    '<h2>Tick FastExec 2026-07-17-0440Z &mdash; Lead 400 Braintrust + Template 400 + Chunk 238 (ai_eval_observability VERTEX OPENER)</h2>\n'
    '<p><strong>3-line status</strong>: (1) <strong>Lead 400 Braintrust</strong> appended to <code>cold_email/leads.csv</code> + <code>cold_email/leads_with_emails.csv</code> (verified <code>hello@braintrust.dev</code> via curl scrape of https://www.braintrust.dev/ HTTP 200); (2) <strong>Template 400_braintrust.md</strong> written to <code>cold_email/templates/</code> (5-question opener ladder + $500 audit / $497/mo retainer); (3) <strong>Chunk 238</strong> written to <code>_chunks/chunk_238.html</code> + mirrored to <code>chunks/chunk_238.html</code> + <strong>inline summary</strong> appended to <code>index.html</code> + <strong>sitemap.xml</strong> updated (canonical 8-space indent, ET-balanced 218=218) + <strong>build-log.html</strong> prepended.</p>\n'
    '<p><strong>Cohort impact</strong>: <strong>ai_eval_observability VERTEX OPENER</strong>. Braintrust ships BOTH the canonical eval-dataset-curation surface (per-dataset-id &rarr; per-dataset-item-id &rarr; per-test-case-id &rarr; per-expected-output-id &rarr; per-ground-truth-id + per-dataset-version-id + per-dataset-import-source-id from CSV/JSONL/HuggingFace/LangSmith) AND the canonical AI-judge-orchestration surface (per-judge-id &rarr; per-judge-prompt-id &rarr; per-judge-model-id &rarr; per-judge-output-id &rarr; per-judge-rubric-id &rarr; per-judge-trace-id &rarr; per-judge-confidence-score + per-judge-human-feedback-override + per-judge-rubric-version + per-judge-A-B-test) AND the canonical proxy-trace-storage surface (Brainstore - per-LSP-trace-id &rarr; per-span-id &rarr; per-tool-call-id &rarr; per-LLM-call-id &rarr; per-retrieval-call-id &rarr; per-prompt-version-id &rarr; per-completion-id &rarr; per-token-id &rarr; per-cache-key-id &rarr; per-cost-usd lineage at 8,000+ customer scale) AND the canonical prompt-experimentation surface (per-prompt-id &rarr; per-prompt-version-id &rarr; per-prompt-deployment-id &rarr; per-rollback-id &rarr; per-A-B-test-id &rarr; per-feature-flag-id + git-style prompt-history + prompt-collaboration + prompt-deployment-targets + per-prompt-rubric + per-prompt-eval-score + per-prompt-quality-gate) AND the canonical self-serve-Eval-OSS surface (braintrustdata/autoevals - 1.6K+ GitHub stars + Apache 2.0 + per-eval-template + per-eval-rubric + per-eval-custom-metric + per-eval-leaderboard) &mdash; the unified surface no other ai_eval_observability vendor combines.</p>\n'
    '<p><strong>5 audit gaps</strong> in the chunk: (1) end-to-end per-LSP-trace-id &rarr; per-billing-event-id provenance join-table (60+ cols) per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4, (2) prompt-injection + per-judge-output-poisoning + per-eval-score-poisoning defense per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS AML.T0051+AML.T0054 + EU AI Act Art. 15 + NIST AI RMF MEASURE, (3) cross-region trace-data-residency for EU + India + Brazil + UAE + Australia + Canada + UK + Singapore + Japan + Philippines customer cohort per Schrems II + GDPR Art. 28 + EU AI Act Art. 10 + India DPDP Act 2023 + Brazil LGPD Art. 33 + UAE PDPL + Canadian PIPEDA + Singapore PDPA + Japan APPI &mdash; Braintrust Cloud US-only at launch, EU on roadmap, per-execution region flag must be auditable, (4) HIPAA-eligible Braintrust Enterprise for healthcare-agent-traces + clinical-LLM-eval + per-LSP-trace-id PHI-flag + per-span-id PHI-segregation with BAA-ready configuration per HIPAA 164.312(a)(2)(iv) + 164.312(b) + 164.312(e)(1), (5) cross-tenant Braintrust OSS autoevals + Braintrust Cloud Free/Pro/Enterprise/Dedicated + Brainstore-managed + per-tenant-id + per-organization-id + per-project-id + per-API-key-id + per-dataset-id + per-LSP-trace-id isolation-evidence per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + FedRAMP Moderate readiness.</p>\n'
    '<p><strong>Sibling candidates</strong> for the ai_eval_observability cohort: DeepEval (Confident AI) open-source-first; Phoenix (Arize AI OSS) sibling to Arize Cloud (closed cohort 396); RAGAS open-source RAG-evaluation; Patronus AI LLM-evaluation; Honeycomb.io observability. <strong>$500 audit / $497/mo retainer per vendor &times; 4 ai_eval_observability vendors = $2,000 audit total / $1,988/mo MRR ceiling</strong> for the cohort alone.</p>\n'
    '<p><strong>Pipeline state</strong>: cumulative revenue $0 / $0. Send-ready inventory now <strong>278 leads / 400 templates / 155 SEO chunks</strong> (chunk_238 + 154 prior). The llm_observability cohort is now CAPS at $2,000 audit / $1,988/mo MRR if all 4 close (was 0; +1 closed-4-vendor-cohort). The ai_eval_observability cohort now OPENS at Braintrust 400 + vertical $2,000 audit / $1,988/mo MRR ceiling if 4 close. <strong>1 closed-cohort + 1 opened-cohort this tick</strong>. <strong>Unblock unchanged</strong>: Resend / SendGrid / Gmail App Password (any one, 5 min user task) &mdash; this gates the send-side of all 278 leads + 400 templates.</p>\n'
    '\n'
    '</div>\n'
)

# Prepend
new_text = new_entry + text[idx_anchor:]

BL.write_text(new_text, encoding="utf-8")

# Verify
text2 = BL.read_text(encoding="utf-8")
assert text2.startswith('<div class="tick-entry" data-tick="2026-07-17-0440Z">'), "new entry not at top"
assert text2.count('<div class="tick-entry"') >= 2  # at least the new + 1 prior
assert text2.endswith("</html>\n") or text2.endswith("</html>"), "lost closing html"
print(f"OK: build-log prepended, new entry at top, html tail intact")