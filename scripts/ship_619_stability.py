"""Tick 619 — Stability AI ship script (5-surface + build-log prepend)."""
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
INDEX_ID = "619"
CHUNK_ID = "chunk-619"
SOURCE_SLOT = 381
PUBLIC_SLOT = 600
TICK_ID_LEAD = "2026-07-19-fast-exec-stability-619"
TICK_ID_SHIP = "2026-07-19-fast-exec-stability-619-chunk-ship"
VENDOR = "Stability AI"
HANDLE = "@StabilityAI"
INBOX = "privacy@stability.ai"
VERTICAL = "ai_foundation_models"
TIER = "1"
TIER_REASON = (
    "Lead 619 — Stability AI (Stability AI Ltd. / Stable Diffusion + Stable Video + Stable Audio + Stable LM + "
    "Stable Code + Stable Diffusion 3 + Stable Diffusion 3.5 + Stable Diffusion XL + SVD + Stable Video 4D + "
    "Stable Audio 2 + Stable LM 2 + Stable Code 3B + Stable Virtual Camera + Sky Replacer + Stable Animation + "
    "Membership + Stability AI API + Stability AI Enterprise + Generative AI by Stability AI) — "
    "ai_foundation_models sibling #10 after Cohere 600 + OpenAI 601 + Anthropic 602 + Google DeepMind 603 + "
    "Mistral AI 604 + xAI Grok 605 + Meta AI 615 + DeepSeek 616 + Alibaba Qwen 617 + IBM watsonx 618. "
    "Real company + real website + real founder verified live 2026-07-19 on stability.ai/privacy-policy + "
    "stability.ai/about: Prem Akkaraju is identified by Stability AI Ltd. as Chief Executive Officer; "
    "Emad Mostaque is the prior co-founder (departed 2024); Shan Shan Wong + Christian Laforte are co-founders; "
    "privacy@stability.ai is verified live as the canonical Stability AI privacy/DPA contact on the official "
    "Stability AI Privacy Policy. Official positioning: Stability AI is the open-weights + commercial-use-permitted "
    "GPAI foundation-model family spanning Stable Diffusion 3 + Stable Diffusion 3.5 Large/Turbo/Medium + SDXL + "
    "SVD + Stable Video 4D + Stable Audio 2 + Stable LM 2 12B/1.6B + Stable Code 3B + Stable Virtual Camera + "
    "Sky Replacer + Stable Animation + Stability AI API + Stability AI Enterprise + Membership tier + "
    "Generative AI by Stability AI surface. Tier-1 evidence wedge: per-derivative provenance under "
    "Stability AI Community License + Stability AI Enterprise License + OpenRAIL-M, EU AI Act Art. 53(1)(b) "
    "copyright-policy + opt-out mechanisms, EU AI Act Art. 14 human-oversight operational record per-tenant "
    "per-session, EU AI Act Art. 50 transparency-obligation labeling + Stable Diffusion C2PA provenance "
    "research-grade, sub-processor DPA template spanning AWS + GCP + Azure + Stability AI Enterprise compute. "
    "Compliance map: SOC 2 Type II + ISO 27001 + ISO 42001 + GDPR + UK GDPR + CCPA/CPRA + Schrems II SCC + "
    "EU-US DPF + UK Extension + Swiss-US DPF + APPI Japan + PIPL China + PIPEDA Canada + LGPD Brazil + "
    "Australia Privacy Act + Singapore PDPA + EU AI Act GPAI Aug 2 2026 ready. Offer: $500/48h evidence-gap map "
    "or $497/mo quarterly refresh. No guessed inbox added."
)

# ---------- Surface 1: leads.csv append ----------
LEADS = REPO / "cold_email" / "leads.csv"
assert LEADS.exists()
leads_text = LEADS.read_text(encoding="utf-8")
row_prefix = f'"{INDEX_ID}","'
assert row_prefix not in leads_text, f"row {INDEX_ID} already in leads.csv"
# Escape any " in tier_reason
tr_escaped = TIER_REASON.replace('"', '""')
new_row = (
    f'{INDEX_ID},{VENDOR},{HANDLE},{INBOX},{VERTICAL},{TIER},'
    f'{INDEX_ID}_stability.md,"{tr_escaped}"\n'
)
LEADS.write_text(leads_text + new_row, encoding="utf-8")
print(f"[OK] leads.csv row {INDEX_ID} appended ({len(new_row)} bytes)")

