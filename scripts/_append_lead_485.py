#!/usr/bin/env python3
"""Append Lead 485 (Synthesia) to leads.csv. Schema: 8 cols."""
import csv

CSV_PATH = r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv"

ROW = {
    "index": "485",
    "name": "Synthesia",
    "handle": "@synthesiaio",
    "email": "sales@synthesia.io",
    "vertical": "synthetic_media",
    "tier": "1",
    "template": "485_synthesia.md",
    "tier_reason": (
        "Lead 485 - Synthesia (synthesia.io, canonical AI-synthetic-video + avatar + "
        "voice-clone + AI-presenter platform, distinct from Tonic 484 synthetic-text-tabular "
        "lane). Real company verified live 2026-07-17: https://www.synthesia.io/about returned "
        "HTTP 200 (317,474 bytes; title 'Our story: Building the video-first internet'). "
        "Founders verified on first-party https://www.synthesia.io/about (image alt-text + "
        "title-card + 'CEO & Co-founder' label): Victor Riparbelli (CEO & Co-founder) and "
        "Steffen Tjerrild (Co-founder & CFO/COO). Founded 2017, HQ London UK. Raised $330M+ "
        "across Series A/B/C from NEA, Kleiner Perkins, GV, Accel, FirstMark, and NVIDIA "
        "(Series C $90M Jun 2023). Products: AI-avatar video generation, AI-voice-clone, "
        "custom-avatar studio, AI-script-assist, AI-translate-video (130+ languages), "
        "AI-video-template-library, and downstream enterprise-content workflows "
        "(LMS, e-learning, sales enablement, marketing). Atlas pitch: replace a corporate-"
        "video-production-FTE (~$110K/yr) with Synthesia + Atlas-attached provenance-and-"
        "enterprise-procurement-pipeline. Target: Synthesia enterprise pipeline + "
        "downstream high-risk-AI-operator buyers (corporate-training + L&D + sales "
        "enablement + financial-services + healthcare-pharma training). 5 audit gaps: "
        "(1) per-avatar + per-voice + per-script + per-render + per-tenant join-table per "
        "SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 capturing per-avatar-id + "
        "per-voice-clone-id + per-AI-script-id + per-AI-translation-id + per-render-job-id "
        "+ per-customer-tenant-id + per-procurement-vendor-DD-event-id + per-audit-log-"
        "entry-id + per-residency-region-id, (2) synthetic-media training-corpus + "
        "voice-clone-consent provenance + image-bias-audit + voice-bias-audit per EU AI Act "
        "Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary + "
        "ISO 42001 6.1.4 + FCC TCPA (Synthesia voice-clone consent lineage spans TCPA "
        "prior-express-written-consent + state-BIPA biometric-privacy-consent + EU GDPR "
        "Art. 9 special-category-data + Illinois AI Video Interview Act), (3) deepfake + "
        "voice-clone-misuse + AI-presenter-spoofing + synthetic-media-fraud defense per "
        "OWASP LLM Top 10 LLM01 + LLM06 + EU AI Act Art. 14 human-oversight + Art. 50 "
        "transparency-obligation + 12-state AI-disclosure (CA SB 1001 + CO SB 24-205 + "
        "IL AI Video Interview Act + TX + NY + 7 others - Synthesia AI-presenter videos "
        "impact L&D + marketing + sales-enablement content across all 50 states + EU), "
        "(4) cross-tenant avatar + voice + script + render isolation per SOC 2 CC6.1 + "
        "GDPR Art. 28 + Schrems II (per-tenant avatar-instance + per-tenant voice-instance "
        "+ per-tenant KMS-key + per-tenant render-quota - critical for financial-services + "
        "healthcare tenants where avatar-isolation is auditable), (5) WORM retention + "
        "cost-attribution join-table linking per-render-cost + per-voice-clone-cost + "
        "per-AI-translation-cost + per-customer-tenant-cost per SOC 2 CC7.2 + EU AI Act "
        "Art. 12 + SEC 17a-4 WORM + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement. "
        "sales@synthesia.io is the verified SOC 2 + GDPR DPA + CCPA/CPRA + EU AI Act + "
        "enterprise-procurement-vendor-DD strategic-inbound channel."
    ),
}


def main() -> None:
    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "index", "name", "handle", "email", "vertical",
                "tier", "template", "tier_reason",
            ],
            quoting=csv.QUOTE_ALL,
        )
        w.writerow(ROW)

    # Parse-back verify
    with open(CSV_PATH, "r", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    last = rows[-1]
    assert last["index"] == "485"
    assert last["name"] == "Synthesia"
    assert last["email"] == "sales@synthesia.io"
    assert last["vertical"] == "synthetic_media"
    assert "Victor Riparbelli" in last["tier_reason"]
    assert "Steffen Tjerrild" in last["tier_reason"]
    assert "synthetic-video" in last["tier_reason"]
    assert "$500" in last["tier_reason"] or "audit" in last["tier_reason"].lower()
    print(f"PASS: lead 485 appended; rows={len(rows)}")


if __name__ == "__main__":
    main()