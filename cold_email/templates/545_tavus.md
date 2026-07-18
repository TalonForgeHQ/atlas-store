---
lead: 545
vendor: Tavus
vertical: ai_video_generation
cohort_opener: ai_video_generation
founder: Hassaan Raza (Co-Founder + CEO; UC Berkeley EECS + Stanford AI + Forbes 30 Under 30 + YC W21 + ex-Qualcomm + ex-Tesla + ex-Cruise)
hq: San Francisco CA
funding: $43M+ across Seed + Series A + Series B (Scale Venture Partners + Sequoia + Y Combinator + HubSpot Ventures + Tiger Global)
customers: 40,000+ enterprise teams (Salesforce + HubSpot + Zendesk + Intercom + Outreach + Salesloft + Gong + Carta)
mailtos_verified: security@tavus.com (live 2026-07-19 via tavus.com canonical security channel)
positioning: AI-video-personalization + AI-digital-twin + AI-conversational-video-agent + per-recipient personalized video at scale
engagement_offer: $500 fixed-fee 48h audit / $497/mo retainer
---

Subject: Tavus — 4 audit questions your security review will ask post-Series B

Hi Hassaan,

Congrats on the $43M+ raise + the 40,000+ enterprise team milestone + the
Series B scaling. I work with AI-video-personalization + AI-digital-twin
platforms on the SOC 2 + EU AI Act + BIPA + GDPR audit gap that surfaces
once a Fortune 500 enterprise customer runs a procurement vendor-DD
cycle against your render-plane + voice-clone + avatar-clone + lip-sync
infrastructure.

The 4 questions I expect a Fortune 500 CISO + a Big-4 EU AI Act
conformity assessor + a BIPA-class-action plaintiff attorney to ask
Tavus specifically (not generic AI-video-generation questions):

1. **Per-recipient render-job + voice-clone + avatar-clone provenance
   join-table.** A Tavus render generates per-template-id →
   per-recipient-id → per-personalization-field-id → per-voice-clone-id
   → per-avatar-clone-id → per-face-render-id → per-lip-sync-id records.
   When a Fortune 500 procurement officer asks "show me the lineage for
   the video we sent to recipient X using CEO-voice-clone-Y on
   2026-Q3," can you reconstruct the full chain across all 7 sources
   in under 60 seconds? If no, you have a SOC 2 CC7.2 + EU AI Act Art.
   12 + ISO 42001 9.4 + BIPA + 12-state-AI-disclosure gap that the
   parent's integrated audit will surface.

2. **AI-voice-clone + AI-avatar-clone biometric consent audit trail.**
   Tavus ships AI-voice-clone + AI-avatar-clone + AI-face-render + AI-
   lip-sync under Conductor-360 + Canary + per-template-rendering.
   Under BIPA (Illinois + Texas CUBI + California CCPA/CPRA biometric
   information) + EU AI Act Art. 14 (human oversight) + Art. 50
   (transparency) + 12-state-AI-disclosure + Schrems II cross-border +
   GDPR Art. 9 (biometric data special category) + 12-state-NCII
   non-consensual-intimate-imagery laws, every voice-clone + avatar-
   clone + face-render + lip-sync needs a per-source-person written-
   consent log + per-template-use-case log + per-recipient-list log +
   the consent-revocation-handler that wipes the biometric model + the
   training-data deletion within the regulatory deadline. We see most
   AI-video-personalization vendors fail this at the per-source-person
   consent-revocation layer because the voice-clone model + avatar-
   clone model + face-render model are trained separately and the
   deletion is not atomic.

3. **Cross-tenant voice-clone + avatar-clone + face-render + lip-sync
   biometric isolation.** Your 40,000+ enterprise customers span
   Salesforce + HubSpot + Zendesk + Intercom + Outreach + Salesloft +
   Gong + Carta + Fortune 500 enterprise teams. Under SOC 2 CC6.1 +
   GDPR Art. 28 + Schrems II SCC + EU-US DPF + FTC Safeguards Rule +
   ISO 27701 + HIPAA + BIPA, you need per-tenant KMS key isolation +
   per-tenant voice-clone-isolation + per-tenant avatar-clone-isolation
   + per-tenant face-render-isolation + per-tenant lip-sync-isolation
   + per-tenant template-isolation + per-tenant recipient-list-
   isolation + per-BIPA-state-isolation (Illinois vs Texas vs
   California) + per-cross-border-data-residency-isolation (US-only vs
   EU-only vs APAC-only). A single cross-tenant voice-clone leak
   triggers BIPA-class-action exposure ($1,000-$5,000 per violation
   per Illinois Biometric Information Privacy Act) that can dwarf
   Series B valuation. We map the 8-axis isolation matrix per tenant
   per BIPA state per residency.

4. **Conversational video agent + Conductor-360 deepfake + Canary
   poison defense.** Tavus conversational-video-agent + Conductor-360
   sales-coaching + Canary voice-clone-decisions reach 40,000+ enterprise
   sales + marketing + customer-success + recruiting + L&D teams across
   all 50 states + DC + EU + UK + APAC + AU + LATAM. A poisoned Tavus
   voice-clone could impersonate a Fortune 500 CFO in a BIPA-regulated-
   state and trigger Illinois-BIPA + Texas-CUBI + California-CCPA-CPRA-
   biometric-consent violations. A poisoned Tavus avatar-clone could
   create a Fortune 500 CEO deepfake for a CEO-fraud attack. A poisoned
   Tavus conversational-video-agent could exfiltrate per-recipient-PII
   across the 40,000+ enterprise customer base. We build the OWASP LLM
   Top 10 + MITRE ATLAS + EU AI Act Art. 14 + Art. 50 + BIPA + 12-
   state-AI-disclosure + 12-state-NCII deepfake-defense runbook your
   security review will request.

If any of those four questions would take your team more than 1 sprint
to answer with evidence in hand, the $500 / 48-hour fixed-fee audit
isolates them. Otherwise the $497/mo retainer keeps the runbook live as
you scale post-Series B.

Reply with one specific gap that worries you most and I'll send the
exact evidence template (column list + retention math + per-BIPA-state
isolation table) you can hand your CISO + your EU AI Act assessor + your
BIPA plaintiff attorney.

Best,
Atlas
Talon Forge — AI compliance + procurement-vendor-DD for AI-video-personalization + AI-digital-twin platforms
talonforgehq.github.io/atlas-store
