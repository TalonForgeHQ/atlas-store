# Supernormal — Focused Outreach Template (Lead 566, meeting_ai_ops cohort sibling #10)

**To:** legal@supernormal.com (canonical first-party privacy contact verified 2026-07-19 via https://www.supernormal.com/privacy-policy)
**Subject:** Can Supernormal reconstruct one client deliverable from meeting to approval?

---

Hi Colin and Fabian,

Your first-party product pages describe a broader workflow than meeting notes alone: Supernormal captures client conversations, creates transcripts and notes, and turns meeting context into client-ready deliverables and AI-agent work. Your About page names Colin Treseler (Co-Founder & CEO) and Fabian Perez (Co-Founder & CTO), and your Security page publishes SOC 2, GDPR, HIPAA/BAA, and AES-256 commitments.

That creates five evidence questions enterprise buyers increasingly ask:

1. **Can one client deliverable be reconstructed end to end?** Meeting ID → consent/capture event → transcript span → speaker attribution → retrieved context → prompt/model version → generated deliverable → human edit/approval → export or downstream action.

2. **Do privacy and security controls propagate across every derivative?** Buyers need deletion, retention, access-control, and residency evidence across recordings, transcripts, summaries, tasks, deliverables, agent outputs, exports, backups, and subprocessors—not just the source meeting.

3. **Are hostile meeting and workspace inputs visible?** Spoken instructions, chat, calendar text, uploaded files, and connected systems can carry prompt injection or poisoned evidence. Detection and reviewer decisions should travel with each affected output.

4. **Can you prove tenant and connector isolation?** Reviewers will ask whether meeting content, OAuth tokens, agent memory, generated deliverables, exports, and model-provider requests stay isolated across client workspaces and subprocessors.

5. **Can security and finance reconcile the same run?** Immutable evidence plus per-meeting and per-deliverable attribution for capture, transcription, inference, storage, integrations, exports, and retention makes audits and margin review faster.

We offer a **$500 fixed-price, 48-hour evidence-gap map** for this workflow, plus an optional **$497/mo quarterly refresh**. The deliverable includes a reconstruction schema, SOC 2/GDPR/HIPAA propagation checklist, prompt-injection test matrix, tenant/connector isolation test plan, and retention/cost-attribution map.

If useful, I can send the one-page outline first.

— Atlas
Talon Forge LLC
atlas@talonforge.io

---

**First-party verification (2026-07-19):**
- `supernormal.com/` returned HTTP 200 and identifies Colin Treseler as Co-Founder & CEO and Fabian Perez as Co-Founder & CTO in first-party organization schema.
- `supernormal.com/about` returned HTTP 200 and states Colin and Fabian founded Supernormal in 2020; it presents both founders and their current roles.
- `supernormal.com/security` returned HTTP 200 and states SOC 2, GDPR, HIPAA support with a BAA, AES-256 storage encryption, and availability of a SOC 2 report, DPA, BAA, and penetration-test summary under NDA.
- `supernormal.com/privacy-policy` returned HTTP 200 and Cloudflare-decodes to `legal@supernormal.com` and `help@supernormal.com`; `legal@supernormal.com` is the canonical privacy-rights contact.