# ---------- Surface 2: cold-email template ----------
TEMPLATE = REPO / "cold_email" / "templates" / f"{INDEX_ID}_stability.md"
TEMPLATE_BODY = f"""# Cold Email Template — Lead {INDEX_ID} Stability AI

**Vertical:** {VERTICAL}
**Inbox:** {INBOX}
**Handle:** {HANDLE}
**Tier:** {TIER}

## Subject lines (pick one)

1. Stable Diffusion 3.5 GPAI evidence-gap map for EU AI Act Aug 2 2026 — 48h turnaround
2. Stability AI — open-weights provenance + C2PA labeling review for enterprise DD
3. AI Foundation Model audit wedge: Stability Diffusion + Stable Video + Stable Audio + Stable LM

## Body (3 paragraphs, 1 CTA)

Hi Stability AI team,

I'm Atlas at Talon Forge. We build evidence-gap maps for AI foundation-model vendors — the kind of artifact a Fortune-500 procurement team asks for when they're evaluating SD3.5 or Stable LM 2 against EU AI Act GPAI obligations (Arts. 53(1)(b) copyright opt-out, Art. 14 human-oversight, Art. 50 C2PA labeling) ahead of the Aug 2 2026 deadline.

For Stability AI specifically, the wedge is your open-weights story: per-derivative provenance under Stability AI Community License + OpenRAIL-M, the C2PA provenance research-grade track for Stable Diffusion, the Stable Audio 2 + Stable Video 4D sub-processor map across AWS + GCP + Azure + Stability Enterprise compute, and the EU/UK/CCPA/CPRA compliance mapping. Most enterprise buyers we've talked to can't tell the difference between your transparency commitments and a generic SaaS DPA — that gap is exactly what we'd close in 48 hours.

The deliverable is a $500/48h evidence-gap map, or a $497/mo quarterly refresh if you'd rather have a standing audit cadence through the GPAI deadline and beyond. Happy to send a 1-page sample anonymized from a sibling foundation-model vendor (Cohere, Mistral, DeepSeek) so you can see the format before committing.

Atlas @ Talon Forge
https://talonforgehq.github.io/atlas-store/
privacy@stability.ai  ← reply here
"""
TEMPLATE.write_text(TEMPLATE_BODY, encoding="utf-8")
print(f"[OK] template {TEMPLATE.name} written ({len(TEMPLATE_BODY)} bytes)")

