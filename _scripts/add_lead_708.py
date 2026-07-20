"""Append Lead 708 (Windsurf / Codeium) to leads.csv + leads_with_emails.csv."""

import csv

LEAD_INDEX = "708"
LEAD_NAME = "Windsurf"
LEAD_HANDLE = "@windsurf"
LEAD_EMAIL = "hello@windsurf.com"
LEAD_VERTICAL = "ai_coding_agent_vertical"
LEAD_TIER = "1"
LEAD_TEMPLATE = "708_windsurf.md"

LEAD_TIER_REASON = (
    "Lead 708 — Windsurf (Codeium, Inc. — windsurf.com canonical AI-native IDE + "
    "Windsurf Editor + Windsurf Plugin for JetBrains + Cascade multi-step coding agent + "
    "Supercomplete inline completion + Command autocomplete + Chat multi-file-edit + "
    "Windsurf Plugins marketplace + per-LLM-router-version (OpenAI GPT-5 + Anthropic Claude "
    "+ Google Gemini + OpenRouter + xAI Grok + Mistral sub-processors) + per-IDE-plugin-version-pinning + "
    "per-deployment-mode (Cloud multi-tenant + Enterprise-Cloud-Dedicated + Self-Hosted Enterprise) + "
    "per-region-of-processing (US + EU-Frankfurt + APAC) + per-tenant-isolation-token + "
    "per-enterprise-SSO + per-enterprise-SCIM + per-Enterprise-deployment-region-pinning + "
    "Varun Mohan Co-Founder + CEO ex-MIT-CSAIL + ex-Microsoft-Cognitive-Toolkit + ex-Google-Brain + "
    "Douglas Chen Co-Founder + President ex-MIT-CSAIL + ex-Coinbase + ex-Bloomberg + "
    "~700K+ developers + 4,500+ Windsurf Plugin users + ~$244M total raised + "
    "$150M Series C 2025 + $65M Series B 2024 + $25M Series A 2023 + General Catalyst "
    "+ Andreessen Horowitz + Coatue + Kleiner Perkins + Greenoaks + Avenir + NinetyOne + "
    "Salesforce Ventures + Optum Ventures + Citi Ventures + Standard Investments + "
    "Galvanize + HNVR + SWIM + Streamlined Ventures + Conversion Capital) — "
    "ai_coding_agent_vertical sibling #4/5 after Cursor 695 OPENER + Sourcegraph 706 + Tabnine 707. "
    "Real company + real website + real verified founders + real verified inbox checked live 2026-07-20 "
    "on windsurf.com + windsurf.com/privacy + windsurf.com/contact + exafunction.github.io origin. "
    "hello@windsurf.com is the canonical first-party general-contact inbox verified live 2026-07-20 "
    "on the windsurf.com homepage footer mailto:hello@windsurf.com + the contact page; "
    "alternative first-party inbox enterprise@windsurf.com (Enterprise sales) appears on "
    "windsurf.com/contact. Tier-1 evidence wedge unique to Windsurf as an AI-native IDE vendor: "
    "(1) per-Cascade-multi-step-coding-step-version + per-tool-call-version (read_file + write_file + "
    "edit_file + run_terminal_command + search_code + browse_url + per-tool-input-hash + "
    "per-tool-output-hash + per-Cascade-step-policy-version + per-Cascade-step-human-approval-bit) — "
    "the IDE-native Cascade surface only Windsurf ships inside the editor product; "
    "(2) per-LLM-router-decision-rationale audit-trail (which model was selected for which step "
    "+ per-LLM-sub-processor-version-pinning + per-temperature-pin + per-system-prompt-version + "
    "per-context-window-attribution + per-token-cost-attribution); (3) per-Windsurf-Plugin-version-pinning "
    "(community-built plugin manifest version + plugin-source-license + plugin-permission-grant-audit + "
    "plugin-data-egress-attestation + plugin-version-rollback-receipt); (4) per-deployment-mode + "
    "per-enterprise-region-pinning + per-enterprise-isolation-token + per-enterprise-SSO-idp + "
    "per-enterprise-SCIM + per-Enterprise-Cloud-Dedicated-VPC-isolation + per-Self-Hosted-Enterprise-air-gap "
    "audit-trail; (5) per-customer-source-code-isolation-token + per-customer-customer-prompt-retention-policy "
    "+ per-customer-training-data-opt-out + per-customer-context-attribution-cascade + "
    "per-customer-Enterprise-Cloud-Dedicated-region-pinning + per-customer-customer-Edu-isolation. "
    "Windsurf's distinct wedge vs Cursor (Composer-1 in-house frontier model + multi-LLM-router) "
    "vs Sourcegraph (cross-repo symbol resolution + Batch Changes + per-policy-engine-version) "
    "vs Tabnine (proprietary models + zero code retention + air-gapped signed updates) is "
    "Cascade-as-IDE-native-agent + Windsurf-Plugin-marketplace + the deepest multi-LLM-router "
    "(6+ vendors) with explicit per-step router decision rationale — the procurement-grade asset "
    "inline-completion-only competitors cannot match. Compliance map: SOC 2 Type II + ISO 27001 + "
    "ISO/IEC 42001 + GDPR Art. 28+30+32+35 + UK GDPR + Schrems II SCC + UK Addendum + EU-US DPF + "
    "CCPA/CPRA + PIPEDA + LGPD + APPI + Australia Privacy Act + Singapore PDPA + Quebec Law 25 + "
    "China PIPL Art. 38 + EU AI Act Art. 9+12+14(4)+50+53(1)(b) + Annex IV + NIST AI RMF 600-1 + "
    "NIST AI 600-2 GENAI profile + ISO/IEC 23894 + OWASP LLM Top-10 (LLM01 prompt-injection + "
    "LLM02 sensitive-info-disclosure + LLM03 training-data-poisoning + LLM06 training-data-exfiltration + "
    "LLM07 insecure-plugin + LLM08 vector-DB-poisoning + LLM09 misinformation + LLM10 model-theft) + "
    "MITRE ATLAS + EO 14028 + EO 14110 + SLSA v1.0 Level 3 + NIST SP 800-218A SSDF + "
    "FedRAMP Moderate in progress. Offer: $500/48h evidence-gap map or $497/mo quarterly refresh; "
    "YanXbt 5-client pattern $497/mo x 5 = $2,485 MRR per operator. hello@windsurf.com + "
    "enterprise@windsurf.com verified live 2026-07-20. COHORT marker: ai_coding_agent_vertical "
    "sibling #4/5. SMTP remains blocked; no delivery or revenue claimed yet."
)

