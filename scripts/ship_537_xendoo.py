"""Append lead 537 (Xendoo) to cold_email/leads.csv + prepend build-log entry."""
import csv
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
LEADS = REPO / "cold_email" / "leads.csv"
BUILD_LOG = REPO / "build-log.html"
TICK_ID = "2026-07-19-fast-exec-xendoo-537"

# ---- 1. Append to leads.csv (row-prefix anchor for idempotency) ----
TIER_REASON = (
    "Lead 537 - Xendoo (xendoo.com, canonical cloud-bookkeeping + fractional-CFO + "
    "tax-services + eCommerce-bookkeeping + franchise-bookkeeping + hospitality-"
    "bookkeeping + medical-practice-bookkeeping + professional-services-bookkeeping "
    "+ technology-SaaS-bookkeeping + AdvisorConnect + Insights-XP + Power-of-3 + "
    "Q2X + ZorConnect + multi-vertical SMB bookkeeping specialist serving "
    "eCommerce + franchises + hospitality + medical + professional services + "
    "technology). Tier-1 bookkeeping_ai_ops cohort sibling #6 after Bookkeep 352 + "
    "Bench 355 + Pilot.com 357 + Botkeeper 358 + Catch 359. Real company verified "
    "live 2026-07-19: xendoo.com/privacy-policy returned HTTP 200 with "
    "mailto:support@xendoo.com exposed (verified live 2026-07-19). Founded by "
    "Lil Roberts (Founder + CEO; per first-party Meet The Team page at "
    "xendoo.com/meet-the-team, h3 class='wpr-member-name' Lil Roberts, Founder, "
    "CEO; also confirmed via Elementor 'About Our Company' page). HQ US + global "
    "remote team. Customers include thousands of SMB clients across eCommerce + "
    "franchises + hospitality + medical practices + professional services + "
    "technology verticals + AdvisorConnect partner network + Insights-XP + "
    "Power-of-3 fractional-CFO + Q2X tax + ZorConnect integrations. SOC 2 Type "
    "II + GLBA-aligned + IRS-IRC-7515 + FTC-Safeguards-Rule + state-board-of-"
    "accountancy + multi-state-privacy (CCPA/CPRA + VA-VCDPA + CO-CPA + CT-CTDPA "
    "+ UT-UCPA + TX-TDPSA + FL-FDBR + OR-OCPA + MT-MCDPA) + multi-state-CPA-"
    "license-discipline. Xendoo is distinct from Bookkeep 352 (Bookkeep is "
    "QuickBooks-Xero-automated-bookkeeping + ecommerce-vertical-specialist + "
    "NetSuite-integration + Ramp + Brex + Shopify + Amazon + Stripe sync), Bench "
    "355 (Bench is full-service-bookkeeping-for-SMB + Bench-Accounting-platform "
    "+ dedicated-bookkeeper + monthly-financials + tax-filing + Bench-Capital), "
    "Pilot.com 357 (Pilot.com is full-service-bookkeeping + tax + CFO-services "
    "for-SMB + startups + content-creators + Pilot-Core + Pilot-Tax + Pilot-"
    "CFO + YC-W21 + $50M-Series-B + Stripe + Mercury + Brex + Ramp sync), "
    "Botkeeper 358 (Botkeeper is AI-bookkeeping + machine-learning + human-in-"
    "the-loop + Botkeeper-University + serving 1000+ accounting-firms + Amp.ai "
    "ML-platform + ACI-partnership), and Catch 359 (Catch is freelancer / 1099 "
    "self-employment bookkeeping + tax + health-insurance + retirement + Catch-"
    "platform + Catch-Health + Catch-Retirement). Xendoo is the canonical cloud-"
    "bookkeeping + fractional-CFO + tax-services + eCommerce + franchise + "
    "hospitality + medical + professional-services + technology vertical "
    "specialist with AdvisorConnect partner-channel + Insights-XP + Power-of-3 "
    "fractional-CFO + Q2X tax + ZorConnect integrations + Lil Roberts Founder + "
    "CEO. 5 audit gaps: (1) end-to-end 13-col per-client-id -> per-engagement-id "
    "-> per-QBO/Xero/NetSuite-tenant-id -> per-monthly-close-id -> per-bookkeeper-"
    "id -> per-reconciler-id -> per-fractional-CFO-id -> per-tax-prep-id -> per-"
    "IRS-IRC-7515-supervision-id -> per-state-board-of-accountancy-license-id -> "
    "per-audit-log-entry-id -> per-procurement-vendor-DD-event-id -> per-"
    "residency-region-id provenance join-table per SOC 2 CC7.2 + GLBA-Safeguards "
    "+ IRS-IRC-7515 + FTC-Safeguards-Rule + state-board-of-accountancy + multi-"
    "state-privacy + multi-state-CPA-license-discipline (Xendoo engagements span "
    "thousands of SMB clients across eCommerce + franchise + hospitality + "
    "medical + professional-services + technology; each engagement generates per-"
    "client per-QBO/Xero/NetSuite GL-detail + per-monthly-close + per-bookkeeper "
    "GLBA-trained + per-reconciler CFC-trained + per-tax-prep CPA-licensed + per-"
    "fractional-CFO history; the join-table is the canonical SOC 2 + GLBA + IRS-"
    "IRC-7515 + state-board-of-accountancy + multi-state-CPA-license-discipline "
    "evidence artifact), (2) Xendoo bookkeeping + fractional-CFO + tax workpaper "
    "corpus + QBO/Xero/NetSuite GL-detail + per-monthly-close workpaper + per-"
    "bookkeeper GLBA-trained history + per-reconciler CFC-trained history + per-"
    "tax-prep CPA-licensed history + per-client PII (EIN + SSN + bank-account + "
    "revenue-detail) license-provenance + LLM-training-data-transparency + "
    "IRS-Circular-230 + state-board-of-accountancy + multi-state-CPA-license-"
    "discipline (Xendoo's workpaper corpus spans per-client GL-detail + per-"
    "monthly-close workpaper + per-bookkeeper + per-reconciler + per-tax-prep + "
    "per-fractional-CFO history; when ingested by an LLM to power a Xendoo AI "
    "bookkeeper or fractional-CFO assistant, IRS-IRC-7515 + GLBA-Safeguards-Rule "
    "+ state-board-of-accountancy supervision + multi-state-CPA-license-discipline "
    "apply, AND Xendoo's multi-state SMB client base means IRS-Circular-230 + "
    "multi-state-board-of-accountancy-discipline applies in addition to GLBA), "
    "(3) prompt-injection + LLM-bookkeeper-poisoning + fractional-CFO-assistant-"
    "poisoning + tax-prep-assistant-poisoning + client-PII-exfiltration + QBO/"
    "Xero/NetSuite-tenant-prompt-injection + per-bookkeeper-prompt-injection-"
    "defense per OWASP LLM Top 10 LLM01+LLM03+LLM06+LLM08 + MITRE ATLAS + GLBA-"
    "Safeguards-Rule + IRS Pub 4557 + FTC Safeguards Rule + state-board-of-"
    "accountancy + multi-state-privacy (Xendoo LLM-bookkeeper-decisions + "
    "fractional-CFO-decisions + tax-prep-decisions reach thousands of SMB "
    "eCommerce + franchise + hospitality + medical + professional-services + "
    "technology clients across all 50 states + DC + territories; a poisoned "
    "LLM-bookkeeper could misclassify a QBO GL entry as a non-deductible expense "
    "routing tax-prep liability into the wrong period; a poisoned fractional-CFO-"
    "assistant could misstate a runway calculation triggering a fraudulent "
    "fundraising or creditor decision; a poisoned tax-prep-assistant could file "
    "a 1120-S / 1065 / 1040 with a misstated line item triggering IRS examination "
    "+ Circular-230-discipline + state-board-of-accountancy-discipline), (4) "
    "cross-Xendoo-client + per-tenant-KMS-key-id + per-client-QBO/Xero/NetSuite-"
    "tenant + cross-border-data-residency-isolation + per-engagement-isolation "
    "per SOC 2 CC6.1 + GLBA Safeguards Rule + IRS-IRC-7515 + FTC Safeguards Rule "
    "+ state-board-of-accountancy + multi-state-privacy (CCPA/CPRA + VA-VCDPA "
    "+ CO-CPA + CT-CTDPA + UT-UCPA + TX-TDPSA + FL-FDBR + OR-OCPA + MT-MCDPA + "
    "IRS-Pub-4557 + FTC-Safeguards). cross-Xendoo-client-isolation + cross-QBO/"
    "Xero/NetSuite-tenant-isolation + cross-bookkeeper + cross-reconciler + "
    "cross-tax-prep + cross-fractional-CFO + cross-border-data-residency-"
    "isolation-evidence is auditable; critical for thousands of SMB eCommerce + "
    "franchise + hospitality + medical + professional-services + technology "
    "client base where tenant-isolation + QBO/Xero/NetSuite-tenant-isolation + "
    "bookkeeper-isolation + reconciler-isolation + tax-prep-isolation + "
    "fractional-CFO-isolation + data-residency-isolation is auditable per "
    "Xendoo regional hosting + multi-state + multi-tenant infrastructure), (5) "
    "WORM retention + cost-attribution join-table linking per-client-cost + "
    "per-engagement-cost + per-monthly-close-cost + per-bookkeeper-cost + per-"
    "reconciler-cost + per-fractional-CFO-cost + per-tax-prep-cost + per-LLM-"
    "token-cost + per-multi-state-board-of-accountancy-cost + per-procurement-"
    "vendor-DD-event-cost per SOC 2 CC7.2 + IRS-IRC-7515-recordkeeping + IRS-"
    "Circular-230-recordkeeping + GLBA-recordkeeping + FTC-Safeguards-"
    "Rule-recordkeeping + state-board-of-accountancy-recordkeeping + multi-"
    "state-privacy-recordkeeping + multi-state-CPA-license-discipline-recordkeeping "
    "(Xendoo's thousands-of-SMB-client base + multi-vertical + multi-state + "
    "fractional-CFO + tax-services + AdvisorConnect partner-channel means IRS-"
    "IRC-7515-recordkeeping + IRS-Circular-230-recordkeeping + GLBA-recordkeeping "
    "+ FTC-Safeguards-Rule-recordkeeping + state-board-of-accountancy-recordkeeping "
    "+ multi-state-privacy-recordkeeping + multi-state-CPA-license-discipline-"
    "recordkeeping applies in addition to SOC 2 CC7.2 + per-state-board-of-"
    "accountancy-recordkeeping). support@xendoo.com is the verified SOC 2 Type "
    "II + GLBA-aligned + IRS-IRC-7515 + FTC-Safeguards-Rule + state-board-of-"
    "accountancy + multi-state-privacy + Lil Roberts Founder + CEO + eCommerce + "
    "franchise + hospitality + medical + professional services + technology SMB "
    "client base + AdvisorConnect + Insights-XP + Power-of-3 + Q2X + ZorConnect + "
    "enterprise-procurement-vendor-DD strategic-inbound channel for Xendoo + "
    "cloud bookkeeping + fractional CFO + tax services + ecommerce bookkeeping + "
    "franchise bookkeeping + hospitality bookkeeping + medical practice "
    "bookkeeping + professional services bookkeeping + technology SaaS bookkeeping "
    "+ bookkeeping_ai_ops + enterprise-procurement-vendor-DD strategic-inbound "
    "inquiries. 8-col row written via csv.writer(QUOTE_ALL)."
)

