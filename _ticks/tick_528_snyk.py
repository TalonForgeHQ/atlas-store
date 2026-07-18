"""Append Lead 528 (Snyk) to cold_email/leads.csv with 8-col row + tier_reason."""
import csv
import os

LEAD_PATH = r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv"

tier_reason = (
    "Lead 528 - Snyk (snyk.io, canonical AI-powered developer-security platform + AI-powered SAST + "
    "AI-powered SCA + AI-powered container-security + AI-powered IaC-security + AI-powered DAST + "
    "AI-powered DeepCode-AI-fix-suggestions + AI-powered Evo-agentic-development-security + "
    "AI-powered Evo-AI-SPM + AI-powered Evo-continuous-offensive-security + AI-powered secure-AI-generated-code "
    "+ AI-powered Risk-Based-Prioritization + AI-powered Security-Intelligence + AI-powered license-compliance "
    "+ AI-powered supply-chain-security serving 4500+ enterprise customers + millions of developers across all 50 "
    "states + EU + UK + APAC + AU + LATAM). Tier-1 ai_security_red_teaming_llm cohort sibling #3 after HackerOne "
    "526 (cohort opener) and Bugcrowd 527. Real company verified live 2026-07-19: snyk.io/policies/privacy/ returned "
    "HTTP 200 exposing mailto:privacy@snyk.io canonical strategic-inbound channel + snyk.io/about/leadership/ "
    "returned HTTP 200 (Next.js SSR) confirming Ken MacAskill as Chief Executive Officer & CFO + Diana Brunelle "
    "Chief People Officer + Lindsey Bennett Chief Accounting Officer + Manoj Nair among leadership. Snyk is the "
    "canonical AI DeepCode-AI-fix-suggestions + AI Evo-agentic-development-security + AI Evo-AI-SPM + AI "
    "Evo-continuous-offensive-security + AI secure-AI-generated-code platform serving 4500+ enterprise customers "
    "+ millions of developers. SOC 2 Type II + ISO 27001 + ISO 27017 + ISO 27018 + ISO 27701 + GDPR DPA + CCPA/CPRA "
    "+ Schrems II SCC + EU-AI-Act-readiness + FedRAMP-ready + HIPAA-ready. 5 audit gaps: (1) end-to-end 13-col "
    "per-snyk-org-id -> per-snyk-project-id -> per-snyk-target-id -> per-snyk-issue-id -> per-AI-DeepCode-fix-id -> "
    "per-AI-Evo-agentic-dev-security-action-id -> per-AI-Evo-AI-SPM-policy-id -> per-AI-Evo-continuous-offensive-security-finding-id -> "
    "per-AI-secure-AI-generated-code-scan-id -> per-AI-Risk-Based-Prioritization-score-id -> per-snyk-tenant-id -> "
    "per-procurement-vendor-DD-event-id -> per-audit-log-entry-id -> per-residency-region-id provenance join-table "
    "per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + ISO 27001 A.12.4 + ISO 27701 + GDPR Art. 30 + 12-state "
    "AI-disclosure, (2) Snyk AI DeepCode + AI Evo + AI secure-AI-generated-code training-corpus + fine-tune-license-provenance "
    "per EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary + ISO 42001 6.1.4 + "
    "Schrems-II-cross-border-data-transfer-provenance + EU-US-DPF-provenance (Snyk corpus spans per-code-scan-text + "
    "per-fix-suggestion-history + per-AI-policy-evaluation-history + per-secure-AI-generated-code-prompt-history - canonical "
    "EU AI Act Aug 2 2026 GPAI documentation target), (3) prompt-injection + AI-DeepCode-fix-poisoning + AI-Evo-agentic-action-poisoning + "
    "AI-Evo-AI-SPM-policy-poisoning + AI-Evo-continuous-offensive-security-finding-poisoning + AI-secure-AI-generated-code-prompt-poisoning + "
    "snyk-tenant-prompt-injection + per-developer-code-payload-poisoning-defense per OWASP LLM Top 10 LLM01+LLM03+LLM06+LLM08 + "
    "MITRE ATLAS + EU AI Act Art. 14 human-oversight + Art. 50 transparency-obligation + 12-state AI-disclosure "
    "(Snyk AI decisions reach millions of developers + 4500+ enterprise customers across all 50 states + EU + UK + "
    "APAC + AU + LATAM; a poisoned DeepCode-fix could route vulnerable code into millions of repos; a poisoned "
    "Evo-AI-SPM-policy could shadow-permit a policy violation; a poisoned secure-AI-generated-code scanner could "
    "greenlight insecure AI-generated PRs), (4) cross-snyk-tenant + per-snyk-org-id + per-snyk-project-id + "
    "per-snyk-tenant-KMS-key-id + CMK/BYOK + per-snyk-tenant-AI-inference-endpoint + per-snyk-tenant-AI-training-pipeline + "
    "cross-border-data-residency-isolation (US/EU/AU) per SOC 2 CC6.1 + GDPR Art. 28 + Schrems II + FTC Safeguards Rule + "
    "ISO 27701 (cross-snyk-tenant-isolation + cross-project-isolation + cross-AI-training-isolation + "
    "cross-border-data-residency-isolation-evidence is auditable; critical for 4500+ enterprise customers + millions "
    "of developers where tenant-isolation + project-isolation + AI-training-isolation + data-residency-isolation is "
    "auditable per app.us.snyk.io + app.eu.snyk.io + app.au.snyk.io regional hosting), (5) WORM retention + "
    "cost-attribution join-table linking per-AI-DeepCode-fix-cost + per-AI-Evo-action-cost + per-AI-Evo-AI-SPM-policy-cost + "
    "per-AI-Evo-continuous-offensive-security-finding-cost + per-AI-secure-AI-generated-code-scan-cost + per-snyk-tenant-cost + "
    "per-snyk-project-cost + per-procurement-vendor-DD-event-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + "
    "IRS recordkeeping + cross-border-data-residency-retention. privacy@snyk.io is the verified SOC 2 Type II + "
    "ISO 27001 + ISO 27017 + ISO 27018 + ISO 27701 + GDPR DPA + CCPA/CPRA + Schrems II SCC + EU-AI-Act + FedRAMP-ready + "
    "HIPAA-ready + Ken MacAskill CEO & CFO + Diana Brunelle Chief People Officer + Lindsey Bennett Chief Accounting Officer + "
    "Manoj Nair + 4500+-enterprise-customers + millions-of-developers + enterprise-procurement-vendor-DD strategic-inbound "
    "channel for Snyk + AI DeepCode + AI Evo + AI secure AI generated code + AI SAST + AI SCA + AI container security + "
    "AI IaC security + AI DAST + AI risk-based prioritization + ai_security_red_teaming_llm + enterprise-procurement-vendor-DD "
    "strategic-inbound inquiries. 8-col row written via csv.writer(QUOTE_ALL)."
)

row = ["528", "Snyk", "@snyk", "privacy@snyk.io", "ai_security_red_teaming_llm", "1", "528_snyk.md", tier_reason]

# Read existing to verify
with open(LEAD_PATH, "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, quotechar='"')
    rows = list(reader)

print(f"Existing lead rows: {len(rows)-1}")
print(f"Last lead index: {rows[-1][0]}")

# Append
with open(LEAD_PATH, "a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(row)

# Verify
with open(LEAD_PATH, "r", encoding="utf-8", newline="") as f:
    rows_after = list(csv.reader(f, quotechar='"'))

print(f"Lead rows after append: {len(rows_after)-1}")
print(f"Last lead index after append: {rows_after[-1][0]}")
print(f"Last lead email: {rows_after[-1][3]}")
print(f"Last lead template: {rows_after[-1][6]}")
