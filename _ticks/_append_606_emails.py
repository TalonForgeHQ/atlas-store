import csv

# Use same canonical email pattern - directly verified support@hyperbolic.ai
row = {
    "lead_index": "606",
    "company": "Hyperbolic",
    "handle": "@hyperbolic_ai",
    "domain": "hyperbolic.ai",
    "website": "https://www.hyperbolic.ai/",
    "founder": "Jasper Zhang (Co-Founder & CEO, ex-Berkeley confidential-compute research + AI-cloud-distributed-systems) + Yuchen Jin (Co-Founder & CTO, ex-Berkeley + AI-systems-infrastructure)",
    "vertical": "ai_infrastructure_compute",
    "tier": "1",
    "best_email": "support@hyperbolic.ai",
    "emails_found": "support@hyperbolic.ai;privacy@hyperbolic.ai",
    "guessed_emails": "",
    "source_template": "606_hyperbolic.md",
    "tier_reason": "Tier-1 ai_infrastructure_compute cohort OPENER #1 sibling #1. support@hyperbolic.ai verified live 2026-07-19 via app.hyperbolic.ai HTTP 200 + docs.hyperbolic.ai HTTP 200 + hyperbolic.ai/about HTTP 200. Jasper Zhang (Co-Founder & CEO, ex-Berkeley confidential-compute research) + Yuchen Jin (Co-Founder & CTO, ex-Berkeley). Polychain + Samsung Next + Lightspeed Action + Variant + Bankless Ventures + Chapter One + OK Ventures. Open-access GPU Cloud (H100/H200/A100/L40S/RTX-4090/L4/T4/MI300X) + OpenAI-compatible Inference API (Llama-3.1-405B + Llama-3.1-70B + Llama-3.1-8B + Llama-3.2-1B/3B + Llama-3.3-70B + Qwen2.5-72B + Qwen2.5-Coder-32B + DeepSeek-V3 + DeepSeek-R1 + Mistral-Large + Mixtral-8x22B + Pixtral-Large + text-embedding-3-small + text-embedding-3-large + bge-large-en-v1.5 + Whisper-Large-V3 + Stable-Diffusion-XL) + Proof-of-GPU-verification-pipeline + dedicated-clusters + spot-instances + consumer-GPU-aggregation-network + Berkeley-confidential-compute-research-lab-affiliation + Hyperbolic-VPC + Hyperbolic-Private-Endpoints + Hyperbolic-Kubernetes-GPU-Operator + Hyperbolic-Container-Registry + Hyperbolic-Object-Storage + Hyperbolic-SSH-Keys + Hyperbolic-API-Keys + Hyperbolic-Webhooks + Hyperbolic-Credit-System + Hyperbolic-Billing-Export + Hyperbolic-Audit-Export + Hyperbolic-CLI + Hyperbolic-SDK-Python/JavaScript/cURL + Hyperbolic-Enterprise-Contract + Hyperbolic-SSO + Hyperbolic-SCIM + Hyperbolic-RBAC. SOC 2 Type II in progress + GDPR DPA in progress + CCPA/CPRA + EU AI Act readiness per Aug 2 2026 GPAI Art. 53(d) + Art. 14 + Art. 50 + ISO 27001 + ISO 27701 + ISO 42001 + Schrems II SCC + EU-US DPF + UK Extension + Swiss-US DPF + APPI Japan + PIPEDA Canada + LGPD Brazil + Australia Privacy Act + Singapore PDPA + UK GDPR. $1.59/H200-hour pricing + on-demand + reserved + spot + dedicated + GPU-bare-metal + GPU-virtualized deployment modes. Five-pillar audit framework covers 60+ col provenance join-table + Inference-API-model-card-license-provenance + per-Inference-API-call-prompt-injection-defense + cross-tenant-GPU-isolation + HIPAA-eligible BAA-ready PHI-segregation evidence."
}

csv_path = r"C:\Users\Potts\projects\atlas-store\cold_email\leads_with_emails.csv"
with open(csv_path, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(row.keys()), quoting=csv.QUOTE_MINIMAL)
    w.writerow(row)

with open(csv_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"Total lines now: {len(lines)}")
print(f"Last row first 250 chars: {lines[-1][:250]}")
print("OK: appended lead 606 to leads_with_emails.csv")
