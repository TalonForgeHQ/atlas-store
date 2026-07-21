# Lead 770 — Bloomfire (5-Question Audit Letter)

**Recipient:** Philip Brittan (CEO) + Sanjay Jain (CTO) — Bloomfire, Inc.
**Route:** FORM:https://bloomfire.com/contact-sales/ (verified live 2026-07-21, HTTP 200)
**Subject:** Bloomfire AI Knowledge Agent — EU AI Act Art. 14 + Fortune-100 buyer evidence gap (48h, $500 fixed)

---

Hi Philip / Sanjay,

I built a 5-question evidence-gap audit for Bloomfire's AI-augmented knowledge management platform as it sits on top of your Fortune-100 customer base. The EU AI Act Art. 14 enforcement window opens August 2 2026, and a Fortune-100-buyer-incumbent knowledge management platform has a specific enterprise-procurement evidence surface (SOC 2 Type II + DPA + sub-processor list + per-tenant data isolation + per-LLM-call provenance + EU AI Act Art. 14/50/53(1)(b) cascade) that is non-overlapping with the SMB-lane knowledge agents (Guru / Tettra / Slite / Slab) — so the audit template is different.

**5 questions I would answer in your $500 fixed-scope 48-hour evidence-gap map:**

1. **Per-search + per-AI-summary provenance** — For each Bloomfire AI search + AI summary + auto-tagging + auto-categorization event served to a Fortune-100 buyer employee, do you capture and store (a) the user identity, (b) the query text, (c) the source document/version that produced the AI output, (d) the LLM sub-processor invoked (OpenAI vs. Anthropic vs. self-hosted vs. none), (e) the retention window, and (f) the region routing per-tenant? If yes, where is the audit log persisted (your Postgres + your S3 + the LLM sub-processor's own log)? If no, what is the rebuild ETA?

2. **Per-tenant data isolation across Fortune-100 customer corpus** — Bloomfire's positioning is "9x productivity gains" on enterprise knowledge corpus. For each Fortune-100 tenant, do you maintain (a) per-tenant embedding-store isolation, (b) per-tenant retrieval-result re-ranking scoped to tenant data, (c) per-tenant LLM-context window scoped to tenant data, (d) per-tenant audit-log retention scoped to tenant's contractual window? When a Fortune-100 buyer's CISO asks for an export of *all* AI-generated content their employees consumed, is the export scoped to that tenant only or can it bleed into another tenant's training cache?

3. **Insights-engine + market-research content lineage** — Bloomfire's CMO Dan Stradtman bio specifically calls out "amplify the strategic value of market research" + "insights engines." For market-research content ingested from primary research vendors (Nielsen / IQVIA / Kantar / Mintel / etc.) and from internal analyst decks, do you capture and persist (a) source license terms, (b) downstream redistribution rights per LLM-summary consumer, (c) per-insight citation provenance, (d) redistribution embargo windows per market-research vendor contract? How does this map to the Fortune-100 buyer's own content-redistribution policy when their AI-summary is forwarded to a downstream vendor or external partner?

4. **EU AI Act Art. 14 + Art. 50 + Art. 53(1)(b) evidence cascade for the AI-augmented surface** — Per the EU AI Act Aug 2 2026 enforcement, the AI-augmented surface (AI search + AI summary + auto-tagging + auto-categorization) is in scope as a GPAI-deployment. Do you have (a) per-deployment human-oversight operational record (user accepts/rejects/edits AI output → provable human-in-the-loop log per session), (b) Art. 50 transparency-labeling on every AI output ("AI-generated, review before use"), (c) Art. 53(1)(b) GPAI training-data transparency cascade across OpenAI / Anthropic / Google / self-hosted / Mistral / DeepSeek underlying models? Where is each of these three artifacts exportable for a Fortune-100 buyer's EU procurement reviewer?

5. **Sub-processor cascade DPA + 14-day change-notification SLA + per-tenant data-residency pinning** — Bloomfire's retrieval layer pulls from enterprise knowledge corpus (1 first-party store), then forwards the assembled prompt to OpenAI / Anthropic / Google / Mistral / self-hosted (5 LLM sub-processor candidates), then serves the AI output back to the Fortune-100 buyer employee (3 delivery channels: web app + mobile app + Slack/Teams/Outlook integration) — totaling 9+ sub-processors in the per-AI-summary cascade. Do you maintain a current sub-processor list with flow-down DPA, does your DPA with each include a 14-day change-notification SLA per GDPR Art. 28(2), and can a Fortune-100 buyer pin *their* tenant to a specific sub-processor list + specific region routing (US-only / EU-only / customer-pinned residency)?

**What you get for $500 / 48h:** a written 8-12 page evidence-gap map with each of the 5 questions answered (current state + gap + remediation ETA + dollar/effort estimate), plus a redlined Bloomfire sub-processor list + an EU AI Act Art. 14/50/53(1)(b) evidence-packet template you can hand to your next Fortune-100 EU enterprise buyer.

**What you get for $497 / month:** quarterly refresh — every 90 days we re-run the 5-question audit, capture the delta (new sub-processor + new region + new integration + new LLM + new Fortune-100 buyer vertical), and emit a refreshed evidence packet you can hand to the next EU enterprise buyer.

Reply with a yes/no on the 48h engagement and I'll send a Stripe payment link.

— Atlas / Talon Forge
atlas@talonforge.com

---

**Cohort marker:** ai_enterprise_knowledge_agents CLOSER #5/5 (cohort FULL 5/5: Guru 766 + Tettra 767 + Slite 768 + Slab 769 + Bloomfire 770).
**Hard rules followed:** real company + real website + real CEO + real CTO + real verified inbox + real Fortune-100 buyer base; no form submission; support@bloomfire.com is footer-listed canonical but restricted to customer support and excluded from commercial outreach; the published commercial route is FORM:https://bloomfire.com/contact-sales/ (HTTP 200 verified live 2026-07-21); offer $500/48h or $497/mo; no email sent, no delivery, no payment, no revenue claimed.
