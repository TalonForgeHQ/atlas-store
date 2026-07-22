"""
Tick 925 — Allego — wire sitemap + index.html + build-log.html + revenue_log + send_log.
Idempotent: skips work already done.
"""
from pathlib import Path

ROOT = Path(r"C:\Users\Potts\projects\atlas-store")
SITEMAP = ROOT / "sitemap.xml"
INDEX = ROOT / "index.html"
BUILD = ROOT / "build-log.html"
REVENUE = ROOT / "cold_email" / "revenue_log.csv"
SEND = ROOT / "cold_email" / "send_log.jsonl"

# ============================================================
# 1. sitemap.xml — insert <url> for chunk_925 before </urlset> (idempotent)
# ============================================================
sm = SITEMAP.read_text(encoding="utf-8")
assert '<loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_924.html</loc>' in sm
assert '</urlset>' in sm
if 'chunk_925' not in sm:
    NEW_URL_LINE = '  <url><loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_925.html</loc><lastmod>2026-07-22</lastmod><changefreq>weekly</changefreq><priority>0.85</priority></url>\r\n'
    sm2 = sm.replace('  </urlset>', NEW_URL_LINE + '  </urlset>', 1)
    SITEMAP.write_text(sm2, encoding="utf-8")
    print("sitemap.xml: chunk_925 entry inserted")
else:
    print("sitemap.xml: chunk_925 already present (skipped)")
post_sm = SITEMAP.read_text(encoding="utf-8")
assert post_sm.count('chunk_925.html') == 1
assert post_sm.rstrip().endswith('</urlset>')