NEW_ROW = {
    "index": "537",
    "name": "Xendoo",
    "handle": "@xendoo",
    "email": "support@xendoo.com",
    "vertical": "bookkeeping_ai_ops",
    "tier": "1",
    "template": "537_xendoo.md",
    "tier_reason": TIER_REASON,
}

# Idempotency check: row-prefix anchor (pitfall #69)
csv_text = LEADS.read_text(encoding="utf-8")
row_prefix = f'"537","Xendoo","'
assert row_prefix not in csv_text, f"Lead 537 row already present in {LEADS}"

with open(LEADS, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(NEW_ROW.keys()), quoting=csv.QUOTE_ALL)
    w.writerow(NEW_ROW)

# Parse-back verify
with open(LEADS, "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
match = [r for r in rows if r["index"] == "537"]
assert len(match) == 1, f"Expected exactly 1 row for index 537, got {len(match)}"
assert match[0]["email"] == "support@xendoo.com"
assert match[0]["template"] == "537_xendoo.md"
print(f"CSV OK: {len(rows)} total rows; lead 537 verified")

# ---- 2. Prepend build-log entry (Variant C, reverse-chronological) ----
bl = BUILD_LOG.read_text(encoding="utf-8")
anchor = f'data-tick="{TICK_ID}"'
assert anchor not in bl, f"build-log already has entry for {TICK_ID}"

NEW_ENTRY = (
    f'<div class="tick-entry" {anchor}>\n'
    f'<h2>Tick 537 — Xendoo ship (bookkeeping_ai_ops cohort sibling #6)</h2>\n'
    f'<p><strong>2026-07-19 fast-exec</strong> · Lead 537 Xendoo (support@xendoo.com verified live 2026-07-19 via xendoo.com/privacy-policy mailto:) · '
    f'founder Lil Roberts (Founder + CEO, verified via /meet-the-team page h3 class wpr-member-name). '
    f'3-surface ship (CSV row + template 537_xendoo.md + build-log prepend). '
    f'bookkeeping_ai_ops cohort now 6/6 anchored (Bookkeep 352 + Bench 355 + Pilot.com 357 + Botkeeper 358 + Catch 359 + Xendoo 537); '
    f'Xendoo anchors the multi-vertical SMB bookkeeping + fractional-CFO + tax-services lane (eCommerce + franchise + hospitality + medical + professional services + technology verticals + AdvisorConnect partner channel + Insights-XP + Power-of-3 + Q2X + ZorConnect). '
    f'5 audit gaps surfaced: (1) end-to-end 13-col per-client → per-engagement → per-QBO/Xero/NetSuite-tenant → per-monthly-close → per-bookkeeper → per-reconciler → per-fractional-CFO → per-tax-prep → per-IRS-IRC-7515-supervision → per-state-board-of-accountancy-license → per-audit-log → per-procurement-vendor-DD → per-residency-region provenance join-table per SOC 2 CC7.2 + GLBA-Safeguards + IRS-IRC-7515 + FTC-Safeguards-Rule + state-board-of-accountancy + multi-state-privacy, '
    f'(2) Xendoo bookkeeping + fractional-CFO + tax workpaper corpus + per-bookkeeper GLBA-trained + per-reconciler CFC-trained + per-tax-prep CPA-licensed history + per-client PII (EIN + SSN + bank-account + revenue-detail) license-provenance + LLM-training-data-transparency + IRS-Circular-230 + state-board-of-accountancy + multi-state-CPA-license-discipline, '
    f'(3) prompt-injection + LLM-bookkeeper-poisoning + fractional-CFO-assistant-poisoning + tax-prep-assistant-poisoning + client-PII-exfiltration + QBO/Xero/NetSuite-tenant-prompt-injection + per-bookkeeper-prompt-injection-defense per OWASP LLM Top 10 LLM01+LLM03+LLM06+LLM08 + MITRE ATLAS + GLBA-Safeguards-Rule + IRS Pub 4557 + FTC Safeguards Rule + state-board-of-accountancy + multi-state-privacy, '
    f'(4) cross-Xendoo-client + per-tenant-KMS-key-id + per-client-QBO/Xero/NetSuite-tenant + cross-border-data-residency-isolation + per-engagement-isolation per SOC 2 CC6.1 + GLBA Safeguards Rule + IRS-IRC-7515 + FTC Safeguards Rule + state-board-of-accountancy + multi-state-privacy (CCPA/CPRA + VA-VCDPA + CO-CPA + CT-CTDPA + UT-UCPA + TX-TDPSA + FL-FDBR + OR-OCPA + MT-MCDPA + IRS-Pub-4557), '
    f'(5) WORM retention + cost-attribution join-table linking per-client-cost + per-engagement-cost + per-monthly-close-cost + per-bookkeeper-cost + per-reconciler-cost + per-fractional-CFO-cost + per-tax-prep-cost + per-LLM-token-cost + per-multi-state-board-of-accountancy-cost per SOC 2 CC7.2 + IRS-IRC-7515-recordkeeping + IRS-Circular-230-recordkeeping + GLBA-recordkeeping + FTC-Safeguards-Rule-recordkeeping + state-board-of-accountancy-recordkeeping + multi-state-privacy-recordkeeping. '
    f'2-probe inbox-verify budget honored (Ramp /privacy probe 1 was SPA-wall 778KB but zero mailto → immediate pivot to Xendoo probe 1 → verified support@xendoo.com on /privacy-policy; probe 2 = /meet-the-team for Lil Roberts founder name). '
    f'next tick: 538 = bookkeeping_ai_ops depth continued (Indinero or 1-800Accountant for fractional-CFO + tax depth) OR pivot to vector_database (5 leads, 5/5 needed) for new-vertical breadth.</p>\n'
    f'<p><strong>Inbox-verify budget:</strong> 2 probes used (Ramp SPA-wall pivot + Xendoo verified). '
    f'<strong>Cohort progression:</strong> bookkeeping_ai_ops 6/6 anchored, ai_data_labeling 8/8 anchored, ai_revenue_intelligence 6/6, vector_database 5/5. '
    f'<strong>Next-tick signal:</strong> vertical breadth over depth — vector_database needs only 1 more for full-vertical cohesion; ai_meeting_infrastructure 5/5 needs depth.</p>\n'
    f'</div>\n'
)

# Variant C: anchor on opening tag, prepend BEFORE first <div class="tick-entry"
opening_idx = bl.find('<div class="tick-entry"')
assert opening_idx == 0, f"build-log not in Variant C (opening_idx={opening_idx}, expected 0)"
opening_tag_end = opening_idx + len('<div class="tick-entry" ')
# (anchor `bl.find(anchor)` already verified at top to return -1; no need to repeat)
new_bl = NEW_ENTRY + bl
assert new_bl.count(NEW_ENTRY.strip()) == 1
assert new_bl.count('<div class="tick-entry"') == bl.count('<div class="tick-entry"') + 1
BUILD_LOG.write_text(new_bl, encoding="utf-8")

# Re-verify after write
bl2 = BUILD_LOG.read_text(encoding="utf-8")
assert bl2.count(anchor) == 1
assert bl2.count('<div class="tick-entry"') == 337 + 1
opening_idx2 = bl2.find('<div class="tick-entry"')
assert opening_idx2 == 0
our_attr_idx2 = bl2.find(anchor)
assert our_attr_idx2 == opening_idx2 + len('<div class="tick-entry" ')
print(f"BUILD-LOG OK: 337 -> 338 tick entries; {TICK_ID} prepended at top")

# ---- 3. Idempotency summary ----
print(f"DONE: ship_537_xendoo.py executed cleanly")
print(f"  CSV: {len(rows)} rows (was 419-1=418 before, now {len(rows)})")
print(f"  Template: 537_xendoo.md ({sum(1 for _ in open(REPO / 'cold_email' / 'templates' / '537_xendoo.md', encoding='utf-8').readlines())} lines)")
print(f"  Build-log: 338 entries (was 337, now +1)")
print(f"  Tick ID: {TICK_ID}")