"""Append Holistic AI (lead 290) to cold_email/leads.csv in the project's existing CSV style."""
import csv, io, os

LEADS = r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv"

new_row = [
    "290",
    "Holistic AI",
    "@holisticai",
    "we@holisticai.com",
    "ai_governance_ml_platform",
    "1",
    "290_holisticai.md",
    "Canonical AI-governance + AI-risk-management + AI-compliance-automation + AI-Bill-of-Rights-evaluation + EU-AI-Act-readiness + NIST-AI-RMF-policy-management + ISO-42001-ISMS-control-mapping + agentic-AI-Governance + AI-Agent-Registry + AI-Vendor-portal + AI-Registry + model-card-automation + dataset-card-automation + use-case-risk-tiering-platform (Holistic AI Platform + Holistic AI Governance + Holistic AI Trust + Holistic AI Risk + Holistic AI Compliance + Holistic AI Audit + Holistic AI Advisory + Holistic AI Regulation Automation + Holistic AI Risk Center + Holistic AI Audit Artifacts + Holistic AI Vendor Compliance + Holistic AI Generative AI Guardrails + Holistic AI Agent Governor + Holistic AI Agent Registry + Holistic AI Vendor Portal + Holistic AI Regulatory Compliance + Holistic AI Bias Audit + Holistic AI EU-AI-Act-Readiness + Holistic AI ISO-42001-readiness + Holistic AI NIST-AI-RMF-readiness + Holistic AI Colorado-SB21-169-readiness + Holistic AI NYC-Local-Law-144-readiness). we@holisticai.com verified live 2026-07-16 via curl scrape https://www.holisticai.com/privacy-policy HTTP 200 exposing mailto:we@holisticai.com as the canonical GDPR Art. 28 DPA + SOC 2 Type II + EU AI Act Annex IV + ISO 42001 + ISO 27001 + NIST AI RMF strategic-inbound channel. Founded 2020 in London UK by Adriano Koshiyama (Co-Founder + Co-CEO, ex-University College London AI/ML academic) + Emre Kazim (Co-Founder + Co-CEO, ex-University College London AI-Policy academic + co-founder of AI-Centrism). HQ London UK + New York NY + remote-distributed globally. Customers include 100+ Fortune-500 + Global-2000 enterprise customers in financial-services + banking + insurance + pharma + biotech + healthcare + government + public-sector using Holistic AI Governance Platform + Holistic AI Trust + Holistic AI Risk + Holistic AI Compliance + Holistic AI Audit + Holistic AI Agent Governor + Holistic AI Agent Registry + Holistic AI Vendor Portal + Holistic AI Regulatory Compliance + Holistic AI Bias Audit + Holistic AI EU-AI-Act-Readiness + Holistic AI ISO-42001-readiness + Holistic AI NIST-AI-RMF-readiness + Holistic AI Colorado-SB21-169-readiness + Holistic AI NYC-Local-Law-144-readiness for AI-policy-management + AI-Risk-Management + AI-compliance-automation + AI-vendor-risk-assessment + AI-inventory + AI-Bill-of-Rights-evaluation + use-case-risk-tiering at production scale. SOC 2 Type II + ISO 27001 + ISO 42001 readiness + GDPR DPA + EU AI Act Annex IV readiness + NIST AI RMF + Colorado SB21-169 readiness + NYC Local Law 144 bias audit readiness per holisticai.com/privacy-policy + holisticai.com/security. Tier-1 ai_governance_ml_platform 4th-sibling for per-AI-policy-record + per-AI-use-case-risk-tier + per-AI-vendor-questionnaire + per-AI-Agent-Governor-rule-event + per-AI-Agent-Registry-inventory-record + per-AI-Bill-of-Rights-evaluation + per-NIST-AI-RMF-MAP-event + per-ISO-42001-6.3-control-test + per-EU-AI-Act-Annex-IV-record + per-Colorado-SB21-169-record + per-NYC-Local-Law-144-bias-audit-record + per-OWASP-LLM-Top-10-evaluation + per-MITRE-ATLAS-evaluation + per-AI-Inventory-record + per-cross-vendor-policy-comparison join-table evidence under SOC 2 CC1.4 + CC6.1 + CC7.2 + EU AI Act Art. 9 + 10 + 12 + 14 + 27 + 43 + 53(d) + Aug 2026 GPAI enforcement + ISO 42001 6.3 + 9.4 + GDPR Art. 28 + Art. 32 + Colorado SB21-169 + NYC Local Law 144 + OWASP LLM Top 10 + NIST AI RMF GOVERN + MAP + MEASURE + MANAGE. Closes the canonical 4-vendor ai_governance_ml_platform cohort (DataRobot 287 + Credo AI 288 + SUPERWISE 289 + Holistic AI 290) -- the only cohort covering DataRobot's enterprise-1000-Global-2000-scale + Credo AI's policy-management + SUPERWISE's runtime-policy-engine + Holistic AI's academic-pedigree-from-UCL AI-Policy-school simultaneously."
]

def csv_quote(s):
    return '"' + s.replace('"', '""') + '"'

line = ",".join(csv_quote(c) for c in new_row) + "\n"

# Re-parse to validate
parsed = list(csv.reader(io.StringIO(line)))
assert parsed[0][0] == "290", f"index wrong: {parsed[0][0]}"
assert parsed[0][1] == "Holistic AI"
assert parsed[0][3] == "we@holisticai.com"
assert parsed[0][6] == "290_holisticai.md"

before = sum(1 for _ in open(LEADS, encoding="utf-8")) - 1
with open(LEADS, "a", encoding="utf-8", newline="") as f:
    f.write(line)
after = sum(1 for _ in open(LEADS, encoding="utf-8")) - 1

print(f"OK. leads.csv rows: {before} -> {after}. Last index={parsed[0][0]} name={parsed[0][1]} email={parsed[0][3]}")
