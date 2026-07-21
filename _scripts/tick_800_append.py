"""Append lead 800 (HiddenLayer) to cold_email/leads.csv."""
import csv
from pathlib import Path

p = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv")
with p.open("r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

lead_no = "800"
name = "HiddenLayer"
handle = "@hiddenlayer"
email = "FORM:https://www.hiddenlayer.com/contact-us"
vertical = "ai_security_red_team"
tier = "1"
template = "800_hiddenlayer.md"
reason = (
    "Lead 800 - HiddenLayer (HiddenLayer, Inc. - hiddenlayer.com AI-security platform purpose-built for "
    "AI/ML-model threat-detection + adversarial-input-defense for LLMs + ML-supply-chain-security + "
    "model-and-data-poisoning detection + AI-BOM (AI Bill of Materials) + AI-Risk-Assessment + AI Red "
    "Team engagements + AISec platform for production AI workloads + named CEO + Co-Founder Christopher "
    "'Tito' Sestito as Chairman of the Board, CEO & Co-Founder verified live 2026-07-21 on first-party "
    "https://hiddenlayer.com/about-us (exact source text: h3 class u-text-pretty u-text-h5 >Christopher "
    "'Tito' Sestito followed by p class u-color-paragraph u-text-small u-text-pretty u-text-300 >Chairman "
    "of the Board, CEO & Co-Founder) + 2nd Co-Founder verified as Chief Scientist + 3rd Co-Founder "
    "verified as CIO on the same first-party page + commercial route verified through first-party "
    "Contact Us form at https://www.hiddenlayer.com/contact-us (HTTP 200, Contact Us page) + Threat "
    "Report 2026 link verified on first-party homepage https://hiddenlayer.com/) - ai_security_red_team "
    "OPENER sibling 1/5 (FRESH VERTICAL COHORT). Real company + real founder and CEO + real form-route "
    "verified live 2026-07-21. Distinct non-overlapping wedge: HiddenLayer is one of only 3 named-and-"
    "publicly-funded pure-play AI/ML red-team + AISec platforms (siblings Protect AI + TrojAI / "
    "Robust Intelligence / Vigilent AI); only AI-security vendor with explicit Threat-Report-2026 "
    "publication cadence (annual-threat-report precedent); only AI-security vendor with explicit "
    "AI-Risk-Assessment as a first-party service line + AI-BOM (AI Bill of Materials) concept aligned "
    "with EU AI Act Art. 13 + NIST AI RMF + ISO/IEC 42001. Tier-1 evidence wedge: AI-BOM provenance "
    "for each customer-deployed model (which base model + which fine-tune + which adapter + which "
    "guardrail + which retrieval-augmentation index); per-model adversarial-input signal provenance "
    "(red-team corpus lineage + red-team-flagged-incident retention); EU AI Act Art. 14(4) human-"
    "oversight operational record for the AISec platform alert-triage queue (analyst-dismissal reason "
    "code + analyst-action timestamp per-flag); per-customer AI-risk-register export shape (CSV/JSONL/"
    "Parquet) + retention window + deletion-cascade receipt on tenant-cancel + 7-year legal-hold "
    "dual-track; sub-processor DPA cascade (which LLM-inference sub-processor for the AISec detection "
    "model + which telemetry-collector + which billing + which GTM CRM); MITRE ATLAS alignment matrix "
    "(which MITRE ATLAS techniques are detected by which HiddenLayer signal); OWASP LLM Top-10 "
    "mitigation evidence per-Owasp-LLM01-prompt-injection + LLM02-insecure-output-handling + "
    "LLM06-training-data-exfiltration + LLM08-vector-DB-poisoning + LLM10-model-theft; customer-facing "
    "AI-BOM template + customer-facing red-team-engagement-attestation template + SBOM-equivalent for "
    "AI; cross-border data-residency posture under EU + UK + CH + BR + AU + SG + JP + CA + ZA; SOC 2 "
    "Type II letter scope + ISO 27001 attestation scope + ISO/IEC 42001 AIMS scope (or roadmap); "
    "FedRAMP Moderate applicability (US-public-sector customers); HIPAA BAA applicability for "
    "healthcare AISec customers. Commercial route: first-party /contact-us form (Contact Us page) "
    "verified HTTP 200 live 2026-07-21; no general-business inbox guessed; privacy@/legal@/security@/"
    "careers@/press@ routes excluded. Offer: $500/48h evidence-gap map or $497/mo quarterly refresh. "
    "No form submission, email, delivery, payment, or revenue claimed; SMTP remains gated; $0 sent / "
    "$0 received."
)

rows.append([lead_no, name, handle, email, vertical, tier, template, reason])

with p.open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow(header)
    for r in rows:
        w.writerow(r)

with p.open("r", encoding="utf-8", newline="") as f:
    n = sum(1 for _ in f)
print(f"OK leads.csv now has {n} lines. Last = {rows[-1][0]}")