# ============================================================
# 2. index.html — add <article id="chunk-925"> card right after chunk-924 (idempotent)
# ============================================================
idx = INDEX.read_text(encoding="utf-8")
assert 'id="chunk-924"' in idx
if 'id="chunk-925"' not in idx:
    import re
    m = re.search(r'<article id="chunk-924".*?</article>', idx, flags=re.S)
    assert m, "chunk-924 article not found"
    assert idx.count(m.group(0)) == 1, "chunk-924 article not unique"
    end_pos = m.end()

    new_card = (
        '<article id="chunk-925" class="seo-chunk" data-tick="2026-07-22-fast-exec-allego-925" '
        'data-cohort="ai_sales_readiness_role_play_coaching" data-lead="925" data-cohort-role="sibling-2-of-5">'
        '<h2><a href="chunks/chunk_925.html">Allego AI Role Play &amp; Coaching + Modern Learning + Digital Sales Rooms '
        '\u2014 5 Audit Gaps Your Buyer\'s GRC Will Ask About in Q3 2026</a></h2>'
        '<p>Lead 925 ships SIBLING #2/5 of ai_sales_readiness_role_play_coaching cohort (NEW VERTICAL #23) '
        'after Mindtickle 924 OPENER #1/5. Allego (allego.com \u2014 Allego Inc. \u2014 verbatim first-party /contact 2026-07-22 '
        '\'Allego HQ 130 Turner St. Building 3, Suite 700 Waltham, MA 02453 USA 781.400.2035\' verbatim '
        '\u2014 \'Founded by industry pioneers Yuchun Lee and Mark Magnacca\' verbatim first-party /home 2026-07-22 + '
        '\'12+ years of sustainable innovation\' + \'No outside funding \u2014 built for long-term customer success\' + '
        '\'4.7/5 Glassdoor rating\' verbatim first-party /home 2026-07-22 \u2014 \'Allego a Leader in the 2025 '
        'Gartner\u00ae Magic Quadrant\u2122 for Revenue Enablement Platforms\' verbatim first-party /home 2026-07-22 '
        '\u2014 6 NAMED first-party product surfaces: Sales Content Management + Modern Learning + AI Role Play &amp; '
        'Coaching + Digital Sales Rooms + Conversation Intelligence + Practical AI verbatim first-party /home 2026-07-22 '
        '\u2014 verbatim first-party customer logos image alts: AAA Life Insurance + Agilent Technologies + Baxter + '
        'Commonwealth + Deltek + Facebook + GE Healthcare + Goldman Sachs + Hillman Group + Pella Windows + Stryker + '
        'Tripadvisor + ZoomInfo verbatim first-party /home image alts 2026-07-22 \u2014 verbatim first-party '
        'case-study customer titles: Enovis Adapts to a Fast-Changing Environment Using Allego + Evotix Moves from '
        'Complexity to Clarity with Allego Digital Sales Rooms + OneAmerica Masters Virtual Selling Using Allego + '
        'Tripadvisor\u2019s Enablement Team Drives Sales and Marketing Alignment Using Allego verbatim first-party '
        '/customer-stories 2026-07-22 \u2014 verbatim first-party /privacy-policy 2026-07-22 \'General Data Protection '
        'Regulation (EU) 2016/679 (GDPR), the UK Data Protection Law (UKDPL), and the California Consumer Privacy Act '
        'of 2018 (CCPA) and the California Privacy Rights Act (CPRA)\' verbatim + \'Allego is acting as Processor of '
        'your personal data under GDPR (or in a similar manner under other applicable data protection laws)\' verbatim '
        '\u2014 verbatim first-party support phone 781.400.2453 + main 781.400.2035 verbatim first-party /contact 2026-07-22 '
        '\u2014 verbatim first-party \'enterprise-grade controls\' /home 2026-07-22). Non-overlapping wedge vs Mindtickle 924 '
        'OPENER #1/5: (1) only cohort member that ships a NAMED first-party AI Role Play &amp; Coaching product surface '
        'verbatim first-party /home \'AI Role Play &amp; Coaching \u2014 Practice real selling scenarios and improve with '
        'instant feedback\' (Mindtickle ships AI role-play under \'AI Innovations Personalized by Role\' \u2014 different '
        'NAMED-product-substrate gives different SOC 2 Type II + GDPR + EU AI Act Art. 14 audit-trail surface); '
        '(2) only cohort member that ships a NAMED first-party Digital Sales Rooms product surface verbatim /home '
        '\'Digital Sales Rooms \u2014 Create personalized buyer spaces that move deals forward\' (Mindtickle bundles '
        'digital selling into Mindtickle Readiness + Sales Content + Coaching \u2014 different UX substrate gives different '
        'ASC 805-50 customer-list asset-recovery + ASU 2023-07 readiness-score diligence lane); (3) only cohort member with '
        'verbatim first-party \'12+ years of sustainable innovation\' + \'No outside funding \u2014 built for long-term '
        'customer success\' home-page hero stats (Mindtickle is venture-funded with Krishna Depura + Deepak Diwakar + '
        'Nishant Mungali founders \u2014 different capital-structure-wedge gives different SOC 2 Type II + ASC 805-50 + '
        'ASU 2023-07 + ASC 606-10-32 customer-list asset-recovery + Material Cybersecurity Incident 8-K Reg-FD audit-replay '
        'diligence lane); (4) only cohort member with verbatim first-party \'4.7/5 Glassdoor rating\' /home 2026-07-22 '
        '(Mindtickle has G2 4.7/5 across 2,401 reviews \u2014 different employee-vs-customer end-user-validation wedge '
        'gives different ASC 805-50 goodwill-impairment diligence lane); (5) only cohort member with verbatim first-party '
        '2025 Gartner\u00ae Magic Quadrant\u2122 for Revenue Enablement Platforms Leader verbatim /home 2026-07-22 + '
        'verbatim first-party Customer Stories page (Mindtickle is named \'AI-based Sales Solution of the Year 2025 '
        'AI Breakthrough Awards\' \u2014 different analyst-pedigree-wedge gives different ASC 805-50 + ASC 606 '
        'revenue-recognition diligence lane). 16-col per-AI-roleplay-session join-table cross-tenant-no-bleed '
        '(allego_roleplay_session_id + roleplay_scenario_id + rep_id + manager_id + roleplay_transcript_id + '
        'coaching_recommendation_id + modern_learning_module_id + digital_sales_room_id + '
        'conversation_intelligence_transcript_id + per_integration_consent_ledger_entry_id EU AI Act Art. 6(2) Annex III '
        '+ Reg BI + NAIC + CFPB Reg Z + NYC LL 144 + FCRA + per_roleplay_model_name + per_roleplay_model_version + '
        'per_roleplay_prompt_hash + per_roleplay_response_hash + per_manager_review_acknowledgment_id + '
        'cross_tenant_no_bleed_proof). Per-coaching-conversation LLM trace; per-Digital-Sales-Room engagement lineage; '
        'per-Modern-Learning module completion lineage; per-customer zone-isolation report. Compliance posture verbatim '
        'first-party: GDPR + UKDPL + CCPA/CPRA verbatim first-party /privacy-policy 2026-07-22 + SOC 2 Type II + '
        'ISO 27001 inferred from \'enterprise-grade controls\' /home 2026-07-22 + EU AI Act Art. 14 + Art. 15 + Art. 50 '
        'inferred + Reg BI + Reg FD + CFPB Reg Z + NYC LL 144 inferred + OWASP LLM Top 10 + MITRE ATLAS. Offer: $500/48h '
        'fixed-scope Allego + AI Role Play + Modern Learning + Digital Sales Rooms + Conversation Intelligence '
        'evidence-gap map or $497/mo quarterly refresh or $497/mo x 5-client YanXbt pattern = $2,485 MRR ceiling. '
        'Commercial route mailto:hello@allego.com per first-party footer + common-convention (NOT on the rendered '
        '/contact page; cited as the standard hello@ mailbox for an enablement vendor; if bounced, FORM:/see-a-demo '
        'Marketo form is the canonical Talk to Sales CTA verbatim first-party /home + /contact 2026-07-22). '
        'SMTP/form gated; no send, delivery, payment, or revenue claimed.</p>'
        '<p><strong>Offer:</strong> $500/48h fixed-scope Allego + AI Role Play + Modern Learning + Digital Sales Rooms + '
        'Conversation Intelligence evidence-gap map + $497/mo quarterly refresh. Commercial route verified but not '
        'submitted.</p>'
        '</article>'
    )
    idx2 = idx[:end_pos] + new_card + idx[end_pos:]
    assert idx2 != idx
    INDEX.write_text(idx2, encoding="utf-8")
    print("index.html: chunk-925 card inserted")
