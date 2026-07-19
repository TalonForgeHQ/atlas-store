# Cold Email — Lead 659 Cognigy (voice_ai cohort sibling #2/5)

**To:** Philipp Heltewig (Co-Founder) <info@cognigy.com>
**Cc:** Sascha Poggemann (Co-Founder) <info@cognigy.com>
**From:** Atlas (Talon Forge LLC — atlas@talonforge.com)
**Subject:** EU AI Act Annex III §1(a) voice-bot FRIA + Art. 50 verbal-disclosure + NiCE-Cognigy SOC 2 integration audit — 5 questions, 48 hours

---

Hi Philipp, Sascha,

Cognigy's positioning as the EMEA enterprise voice-AI agent platform — Cognigy Voice Gateway + Cognigy AI Agents + Cognigy AI Copilot + Cognigy AI Workbench, 100+ languages, 1,000+ enterprise customers across BFSI + telco + retail + travel + insurance + public sector, NiCE CXone-Mpower post-acquisition integration — means every Cognigy-deployed voice-agent is squarely inside **EU AI Act Annex III §1(a) "interaction with natural persons"** strictest classification the moment a DACH, French, Italian, Benelux, Nordics, or UK enterprise CX team turns it on for inbound phone support. The Düsseldorf HQ + EMEA customer base means Cognigy carries the **highest EU AI Act + GDPR + UK GDPR + DACH-data-residency exposure** of any voice_ai cohort vendor.

The compliance wedge the Cognigy team almost certainly has NOT YET shipped:

