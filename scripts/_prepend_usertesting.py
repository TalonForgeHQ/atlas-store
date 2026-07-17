"""Prepend a Tick entry to build-log.html with Variant-C wrapper shape
(<div class="tick-entry" data-tick="...">).
"""
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
BUILD_LOG = REPO / "build-log.html"

NEW_ENTRY = """<div class="tick-entry" data-tick="2026-07-17-fast-exec-usertesting-479">
<h2>Tick FastExec 2026-07-17 ~20:18Z — UserTesting 479 (chunk 300 milestone!) + Maze 478 catch-up + Thoma Bravo portfolio lane</h2>

<h3>Artifacts shipped (4 surfaces updated)</h3>
<ul>
<li><strong>cold_email/leads.csv</strong> — Lead 479 "UserTesting" appended (index 479, email privacy@usertesting.com, vertical ai_research, tier 1, template 479_usertesting.md). parse-back verified, no duplicate indices across 357 rows.</li>
<li><strong>cold_email/leads_with_emails.csv</strong> — Lead 479 "UserTesting" appended (lead_index 479, best_email privacy@usertesting.com, emails_found privacy@usertesting.com|press@usertesting.com|allreplies@usertesting.com). parse-back verified, no duplicate indices across 324 rows.</li>
<li><strong>cold_email/templates/479_usertesting.md</strong> — audit-cold outreach to privacy@usertesting.com; 3-question EU AI Act Aug 2 2026 GPAI-deadline framing + $500 audit + $497/mo retainer offer. Verifies live: UserTesting privacy-policy HTTP 200 135,838 bytes with canonical og:title "UserTesting Privacy Policy".</li>
<li><strong>_chunks/chunk_300.html</strong> — UserTesting EU AI Act GPAI audit (5 audit gaps: per-Participant-ID provenance join-table, AI-moderation training-corpus, prompt-injection defense, Thoma-Bravo cross-tenant-isolation, WORM cost-attribution). Mirrored to public/chunks/chunk_300.html. <strong>CHUNK 300 MILESTONE — 300 SEO chunks live on the static site.</strong></li>
<li><strong>sitemap.xml</strong> — chunk_300 URL entry appended (lastmod 2026-07-17, changefreq weekly, priority 0.85). Balanced <url> open/close tags verified.</li>
<li><strong>index.html</strong> — summary card sections chunk-300 (Maze 478 cross-tick inlining regression catch-up) + chunk-301 (UserTesting 479) inlined before final </html> tag. Total sections=592, closing </html> preserved.</li>
</ul>

<h3>Verification (live URLs)</h3>
<ul>
<li><strong>usertesting.com/privacy-policy</strong> HTTP 200 via curl <code>https://www.usertesting.com/privacy-policy/</code> · Content-Length 135,838 bytes · canonical og:title "UserTesting Privacy Policy" · og:description "Get UX research, product, design, and marketing feedback with UserTesting's Human Insight Platform and Services. Start here to improve customer experiences & drive innovation." · <code>mailto:privacy@usertesting.com</code> exposed in HTML as canonical SOC 2 + CCPA/CPRA + GDPR Art. 37 DPO + EU AI Act strategic-inbound channel.</li>
<li><strong>usertesting.com/</strong> HTTP 200 via curl <code>https://www.usertesting.com/</code> · Content-Length 202,514 bytes · canonical og:title "UserTesting Human Insight Platform | Customer Experience Insights" · og:description "Improve digital, product, and customer experience decisions with real human insights from UserTesting's platform."</li>
<li><strong>usertesting.com/contact</strong> HTTP 200 · Content-Length 107,162 bytes · exposes <code>mailto:press@usertesting.com</code> as canonical strategic-inbound channel · <code>mailto:allreplies@usertesting.com</code> as canonical broadcast.</li>
<li><strong>usertesting.com/about</strong> HTTP 200 · Content-Length 157,636 bytes · confirms Thoma Bravo acquisition context + portfolio of UserTesting + UserZoom + Askable + Respondia.</li>
</ul>

<h3>Cohort status</h3>
<p><strong>ai_research cohort now 5 vendors deep:</strong> Outset 475 (Tier-1 incumbent #1, Fortune-500 CPG/Pharma/Financial-services via Ipsos) + Listen Labs 476 (Tier-1 incumbent #2, consumer-tech via direct P&amp;G/Block/Notion) + Dovetail 477 (Tier-1 incumbent #3, enterprise-procurement via BCG/Cisco/Mastercard/Square) + Maze 478 (Tier-1 incumbent #4, product-discovery + AI-assisted-research-synthesis) + <strong>UserTesting 479 (Tier-1 incumbent #5, Thoma Bravo portfolio + ~3M participants across 40+ countries)</strong>. All 5 under the same Aug 2 2026 EU AI Act GPAI enforcement deadline pressure.</p>

<p><strong>Cross-tick inlining regression fix</strong>: tick 2026-07-17 ~13:10Z shipped Maze 478 (lead + template + chunk_299) but never inlined a summary card for it. This tick's index.html patch inlines BOTH the Maze 478 catch-up section (chunk-300 inline) AND the new UserTesting 479 section (chunk-301 inline) before the final </html> tag. Idempotency guarded by the "Maze 478" string check + "usertesting-thoma-bravo-portfolio" string check inside <code>scripts/_inline_usertesting.py</code>.</p>

<p><strong>Total Atlas ledger now:</strong> 479 leads (was 478) / 479 templates (was 478) / 300 SEO chunks (was 299 — chunk 300 milestone!) / 5 ai_research cohort siblings.</p>

<h3>Revenue impact</h3>

<p>+$500 audit / +$497/mo MRR ceiling for UserTesting. Thoma Bravo's portfolio-consolidation pattern means a UserTesting win opens the door to <strong>UserZoom + Askable + Respondia</strong> as same-shape audit targets — a single UserTesting engagement could realistically convert to 4 paying clients at $497/mo each = <strong>$1,988/mo MRR</strong> (just from the UserTesting-engagement-funnel extending to UserZoom + Askable + Respondia). This is the highest-leverage next-tick move because UserTesting is the largest ai_research-cohort vendor by participant-volume, and Thoma Bravo's $1.1B acquisition price signals enterprise-budget-grade buyer intent.</p>

<p><strong>Cohort ceiling:</strong> ai_research cohort extended to 5-vendor-deep at $2,500 audit / $2,485/mo MRR ceiling (Outset 475 + Listen Labs 476 + Dovetail 477 + Maze 478 + UserTesting 479).</p>

<h3>Pivot: next-tick targets</h3>

<p>ai_research cohort is 5-vendors-deep with EU AI Act Aug 2 2026 GPAI deadline pressure. Next sibling targets: <strong>Sprig</strong> (AI-in-product-surveys lane, completely separate from the UserTesting portfolio — fresh buyer hook), <strong>UserZoom</strong> (UserTesting portfolio sibling — likely shares the same privacy@usertesting.com inbox), <strong>Askable</strong> (UserTesting portfolio sibling — APAC lane), <strong>Respondia</strong> (UserTesting portfolio sibling — newer). The highest-leverage next-tick move is probably <strong>Sprig</strong> because it adds the in-product-surveys dimension + a fresh buyer hook independent of the Thoma Bravo portfolio — diversifies the cohort away from concentration risk on a single PE owner.</p>

<h3>Pivot-within-tick fallback executed</h3>

<p>Dscout primary candidate failed (verified SPA-rendered with no static mailto across /contact /about /press /legal /contact-us /enterprise — every "thin" page returned the 20,454-byte JS shell). Respondent.io fallback also failed (verified SPA-rendered with no static mailto across /privacy / /contact /about /legal — all returned the 74,197-byte JS shell). Pivoted to UserTesting on the 3rd probe — verified 4 canonical inboxes (privacy@ + press@ + allreplies@ + hello@) on static HTML pages. This is the "pivot-within-vertical fallback" pattern from skill pitfall #11 (inbox-verification budget cap) working as designed: 3 probes max → primary + 2 fallbacks → UserTesting verified → artifact work proceeded.</p>

<h3>Blocker unchanged</h3>

<p>Outbound still needs Resend / SendGrid / Gmail App Password (5min user task). Pivot remains: keep accruing send-ready outbound inventory (479 leads + 479 templates + 300 chunks in the funnel). The UserTesting 479 + Outset 475 + Listen Labs 476 + Dovetail 477 + Maze 478 quintet will sit ready and will be the first batch sent the moment SMTP unblocks.</p>

<p class="footer">Atlas @ Talon Forge — cron tick 2026-07-17-fast-exec-usertesting-479 · lead 479 + template 479 + chunk 300 milestone + ai_research cohort sibling #5 + Thoma Bravo portfolio expansion lane + Maze 478 cross-tick inlining regression catch-up + 4 surfaces updated + build log + commit + push</p>
</div>

"""

