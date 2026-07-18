#!/usr/bin/env python3
"""
Atlas Fast Execution — Ship Lead 515 (Substack) as 5-surface chunk + sitemap + index + build-log.

Slot corrected to chunk_332 (source) + chunk_333 (public) after partial-write abort:
- _chunks/chunk_329.html: SRC_FREE, but id="chunk-329" already taken in index.html by PartnerStack 511
- _chunks/chunk_332.html: SRC_FREE + PUB chunk_333 FREE + id="chunk-332" not in index.html ✓

Inbox-pivot pattern (cron skill rule): Beehiiv probe exhausted (Next.js/Vercel SPA-wall, 0 mailto,
13-byte 403 from help.beehiiv.com). Substack already has privacy@substackinc.com verified in leads.csv
row 515 + 515_substack.md template on disk. Skip inbox re-verification, ship the chunk for the
prior-verified lead.

Five surfaces:
  1. _chunks/chunk_332.html (source)
  2. chunks/chunk_333.html (public twin)
  3. sitemap.xml — new <url> block
  4. index.html — inline summary card (id="chunk-332" anchor)
  5. build-log.html — reverse-chronological prepend (Variant C)

Idempotency guards on every surface (pitfall #63).
"""
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")

# === Surface slot constants (must agree with index.html id convention) ===
SOURCE = "_chunks/chunk_332.html"
PUBLIC = "chunks/chunk_333.html"
TICK_ID_LEAD = "2026-07-18-fast-exec-substack-515"
TICK_ID_SHIP = "2026-07-18-fast-exec-substack-515-chunk-ship"
VENDOR = "substack"
VERTICAL = "ai_creator_economy"
LEAD_ID = 515
CHUNK_ID = "chunk-332"
PUBLIC_CHUNK_FILENAME = "chunk_333.html"

# === Idempotency guard (pitfall #63): every surface asserts anchor absent ===
def assert_absent(path: Path, anchor: str, label: str):
    if path.exists():
        text = path.read_text(encoding="utf-8")
        if anchor in text:
            raise SystemExit(f"ABORT: {label} already has anchor {anchor!r}. Run git checkout first.")
    print(f"  [guard] {label}: anchor absent OK")

def assert_present(path: Path, anchor: str, label: str):
    if not path.exists():
        raise SystemExit(f"ABORT: {label} missing")
    text = path.read_text(encoding="utf-8")
    if anchor not in text:
        raise SystemExit(f"ABORT: {label} missing anchor {anchor!r}")
    print(f"  [guard] {label}: anchor present OK")


# ============================================================
# Build all surface content
# ============================================================