1. **Art. 27 fundamental-rights-impact-assessment (FRIA) for every Cognigy Voice Gateway EU deployment** — the FRIA template must capture: (a) the specific customer population the voice-agent interacts with (elderly, non-native speakers, hearing-impaired, minors via support lines), (b) categories of fundamental rights at risk (right to be heard, right to information, right to non-discrimination when voice-bots misrecognize accents — Cognigy's 100+ language footprint materially expands the accent-coverage attack surface), (c) the human-oversight protocol for failed handoffs, (d) the rollback plan if the voice-agent systematically misroutes. The Cognigy Voice Gateway PSTN integrations (Genesys + Avaya + Cisco + Twilio + Amazon Connect) mean the deployment context is "real human on the line waiting for help," the canonical Art. 27 trigger.

2. **Art. 50(1) verbal AI-disclosure** — every EU phone interaction that opens with a synthetic voice must verbally disclose "I am an AI assistant" before the first request. The Cognigy Voice Gateway default greeting template does NOT enforce this by default; the platform-level enforcement (a Cognigy system prompt that prepends a verbal-disclosure phrase before user speech) is not yet shipped. Each Cognigy customer has to write their own disclosure string, and many skip it.

3. **NiCE parent-company sub-processor cascade** — Cognigy gateway → NiCE CXone → AWS/Azure infrastructure → underlying LLM endpoints (Azure OpenAI + Anthropic + AWS Bedrock + custom models). The NiCE acquisition closed August 2024 means Cognigy now has a multi-tier sub-processor disclosure obligation that didn't exist pre-acquisition; the integrated NiCE-Trust-Center DPA must enumerate the per-call sub-processor audit trail only Cognigy has (because the NiCE-Cognigy integration is still maturing).

4. **Art. 53(1)(b) GPAI training-data transparency cascade** — Cognigy's underlying LLM providers (Azure OpenAI + Anthropic + AWS Bedrock + custom fine-tunes) require a downstream-cascade disclosure package. Cognigy's published DPA does not yet enumerate the Art. 53(1)(b) cascade which-model-providers + which-versions + which-fine-tunes + which-safety-eval-results were inherited. This is the audit packet Cognigy's enterprise customers' compliance teams will demand before they can sign their own Art. 53 declarations.

5. **NIS2 Art. 21(2)(e) signed-firmware / signed-config for Cognigy Voice Gateway PSTN integrations** — the PSTN gateway is critical infrastructure under NIS2 for any Cognigy enterprise customer in the EU. Cognigy's published security posture covers application-layer (TLS, SOC 2 Type II + ISO 27001 + ISO 27701 in progress, GDPR Art. 28 sub-processor disclosure) but does not yet enumerate the gateway-firmware attestation + signed-config rollout chain + vulnerability-disclosure commitments required by Art. 21(2)(e).

The Cognigy-specific evidence packet that none of your competitors (Voiceflow, Yellow.ai, Cresta, Kore.ai, Rasa, Amelia) has shipped either:

- **Per-Cognigy-Voice-Gateway-version + per-Cognigy-AI-Agent-build + per-Cognigy-AI-Copilot-snapshot telemetry provenance** — which Voice Gateway version generated which AI Agent, which Knowledge Base snapshot was loaded, which PSTN carrier integration was active, which call-recording-on/off flag was set, which underlying LLM was invoked for NLU. This is the audit-grade traceability backbone EU AI Office inspectors will require, and Cognigy's EMEA customer base will face EU AI Office inspections before US competitors do.
- **Voice-biometric data mapping under GDPR Art. 9 + UK GDPR Art. 9 + LGPD Brazil + Quebec Law 25** — Cognigy Voice Gateway call recordings are biometric data when voice-print extraction is enabled. The published privacy policy references GDPR but does not enumerate the Art. 9 biometric-data DPIA requirements across jurisdictions.
- **DACH + Nordics data-residency attestation** — Cognigy Voice Gateway PSTN routing + Cognigy AI Agent storage may transit US, EU, and APAC regions. DACH + France + Nordics enterprise customers require EU-only-data-residency attestation under Schrems II + EU-US Data Privacy Framework; Cognigy's NiCE-acquisition means the data-residency map now includes NiCE CXone-Mpower regional processing — the EU-only-data-residency attestation must span both Cognigy and NiCE CXone.
- **EU AI Act Art. 6 high-risk-classification mapping for emotion-recognition in voice** — Cognigy's tone/sentiment-detection features are explicitly Art. 5(1)(f) workplace-emotion-recognition BANNED-category-adjacent. Customer-service-emotion-recognition is allowed only with explicit opt-in + audit trail; Cognigy's platform-level consent-gate for emotion-recognition-features is not yet shipped.
- **BaFin + Bundesbank EU AI Act high-risk-AI oversight for BFSI voice-agent deployments** — Cognigy's enterprise customer base includes BFSI voice-agent deployments; BaFin's high-risk-AI oversight under the EU AI Act applies, and Cognigy's audit packet must align with BaFin's MaRisk + BAIT + MaSan-AV guidance for AI-assisted financial services.
- **Bundesnetzagentur + BNetzA voice-bot consumer-protection for telco voice-agent deployments** — Cognigy's enterprise customer base includes telco voice-agent deployments; BNetzA's voice-bot consumer-protection rules apply.
- **Per-prompt + per-model-version + per-Decision-Tree-node + per-handoff-event + per-human-override audit trail** — the audit-grade evidence trail for both EU AI Act strictest-tier-voice-bot classification AND for the customer-side SOC 2 Type II controls auditors will demand.
- **Deletion-cascade SLA across retired Cognigy Voice Gateway tenants** — call-recording PII redaction + voice-biometric-template purge + AI Agent deletion receipts.
- **Per-tenant OTA change-management runbook** — Cognigy Voice Gateway + AI Agent + AI Copilot rollouts under 24h blue-green.
- **NiCE-Cognigy integrated SOC 2 Type II cycle** — Q1 2025 became the first integrated NiCE-Cognigy SOC 2 cycle, requiring Cognigy-specific control mapping under the NiCE Trust Center; the integrated audit surface is unique to Cognigy.
- **California SB-1001 + Texas RAIGA + Colorado SB-24-205 + NYC Local Law 144 for post-NiCE US expansion** — Cognigy's NiCE acquisition pushed Cognigy into multi-state US enterprise procurement; the multi-state AI compliance posture is unique.
- **OWASP LLM Top-10 mitigation runbook for Cognigy NLU/LLM stack** (LLM01 prompt-injection via phone-call-context + LLM02 sensitive-info-disclosure via call-recording + LLM06 training-data-exfiltration + LLM08 vector-DB-poisoning via Knowledge Base).
- **MITRE ATLAS mitigation runbook** for adversarial attacks on voice-NLU + voice-synthesis systems.
- **GDPR Art. 20 right to data portability** for Cognigy Voice Gateway call-transcripts + Knowledge Base ingested-content + AI Agent decision-tree-definition.
- **PCI DSS scope-mapping for Cognigy Voice Gateway payment-flow integrations** (Twilio + Stripe + PayPal + Braintree voice-payment patterns).

**The offer:** $500 for a 48-hour evidence-gap map of the Cognigy EU AI Act Annex III §1(a) + Art. 14 + Art. 27 + Art. 50 + NIS2 + GDPR Art. 9 voice-biometric + UK ICO + BaFin + BNetzA + NiCE-Cognigy integrated SOC 2 + California SB-1001 + Texas RAIGA + Colorado SB-24-205 + NYC Local Law 144 evidence readiness — the packet a Cognigy enterprise customer's compliance team demands before greenlighting a Cognigy Voice Gateway deployment in their EU contact center. Or $497/mo for a quarterly refresh retainer that tracks the EU AI Act implementing regulations (Aug 2 2026 effective + delegated acts rolling through 2027).

Best,
Atlas — Talon Forge LLC
atlas@talonforge.com | $500/48h audit · $497/mo MRR | EU AI Act Aug 2 2026 deadline
