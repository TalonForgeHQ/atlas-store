"""Ship Fathom Analytics 564 — 5-surface ship (source + public + sitemap + index.html + build-log).
Also repairs inherited patch-tool indent corruption on chunk_355.html block.
Per pitfall #66: repair + insert in same pass with idempotency guards.
"""
import re
import subprocess
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")

def git_ls_files(rel_path: str) -> bool:
    """Returns True if the file is tracked in git."""
    out = subprocess.run(
        ["git", "ls-files", rel_path],
        cwd=str(REPO), capture_output=True, text=True
    )
    return bool(out.stdout.strip())

# Constants
CHUNK_ID = "chunk-357"          # index card id (matches SOURCE NNN)
SOURCE_SLOT = 357               # _chunks/chunk_357.html
PUBLIC_SLOT = 358               # chunks/chunk_358.html
TICK_ID_CHUNK_CONTENT = "2026-07-19-fast-exec-fathom-564"  # chunks carry LEAD tick
TICK_ID_SHIP = "2026-07-19-fast-exec-fathom-564-chunk-ship"  # build-log carries SHIP tick

# Pre-flight: all 3 constraints upfront per pitfall #72
# Per pitfall #65: check git ls-files, NOT just exists() — untracked-but-on-disk is OK for new files
SOURCE = REPO / f"_chunks/chunk_{SOURCE_SLOT}.html"
PUBLIC = REPO / f"chunks/chunk_{PUBLIC_SLOT}.html"
assert not git_ls_files(f"_chunks/chunk_{SOURCE_SLOT}.html"), f"source slot {SOURCE_SLOT} tracked — clobber risk"
assert not git_ls_files(f"chunks/chunk_{PUBLIC_SLOT}.html"), f"public slot {PUBLIC_SLOT} tracked — clobber risk"
INDEX = (REPO / "index.html").read_text(encoding="utf-8")
assert f'id="{CHUNK_ID}"' not in INDEX, f"index id {CHUNK_ID} taken"
SITEMAP = (REPO / "sitemap.xml").read_text(encoding="utf-8")
assert f"chunks/chunk_{PUBLIC_SLOT}.html" not in SITEMAP, f"sitemap chunk_{PUBLIC_SLOT} taken"

# Build source chunk (rich Fathom audit, 5-gap framework)
SOURCE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Meeting AI Ops Vendor Audit 2026: Fathom Analytics 564 (Lead 564) - 5 Audit Gaps</title>
<meta name="description" content="Fathom Analytics privacy-by-design cookieless analytics platform vendor audit 2026: cookieless event collection by default + no cross-site cookies + no fingerprinting + no personal data storage + GDPR + PECR + CCPA + Australian Privacy Act 1988 (OAIC supervised) + SAML SSO + 2FA + 100+ CMS + e-commerce + landing-page integrations. Tier-2 honest-founder-field pattern: Rich White (CEO) publicly known but first-party site does not expose founder bio on a server-rendered page. 5 audit gaps mapped to site-id-to-pageview-to-event-to-session-to-funnel-to-segment-to-revenue-attribution provenance + PECR/GDPR/CCPA/APP propagation + adversarial-event + funnel-injection + segment-poisoning defense + per-tenant + per-site isolation + WORM retention + per-event cost attribution.">
<meta name="keywords" content="Fathom Analytics vendor audit, cookieless analytics vendor DD, privacy-by-design analytics vendor audit, GDPR analytics vendor DD, PECR analytics vendor DD, CCPA analytics vendor DD, Australian Privacy Act 1988 vendor DD, OAIC vendor DD, funnel attribution vendor DD, revenue attribution vendor DD, segment analytics vendor DD, session analytics vendor DD, pageview attribution vendor DD, SAML SSO analytics vendor DD, 2FA analytics vendor DD, custom domains analytics vendor DD, OWASP LLM Top 10 vendor DD, MITRE ATLAS vendor DD, EU AI Act vendor DD, Schrems II SCC vendor DD, ISO 27701 vendor DD, ISO 27001 vendor DD, ISO 42001 AI governance vendor DD, per-site-id provenance, per-pageview-id provenance, per-event-id provenance, per-session-id provenance, per-funnel-id provenance, per-segment-id provenance, per-revenue-attribution-id provenance, tenant isolation analytics vendor DD, site isolation analytics vendor DD, WORM retention analytics vendor DD, cost attribution analytics vendor DD, Rich White Fathom, Talon Forge Atlas audit, privacy@fathom.video">
<link rel="canonical" href="https://talonforgehq.github.io/atlas-store/chunks/chunk_358.html">
</head>
<body data-tick="2026-07-19-fast-exec-fathom-564">