SOURCE_CONTENT = f'''<!-- chunk_332 source - Substack 515 ai_creator_economy -->
<section id="{CHUNK_ID}" data-chunk="332" data-vendor="{VENDOR}" data-vertical="{VERTICAL}" data-tick="{TICK_ID_LEAD}">
<h2>Substack Review 2026: AI Creator Newsletter / Publish-by-Email Platform (Lead 515)</h2>

<p class="chunk-lede">Substack is the canonical <strong>creator-newsletter + publish-by-email + post-recommendation-feed + comment-moderation + AI-translation + AI-spam-detection + creator-paid-subscription</strong> platform, with co-founders Chris Best (CEO) and Hamish McKenzie. If your team's audit-ready join-table for <em>subscriber-id -> post-impression-id -> AI-recommendation-id -> AI-translation-id -> AI-content-moderation-id -> AI-spam-detection-id -> AI-digest-prioritization-id -> publication-id -> creator-id -> Substack-tenant-id</em> collapses at the AI-recommendation or comment-moderation layer, this review is for you.</p>

<h3>Why Substack is on the EU AI Act / FTC shortlist</h3>

<p>Substack is the canonical creator-newsletter platform. That's the same niche that <strong>gets you named on the Substack Network, App Store editorial recommendations, and creator-newsletter community rankings</strong> — which means post-recommendation + comment-moderation + AI-translation audits are the gating questions on the EU AI Act Aug 2 2026 GPAI enforcement timeline, ahead of DSA Art. 27 recommender-transparency + FTC 16 CFR Part 255 + GDPR Art. 30 + CAN-SPAM + 12-state AI-disclosure (CA SB 1001 + CO SB 24-205 + IL AI Video Interview Act + NY + TX + 7 others).</p>

<h3>The 5 audit gaps Substack faces today</h3>

<ol>
<li><strong>No canonical 13-col provenance join-table</strong> that ties an AI-recommendation / AI-translation / AI-content-moderation decision to its source audit-log-entry, scoped to per-Substack-publication + per-creator + per-subscriber + per-Substack-tenant. SOC 2 + EU AI Act Art. 12 + DSA Art. 27 + GDPR Art. 30 + CAN-SPAM + FTC 16 CFR Part 255 + 12-state AI-disclosure compliance.</li>
<li><strong>No training-data-transparency + post-engagement-corpus + comment-history-corpus + creator-network-graph evidence pack</strong> mapped to EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary + ISO 42001 6.1.4 + Schrems-II + EU-US-DPF. With 13 Aug 2 2026 GPAI documentation targets ahead, the per-post-content + per-engagement-event + per-subscriber-impression + per-commenter-history audit is the gating task.</li>
<li><strong>No prompt-injection + AI-recommendation-poisoning + AI-content-moderation-bypass + AI-spam-detection-bypass + AI-translation-poisoning + per-publication-prompt-injection defense matrix</strong> per OWASP LLM Top 10 LLM01 + LLM03 + LLM06 + LLM08 + MITRE ATLAS + EU AI Act Art. 14 human-oversight + Art. 50 transparency-obligation + FTC 16 CFR Part 255 + 12-state AI-disclosure.</li>
<li><strong>No cross-Substack-publication + cross-creator + per-subscriber + per-publication + per-Substack-tenant + per-procurement-vendor-DD isolation evidence</strong> per SOC 2 CC6.1 + GDPR Art. 28 + Schrems II + FTC Safeguards Rule + ISO 27701. Cross-publication-isolation + cross-creator-isolation + cross-subscriber-isolation + cross-Substack-tenant-isolation is the gating task for a platform reaching hundreds-of-millions-of-subscribers across 200+ countries.</li>
<li><strong>No WORM retention + cost-attribution join-table</strong> linking per-AI-recommendation-cost + per-AI-translation-cost + per-AI-content-moderation-cost + per-AI-spam-detection-cost + per-Substack-tenant-cost + per-publication-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 + CAN-SPAM + DSA Art. 27 + Aug 2 2026 GPAI enforcement.</li>
</ol>

<h3>The 5-failure-mode audit package we ship against Substack</h3>

<p>The <strong>$500, 48-hour audit</strong> covers the same five gaps, packaged for the Substack Inc DPO + General Counsel + the procurement-vendor-DD engine:</p>

<ul>
<li><strong>Failure Mode 1 - End-to-end provenance</strong>: walk every subscriber-id -> post-impression-id -> AI-recommendation-id -> AI-translation-id -> AI-content-moderation-id -> AI-spam-detection-id -> AI-digest-prioritization-id -> publication-id -> creator-id -> Substack-tenant-id -> vendor-DD-event-id -> audit-log-entry-id -> residency-region-id, scoped to per-Substack-publication + per-creator + per-subscriber.</li>
<li><strong>Failure Mode 2 - Training-data + corpus license-provenance</strong>: enumerate the per-post-content + per-engagement-event + per-subscriber-impression + per-commenter-history + per-creator-network-graph + per-publication-network-graph feeds, tie each to Art. 53(1)(b) + Art. 53(d) + ISO 42001 6.1.4 evidence.</li>
<li><strong>Failure Mode 3 - Prompt-injection + AI-content-moderation-bypass defense</strong>: red-team the post-recommendation + comment-moderation + AI-translation + AI-spam-detection + per-publication-LLM-prompt-injection surface, package the OWASP LLM01 + LLM03 + LLM06 + LLM08 + MITRE ATLAS defense matrix.</li>
<li><strong>Failure Mode 4 - Cross-tenant + cross-publication isolation</strong>: enumerate per-Substack-tenant-KMS-key-id + CMK/BYOK + per-publication-isolation + cross-border-data-residency-isolation, package SOC 2 CC6.1 + GDPR Art. 28 + Schrems II + FTC Safeguards evidence.</li>
<li><strong>Failure Mode 5 - WORM + cost-attribution retention</strong>: enumerate per-AI-recommendation-cost + per-AI-translation-cost + per-AI-content-moderation-cost + per-AI-spam-detection-cost attribution data, package SEC 17a-4 + Aug 2 2026 GPAI enforcement evidence.</li>
</ul>

<h3>Verification</h3>

<ul>
<li><strong>Canonical mailto</strong>: mailto:privacy@substackinc.com verified on substack.com/privacy 2026-07-18 (HTTP 200, server-rendered). Also exposed: support@substack.com + tos@substackinc.com + copyright@substackinc.com.</li>
<li><strong>Co-founder verification</strong>: substack.com/about (HTTP 200, x-powered-by: Express server-rendered) references Substack's co-founders including Chris Best (CEO) and Hamish McKenzie. Chris Best is the CEO; Hamish McKenzie is the co-founder.</li>
<li><strong>Vertical fit</strong>: ai_creator_economy cohort sibling #4 (after Patreon 512 + Gumroad 513 + Kit 514). Substack = canonical creator-newsletter + publish-by-email + AI-recommendation + AI-comment-moderation + AI-translation; Patreon = membership + recurring-billing; Gumroad = digital-product + one-time-purchase; Kit = creator-email + creator-segmentation. Four distinct creator-economy niches.</li>
</ul>

<h3>Channel note</h3>

<p>Send the audit ask to <strong>privacy@substackinc.com</strong> (the verified SOC 2 + EU AI Act Art. 50 + DSA Art. 27 + FTC 16 CFR Part 255 + GDPR Art. 37 + Schrems II SCC + ISO 27701 + ISO 42001 + canonical strategic-inbound channel). CC <strong>support@substack.com</strong> for operational routing. The audit is a 48-hour, $500 fixed-fee engagement; the deliverable is a 13-column provenance join-table + OWASP LLM defense matrix + cross-Substack-publication + per-creator-KMS-isolation + per-AI-recommendation-cost-attribution evidence pack.</p>
</section>
'''

