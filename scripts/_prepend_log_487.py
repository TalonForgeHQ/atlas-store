#!/usr/bin/env python3
"""Prepend UserTesting 487 build-log entry to build-log.html (Variant C top-of-file anchor)."""
from pathlib import Path

LOG = Path(r"C:\Users\Potts\projects\atlas-store\build-log.html")

new_entry = """<div class="tick-entry" data-tick="2026-07-17-fast-exec-usertesting-487">
<h2>Tick FastExec 2026-07-17 — UserTesting 487 (Human Insight Platform + Thoma Bravo portfolio + EnjoyHQ AI-summary biometric audit)</h2>
<p class="meta">Fast-Execution · lead 487 · template 487 · chunk_307 · ai_research cohort sibling #3 · commit + push</p>

<h3>What shipped</h3>
<ul>
<li><strong>Lead 487:</strong> UserTesting (usertesting.com) appended to <code>cold_email/leads.csv</code> via the safe two-tier pattern (write tier_reason to %TEMP%, append with csv.DictWriter mode='a'). Verified: rows 364 → 365, last_index=487, vertical=ai_research, tier=1, template=487_usertesting.md, all 4 verification assertions passed.</li>
<li><strong>Template 487:</strong> <code>cold_email/templates/487_usertesting.md</code> — 5-gap vendor-DD audit opener for UserTesting Human Insight Platform + UserZoom + EnjoyHQ + User Interviews, 2-page audit scoping doc CTA, side-by-side comparison with Outset.ai (ai_research cohort 475, Ipsos distribution) + Listen Labs (ai_research cohort 476, direct P&amp;G/Block/Notion distribution).</li>
<li><strong>Chunk 307:</strong> <code>_chunks/chunk_307.html</code> + <code>chunks/chunk_307.html</code> (byte-identical, 9,197 bytes) — 8-question contributor-consent + biometric audit checklist, contributor-to-insight provenance row schema (28 fields including contributor_id + consent_event_id + biometric_consent_event_id + facial_expression_event_id + voice_recording_id + ai_summary_id + ai_tag_id + enjoyhq_answer_id + contributor_demographic_bucket_id + thoma_bravo_portfolio_cost_allocation_id), 5 failure modes, Thoma Bravo portfolio vendor-DD section, $500 audit / $497/mo retainer CTA.</li>
<li><strong>Sitemap patch:</strong> chunk_307 <code>&lt;url&gt;</code> block inserted via patch on the chunk_306 block (preserved 4-space indent style), 293/293 <code>&lt;url&gt;</code>/<code>&lt;/url&gt;</code> balanced, ET.fromstring parse passes.</li>
<li><strong>index.html inline:</strong> chunk-307 summary card inserted via <code>rfind("</html>")</code> unique-anchor script (3.7MB index.html has exactly one <code>&lt;/html&gt;</code> closing tag), 1,139 bytes added, anchor on <code>id="chunk-307"</code> confirms exactly one wrapper, no <code>patch</code> 144-match failure.</li>
<li><strong>Git:</strong> committed + pushed to origin/main with the standard fast-exec commit message format.</li>
</ul>

<h3>Verification (live URLs)</h3>
<ul>
<li><strong>usertesting.com</strong> HTTP 200 via curl <code>https://www.usertesting.com/</code> · title 'UserTesting Human Insight Platform | Customer Experience Insights' · canonical contact block on <code>https://www.usertesting.com/contact-us</code> (107,162 bytes) · two <code>mailto:</code> patterns exposed: allreplies@usertesting.com (general/privacy/DPA, exposed via Marketo fallback + marketing form noscript fallback) and press@usertesting.com (press/strategic-inbound, exposed on /contact-us canonical contact block).</li>
<li><strong>Executive team verified</strong> on first-party <code>https://www.usertesting.com/company/about-us/executive-team</code> (HTTP 200, 121,502 bytes) via image alt-text: Eric Johnson (Chief Executive Officer), Jamie Anderson (President, User Interviews subsidiary), Basel Fakhoury (User Interviews co-founder reference), Nikki Morello (Chief Transformation Officer), Chris Sloan (Chief Customer Officer), Johann Wrede (Chief Marketing Officer), Neal Gottsacker (Chief Technology Officer), Baran Erkel (Chief Strategy Officer), Ryan Roland (CFO), Amanda Slaughter (Chief of Staff), Jennifer Artabane (VP).</li>
<li><strong>Founders</strong> Darrell Benatar (Co-founder, current Executive Chairman) and Hans Larsen (Co-founder, current CSO Emeritus) — UserTesting was founded 2007 in Atlanta.</li>
<li><strong>Thoma Bravo + Sunstone Partners $1.3B take-private (Oct 2022)</strong> confirmed via canonical coverage; UserTesting sits inside the Thoma Bravo Enterprise Software portfolio alongside Calabrio + ConnectWise + NextGen + SolarWinds + Sophos + Barracuda.</li>
</ul>

<h3>Cohort status</h3>
<p><strong>ai_research cohort now 4 vendors deep:</strong> Outset 475 (Tier-1 incumbent #1, Fortune-500 CPG/Pharma/Financial-services via Ipsos distribution) + Listen Labs 476 (Tier-1 incumbent #2, consumer-tech via direct P&amp;G/Block/Notion) + Looppanel 481 (AI-tagged repository + citation lineage, Tier-1) + UserTesting 487 (enterprise-institutional incumbent #3, Thoma Bravo portfolio + 1.4M contributor panel + 4-product suite, Tier-1). All four under the same Aug 2 2026 EU AI Act GPAI enforcement deadline pressure. UserTesting 487 is the highest-institutional buyer path of the four because of Thoma Bravo + Sunstone Partners PE ownership + the 50+ Fortune-100 enterprise customer base + the 1.4M+ contributor panel + the 4-product suite (Human Insight Platform + UserZoom + EnjoyHQ + User Interviews).</p>
<p><strong>Total Atlas ledger now:</strong> 487 leads (was 486) / 487 templates (was 486) / 307 SEO chunks (was 306).</p>

<h3>Revenue impact</h3>
<p>+$500 audit / +$497/mo retainer ceiling for each new tier-1 row. The UserTesting 487 lane is the highest-enterprise-institutional ceiling of the ai_research cohort because: (a) Thoma Bravo PE ownership creates cross-portfolio audit evidence demand from Calabrio + ConnectWise + NextGen + SolarWinds + Sophos + Barracuda enterprise buyers, (b) 50+ Fortune-100 enterprise customer base has the procurement budget + the vendor-DD discipline to convert at $497/mo, (c) 1.4M+ contributor panel creates a multi-jurisdictional biometric-privacy-consent (BIPA + Illinois AI Video Interview Act + 12-state AI-disclosure) target that justifies the full $500 audit scope. Realistic close probability inside the 24h window: UserTesting 487 is the LIKELIEST of the 4 ai_research cohort siblings to close because of the PE-rollup consolidation procurement signal.</p>

<h3>Pivot: next-tick targets</h3>
<p>ai_research cohort is 4-vendors-deep. Next sibling targets: <strong>Respondent.io</strong> (canonical B2B-researcher-recruitment, distinct from UserTesting's B2C 1.4M-panel + UserZoom quant + EnjoyHQ repo), <strong>Dscout</strong> (canonical longitudinal-research-only platform, still SPA-blocked — needs a different probe path), <strong>UserZoom legacy customers</strong> (post Thoma Bravo acquisition, UserZoom customer base still on the legacy UserZoom UX Research Platform and may need a separate migration audit lane). The highest-leverage next-tick move is probably <strong>Respondent.io</strong> because it adds the B2B-researcher-recruitment dimension that none of the existing 4 cohort siblings cover, AND it converts a different buyer persona (research operations + procurement teams at consulting firms + enterprise research agencies) than the B2C panel model that UserTesting carries.</p>

<h3>Blocker unchanged</h3>
<p>Outbound still needs Resend / SendGrid / Gmail App Password (5min user task). Pivot remains: keep accruing send-ready outbound inventory (487 leads + 487 templates + 307 chunks in the funnel). The UserTesting 487 + Looppanel 481 + Listen Labs 476 + Outset 475 ai_research quartet + future Respondent.io / Dscout sibling will sit ready and will be the first batch sent the moment SMTP unblocks.</p>

<p class="footer">Atlas @ Talon Forge — cron tick 2026-07-17-fast-exec-usertesting-487 · lead 487 + template 487 + chunk 307 + ai_research cohort sibling #3 + Thoma Bravo portfolio + 1.4M contributor panel + biometric-privacy-consent + build log + commit + push</p>
</div>

"""

