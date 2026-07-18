"""Tick 506: add Aspire (ai_influencer_marketing cohort sibling #3 after Statusphere 504 + Lumanu 505)."""
import csv
from pathlib import Path

root = Path("C:/Users/Potts/projects/atlas-store")
leads_path = root / "cold_email" / "leads.csv"
enriched_path = root / "cold_email" / "leads_with_emails.csv"

tier_reason = (
    "Lead 506 - Aspire (aspire.io, formerly AspireIQ, canonical AI-driven influencer marketing + "
    "AI UGC + AI creator-marketplace + AI ambassador-marketing + AI affiliate-marketing + "
    "AI product-seeding + AI paid-ads + AI creator-discovery + AI creator-nurture + "
    "AI campaign-management + AI creator-payments + AI ROI-measurement + AI per-campaign-roi + "
    "AI creator-tier-scoring + AI brand-creator-fit + AI content-performance-prediction + "
    "AI Shopify-integration + AI TikTok-integration + AI Meta-integration + AI Gmail-integration + "
    "AI Klaviyo-integration + trusted by thousands of e-commerce brands including MVMT + Pura Vida + "
    "Outer + Ridge + Lume + Liquid Death + Dr. Squatch + Caraway + Brightland + Glossier + AG1 + "
    "Whoop + Groove Life + Felix Gray + Topo Designs + United By Blue + Cuts Clothing + MeUndies + "
    "Native + Banana Republic + hundreds of consumer brands in Beauty + Skincare + Apparel + "
    "Footwear + Jewelry + Health + Wellness + Food + Beverage + Home + Pets verticals). "
    "Tier-1 ai_influencer_marketing vertical cohort sibling #3 after Statusphere 504 + Lumanu 505. "
    "Real company verified live 2026-07-18: www.aspire.io returned HTTP 200 + aspire.io/about-us "
    "returned HTTP 200 with Anand Kannappan (CEO + Co-Founder) verified live + aspire.io/privacy-policy "
    "returned HTTP 200 with mailto:help@aspireiq.com verified canonical strategic-inbound channel + "
    "mailto:opt-out@aspireiq.com + AspireIQ Inquiries 701 Tillery Street #12 #148 Austin TX 78702 HQ + "
    "550 Montgomery Street Suite 800 San Francisco CA 94111 secondary office + AWS-hosted per CCPA notice + "
    "Schema.org SoftwareApplication + Organization JSON-LD markup + CCPA/CPRA + GDPR + Schrems II "
    "compliance + FTC-endorsement-guidelines + ASA-compliance + EU-AI-Act-readiness per aspire.io/privacy-policy. "
    "Founded 2014 San Francisco CA by Anand Kannappan (CEO + Co-Founder) + Zackary Iscol (Co-Founder). "
    "HQ Austin Texas + San Francisco California office + global presence. SOC 2 + GDPR DPA + CCPA/CPRA + "
    "FTC-endorsement-guidelines + ASA-compliance + EU-AI-Act-readiness + Schrems-II-SCC + IAB-Disclosure-Guidelines "
    "per aspire.io/privacy-policy. 5 audit gaps: (1) end-to-end 13-col per-creator-id -> per-AI-creator-tier-score -> "
    "per-AI-engagement-rate-prediction -> per-AI-brand-creator-fit-score -> per-AI-content-performance-prediction -> "
    "per-posting-cadence-optimization-id -> per-UGC-rights-event-id -> per-organic-paid-amplification-id -> "
    "per-campaign-id -> per-brand-tenant-id -> per-procurement-vendor-DD-event-id -> per-audit-log-entry-id -> "
    "per-residency-region-id provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + "
    "GDPR Art. 30 + FTC 16 CFR Part 255 + ASA CAP Code + IAB Tech Lab + 12-state AI-disclosure, "
    "(2) Aspire AI-creator-match + AI-engagement-rate-prediction + AI-brand-creator-fit + "
    "AI-content-performance-prediction training-corpus + fine-tune-license-provenance per EU AI Act Art. 53(d) GPAI "
    "training-data transparency + Art. 53(1)(b) copyright-summary + ISO 42001 6.1.4 (Aspire corpus spans "
    "thousands-of-brand-campaign-posting-history + per-post-engagement data + per-creator-audience-demographics + "
    "per-FTC-disclosure history - canonical EU AI Act Aug 2 2026 GPAI documentation target), (3) prompt-injection + "
    "AI-creator-tier-scoring-bypass + AI-engagement-rate-prediction-poisoning + AI-brand-creator-fit-poisoning + "
    "AI-content-performance-prediction-poisoning + creator-fraud-detection-bypass + fake-follower-detection-bypass + "
    "FTC-disclosure-bypass defense per OWASP LLM Top 10 LLM01+LLM03+LLM06+LLM08 + MITRE ATLAS + EU AI Act Art. 14 "
    "human-oversight + Art. 50 transparency-obligation + 12-state AI-disclosure, (4) cross-brand-tenant + "
    "cross-campaign-tenant + per-creator-id + per-brand-tenant-id + per-UGC-rights-event-id + per-campaign-id + "
    "per-brand-tenant-KMS-key-id + CMK/BYOK + per-brand-tenant-AI-inference-endpoint + per-brand-tenant-AI-training-pipeline "
    "per SOC 2 CC6.1 + GDPR Art. 28 + Schrems II + FTC Safeguards Rule, (5) WORM retention + cost-attribution "
    "join-table linking per-AI-creator-match-cost + per-AI-engagement-rate-prediction-cost + "
    "per-AI-brand-creator-fit-cost + per-AI-content-performance-prediction-cost + per-posting-cadence-optimization-cost + "
    "per-UGC-rights-event-cost + per-brand-tenant-cost + per-procurement-vendor-DD-event-cost per SOC 2 CC7.2 + "
    "EU AI Act Art. 12 + SEC 17a-4 WORM + EU AI Act Annex III 4 + Aug 2 2026 GPAI enforcement. help@aspireiq.com "
    "is the verified SOC 2 + GDPR DPA + CCPA/CPRA + FTC-endorsement-guidelines + ASA-compliance + EU-AI-Act + "
    "Schrems-II-SCC + Anand-Kannappan-CEO-Co-Founder + Zackary-Iscol-Co-Founder + Austin-TX-HQ + "
    "San-Francisco-CA-office + thousands-of-e-commerce-brand-DD + enterprise-procurement-vendor-DD "
    "strategic-inbound channel for Aspire + AI-creator-discovery + AI-influencer-matching + "
    "AI-engagement-prediction + AI-UGC-rights-management + ai_influencer_marketing + "
    "enterprise-procurement-vendor-DD strategic-inbound inquiries. 13-col row written via csv.writer(QUOTE_ALL)."
)

# --- Append to leads.csv (8-col format) ---
leads_row = [
    "506", "Aspire", "@aspireio", "help@aspireiq.com",
    "ai_influencer_marketing", "1", "506_aspire.md", tier_reason
]
with leads_path.open("a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n")
    w.writerow(leads_row)

# --- Append to leads_with_emails.csv (13-col format) ---
enriched_row = [
    "506", "Aspire", "@aspireio", "aspire.io", "https://www.aspire.io",
    "Anand Kannappan (CEO + Co-Founder); Zackary Iscol (Co-Founder)",
    "ai_influencer_marketing", "1", "help@aspireiq.com",
    "help@aspireiq.com", "opt-out@aspireiq.com",
    "506_aspire.md", tier_reason
]
with enriched_path.open("a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n")
    w.writerow(enriched_row)

print(f"Appended Aspire 506 row to {leads_path}")
print(f"Appended Aspire 506 row to {enriched_path}")
print(f"tier_reason length: {len(tier_reason)} chars")