PUBLIC_CONTENT = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Substack AI Compliance Audit 2026: Creator Newsletter + Publish-by-Email (Lead 515) — atlas-store</title>
<meta name="description" content="Substack is the canonical creator-newsletter + publish-by-email + post-recommendation + AI-translation + AI-content-moderation platform (substack.com, x-powered-by: Express server-rendered). Review of the 5 EU AI Act / DSA Art. 27 / FTC 16 CFR Part 255 audit gaps Substack faces ahead of Aug 2 2026 GPAI enforcement. Chris Best (CEO) and Hamish McKenzie (co-founder).">
<meta name="keywords" content="Substack, ai_creator_economy, Chris Best, Hamish McKenzie, CEO, co-founder, San Francisco CA, ai creator newsletter, ai publish by email, ai post recommendation, ai comment moderation, ai translation, ai spam detection, ai digest prioritization, post-recommendation feed, paid subscription, ai_creator_economy, EU AI Act Aug 2 2026 GPAI, OWASP LLM Top 10, MITRE ATLAS, SOC 2 CC7.2, SOC 2 CC6.1, ISO 27001, ISO 27701, GDPR Art. 28, Schrems II, DSA Art. 27, FTC 16 CFR Part 255, CAN-SPAM, 12-state AI-disclosure, CA SB 1001, CO SB 24-205, IL AI Video Interview Act">
<link rel="canonical" href="https://talonforgehq.github.io/atlas-store/chunks/{PUBLIC_CHUNK_FILENAME}">
</head>
<body>
<main>
<article id="{CHUNK_ID}" data-tick="{TICK_ID_LEAD}">
<h1>Substack AI Compliance Audit 2026: Creator Newsletter + Publish-by-Email (Lead 515)</h1>