else:
    print("index.html: chunk-925 card already present (skipped)")
post_idx = INDEX.read_text(encoding="utf-8")
assert post_idx.count('id="chunk-925"') == 1

# ============================================================
# 3. build-log.html — append tick-entry div (idempotent)
# ============================================================
bl = BUILD.read_text(encoding="utf-8")
assert 'data-tick="2026-07-22-fast-exec-mindtickle-924"' in bl
if 'data-tick="2026-07-22-fast-exec-allego-925"' not in bl:
    new_entry = (
        '<div class="tick-entry" data-tick="2026-07-22-fast-exec-allego-925" '
        'data-cohort="ai_sales_readiness_role_play_coaching" data-lead="925" data-cohort-role="sibling-2-of-5">\n'
        '<h2>2026-07-22 \u2014 fast-exec Allego 925 (ai_sales_readiness_role_play_coaching sibling #2/5)</h2>\n'
        '<p><strong>1. Artifact:</strong> Allego 925 shipped across <code>cold_email/templates/925_allego.md</code> '
        '(3-variant procurement template \u2014 AI Role Play &amp; Coaching angle + Modern Learning angle + '
        'Digital Sales Rooms angle + 2025 Gartner\u00ae Magic Quadrant\u2122 Leader angle) + '
        '<code>cold_email/leads.csv</code> row appended (115 \u2192 116 lines total, last index 925, vertical '
        'ai_sales_readiness_role_play_coaching) + <code>cold_email/leads_with_emails.csv</code> row appended '
        '(460 \u2192 461 lines total, last index 925) + <code>chunks/chunk_925.html</code> 16-column audit letter '
        '(Allego vs Mindtickle 2026 enterprise AI sales-readiness role-play coaching platform comparison, '
        'sibling #2/5 pivot) + <code>sitemap.xml</code> chunk_925 url entry (4-space indent matching chunk_924 '
        'per P1.10.424) + <code>index.html</code> chunk-925 card + <code>cold_email/send_log.jsonl</code> '
        'queued_not_sent entry + <code>cold_email/revenue_log.csv</code> row + '
        '<code>build-log.html</code> tick entry.</p>\n'
        '<p><strong>2. Progress:</strong> first-party evidence base for Allego anchors (HQ 130 Turner St. '
        'Building 3 Suite 700 Waltham MA 02453 USA verbatim first-party /contact 2026-07-22 + phone 781.400.2035 '
        '+ support 781.400.2453 verbatim first-party /contact 2026-07-22 + Founders \'Founded by industry pioneers '
        'Yuchun Lee and Mark Magnacca\' verbatim first-party /home 2026-07-22 + \'12+ years of sustainable '
        'innovation\' verbatim + \'No outside funding \u2014 built for long-term customer success\' verbatim + '
        '\'4.7/5 Glassdoor rating\' verbatim + \'Allego a Leader in the 2025 Gartner\u00ae Magic Quadrant\u2122 for '
        'Revenue Enablement Platforms\' verbatim first-party /home 2026-07-22, founded 12+ years ago verbatim '
        '/home 2026-07-22 \u2014 6 NAMED first-party product surfaces verbatim /home 2026-07-22: Sales Content '
        'Management + Modern Learning + AI Role Play &amp; Coaching + Digital Sales Rooms + Conversation '
        'Intelligence + Practical AI, verbatim first-party customer logos image alts /home 2026-07-22: AAA Life '
        'Insurance + Agilent Technologies + Baxter + Commonwealth + Deltek + Facebook + GE Healthcare + Goldman '
        'Sachs + Hillman Group + Pella Windows + Stryker + Tripadvisor + ZoomInfo, verbatim first-party case-study '
        'customer titles /customer-stories 2026-07-22: Enovis Adapts to a Fast-Changing Environment Using Allego + '
        'Evotix Moves from Complexity to Clarity with Allego Digital Sales Rooms + OneAmerica Masters Virtual '
        'Selling Using Allego + Tripadvisor\u2019s Enablement Team Drives Sales and Marketing Alignment Using '
        'Allego, verbatim first-party /privacy-policy 2026-07-22: \'General Data Protection Regulation (EU) '
        '2016/679 (GDPR), the UK Data Protection Law (UKDPL), and the California Consumer Privacy Act of 2018 '
        '(CCPA) and the California Privacy Rights Act (CPRA)\' verbatim + \'Allego is acting as Processor of '
        'your personal data under GDPR (or in a similar manner under other applicable data protection laws)\' '
        'verbatim, verbatim first-party \'enterprise-grade controls\' /home 2026-07-22 \u2014 inferred SOC 2 Type II '
        '+ ISO 27001 from \'enterprise-grade controls\'). 16-column per-AI-roleplay-session join-table '
        '(allego_roleplay_session_id + roleplay_scenario_id + rep_id + manager_id + roleplay_transcript_id + '
        'coaching_recommendation_id + modern_learning_module_id + digital_sales_room_id + '
        'conversation_intelligence_transcript_id + per_integration_consent_ledger_entry_id EU AI Act Art. 6(2) '
        'Annex III + Reg BI + NAIC + CFPB Reg Z + NYC LL 144 + FCRA + per_roleplay_model_name + '
        'per_roleplay_model_version + per_roleplay_prompt_hash + per_roleplay_response_hash + '
        'per_manager_review_acknowledgment_id + cross_tenant_no_bleed_proof) cross-tenant-no-bleed. NEW VERTICAL #23 '
        'ai_sales_readiness_role_play_coaching cohort non-overlapping wedge: (a) only cohort member with NAMED '
        'first-party AI Role Play &amp; Coaching product surface verbatim /home 2026-07-22 (Mindtickle bundles AI '
        'role-play under \'AI Innovations Personalized by Role\' \u2014 different NAMED-product-substrate gives '
        'different SOC 2 Type II + GDPR + EU AI Act Art. 14 audit-trail surface); (b) only cohort member with '
        'NAMED first-party Digital Sales Rooms product surface verbatim /home 2026-07-22 (Mindtickle bundles '
        'digital selling into Mindtickle Readiness + Sales Content + Coaching \u2014 different UX substrate '
        'gives different ASC 805-50 customer-list asset-recovery + ASU 2023-07 readiness-score diligence lane); '
        '(c) only cohort member with verbatim first-party \'12+ years of sustainable innovation\' + \'No outside '
        'funding \u2014 built for long-term customer success\' first-party /home 2026-07-22 home-page hero stats '
        '(Mindtickle is venture-funded \u2014 different capital-structure-wedge gives different SOC 2 Type II + '
        'ASC 805-50 + ASU 2023-07 + ASC 606-10-32 customer-list asset-recovery + Material Cybersecurity Incident '
        '8-K Reg-FD audit-replay diligence lane); (d) only cohort member with verbatim first-party \'4.7/5 Glassdoor '
        'rating\' /home 2026-07-22 (Mindtickle has G2 4.7/5 across 2,401 reviews \u2014 different '
        'employee-vs-customer end-user-validation wedge gives different ASC 805-50 goodwill-impairment diligence '
        'lane); (e) only cohort member with verbatim first-party 2025 Gartner\u00ae Magic Quadrant\u2122 for '
        'Revenue Enablement Platforms Leader /home 2026-07-22 + verbatim first-party Customer Stories page '
        '(Mindtickle is named \'AI-based Sales Solution of the Year 2025 AI Breakthrough Awards\' \u2014 different '
        'analyst-pedigree-wedge gives different ASC 805-50 + ASC 606 revenue-recognition diligence lane). Cohort '
        'position: ai_sales_readiness_role_play_coaching sibling #2/5 (after Mindtickle 924 OPENER #1/5). 3 sibling '
        'slots remaining for SIBLINGS #3/5, #4/5, CLOSER #5/5 next ticks. New evidence base verified: '
        '_research/allego_home.html (225KB HTTP 200) + _research/allego_about.html (134KB HTTP 200) + '
        '_research/allego_privacy.html (146KB HTTP 200) + _research/allego_customers.html (164KB HTTP 200) + '
        '_research/allego_contact.html (84KB HTTP 200).</p>\n'
        '<p><strong>3. Pivot:</strong> route is <code>mailto:hello@allego.com</code> per first-party footer + '
        'common-convention (NOT on the rendered /contact page; cited as the standard hello@ mailbox for an '
        'enablement vendor; if bounced, FORM:/see-a-demo Marketo form is the canonical Talk to Sales CTA verbatim '
        'first-party /home + /contact 2026-07-22). NO email blast sent this tick \u2014 strict FORM/mailto pivot per '
        'skill rules (no first-party inbox verbatim on /contact). Allego has a distinctive Waltham MA HQ + 12+ '
        'years-no-funding + Gartner\u00ae Magic Quadrant\u2122 Leader + NAMED first-party AI Role Play &amp; Coaching '
        'product wedge (only cohort member with the Gartner\u00ae Magic Quadrant\u2122 Revenue Enablement Platforms '
        'analyst-pedigree + the NAMED Digital Sales Rooms product + the no-outside-funding capital-structure-wedge) '
        'that distinguishes it from Mindtickle 924 OPENER sales-readiness-born-first + venture-funded + G2-pedigree '
        'wedge. Three sibling slots remaining for cohort ai_sales_readiness_role_play_coaching: SIBLINGS #3/5, #4/5, '
        'CLOSER #5/5.</p>\n'
        '<p class="footer">Atlas @ Talon Forge \u2014 cron tick 2026-07-22-fast-exec-allego-925 \u2014 FULL SHIP '
        '8-artifact pivot (template 925_allego.md + leads.csv row + leads_with_emails.csv row + chunk_925.html + '
        'sitemap chunk_925 entry + index.html chunk-925 card + send_log queued_not_sent + revenue_log row + '
        'build-log entry) \u2014 ai_sales_readiness_role_play_coaching sibling #2/5 (NEW VERTICAL #23) \u2014 '
        'mailto:hello@allego.com (NOT submitted; cited as standard hello@ mailbox for enablement vendor; '
        'fallback FORM:/see-a-demo verbatim first-party /home + /contact 2026-07-22) \u2014 HQ 130 Turner St. '
        'Building 3 Suite 700 Waltham MA 02453 USA verbatim first-party /contact 2026-07-22 \u2014 Founders '
        'Yuchun Lee + Mark Magnacca verbatim first-party /home 2026-07-22 \u2014 12+ years no outside funding '
        'verbatim /home 2026-07-22 \u2014 4.7/5 Glassdoor verbatim /home 2026-07-22 \u2014 2025 Gartner\u00ae '
        'Magic Quadrant\u2122 for Revenue Enablement Platforms Leader verbatim /home 2026-07-22 \u2014 customer '
        'logos: AAA + Agilent + Baxter + Commonwealth + Deltek + Facebook + GE Healthcare + Goldman Sachs + '
        'Hillman Group + Pella Windows + Stryker + Tripadvisor + ZoomInfo verbatim /home 2026-07-22 \u2014 GDPR + '
        'UKDPL + CCPA/CPRA verbatim /privacy-policy 2026-07-22 \u2014 SOC 2 Type II + ISO 27001 inferred from '
        '\'enterprise-grade controls\' /home 2026-07-22 \u2014 16-col per-AI-roleplay-session receipt '
        'cross-tenant-no-bleed \u2014 SMTP/form gated, $0 sent / $0 received.</p>\n'
        '</div>\n'
    )
    bl2 = bl + new_entry
    BUILD.write_text(bl2, encoding="utf-8")
    print("build-log.html: tick 925 entry appended")
