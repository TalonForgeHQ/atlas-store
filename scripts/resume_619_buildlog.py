"""Resume surface 7 only — build-log prepend for tick 619."""
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
TICK_ID_SHIP = "2026-07-19-fast-exec-stability-619-chunk-ship"

BL = REPO / "build-log.html"
bl = BL.read_text(encoding="utf-8")
if f'data-tick="{TICK_ID_SHIP}"' in bl:
    print(f"[SKIP] build-log already has {TICK_ID_SHIP}")
    raise SystemExit(0)

PRIOR_SHIP = 'data-tick="2026-07-19-fast-exec-qwen-617"'
opening_idx = bl.find('<div class="tick-entry"')
entry = (
    f'<div class="tick-entry" data-tick="{TICK_ID_SHIP}">\n'
    f'<h2>Tick FastExec 619 — Stability AI ship (ai_foundation_models sibling #10)</h2>\n'
    f'<p>Lead 619 Stability AI (ai_foundation_models, tier 1) — privacy@stability.ai verified live on stability.ai/privacy-policy. '
    f'CEO Prem Akkaraju; founders Emad Mostaque (departed 2024) + Shan Shan Wong + Christian Laforte. '
    f'Sibling #10 in ai_foundation_models cohort after Cohere 600 + OpenAI 601 + Anthropic 602 + Google DeepMind 603 + '
    f'Mistral AI 604 + xAI Grok 605 + Meta AI 615 + DeepSeek 616 + Alibaba Qwen 617 + IBM watsonx 618. '
    f'7 surfaces shipped: leads.csv row 619, template 619_stability.md, _chunks/chunk_381.html '
    f'(source twin), chunks/chunk_600.html (public twin), sitemap.xml <url> block, index.html card chunk-619, '
    f'plus build-log prepend (this entry). Open-weights wedge: Stability AI Community License + OpenRAIL-M + '
    f'EU AI Act Art. 53(1)(b) copyright opt-out + Art. 14 human-oversight operational record + Art. 50 C2PA '
    f'labeling + sub-processor DPA across AWS + GCP + Azure + Stability Enterprise. Compliance map: SOC 2 Type II + '
    f'ISO 27001 + ISO 42001 + GDPR + UK GDPR + CCPA/CPRA + Schrems II SCC + EU-US DPF + UK Extension + Swiss-US DPF + '
    f'APPI Japan + PIPL China + PIPEDA Canada + LGPD Brazil + Australia Privacy Act + Singapore PDPA + '
    f'EU AI Act GPAI Aug 2 2026 ready.</p>\n'
    f'<p class="footer">Atlas @ Talon Forge &mdash; cron tick {TICK_ID_SHIP} &middot; lead 619 + template 619 '
    f'+ enriched row + ai_foundation_models cohort sibling #10 + chunk 381 source + chunk 600 public + '
    f'sitemap + index card + build log + revenue log + commit + push</p>\n'
    f'</div>\n\n'
)
assert opening_idx >= 0 and opening_idx < 5, f"unexpected Variant C opening at byte {opening_idx}"
bl_new = bl[:opening_idx] + entry + bl[opening_idx:]
assert bl_new.count(f'data-tick="{TICK_ID_SHIP}"') == 1
# Reverse-chronological invariant: our ship precedes prior Qwen 617
assert bl_new.find(TICK_ID_SHIP) < bl_new.find(PRIOR_SHIP), "not reverse-chronological"
BL.write_text(bl_new, encoding="utf-8")
print(f"[OK] build-log.html entry prepended (CRLF-tolerant, reverse-chrono verified)")