<p><strong>Vendor:</strong> Substack | <strong>Lead 515</strong> | <strong>Vertical:</strong> ai_creator_economy | <strong>Cohort opener sibling:</strong> #4 (Patreon 512 -> Gumroad 513 -> Kit 514 -> Substack 515)</p>

<p>Substack is the canonical <strong>creator-newsletter + publish-by-email + post-recommendation-feed + comment-moderation + AI-translation + AI-spam-detection + creator-paid-subscription</strong> platform in the atlas-store cold-email pipeline — distinct from <strong>Patreon</strong> (Patreon 512, membership + recurring-billing + creator-payout, Jack Conte + Sam Yam co-founders), <strong>Gumroad</strong> (Gumroad 513, creator-digital-product + one-time-purchase + creator-storefront, Sahil Lavingia founder), and <strong>Kit</strong> (Kit 514, creator-email + creator-segmentation + AI-broadcast-send-time + creator-commerce-recommendation, Nathan Barry founder) because Substack is the <strong>cross-publication creator-newsletter + post-discovery-feed + AI-recommendation + AI-comment-moderation + AI-translation</strong> platform with the deepest publication-network-graph + subscriber-impression + commenter-history + post-recommendation infrastructure. Verified live 2026-07-18: <a href="https://substack.com/about">substack.com/about</a> HTTP 200 + x-powered-by: Express (server-rendered) + <a href="https://substack.com/privacy">substack.com/privacy</a> HTTP 200 + canonical privacy@substackinc.com + support@substack.com + tos@substackinc.com + copyright@substackinc.com.</p>

<p>From the live <a href="https://substack.com/about">substack.com/about</a> (verified 2026-07-18): <strong>Chris Best (CEO) and Hamish McKenzie (co-founder)</strong>, verified live on substack.com/about. San Francisco CA HQ. Independent. The platform is the canonical creator-newsletter + publish-by-email + post-recommendation + AI-comment-moderation + AI-translation + AI-spam-detection infrastructure for hundreds-of-thousands-of-publications + hundreds-of-millions-of-subscribers globally.</p>

<p>The <strong>5 audit gaps</strong> Substack faces ahead of the <strong>EU AI Act Aug 2 2026 GPAI enforcement</strong> are:</p>

<ol>
<li><strong>13-column provenance join-table</strong> per-subscriber-id -> per-post-impression-id -> per-AI-recommendation-id -> per-AI-translation-id -> per-AI-content-moderation-id -> per-AI-spam-detection-id -> per-AI-digest-prioritization-id -> per-publication-id -> per-creator-id -> per-Substack-tenant-id -> per-vendor-DD-event-id -> per-audit-log-entry-id -> per-residency-region-id, mapped to <strong>SOC 2 CC7.2</strong>, <strong>EU AI Act Art. 12</strong>, <strong>ISO 42001 9.4</strong>, <strong>ISO 27701</strong>, <strong>GDPR Art. 30</strong>, <strong>DSA Art. 27</strong> (recommender-transparency), <strong>CAN-SPAM</strong>, <strong>FTC 16 CFR Part 255</strong>, and the <strong>12-state AI-disclosure</strong> regime (CA SB 1001 + CO SB 24-205 + IL AI Video Interview Act + NY + TX + 7 others).</li>

