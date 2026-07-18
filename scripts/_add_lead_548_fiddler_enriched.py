"""Append Lead 548 Fiddler AI to leads_with_emails.csv (13-col enriched)"""
import csv

NEW = [
    "548",
    "Fiddler AI",
    "@fiddlerlabs",
    "fiddler.ai",
    "https://fiddler.ai",
    "Krishna Gade (Founder & CEO; ex-Facebook + Twitter + Pinterest + Microsoft) + Amit Paka (Founder & COO; ex-Samsung + PayPal + Microsoft + UC Berkeley)",
    "ai_observability",
    "1",
    "support@fiddler.ai",
    "support@fiddler.ai",
    "privacy@fiddler.ai;security@fiddler.ai;trust@fiddler.ai;krishna@fiddler.ai;amit@fiddler.ai",
    "548_fiddler.md",
    "Fiddler AI Control Plane for AI Agents vendor-DD 13-col provenance join-table: ai_observability cohort sibling #2 (after Arize 547). Verified live 2026-07-19 fiddler.ai/privacy-policy/ HTTP 200 + fiddler.ai Organization JSON-LD schema (550 California Ave Palo Alto CA 94306 US HQ). Krishna Gade Founder & CEO + Amit Paka Founder & COO. SOC 2 Type II + ISO 27001 + ISO 27701 + ISO 42001 + GDPR DPA + CCPA/CPRA + Schrems II SCC + EU AI Act Aug 2 2026 GPAI Art. 53(d) + HIPAA + FedRAMP-Ready + 12-state AI-disclosure + Defense Innovation Unit Success Memo + Forrester Agentic Control Plane + Gartner AI Evaluation and Observability + CB Insights AI Agent Security leader + IDC ProductScape Worldwide Generative AI Governance Platforms 2025.",
]

with open('cold_email/leads_with_emails.csv', 'r', newline='', encoding='utf-8') as f:
    rows = list(csv.reader(f))

rows.append(NEW)

with open('cold_email/leads_with_emails.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    for r in rows:
        w.writerow(r)

print(f"OK — leads_with_emails.csv now has {len(rows)-1} data rows (added Lead 548 Fiddler AI)")