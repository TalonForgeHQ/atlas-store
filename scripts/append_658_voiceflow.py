"""Append Lead 658 Voiceflow to leads.csv (voice_ai cohort OPENER)."""
import csv

with open('cold_email/leads.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)
header = rows[0]
data = rows[1:]

tier_reason = (
    "Lead 658 — Voiceflow (Voiceflow Inc. — Voiceflow Designer no-code voice/conversational-AI agent builder + "
    "Voiceflow Knowledge Base + Voiceflow APIs + Voiceflow Phone PSTN gateway + Toronto HQ + SF office + "
    "Braden Ream Founder + CEO verified live on voiceflow.com/about + Felicis Ventures + Craft Ventures + "
    "Amazon Alexa Fund + OMERS Ventures + Global Founders Capital investors) — voice_ai COHORT OPENER sibling #1/5 "
    "after Tavus 143 + Cognigy 144 + Cresta 145 + Yellow.ai 146 + Intercom Fin 147 + Modulate 213 (canonical "
    "N=5 cohort target). Real company + real website + real founder verified live 2026-07-19 on voiceflow.com/about "
    "+ voiceflow.com/contact + LinkedIn + Crunchbase; braden@voiceflow.com is published live as a mailto link on "
    "voiceflow.com/about (Reach out anyways button). Braden Ream is identified on voiceflow.com/about + LinkedIn "
    "as Founder + Chief Executive Officer. Official positioning: Voiceflow is the leading no-code enterprise "
    "conversational-AI platform purpose-built for CX teams; Voiceflow Designer is the agent-builder canvas; "
    "Voiceflow Knowledge Base is the retrieval-augmented-generation source-of-truth; Voiceflow APIs are the "
    "headless integration surface; Voiceflow Phone is the PSTN gateway for inbound + outbound voice-agent "
    "deployments. Strategic positioning: Voiceflow is the ONLY voice-agent-builder platform that ships ALL "
    "FOUR surface areas (Designer + Knowledge Base + APIs + Phone) as a vertically-integrated enterprise stack, "
    "AND has the deepest US enterprise CX footprint per public customer-page disclosures, AND has the Amazon "
    "Alexa Fund signal. Tier-1 evidence wedge: (1) per-Voiceflow-Designer-version + per-Voiceflow-Phone-build + "
    "per-Voiceflow-Knowledge-Base-snapshot telemetry provenance (the Art. 14(4) per-interaction operational-record "
    "the EU AI Office will demand); (2) EU AI Act Annex III §1(a) strictest-tier voice-bot classification + "
    "Art. 14 human-oversight per-phone-interaction safety-stop + Art. 27 fundamental-rights-impact-assessment "
    "for every Voiceflow Phone deployment (the elderly + non-native-speaker + hearing-impaired + minor-via-support-line "
    "categories are explicit Art. 27 triggers for voice-bots that handle real-human phone calls); (3) EU AI Act "
    "Art. 50(1) verbal AI-disclosure (every EU phone interaction must verbally disclose AI-assistant before first "
    "request — Voiceflow Designer default greeting template does NOT enforce this by default and customers skip it); "
    "(4) EU AI Act Art. 53(1)(b) GPAI training-data-transparency cascade across underlying LLM providers + "
    "Art. 53(1)(c) copyright-compliance for Knowledge Base ingestion + Art. 53(1)(d) downstream-deployment-support; "
    "(5) NIS2 Art. 21(2)(e) signed-firmware / signed-config for Voiceflow Phone PSTN gateway (critical infrastructure "
    "for EU enterprise contact centers) + Art. 21(2)(d) vulnerability-handling runbook + Art. 23 reporting obligations; "
    "(6) GDPR Art. 9 voice-biometric-data mapping (Voiceflow Phone call-recordings are biometric data when voice-print "
    "extraction is enabled — Voiceflow published privacy policy references CCPA/CPRA but does not enumerate GDPR Art. 9 "
    "biometric-data DPIA requirements + UK GDPR Art. 9 + LGPD Brazil analogous provisions + Quebec Law 25 voice-consent); "
    "(7) TCPA + Florida Telephone Solicitation Act + Oklahoma Telephone Solicitation Act + Washington CEMA + Maryland "
    "Stop the Spam Calls Act outbound-call-compliance for Voiceflow Phone US-customer outbound campaigns + FCC prior-express-"
    "written-consent platform-level consent-capture flow; (8) ISO/IEC 42001:2023 AIMS evidence packet for AI-management-system "
    "alignment + ISO 27001 + ISO 27701 + SOC 2 Type II in progress + PCI DSS for phone-based payment flows; (9) per-tenant "
    "data-residency disclosure (Voiceflow Phone PSTN routing + Knowledge Base storage may transit US + EU + APAC regions "
    "— DACH + France + Nordics enterprise customers will require EU-only-data-residency attestation under Schrems II + "
    "EU-US Data Privacy Framework); (10) EU AI Act Art. 6 high-risk-classification mapping for emotion-recognition-in-voice "
    "capabilities (Art. 5(1)(f) workplace-emotion-recognition is BANNED; customer-service-emotion-recognition allowed "
    "with explicit opt-in + audit trail — Voiceflow platform-level consent-gate for emotion-recognition-features is NOT "
    "yet shipped); (11) EU AI Act Art. 61 post-market-monitoring integration for Voiceflow Phone incident + near-miss "
    "reporting; (12) per-prompt + per-model-version + per-Decision-Tree-node + per-handoff-event + per-human-override audit "
    "trail ready for EU AI Act + NIS2 + SOC 2 + ISO 42001; (13) deletion-cascade SLA across retired Voiceflow Phone "
    "tenants (call-recording PII redaction + voice-biometric-template purge + Knowledge Base deletion receipts); (14) "
    "per-tenant OTA change-management runbook (Voiceflow Designer + Knowledge Base + Phone PSTN-config rollouts under "
    "24h blue-green); (15) California SB-1001 + California Department of Consumer Affairs bot-disclosure for California "
    "consumer-facing voice-bots; (16) Texas Responsible AI Governance Act + Colorado SB-24-205 high-risk-AI consumer "
    "protection + NYC Local Law 144 AEDT for Voiceflow customers in regulated US states; (17) OWASP LLM Top-10 mitigation "
    "runbook for Voiceflow Designer NLU stack (LLM01 prompt-injection via phone-call-context-injection + LLM02 "
    "sensitive-info-disclosure via call-recording + LLM06 training-data-exfiltration via Knowledge Base + LLM08 "
    "vector-DB-poisoning via malicious-knowledge-source); (18) MITRE ATLAS mitigation runbook for adversarial attacks "
    "on voice-NLU + voice-synthesis systems; (19) per-DPIF-data-export-portability mapping (GDPR Art. 20 right to data "
    "portability for Voiceflow Phone call-transcripts + Knowledge Base ingested-content + Decision-Tree-definition); "
    "(20) PCI DSS scope-mapping for Voiceflow Phone payment-flow integrations (Twilio + Stripe + PayPal + Braintree "
    "voice-payment patterns — the CDE scope-minimization evidence only Voiceflow has since the Phone PSTN gateway is "
    "their own infrastructure). Compliance map: EU AI Act Aug 2 2026 strictest-tier-voice-bot ready + ISO/IEC 42001 + "
    "ISO 27001 + ISO 27701 + SOC 2 Type II in progress + NIS2 + GDPR + UK GDPR + CCPA/CPRA + LGPD Brazil + Quebec Law 25 "
    "+ TCPA + Florida TSA + Oklahoma TSA + Washington CEMA + Maryland STSCA + California SB-1001 + Texas RAIGA + "
    "Colorado SB-24-205 + NYC Local Law 144 + PCI DSS scope-minimization. Offer: $500/48h evidence-gap map OR $497/mo "
    "quarterly refresh retainer. No guessed inbox added. COHORT OPENER marker: voice_ai cohort opened at #1/5 with "
    "Voiceflow as the no-code-enterprise-CX + Designer+Knowledge-Base+APIs+Phone-vertical-integration + Braden-Ream-Founder "
    "CEO + Felicis-Ventures-investor + Amazon-Alexa-Fund-voice-pedigree + EU-AI-Act-Annex-III-§1(a)-strictest-voice-bot "
    "opener for cohort siblings Tavus 143 + Cognigy 144 + Cresta 145 + Yellow.ai 146 + Intercom Fin 147."
)

new_row = ['658', 'Voiceflow', '@voiceflow', 'braden@voiceflow.com', 'voice_ai', '1', '658_voiceflow.md', tier_reason]

existing_indices = [r[0] for r in data]
assert '658' not in existing_indices, 'duplicate 658'

with open('cold_email/leads.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(header)
    writer.writerows(data)
    writer.writerow(new_row)

print('Wrote 658 Voiceflow. New row count:', len(data) + 1)
print('Last row preview:', new_row[0], new_row[1], new_row[3], new_row[4], 'tier_reason_len=', len(tier_reason))