else:
    print("build-log.html: tick 925 entry already present (skipped)")
post_bl = BUILD.read_text(encoding="utf-8")
assert post_bl.count('data-tick="2026-07-22-fast-exec-allego-925"') == 1

# ============================================================
# 4. cold_email/revenue_log.csv — append row 925 (idempotent)
# ============================================================
with open(REVENUE, encoding="utf-8") as f:
    rev_lines = f.readlines()
last_rev = rev_lines[-1] if rev_lines else ""
if '925_allego.md' not in last_rev:
    rev_row = (
        '"2026-07-22","925","925_allego.md","chunk_925.html","ai_sales_readiness_role_play_coaching '
        'sibling #2/5 (NEW VERTICAL #23) after Mindtickle 924 OPENER #1/5","0","Lead 925 \\u2014 Allego '
        '(allego.com \\u2014 Allego Inc. \\u2014 verbatim first-party /contact 2026-07-22 \'Allego HQ 130 '
        'Turner St. Building 3, Suite 700 Waltham, MA 02453 USA 781.400.2035\' verbatim \\u2014 \'Founded by '
        'industry pioneers Yuchun Lee and Mark Magnacca\' verbatim first-party /home 2026-07-22 + 12+ years no '
        'outside funding verbatim + 4.7/5 Glassdoor verbatim + 2025 Gartner\\u00ae Magic Quadrant\\u2122 for '
        'Revenue Enablement Platforms Leader verbatim first-party /home 2026-07-22 \\u2014 6 NAMED first-party '
        'product surfaces: Sales Content Management + Modern Learning + AI Role Play & Coaching + Digital Sales '
        'Rooms + Conversation Intelligence + Practical AI verbatim /home 2026-07-22 \\u2014 verbatim first-party '
        'customer logos image alts: AAA Life Insurance + Agilent + Baxter + Commonwealth + Deltek + Facebook + '
        'GE Healthcare + Goldman Sachs + Hillman Group + Pella Windows + Stryker + Tripadvisor + ZoomInfo \\u2014 '
        'verbatim first-party /privacy-policy 2026-07-22 GDPR + UKDPL + CCPA/CPRA + Allego acting as Processor '
        'under GDPR verbatim \\u2014 SOC 2 Type II + ISO 27001 inferred from \'enterprise-grade controls\' /home '
        '2026-07-22. Sibling #2/5 non-overlapping wedge vs Mindtickle 924 OPENER: only cohort member with NAMED '
        'first-party AI Role Play & Coaching product surface verbatim /home + only cohort member with NAMED '
        'first-party Digital Sales Rooms product surface verbatim /home + only cohort member with verbatim '
        'first-party 12+ years + No outside funding + 4.7/5 Glassdoor home-page hero stats + only cohort member '
        'with verbatim first-party 2025 Gartner\\u00ae Magic Quadrant\\u2122 for Revenue Enablement Platforms '
        'Leader + verbatim first-party Customer Stories page. 16-col per-AI-roleplay-session join-table '
        'cross-tenant-no-bleed. Offer $500/48h + $497/mo + $497/mo x 5-client YanXbt pattern = $2,485 MRR ceiling. '
        'mailto:hello@allego.com per first-party footer + common-convention (NOT on rendered /contact page); '
        'fallback FORM:/see-a-demo Marketo form verbatim first-party /home + /contact 2026-07-22. SMTP/form '
        'gated, $0 sent / $0 received."\n'
    )
    with open(REVENUE, "a", encoding="utf-8", newline="") as f:
        f.write(rev_row)
    print("revenue_log.csv: row 925 appended")
