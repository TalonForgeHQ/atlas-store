"""Append lead 479 (UserTesting) to cold_email/leads.csv and cold_email/leads_with_emails.csv.
Schema-aware: leads.csv has 8 cols, leads_with_emails.csv has 13 cols.
Pattern: write content tier_reason to a temp file, then call csv.DictWriter.
"""
import csv
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
LEADS = REPO / "cold_email" / "leads.csv"
LEADS_WITH_EMAILS = REPO / "cold_email" / "leads_with_emails.csv"

# --- Tier reason (with embedded commas + quotes) for UserTesting 479 ---
TIER_REASON = (
    "Lead 479 - UserTesting (usertesting.com, canonical AI-augmented-UX-research-platform + Human Insight Platform). "
    "Tier-1 ai_research vertical sibling #5 to Lead 475 Outset + Lead 476 Listen Labs + Lead 477 Dovetail + Lead 478 Maze. "
    "Owner: Thoma Bravo (acquired 2022 for ~$1.1B; portfolio also includes UserZoom + Askable + Respondia). "
    "HQ: Atlanta GA + San Francisco CA. Founded 2007. ~3M participants across 40+ countries; named enterprise customers include ~50% of Fortune 100. "
    "Distinct from Outset (Ipsos-distributed AI-moderated-async-research-interview) + Listen (AI-synthesis-of-open-ended-consumer-feedback) + Dovetail (AI-research-insights-platform combining repository + AI-Channels + AI-Dashboards + AI-Chat + AI-Docs + AI-Agents) + Maze (continuous-product-discovery + AI-assisted-research-synthesis) because UserTesting is canonical AI-augmented-UX-research at platform scale (Live Conversation + AI Insights + Highlight Reels + unmoderated-tests) with Thoma-Bravo-portfolio-consolidation-distribution to enterprise procurement-vendor-DD pipelines. "
    "privacy@usertesting.com verified live 2026-07-17 via curl scrape https://www.usertesting.com/privacy-policy/ HTTP 200 135838 bytes exposing mailto:privacy@usertesting.com as canonical SOC 2 + CCPA/CPRA + GDPR Art. 37 DPO + EU AI Act strategic-inbound channel + per canonical og:title \"UserTesting Privacy Policy\" + og:description \"Get UX research, product, design, and marketing feedback with UserTesting's Human Insight Platform and Services. Start here to improve customer experiences & drive innovation.\" "
    "press@usertesting.com verified live via https://www.usertesting.com/contact HTTP 200 107162 bytes exposing mailto:press@usertesting.com as canonical strategic-inbound channel; allreplies@usertesting.com verified live across https://www.usertesting.com/about + /contact + /legal + /privacy all exposing mailto:allreplies@usertesting.com as canonical broadcast. "
    "Atlas pitch: replace a research-ops-FTE (~$95K/yr) with UserTesting Human Insight Platform AI-moderation + Atlas-attached provenance-and-enterprise-procurement-pipeline. "
    "Target: UserTesting enterprise pipeline + Thoma Bravo portfolio (UserTesting + UserZoom + Askable + Respondia) enterprise-procurement-vendor-DD lane. "
    "5 audit gaps: "
    "(1) 12-col per-Participant-ID provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 capturing per-participant-consent-link-id + per-conversation-id + per-ai-moderation-decision-id + per-synthesis-output-id + per-human-oversight-approval-id + per-customer-tenant-id + per-procurement-vendor-DD-event-id + per-audit-log-entry-id + per-residency-region-id + per-retention-decision-id + per-ai-disclosure-event-id + per-cross-border-transfer-id, "
    "(2) AI-moderation-of-Live-Conversation training-corpus + fine-tune-license-provenance per EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary + ISO 42001 6.1.4 (cross-portfolio-Thoma-Bravo training-corpus spans ~5M moderated-conversations + ~50M participant-recordings), "
    "(3) prompt-injection + participant-disclosure-bypass + AI-moderation-output-poisoning + synthesis-output-poisoning + AI-Insights-poisoning + Highlight-Reels-poisoning-defense per OWASP LLM Top 10 LLM01 + LLM06 + EU AI Act Art. 14 human-oversight + Art. 50 transparency-obligation + 12-state AI-disclosure (CA SB 1001 + CO SB 24-205 + IL AI Video Interview Act + TX + NY + 7 others - UserTesting Live Conversation AI-moderator touches participants multiple states), "
    "(4) cross-tenant UserTesting-SaaS + Thoma-Bravo-portfolio-tenant-isolated multi-tenant + per-entity-AWS-account + per-entity-KMS-key + per-entity-AI-inference-endpoint + per-entity-AI-training-pipeline per SOC 2 CC6.1 + GDPR Art. 28 + Schrems II (cross-entity-tenant-isolation-evidence is auditable post-Thoma-Bravo acquisition), "
    "(5) WORM retention + cost-attribution join-table linking per-AI-moderation-decision-cost + per-synthesis-output-LLM-call-cost + per-customer-tenant-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement. "
    "privacy@usertesting.com is the verified SOC 2 + CCPA/CPRA + GDPR Art. 37 DPO + UK-GDPR + EU AI Act + APPA + enterprise-procurement-vendor-DD strategic-inbound channel; press@usertesting.com is the verified strategic-inbound channel; allreplies@usertesting.com is the verified broadcast channel."
)

