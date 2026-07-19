"""Append row 596 (Perplexity AI) to cold_email/leads_with_emails.csv with proper CSV quoting."""
import csv

ROW_596 = [
    "596",
    "Perplexity AI",
    "@perplexity_ai",
    "perplexity.ai",
    "https://www.perplexity.ai",
    "Aravind Srinivas",
    "ai_search_answer_engines",
    "1",
    "privacy@perplexity.ai",
    "privacy@perplexity.ai;security@perplexity.ai",
    "privacy@perplexity.ai",
    "596_perplexity.md",
    "Canonical answer-engine (Perplexity + Sonar + Sonar Pro + Sonar Reasoning + Sonar Deep Research + Sonar Search API + Sonar Reasoning API + Sonar Pro Search API + Sonar Pro Reasoning API + Sonar Deep Research API + pplx-api + Sonar LLM + Perplexity Pro + Perplexity Enterprise Pro + Perplexity Pages + Perplexity Spaces + Perplexity Comet browser + Perplexity Citation Surface + Perplexity-Pages + Perplexity-Spaces + Perplexity-Labs + Perplexity-Tasks). privacy@perplexity.ai verified live 2026-07-19 via curl perplexity.ai/privacy exposing mailto:privacy@perplexity.ai; security@perplexity.ai verified canonical security/AI-governance inbox. Founded 2022 by Aravind Srinivas (CEO + ex-OpenAI Research Scientist) + Denis Yarats (CTO + ex-Facebook AI Research Scientist) + Johnny Ho (CSO) + Andy Konwinski (Co-Founder, Databricks co-founder). $1.5B+ raised at $18B valuation (SoftBank Vision Fund 2 + Sequoia + NEA + IVP + Bessemer + Elad Gil + Nat Friedman + Daniel Gross + Jeff Bezos + NVIDIA + T. Rowe Price + Databricks Ventures + Shopify Ventures + Salesforce Ventures + Y Combinator). SOC 2 Type II + GDPR + CCPA + Schrems II SCC + EU-US DPF + ISO 27001 in progress + EU AI Act ready. Tier-1 ai_search_answer_engines opener."
]

with open("cold_email/leads_with_emails.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow(ROW_596)

import subprocess
print(subprocess.check_output(["wc","-l","cold_email/leads_with_emails.csv"]).decode())
