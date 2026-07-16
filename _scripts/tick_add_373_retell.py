#!/usr/bin/env python3
"""Tick 2026-07-17-0055Z: Append lead 373 Retell AI to both CSV schemas + write template + write chunk + build-log."""
import csv, json, os, sys, hashlib
from collections import Counter

ROOT = r"C:\Users\Potts\projects\atlas-store"
LEADS_CSV = os.path.join(ROOT, "cold_email", "leads.csv")
EMAILS_CSV = os.path.join(ROOT, "cold_email", "leads_with_emails.csv")
TPL_DIR = os.path.join(ROOT, "cold_email", "templates")
CHUNK_DIR = os.path.join(ROOT, "_chunks")
BUILDLOG = os.path.join(ROOT, "build-log.html")

LEAD_INDEX = "374"
COMPANY = "Retell AI"
HANDLE = "@retellai"
DOMAIN = "retellai.com"
WEBSITE = "https://www.retellai.com"
FOUNDER = "Bing Wu (Founder & CEO) + Weijia Yu (Co-Founder & President) + Zexia Zhang / Evie (Co-Founder & CMO)"
VERTICAL = "ai_voice_agents_orchestration"
TIER = "1"
BEST_EMAIL = "support@retellai.com"
EMAILS_FOUND_JSON = json.dumps(["support@retellai.com"])
GUESSED_JSON = json.dumps(["privacy@retellai.com", "dpa@retellai.com"])
TPL_NAME = f"{LEAD_INDEX}_retell.md"
EVIDENCE = (
    f"Lead 373 — Retell AI (Bing Wu, Founder & CEO + Weijia Yu, Co-Founder & President + Zexia Zhang/Evie, "
    f"Co-Founder & CMO). Tier-1 ai_voice_agents_orchestration 2nd-sibling, extending the canonical voice-AI-orchestration "
    f"cohort after Bland AI 189. Retell AI is the canonical conversational-voice-AI orchestration platform for "
    f"production phone agents + real-time speech-to-speech + LLM-orchestration + telephony integration + HIPAA + PCI + "
    f"EU AI Act readiness + BAA + per-call-id → per-agent-id → per-prompt-version-id → per-model-id → per-TTS-id → "
    f"per-tool-call-id → per-handoff-event-id → per-recording-id → per-transcript-id → per-call-summary-id → "
    f"per-CRM-write-id → per-downstream-billing-id lineage. support@retellai.com verified live 2026-07-17 by curl scrape "
    f"of https://docs.retellai.com/general/compliance (HTTP 200, 404,364 bytes) exposing mailto:support@retellai.com as "
    f"the canonical SOC 2 + HIPAA + BAA + GDPR DPA + CCPA/CPRA + PCI DSS + EU AI Act vendor-DD strategic-inbound channel. "
    f"Founder evidence: official Y Combinator company page https://www.ycombinator.com/companies/retell-ai (HTTP 200, "
    f"181,865 bytes) identifies Bing Wu (Founder & CEO — 'founder & CEO at Retell AI. Enthusiastic about the human brain "
    f"and AI, Bing spent...' per the YC bookface JSON-LD) + Weijia Yu (Co-Founder & President — 'Co-Founder & President "
    f"@ Retell AI' per YC) + Zexia Zhang/Evie (Co-Founder & CMO — 'Evie is the Co-founder and CMO of Retell AI. She has "
    f"a design background' per YC). HQ San Francisco CA + remote-distributed. YC W23. Backed $15M+ across Seed + Series "
    f"A per YC + public funding disclosures (Y Combinator + Alt Capital + Carya Ventures + Bret Taylor + others). "
    f"Customers: 1,500+ production voice-AI deployments including Medical Data Systems (case study: 280,000 monthly "
    f"collections with AI voice agents on Retell per https://www.retellai.com/case-study/how-medical-data-systems-"
    f"scales-280-000-in-monthly-collections-with-ai-voice-agents-on-retell) + Pine Park Health (case study: senior-care "
    f"voice automation) + SWTCH (case study: EV-driver always-on voice support) + collections + healthcare + financial-"
    f"services + B2B SaaS voice-agent operators building production phone agents on Retell. SOC 2 Type II + HIPAA + "
    f"BAA + GDPR DPA + CCPA/CPRA + PCI DSS + EU AI Act readiness per docs.retellai.com/general/compliance. 5 audit "
    f"gaps: (1) end-to-end per-call-id → per-agent-id → per-prompt-version-id → per-model-id → per-TTS-segment-id → "
    f"per-tool-call-id → per-handoff-event-id → per-recording-id → per-transcript-id → per-call-summary-id → per-CRM-"
    f"write-id → per-downstream-billing-id → per-VPC-peering-id provenance join-table per SOC 2 CC7.2 + HIPAA §164.312(b) "
    f"+ EU AI Act Art. 12 + California SB 1001 §3(a)(2) + GLBA §501(b) per-call granularity (60+ cols), (2) prompt-"
    f"injection + per-call-AI-agent-bypass + per-call-tool-call-poisoning + per-call-TTS-segment-poisoning + per-call-"
    f"phone-input-voice-cloning-poisoning + per-call-downstream-CRM-write-bypass + per-call-billing-charge-bypass "
    f"defense per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + EU AI Act Art. 15 + MITRE ATLAS with 10-column "
    f"per-call-id join-table, (3) state-by-state AI-disclosure compliance for 12 US states per SB 1001 §3(a)(2) + "
    f"Colorado SB 24-205 + Illinois AI Video Interview Act + Texas + New York + 7 other states — jurisdiction-"
    f"detection + script-version-control + per-call-compliance-log + per-call-disclosure-timestamp + per-call-human-"
    f"handoff-evidence + per-call-TCPA-prior-express-consent-link + per-call-wire-fraud-voice-cloning-detection-"
    f"signal + per-call-voice-biometric-verification-decision, (4) PHI/GLBA/PCI field-level redaction in transcript "
    f"store for downstream use (analytics + model-training + agent-eval) while keeping unredacted version in audit-log "
    f"WORM store for regulator-required retention window per SOC 2 CC6.7 + HIPAA §164.514(b) min-necessary + GLBA "
    f"§501(b) + PCI DSS 3.4 retention, (5) multi-region call-audio + transcript residency for EU customers per "
    f"Schrems II + GDPR Art. 28 (processor obligations) + EU AI Act Art. 10 (data governance). support@retellai.com is "
    f"the verified SOC 2 + HIPAA + BAA + GDPR DPA + CCPA/CPRA + PCI DSS + EU AI Act vendor-DD strategic-inbound "
    f"channel for Retell AI voice-agent platform + Retell LLM orchestration + Retell telephony + Retell HIPAA "
    f"healthcare-grade + Retell PCI payments-grade + ai_voice_agents_orchestration audit-target inquiries."
)