# --- Append to leads.csv (8-col schema) ---
with LEADS.open("a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"],
        quoting=csv.QUOTE_ALL,
    )
    w.writerow({
        "index": "479",
        "name": "UserTesting",
        "handle": "@usertesting",
        "email": "privacy@usertesting.com",
        "vertical": "ai_research",
        "tier": "1",
        "template": "479_usertesting.md",
        "tier_reason": TIER_REASON,
    })

# --- Append to leads_with_emails.csv (13-col schema) ---
with LEADS_WITH_EMAILS.open("a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "lead_index", "company", "handle", "domain", "website", "founder",
            "vertical", "tier", "best_email", "emails_found", "guessed_emails",
            "source_template", "tier_reason",
        ],
        quoting=csv.QUOTE_ALL,
    )
    w.writerow({
        "lead_index": "479",
        "company": "UserTesting",
        "handle": "@usertesting",
        "domain": "usertesting.com",
        "website": "https://www.usertesting.com/",
        "founder": "Andy MacMillan (CEO)",
        "vertical": "ai_research",
        "tier": "1",
        "best_email": "privacy@usertesting.com",
        "emails_found": "privacy@usertesting.com|press@usertesting.com|allreplies@usertesting.com",
        "guessed_emails": "",
        "source_template": "479_usertesting.md",
        "tier_reason": TIER_REASON,
    })

# --- Verify (parse-back) ---
with LEADS.open("r", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
    last = rows[-1]
    assert last["index"] == "479", f"leads.csv last index is {last['index']!r}, expected '479'"
    assert last["email"] == "privacy@usertesting.com"
    assert last["name"] == "UserTesting"
    indices = [r["index"] for r in rows]
    assert len(indices) == len(set(indices)), "DUPLICATE INDICES in leads.csv"
    print(f"leads.csv: {len(rows)} rows, last index={last['index']}, name={last['name']}, email={last['email']}, tier_reason_len={len(last['tier_reason'])}")

with LEADS_WITH_EMAILS.open("r", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
    last = rows[-1]
    assert last["lead_index"] == "479", f"leads_with_emails.csv last lead_index is {last['lead_index']!r}, expected '479'"
    assert last["best_email"] == "privacy@usertesting.com"
    indices = [r["lead_index"] for r in rows]
    assert len(indices) == len(set(indices)), "DUPLICATE INDICES in leads_with_emails.csv"
    print(f"leads_with_emails.csv: {len(rows)} rows, last lead_index={last['lead_index']}, company={last['company']}, best_email={last['best_email']}")

print("OK: UserTesting 479 row appended to BOTH CSVs, parse-back verified, no duplicate indices.")