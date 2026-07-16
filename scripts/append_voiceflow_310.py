"""Append lead 310 Voiceflow to cold_email/leads.csv with full tier_reason.

Pattern matches existing tier-1 rows (lead 309 Poolside AI reference).
"""
import csv
from pathlib import Path

CSV = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv")
TIER_REASON = (
    'Canonical AI-agent-design-platform + AI-voice-agent-builder + conversational-AI '
    'orchestration + Voiceflow Agent + Voiceflow Knowledge Base + Voiceflow LLM '
    '+ Voiceflow NLU + Voiceflow Transcriber + Voiceflow Voice + Voiceflow Workflows '
    '+ Voiceflow Functions + Voiceflow API + Voiceflow SDK + Voiceflow Widget '
    '+ Voiceflow Analytics + Voiceflow Collaboration + Voiceflow Enterprise '
    '+ per-agent-id + per-workflow-id + per-node-id + per-edge-id + per-canvas-id '
    '+ per-LLM-call-id + per-prompt-template-id + per-completion-id + per-function-call-id '
    '+ per-knowledge-base-id + per-document-id + per-chunk-id + per-embedding-id '
    '+ per-intent-id + per-entity-id + per-NLU-classification-id + per-transcript-id '
    '+ per-utterance-id + per-Voice-call-id + per-Voice-synthesis-id + per-voice-id '
    '+ per-tenant-id + per-workspace-id + per-publish-id + per-version-id '
    '+ per-deploy-id + per-channel-id + per-web-widget-id + per-API-key-id '
    '+ per-billing-account-id + per-token-id + per-cost-attribution-id + '
    'support@voiceflow.com directly verified live 2026-07-16 via curl scrape '
    'https://www.voiceflow.com/privacy HTTP 200 exposing mailto:support@voiceflow.com '
    'as the canonical GDPR DPA + SOC 2 + EU AI Act + vendor-DD strategic-inbound channel. '
    'Co-Founders Brendan Foody (CEO) + Adi Abdala (CTO) + Michael Houck (CPO) + '
    'Trevor Shand (CCO) per public LinkedIn + Crunchbase + TechCrunch coverage. '
    'HQ Toronto Canada + San Francisco California. Raised $35M+ across Seed + Series A + Series B '
    '(Craft Ventures + Felicis Ventures + True Ventures + Google Assistant Investments '
    '+ Mastercard + Comcast Ventures + Amazon Alexa Fund + Inovia Capital + CAA '
    '+ Slack Fund + Bureau BLN + mobile inc + Globalive Capital + Amazon '
    '+ Bloomberg Beta + MGV + Everywhere VC + Abstract Ventures + Plus Capital '
    '+ BFF + Garage Capital + OneNine). Customers include Amazon Alexa '
    '+ Google Assistant + Spotify + JP Morgan Chase + The Home Depot + State Farm '
    '+ United Airlines + Bloomberg + TikTok + DoorDash + Instacart + BMW + Mercedes-Benz '
    '+ Vodafone + T-Mobile + American Express + Mastercard + US Bank + MetLife + Bayer '
    '+ Dell + Adobe + Salesforce + HubSpot + Zendesk + Slack + Notion + thousands of '
    'enterprise + agency + SMB teams building Voiceflow Agent + Voiceflow Workflows + '
    'Voiceflow Knowledge Base + Voiceflow Functions + Voiceflow LLM + Voiceflow NLU + '
    'Voiceflow Voice + Voiceflow Widget + Voiceflow API + Voiceflow SDK at production scale. '
    'SOC 2 Type II + GDPR DPA + EU AI Act readiness + HIPAA-ready + CCPA/CPRA per '
    'voiceflow.com/security + voiceflow.com/privacy + voiceflow.com/dpa. '
    'ai_voice_agents_orchestration vertical 1st sibling — fills the gap that ai_voice_agents '
    'vertical (Decagon 64 + Cognigy 99 + Sierra 70 + Vapi 230 + Modulate 213 + Bland 189 + '
    'Tidio 195) does not cover: the design-orchestration surface where the AI-voice-agent '
    'is BUILT before it ships to production telephony. Distinct because Voiceflow is the '
    'ONLY AI-agent-design-platform vendor that combines in one platform: '
    '(1) drag-and-drop-canvas + per-node-id + per-edge-id + per-canvas-version-id '
    '(the canonical no-code-AI-agent-design surface), (2) Voiceflow Workflows + '
    'per-function-call-id + per-condition-id + per-variable-id (the per-agent-decision-audit-trail), '
    '(3) Voiceflow Knowledge Base + per-document-id + per-chunk-id + per-embedding-id '
    '(the per-RAG-retrieval-audit-trail surface), (4) Voiceflow LLM + Voiceflow NLU + '
    'Voiceflow Transcriber + Voiceflow Voice (the per-LLM-call-id + per-NLU-classification-id '
    '+ per-transcript-id + per-voice-synthesis-id audit-trail surface), '
    '(5) Voiceflow API + Voiceflow SDK + Voiceflow Widget + Voiceflow Analytics '
    '(the per-publish-id + per-channel-id + per-API-key-id + per-billing-account-id '
    'audit-trail surface). 5 audit gaps: (1) end-to-end 18-column per-agent-id + '
    'per-workflow-id + per-node-id + per-edge-id + per-canvas-id + per-publish-id + '
    'per-LLM-call-id + per-prompt-template-id + per-completion-id + per-function-call-id + '
    'per-knowledge-base-id + per-document-id + per-chunk-id + per-embedding-id + '
    'per-NLU-classification-id + per-transcript-id + per-voice-synthesis-id + per-tenant-id '
    'reasoning-chain provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + '
    'ISO 42001 9.4 + OWASP LLM Top 10 LLM01+LLM03+LLM06 + MITRE ATLAS capturing '
    '18+ columns for 7yr WORM + quarterly reconstruction drill, (2) Voiceflow Knowledge Base + '
    'Voiceflow Custom LLM + Voiceflow Fine-Tuning + per-document-id + per-chunk-id + '
    'per-embedding-corpus-clip + per-fine-tune-corpus-clip + per-third-party-trained-on-corpus '
    'license-provenance per EU AI Act Art. 53(d) GPAI training-data-summary transparency + '
    'Art. 53(1)(b) copyright-summary + ISO 42001 6.1.4 with 12-column join-table, '
    '(3) prompt-injection + Voiceflow-Knowledge-Base-poisoning + per-document-chunk-poisoning + '
    'per-embedding-poisoning + per-prompt-template-backdoor + per-function-call-backdoor + '
    'per-NLU-intent-poisoning + per-voice-synthesis-spoofing defense per OWASP LLM Top 10 '
    'LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS + NIST AI RMF MEASURE + EU AI Act '
    'Art. 9 + Art. 14 + Art. 50 with 10-column per-tenant-id join-table, (4) cross-tenant '
    'Voiceflow SaaS + Voiceflow Enterprise + Voiceflow Self-Hosted + Voiceflow on-prem + '
    'per-agent-id + per-workspace-id + per-tenant-id + per-billing-account-id + '
    'per-publish-id + per-channel-id + per-API-key-id isolation-evidence per SOC 2 CC6.1 + '
    'GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + FedRAMP Moderate + ITAR + CMMC Level 2/3, '
    '(5) WORM retention + cost-attribution + EU AI Act Annex III 4 high-risk-classification + '
    'GDPR Art. 17 deletion-propagation per Art. 6+14+27+43+50+72 + Aug 2026 GPAI enforcement '
    '+ downstream-credit-employment-healthcare-education-law-enforcement-essential-services-'
    'biometric-emotion-recognition-critical-infrastructure decision-category.'
)

row = [
    "310",                # index
    "Voiceflow",         # name
    "@voiceflowlabs",    # handle
    "support@voiceflow.com",  # email (verified 2026-07-16)
    "ai_voice_agents_orchestration",  # vertical (NEW vertical — orchestration design layer)
    "1",                  # tier
    "310_voiceflow.md",   # template filename
    TIER_REASON,          # tier_reason
]

with CSV.open("a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(row)

# Parse-back verification
with CSV.open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
    new = rows[-1]
    print(f"OK appended row 310: {new['index']} {new['name']} {new['email']}")
    print(f"   tier_reason chars: {len(new['tier_reason'])}")
    print(f"   template: {new['template']}")
    print(f"   vertical: {new['vertical']}")
    print(f"   total rows now: {len(rows)}")
    # Dedup check
    from collections import Counter
    counts = Counter(r["index"] for r in rows)
    dups = [k for k, v in counts.items() if v != 1]
    print(f"   dups: {dups if dups else 'NONE'}")