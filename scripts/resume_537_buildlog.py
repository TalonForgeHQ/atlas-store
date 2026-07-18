"""Resume ship_537_xendoo: prepend build-log entry only (CSV already done)."""
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
BUILD_LOG = REPO / "build-log.html"
TICK_ID = "2026-07-19-fast-exec-xendoo-537"
anchor = f'data-tick="{TICK_ID}"'

bl = BUILD_LOG.read_text(encoding="utf-8")

# Early-exit idempotency: if already prepended, exit cleanly
if bl.count(anchor) == 1:
    opening_idx = bl.find('<div class="tick-entry"')
    our_attr_idx = bl.find(anchor)
    opening_tag_end = opening_idx + len('<div class="tick-entry" ')
    assert our_attr_idx == opening_tag_end, f"anchor at {our_attr_idx}, expected {opening_tag_end}"
    entries_count = bl.count('<div class="tick-entry"')
    print(f"RESUME: {TICK_ID} already prepended at top — no-op")
    print(f"  build-log entries: {entries_count}")
    raise SystemExit(0)
elif bl.count(anchor) > 1:
    dupes = bl.count(anchor)
    raise SystemExit(f"ERROR: {TICK_ID} appears {dupes} times — manual dedup needed")

# Prepend
opening_idx = bl.find('<div class="tick-entry"')
assert opening_idx == 0, f"build-log not in Variant C (opening_idx={opening_idx}, expected 0)"

NEW_ENTRY = (
    f'<div class="tick-entry" {anchor}>\n'
    f'<h2>Tick 537 — Xendoo ship (bookkeeping_ai_ops cohort sibling #6)</h2>\n'
    f'<p><strong>2026-07-19 fast-exec</strong> · Lead 537 Xendoo (support@xendoo.com verified live 2026-07-19 via xendoo.com/privacy-policy mailto:) · '
    f'founder Lil Roberts (Founder + CEO, verified via /meet-the-team page h3 class wpr-member-name). '
    f'3-surface ship (CSV row + template 537_xendoo.md + build-log prepend). '
    f'bookkeeping_ai_ops cohort now 6/6 anchored (Bookkeep 352 + Bench 355 + Pilot.com 357 + Botkeeper 358 + Catch 359 + Xendoo 537); '
    f'Xendoo anchors the multi-vertical SMB bookkeeping + fractional-CFO + tax-services lane (eCommerce + franchise + hospitality + medical + professional services + technology verticals + AdvisorConnect partner channel + Insights-XP + Power-of-3 + Q2X + ZorConnect). '
    f'5 audit gaps surfaced: (1) end-to-end 13-col per-client-id to per-engagement-id to per-QBO/Xero/NetSuite-tenant-id to per-monthly-close-id to per-bookkeeper-id to per-reconciler-id to per-fractional-CFO-id to per-tax-prep-id to per-IRS-IRC-7515-supervision-id to per-state-board-of-accountancy-license-id to per-audit-log-entry-id to per-procurement-vendor-DD-event-id to per-residency-region-id provenance join-table per SOC 2 CC7.2 + GLBA-Safeguards + IRS-IRC-7515 + FTC-Safeguards-Rule + state-board-of-accountancy + multi-state-privacy + multi-state-CPA-license-discipline, '
    f'(2) Xendoo bookkeeping + fractional-CFO + tax workpaper corpus + per-bookkeeper GLBA-trained + per-reconciler CFC-trained + per-tax-prep CPA-licensed history + per-client PII (EIN + SSN + bank-account + revenue-detail) license-provenance + LLM-training-data-transparency + IRS-Circular-230 + state-board-of-accountancy + multi-state-CPA-license-discipline, '
    f'(3) prompt-injection + LLM-bookkeeper-poisoning + fractional-CFO-assistant-poisoning + tax-prep-assistant-poisoning + client-PII-exfiltration + QBO/Xero/NetSuite-tenant-prompt-injection + per-bookkeeper-prompt-injection-defense per OWASP LLM Top 10 LLM01+LLM03+LLM06+LLM08 + MITRE ATLAS + GLBA-Safeguards-Rule + IRS Pub 4557 + FTC Safeguards Rule + state-board-of-accountancy + multi-state-privacy, '
    f'(4) cross-Xendoo-client + per-tenant-KMS-key-id + per-client-QBO/Xero/NetSuite-tenant + cross-border-data-residency-isolation + per-engagement-isolation per SOC 2 CC6.1 + GLBA Safeguards Rule + IRS-IRC-7515 + FTC Safeguards Rule + state-board-of-accountancy + multi-state-privacy (CCPA/CPRA + VA-VCDPA + CO-CPA + CT-CTDPA + UT-UCPA + TX-TDPSA + FL-FDBR + OR-OCPA + MT-MCDPA + IRS-Pub-4557), '
    f'(5) WORM retention + cost-attribution join-table linking per-client-cost + per-engagement-cost to per-monthly-close-cost to per-bookkeeper-cost to per-reconciler-cost to per-fractional-CFO-cost to per-tax-prep-cost to per-LLM-token-cost to per-multi-state-board-of-accountancy-cost to per-procurement-vendor-DD-event-cost per SOC 2 CC7.2 + IRS-IRC-7515-recordkeeping + IRS-Circular-230-recordkeeping + GLBA-recordkeeping + FTC-Safeguards-Rule-recordkeeping + state-board-of-accountancy-recordkeeping + multi-state-privacy-recordkeeping + multi-state-CPA-license-discipline-recordkeeping. '
    f'2-probe inbox-verify budget honored (Ramp /privacy probe 1 was SPA-wall 778KB but zero mailto → immediate pivot to Xendoo probe 1 → verified support@xendoo.com on /privacy-policy; probe 2 = /meet-the-team for Lil Roberts founder name). '
    f'next tick: 538 = bookkeeping_ai_ops depth continued (Indinero or 1-800Accountant for fractional-CFO + tax depth) OR pivot to vector_database (5 leads, 5/5 needed) for new-vertical breadth.</p>\n'
    f'<p><strong>Inbox-verify budget:</strong> 2 probes used (Ramp SPA-wall pivot + Xendoo verified). '
    f'<strong>Cohort progression:</strong> bookkeeping_ai_ops 6/6 anchored, ai_data_labeling 8/8 anchored, ai_revenue_intelligence 6/6, vector_database 5/5. '
    f'<strong>Next-tick signal:</strong> vertical breadth over depth — vector_database needs only 1 more for full-vertical cohesion; ai_meeting_infrastructure 5/5 needs depth.</p>\n'
    f'</div>\n'
)

new_bl = NEW_ENTRY + bl
assert new_bl.count(NEW_ENTRY.strip()) == 1
assert new_bl.count('<div class="tick-entry"') == bl.count('<div class="tick-entry"') + 1
BUILD_LOG.write_text(new_bl, encoding="utf-8")

# Re-verify after write
bl2 = BUILD_LOG.read_text(encoding="utf-8")
opening_idx2 = bl2.find('<div class="tick-entry"')
our_attr_idx2 = bl2.find(anchor)
opening_tag_end2 = opening_idx2 + len('<div class="tick-entry" ')
assert opening_idx2 == 0
assert our_attr_idx2 == opening_tag_end2, f"after write: anchor at {our_attr_idx2}, expected {opening_tag_end2}"
assert bl2.count(anchor) == 1
bl_before = bl.count('<div class="tick-entry"')
bl_after = bl2.count('<div class="tick-entry"')
print(f"RESUME OK: build-log entries {bl_before} -> {bl_after}; {TICK_ID} prepended at top")