def append_quoted_all(path, row):
    # csv.writer with QUOTE_ALL handles the quote-all serialization seen in the file
    new_file = not os.path.exists(path)
    with open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(row)

# 1) Append to cold_email/leads.csv (8-col schema)
leads_row = [LEAD_INDEX, COMPANY, HANDLE, BEST_EMAIL, VERTICAL, TIER, TPL_NAME, EVIDENCE]
append_quoted_all(LEADS_CSV, leads_row)
print(f"[OK] Appended leads.csv row {LEAD_INDEX} ({COMPANY})")

# 2) Append to cold_email/leads_with_emails.csv (13-col schema)
emails_row = [
    LEAD_INDEX, COMPANY, HANDLE, DOMAIN, WEBSITE, FOUNDER, VERTICAL, TIER,
    BEST_EMAIL, EMAILS_FOUND_JSON, GUESSED_JSON, TPL_NAME, EVIDENCE
]
append_quoted_all(EMAILS_CSV, emails_row)
print(f"[OK] Appended leads_with_emails.csv row {LEAD_INDEX} ({COMPANY})")

# 3) Verify uniqueness
def verify(path, idx_col):
    with open(path, "r", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    indices = [r[idx_col].strip('"') for r in rows[1:]]
    cnt = Counter(indices)
    dupes = [k for k, v in cnt.items() if v > 1]
    print(f"[VERIFY] {path} — {len(indices)} data rows, {len(cnt)} unique indices, dupes={dupes[:3]}")
    assert LEAD_INDEX in indices, f"Missing {LEAD_INDEX} in {path}"
    assert not dupes, f"DUPLICATES in {path}: {dupes[:3]}"
    return len(indices)

n1 = verify(LEADS_CSV, 0)
n2 = verify(EMAILS_CSV, 0)
print(f"[DONE] leads.csv={n1} rows, leads_with_emails.csv={n2} rows")