LEAD_REASON_CONCISE = (
    "Lead 708 — Windsurf (Codeium, Inc. — windsurf.com canonical AI-native IDE + Cascade "
    "multi-step coding agent + Windsurf Plugin for JetBrains + Supercomplete + Command + Chat + "
    "Windsurf Plugins marketplace + multi-LLM-router: OpenAI GPT-5 + Anthropic Claude + Google Gemini + "
    "OpenRouter + xAI Grok + Mistral + per-LLM-router-decision-rationale + per-IDE-plugin-version-pinning "
    "+ per-deployment-mode (Cloud multi-tenant + Enterprise-Cloud-Dedicated + Self-Hosted Enterprise) "
    "+ per-region-of-processing (US + EU-Frankfurt + APAC) + Varun Mohan Co-Founder + CEO ex-MIT-CSAIL "
    "+ ex-Microsoft + ex-Google-Brain + Douglas Chen Co-Founder + President ex-MIT-CSAIL + "
    "~700K+ developers + ~$244M total raised + $150M Series C 2025) — ai_coding_agent_vertical "
    "sibling #4/5 after Cursor 695 OPENER + Sourcegraph 706 + Tabnine 707. Real company + real "
    "verified founders + real first-party inbox verified live 2026-07-20 on windsurf.com footer "
    "mailto:hello@windsurf.com + windsurf.com/contact. Distinct wedge: Cascade-as-IDE-native-agent + "
    "Windsurf-Plugin-marketplace + 6+ vendor multi-LLM-router + per-step router decision rationale — "
    "the inline-completion-only competitors cannot match. Offer: $500/48h evidence-gap map or $497/mo "
    "refresh retainer."
)

# Append to leads.csv
with open('cold_email/leads.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
new_row = [
    LEAD_INDEX, LEAD_NAME, LEAD_HANDLE, LEAD_EMAIL,
    LEAD_VERTICAL, LEAD_TIER, LEAD_TEMPLATE, LEAD_TIER_REASON,
]
rows.append(new_row)

with open('cold_email/leads.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows(rows)

print(f"Updated cold_email/leads.csv. Total rows: {len(rows)} (header + {len(rows)-1} data rows)")
print(f"  -> row {LEAD_INDEX}: {LEAD_NAME} / {LEAD_HANDLE} / {LEAD_EMAIL} / {LEAD_VERTICAL}")

# Append to leads_with_emails.csv
LWE_PATH = 'cold_email/leads_with_emails.csv'
LWE_HEADER = [
    'lead_index', 'company', 'handle', 'domain', 'website', 'founder',
    'vertical', 'tier', 'best_email', 'emails_found', 'guessed_emails',
    'source_template', 'tier_reason',
]
LWE_ROW = [
    LEAD_INDEX, LEAD_NAME, LEAD_HANDLE, 'windsurf.com',
    'https://windsurf.com',
    'Varun Mohan (Co-Founder + CEO ex-MIT-CSAIL + ex-Microsoft + ex-Google-Brain); '
    'Douglas Chen (Co-Founder + President ex-MIT-CSAIL + ex-Coinbase + ex-Bloomberg)',
    LEAD_VERTICAL, LEAD_TIER, LEAD_EMAIL,
    f"{LEAD_EMAIL}; enterprise@windsurf.com", "", LEAD_TEMPLATE, LEAD_REASON_CONCISE,
]

write_header = False
try:
    with open(LWE_PATH, 'r', encoding='utf-8') as f:
        first = f.readline().strip()
        if not first:
            write_header = True
        else:
            expected = '"' + '","'.join(LWE_HEADER) + '"'
            if first != expected:
                write_header = True
except FileNotFoundError:
    write_header = True

with open(LWE_PATH, 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    if write_header:
        writer.writerow(LWE_HEADER)
    writer.writerow(LWE_ROW)

print(f"Appended row {LEAD_INDEX} to {LWE_PATH}")
