# Lead 803 — Astrix Security

**Company:** Astrix Security (astrix.security)
**Vertical:** `ai_security_red_team`, sibling #4/5 by pivot
**Commercial route:** `FORM:https://astrix.security/contact-us/` (first-party contact page; not submitted)

## Verification

- Homepage: <https://astrix.security/> — first-party title is “Identity Security for AI Agents & NHIs” and the description says Astrix secures agent identities with governance, least-privilege access, and full audit trails.
- Company page: <https://astrix.security/company/> — first-party page title is “About Astrix Security: Mission, Team & Vision”; it describes Astrix as a pioneer of non-human identity security.
- Founder evidence: the same first-party Company page has a **Founders** section naming **Alon Jackson — Co-Founder & CEO** and **Idan Gour — Co-Founder & President**.
- Commercial route: <https://astrix.security/contact-us/> — first-party “Get in Touch with the Astrix Security Team” page says it is for the Astrix platform, a demo, or NHI Security help.

## Cohort fit and pivot

Astrix is a deliberate pivot from the planned Microsoft PyRIT / Microsoft AI Red Team candidate. PyRIT is an open-source Microsoft project rather than a standalone company with a founder-led commercial route, while Astrix is a real company with a current first-party founder roster and a public demo/contact route. Its non-overlapping wedge is **identity security for AI agents and other non-human identities**: API keys, OAuth apps, service accounts, least-privilege governance, and audit trails. This complements HiddenLayer 800’s AI/ML threat-detection + AI-BOM lane, Protect AI 801’s full-stack model-security lane, and Cisco AI Defense 802’s parent-trust-pack inheritance lane.

## Evidence-gap map

1. Inventory provenance: AI-agent identity → API key/OAuth app/service account → owner, environment, scope, creation, last-use, and revocation event.
2. Least-privilege evidence: requested scope → approved scope → policy version → expiry/rotation → human approver → downstream tool call.
3. Non-human identity isolation: tenant, application, environment, secret store, and region boundaries with no cross-tenant credential or audit-log bleed.
4. Runtime accountability: agent instruction → identity selected → credential version → API/OAuth action → downstream state change → rollback or incident record.
5. Compliance and retention: exportable audit trail, deletion cascade, legal hold, DPA/sub-processor boundary, and EU AI Act Art. 14(4) human-oversight record where an agent action is reviewed or blocked.

**Offer:** $500 fixed-scope 48-hour evidence-gap map or $497/month quarterly refresh. No inbox guessed; no form submission, email, delivery, payment, or revenue claimed; SMTP remains gated; `$0 sent / $0 received`.
