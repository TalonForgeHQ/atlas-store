# MeetGeek — Focused Outreach Template (Lead 561, meeting_ai_ops cohort sibling #5)

**To:** privacy@meetgeek.ai (canonical first-party inbox verified 2026-07-19 via https://meetgeek.ai/privacy-policy/)
**Subject:** Can MeetGeek reconstruct one meeting insight from capture to share-clip?

---

Hi MeetGeek team,

MeetGeek is moving beyond meeting transcription into a privacy-first AI meeting assistant for regulated teams: auto-recording, transcription across 100+ languages, speaker attribution, AI summaries, meeting search, shareable clips, and coaching recommendations. Your first-party privacy policy identifies MeetGeek as a European company supervised by the BfDI (Federal Commissioner for Data Protection and Freedom of Information, Germany) and hosted in AWS EU regions (ISO 27001, PCI DSS Service Provider Level 1, SOC 1/2).

That creates five evidence questions enterprise buyers increasingly ask:

1. **Can one output be reconstructed end to end?** Meeting ID → recording mode → transcript span → speaker attribution → language code → retrieved company context → prompt/model version → summary claim or action item → user edit → share-clip → downstream delivery.

2. **Do consent, pause, access, and deletion events propagate everywhere?** Buyers need traceable controls across recordings, transcripts, summaries, share-clips, search indexes, integrations, backups, and derived analytics. BfDI-led cross-border transfer decisions need per-recording reconstruction.

3. **Are hostile meeting inputs visible?** Spoken instructions, chat, agendas, shared documents, calendar text, and connector content can carry prompt injection or poisoned context. Detection and human-review evidence should travel with the affected output.

4. **Can you prove workspace and connector isolation?** Reviewers will ask whether meeting content, permissioned libraries, OAuth tokens, AI outputs, and the share-clip distribution channel remain isolated across teams, customers, and AWS EU regions.

5. **Can security and finance reconcile the same run?** Immutable evidence plus per-meeting attribution for capture, transcription, model use, storage, share-clip distribution, and downstream actions makes audits and margin review faster.

We offer a **$500 fixed-price, 48-hour evidence-gap map** for this workflow, plus an optional **$497/mo quarterly refresh**. The deliverable includes a reconstruction schema, consent/deletion propagation checklist, prompt-injection test matrix, isolation test plan, and retention/cost-attribution map.

If useful, I can send the one-page outline first.

— Atlas
Talon Forge LLC
atlas@talonforge.io

---

**First-party verification (2026-07-19):**
- `meetgeek.ai/privacy-policy/` returned HTTP 200 (128366 bytes, server-rendered) — exposes `mailto:privacy@meetgeek.ai` and `mailto:hello@meetgeek.ai`
- The privacy policy explicitly states: "As a European company, Meetgeek uses the Federal Commissioner for Data Protection and Freedom of Information as a supervising authority"
- The privacy policy states AWS hosting: "Meetgeek hosts its software in Amazon Web Services (AWS). AWS data centers are certified as ISO 27001, PCI DSS Service Provider Level 1, and/or SOC 1 and 2 compliant. Our database is located in a Virtual Private Cloud (VPC) with AWS and protected by restricted security groups."
- Founder names are not exposed on any first-party server-rendered page (`/about-us`, `/about`, `/team`, `/` are all JS-SPA-walled); the verifiable first-party contact surface is the operations/security team at `privacy@meetgeek.ai`
- Distinct from Granola 557 (human-augmented meeting-notes), Read AI 558 (automated meeting-bot + cross-meeting analytics), Avoma 559 (AI meeting-assistant + AI meeting-scheduler + lead router + revenue-intelligence), and Fellow.ai 560 (botless recording)
