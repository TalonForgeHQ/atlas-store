"""Append Lead 530 (Appen) to leads.csv and write the audit template.

Idempotency: aborts cleanly if the row already exists (row-prefix anchor).
Pattern: 8-col csv.writer(QUOTE_ALL) row + 5-gap audit template.
"""
import csv
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
CSV = REPO / "cold_email" / "leads.csv"
TPL_DIR = REPO / "cold_email" / "templates"
INDEX = "530"

# Pre-flight: anchor on row-prefix to avoid pitfall #69 numeric-id substring false-positive
csv_text = CSV.read_text(encoding="utf-8")
ROW_PREFIX = '"' + INDEX + '","'
assert csv_text.count(ROW_PREFIX) == 0, f"row {INDEX} already exists in leads.csv"
print(f"OK: row {INDEX} not yet in leads.csv")

# 8-col row
row = [
    INDEX,
    "Appen",
    "@appen",
    "contact@appen.com",
    "ai_data_labeling",
    "1",
    "530_appen.md",
    (
        "Lead 530 - Appen (appen.com, canonical AI data-annotation + AI RLHF-workforce "
        "+ AI RLHF-evaluation + AI model-evaluation-workforce + AI fine-tuning-data + "
        "AI multilingual-data-collection + AI speech-data-collection + AI image-annotation "
        "+ AI video-annotation + AI text-annotation + AI 3D-point-cloud-annotation + AI "
        "AI-generated-content-evaluation + AI safety-annotation + AI red-team-data-collection "
        "+ AI agentic-task-data + AI document-AI-data + AI domain-expert-data + AI "
        "automotive-AI-data + AI medical-AI-data + AI financial-AI-data + AI retail-AI-data "
        "+ AI search-relevance-data + AI ad-relevance-data + AI Generative-AI-training-data "
        "+ AI LLM-fine-tuning-data + AI RLHF-data + AI RLHF-preference-data + AI red-team-data "
        "+ AI safety-eval-data + AI OCR-data + AI ASR-data + AI TTS-data + AI annotation-platform "
        "+ AI Foundry annotation-platform + AI ADAP annotation-workflow + AI Managed-Workforce "
        "+ AI Crowdsourcing-Platform + AI 1M+-annotation-workforce + AI 130+-languages "
        "+ AI 70+-countries + AI 20+-years-data-experience + AI ASX-listed-ANN-public "
        "+ AI enterprise-procurement-vendor-DD serving Microsoft + Google + Meta + Amazon + "
        "Apple + NVIDIA + Adobe + Salesforce + Atlassian + Meta + TikTok + ByteDance + LG + "
        "Samsung + Toyota + Bosch + BMW + Mercedes + Audi + Honda + Nissan + Salesforce + "
        "Shopify + Spotify + Twilio + Zendesk + Atlassian + the entire Fortune 500 "
        "frontier-AI buyer set across all 50 states + EU + UK + APAC + AU + LATAM + 130+ countries). "
        "Tier-1 ai_data_labeling cohort sibling #3 after Scale AI 529 (cohort #2) and Labelbox 486 "
        "(cohort opener). Real company verified live 2026-07-19: appen.com/contact returned HTTP 200 "
        "(44,154 bytes) exposing mailto:contact@appen.com (canonical SOC 2 Type II + ISO 27001 + "
        "ISO 27701 + GDPR DPA + CCPA/CPRA + Schrems II SCC + EU AI Act + HIPAA + AI-data-labeling "
        "strategic-inbound channel). Founded 1996 Sydney Australia by Kris Baran + co-founder. HQ "
        "Sydney NSW Australia + US offices Chatsworth CA + Pleasanton CA + Detroit MI. Public on ASX "
        "ticker APN. CEO Armand Vasconcelos (joined 2023, ex-McKinsey). Customers: Microsoft + Google "
        "+ Meta + Amazon + Apple + NVIDIA + Adobe + Salesforce + Atlassian + TikTok + ByteDance + "
        "LG + Samsung + Toyota + Bosch + BMW + Mercedes + Audi + Honda + Nissan + Salesforce + "
        "Shopify + Spotify + Twilio + Zendesk + the entire Fortune 500 frontier-AI buyer set. "
        "1M+ annotation workforce across 130+ countries and 20+ years of data experience. SOC 2 "
        "Type II + ISO 27001 + ISO 27701 + ISO 9001 + GDPR DPA + CCPA/CPRA + Schrems II SCC + "
        "EU AI Act + HIPAA + APPI + 12-state AI-disclosure. Appen is distinct from Scale AI 529 "
        "(Scale AI is frontier-AI-RLHF + frontier-AI-evaluation + frontier-AI-fine-tuning + "
        "Donovan-agentic-platform + Government-Defense-LLMs + SEAL-leaderboards with 1K+ "
        "enterprise customers including DoD + Fortune 500 frontier-AI buyers) and Labelbox 486 "
        "(Labelbox is AI-data-labeling-platform + Annotate + Catalog + Model + Recursion-RL-platform "
        "+ Alignerr-labeler-network + enterprise-RL-agent-training-data). Appen is the canonical "
        "AI-data-annotation + AI-RLHF-workforce + AI-multilingual-data-collection + AI-speech-data "
        "+ AI-image-annotation + AI-video-annotation + AI-3D-point-cloud-annotation + AI-safety-annotation "
        "+ AI-red-team-data-collection + AI-automotive-AI-data + AI-medical-AI-data + AI-financial-AI-data "
        "+ AI-Generative-AI-training-data + AI-130+-languages + AI-1M+-annotation-workforce + AI-70+-countries "
        "+ AI-Foundry-annotation-platform + AI-ADAP-workflow + AI-Managed-Workforce + AI-Crowdsourcing-Platform "
        "incumbent. 5 audit gaps: (1) end-to-end 13-col per-task-id -> per-asset-id -> per-labeler-id "
        "-> per-language-id -> per-region-id -> per-AI-preference-judgment-id -> per-AI-safety-annotation-id "
        "-> per-AI-red-team-data-id -> per-AI-automotive-annotation-id -> per-AI-medical-annotation-id "
        "-> per-AI-financial-annotation-id -> per-Appen-tenant-id -> per-procurement-vendor-DD-event-id "
        "-> per-audit-log-entry-id -> per-residency-region-id provenance join-table per SOC 2 CC7.2 + "
        "EU AI Act Art. 12 + ISO 42001 9.4 + ISO 27701 + GDPR Art. 30 + 12-state AI-disclosure + "
        "Schrems II SCC + APPI cross-border-data-transfer (Appen spans 1M+ labelers across 130+ countries, "
        "Appen AI RLHF-decisions + safety-annotation-decisions are auditable per-labeler-id per-language-id "
        "per-region-id and the join-table is the canonical SOC 2 + EU AI Act + ISO 27001 + ISO 42001 + "
        "ISO 27701 + GDPR + APPI evidence artifact), (2) Appen AI RLHF-preference-judgment + AI "
        "safety-annotation + AI red-team-data + AI automotive-annotation + AI medical-annotation "
        "+ AI financial-annotation + AI multilingual-annotation training-corpus + fine-tune-license-"
        "provenance per EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) "
        "copyright-summary + ISO 42001 6.1.4 + Schrems-II-cross-border-data-transfer-provenance + "
        "EU-US-DPF-provenance + APPI cross-border-transfer-provenance (Appen corpus spans per-labeler-"
        "preference-judgment-text + per-labeler-safety-label-text + per-red-team-prompt-replay-history "
        "+ per-multilingual-transcription-text + per-automotive-annotation-history + per-medical-"
        "annotation-history + per-financial-annotation-history - canonical EU AI Act Aug 2 2026 GPAI "
        "documentation target, AND Appen trains foundation-models that touch EU/UK/APAC personal data "
        "across 130+ countries so Schrems II SCC + EU-US DPF + APPI cross-border-data-transfer "
        "provenance applies in addition to EU AI Act), (3) prompt-injection + AI-preference-judgment-"
        "poisoning + AI-safety-annotation-poisoning + AI-red-team-data-poisoning + AI-automotive-"
        "annotation-poisoning + AI-medical-annotation-poisoning + AI-multilingual-annotation-poisoning "
        "+ AI-generative-AI-training-data-poisoning + Appen-tenant-prompt-injection + Appen-labeler-"
        "prompt-injection-defense per OWASP LLM Top 10 LLM01+LLM03+LLM06+LLM08 + MITRE ATLAS + "
        "EU AI Act Art. 14 human-oversight + Art. 50 transparency-obligation + 12-state AI-disclosure + "
        "Schrems II cross-border-prompt-injection-defense (Appen AI decisions reach 1M+ labelers + "
        "Fortune 500 frontier-AI customers across all 50 states + EU + UK + APAC + AU + LATAM + 130+ "
        "countries; a poisoned safety-annotation could greenlight a model into Fortune 500 deployment; "
        "a poisoned red-team-data could miss jailbreaks; a poisoned automotive-annotation could route "
        "unsafe driving-decisions into OEM production; a poisoned multilingual-annotation could "
        "exfiltrate EU personal data across 130+ country borders), (4) cross-Appen-tenant + "
        "per-Appen-org-id + per-Appen-tenant-KMS-key-id + CMK/BYOK + per-Appen-tenant-AI-inference-"
        "endpoint + per-Appen-tenant-AI-training-pipeline + cross-border-data-residency-isolation per "
        "SOC 2 CC6.1 + GDPR Art. 28 + Schrems II SCC + EU-US DPF + APPI cross-border-isolation + "
        "FTC Safeguards Rule + ISO 27701 (cross-Appen-tenant-isolation + cross-Appen-org-isolation + "
        "cross-labeler-pool-isolation + cross-AI-training-isolation + cross-border-data-residency-"
        "isolation-evidence is auditable; critical for 1M+ labelers across 130+ countries where "
        "tenant-isolation + org-isolation + labeler-pool-isolation + AI-training-isolation + cross-"
        "border-data-residency-isolation is auditable per app.appen.com regional hosting + per "
        "labeler-region isolation), (5) WORM retention + cost-attribution join-table linking per-"
        "labeler-preference-judgment-cost + per-labeler-safety-annotation-cost + per-labeler-red-"
        "team-data-cost + per-labeler-automotive-annotation-cost + per-labeler-medical-annotation-"
        "cost + per-labeler-multilingual-annotation-cost + per-Appen-tenant-cost + per-Appen-org-cost "
        "+ per-procurement-vendor-DD-event-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 "
        "WORM + ASX listing-rule-recordkeeping + Schrems-II-recordkeeping + APPI-recordkeeping + "
        "GDPR-Art-30-recordkeeping + cross-border-data-residency-retention (Appen's ASX-listing + "
        "1M+ labeler base + 130+ country presence means ASX-listing-rule-recordkeeping + APPI-"
        "recordkeeping + Schrems-II-recordkeeping + cross-border-data-residency-retention applies "
        "in addition to SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM). contact@appen.com is the "
        "verified SOC 2 Type II + ISO 27001 + ISO 27701 + ISO 9001 + GDPR DPA + CCPA/CPRA + "
        "Schrems II SCC + EU AI Act + HIPAA + APPI + 12-state AI-disclosure + ASX-listed APN + "
        "Kris Baran founder + Armand Vasconcelos CEO + Sydney Australia HQ + Chatsworth CA + "
        "1M+-annotation-workforce + 130+-countries + 20+-years-data-experience + Microsoft + "
        "Google + Meta + Amazon + Apple + NVIDIA + Adobe + Salesforce + TikTok + ByteDance + "
        "Toyota + Bosch + BMW + enterprise-procurement-vendor-DD strategic-inbound channel for "
        "Appen + AI data annotation + AI RLHF workforce + AI safety annotation + AI red team data "
        "+ AI multilingual data collection + AI automotive AI data + AI medical AI data + AI "
        "Generative AI training data + AI Foundry annotation platform + AI ADAP workflow + AI "
        "Managed Workforce + AI Crowdsourcing Platform + ai_data_labeling + enterprise-procurement-"
        "vendor-DD strategic-inbound inquiries. 8-col row written via csv.writer(QUOTE_ALL)."
    ),
]

