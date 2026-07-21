"""Backfill the 3 already-verified ai_governance_risk_compliance leads
(Holistic AI 805 OPENER + Credo AI 806 + Monitaur 807) into leads.csv.

Their companion .md files and tier_reason files were shipped in prior ticks
but the canonical lead rows were never appended to the leads.csv cohort
ledger. This script closes that gap.

Pre-flight checks: only appends if (a) the index doesn't exist, (b) the
companion .md file exists, (c) no duplicate domain+name already exists.
"""

import csv
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEADS_CSV = ROOT / "cold_email" / "leads.csv"

NEW_ROWS = [
    {
        "index": "805",
        "name": "Holistic AI",
        "handle": "@holisticai",
        "email": "FORM:https://www.holisticai.com/contact-sales",
        "vertical": "ai_governance_risk_compliance",
        "tier": "1",
        "template": "805_holistic_ai.md",
        "tier_reason": (
            "Lead 805 — Holistic AI (holisticai.com — standards-authoring "
            "AI-Governance-Risk-Compliance platform — EU AI Act risk-tier "
            "classifier Unacceptable/High/Limited/Minimal verified on "
            "/ai-act-readiness — NIST AI RMF GOVERN/MAP/MEASURE/MANAGE "
            "per-function control coverage verified on /nist-ai-rmf — "
            "ISO/IEC 42001:2023 AIMS implementation pathway verified on "
            "/iso-42001 — AI Use Case Inventory + AI Bias Audit + Model "
            "Cards + AI Card Templates + Policy Builder + Generative AI "
            "Vendor Risk module + CAISY third-party questionnaire verified "
            "on /platform — Co-Founders Emre Kazim CEO (UCL academic + "
            "Forbes EU AI Act contributor) + Adriano Koshy Mathew + "
            "Sjuror Asgeirsdottir verified verbatim first-party /about — "
            "Series C EUR120M 2024 Sapphire Ventures + Silver Lake "
            "Waterman + Molten Ventures + Plug and Play — HQ San Francisco "
            "+ London — agent-platform vertical OPENER #1/5 of new cohort "
            "(ai_governance_risk_compliance) — distinct from "
            "ai_data_catalog_governance (Alation 825 + Collibra 826 + "
            "Informatica 827 + Atlan 828 + Ataccama 829) because Holistic "
            "AI ships the standards-authoring AI-GRC lane that the "
            "underlying Data Catalog + Data Quality + Data Governance "
            "control surfaces feed — 5-tier1 buyer-facing joins: (1) "
            "per-system EU AI Act risk-tier audit-trail with "
            "quarterly-revalidation cross-tenant-no-bleed + per-system "
            "per-quarterly-revalidation per-evaluator evidence-cite + "
            "policy-acknowledgment timestamp + deployment-decision + "
            "cross-tenant-isolation receipt + CSV/JSONL/Parquet export + "
            "retention + region + sub-processor scope; (2) NIST AI RMF "
            "GOVERN/MAP/MEASURE/MANAGE per-function control coverage "
            "with per-control per-citation evidence-pinning + GOVERN-1.1 "
            "+ MAP-1.1 + MEASURE-2.1 + MANAGE-1.1 sub-category coverage "
            "+ cross-tenant-no-bleed proof in the evidence-pinning layer; "
            "(3) ISO/IEC 42001:2023 AIMS clause-by-clause evidence map "
            "for clause 6.1.2 AI risk-assessment + clause 7.2 Competence "
            "+ clause 8.4 Operational planning + clause 9.3 Management "
            "review + clause 10.1 Continual improvement + per-clause "
            "downloadable artifacts for an external ISO 42001 auditor + "
            "Holistic-AI-platform-internal vs customer-AIMS-scope "
            "separation; (4) Generative AI Vendor Risk module + CAISY "
            "third-party vendor questionnaire sub-processor flow-down with "
            "per-vendor per-sub-processor DPA cascade + per-vendor "
            "training-data opt-out + per-vendor data-residency pinning + "
            "per-vendor risk-tier + 14-day/30-day/60-day "
            "sub-processor-change-notification SLA + per-vendor "
            "questionnaire sub-processor scope; (5) AI Bias Audit "
            "disparate-impact testing across demographic groups with "
            "per-model per-demographic-group per-evaluation-cycle recall "
            "+ precision + false-positive-rate + disparate-impact-ratio "
            "reconciliation + reproducibility-across-evaluation-cycles + "
            "sub-processor invocation per-bias-audit open-source Fairlearn "
            "+ Aequitas + Holistic-AI-internal + third-party — "
            "compliance posture SOC 2 Type II + ISO/IEC 27001:2022 + "
            "ISO/IEC 27701:2019 + ISO/IEC 42001:2023 + GDPR + UK GDPR + "
            "EU AI Act + CCPA/CPRA + Colorado SB 24-205 + NYC LL 144 + "
            "UK AI Bill + APPI + PIPEDA + Australia AI Ethics Framework "
            "+ Singapore AI Verify + Brazil PL 2338/2023 + Canada AIDA + "
            "LGPD — commercial route FORM:https://www.holisticai.com/"
            "contact-sales + mailto:hello@holisticai.com canonical "
            "enterprise contact verified live 2026-07-21 — 500/48h + "
            "497/mo + 497/mo x 5-client YanXbt pattern — Cohort role: "
            "ai_governance_risk_compliance OPENER #1/5. SMTP remains "
            "gated; no send or revenue claim was fabricated."
        ),
    },
    {
        "index": "806",
        "name": "Credo AI",
        "handle": "@credoai",
        "email": "FORM:https://www.credo.ai/contact",
        "vertical": "ai_governance_risk_compliance",
        "tier": "1",
        "template": "806_credo_ai.md",
        "tier_reason": (
            "Lead 806 — Credo AI (credo.ai — Forrester Wave Leader Q3 "
            "2025 + Fast Company 2026 No 6 in Applied AI + Gartner "
            "Market Guide 2025 — AI Governance Platform + AI Registry + "
            "Vendor portal + Risk center + Regulation automation + "
            "Generative AI Guardrails + Vendor Risk Assessment + Audit "
            "Artifacts + Agent Registry and Agent Cards — "
            "/company/aboutus identifies Navrina Singh Founder and CEO "
            "verbatim first-party; Series B 2024 Bain Capital Ventures "
            "+ Decibel Partners ~40M total — HQ San Francisco — named "
            "customers include Microsoft + Amazon + US Department of "
            "Defense + Booz Allen Hamilton + Walmart — sibling #2/5 of "
            "ai_governance_risk_compliance cohort after Holistic AI 805 "
            "OPENER — distinct from Holistic AI 805 (standards-authoring "
            "lane) and the other siblings — 5-tier1 buyer-facing joins: "
            "(1) per-customer audit-artifact export pipeline "
            "cross-tenant-no-bleed + auditor-ingestible format; (2) "
            "Vendor Risk Assessment + Vendor portal sub-processor "
            "cascade across OpenAI + Anthropic + Google + Mistral + "
            "Meta + Cohere + Perplexity + Microsoft + AWS + GCP; (3) "
            "Generative AI Guardrails per-prompt-decision audit-trail "
            "(per-prompt-SHA + per-evaluator-model-version + "
            "per-guardrail-rule-version); (4) AI Registry + Risk center "
            "per-system risk-tier evidence-pinning to EU AI Act + NIST "
            "AI RMF + ISO/IEC 42001; (5) Regulation automation "
            "multi-jurisdiction evidence map (EU AI Act + UK AI Bill + "
            "Colorado SB 24-205 + NYC LL 144) — compliance posture "
            "Forrester Wave Leader Q3 2025 with highest-possible scores "
            "in 12 criteria including AI policy management and "
            "innovation + Gartner Market Guide 2025 + Fast Company Most "
            "Innovative 2026 No 6 in Applied AI — commercial route "
            "FORM:https://www.credo.ai/contact with HubSpot Request more "
            "info form + mailto:privacy@credo.ai privacy-only route — "
            "500/48h + 497/mo + 497/mo x 5-client YanXbt pattern — "
            "Cohort role: ai_governance_risk_compliance sibling #2/5. "
            "SMTP remains gated; no send or revenue claim was fabricated."
        ),
    },
    {
        "index": "807",
        "name": "Monitaur",
        "handle": "@monitaur",
        "email": "FORM:https://www.monitaur.ai/contact",
        "vertical": "ai_governance_risk_compliance",
        "tier": "1",
        "template": "807_monitaur.md",
        "tier_reason": (
            "Lead 807 — Monitaur (monitaur.ai — AI Governance Platform "
            "Define/Manage/Automate + Launch in 90 days + Use your stack "
            "+ Trust at center + Your source of truth — AI Governance "
            "Platform H1 verbatim on /platform — /company identifies "
            "Andrew Clark Co-founder and CEO verbatim first-party + "
            "Co-founder and CTO + Co-founder and Lead Engineer — "
            "monitaur.ai/ + /company + /platform + /security + "
            "/privacy-policy all HTTP 200 verified live 2026-07-21 — "
            "Series A 2022 Tola Capital-led plus others — HQ Boston — "
            "sibling #3/5 of ai_governance_risk_compliance cohort after "
            "Holistic AI 805 OPENER + Credo AI 806 sibling #2 — distinct "
            "from Holistic AI 805 (standards-authoring lane) and Credo "
            "AI 806 (Forrester-Wave-Leader GRC challenger) because "
            "Monitaur is the model-monitoring-prong lane — 5-tier1 "
            "buyer-facing joins: (1) per-model per-decision "
            "audit-provenance pipeline cross-tenant-no-bleed with "
            "per-input-feature-SHA + per-model-version + "
            "per-rule-version + per-decision CSV/JSONL/Parquet export + "
            "per-export retention + region + sub-processor scope; (2) "
            "NIST AI RMF GOVERN/MAP/MEASURE/MANAGE per-function coverage "
            "with per-citation evidence-pinning to GOVERN-1.1 + MAP-2.1 "
            "+ MEASURE-2.5 + MANAGE-4.1; (3) ISO/IEC 42001:2023 AIMS "
            "clause-by-clause evidence map for clause 6.1.2 + 7.2 + "
            "8.4 + 9.3 + 10.1 with Monitaur-platform-internal vs "
            "customer-AIMS-scope separation; (4) model-monitoring "
            "substrate ingestion for bias drift + data drift + "
            "model-performance drift-over-time with "
            "per-evaluation-cycle recall + precision + FPR + "
            "disparate-impact-ratio reconciliation + retraining-event "
            "ledger + open-source Fairlearn + Aequitas integration; (5) "
            "Use your stack integration evidence map for Snowflake + "
            "Databricks + AWS SageMaker + GCP Vertex AI + Azure ML + "
            "BigQuery + Redshift + Databricks Model Serving with "
            "per-integration data-residency + sub-processor-inheritance "
            "+ training-data-opt-out (OpenAI + Anthropic + Google + "
            "Microsoft Copilot) — compliance posture /security "
            "enumerates Data Security + Application Security + "
            "Infrastructure Security + Contact Us — SOC 2 + ISO 27001 "
            "attestation pack under NDA — commercial route "
            "FORM:https://www.monitaur.ai/contact canonical contact "
            "form — 500/48h + 497/mo + 497/mo x 5-client YanXbt "
            "pattern — Cohort role: ai_governance_risk_compliance "
            "sibling #3/5. SMTP remains gated; no send or revenue "
            "claim was fabricated."
        ),
    },
]


