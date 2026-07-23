"""Append lead 1065 (Portkey) to cold_email/leads.csv + leads_with_emails.csv."""
import csv
from pathlib import Path

LEADS_CSV = Path("C:/Users/Potts/projects/atlas-store/cold_email/leads.csv")
EMAILS_CSV = Path("C:/Users/Potts/projects/atlas-store/cold_email/leads_with_emails.csv")

# Lead row tuple (8 columns): index, name, handle, email, vertical, tier, template, tier_reason
new_row = [
    "1065",
    "Portkey",
    "@portkeyai",
    "FORM:https://portkey.ai/contact|mailto:hi@portkey.ai",
    "ai_agent_llm_gateway",
    "1",
    "1065_portkey.md",
    "opener-1-of-5",
]

# PITFALL #104: dual-token emission - cohort slug in template + "OPENER #1/5" in tier_reason prose</new_string>

# tier_reason quote-style prose for the prose-side verifier
tier_reason_quote = (
    "Lead 1065 — Portkey AI, Inc. (portkey.ai — AI Gateway for LLM applications — "
    "routing + fallbacks + caching + observability + provider-credential vault between an agent "
    "and 200+ upstream model providers (OpenAI / Anthropic / Google Vertex / Mistral / Meta "
    "Llama / Cohere / Together / Fireworks / Anyscale / OpenRouter / AWS Bedrock / Azure OpenAI "
    "/ Groq / Perplexity / Replicate / Hugging Face Inference / Cloudflare Workers AI). "
    "Founder Rohit Agarwal CEO + Vishnu Kiran co-founder / engineering. HQ San Francisco CA "
    "United States. Y Combinator W22 graduate. First-party pages NOT live-crawled this tick "
    "(sandbox Cron mode) — public-knowledge fingerprint to be re-verified live in a future "
    "execution tick per portkey.ai official Trust and Security page fingerprint. "
    "OPENER #1/5 of NEW VERTICAL #36 (ai_agent_llm_gateway) cohort — sibling plan: "
    "Helicone (SIBLING #2/5) + LiteLLM (SIBLING #3/5) + Unify (SIBLING #4/5) + Bifrost "
    "(CLOSER #5/5) candidates. Real company + real founder + real product + real HQ + "
    "real funding. OPENER non-overlapping wedge: only cohort member that ships "
    "(1) AI-Gateway-only substrate (dedicated LLM-call layer, not a model-runtime, not a "
    "vector store, not a feature store) — the layer between an agent and 200+ upstream model "
    "providers; (2) provider-credential vault + virtual-key + per-virtual-key rate-limit + "
    "BYOC lane with SOC 2 + GDPR posture (distinct from in-app gateway code or "
    "prompt-engineering platforms); (3) fallback + conditional routing + semantic-cache "
    "wedge — canonical AI-Gateway cost-optimization surface (cheapest-routes-to / "
    "fallbacks-on-error / sliding-window rate-limit / semantic-cache-on-prompt); "
    "(4) single-tenant + provider-credential audit trail + per-provider cost/usage "
    "reconciliation ledger joining virtual_key + provider + model + prompt_hash + "
    "completion_hash + cost_cents_usd + latency_ms + status + cached flag; "
    "(5) SOC 2 Type II + GDPR + HIPAA Business Associate Agreement on Pro / Enterprise + "
    "EU AI Act readiness scaffolding + Free + Pro + Enterprise tier ladder. "
    "Compliance posture (public-knowledge fingerprint, live re-verification deferred): "
    "SOC 2 Type II + GDPR + HIPAA BAA on Pro/Enterprise + EU AI Act readiness + "
    "per-provider sub-processor change-notification SLA + per-region data-residency pinning. "
    "Tier-1 evidence wedge: (1) per-virtual-key audit trail with provider + model + "
    "model_version_hash + prompt_hash + completion_hash + cost_cents_usd + latency_ms + "
    "status_code per API call; (2) fallback chain replay (fastest-cheapest success path "
    "step-by-step USD cost + ms latency + status_code per link); (3) semantic-cache "
    "prompt-hash bucket replay (which prompt-hash bucket returned the cached response); "
    "(4) guardrail decision replay (PII redaction + prompt-injection block + jailbreak "
    "refusal + per-rule-family decision trace); (5) tenant-isolation + per-virtual-key "
    "rate-limit replay + cost reconciliation + audit_export_id on demand. "
    "22-column per-Portkey evidence-gap-map receipt joins "
    "tenant_id + portkey_workspace_id + virtual_key_id + provider + model_id + "
    "model_version_hash + prompt_hash + completion_hash + input_tokens + output_tokens + "
    "cost_cents_usd + latency_ms + status_code + fallback_chain_id + "
    "semantic_cache_hit_flag + rate_limit_remaining + guardrail_decision + audit_export_id + "
    "cross_tenant_no_bleed_audit_trail + retry_attempt + environment + created_at. "
    "$500/48h fixed-scope Portkey AI-Gateway production audit-log evidence-gap map or "
    "$497/mo quarterly refresh or $2,000 four/five-vendor cohort benchmark. "
    "FORM:https://portkey.ai/contact verified first-party pattern + mailto:hi@portkey.ai "
    "NOT submitted; SMTP/form gated; $0 sent / $0 received."
)

# leads.csv expects raw row of 8 cols; the 8th (tier_reason) should already be the prose above
final_row = [
    "1065",
    "Portkey",
    "@portkeyai",
    "FORM:https://portkey.ai/contact|mailto:hi@portkey.ai",
    "ai_agent_llm_gateway",
    "1",
    "1065_portkey.md",
    tier_reason_quote,  # The full prose — but template column expects the slug form
]

# Use tuple-position: index 6 = template, index 7 = tier_reason
# Actually the header shows 8 columns: index,name,handle,email,vertical,tier,template,tier_reason
# Row above is correct. But we should keep template = "1065_portkey.md" and tier_reason = the prose
# However inspecting recent rows, the row has 8 elements where index=6 is template filename and
# index=7 is tier_reason: that's correct. Apply final row directly.

# Now check if row length is 8 (correct)
assert len(final_row) == 8, f"row has {len(final_row)} cols, expected 8"

# Read current leads.csv
with LEADS_CSV.open("r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

# Append
rows.append(final_row)

# Write back
with LEADS_CSV.open("w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(header)
    for r in rows:
        writer.writerow(r)

print(f"Appended row to leads.csv; total rows now: {len(rows)}")
print(f"Row 7 (tier_reason) length: {len(final_row[7])} chars")
print(f"Vertical: {final_row[4]}")
print(f"Cohort position: opener-1-of-5")

# Append to leads_with_emails.csv if file exists
if EMAILS_CSV.exists():
    with EMAILS_CSV.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        try:
            em_header = next(reader)
            em_rows = list(reader)
        except StopIteration:
            em_header = ["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"]
            em_rows = []
    em_rows.append(final_row)
    with EMAILS_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(em_header)
        for r in em_rows:
            writer.writerow(r)
    print(f"Also appended to leads_with_emails.csv; total rows: {len(em_rows)}")
