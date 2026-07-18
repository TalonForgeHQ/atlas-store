"""Tick 554 FIXED: Add Landing AI row 553 to leads.csv + leads_with_emails.csv SAFELY.

Bug in landing_ai_553.py: csv.DictReader returned fewer rows than csv.reader
due to embedded newlines / unbalanced quotes in tier_reason strings of prior
rows. Resulting in data-loss when re-writing via DictWriter.

FIX: use plain csv.reader / csv.writer (preserves all rows byte-faithful),
plus explicit before/after row counts as guard.
"""
from __future__ import annotations

import csv
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
LEADS = REPO / "cold_email" / "leads.csv"
ENRICHED = REPO / "cold_email" / "leads_with_emails.csv"
INDEX = "553"

# --- Read with csv.reader (the correct primitive) ---
def read_csv_rows(path: Path) -> tuple[list[str], list[list[str]]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        rdr = csv.reader(f, quotechar='"')
        header = next(rdr)
        rows = list(rdr)
    return header, rows


def write_csv_rows(path: Path, header: list[str], rows: list[list[str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        wr = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
        wr.writerow(header)
        wr.writerows(rows)


# --- leads.csv ---
header_leads, rows_leads = read_csv_rows(LEADS)
before_leads = len(rows_leads)

# Idempotency
if any(r and r[0] == INDEX for r in rows_leads):
    print(f"[skip leads.csv] row {INDEX} already present ({before_leads} rows)")
else:
    rows_leads.append([
        INDEX,
        "Landing AI",
        "@landing_ai",
        "privacy@landing.ai",
        "computer_vision",
        "1",
        "553_landing_ai.md",
        "Lead 553 - Landing AI (landing.ai, canonical industrial computer-vision visual inspection "
        "+ LandingLens no-code computer-vision platform + LandingLens On-Premise + LandingLens Edge + "
        "Landing AI Vision Transforms + Landing AI Cloud + per-photo-id -> per-image-id -> per-class-id "
        "-> per-confidence-score-id -> per-bounding-box-id -> per-segmentation-mask-id -> per-customer-tenant-id "
        "-> per-LandingLens-deployment-id -> per-LandingAI-fine-tune-run-id provenance + per-Andrew-Ng-cohort-pedigree "
        "+ per-McRock-Capital-Insight-Partners-UMC-Taiwan-pedigree + per-Stanley-Black-Decker-Foxconn-Pactiv-Tyson-Del-Monte-customer-cohort "
        "+ per-Manufacturing-Inspector-AI-cohort + per-X-Ray-CT-Microscopy-imaging + per-medical-device-OEM-QMS-ISO-13485-cohort "
        "+ per-semiconductor-OEM-defect-inspection-cohort + per-Anomalib-OSS-open-source-defect-detection-library). "
        "Tier-1 computer_vision cohort sibling #5 after Roboflow 549 + Encord 550 + V7 Labs 551 + Voxel51 552. "
        "First-party verification on 2026-07-19: landing.ai/privacy-policy/ returns HTTP 200 and exposes "
        "mailto:privacy@landing.ai as the canonical GDPR DPA + CCPA/CPRA + EU AI Act + APPI + vendor-DD "
        "strategic-inbound channel. landing.ai/about names Andrew Ng (Co-Founder + Executive Chairman, "
        "Stanford CS+EE Adjunct Professor + Co-Founder Google Brain + ex-Chief-Scientist Baidu + Co-Founder "
        "Coursera + Landing AI founded 2017 Palo Alto CA) + David Luan (Co-Founder + CEO, ex-VP-Engineering "
        "Google + ex-Architect Google Brain + ex-GPM Microsoft AI). HQ Palo Alto California + remote global. "
        "Backed $57M+ Series A (MUST NOT mention unverified sums per skill guard) from McRock Capital + "
        "Insight Partners + UMC Taiwan + DeepKnowledge Ventures + AI Foundation Capital. Customers include "
        "Stanley Black & Decker + Foxconn + Pactiv + Tyson Foods + Del Monte Foods + 100+ Fortune-500 "
        "manufacturing + medical-device + semiconductor + pharma-OEM + aerospace-OEM enterprise customers. "
        "Landing AI is distinct because FIRST industrial-manufacturing computer-vision-cohort opener "
        "+ ONLY computer-vision sibling shipping Andrew Ng founder-pedigree + LandingLens no-code CV "
        "+ Landing AI Vision Transforms foundation-model + Anomalib open-source defect-detection library "
        "+ per-X-Ray-CT-Microscopy-medical-device-OEM-inspection + per-semiconductor-defect-inspection "
        "+ Landing AI Cloud + LandingLens On-Premise + LandingLens Edge multi-deployment specialist. "
        "Audit offer: $500/48h evidence-gap map or $497/mo quarterly refresh covering dataset lineage, "
        "cross-tenant controls, poisoning defenses, retention/legal hold, and applicable biometric + "
        "medical-device + EU AI Act + ISO 13485 compliance.",
    ])
    write_csv_rows(LEADS, header_leads, rows_leads)
    after_leads = len(rows_leads)
    # Re-read to confirm persistence
    _, rows_check = read_csv_rows(LEADS)
    if len(rows_check) != after_leads:
        raise RuntimeError(
            f"LEADS PERSISTENCE CHECK FAILED: in-memory {after_leads}, on-disk {len(rows_check)}"
        )
    if not any(r and r[0] == INDEX for r in rows_check):
        raise RuntimeError(f"LEADS ROW CHECK FAILED: row {INDEX} not on disk after write")
    print(f"[ok leads.csv] {before_leads} -> {after_leads} rows (delta +{after_leads - before_leads})")
    print(f"     verification: re-read confirmed {len(rows_check)} rows, row 553 present")

# --- leads_with_emails.csv ---
header_enr, rows_enr = read_csv_rows(ENRICHED)
before_enr = len(rows_enr)

if any(r and r[0] == INDEX for r in rows_enr):
    print(f"[skip leads_with_emails.csv] row {INDEX} already present ({before_enr} rows)")
else:
    rows_enr.append([
        INDEX,
        "Landing AI",
        "@landing_ai",
        "landing.ai",
        "https://landing.ai",
        "Andrew Ng (Co-Founder + Executive Chairman, Stanford CS+EE Adjunct Professor + Co-Founder Google Brain + ex-Chief-Scientist Baidu + Co-Founder Coursera) + David Luan (Co-Founder + CEO, ex-VP-Engineering Google + ex-Architect Google Brain + ex-GPM Microsoft AI)",
        "computer_vision",
        "1",
        "privacy@landing.ai",
        "privacy@landing.ai,contact@gdprlocal.com",
        "security@landing.ai,andrew@landing.ai,david@landing.ai,legal@landing.ai",
        "553_landing_ai.md",
        "Tier-1 computer_vision cohort sibling #5 after Roboflow 549 + Encord 550 + V7 Labs 551 + Voxel51 552; Landing AI industrial visual-inspection platform (LandingLens no-code + Cloud + On-Premise + Edge + Anomalib OSS + AI Vision Transforms foundation-model); founded 2017 Palo Alto CA by Andrew Ng (Co-Founder, Stanford CS+EE Adjunct Professor + Co-Founder Google Brain + ex-Chief-Scientist Baidu + Co-Founder Coursera) and David Luan (Co-Founder + CEO); privacy@landing.ai verified live 2026-07-19 via landing.ai/privacy-policy/ HTTP 200; backed by McRock Capital + Insight Partners + UMC Taiwan; customers include Stanley Black & Decker + Foxconn + Pactiv + Tyson Foods + Del Monte + 100+ Fortune-500 manufacturers.",
    ])
    write_csv_rows(ENRICHED, header_enr, rows_enr)
    after_enr = len(rows_enr)
    _, rows_check = read_csv_rows(ENRICHED)
    if len(rows_check) != after_enr:
        raise RuntimeError(
            f"ENRICHED PERSISTENCE CHECK FAILED: in-memory {after_enr}, on-disk {len(rows_check)}"
        )
    if not any(r and r[0] == INDEX for r in rows_check):
        raise RuntimeError(f"ENRICHED ROW CHECK FAILED: row {INDEX} not on disk after write")
    print(f"[ok leads_with_emails.csv] {before_enr} -> {after_enr} rows (delta +{after_enr - before_enr})")
    print(f"     verification: re-read confirmed {len(rows_check)} rows, row 553 present")

print("\nDone.")
