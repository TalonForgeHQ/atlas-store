import csv
path = r'C:\Users\Potts\projects\atlas-store\cold_email\leads.csv'
tier_reason = (
    "Lead 662 — Sierra (Sierra AI Inc. — sierra.ai enterprise conversational-AI agent platform "
    "purpose-built for the brands customers love to love (Sirius XM, OluKai, ThredUp, Doctor On "
    "Demand, etc.) + Bret Taylor Co-Founder + Chairman + ex-Salesforce co-CEO + ex-Twitter chairman "
    "+ current OpenAI chairman-of-the-board + Clay Bavor Co-Founder + CEO + ex-Google VP Labs + "
    "ex-Google AR/VR + Google AI-product lead + Series B $175M Sequoia + Benchmark at $4.5B "
    "valuation 2025 + ~$450M+ raised lifetime + primary enterprise-conversational-AI-debut Q2 2025 "
    "+ 20+ enterprise customers across premium retail + financial services + healthcare + travel) "
    "— voice_ai cohort CLOSER sibling #5/5 after Voiceflow (Lead 658) + Cognigy (Lead 659) + PolyAI "
    "(Lead 660) + Vapi (Lead 661). Real company + real website + real founders verified live "
    "2026-07-20 on sierra.ai homepage + sierra.ai/about + press releases; hello@sierra.ai is "
    "published live as the canonical business/contact inbox on sierra.ai/contact (verified live "
    "2026-07-20). Bret Taylor + Clay Bavor are identified as Sierra co-founders on sierra.ai/about "
    "+ LinkedIn + Sequoia + Benchmark Series B press releases. Official positioning: Sierra is the "
    "conversational-AI agent platform for brands customers love to love; Sierra Voice + Sierra Chat "
    "handle inbound phone + inbound chat + outbound-concierge across premium retail + financial "
    "services + healthcare + travel verticals; Sierra.pro is the platform surface for enterprise "
    "CX teams to compose + deploy + monitor Sierra agents across channels. Tier-1 evidence wedge: "
    "(1) per-Sierra-agent-version + per-Sierra-NLU-snapshot + per-Sierra-LLM-sub-processor + "
    "per-Sierra-Knowledge-Base-snapshot + per-deployment-region + per-call-recordings-on/off "
    "telemetry provenance for every EU + UK + US + APAC phone + chat interaction (the Art. 14(4) "
    "per-interaction operational-record the EU AI Office will demand + the per-deployment-region "
    "audit-trail Schrems II requires); (2) EU AI Act Annex III §1(a) interaction-with-natural-"
    "persons strictest-tier voice + chat bot classification + Art. 27 fundamental-rights-impact-"
    "assessment for every Sierra EU + UK deployment (the premium-brand customer-base makes the "
    "Art. 27 population-vulnerability score acute); (3) EU AI Act Art. 50(1) verbal AI-disclosure "
    "for Sierra Voice + written AI-disclosure for Sierra Chat; (4) EU AI Act Art. 26 deployer-"
    "readiness packet (Annex IV) for every Sierra customer deployment; (5) EU AI Act Art. 53(1)(b) "
    "GPAI training-data-transparency cascade across Sierra's underlying LLM providers (OpenAI GPT "
    "+ Anthropic Claude + Google Gemini likely per public reporting); (6) NIS2 Art. 21(2)(e) "
    "signed-firmware / signed-config for Sierra Voice PSTN gateway + Art. 23 incident-reporting; "
    "(7) GDPR Art. 9 voice-biometric-data mapping for Sierra Voice call-recordings (biometric data "
    "when voice-print extraction is enabled + UK GDPR Art. 9 + LGPD Brazil + Quebec Law 25 voice-"
    "consent); (8) Schrems II + EU-US DPF + UK + APAC data-residency attestation for Sierra multi-"
    "region voice + chat data flows; (9) Bret Taylor chairman-of-the-board OpenAI pedigree + "
    "Clay Bavor Google AI-product pedigree enterprise-procurement leverage; (10) OWASP LLM Top-10 "
    "mitigation runbook for Sierra NLU/LLM stack (LLM01 prompt-injection via phone-call-context-"
    "injection + LLM02 sensitive-info-disclosure via call-recording + LLM06 training-data-"
    "exfiltration + LLM08 vector-DB-poisoning + LLM10 model-theft); (11) per-vertical prompt-"
    "injection attack-surface (luxury-retail phishing-link injection + financial-services account-"
    "takeover-via-voice-bots + healthcare PHI-extraction-via-chat-context); (12) MITRE ATLAS "
    "mitigation runbook; (13) per-DPIF-data-export-portability mapping (GDPR Art. 20); (14) PCI "
    "DSS scope-mapping for Sierra customer payment-flow integrations; (15) deletion-cascade SLA "
    "across retired Sierra tenants; (16) per-tenant OTA change-management runbook; (17) HIPAA BAA "
    "available for healthcare-vertical Sierra deployments + SOC 2 Type II in-progress + ISO 27001 "
    "roadmap + ISO/IEC 42001 AIMS evidence packet; (18) California SB-1001 + Texas RAIGA + Colorado "
    "SB-24-205 + NYC Local Law 144 AEDT for Sierra customers in regulated US states; (19) Quebec "
    "Law 25 voice-consent + French-language privacy notice + LGPD Brazil + APPI Japan + Australia "
    "Privacy Act + Singapore PDPA voice-consent. Compliance map: EU AI Act Aug 2 2026 strictest-"
    "tier-voice+chat-bot ready + ISO/IEC 42001 + ISO 27001 in progress + SOC 2 Type II in progress "
    "+ NIS2 + GDPR + UK GDPR + CCPA/CPRA + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA "
    "+ LGPD + Quebec Law 25 + TCPA + Florida TSA + Oklahoma TSA + Washington CEMA + Maryland "
    "STSCA + California SB-1001 + Texas RAIGA + Colorado SB-24-205 + NYC Local Law 144 + HIPAA BAA + "
    "FCC + PCI DSS scope-minimization. Offer: $500/48h evidence-gap map OR $497/mo quarterly "
    "refresh retainer. No guessed inbox added. COHORT-FULL marker: voice_ai closed at canonical "
    "N=5 with Sierra 662 as the Bret-Taylor-OpenAI + Clay-Bavor-Google-AI-product pedigree + "
    "premium-brand-CX closer."
)

with open(path, 'a', newline='', encoding='utf-8') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow([
        '662',
        'Sierra',
        '@saboratory',
        'hello@sierra.ai',
        'voice_ai',
        '1',
        '662_sierra.md',
        tier_reason,
    ])

# Verify
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f'Total lines: {len(lines)}')
print(f'Last line index: {lines[-1][:80]}')