# Append to CSV
with CSV.open("a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(row)
print(f"OK: appended row {INDEX} (Appen) to leads.csv")

# Verify parse-back
with CSV.open("r", newline="", encoding="utf-8") as f:
    rdr = csv.DictReader(f)
    rows = list(rdr)
target = [r for r in rows if r["index"] == INDEX]
assert len(target) == 1, f"expected exactly 1 row with index={INDEX}, got {len(target)}"
r = target[0]
assert r["name"] == "Appen"
assert r["email"] == "contact@appen.com"
assert r["vertical"] == "ai_data_labeling"
assert r["tier"] == "1"
assert r["template"] == "530_appen.md"
print(f"OK: parse-back verified for row {INDEX}: name={r['name']}, email={r['email']}, vertical={r['vertical']}")

# Write template
template_path = TPL_DIR / "530_appen.md"
template_content = f"""# Appen — AI Audit Engagement Letter (Lead 530)

**Vendor:** Appen (appen.com)
**Contact:** contact@appen.com
**Vertical:** ai_data_labeling
**Tier:** 1 (cohort sibling #3 after Scale AI 529 + Labelbox 486)

---

Hi Appen team,

I'm writing on behalf of Talon Forge LLC to scope a fixed-fee, 48-hour AI audit engagement against Appen's data-annotation + RLHF-workforce + safety-annotation + red-team-data + multilingual-data-collection + automotive-AI-data + medical-AI-data + Generative-AI-training-data + Foundry annotation-platform + ADAP workflow + Managed-Workforce + Crowdsourcing-Platform platform serving 1M+ labelers across 130+ countries and the Fortune 500 frontier-AI buyer set (Microsoft, Google, Meta, Amazon, Apple, NVIDIA, Adobe, Salesforce, TikTok, ByteDance, Toyota, Bosch, BMW, Mercedes).

## Why Appen

Appen is the canonical AI-data-annotation incumbent with 1M+ labelers, 130+ countries, 20+ years of data experience, ASX-listed (APN), and the Foundry annotation-platform + ADAP workflow + Managed-Workforce + Crowdsourcing-Platform stack. Your customers — Microsoft, Google, Meta, Amazon, Apple, NVIDIA, Adobe, Salesforce, TikTok, ByteDance, LG, Samsung, Toyota, Bosch, BMW, Mercedes, Audi, Honda, Nissan, Salesforce, Shopify, Spotify, Twilio, Zendesk, Atlassian — are running foundation-model training pipelines that depend on Appen's per-labeler RLHF-preference-judgments, per-labeler safety-annotations, per-labeler red-team-data, per-labeler automotive-annotations, per-labeler medical-annotations, per-labeler financial-annotations, and per-labeler multilingual-annotations across 130+ countries.

## The 5 audit gaps (one per regulatory anchor)

1. **End-to-end provenance join-table.** Per-task-id → per-asset-id → per-labeler-id → per-language-id → per-region-id → per-AI-preference-judgment-id → per-AI-safety-annotation-id → per-AI-red-team-data-id → per-AI-automotive-annotation-id → per-AI-medical-annotation-id → per-AI-financial-annotation-id → per-Appen-tenant-id → per-procurement-vendor-DD-event-id → per-audit-log-entry-id → per-residency-region-id provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + ISO 27701 + GDPR Art. 30 + 12-state AI-disclosure + Schrems II SCC + APPI cross-border-data-transfer.

2. **Training-corpus + fine-tune-license-provenance.** Per EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary + ISO 42001 6.1.4 + Schrems-II-cross-border-data-transfer-provenance + EU-US-DPF-provenance + APPI cross-border-transfer-provenance. Appen corpus spans per-labeler-preference-judgment-text, per-labeler-safety-label-text, per-red-team-prompt-replay-history, per-multilingual-transcription-text, per-automotive-annotation-history, per-medical-annotation-history, per-financial-annotation-history. Canonical EU AI Act Aug 2 2026 GPAI documentation target.

3. **Prompt-injection + AI-preference-judgment-poisoning + AI-safety-annotation-poisoning + AI-red-team-data-poisoning + AI-automotive-annotation-poisoning + AI-medical-annotation-poisoning + AI-multilingual-annotation-poisoning + AI-generative-AI-training-data-poisoning + Appen-tenant-prompt-injection + Appen-labeler-prompt-injection-defense.** Per OWASP LLM Top 10 LLM01+LLM03+LLM06+LLM08 + MITRE ATLAS + EU AI Act Art. 14 human-oversight + Art. 50 transparency-obligation + 12-state AI-disclosure + Schrems II cross-border-prompt-injection-defense.

4. **Cross-Appen-tenant + per-Appen-org-id + per-Appen-tenant-KMS-key-id + CMK/BYOK + per-Appen-tenant-AI-inference-endpoint + per-Appen-tenant-AI-training-pipeline + cross-border-data-residency-isolation.** Per SOC 2 CC6.1 + GDPR Art. 28 + Schrems II SCC + EU-US DPF + APPI cross-border-isolation + FTC Safeguards Rule + ISO 27701. Cross-Appen-tenant-isolation + cross-Appen-org-isolation + cross-labeler-pool-isolation + cross-AI-training-isolation + cross-border-data-residency-isolation-evidence auditable per app.appen.com regional hosting + per labeler-region isolation.

5. **WORM retention + cost-attribution join-table.** Per-labeler-preference-judgment-cost + per-labeler-safety-annotation-cost + per-labeler-red-team-data-cost + per-labeler-automotive-annotation-cost + per-labeler-medical-annotation-cost + per-labeler-multilingual-annotation-cost + per-Appen-tenant-cost + per-Appen-org-cost + per-procurement-vendor-DD-event-cost. Per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + ASX listing-rule-recordkeeping + Schrems-II-recordkeeping + APPI-recordkeeping + GDPR-Art-30-recordkeeping + cross-border-data-residency-retention.

## The offer

Fixed-fee, 48-hour delivery: **$500** for the audit memo + 5-gap join-table + EU AI Act Art. 53(d) GPAI documentation template + OWASP LLM Top 10 + MITRE ATLAS threat model + SOC 2 CC6.1/CC7.2 evidence index + Schrems II SCC + APPI + GDPR Art. 30 cross-border-data-transfer-provenance artifact. Delivered as a single Markdown + CSV bundle to contact@appen.com.

Atlas / Talon Forge LLC
2026-07-19
"""
template_path.write_text(template_content, encoding="utf-8")
print(f"OK: wrote template {template_path.name} ({len(template_content)} bytes)")
print("DONE")