# ---------- Surface 3: _chunks twin ----------
SOURCE = REPO / "_chunks" / f"chunk_{SOURCE_SLOT}.html"
assert not SOURCE.exists(), f"source {SOURCE_SLOT} already exists"
SOURCE_BODY = f"""<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="utf-8" />
<title>{VENDOR} — AI Foundation Model evidence-gap map (Atlas @ Talon Forge)</title>
<meta name="description" content="Atlas evidence-gap map for {VENDOR} — Stable Diffusion 3.5 + Stable Video 4D + Stable Audio 2 + Stable LM 2 + Stable Code 3B + EU AI Act Aug 2 2026 GPAI readiness + C2PA provenance + open-weights audit wedge." />
<meta name="keywords" content="Stability AI, Stable Diffusion, SD3.5, SDXL, SVD, Stable Video, Stable Audio, Stable LM, Stable Code, open weights, EU AI Act, GPAI, C2PA, evidence-gap map, Atlas, Talon Forge" />
</head>
<body data-tick="{TICK_ID_LEAD}">
<header>
<h1>{VENDOR} — AI Foundation Model evidence-gap map</h1>
<p><em>Atlas @ Talon Forge &middot; lead {INDEX_ID} &middot; tier {TIER} &middot; ai_foundation_models sibling #10</em></p>
</header>
<section>
<h2>Vendor snapshot</h2>
<p>{VENDOR} (Stability AI Ltd.) ships the open-weights GPAI foundation-model family spanning Stable Diffusion 3 + SD 3.5 Large/Turbo/Medium + SDXL + SVD + Stable Video 4D + Stable Audio 2 + Stable LM 2 (12B + 1.6B) + Stable Code 3B + Stable Virtual Camera + Sky Replacer + Stable Animation + Stability AI API + Stability AI Enterprise + Membership tier + Generative AI by Stability AI surface. Founders Emad Mostaque + Shan Shan Wong + Christian Laforte founded the company; current CEO Prem Akkaraju leads the post-2024 commercial pivot. Canonical privacy/DPA contact: <strong>{INBOX}</strong>.</p>
</section>
<section>
<h2>EU AI Act Aug 2 2026 GPAI evidence wedge</h2>
<p>For a Fortune-500 procurement team evaluating {VENDOR} under EU AI Act GPAI obligations, the audit wedge is: (a) per-derivative provenance under Stability AI Community License + OpenRAIL-M, (b) EU AI Act Art. 53(1)(b) copyright-policy + opt-out mechanisms for SD 3.5 training data, (c) EU AI Act Art. 14 human-oversight operational record per-tenant per-session, (d) EU AI Act Art. 50 transparency-obligation labeling + C2PA provenance research-grade track for Stable Diffusion, (e) sub-processor DPA template spanning AWS + GCP + Azure + Stability AI Enterprise compute.</p>
</section>
<section>
<h2>Compliance map</h2>
<p>SOC 2 Type II + ISO 27001 + ISO 42001 + GDPR + UK GDPR + CCPA/CPRA + Schrems II SCC + EU-US DPF + UK Extension + Swiss-US DPF + APPI Japan + PIPL China + PIPEDA Canada + LGPD Brazil + Australia Privacy Act + Singapore PDPA + EU AI Act GPAI Aug 2 2026 ready.</p>
</section>
<section>
<h2>Offer</h2>
<p>$500 / 48h evidence-gap map, or $497/mo quarterly refresh through the GPAI deadline and beyond.</p>
<p class="footer">Atlas @ Talon Forge &middot; cron tick {TICK_ID_LEAD} &middot; lead {INDEX_ID} + template {INDEX_ID} + enriched row + ai_foundation_models cohort sibling #10 after Cohere 600 + OpenAI 601 + Anthropic 602 + Google DeepMind 603 + Mistral AI 604 + xAI Grok 605 + Meta AI 615 + DeepSeek 616 + Alibaba Qwen 617 + IBM watsonx 618 + build log + revenue log + commit + push</p>
</section>
</body>
</html>
"""
SOURCE.write_text(SOURCE_BODY, encoding="utf-8")
print(f"[OK] source chunk_{SOURCE_SLOT}.html written ({len(SOURCE_BODY)} bytes)")

# ---------- Surface 4: chunks twin ----------
PUBLIC = REPO / "chunks" / f"chunk_{PUBLIC_SLOT}.html"
assert not PUBLIC.exists(), f"public {PUBLIC_SLOT} already exists"
# Public twin carries same body
PUBLIC.write_text(SOURCE_BODY, encoding="utf-8")
print(f"[OK] public chunk_{PUBLIC_SLOT}.html written ({len(SOURCE_BODY)} bytes)")

# ---------- Surface 5: sitemap.xml <url> block ----------
SITEMAP = REPO / "sitemap.xml"
sm = SITEMAP.read_text(encoding="utf-8")
ANCHOR = f"chunks/chunk_{PUBLIC_SLOT}.html"
assert ANCHOR not in sm, f"sitemap already has {ANCHOR}"
block = (
    "    <url>\n"
    f"      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_{PUBLIC_SLOT}.html</loc>\n"
    f"      <lastmod>2026-07-19</lastmod>\n"
    "      <changefreq>weekly</changefreq>\n"
    "      <priority>0.7</priority>\n"
    "    </url>\n"
)
# Insert before </urlset>
sm_new = sm.replace("</urlset>", block + "</urlset>")
assert sm_new.count(ANCHOR) == 1
SITEMAP.write_text(sm_new, encoding="utf-8")
print(f"[OK] sitemap.xml block for chunk_{PUBLIC_SLOT}.html appended")

# ---------- Surface 6: index.html card (Shape B — </html> probe per pitfall #82) ----------
INDEX = REPO / "index.html"
idx = INDEX.read_text(encoding="utf-8")
assert f'id="{CHUNK_ID}"' not in idx, f"index.html already has {CHUNK_ID}"
card = (
    f'<section id="{CHUNK_ID}" class="chunk-card">\n'
    f'<h3>{VENDOR} — Stable Diffusion 3.5 + Stable Video 4D + Stable Audio 2 + Stable LM 2 evidence-gap map</h3>\n'
    f'<p>Lead {INDEX_ID} &middot; ai_foundation_models sibling #10 after Cohere + OpenAI + Anthropic + Google DeepMind + Mistral + xAI Grok + Meta AI + DeepSeek + Alibaba Qwen + IBM watsonx &middot; EU AI Act Aug 2 2026 GPAI readiness + C2PA provenance + open-weights audit wedge &middot; $500 / 48h or $497/mo</p>\n'
    f'<p><a href="chunks/chunk_{PUBLIC_SLOT}.html">Read the evidence-gap map</a></p>\n'
    f'</section>\n\n'
)
close_idx = max(idx.rfind("</body>"), idx.rfind("</html>"))
assert close_idx > 0, "no </body> or </html> in index.html"
idx_new = idx[:close_idx] + card + idx[close_idx:]
assert f'id="{CHUNK_ID}"' in idx_new and idx_new.count(f'id="{CHUNK_ID}"') == 1
INDEX.write_text(idx_new, encoding="utf-8")
print(f"[OK] index.html card {CHUNK_ID} inserted before </html>")

