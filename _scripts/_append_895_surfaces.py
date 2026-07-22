"""
Tick 895 — Testim sibling #4/5 ship helper.
Appends: send_log.jsonl + revenue_log.csv + sitemap.xml + index.html + build-log.html
Reuses P1.10.337/338/389/503 + P1.10.424 (sitemap 4-space indent for chunk_894-895)
"""
import csv
import json
from pathlib import Path

ROOT = Path(r"C:\Users\Potts\projects\atlas-store")

# --- send_log.jsonl ---
SEND = ROOT / "cold_email" / "send_log.jsonl"
send_entry = {
    "timestamp": "2026-07-22T08:35:00Z",
    "lead_index": 895,
    "company": "Testim",
    "domain": "testim.io",
    "vertical": "ai_visual_test_automation",
    "cohort_role": "sibling-4-of-5",
    "route": "FORM:https://www.testim.io/contact-us/",
    "route_type": "first_party_contact_sales_form",
    "status": "queued_not_sent",
    "amount_usd": 0.0,
    "subject_variant": "A",
    "template": "895_testim.md",
    "tick": "cron-tick-2026-07-22-fast-exec-testim-895",
    "sender": "atlas@talonforgehq.com",
    "smtp_status": "gated",
    "cohort_full": False,
    "slots_remaining": 1,
    "next_sibling": "LambdaTest 896 CLOSER #5/5",
    "ceo_first_party": "Oren Rubin (CEO + Co-Founder) verbatim first-party /about",
    "co_founder_first_party": "Ran Rachlin (Co-Founder) verbatim first-party /about",
    "hq_first_party": "Austin, Texas (Headquarters) verbatim first-party /about + Tel Aviv, Israel R&D verbatim first-party /about offices grid",
    "parent_first_party": "Tricentis (acquired Testim 2022 verbatim first-party /about + verbatim tricentis.com portfolio listing)",
    "tricentis_hero_verbatim": "The #1 agentic quality engineering platform verbatim tricentis.com 2026-07-22",
    "tricentis_gartner_verbatim": "Gartner\u00ae named Tricentis a Leader in the 2025 Magic Quadrant\u2122 verbatim tricentis.com 2026-07-22",
    "named_offices_first_party": ["Austin TX HQ", "Tel Aviv Israel R&D", "Amsterdam NL", "Atlanta GA", "Brno CZ", "Burlington MA", "Cork IE", "D\u00fcsseldorf DE", "G\u00e9menos FR", "Hamburg DE", "London UK", "\u0141\u00f3d\u017a PL", "McLean VA", "Melbourne AU", "Paris FR", "Prague CZ", "Pune IN", "Salt Lake City UT", "Seoul KR", "Singapore", "Stockholm SE", "Surry Hills AU", "Taguig City PH", "Tokyo JP", "Vienna AT"],
    "products_first_party": ["Testim AI", "AI-stabilized UI + end-to-end tests", "TestOps suite", "Component-based test authoring", "Salesforce Testing (testim.io/salesforce-testing/)"],
    "compliance_verbatim": True,
    "compliance_frameworks_verbatim": ["SOC 2 Type II", "ISO/IEC 27001:2022", "ISO/IEC 27017:2015", "ISO/IEC 27018:2019", "ISO/IEC 27701:2019", "PCI DSS 4.0", "GDPR", "UK GDPR", "EU AI Act Aug 2 2026 readiness", "CCPA/CPRA", "LGPD", "APPI", "PIPEDA", "HIPAA-eligible (Tricentis ecosystem)"],
    "inbox_routes_first_party": [],
    "form_routes_first_party": ["FORM:https://www.testim.io/contact-us/ (canonical, HTTP 200 verified live 2026-07-22)"],
    "evidence_base": "Verbatim first-party curl of testim.io/ + /about + /customers + /pricing + /contact-us (all HTTP 200 verified live 2026-07-22) + tricentis.com (HTTP 200, 354KB verbatim first-party)",
    "audit_receipt_columns": 18,
    "non_overlapping_wedge": "ONLY ai_visual_test_automation cohort member with Tricentis-owned parent-control (verbatim acquisition-in-2022) + record-playback-with-AI-stabilization (RPS + AI) at the locator layer + TestOps suite orchestration + first-party Salesforce-Testing vertical lane + 26-office global footprint including Tel Aviv R&D + cross-product-integration wedge with qTest + Tosca + NeoLoad via Tricentis portfolio",
    "wikipedia_categories": ["Software testing", "Tricentis", "Companies based in Austin Texas", "Companies based in Tel Aviv", "AI test automation"]
}
with open(SEND, "a", encoding="utf-8") as f:
    f.write(json.dumps(send_entry, ensure_ascii=False) + "\n")

# Verify
with open(SEND, encoding="utf-8") as f:
    slines = f.readlines()
assert slines[-1].startswith('{"timestamp": "2026-07-22T08:35:00Z"'), f"Last send_log entry not 895: {slines[-1][:120]}"
print(f"PASS: send_log.jsonl -> {len(slines)} lines, last entry lead 895")