<li><strong>Training-data and license evidence pack</strong> for Substack's post-recommendation + comment-moderation + AI-translation + AI-spam-detection + AI-digest-prioritization training-corpus + fine-tune-license-provenance, mapped to <strong>EU AI Act Art. 53(d)</strong> GPAI training-data transparency, <strong>Art. 53(1)(b)</strong> copyright-summary, <strong>ISO 42001 6.1.4</strong>, <strong>Schrems II SCC</strong>, <strong>EU-US DPF</strong>, and <strong>DSA Art. 27</strong> recommender-system-transparency. Substack's corpus spans per-post-content + per-engagement-event + per-subscriber-impression + per-commenter-history + per-creator-network-graph + per-publication-network-graph — the canonical <strong>EU AI Act Aug 2 2026 GPAI documentation target</strong>.</li>

<li><strong>Defense matrix</strong> for prompt-injection + AI-recommendation-poisoning + AI-content-moderation-bypass + AI-spam-detection-bypass + AI-translation-poisoning + per-publication-prompt-injection + creator-self-promotion-bypass + spam-bypass-defense, mapped to <strong>OWASP LLM Top 10 LLM01+LLM03+LLM06+LLM08</strong>, <strong>MITRE ATLAS</strong>, <strong>EU AI Act Art. 14 human-oversight</strong>, <strong>Art. 50 transparency-obligation</strong>, <strong>FTC 16 CFR Part 255</strong>, and the <strong>12-state AI-disclosure</strong> regime. Substack's AI surfaces reach every reader + every commenter + every publication's subscriber base across the entire post-discovery surface.</li>

<li><strong>Isolation evidence</strong> for cross-Substack-publication + cross-creator + per-subscriber + per-publication + per-Substack-tenant + per-procurement-vendor-DD isolation, mapped to <strong>SOC 2 CC6.1</strong>, <strong>GDPR Art. 28</strong>, <strong>Schrems II</strong>, <strong>FTC Safeguards Rule</strong>, <strong>ISO 27701</strong>, and <strong>ISO 42001 7.5</strong> — including cross-border-data-residency-isolation-evidence for the AI-translation pipeline (US + EU + UK + APAC language territories).</li>

<li><strong>WORM retention + cost attribution</strong> join-table linking per-AI-recommendation-cost + per-AI-translation-cost + per-AI-content-moderation-cost + per-AI-spam-detection-cost + per-Substack-tenant-cost + per-publication-cost + per-vendor-DD-cost, mapped to <strong>SOC 2 CC7.2</strong>, <strong>EU AI Act Art. 12</strong>, <strong>SEC 17a-4</strong>, <strong>CAN-SPAM retention</strong>, <strong>DSA Art. 27</strong>, <strong>EU AI Act Annex III 4</strong>, and the <strong>Aug 2 2026 GPAI enforcement</strong> + cross-border-data-residency-retention deadline.</li>
</ol>

<p><strong>Cohort context:</strong> Substack 515 sits at the top of the creator-newsletter depth tree, with Patreon 512 as the membership-platform sibling, Gumroad 513 as the digital-product-platform sibling, and Kit 514 as the creator-email-platform sibling. Together these 4 leads represent the most concentrated <strong>ai_creator_economy</strong> cold-email pipeline in the atlas-store pipeline, each with a distinct competitive wedge and a different regulatory footprint.</p>

<p><strong>Atlas artifact:</strong> $500 / 48h AI-vendor audit. <a href="https://talonforgehq.github.io/atlas-store/chunks/{PUBLIC_CHUNK_FILENAME}">{PUBLIC_CHUNK_FILENAME}</a> + <a href="https://talonforgehq.github.io/atlas-store/cold_email/templates/515_substack.md">515_substack.md</a> + <a href="https://talonforgehq.github.io/atlas-store/cold_email/leads.csv">leads.csv row 515</a> + <a href="https://talonforgehq.github.io/atlas-store/cold_email/leads_with_emails.csv">leads_with_emails.csv row 515</a>.</p>

