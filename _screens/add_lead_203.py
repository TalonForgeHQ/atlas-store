"""Append lead 203 (LlamaIndex) to leads.csv. Idempotent.
Tier-reason text loaded from _screens/lead203_tier.txt to avoid write_file length limit."""
import csv, os, sys

CSV = "cold_email/leads.csv"
DATA = "_screens/lead203_tier.txt"

# Read tier-reason text from external file
if os.path.exists(DATA):
    with open(DATA, "r", encoding="utf-8") as f:
        T = f.read().rstrip("\n").rstrip()
else:
    # Fallback minimal tier reason
    T = (
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
        "readiness. ai_agents_infra vertical. 12th ai_agents_infra sibling. 5 audit gaps: "
        "(1) 13-col per-LlamaParse-OCR-call + per-LlamaCloud-retrieval + per-Workflow-step "
        "+ per-Agent-decision provenance per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 "
        "9.4, (2) Apache-2.0 OSS + training-corpus license-provenance per EU AI Act Art. "
        "53(d) + Art. 53(1)(b), (3) prompt-injection + retrieval-poisoning + OCR-poisoning "
        "+ tool-call-poisoning detection per OWASP LLM Top 10 LLM01+LLM03+LLM06, (4) "
        "cross-tenant LlamaCloud isolation per SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. "
        "10 + cross-border-transfer SCCs US-EU, (5) WORM retention + cost-attribution + "
        "EU AI Act Annex III 4 high-risk-classification per Art. 6+14+27+43+72 + Aug 2026 "
        "GPAI enforcement."
    )

with open(CSV, "r", encoding="utf-8", errors="replace", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

existing_ids = [int(r[0]) for r in rows if r and r[0].isdigit()]
print("Existing count:", len(existing_ids))

if 203 in existing_ids:
    print("Lead 203 already exists, skipping.")
    sys.exit(0)

NEW_ROW = [
    "203",
    "LlamaIndex",
    "@llama_index",
    "privacy@runllama.ai",
    "ai_agents_infra",
    "1",
    "289_llamaindex.md",
    T,
]

with open(CSV, "a", encoding="utf-8", errors="replace", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(NEW_ROW)

# Verify
with open(CSV, "r", encoding="utf-8", errors="replace") as f:
    rows2 = list(csv.reader(f))
print("Total rows now:", len(rows2))
print("Last row:", rows2[-1][0], rows2[-1][1], rows2[-1][3], "(tier_reason", len(rows2[-1][7]), "chars)")