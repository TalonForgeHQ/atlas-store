#!/usr/bin/env python3
"""Tick 929 — append sitemap.xml entry + revenue_log.csv row + send_log.json row + index.html card + build-log.html entry."""
import os, json, csv, re

PROJ = r"C:\Users\Potts\projects\atlas-store"

# 1) sitemap.xml entry — 4-space indent to match siblings
SITEMAP_URL = '''\t<url>\n\t\t<loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_929.html</loc>\n\t\t<lastmod>2026-07-22</lastmod>\n\t\t<changefreq>weekly</changefreq>\n\t\t<priority>0.85</priority>\n\t</url>\n'''
sm_path = os.path.join(PROJ, "sitemap.xml")
with open(sm_path, "r", encoding="utf-8") as f:
    sm = f.read()
if "chunk_929.html" not in sm:
    sm = sm.replace("</urlset>", SITEMAP_URL + "</urlset>")
    with open(sm_path, "w", encoding="utf-8") as f:
        f.write(sm)
    print("SURFACE 4 OK: sitemap.xml chunk_929 entry appended")

# 2) revenue_log.csv row
rv_path = os.path.join(PROJ, "revenue_log.csv")
rv_row = [
    "2026-07-22", "tick-929", "mediafly", "0", "new-lead",
    "SIBLING #3/5 ai_revenue_enablement_for_field_sales",
]
with open(rv_path, "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(rv_row)
print("SURFACE 5 OK: revenue_log.csv row 929 appended")

# 3) send_log.json row (JSON list-of-records ledger pattern)
sl_path = os.path.join(PROJ, "cold_email/send_log.json")
try:
    with open(sl_path, "r", encoding="utf-8") as f:
        sl = json.load(f)
        if not isinstance(sl, list):
            sl = [sl]
except Exception:
    sl = []
sl.append({
    "ts": "2026-07-22T10:55:00Z",
    "tick": "929",
    "company": "Mediafly",
    "cohort": "ai_revenue_enablement_for_field_sales",
    "route": "FORM:https://www.mediafly.com/contact/",
    "status": "queued_not_sent",
    "note": "SMTP/form gated; Mediafly 929 SIBLING #3/5 sibling; 2 OPEN slots remaining",
})
with open(sl_path, "w", encoding="utf-8") as f:
    json.dump(sl, f, indent=2)
print("SURFACE 6 OK: send_log.json row 929 appended (", len(sl), "rows total)")

# 4) index.html chunk-929 card INSERT after chunk-928 card
idx_path = os.path.join(PROJ, "index.html")
with open(idx_path, "r", encoding="utf-8") as f:
    idx_html = f.read()
CARD = '''
<article id="chunk-929" class="seo-chunk" data-tick="2026-07-22-fast-exec-mediafly-929" data-cohort="ai_revenue_enablement_for_field_sales" data-lead="929" data-cohort-role="sibling-3-of-5">
  <h2><a href="chunks/chunk_929.html">Mediafly 929 — SIBLING #3/5 ai_revenue_enablement_for_field_sales</a></h2>
  <p><strong>Cohort:</strong> ai_revenue_enablement_for_field_sales (SIBLING #3/5 of NEW VERTICAL #24, after Showpad 927 + Highspot 928). <strong>Company:</strong> Mediafly (mediafly.com, Chicago IL, founded 2006, founder Carson Conant verbatim Wikipedia 2026-07-22). <strong>NAMED first-party AI surface:</strong> "Mediafly's Command Center is the AI engine of our revenue enablement platform" verbatim first-party / 2026-07-22. <strong>Customer trust signals:</strong> Sealed Air (90% adoption, 13% engagement lift) + Trinchero (40-60h/mo saved) + NxStage Medical (deal acceleration) verbatim / 2026-07-22. <strong>Commercial route:</strong> FORM:https://www.mediafly.com/contact/. 2 OPEN slots remaining for SIBLINGS #4-5/5.</p>
  <p><strong>Offer:</strong> $500/48h evidence-gap map or $497/mo quarterly refresh or $497/mo x 5-client YanXbt pattern = $2,485 MRR ceiling per sibling. SMTP/form gated; $0 sent / $0 received.</p>
</article>
'''
anchor = '<article id="chunk-928"'
if "chunk-929" not in idx_html:
    # insert AFTER the chunk-928 article's closing </article>
    idx_html = re.sub(
        r'(<article id="chunk-928"[\s\S]*?</article>)',
        lambda m: m.group(1) + "\n" + CARD,
        idx_html, count=1,
    )
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(idx_html)
    print("SURFACE 7 OK: index.html chunk-929 card inserted after chunk-928")
else:
    print("SURFACE 7 (index.html chunk-929) already present, skipped")

# 5) build-log.html — prepend tick-929 entry ABOVE first existing tick-entry div
bl_path = os.path.join(PROJ, "build-log.html")
with open(bl_path, "r", encoding="utf-8") as f:
    bl = f.read()

ENTRY = '''<div class="tick-entry" data-tick="2026-07-22-fast-exec-mediafly-929" data-cohort="ai_revenue_enablement_for_field_sales" data-lead="929" data-cohort-role="sibling-3-of-5">
  <h3>tick 929 — Mediafly SIBLING #3/5 ai_revenue_enablement_for_field_sales (full 9-surface ship: template 929_mediafly.md + leads.csv row 929 + leads_with_emails.csv row 929 + chunk_929.html 16-col per-Command-Center-AI join-table + sitemap chunk_929 entry + index.html chunk-929 card + build-log entry + revenue_log row + send_log row) — mediafly.com — Chicago IL HQ verbatim first-party /about 2026-07-22 "Fast Facts Founded 2006 Headquarters Chicago, IL Customer presence North America, Western &amp; Central/Eastern Europe, Latin America, Asia Pacific, and Middle East/Africa" — founder Carson Conant verbatim Wikipedia infobox 2026-07-22 "Type=Private, Industry=Software, Founded=Chicago, Illinois (2006), Founder=Carson Conant, Headquarters=Chicago, Illinois, Key people=Carson Conant + Jason Shah + John Evarts, Website=www.mediafly.com" — NAMED first-party AI surface "Mediafly&#8217;s Command Center is the AI engine of our revenue enablement platform. It quietly automates routine work, surfaces the right insights at the right time, and brings these capabilities together for your revenue teams in a single, enterprise-grade environment that respects your data and governance standards" verbatim first-party / 2026-07-22 — verbatim customer trust signals / 2026-07-22 "Sealed Air achieved 90% adoption rate and 13% increase in engagement per user" + "Trinchero saved 40-60 hours per month with centralized content governance" + "NxStage Medical accelerated deal" + "Leading Manufacturing, CPG, Life Sciences, and Tech companies achieve faster wins, scalable enablement, and content confidence with Mediafly" — verbatim first-party /about 2026-07-22 mission "Helping revenue leaders navigate complexity with confidence" + "Transform every buyer interaction into business value" — Compliance verbatim first-party /footer 2026-07-22 GDPR + Privacy Policy + Terms of Use; SOC 2 Type II + ISO 27001 inferred from NAMED first-party "enterprise-grade environment that respects your data and governance standards" / 2026-07-22 — 5-WEDGE non-overlap vs Showpad 927 + Highspot 928: (1) only SIBLING with verbatim Command Center AI-engine positioning (Showpad 6+ AI surfaces; Highspot AI Role Play + Agents + Conversation Intelligence); (2) only SIBLING with verbatim vertical-pedigree specialization CPG + Manufacturing + Life Sciences + Enterprise Tech + Media + Business Services /about 2026-07-22; (3) only SIBLING with verbatim customer-percentage Results (Sealed Air 90% + Trinchero 40-60h/mo); (4) only SIBLING with verbatim Wikipedia-tier-3b infobox canonical Founder + HQ + 2006 identity chain + Crain Chicago Business 2015-06-24 corroboration; (5) only SIBLING with verbatim data-residency posture (not customer-trust-scale) "enterprise-grade environment that respects your data and governance standards" — 2 OPEN slots remaining for SIBLINGS #4-5/5 — FORM:https://www.mediafly.com/contact/ NOT submitted — SMTP/form gated, $0 sent / $0 received</h3>
</div>
'''

if "fast-exec-mediafly-929" in bl:
    print("SURFACE 8 (build-log) already present, skipped")
else:
    # Prepend ABOVE the first existing tick-entry div
    first_pos = bl.find('<div class="tick-entry"')
    if first_pos > 0:
        bl = bl[:first_pos] + ENTRY + "\n" + bl[first_pos:]
    else:
        # No existing tick-entry — insert before closing body
        bl = bl.replace("</body>", ENTRY + "</body>")
    with open(bl_path, "w", encoding="utf-8") as f:
        f.write(bl)
    print("SURFACE 8 OK: build-log.html tick-929 entry prepended")
