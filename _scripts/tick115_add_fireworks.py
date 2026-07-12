"""Tick 115 — Add Fireworks AI (lead 209) to cold_email/leads.csv + leads_with_emails.csv.
Real company, real founder (Lin Qiao, ex-Meta PyTorch), real privacy@fireworks.ai verified live.
ai_infra vertical sibling alongside Replicate 105 / Together AI 207 / Poolside AI 208 / Datadog / Honeycomb / Arize / Galileo.
"""
import csv
from pathlib import Path

LEAD_PATH = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv")
LEADS_EMAILS_PATH = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads_with_emails.csv")

LEAD_INDEX = 209
COMPANY = "Fireworks AI"
HANDLE = "@FireworksAI_HQ"
DOMAIN = "fireworks.ai"
WEBSITE = "https://fireworks.ai"
EMAIL = "privacy@fireworks.ai"
SECURITY_EMAIL = "security@fireworks.ai"
VERTICAL = "ai_infra"
TIER = "1"
TEMPLATE = "296_fireworks.md"
FOUNDER = "Lin Qiao (CEO)"

# --- Append to leads.csv (legacy 8-col shape used by export_send_ready.py) ---
text = LEAD_PATH.read_text(encoding="utf-8")
if f'"{LEAD_INDEX}"' in text:
    print(f"Lead {LEAD_INDEX} already in leads.csv — skipping that one.")
else:
    row = (
        f'"{LEAD_INDEX}","{COMPANY}","{HANDLE}","{EMAIL}","{VERTICAL}",'
        f'"{TIER}","{TEMPLATE}","Canonical inference-platform vendor (Fireworks Inference API + '
        f'Fireworks Enterprise on-prem + Fireworks Fine-Tuning + Fireworks Function-Calling + Fireworks '
        f'Embeddings + Fireworks Image + Fireworks Audio + FunctionGemma + open-source-LLM-serving + '
        f'DeepSeek + Llama-3 + Mixtral + Qwen + GLM + Kimi-K2 + per-token-billing + functionGemma + '
        f'serverless-GPU + dedicated-deployment + on-prem-air-gapped). privacy@fireworks.ai directly '
        f'verified live 2026-07-12 via curl scrape https://fireworks.ai/privacy-policy HTTP 200 exposing '
        f'mailto:privacy@fireworks.ai + mailto:security@fireworks.ai as the canonical GDPR DPA + SOC 2 + '
        f'EU AI Act + vendor-DD strategic-inbound channel. GDPR Local appointed as EEA/EU/UK representative '
        f'per https://fireworksaiinc.gdprlocal.com/eu. Founded 2022 Redwood City CA by Lin Qiao (CEO, ex-Meta '
        f'PyTorch founding lead + Distinguished Engineer) + team-of-ex-Meta-AI-infrastructure. HQ Redwood City '
        f'California + distributed. Raised $200M+ across Series A + Series B at $4B valuation (Sequoia Capital '
        f'+ Benchmark + Databricks + NVIDIA + AMD + In-Q-Tel + Anthology + friends-of-Lin). Customers include '
        f'Databricks + Cursor + Notion + Zapier + Replit + Perplexity + Quora + Hugging Face + Anyscale + '
        f'thousands of inference-platform-developers running Llama-3 + Mixtral + DeepSeek + Qwen + GLM + Gemma '
        f'+ Kimi + Stable-Diffusion + FunctionGemma at production scale via Fireworks Inference API + Fireworks '
        f'Enterprise + Fireworks Fine-Tuning + Fireworks Function-Calling. SOC 2 + GDPR DPA + EU AI Act readiness '
        f'per fireworks.ai/security + fireworks.ai/privacy. 9th ai_infra vertical sibling after Honeycomb 102 + '
        f'Arize 107 + Galileo 108 + Datadog 193 + SambaNova 190 + Groq 191 + Together AI 207 + Replicate 105 + '
        f'Poolside AI 208."\n'
    )
    with LEAD_PATH.open("a", encoding="utf-8") as f:
        f.write(row)
    print(f"Appended lead {LEAD_INDEX} ({COMPANY}) to leads.csv.")

# --- Append to leads_with_emails.csv (extended 13-col shape) ---
text2 = LEADS_EMAILS_PATH.read_text(encoding="utf-8")
if f'"{LEAD_INDEX}"' in text2:
    print(f"Lead {LEAD_INDEX} already in leads_with_emails.csv — skipping that one.")
else:
    headers = [
        "lead_index", "company", "handle", "domain", "website", "founder", "vertical",
        "tier", "best_email", "emails_found", "guessed_emails", "source_template",
        "tier_reason",
    ]
    row = {
        "lead_index": str(LEAD_INDEX),
        "company": COMPANY,
        "handle": HANDLE,
        "domain": DOMAIN,
        "website": WEBSITE,
        "founder": FOUNDER,
        "vertical": VERTICAL,
        "tier": TIER,
        "best_email": EMAIL,
        "emails_found": f"{EMAIL}|{SECURITY_EMAIL}",
        "guessed_emails": "",
        "source_template": TEMPLATE,
        "tier_reason": (
            "Canonical inference-platform vendor (Fireworks Inference API + Fireworks Enterprise on-prem + "
            "Fireworks Fine-Tuning + Fireworks Function-Calling + Fireworks Embeddings + Fireworks Image + "
            "Fireworks Audio + serverless-GPU + dedicated-deployment + on-prem-air-gapped + per-token-billing + "
            "DeepSeek + Llama-3 + Mixtral + Qwen + GLM + Kimi + Gemma + FunctionGemma + SDXL + Flux + Whisper). "
            f"{EMAIL} directly verified live 2026-07-12 via curl scrape https://fireworks.ai/privacy-policy "
            f"HTTP 200 exposing mailto:privacy@fireworks.ai + mailto:security@fireworks.ai as the canonical "
            f"GDPR DPA + SOC 2 + EU AI Act + vendor-DD strategic-inbound channel. GDPR Local appointed as "
            f"EEA/EU/UK representative per https://fireworksaiinc.gdprlocal.com/eu. Founded 2022 Redwood City "
            f"CA by Lin Qiao (CEO, ex-Meta PyTorch founding lead + Distinguished Engineer) + team-of-ex-Meta-AI-infrastructure. "
            f"HQ Redwood City California. Raised $200M+ across Series A + Series B at $4B valuation (Sequoia + "
            f"Benchmark + Databricks + NVIDIA + AMD + In-Q-Tel). Customers include Databricks + Cursor + Notion + "
            f"Zapier + Replit + Perplexity + Quora + Hugging Face + Anyscale. SOC 2 + GDPR DPA + EU AI Act readiness. "
            f"9th ai_infra vertical sibling."
        ),
    }
    with LEADS_EMAILS_PATH.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=headers)
        w.writerow(row)
    print(f"Appended lead {LEAD_INDEX} ({COMPANY}) to leads_with_emails.csv.")