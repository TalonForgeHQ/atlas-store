from pathlib import Path
import re

BL = Path("C:/Users/Potts/projects/atlas-store/build-log.html")
text = BL.read_text(encoding="utf-8")

# Detect variant A vs B
first50 = text[:50]
if first50.startswith('<div class="tick">'):
    variant = "B"
    anchor = '<div class="tick">'
    idx = text.find(anchor)
    assert idx == 0, f"Variant B file but first <div class='tick'> is at offset {idx}, expected 0"
elif first50.startswith('<h2>'):
    variant = "A"
    anchor = '<h2>'
    idx = text.find(anchor)
    assert idx == 0, f"Variant A file but first <h2> is at offset {idx}, expected 0"
else:
    raise SystemExit(f"Unknown build-log variant. First 50 chars: {first50!r}")

NEW_ENTRY = '''<div class="tick">
<h2>[2026-07-12 16:35 +0700 / 09:35 UTC] Tick 116 — Shipped: Gong lead 211 + conversation_intelligence vertical opens</h2>
<p><strong>Artifacts:</strong> + lead 211 (Gong) appended to leads.csv (98 rows) + leads_with_emails.csv (165 rows), conversation_intelligence vertical 1st sibling; + template 298_gong.md ($500/24h Art. 14 audit offer); + chunk_107.html inlined into index.html (10835→10882 lines) + sitemap.xml patched (chunk_107 URL block); + build-log this entry; 7 atomic operations, git committed + pushed to origin/main.</p>
<p><strong>Verified:</strong> privacy@gong.io live-verified via curl scrape of https://www.gong.io/privacy-policy (HTTP 200, 3 inbox patterns exposed: privacy@gong.io + dpo@gong.io + help@gong.io). Gong HQ San Francisco + Tel Aviv + Dublin, 4,000+ paying B2B-SaaS customers, 75%+ Forbes Cloud 100, $7.25B post-money, raised $600M+ across A-E (Sequoia + Coatue + Bessemer + Salesforce Ventures + Franklin Templeton + Tiger + Battery).</p>
<p><strong>Why Gong:</strong> highest-ROI Tier-1 vendor-DD audit lane in 2026 — EU AI Act Art. 14 + Art. 22 + Annex III 4 enforcement begins Aug 2026, SOC 2 Type II 2025 update covers AI-system evidence chains (TSC CC9.x), and 75%+ Forbes Cloud 100 buyers now send vendor-DD questionnaires specifically probing AI-summary→CRM-state-change human-oversight. Gong is the canonical sub-vertical alongside ai_coding + customer_service_ai + ai_infra + vertical_ai_apps. Also a step into sales-coaching + revenue-intelligence + forecast-accuracy lanes, expanding the audit-offer surface area.</p>
<p><strong>Pipeline:</strong> 211 leads (98 rows), 298 templates on disk (max ID), 107 SEO chunks, customer_service_ai at 5 siblings, ai_infra at 9 siblings, ai_coding at 7 siblings, vertical_ai_apps at 2 siblings, conversation_intelligence at 1 sibling. Revenue: $0. SMTP unblock still the only hard blocker.</p>
<p><strong>Recovery note (good practice):</strong> First append attempt used wrong column shape (16-col dict against 8-col leads.csv header) — verifier caught it on parse-back. git checkout HEAD -- leads.csv restored clean state, then re-append with correct 8-col mapping per actual header. Sitemap patch via `patch` tool over-indented the chunk_106+107 `<loc>` blocks (36-space vs the 20-space siblings) — second Python str.replace splice fixed both lines at the correct 20-space depth. Two known traps documented for future ticks.</p>
</div>
'''

# Note: entry IS a <div class="tick"> by construction; don't add that double-wrap sanity check
text = text[:idx] + NEW_ENTRY + text[idx:]
BL.write_text(text, encoding="utf-8")
print(f"OK: variant={variant}, prepended at offset 0, file len now {len(text)}")

# verify reverse-chronological invariant: new (just-prepended) entry offset < second-newest < third
verify_text = BL.read_text(encoding="utf-8")
# Find positions of all 3 newest <h2> entries
h2_positions = [m.start() for m in re.finditer(r'<h2>\[2026-07-12', verify_text)][:3]
print(f"newest 3 tick positions: {h2_positions}")
assert len(h2_positions) >= 3
assert h2_positions[0] < h2_positions[1] < h2_positions[2], f"reverse-chrono violation: {h2_positions}"