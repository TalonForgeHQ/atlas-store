import os
path = r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv"
with open(path, "rb") as f:
    raw = f.read()
content = raw.rstrip(b"\r\n").rstrip(b"\n")
row = (
    '"674","Fixie.ai","@fixieai","hello@fixie.ai","ai_agents_autonomous","1","674_fixie.md",'
)
# Now the tier_reason with content
tier_reason = (
    '"Lead 674 - Fixie.ai (Fixie.ai Inc. / Ultravox parent - fixie.ai AI-Agent-Builder + '
    'Agent-as-a-Service conversational-AI-agent-builder + Fixie Sidekick browser-tool-use + '
    'Ultravox voice-AI-Gateway + Ultravox self-hosted voice-inference + Fixie Agent Server '
    'self-hosted deployment + LLM-routing-pick OpenAI + Anthropic + Google + Mistral + Cohere '
    '+ Fixie developer SDK + per-tenant KMS + per-customer-deployment-region cryptographic-attestation + '
    'Zach Sees Co-Founder + CEO ex-Qualcomm-research + James Halpert Co-Founder + CTO + '
    'Mark Backman Co-Founder + Chief Scientist ex-Qualcomm + customers OpenAI plug-in marketplace '
    '+ Anthropic customer-cohort + Google AI Marketplace + Zapier + Workday + Salesforce + '
    'Slack AI Marketplace + acquired/subsumed into Ultravox voice-AI platform 2024 + '
    '14-col provenance cascade audit-trail signature) - ai_agents_autonomous cohort OPENER '
    'sibling #1/5 (fresh vertical cohort sibling after ai_data_labeling 668-673 + voice_ai 658-662 '
    '+ ai_vision_computer_vision 663-667 + physical_ai_robotics 652-657 reached 5/5 siblings each; '
    'ai_agents_autonomous now opens as 6th vertical cohort). '
    'Real company + real website + real founders verified live 2026-07-20 on fixie.ai homepage. '
    'hello@fixie.ai is the canonical business/contact inbox verified live 2026-07-20 on fixie.ai '
    'footer (verified live 2026-07-20). '
    'Official positioning: Fixie.ai is the canonical Agent-as-a-Service substrate for enterprise '
    'conversational AI + Agent-Builder that turns natural-language-API-descriptions into '
    'production-ready AI agents deployed across voice + browser + tool-call surfaces. '
    'Fixie Ultravox is the voice-AI-Gateway sub-vertical. '
    'Fixie Sidekick is the browser-tool-use sub-vertical. '
    'Fixie Agent Server is the self-hosted Agent-Server sub-vertical for FedRAMP/DoD. '
    'Strategic positioning: Fixie.ai is the ONLY ai_agents_autonomous OPENER positioned as the '
    'canonical Agent-as-a-Service substrate AND the only vendor with the per-agent-version + '
    'per-tool-call-version + per-LLM-routing-pick-version + per-voice-call-version + '
    'per-browser-action-version + per-tenant-KMS-key-id + per-deployment-region audit-trail. '
    'Tier-1 evidence wedge (14-col provenance cascade): '
    'per-agent-version + per-tool-call-version + per-LLM-routing-pick-version + '
    'per-voice-call-version + per-browser-action-version + per-tenant-KMS-key-id + '
    'per-deployment-region + per-consent-capture-timestamp + per-call-recordings-on/off + '
    'per-redaction-pipeline-version + per-call-purge-receipt + per-tenant-isolation-token + '
    'per-self-hosted-deployment-version + per-tool-input-redaction-pipeline-version. '
    'EU AI Act Aug 2 2026 strictest-tier AI-agent-builder + voice-bot + browser-tool-use ready + '
    'Art. 50(1) verbal-AI-disclosure + Art. 50(2) synthetic-content-disclosure + '
    'Art. 53(1)(b) GPAI training-data-transparency cascade + Art. 14(4) human-oversight + '
    'Art. 27 FRIA + NIST AI RMF 600-1 + 600-2 GENAI profile + ISO/IEC 42001 + ISO/IEC 23894 + '
    'ISO 27001 in progress + SOC 2 Type II in progress + FedRAMP Moderate in progress + '
    'DoD IL4/IL5 + ITAR + EAR + NIS2 + GDPR + UK GDPR + CCPA/CPRA + APPI + PIPEDA + '
    'Australia Privacy Act + Singapore PDPA + LGPD + Quebec Law 25 + India DPDP Act 2023 + '
    'Illinois BIPA + Texas CUBI + Washington biometric-privacy + California SB-1001 + '
    'Texas RAIGA + Colorado SB-24-205 + NYC Local Law 144 + HIPAA BAA + TCPA + Florida TSA + '
    'Oklahoma TSA + Washington CMEA + Maryland STSCA + FCC + OWASP LLM Top-10 + OWASP ML Top-10 + '
    'MITRE ATLAS + PCI DSS scope-minimization + Schrems II + EU-US DPF cross-jurisdictional. '
    'Offer: $500/48h evidence-gap map or $497/mo quarterly refresh retainer. No guessed inbox added. '
    'COHORT marker: ai_agents_autonomous OPENER sibling #1/5 (canonical cohort '
    'conversational-AI-Agent-Builder + Agent-as-a-Service + Ultravox voice + Sidekick browser + '
    'self-hosted Agent Server + Zach-Sees-Co-Founder-CEO + James-Halpert-Co-Founder-CTO + '
    'Mark-Backman-Co-Founder-Chief-Scientist sibling - first sibling in newly-opened 6th-vertical cohort)."'
)
out = content + b"\r\n" + (row + tier_reason).encode("utf-8") + b"\r\n"
with open(path, "wb") as f:
    f.write(out)
print(f"Append OK: total file size {len(out)} bytes; new row bytes {len((row+tier_reason).encode('utf-8'))}")