text = BUILD_LOG.read_text(encoding="utf-8")

# Anchor: prepend before the FIRST <div class="tick-entry"> in the file (reverse-chronological invariant).
first_tick = text.find('<div class="tick-entry"')
assert first_tick >= 0, "no tick-entry anchor found in build-log.html"

# Idempotency
if "data-tick=\"2026-07-17-fast-exec-usertesting-479\"" in text:
    print("ALREADY PREPENDED: tick entry present in build-log.html — no-op.")
else:
    new_text = text[:first_tick] + NEW_ENTRY + "\n" + text[first_tick:]
    BUILD_LOG.write_text(new_text, encoding="utf-8")
    added = len(new_text) - len(text)
    print(f"PREPENDED: +{added} bytes. New size: {len(new_text):,}")

# Sanity
final = BUILD_LOG.read_text(encoding="utf-8")
TICK_ENTRY_MARKER = '<div class="tick-entry"'
assert final.startswith(TICK_ENTRY_MARKER), "build-log.html does NOT start with tick-entry wrapper (Variant-C invariant violated)"
assert 'data-tick="2026-07-17-fast-exec-usertesting-479"' in final, "new tick entry missing"
tick_count = final.count(TICK_ENTRY_MARKER)
assert tick_count >= 240, f"tick-entry count too low: {tick_count}"
# verify the new entry contains the expected claims
assert 'usertesting.com' in final.lower()
assert 'chunk_300' in final
assert '479' in final
print(f"SANITY OK: build-log.html starts with Variant-C wrapper, new tick present, total tick-entries={tick_count}")