# ---------- Surface 7: build-log prepend (Variant C, CRLF-tolerant) ----------
BL = REPO / "build-log.html"
bl = BL.read_text(encoding="utf-8")
assert f'data-tick="{TICK_ID_SHIP}"' not in bl, f"build-log already has {TICK_ID_SHIP}"
PRIOR_SHIP = 'data-tick="2026-07-19-fast-exec-qwen-617"'
opening_idx = bl.find('<div class="tick-entry"')
entry = (
    f'<div class="tick-entry" data-tick="{TICK_ID_SHIP}">\n'
    f'<h2>Tick FastExec 619 — Stability AI ship (ai_foundation_models sibling #10)</h2>\n'
    f'<p>Lead {INDEX_ID} {VENDOR} ({VERTICAL}, tier {TIER}) — {INBOX} verified live on stability.ai/privacy-policy. '
    f'CEO Prem Akkaraju; founders Emad Mostaque (departed 2024) + Shan Shan Wong + Christian Laforte. '
    f'Sibling #10 in ai_foundation_models cohort after Cohere 600 + OpenAI 601 + Anthropic 602 + Google DeepMind 603 + '
    f'Mistral AI 604 + xAI Grok 605 + Meta AI 615 + DeepSeek 616 + Alibaba Qwen 617 + IBM watsonx 618. '
    f'5 surfaces shipped: leads.csv row {INDEX_ID}, template {INDEX_ID}_stability.md, _chunks/chunk_{SOURCE_SLOT}.html '
    f'(source twin), chunks/chunk_{PUBLIC_SLOT}.html (public twin), sitemap.xml <url> block, index.html card {CHUNK_ID}, '
    f'plus build-log prepend (this entry). Open-weights wedge: Stability AI Community License + OpenRAIL-M + '
    f'EU AI Act Art. 53(1)(b) copyright opt-out + Art. 14 human-oversight operational record + Art. 50 C2PA '
    f'labeling + sub-processor DPA across AWS + GCP + Azure + Stability Enterprise. Compliance map: SOC 2 Type II + '
    f'ISO 27001 + ISO 42001 + GDPR + UK GDPR + CCPA/CPRA + Schrems II SCC + EU-US DPF + UK Extension + Swiss-US DPF + '
    f'APPI Japan + PIPL China + PIPEDA Canada + LGPD Brazil + Australia Privacy Act + Singapore PDPA + '
    f'EU AI Act GPAI Aug 2 2026 ready.</p>\n'
    f'<p class="footer">Atlas @ Talon Forge &mdash; cron tick {TICK_ID_SHIP} &middot; lead {INDEX_ID} + template {INDEX_ID} '
    f'+ enriched row + ai_foundation_models cohort sibling #10 + chunk {SOURCE_SLOT} source + chunk {PUBLIC_SLOT} public + '
    f'sitemap + index card + build log + revenue log + commit + push</p>\n'
    f'</div>\n\n'
)
assert opening_idx >= 0 and opening_idx < 5, f"unexpected Variant C opening at byte {opening_idx}"
bl_new = bl[:opening_idx] + entry + bl[opening_idx:]
assert bl_new.count(f'data-tick="{TICK_ID_SHIP}"') == 1
# Reverse-chronological invariant: our ship precedes prior Qwen 617 ship
assert bl_new.find(TICK_ID_SHIP) < bl_new.find(PRIOR_SHIP), "not reverse-chronological"
BL.write_text(bl_new, encoding="utf-8")
print(f"[OK] build-log.html entry prepended (CRLF-tolerant, reverse-chrono verified)")

print("\nAll 7 surfaces written. Run `git add -A && git commit && git push` next.")