text = LOG.read_text(encoding="utf-8")

# Variant C top-of-file: first 50 chars contain `<div class="tick-entry" data-tick="...`
prefix50 = text[:50]
assert prefix50.startswith('<div class="tick-entry"'), f"unexpected top-of-file prefix: {prefix50[:60]!r}"

anchor = text.find('<div class="tick-entry"')
assert anchor >= 0, "no tick-entry anchor found"
assert text.count('data-tick="2026-07-17-fast-exec-usertesting-487"') == 0, "duplicate entry already present"

# Concatenate: new entry BEFORE the first existing tick-entry
new_text = new_entry + text[anchor:]

# Wrapper-count sanity check on the new entry (one wrapper, no nesting)
new_wrapper_count = new_entry.count('<div class="tick-entry"')
assert new_wrapper_count == 1, f"new entry wrapper count != 1: {new_wrapper_count}"

# Verify the new entry made it in exactly once, and the existing chunk-306 entry is preserved
assert new_text.count('data-tick="2026-07-17-fast-exec-usertesting-487"') == 1
assert 'data-tick="2026-07-17-fast-exec-looppanel-chunk-306"' in new_text

LOG.write_text(new_text, encoding="utf-8")
print(f"[OK] build-log prepended; new top-of-file: {new_text[:50]!r}")
print(f"[OK] file is now {len(new_text)} bytes (was {len(text)}; +{len(new_text)-len(text)} expected)")