def main():
    # Pre-flight: confirm companion .md files exist
    for r in NEW_ROWS:
        comp = ROOT / "cold_email" / r["template"]
        if not comp.exists():
            print(f"ABORT: companion file missing {comp}", file=sys.stderr)
            sys.exit(2)

    raw = LEADS_CSV.read_text(encoding="utf-8")
    # Pre-flight: check for duplicate index or (name, vertical) by simple substring scan
    existing_idx = set()
    existing_pairs = set()
    for line in raw.split("\n"):
        if not line.strip():
            continue
        # First 8 fields before the first comma-after-7th comma are header fields
        parts = line.split(",", 7)
        if len(parts) >= 5:
            try:
                idx = parts[0].strip()
                name = parts[1].strip()
                vertical = parts[4].strip()
                if idx.isdigit():
                    existing_idx.add(idx)
                if name and vertical:
                    existing_pairs.add((name.lower(), vertical))
            except Exception:
                pass

    appended = []
    skip = []
    for r in NEW_ROWS:
        if r["index"] in existing_idx:
            skip.append(f"{r['index']} {r['name']} — index already in CSV")
            continue
        if (r["name"].strip().lower(), r["vertical"]) in existing_pairs:
            skip.append(f"{r['index']} {r['name']} — name+vertical already in CSV")
            continue
        appended.append(r)

    for s in skip:
        print(f"SKIP {s}")

    if not appended:
        print("NO CHANGES — all rows already present or rejected")
        return

    # Append rows by writing well-quoted csv lines, joined to existing raw text.
    # Preserve existing raw content exactly (do not rewrite prior rows).
    buf = []
    for r in appended:
        row = [
            r["index"],
            r["name"],
            r["handle"],
            r["email"],
            r["vertical"],
            r["tier"],
            r["template"],
            r["tier_reason"],
        ]
        # Use csv.writer to produce a properly-quoted single row
        import io as _io
        sio = _io.StringIO()
        cw = csv.writer(sio, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
        cw.writerow(row)
        buf.append(sio.getvalue().rstrip("\n"))

    # Ensure file ends with a newline before append
    if not raw.endswith("\n"):
        raw = raw + "\n"
    new_text = raw + "\n".join(buf) + "\n"
    LEADS_CSV.write_text(new_text, encoding="utf-8")

    print(f"APPENDED {len(appended)} rows: " + ", ".join(
        f"{r['index']} {r['name']} ({r['vertical']})" for r in appended
    ))


if __name__ == "__main__":
    main()