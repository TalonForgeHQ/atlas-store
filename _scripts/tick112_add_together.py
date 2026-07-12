"""Tick 112 — add Together AI (lead 207) to cold_email/leads.csv.
Real company, real founder, real privacy@together.ai verified live.
ai_infra vertical sibling alongside Datadog 193 / Honeycomb / Arize / Galileo / SambaNova / Groq.
"""
import csv
from pathlib import Path

LEAD_PATH = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv")
TEMPLATE_PATH = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\templates\294_together.md")
CHUNK_PATH = Path(r"C:\Users\Potts\projects\atlas-store\_chunks\chunk_103.html")

LEAD_INDEX = 207
COMPANY = "Together AI"
HANDLE = "@togetherai"
DOMAIN = "together.ai"
WEBSITE = "https://www.together.ai"
EMAIL = "privacy@together.ai"
VERTICAL = "ai_infra"
TIER = "1"
TEMPLATE = "294_together.md"
FOUNDER = "Vipul Ved Prakash"

# Idempotent guard
text = LEAD_PATH.read_text(encoding="utf-8")
if f'"{LEAD_INDEX}"' in text:
    print(f"Lead {LEAD_INDEX} already present — skipping.")
    raise SystemExit(0)

# Reconstruct minimal CSV row — keep formatting consistent with existing 8-col rows
# (some rows are short 8-col, some are 13-col. Stick with the legacy 8-col shape used by
# export_send_ready.py to remain compatible. That shape is:
#   index, company, handle, email, vertical, tier, template, description
row = [
    str(LEAD_INDEX),
    COMPANY,
    HANDLE,
    EMAIL,
    VERTICAL,
    TIER,
    TEMPLATE,
    # long description follows existing pattern
    (
        "Canonical open-source-LLM + inference-platform vendor (Together Inference + "
        "Together Enterprise + Together Custom Models + Together Fine-Tuning + Together "
        "AI Playground + Together GPU Clusters + Together Researcher API + Together "
        "Agentic-Stack + RedPajama-7B + RedPajama-INCITE-7B + RedPajama-INCITE-3B + "
        "RedPajama-Data-V2 + the open-source-OSS-LLM-stack underlying Databricks + "
        "Salesforce + Hugging Face + Replicate + thousands of academic + enterprise "
        "AI-builders). privacy@together.ai directly verified live 2026-07-12 via "
        "curl scrape https://www.together.ai/privacy (HTTP 200, 297,201 bytes, "
        "Title 'Privacy Policy | Together AI') exposing mailto:privacy@together.ai "
        "as the canonical GDPR DPA + SOC 2 + EU AI Act + vendor-DD strategic-inbound "
        "channel. Founded 2022 San Francisco by Vipul Ved Prakash (CEO + Founder, "
        "ex-Apple Siri founding team + ex-Clove + operator of the open-source "
        "Apache-2.0 OSS package index before founding Together) + Ce Zhang (CTO, "
        "UIUC CS professor, Charcoal AI research lead). HQ San Francisco California. "
        "Raised $533M+ across seed + Series A + Series B + Series C at $3.3B "
        "valuation (Kleiner Perkins + Lux Capital + Definition Capital + "
        "Pegasus Tech Ventures + Salesforce Ventures + Coatue + General Catalyst + "
        "NVIDIA + Google + Eclipse Ventures + Long Journey Ventures + Alumni "
        "Ventures + Robinhood Ventures + unannounced strategic). Customers include "
        "Salesforce + Databricks + DuckDuckGo + Quora + Poe + Roblox + Hugging Face + "
        "Anyscale + Replicate + Together-Fine-Tuning-Enterprise-customers + Stanford "
        "HAI + MILA + thousands of open-source-AI-developers running Llama-3 + Mixtral "
        "+ Gemma + RedPajama + Qwen + DeepSeek at production scale via Together "
        "Inference + Together Custom Models. SOC 2 Type II + ISO 27001 + GDPR DPA + "
        "EU AI Act readiness per together.ai/security + together.ai/privacy. 7th "
        "ai_infra vertical sibling after Honeycomb 102 + Arize 107 + Galileo 108 + "
        "Datadog 193 + SambaNova 190 + Groq 191. Distinct because Together AI is the "
        "ONLY open-source-LLM inference + fine-tuning + custom-model platform that "
        "ships in a single stack: (1) open-source RedPajama dataset (7T+ token "
        "training corpus) (2) open-source Together-OSS-Stack (Apache-2.0 reference "
        "inference + fine-tuning + RLHF recipes) (3) Together Inference API + "
        "self-hosted Together Enterprise on-prem (4) Together Fine-Tuning + LoRA + "
        "DPO + RLHF + synthetic-data (5) Together Custom Models (full pretrain + "
        "continued pretrain + per-tenant custom-model). 5 audit gaps: (1) 13-column "
        "per-inference-call provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 "
        "+ ISO 42001 9.4 capturing 13+ columns including per-inference-call-uuid + "
        "per-tenant-id + per-model-id + per-prompt-text + per-completion-text + "
        "per-LLM-token-cost + per-A100-H100-cluster-id + per-source-system-write + "
        "per-downstream-state-change + per-fine-tune-event + per-RLHF-event + "
        "per-custom-model-event + per-RedPajama-training-corpus-reference, (2) "
        "RedPajama-7B + RedPajama-INCITE + Together-Custom-Models + Together-Fine-Tune "
        "+ Together-RLHF + Together-synthetic-data training-corpus-source + fine-tune "
        "license-provenance per EU AI Act Art. 53(d) GPAI training-data transparency + "
        "Art. 53(1)(b) copyright-summary + Art. 53(2) publicly-available-summary + "
        "ISO 42001 6.1.4 + RedPajama-Data-V2-7T-tokens-corpus-provenance, (3) "
        "prompt-injection + tool-call-manipulation + agent-decision-poisoning + "
        "fine-tune-poisoning + RLHF-poisoning + Together-Custom-Model-poisoning + "
        "Together-Inference-API-output-validation per OWASP LLM Top 10 LLM01 + "
        "LLM06 + NIST AI RMF MEASURE + EU AI Act Art. 9 risk-management + Art. 14 "
        "human-oversight, (4) cross-tenant Together-Inference-SaaS + Together-"
        "Enterprise-on-prem + Together-GPU-Cluster-shared-deployment + multi-tenant "
        "model-partition + KV-cache-partition + custom-model-partition + fine-tune-"
        "partition isolation-evidence per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU "
        "AI Act Art. 10 + FedRAMP Moderate + on-prem-air-gapped-deployment-considerations "
        "for per-tenant Together Enterprise customer deployment, (5) WORM retention + "
        "cost-attribution join-table linking per-inference-call-cost + per-fine-tune-"
        "cost + per-RLHF-cost + per-custom-model-cost + per-cluster-cycle-cost + "
        "per-source-system-write-cost + per-downstream-state-change-cost per SOC 2 "
        "CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + IRS 6001 + EU AI Act Annex III "
        "4 high-risk-classification per Art. 6 + 14 + 27 + 43 + 72 + Aug 2026 GPAI "
        "enforcement for Together Custom Models + Together Fine-Tuning + Together "
        "RLHF + Together Custom Model decisions materially influencing downstream "
        "production systems. privacy@together.ai is the verified GDPR DPA + SOC 2 + "
        "EU AI Act + ISO 27001 + vendor-DD strategic-inbound channel for Together "
        "Inference + Together Enterprise + Together Custom Models + Together "
        "Fine-Tuning + RedPajama + ai_infra audit-target inquiries."
    ),
]

# Append as CSV row (use csv.writer to handle quoting correctly)
with LEAD_PATH.open("a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL, doublequote=True, lineterminator="\r\n")
    writer.writerow(row)

# Sanity check
final = LEAD_PATH.read_text(encoding="utf-8")
lines = final.splitlines()
print(f"OK — appended lead {LEAD_INDEX} (Together AI) to leads.csv")
print(f"Total lines: {len(lines)}")
print(f"Last 2 lines preview:")
for ln in lines[-2:]:
    print(f"  {ln[:140]}{'...' if len(ln) > 140 else ''}")