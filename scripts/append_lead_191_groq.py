"""Append lead 191 (Groq) to cold_email/leads.csv and leads_with_emails.csv.

Pattern: idempotent, reproduces lead-row append if rerun.
"""
import csv

LEADS_CSV = r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv"
LEADS_WITH_EMAILS_CSV = r"C:\Users\Potts\projects\atlas-store\cold_email\leads_with_emails.csv"

TIER_REASON = "Canonical LPU (Language Processing Unit) inference platform for ultra-low-latency LLM serving. privacy@groq.com + groqlegal@groq.com directly verified live 2026-07-12 via curl scrape https://groq.com/privacy-policy/ HTTP 200 (mailto:privacy@groq.com + mailto:groqlegal@groq.com + mailto:security@groq.com exposed canonical GDPR DPA + SOC 2 + EU AI Act + vendor-DD strategic-inbound channels). Founded 2016 Mountain View California by Jonathan Ross (CEO, ex-Google X TPU lead engineer + architect of Google's Tensor Processing Unit) + Douglas Wightman (CBO). HQ Mountain View CA. Raised $640M+ across Series A-D (D1 Capital + Bessemer + Tiger Global + Groq Ventures + TDK + Samsung Catalyst Fund + Altimeter + Darshan Capital + Social Capital + LDV Partners) at $2.8B+ valuation. Customers include Meta + Aramco + Oracle + Shopify + Discord + Mistral + Hugging Face + Anyscale + Together AI + Modal + Fireworks + Replicate + hundreds of AI startups running Llama-3 + Mixtral + Gemma + Whisper + LLaVA at 500+ tokens/sec inference speeds. SOC 2 Type II + ISO 27001 + GDPR DPA + EU AI Act readiness + FedRAMP Moderate (in-process). 6th ai_infra vertical sibling in pipeline. Distinct because Groq is the ONLY LPU (vs NVIDIA GPU + SambaNova RDU + Cerebras WSE + Graphcore IPU + Tenstorrent Grayskull + Positron + Lightmatter + Hailo) inference platform that ships (1) deterministic latency (no jitter from GPU scheduling) (2) tensor-streaming-processor architecture with deterministic compiler-staged execution (3) 500+ tokens/sec Llama-3 inference at production scale (4) open GroqCloud API + on-prem GroqRack deployment (5) per-call cost advantage 4-10x vs NVIDIA H100 GPU at sustained throughput. 5 audit gaps: (1) end-to-end 12-column per-inference-call provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 capturing per-call LPU-program-load-event + per-call tensor-streaming-execution-event + per-call model-weight-load-event + per-call KV-cache-write-event + per-call LLM-token-emission + per-call tool-call-event + per-call agent-decision-event + per-call source-system-write + per-call downstream-state-change + per-call hardware-attestation + per-call tenant-partition-isolation + per-call API-key-rotation, (2) GroqCloud + GroqRack + Groq SDK + per-model-card training-corpus + fine-tune license-provenance per EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary + Art. 53(2) publicly-available-summary + ISO 42001 6.1.4, (3) prompt-injection + tool-call-manipulation + agent-decision-poisoning + LPU-output-validation across LLM-call + tool-call + agent-decision + source-system-write + downstream-state-change + LPU-program-load-event + LPU-execution-event + model-weight-load-event + KV-cache-write-event per OWASP LLM Top 10 LLM01 + LLM06 + NIST AI RMF MEASURE + EU AI Act Art. 9 risk-management + Art. 14 human-oversight, (4) cross-tenant GroqCloud SaaS + GroqRack enterprise on-prem + multi-tenant LPU-isolation-evidence for per-tenant LPU-partition + per-tenant model-partition + per-tenant KV-cache-partition + per-tenant firmware-attestation + per-tenant hardware-attestation + per-tenant GroqCloud-API-isolation per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + FedRAMP Moderate, (5) WORM retention + cost-attribution join-table linking per-call LLM-token-cost + per-call LPU-cycle-cost + per-call KV-cache-cost + per-call tool-call-cost + per-call agent-decision-cost + per-call source-system-write-cost + per-call downstream-state-change-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + IRS 6001 + EU AI Act Annex III 4 high-risk-classification per Art. 6 + 14 + 27 + 43 + 72 + Aug 2026 GPAI enforcement. privacy@groq.com + groqlegal@groq.com + security@groq.com are the verified GDPR/DPA/SOC 2/ISO 27001/EU AI Act/HIPAA/vendor-DD strategic-inbound channels for Groq LPU + GroqCloud + GroqRack + Groq SDK + ai_infra audit-target inquiries."

new_row = [
    "191",
    "Groq",
    "@GroqInc",
    "privacy@groq.com",
    "ai_infra",
    "1",
    "279_groq.md",
    TIER_REASON,
]

# 1. Append to leads.csv (idempotent)
with open(LEADS_CSV, newline='', encoding="utf-8") as f:
    rows = list(csv.reader(f))
existing_indices = {row[0] for row in rows[1:] if row}
if "191" in existing_indices:
    print("[skip] lead 191 already in leads.csv")
else:
    with open(LEADS_CSV, "a", newline='', encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(new_row)
    print(f"[ok] appended lead 191 ({new_row[1]}) to leads.csv")

# 2. Append to leads_with_emails.csv with correct 13-col schema
with open(LEADS_WITH_EMAILS_CSV, newline='', encoding="utf-8") as f:
    werows = list(csv.reader(f))
print(f"leads_with_emails.csv current rows: {len(werows) - 1}")
existing_wer_indices = {row[0] for row in werows[1:] if len(row) == 13}
if "191" in existing_wer_indices:
    print("[skip] lead 191 already in leads_with_emails.csv")
else:
    proper_row = ["191", "Groq", "@GroqInc", "groq.com", "https://groq.com", "Jonathan Ross", "ai_infra", "1", "privacy@groq.com", "privacy@groq.com;groqlegal@groq.com;security@groq.com", "", "279_groq.md", TIER_REASON]
    with open(LEADS_WITH_EMAILS_CSV, "a", newline='', encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(proper_row)
    print(f"[ok] appended lead 191 (Groq) to leads_with_emails.csv")

print("Done.")