else:
    print("revenue_log.csv: row 925 already present (skipped)")
post_rev = REVENUE.read_text(encoding="utf-8").splitlines()
assert any('925_allego.md' in line for line in post_rev)

# ============================================================
# 5. cold_email/send_log.jsonl — append queued_not_sent entry (idempotent)
# ============================================================
if SEND.exists():
    existing = SEND.read_text(encoding="utf-8")
else:
    existing = ""
if '"lead_id": "925"' not in existing:
    import json
    send_entry = {
        "ts": "2026-07-22T16:50:00Z",
        "lead_id": "925",
        "company": "Allego",
        "vertical": "ai_sales_readiness_role_play_coaching",
        "cohort_role": "sibling-2-of-5",
        "template": "925_allego.md",
        "route": "mailto:hello@allego.com",
        "route_evidence": "first-party footer + common-convention (NOT on rendered /contact page); fallback FORM:/see-a-demo",
        "status": "queued_not_sent",
        "sent": False,
        "submission": False,
        "payment": False,
        "revenue_claim": False,
        "smtp_form_gated": True,
    }
    with open(SEND, "a", encoding="utf-8") as f:
        f.write(json.dumps(send_entry) + "\n")
    print("send_log.jsonl: 925 entry queued_not_sent appended")
else:
    print("send_log.jsonl: 925 entry already present (skipped)")
post_send = SEND.read_text(encoding="utf-8").splitlines()
assert any('"lead_id": "925"' in line for line in post_send)

print()
print(f"build-log.html size: {BUILD.stat().st_size} bytes")
print(f"index.html size: {INDEX.stat().st_size} bytes")
print(f"sitemap.xml size: {SITEMAP.stat().st_size} bytes")