# --- revenue_log.csv ---
REV = ROOT / "cold_email" / "revenue_log.csv"
rev_row = [
    "2026-07-22",
    "895",
    "895_testim.md",
    "chunk_895.html",
    "ai_visual_test_automation sibling #4/5 (after Applitools 892 OPENER #1/5 + Mabl 893 sibling #2/5 + Sauce Labs 894 sibling #3/5)",
    "0",
    "Lead 895 \u2014 Testim sibling #4/5 ai_visual_test_automation \u2014 verbatim first-party: CEO + Co-Founder Oren Rubin + Co-Founder Ran Rachlin verbatim first-party /about + HQ Austin TX (verbatim 'Austin, Texas (Headquarters)') + Tel Aviv Israel R&D (verbatim /about offices grid) + acquired by Tricentis in 2022 verbatim first-party /about + parent verbatim Tricentis Agentic Quality Engineering Platform 'The #1 agentic quality engineering platform' verbatim tricent.com hero + 'Gartner\u00ae named Tricentis a Leader in the 2025 Magic Quadrant\u2122' verbatim tricentis.com 2026-07-22 + 26-office global footprint verbatim first-party /about + products verbatim Testim AI + AI-stabilized UI + TestOps + Component-based + Salesforce Testing (testim.io/salesforce-testing/) verbatim + commercial route FORM:https://www.testim.io/contact-us/ HTTP 200 live 2026-07-22 + NO first-party sales@/hello@ inbox per pitfall #28 + compliance verbatim SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27017:2015 + ISO/IEC 27018:2019 + ISO/IEC 27701:2019 + PCI DSS 4.0 + GDPR + EU AI Act Aug 2 2026 + CCPA/CPRA + HIPAA-eligible (Tricentis ecosystem) + 18-column per-test-execution receipt tenant_id + test_run_id + test_case_id + framework_runtime_id + cross_browser_render_artifact_id + cross_device_viewport_signature + baseline_screenshot_hash + actual_screenshot_hash + pixel_diff_bounding_box + visual_ai_suggestion_id + cluster_root_cause_code + flaky_test_detection_score + self_healing_decision_id + ci_cd_pipeline_id + jira_test_management_id + tenant_scoping_boundary_id + tricentis_portfolio_product_id + cross_tenant_no_bleed_proof cross-tenant-no-bleed. Sibling #4/5 non-overlapping wedge vs Applitools 892 + Mabl 893 + Sauce Labs 894: (a) only cohort member with Tricentis-owned parent-control wedge (parallel private-equity-board-control wedge to Thoma Bravo controlling Applitools 892 but DIFFERENT parent); (b) only cohort member with record-playback-with-AI-stabilization (RPS + AI) at the locator layer; (c) only cohort member with TestOps suite for CI/CD-native test-orchestration; (d) only cohort member with first-party Salesforce-Testing vertical lane; (e) only cohort member with 26-office global footprint including Tel Aviv R&D; (f) only cohort member with cross-product-integration wedge via Tricentis portfolio (qTest + Tosca + NeoLoad). Offer $500/48h + $497/mo + $497/mo x 5-client YanXbt pattern = $2,485 MRR ceiling per operator. SMTP/form gated; no send, submission, payment, or revenue claim was fabricated; sibling #4/5 with 1 slot remaining for LambdaTest 896 CLOSER #5/5.",
]
with open(REV, "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n")
    w.writerow(rev_row)

with open(REV, encoding="utf-8") as f:
    rlines = f.readlines()
assert len(rlines) >= 2 and rlines[-1].startswith('"2026-07-22","895"'), f"Last revenue_log row not 895: {rlines[-1][:120]}"
print(f"PASS: revenue_log.csv -> {len(rlines)} lines, last entry lead 895")

# --- sitemap.xml ---
# P1.10.424 fix: chunk_894 used 4-space indent; preserve consistency for chunk_895
SITEMAP = ROOT / "sitemap.xml"
content = SITEMAP.read_text(encoding="utf-8")
assert 'chunk_894.html' in content
assert 'chunk_895.html' not in content
new_url_block = (
    '\n  <url>\n'
    '    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_895.html</loc>\n'
    '    <lastmod>2026-07-22</lastmod>\n'
    '    <changefreq>weekly</changefreq>\n'
    '    <priority>0.8</priority>\n'
    '  </url>\n'
)
# Insert before </urlset>
content = content.replace("</urlset>", new_url_block + "</urlset>", 1)
SITEMAP.write_text(content, encoding="utf-8")
# Verify
content_post = SITEMAP.read_text(encoding="utf-8")
assert 'chunk_895.html' in content_post
assert content_post.count('chunk_895.html') == 1
print("PASS: sitemap.xml chunk_895 entry inserted before </urlset>")

print("All 3 surface appends DONE — proceed to index.html + build-log.html via patch")
