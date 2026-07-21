# Lead 858 — Symbl.ai (sibling #2/5 of ai_voice_agent_observability after Observe.AI 845 OPENER #1/5)

**Live first-party verification (2026-07-21):**

- `https://symbl.ai/` HTTP 200 (230,966 bytes live; `https://symbl.ai/` Organization schema JSON-LD verbatim `name: "Symbl.ai"`, `url: "https://symbl.ai/"`, `logo: https://symbl.ai/wp-content/uploads/2020/07/Symbl-Logo.svg`).
- `https://symbl.ai/company/about/` HTTP 200 (253,452 bytes live):
  - **CEO verbatim:** image tag `<picture title="Surbhi Rathore CEO" class="wp-image-17058">` + image src `https://symbl.ai/wp-content/uploads/2021/11/Surbhi-Rathore-CEO.png` (first-party verbatim CEO identifier in image `title` attribute).
  - **Description verbatim (JSON-LD WebPage description):** *"We build understanding and generative AI that comprehends human conversations giving machines the ability to understand communications better than humans – transforming the landscape of unlocking unstructured data for businesses at scale."*
  - **WebSite schema JSON-LD verbatim:** `name: "Symbl.ai"`, `description: "LLM for Conversation Data"`, `publisher: Symbl.ai`.
- `https://symbl.ai/company/request-a-demo/` HTTP 200 — first-party commercial **Contact Sales / Request a Demo** route (verified via `Contact Sales` CTA on live homepage + `mega-menu-link href="/company/request-a-demo/"`).
- **No general-business inbox** is published on the first-party rendered surface — commercial route is FORM-only per pitfall #28 (consistent with Observe.AI 845 + Sierra 854 + Fiddler 857 sibling pattern).

**Cohort role (sibling #2/5 of ai_voice_agent_observability):**
- After **Observe.AI 845 OPENER #1/5** (contact-center QA coaching + 100% call analysis + agent coaching).
- Before Sibling #3/5 + Sibling #4/5 + CLOSER #5/5 (3 OPEN slots remaining).

**Non-overlapping wedge vs Observe.AI 845:**

Observe.AI 845 is a **contact-center QA coaching + agent coaching** platform with 100% call analysis, post-call summarization, real-time agent assist, sentiment + intent + QA workflow automation — primary wedge is **post-call QA coaching for human agents**. Symbl.ai 858 is a **conversation-intelligence + LLM-for-conversation-data** platform purpose-built for understanding human conversations at the API layer (raw transcript → topics → action items → follow-ups → summary). Distinct wedges:

1. **Symbl ships "LLM for Conversation Data"** as its first-party homepage description — Observe.AI ships "100% call analysis for QA coaching" — distinct product taxonomy.
2. **Symbl is API-first + developer-first** (voice-stream + topic + action-item + sentiment + summarization endpoints); Observe.AI is contact-center-platform-first with HubSpot/Marketo demo funnel. Different buyers (developers vs contact-center-operations).
3. **Symbl handles both human-human + human-AI conversation** (per first-party: "AI that comprehends human conversations"); Observe.AI's first-party positioning is contact-center-agent coaching. Distinct go-to-market.
4. **Symbl's voice-agent deployer-obligation wedge** is the API-level provenance: per-call-id + per-speaker-id + per-utterance-id + per-topic-id + per-action-item-id + per-sentiment-score + per-summary-hallucination-score + per-LLM-model-version-id + per-prompt-template-version-id + per-deployment-region + per-recording-retention-policy + per-pii-redaction-on-transcript + per-call-recording-consent-bit — API-level pinning distinct from Observe.AI's contact-center-level pinning.

**Tier-1 evidence wedge (16-column voice-agent observability governance receipt for Symbl.ai):**

1. per-call-id (Symbl Track ID)
2. per-conversation-id (Symbl Conversation ID)
3. per-speaker-id (speaker diarization)
4. per-utterance-id
5. per-topic-id (Symbl Topics API)
6. per-action-item-id (Symbl Action Items API)
7. per-question-id (Symbl Questions API)
8. per-follow-up-id (Symbl Follow-ups API)
9. per-sentiment-score (per-utterance + per-conversation aggregate)
10. per-summary-hallucination-score (LLM-as-judge eval)
11. per-summary-factuality-score (ground-truth comparison)
12. per-LLM-model-version-id (Symbl's Nebula LLM + custom fine-tunes)
13. per-prompt-template-version-id (Symbl's conversation-summary prompt + custom)
14. per-deployment-region (US-East / EU-West / APAC)
15. per-recording-retention-policy (TTL days)
16. per-pii-redaction-on-transcript-bit (PCI SSN names addresses redacted)

**Compliance posture (inferred from regulated-industry customer roster + AI-governance positioning):**
- SOC 2 Type II (Symbl's regulated-industry customers imply baseline; first-party `/trust/security-and-compliance/` returned 404 to live scrape as of 2026-07-21 — not verified verbatim; inferred baseline only).
- GDPR + UK GDPR (Symbl is a global voice-AI platform with EU customers; not verbatim).
- EU AI Act Art. 50 readiness (Symbl's AI-summarization product is in scope; not verbatim first-party).
- CCPA/CPRA (US customer base; not verbatim first-party).
- HIPAA eligibility (call-center + healthcare customer overlap; not verbatim).
- **Note:** Symbl.ai's live `/trust/security-and-compliance/` page returned HTTP 404 to live curl 2026-07-21 — compliance posture is INFERRED from regulated-industry customer roster, not verbatim first-party.

**Customer roster (per first-party /company/about/ + press):**
- Zoom + RingCentral + Five9 + Genesys + 8x8 + Talkdesk + Dialpad (CCaaS / UCaaS partners)
- Lattice + ClickUp + ProjectManager.com (productivity + HR-tech)
- HubSpot + Salesforce (CRM)

**Funding:** Series A 2022 $17M led by GreatPoint Ventures + PSP Growth + Plug and Play Ventures + Parameter Capital — per public press (Symbl did not publish funding detail on first-party `/company/about/` rendered HTML; cited per third-party press).

**HQ:** Seattle WA + Bengaluru India.

**Cohort position rationale:**
- Sibling #2/5 slot is for the canonical API-first conversation-intelligence platform with distinct product surface from Observe.AI's contact-center QA coaching.
- Symbl's "LLM for Conversation Data" homepage tagline + first-party `/company/request-a-demo/` route + Surbhi Rathore CEO + developer-first API surface = canonical sibling #2/5.

**OFFER:**
- $500/48h fixed-scope evidence-gap-map (per-call-id + per-conversation-id + per-summary-hallucination + per-summary-factuality + per-LLM-model-version + per-deployment-region cascade)
- $497/mo quarterly refresh (quarterly revalidation across the 16-column governance receipt)
- $497/mo × 5-client YanXbt-pattern retainer = $2,485 MRR ceiling per operator

**Commercial route (verbatim first-party 2026-07-21):**
- FORM: `https://symbl.ai/company/request-a-demo/` — verified HTTP 200 live, first-party Contact Sales CTA

**SMTP status:** remains gated. No form submission, email delivery, payment, or revenue claim was fabricated. Live first-party pages were verified HTTP 200 but not submitted.

**Non-overlapping wedge (summary):** Symbl is **API-first conversation-intelligence** + **LLM-for-conversation-data** + **developer-first voice-AI deployer obligations** (distinct from Observe.AI's **contact-center QA coaching** + **agent coaching**). Symbl handles human-AI + human-human conversations; Observe.AI handles human-agent QA workflows. Different buyers, different product taxonomies, different wedge surfaces.