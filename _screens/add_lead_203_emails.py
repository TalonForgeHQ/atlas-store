"""Append lead 203 (LlamaIndex) to leads_with_emails.csv. Idempotent."""
import csv, sys

CSV = "cold_email/leads_with_emails.csv"
TIER_REASON = (
    "Canonical RAG-framework + LlamaParse agentic-OCR + LlamaCloud managed-RAG + "
    "LlamaIndex Workflows + LlamaIndex OSS Apache-2.0 + Jerry Liu CEO + Simon Suo CTO + "
    "4M+ downloads + 60K+ GitHub stars + Greylock + Norwest VP backers. "
    "privacy@runllama.ai verified live 2026-07-12 via curl scrape "
    "https://www.llamaindex.ai/legal/privacy-notice HTTP 200 214993 bytes exposing "
    "mailto:privacy@runllama.ai as the canonical GDPR DPA + SOC 2 + EU AI Act + "
    "vendor-DD strategic-inbound channel. Founded 2023 SF by Jerry Liu (CEO, ex-OpenAI "
    "+ ex-Stripe) + Simon Suo (CTO). HQ San Francisco California. Raised $27.5M Series A "
    "led by Greylock. Customers include Salesforce + RBC + Carlyle + Siemens + Vanguard "
    "+ Cigna + KPMG + OpenAI + Anthropic. SOC 2 Type II + GDPR DPA + HIPAA + EU AI Act "
    "readiness. ai_agents_infra vertical. 12th ai_agents_infra sibling."
)

with open(CSV, "r", encoding="utf-8", errors="replace", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

existing_ids = [r[0] for r in rows if r and r[0].isdigit()]
print("Existing lead_indexes in leads_with_emails:", len(existing_ids))

if "203" in existing_ids:
    print("Lead 203 already in leads_with_emails.csv, skipping.")
    sys.exit(0)

NEW_ROW = [
    "203",
    "LlamaIndex",
    "@llama_index",
    "runllama.ai",
    "https://www.llamaindex.ai",
    "Jerry Liu (CEO) + Simon Suo (CTO)",
    "ai_agents_infra",
    "1",
    "privacy@runllama.ai",
    "privacy@runllama.ai",
    "",
    "289_llamaindex.md",
    TIER_REASON,
]

with open(CSV, "a", encoding="utf-8", errors="replace", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(NEW_ROW)

with open(CSV, "r", encoding="utf-8", errors="replace") as f:
    rows2 = list(csv.reader(f))
print("Total rows now:", len(rows2))
print("Last row:", rows2[-1][0], rows2[-1][1], rows2[-1][8])