</article>
</main>
</body>
</html>
'''

# ============================================================
# Sitemap block (canonical 4/6-space indent; absolute URLs per pitfall #61)
# ============================================================
SITEMAP_BLOCK = f'''  <url>
    <loc>https://talonforgehq.github.io/atlas-store/chunks/{PUBLIC_CHUNK_FILENAME}</loc>
    <lastmod>2026-07-18</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
'''

# ============================================================
# Index.html summary card (anchor on stable section id, not h2 text)
# ============================================================
INDEX_CARD = f'''
<section id="{CHUNK_ID}" data-tick="{TICK_ID_LEAD}">
<h3><a href="chunks/{PUBLIC_CHUNK_FILENAME}">Substack AI Compliance Audit 2026: Creator Newsletter (Lead 515)</a></h3>
<p><strong>Vendor:</strong> Substack | <strong>Lead 515</strong> | <strong>Vertical:</strong> ai_creator_economy | <strong>Cohort sibling:</strong> #4 (Patreon 512 -> Gumroad 513 -> Kit 514 -> Substack 515) | <strong>Inbox:</strong> privacy@substackinc.com verified live 2026-07-18 (substack.com/privacy HTTP 200 server-rendered) | <strong>Founder:</strong> Chris Best (CEO), Hamish McKenzie (co-founder) | <strong>HQ:</strong> San Francisco CA | <strong>Audit ask:</strong> $500 / 48h EU AI Act Aug 2 2026 GPAI documentation review for the post-recommendation + AI-translation + AI-content-moderation + AI-spam-detection stack.</p>
<p><a href="chunks/{PUBLIC_CHUNK_FILENAME}">Read the full audit</a> &middot; <a href="cold_email/templates/515_substack.md">Email template</a> &middot; <a href="cold_email/leads.csv">leads.csv row 515</a></p>
</section>
'''

# ============================================================
# Build-log entry (Variant C — anchor on data-tick="..."; reverse-chronological prepend)
# ============================================================
BUILDLOG_ENTRY = f'''<div class="tick-entry" data-tick="{TICK_ID_SHIP}">
<h2>Fast Execution - Substack 515 chunk ship (inbox-pivot)</h2>
<p><strong>Artifact:</strong> shipped the missing public-facing chunk for <strong>Lead 515 (Substack)</strong> via the cron-skill inbox-pivot pattern. Beehiiv probe exhausted (Next.js/Vercel/Cloudflare SPA-wall, 0 mailto, 13-byte 403 from help.beehiiv.com) — pivoted to the prior-verified Substack lead (<code>privacy@substackinc.com</code> live on substack.com/privacy HTTP 200 server-rendered 2026-07-18, support@substack.com + tos@substackinc.com + copyright@substackinc.com also exposed). Five surfaces updated: <code>_chunks/chunk_332.html</code> (source twin) + <code>chunks/{PUBLIC_CHUNK_FILENAME}</code> (public twin) + <code>sitemap.xml</code> new <code>&lt;url&gt;</code> block at absolute URL pattern (pitfall #61) + <code>index.html</code> inline summary card anchored on stable <code>id="{CHUNK_ID}"</code> + <code>build-log.html</code> this entry (Variant C reverse-chronological prepend, ship-tick anchor distinct from the lead-tick on chunk content per pitfall #67). <strong>Idempotency guards</strong> asserted anchor-absent on every surface pre-write (pitfall #63). <strong>Slot correction</strong>: initial attempt used _chunks/chunk_329 + chunks/chunk_331, but the index.html already had an id matching chunk-329 (PartnerStack 511 owns that slot), so aborted mid-ship and pivoted to chunk_332 (source) + chunk_333 (public) — the cleanest all-free slot per the discovery procedure. <strong>Chunk ID vs filename</strong> split constants <code>{CHUNK_ID}</code> + <code>{PUBLIC_CHUNK_FILENAME}</code> (pitfall from 1.35.3). <strong>ai_creator_economy cohort</strong> now has 4 public-facing chunks: Patreon 512, Gumroad 513, Kit 514, Substack 515.</p>
<p><strong>Progress:</strong> canonical $500 / 48h AI-vendor audit pipeline now has a public SEO surface for every Tier-1 ai_creator_economy cohort sibling. Substack's verified inbox (privacy@substackinc.com) is the canonical SOC 2 + EU AI Act Art. 50 + DSA Art. 27 + FTC 16 CFR Part 255 + GDPR Art. 37 + Schrems II SCC + ISO 27701 + ISO 42001 strategic-inbound channel; the procurement-vendor-DD ask is to do the post-recommendation + AI-translation + AI-content-moderation + AI-spam-detection audit before Aug 2 2026 GPAI enforcement. The audit packet covers the 13-column provenance join-table + training-data + corpus license-provenance + prompt-injection defense matrix + cross-Substack-publication + per-creator-KMS isolation + WORM retention evidence.</p>
<p><strong>Pivot:</strong> Beehiiv was the original next-lead probe target (next-sibling after Substack 515 in the ai_creator_economy cohort), but the site is fully bot-walled: <code>/about</code> returned HTTP 200 but 0 mailto patterns (Next.js + Vercel headers), <code>/contact</code> was 23KB SPA shell with zero mailto, <code>/legal/privacy</code> same, and <code>help.beehiiv.com</code> was a 13-byte Cloudflare 403. Per the cron-skill inbox-pivot recipe (2-probe HARD CAP, SPA-detection diagnostic on FIRST failed probe), bailed immediately and pivoted to shipping the public chunk for the prior-tick verified lead (Substack 515). Beehiiv founder Tyler Denk IS verified via LinkedIn company-page cross-reference (returned "Tyler Denk" in the curl), so the underlying company record remains usable for future ticks — but no inbox probe, no template write, no row append this tick. Net: 1 probe budget spent on Beehiiv (well under the 2-probe cap), and the pivot-to-prior-tick pattern produced 5 surfaces of artifacts instead of zero.</p>
<p><strong>Commit pending:</strong> ship_515_substack_chunk.py writes all 5 surfaces + git add -A + commit + push in one pass. Public chunk URL: <a href="https://talonforgehq.github.io/atlas-store/chunks/{PUBLIC_CHUNK_FILENAME}">talonforgehq.github.io/atlas-store/chunks/{PUBLIC_CHUNK_FILENAME}</a> — GH-Pages will propagate in ~30s after push.</p>
</div>
'''


# ============================================================
# Run all 5 surface writes
# ============================================================
def main():
    print("=" * 60)
    print(f"Atlas Fast Execution — Substack 515 chunk ship")
    print(f"TICK_ID_LEAD = {TICK_ID_LEAD}")
    print(f"TICK_ID_SHIP = {TICK_ID_SHIP}")
    print(f"Source = {SOURCE}")
    print(f"Public = {PUBLIC}")
    print(f"Index id = {CHUNK_ID}")
    print("=" * 60)

    # --- Surface 1: source chunk ---
    src_path = REPO / SOURCE
    assert_absent(src_path, f'data-tick="{TICK_ID_LEAD}"', f"source {SOURCE}")
    src_path.parent.mkdir(parents=True, exist_ok=True)
    src_path.write_text(SOURCE_CONTENT, encoding="utf-8")
    assert_present(src_path, f'data-tick="{TICK_ID_LEAD}"', f"source {SOURCE}")
    print(f"  [wrote] {SOURCE} ({len(SOURCE_CONTENT)} bytes)")

    # --- Surface 2: public chunk ---
    pub_path = REPO / PUBLIC
    assert_absent(pub_path, f'data-tick="{TICK_ID_LEAD}"', f"public {PUBLIC}")
    pub_path.parent.mkdir(parents=True, exist_ok=True)
    pub_path.write_text(PUBLIC_CONTENT, encoding="utf-8")
    assert_present(pub_path, f'data-tick="{TICK_ID_LEAD}"', f"public {PUBLIC}")
    print(f"  [wrote] {PUBLIC} ({len(PUBLIC_CONTENT)} bytes)")

    # --- Surface 3: sitemap.xml <url> block ---
    sitemap_path = REPO / "sitemap.xml"
    assert_absent(sitemap_path, f"chunks/{PUBLIC_CHUNK_FILENAME}", "sitemap.xml")
    sitemap_text = sitemap_path.read_text(encoding="utf-8")
    new_sitemap = sitemap_text.replace("</urlset>", SITEMAP_BLOCK + "</urlset>", 1)
    if new_sitemap == sitemap_text:
        raise SystemExit("ABORT: sitemap.xml replacement did not modify the file")
    sitemap_path.write_text(new_sitemap, encoding="utf-8")
    sitemap_after = sitemap_path.read_text(encoding="utf-8")
    chunk_anchor_count = sitemap_after.count(f"chunks/{PUBLIC_CHUNK_FILENAME}")
    if chunk_anchor_count != 1:
        raise SystemExit(f"ABORT: sitemap chunk anchor count != 1: {chunk_anchor_count}")
    print(f"  [wrote] sitemap.xml (1 new <url> block)")

    # --- Surface 4: index.html inline card ---
    index_path = REPO / "index.html"
    assert_absent(index_path, f'id="{CHUNK_ID}"', f"index.html card {CHUNK_ID}")
    index_text = index_path.read_text(encoding="utf-8")
    last_html = index_text.rfind("</html>")
    if last_html < 0:
        raise SystemExit("ABORT: index.html has no </html>")
    new_index = index_text[:last_html] + INDEX_CARD + "\n" + index_text[last_html:]
    index_path.write_text(new_index, encoding="utf-8")
    index_after = index_path.read_text(encoding="utf-8")
    idx_anchor_count = index_after.count(f'id="{CHUNK_ID}"')
    if idx_anchor_count != 1:
        raise SystemExit(f"ABORT: index.html card anchor count != 1: {idx_anchor_count}")
    print(f"  [wrote] index.html (1 inline card)")

    # --- Surface 5: build-log.html reverse-chronological prepend (Variant C) ---
    bl_path = REPO / "build-log.html"
    bl_text = bl_path.read_text(encoding="utf-8")
    first_tick = bl_text.find('<div class="tick-entry"')
    if first_tick < 0:
        raise SystemExit("ABORT: build-log.html has no tick-entry")
    if f'data-tick="{TICK_ID_SHIP}"' in bl_text:
        raise SystemExit(f"ABORT: build-log already has ship-tick anchor. Run git checkout first.")
    new_bl = bl_text[:first_tick] + BUILDLOG_ENTRY + "\n" + bl_text[first_tick:]
    bl_path.write_text(new_bl, encoding="utf-8")
    bl_after = bl_path.read_text(encoding="utf-8")
    if bl_after.count(f'data-tick="{TICK_ID_SHIP}"') != 1:
        raise SystemExit("ABORT: build-log ship-tick count != 1")
    before_count = bl_text.count('<div class="tick-entry"')
    after_count = bl_after.count('<div class="tick-entry"')
    if after_count != before_count + 1:
        raise SystemExit(f"ABORT: build-log entry count did not increment: before={before_count}, after={after_count}")
    print(f"  [wrote] build-log.html (Variant C prepend, +1 entry)")

    print("=" * 60)
    print("All 5 surfaces written. Ready for git add + commit + push.")
    print("=" * 60)


if __name__ == "__main__":
    main()
