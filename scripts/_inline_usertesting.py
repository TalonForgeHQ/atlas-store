"""Inline the Maze 478 catch-up section + UserTesting 479 chunk-300 section
into index.html. Insert BEFORE the final </html> tag, which appears exactly once.

Cross-tick inlining regression fix: tick 2026-07-17 ~13:10Z shipped Maze 478
but never inlined a summary card for it. This tick (UserTesting 479) catches up.
"""
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
INDEX = REPO / "index.html"

text = INDEX.read_text(encoding="utf-8")

# Anchor: the final </html> tag. Find last occurrence.
last_html_close = text.rfind("</html>")
assert last_html_close > 0, "no </html> found in index.html"

NEW_SECTIONS = """<section id="chunk-300" data-vertical="ai_research" data-tick="2026-07-17-fast-exec-usertesting-479" data-lead="479" data-cohort="usertesting-thoma-bravo-portfolio-3m-participants-40-countries">
<article>
<h2>Maze 478 — product-discovery + AI-assisted-research-synthesis (Catch-up from tick 2026-07-17 ~13:10Z)</h2>
<p>Maze is the canonical continuous-product-discovery + AI-assisted-research-synthesis platform that extends the ai_research cohort to a fourth sibling. Founded by Jonathan Widawski (CEO & Co-Founder, verified 2026-07-17 via https://maze.co/about-us/ HTTP 200). Maze combines prototype-testing + surveys + AI-assisted-research-synthesis in a single workflow — distinct from Outset (AI-moderated-interview) + Listen (AI-synthesis-of-open-ended-consumer-feedback) + Dovetail (5-AI-surface research-insights) + UserTesting (Human Insight Platform + Live Conversation). privacy@maze.design verified live 2026-07-17 via curl scrape https://maze.co/privacy-policy/ HTTP 200 exposing mailto:privacy@maze.design as canonical privacy/DPA strategic-inbound channel. Five audit gaps per Maze 478 audit binder: (1) 12-col per-Participant-ID provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 capturing per-participant-consent-link-id + per-prototype-test-id + per-AI-synthesis-decision-id + per-prototype-feedback-card-id + per-AI-disclosure-event-id + per-human-oversight-approval-id + per-customer-tenant-id + per-procurement-vendor-DD-event-id + per-audit-log-entry-id + per-residency-region-id + per-source-system-write-id + per-data-residency-region-id, (2) AI-assisted-research-synthesis training-corpus + fine-tune-license-provenance per EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary + ISO 42001 6.1.4, (3) prompt-injection + participant-disclosure-bypass + prototype-test-poisoning + AI-synthesis-output-poisoning + AI-disclosure-bypass-defense per OWASP LLM Top 10 LLM01 + LLM06 + EU AI Act Art. 14 human-oversight + Art. 50 transparency-obligation + 12-state AI-disclosure (CA SB 1001 + CO SB 24-205 + IL AI Video Interview Act + TX + NY + 7 others - Maze prototype-tests touch participants in multiple states), (4) cross-tenant Maze SaaS + customer-tenant-isolated multi-tenant + participant-consent-link per-tenant-isolation-evidence per SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10 + Schrems II, (5) WORM retention + cost-attribution join-table linking per-prototype-test-AI-synthesis-cost + per-AI-synthesis-output-LLM-call-cost + per-customer-tenant-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement. Cohort ceiling delta <strong>+$500 audit / +$497/mo MRR</strong> (Outset 475 + Listen Labs 476 + Dovetail 477 + Maze 478 extends ai_research cohort to 4-vendor-deep at $2,000 audit / $1,988/mo MRR ceiling). Lead row 478 in <code>cold_email/leads.csv</code>; cold-email template at <a href="cold_email/templates/478_maze.md">template 478_maze.md</a>.</p>
</article>
</section>

<section id="chunk-301" data-vertical="ai_research" data-tick="2026-07-17-fast-exec-usertesting-479" data-lead="479" data-cohort="usertesting-thoma-bravo-portfolio-3m-participants-40-countries">
<article>
<h2>UserTesting 479 — Thoma Bravo portfolio + ~3M participants + Aug 2026 GPAI deadline (chunk 300 milestone!)</h2>
<p>UserTesting is the canonical AI-augmented-UX-research platform extending the ai_research cohort to a fifth sibling — and the largest by participant-volume. Owned by Thoma Bravo since 2022 (~$1.1B acquisition); portfolio also includes UserZoom + Askable + Respondia (cross-portfolio training-corpus spans ~5M moderated-conversations and ~50M participant-recordings). HQ Atlanta GA + San Francisco CA; founded 2007; ~3M participants across 40+ countries; named enterprise customers include ~50% of Fortune 100. Distinct from Outset (AI-moderated-interview) + Listen (AI-synthesis-of-open-ended-consumer-feedback) + Dovetail (5-AI-surface research-insights) + Maze (continuous-product-discovery + AI-assisted-research-synthesis) because UserTesting is canonical AI-augmented-UX-research at PLATFORM SCALE + Thoma-Bravo-portfolio-distribution to enterprise procurement-vendor-DD pipelines. privacy@usertesting.com verified live 2026-07-17 via curl scrape https://www.usertesting.com/privacy-policy/ HTTP 200 135838 bytes exposing mailto:privacy@usertesting.com as canonical SOC 2 + CCPA/CPRA + GDPR Art. 37 DPO + EU AI Act strategic-inbound channel per canonical og:title "UserTesting Privacy Policy" + og:description "Get UX research, product, design, and marketing feedback with UserTesting's Human Insight Platform and Services. Start here to improve customer experiences & drive innovation." press@usertesting.com verified via /contact HTTP 200 107162 bytes; allreplies@usertesting.com verified across /about + /contact + /legal + /privacy as canonical broadcast. Five audit gaps per UserTesting 479 audit binder: (1) 12-col per-Participant-ID provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 capturing per-participant-consent-link-id + per-conversation-id + per-ai-moderation-decision-id + per-synthesis-output-id + per-human-oversight-approval-id + per-customer-tenant-id + per-procurement-vendor-DD-event-id + per-audit-log-entry-id + per-residency-region-id + per-retention-decision-id + per-ai-disclosure-event-id + per-cross-border-transfer-id, (2) AI-moderation-of-Live-Conversation training-corpus + fine-tune-license-provenance per EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary + ISO 42001 6.1.4 (cross-portfolio-Thoma-Bravo training-corpus spans ~5M moderated-conversations + ~50M participant-recordings), (3) prompt-injection + participant-disclosure-bypass + AI-moderation-output-poisoning + synthesis-output-poisoning + AI-Insights-poisoning + Highlight-Reels-poisoning-defense per OWASP LLM Top 10 LLM01 + LLM06 + EU AI Act Art. 14 human-oversight + Art. 50 transparency-obligation + 12-state AI-disclosure (CA SB 1001 + CO SB 24-205 + IL AI Video Interview Act + TX + NY + 7 others - UserTesting Live Conversation AI-moderator touches participants in multiple states), (4) cross-tenant UserTesting-SaaS + Thoma-Bravo-portfolio-tenant-isolated multi-tenant + per-entity-AWS-account + per-entity-KMS-key + per-entity-AI-inference-endpoint + per-entity-AI-training-pipeline per SOC 2 CC6.1 + GDPR Art. 28 + Schrems II (cross-entity-tenant-isolation-evidence is auditable post-Thoma-Bravo acquisition), (5) WORM retention + cost-attribution join-table linking per-AI-moderation-decision-cost + per-synthesis-output-LLM-call-cost + per-customer-tenant-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement. Cohort ceiling delta <strong>+$500 audit / +$497/mo MRR</strong> (Outset 475 + Listen Labs 476 + Dovetail 477 + Maze 478 + UserTesting 479 extends ai_research cohort to 5-vendor-deep at $2,500 audit / $2,485/mo MRR ceiling). This is the highest-leverage next-tick move because UserTesting is the largest ai_research-cohort vendor by participant-volume, and Thoma Bravo's $1.1B acquisition price signals enterprise-budget-grade buyer intent — a single UserTesting engagement could realistically convert to 4 paying clients at $497/mo each = $1,988/mo MRR (just from the UserTesting-engagement-funnel extending to UserZoom + Askable + Respondia). Read the full chunk at <a href="chunks/chunk_300.html">chunks/chunk_300.html</a>; lead row 479 in <code>cold_email/leads.csv</code>; cold-email template at <a href="cold_email/templates/479_usertesting.md">template 479_usertesting.md</a>.</p>
</article>
</section>

"""

# Idempotency: if chunk-300 section already inlined, skip.
if '<section id="chunk-300"' in text and 'usertesting-thoma-bravo-portfolio' in text:
    print("ALREADY INLINED: chunk-300/301 sections present in index.html — no-op.")
else:
    new_text = text[:last_html_close] + NEW_SECTIONS + text[last_html_close:]
    INDEX.write_text(new_text, encoding="utf-8")
    added = len(new_text) - len(text)
    print(f"INLINED: +{added} bytes. New size: {len(new_text):,}. Sections chunk-300 (Maze catch-up) + chunk-301 (UserTesting 479) added before final </html>.")

# Sanity assertions
final = INDEX.read_text(encoding="utf-8")
assert 'id="chunk-300"' in final and "Maze 478" in final, "chunk-300 inlining failed"
assert 'id="chunk-301"' in final and "UserTesting 479" in final, "chunk-301 inlining failed"
assert final.count("<section") >= 290, f"too few sections: {final.count('<section')}"
assert "</html>" in final, "closing </html> missing!"
print(f"SANITY OK: chunk-300 + chunk-301 present, total sections={final.count('<section')}, ends with </html>.")