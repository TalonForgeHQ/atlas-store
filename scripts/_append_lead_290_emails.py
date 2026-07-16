"""Append Holistic AI (lead 290) to cold_email/leads_with_emails.csv in its existing style."""
import csv, io

LEADS = r"C:\Users\Potts\projects\atlas-store\cold_email\leads_with_emails.csv"

new_row = [
    "290",
    "Holistic AI",
    "@holisticai",
    "holisticai.com",
    "https://www.holisticai.com",
    "Adriano Koshiyama (Co-Founder + Co-CEO, ex-UCL AI/ML academic) + Emre Kazim (Co-Founder + Co-CEO, ex-UCL AI-Policy academic, co-founder of AI-Centrism)",
    "ai_governance_ml_platform",
    "1",
    "we@holisticai.com",
    "we@holisticai.com",
    "",
    "290_holisticai.md",
    "Canonical AI-governance + AI-risk-management + AI-compliance-automation + AI-Bill-of-Rights-evaluation + EU-AI-Act-readiness + NIST-AI-RMF-policy-management + ISO-42001-ISMS-control-mapping + agentic-AI-Governance + AI-Agent-Registry + AI-Vendor-portal + AI-Registry + model-card-automation + dataset-card-automation + use-case-risk-tiering-platform (Holistic AI Platform + Holistic AI Governance + Holistic AI Trust + Holistic AI Risk + Holistic AI Compliance + Holistic AI Audit + Holistic AI Advisory + Holistic AI Regulation Automation + Holistic AI Risk Center + Holistic AI Audit Artifacts + Holistic AI Vendor Compliance + Holistic AI Generative AI Guardrails + Holistic AI Agent Governor + Holistic AI Agent Registry + Holistic AI Vendor Portal + Holistic AI Regulatory Compliance + Holistic AI Bias Audit + Holistic AI EU-AI-Act-Readiness + Holistic AI ISO-42001-readiness + Holistic AI NIST-AI-RMF-readiness + Holistic AI Colorado-SB21-169-readiness + Holistic AI NYC-Local-Law-144-readiness). we@holisticai.com verified live 2026-07-16 via curl scrape https://www.holisticai.com/privacy-policy HTTP 200 exposing mailto:we@holisticai.com as the canonical GDPR Art. 28 DPA + SOC 2 Type II + EU AI Act Annex IV + ISO 42001 + ISO 27001 + NIST AI RMF strategic-inbound channel. Founded 2020 in London UK. HQ London UK + New York NY. 100+ Fortune-500 + Global-2000 enterprise customers. SOC 2 Type II + ISO 27001 + ISO 42001 + GDPR DPA + EU AI Act Annex IV + NIST AI RMF + Colorado SB21-169 + NYC Local Law 144. Tier-1 ai_governance_ml_platform 4th-sibling; closes the 4-vendor cohort (DataRobot 287 + Credo AI 288 + SUPERWISE 289 + Holistic AI 290)."
]

def csv_quote(s):
    return '"' + s.replace('"', '""') + '"'

line = ",".join(csv_quote(c) for c in new_row) + "\n"

parsed = list(csv.reader(io.StringIO(line)))
assert parsed[0][0] == "290"
assert parsed[0][1] == "Holistic AI"
assert parsed[0][8] == "we@holisticai.com"

before = sum(1 for _ in open(LEADS, encoding="utf-8")) - 1
with open(LEADS, "a", encoding="utf-8", newline="") as f:
    f.write(line)
after = sum(1 for _ in open(LEADS, encoding="utf-8")) - 1

print(f"OK. leads_with_emails.csv rows: {before} -> {after}. Last index={parsed[0][0]} name={parsed[0][1]} email={parsed[0][8]}")