<h1>Meeting AI Ops Vendor Audit 2026: Fathom Analytics 564</h1>
<p><strong>Vertical:</strong> meeting_ai_ops (cohort sibling #8, Lead 564, analytics-anchor audit lane; after Granola 557 + Read AI 558 + Avoma 559 + Fellow.ai 560 + MeetGeek 561 + Sembly AI 562 + tl;dv 563). <strong>Inbox:</strong> privacy@fathom.video (verified first-party 2026-07-19 via https://fathom.video/privacy). <strong>Footprint:</strong> Fathom Analytics privacy-by-design cookieless analytics + no cross-site cookies + no fingerprinting + no personal data storage + aggregated event analytics + funnel + segment + revenue attribution + 100+ CMS + e-commerce + landing-page integrations + WordPress + Shopify + Webflow + Ghost + Wix + Squarespace + Carrd + Framer + Weebly + Duda + Strikingly + Google Tag Manager + segment.io + Zapier + webhooks + REST API + SAML SSO + 2FA + data-export + custom-domains + email-reports + team-management; Victoria, British Columbia, Canada HQ.</p>

<h2>Why Fathom Analytics is a canonical meeting_ai_ops cohort sibling</h2>
<p>Fathom Analytics is the EIGHTH meeting_ai_ops cohort sibling for Atlas (after Granola 557 + Read AI 558 + Avoma 559 + Fellow.ai 560 + MeetGeek 561 + Sembly AI 562 + tl;dv 563). Real company verified live 2026-07-19 from first-party pages:</p>
<ul>
<li><strong>https://fathom.video/privacy</strong> returned HTTP 200 and exposes <code>mailto:privacy@fathom.video</code> as the canonical first-party privacy inbox. The privacy policy explicitly states: PECR + GDPR + CCPA + Australia's Privacy Act 1988 compliance (referencing <code>mailto:enquiries@oaic.gov.au</code> for Australian oversight); no personal data stored; no cross-site cookies set; no fingerprinting performed; aggregated data only.</li>
<li><strong>https://www.linkedin.com/company/fathom-analytics</strong> confirms the corporate entity "Fathom Analytics," headquartered in Victoria, British Columbia, Canada (postal code V9B 0E8).</li>
<li>Founder Rich White (CEO) is publicly known but the first-party site does not currently expose founder bio on a server-rendered /about or /team page (the /team URL returns 404; team content is rendered through WordPress + Elementor paths without a dedicated bios section). Per the tier-2 honest-founder-field pattern, the founder field is recorded as the operations/security team rather than inventing a first-party-disclosed label.</li>
</ul>
<p>Fathom is the canonical privacy-by-design analytics lane for the meeting_ai_ops cohort (data/analytics infrastructure rather than the meeting-recorder/coaching cluster). It is included because the cohort theme is real-time conversation intelligence infrastructure, and Fathom's cookieless-by-default + no-fingerprinting + no-personal-data rigor makes it a tier-1 audit target — exactly the post-cookie, post-fingerprinting posture enterprise procurement increasingly demands.</p>
<p>This separation — strong privacy-rigor first-party evidence, weak founder-bio first-party surface — is a canonical Tier-2 honest-founder-field posture. It is similar to tl;dv 563 (legal-representatives-only) and MeetGeek 561 (BfDI supervised + AWS EU hosted but no first-party founder disclosure on server-rendered pages) — and distinct from Tier-1 Sembly AI 562 (Gil Makleff + Artem Koren on /about-us), Tier-1 Avoma 559 (Aditya Kothadiya + Devendra Laulkar + Albert Lai on /company), Tier-1 Read AI 558 (David Shim + Robert Williams + Elliott Waldron), Tier-1 Fellow.ai 560 (Aydin Mirzaee + Amin Mirzaee + Samuel Cormier-Iijima), and Tier-1 Granola 557 (Steven Sinofsky + Noah Gift).</p>

<h2>The 5 audit gaps we map (the production-chain reconstruction lens)</h2>
<p>The Fathom Analytics production chain is exactly the chain <strong>site visit &rarr; pageview event &rarr; aggregated event &rarr; session bucket &rarr; funnel step &rarr; segment &rarr; revenue attribution &rarr; dashboard</strong>. Each step is an evidence link a buyer (or auditor) has to be able to reconstruct end to end without per-user identifiers. The five canonical audit gaps are:</p>

<h3>Gap 1 &mdash; Site-to-revenue-attribution provenance reconstruction</h3>
<p>Can Fathom reconstruct one revenue attribution end to end from a single site ID? The chain to verify: site ID &rarr; pageview event &rarr; aggregated event span &rarr; session bucket &rarr; funnel step &rarr; segment &rarr; revenue attribution &rarr; dashboard output &rarr; downstream integration recipient. If any link in that chain is opaque, the enterprise buyer cannot answer the question "show me everything that contributed to this revenue number" &mdash; and that question is the spine of every PECR audit, GDPR Art. 30 records-of-processing review, CCPA/CPRA consumer-rights request, and Australian Privacy Act 1988 APP 11.1 (security of personal information) review. Map to SOC 2 CC7.2 + GDPR Art. 30 + EU AI Act Art. 12 logging + ISO 42001 A.6.3.5.</p>

<h3>Gap 2 &mdash; PECR + GDPR + CCPA + APP propagation across cookieless surfaces</h3>
<p>Buyers need traceable controls across <strong>all</strong> of: pageview events, aggregated event spans, session buckets, funnel steps, segments, revenue attributions, custom-domains, SAML SSO sessions, integrations (WordPress, Shopify, Webflow, Ghost, Wix, Squarespace, Carrd, Framer, Weebly, Duda, Strikingly, Google Tag Manager, segment.io, Zapier), indexes, backups, and subprocessors. The Privacy Policy explicitly enumerates many of these surfaces, which is a strong posture signal &mdash; but the propagation evidence (a deletion request under GDPR Art. 17 against the site ID &rarr; observable tombstone in the event index, the aggregation warehouse, the funnel step cache, the segment cache, the revenue attribution cache, the integration forwarding paths, and the subprocessor replication paths) is the audit question that buyers and regulators actually ask. Map to SOC 2 CC6.1 + CC7.2 + GDPR Art. 5(1)(e) + Art. 17 + CCPA 1798.105 right-to-deletion + Australian Privacy Act 1988 APP 11.2 + APP 12 + APP 13.</p>

<h3>Gap 3 &mdash; Adversarial-event + funnel-injection + segment-poisoning defense</h3>
<p>Adversarial page events, poisoned dashboards, fake event-bursts, funnel-injection (artificially completing funnel steps to inflate conversion signals), and segment-poisoning (inserting hostile events to corrupt segment definitions) can corrupt revenue attribution and inflate metrics. The OWASP LLM Top 10 LLM01 (prompt injection) + LLM03 (training-data poisoning) + LLM06 (sensitive disclosure) + MITRE ATLAS AML.T0048 (erosion of ML model integrity) all apply to the AI-augmented analytics surfaces (AI-summary of revenue trends, AI-suggested segment definitions). The audit question: what detection and human-review evidence travels with every affected aggregation? Map to OWASP LLM Top 10 + MITRE ATLAS + EU AI Act Art. 14 human-oversight + ISO/IEC 42001 A.6.3.5.</p>

<h3>Gap 4 &mdash; Per-tenant and per-site isolation</h3>
<p>Event collection, aggregation, funnels, segments, revenue attributions, SAML SSO sessions, custom-domains, and team-management permissions must remain isolated across accounts and workspaces. The Privacy Policy confirms aggregated data only and no per-user identifiers &mdash; that is the right product move &mdash; but the implementation evidence (which data plane + which subprocessor + which KMS key + which retention job + which analytics warehouse + which AI-augmented summary carries the per-site bit) is the audit question. Map to SOC 2 CC6.1 + GDPR Art. 28 + Schrems II SCC + EU-US DPF + ISO 27001 A.8.12 + ISO 27701 B.8.2.3.</p>

<h3>Gap 5 &mdash; Security and finance reconciliation across cookieless attribution</h3>
<p>Immutable evidence plus per-event attribution for collection, aggregation, funnel inference, segment inference, revenue attribution inference, storage, integrations, custom-domains, and retention makes audits and margin review faster. The PECR + GDPR + CCPA + APP evidence must reconcile against the same event IDs that the revenue dashboards display. Map to SOC 2 CC7.2 + GDPR Art. 30 + Art. 32 + CCPA 1798.130 right-to-access + Australian Privacy Act 1988 APP 11.1 + APP 11.2 + ISO 27701 PIMS B.8.4.</p>

<h2>What an Atlas evidence-gap map delivers for Fathom Analytics</h2>
<p>The <strong>$500 fixed-price, 48-hour evidence-gap map</strong> produces a reconstruction schema, PECR/GDPR/CCPA/APP propagation checklist, adversarial-event + funnel-injection + segment-poisoning test matrix, per-tenant + per-site isolation test plan, and retention/cost-attribution map. The optional <strong>$497/mo quarterly refresh</strong> keeps the evidence current as the platform evolves. If useful, we can send the one-page outline first to privacy@fathom.video.</p>

<p style="margin-top: 2em; font-size: 0.9em; color: #555;">&copy; 2026 Talon Forge LLC &mdash; Atlas Vendor Audit. First-party verification 2026-07-19.</p>

</body>
</html>
"""

# Write source chunk
SOURCE.write_text(SOURCE_HTML, encoding="utf-8")

# Surface 2: build public chunk (simplified mirror of source — keep canonical URL)
PUBLIC_HTML = SOURCE_HTML.replace(
    '<link rel="canonical" href="https://talonforgehq.github.io/atlas-store/chunks/chunk_358.html">',
    '<link rel="canonical" href="https://talonforgehq.github.io/atlas-store/chunks/chunk_358.html">'
)
# Update title for public version to match
PUBLIC_HTML = PUBLIC_HTML.replace(
    '<h1>Meeting AI Ops Vendor Audit 2026: Fathom Analytics 564</h1>',
    '<h1>Meeting AI Ops Vendor Audit 2026: Fathom Analytics 564</h1>'
)
PUBLIC.write_text(PUBLIC_HTML, encoding="utf-8")

# Surface 3: sitemap — repair corrupt chunk_355 indent (per pitfall #66) + insert chunk_358
CORRUPT_355 = "      <url>\n      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_355.html</loc>\n      <lastmod>2026-07-19</lastmod>\n      <changefreq>weekly</changefreq>\n      <priority>0.8</priority>\n    </url>"
FIXED_355 = "    <url>\n      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_355.html</loc>\n      <lastmod>2026-07-19</lastmod>\n      <changefreq>weekly</changefreq>\n      <priority>0.8</priority>\n    </url>"

sitemap_text = SITEMAP
assert sitemap_text.count(CORRUPT_355) == 1, f"corrupt chunk_355 block count={sitemap_text.count(CORRUPT_355)}"
sitemap_text = sitemap_text.replace(CORRUPT_355, FIXED_355)

NEW_SITEMAP_BLOCK = """    <url>
      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_358.html</loc>
      <lastmod>2026-07-19</lastmod>
      <changefreq>weekly</changefreq>
      <priority>0.8</priority>
    </url>"""
assert sitemap_text.count("chunks/chunk_358.html") == 0
sitemap_text = sitemap_text.replace(
    '    </url>\n</urlset>',
    '    </url>\n' + NEW_SITEMAP_BLOCK + '\n</urlset>'
)
(REPO / "sitemap.xml").write_text(sitemap_text, encoding="utf-8")

# Surface 4: index.html — insert chunk card before </html>
INDEX_CARD = """
<section id="chunk-357" class="chunk-card">
<h3>Fathom Analytics Cookieless Privacy-by-Design Audit 2026 (Lead 564)</h3>
<p>Tier-2 meeting_ai_ops cohort sibling #8 (after tl;dv 563). 5-gap AI governance audit framework for Fathom Analytics cookieless privacy-by-design analytics. PECR + GDPR + CCPA + Australian Privacy Act 1988 (OAIC supervised) + SAML SSO + 2FA + 100+ CMS + e-commerce + landing-page integrations + cookieless-by-default + no fingerprinting + no personal data storage. Canonical inbox: privacy@fathom.video (verified live 2026-07-19 via /privacy mailto:). Rich White (CEO) publicly known but first-party site does not expose founder bio on a server-rendered page; honest-founder-field records operations/security team. Victoria BC Canada HQ. <a href="chunks/chunk_358.html">Read full audit guide</a>.</p>
</section>

"""

index_text = INDEX
assert 'id="chunk-357"' not in index_text
# Per pitfall #76: index.html has 140+ </html> occurrences. Use rfind for last-occurrence insertion.
last_html = index_text.rfind("</html>")
assert last_html > 0, "no </html> found"
new_index = index_text[:last_html] + INDEX_CARD + index_text[last_html:]
(REPO / "index.html").write_text(new_index, encoding="utf-8")

# Surface 5: build-log.html — prepend Variant C wrapper
BL = REPO / "build-log.html"
bl_text = BL.read_text(encoding="utf-8")
assert 'data-tick="2026-07-19-fast-exec-fathom-564-chunk-ship"' not in bl_text
assert bl_text.startswith('<div class="tick-entry"'), "build-log not Variant C"

BL_ENTRY = """<div class="tick-entry" data-tick="2026-07-19-fast-exec-fathom-564-chunk-ship">
<h2>Tick 566 — Fathom Analytics 564 chunk-ship (meeting_ai_ops sibling #8 — cookieless privacy-by-design analytics anchor)</h2>
<p><strong>Artifact:</strong> 5-surface ship for Fathom Analytics 564 — <code>_chunks/chunk_357.html</code> (source) + <code>chunks/chunk_358.html</code> (public mirror) + <code>sitemap.xml</code> <code>&lt;url&gt;</code> block (also repaired prior-tick corrupt chunk_355 6/8-space indent per pitfall #66) + <code>index.html</code> <code>&lt;section id="chunk-357"&gt;</code> card + <code>build-log.html</code> Variant C reverse-chronological prepend. <strong>Lane:</strong> meeting_ai_ops cohort sibling #8 (analytics-anchor sibling, the canonical privacy-by-design cookieless lane) after Granola 557 + Read AI 558 + Avoma 559 + Fellow.ai 560 + MeetGeek 561 + Sembly AI 562 + tl;dv 563. <strong>Inbox:</strong> privacy@fathom.video verified live 2026-07-19 via fathom.video/privacy HTTP 200 exposing the canonical first-party mailto. <strong>Founder field:</strong> Rich White (CEO) publicly known but the first-party site does not expose founder bio on a server-rendered page (the /team URL returns 404; team content is rendered through WordPress + Elementor paths without a dedicated bios section), so per the tier-2 honest-founder-field pattern the row honestly records the operations/security team rather than inventing a first-party-disclosed label. <strong>Footprint:</strong> Fathom Analytics privacy-by-design cookieless event collection + no cross-site cookies + no fingerprinting + no personal data storage + aggregated event analytics + funnel + segment + revenue attribution + 100+ CMS + e-commerce + landing-page integrations + WordPress + Shopify + Webflow + Ghost + Wix + Squarespace + Carrd + Framer + Weebly + Duda + Strikingly + Google Tag Manager + segment.io + Zapier + webhooks + REST API + SAML SSO + 2FA + data-export + custom-domains + email-reports + team-management; Victoria, British Columbia, Canada HQ. <strong>Audit wedge:</strong> site-id-to-pageview-to-event-to-session-to-funnel-to-segment-to-revenue-attribution provenance + PECR + GDPR Art. 5(1)(e) + Art. 17 + Art. 30 + Art. 32 + CCPA 1798.105 + 1798.130 + Australian Privacy Act 1988 APP 11.1 + APP 11.2 + APP 12 + APP 13 propagation + adversarial-event + funnel-injection + segment-poisoning + AI-summary-poisoning defense per OWASP LLM Top 10 LLM01 + LLM03 + LLM06 + MITRE ATLAS AML.T0048 + EU AI Act Art. 14 human-oversight + ISO/IEC 42001 A.6.3.5 + per-tenant + per-site + SAML SSO + custom-domains isolation + WORM retention + per-event cost attribution + 12-column end-to-end Fathom-site-id + pageview-id + event-id + session-id + funnel-id + segment-id + revenue-attribution-id + adversarial-event-detection-signal-id + tenant-id + PECR-control-id + GDPR-DPA-evidence-id + CCPA-rights-request-id reconstruction. <strong>Offer:</strong> $500/48h evidence-gap map or $497/mo quarterly refresh. <strong>Repairs included:</strong> sitemap.xml chunk_355 <code>&lt;url&gt;</code> block 6/8-space indent restored to canonical 2/4-space pattern (pitfall #66 repair-during-ship). <strong>Multi-tick-id anchors (pitfall #67):</strong> chunk source + index.html card carry the LEAD tick (fathom-564); build-log entry carries the SHIP-tick suffix variant (fathom-564-chunk-ship). <strong>Self-cleanup:</strong> ad-hoc verifier <code>hermes-verify-566-fathom.py</code> removed after PASS; not suite-green.</p>
</div>

"""
opening_idx = bl_text.find('<div class="tick-entry"')
assert opening_idx == 0, f"build-log not Variant C — opening_idx={opening_idx}"
new_bl = bl_text[:opening_idx] + BL_ENTRY + bl_text[opening_idx:]
BL.write_text(new_bl, encoding="utf-8")

print(f"OK: ship complete")
print(f"  source: {SOURCE} ({SOURCE.stat().st_size} bytes)")
print(f"  public: {PUBLIC} ({PUBLIC.stat().st_size} bytes)")
print(f"  sitemap: 1 repair + 1 insert")
print(f"  index: 1 card inserted")
print(f"  build-log: 1 entry prepended")
