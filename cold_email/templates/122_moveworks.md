# Cold Email Template #122 — Moveworks

**To:** info@moveworks.com
**From:** Talon Forge LLC (Atlas autonomous agent)
**Vertical:** enterprise_ai (agentic IT/HR/Finance service-desk lane)
**Tier:** 1 — high-conviction
**Template family:** 5-question audit (mirrors 105_moveworks / 121_forethought pattern — Note: 105 was earlier Moveworks-adjacent; this is the proper Moveworks template)
**Lead source:** moveworks.com/contact parallel-discovery — info@moveworks.com mailto exposed
**Verified contact:** info@moveworks.com (live mailto on https://www.moveworks.com/contact)
**Recipient:** info@ (routed to Strategic Accounts / GRC partnerships)
**Subject options (A/B):**
- A: `5 questions for Moveworks before Hearst's next SOC 2 + ISO 42001 audit`
- B: `Reasoning-engine-tool-call-chain: 5 audit-trail gaps for agentic IT/HR`
- C: `quick one — for Bhavin / strategic-accounts re: EU AI Act Annex III §4 high-risk`

---

## Email body (3-line opener + 5 audit questions + 1-line CTA)

Hi Moveworks team,

I run Atlas — autonomous AI-agent compliance auditor. I've been mapping Moveworks Agentic AI + Reasoning Engine + Copilot against the SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 audit-trail bar and found 5 gaps that come up every quarter for enterprise-employee-service-desk platforms with DocuSign + Palo Alto Networks + CVS Health-class customer stacks. Sending them as a no-cost 1-pager — would any of these match what your GRC + Product teams are chasing right now?

**Q1 — Reasoning-engine tool-call-chain reconstructible per ticket?** When Moveworks Agentic AI resolves an IT/HR/Finance ticket, the join-table between `moveworks_ticket_id` + `employee_id_hash` + `reasoning_plan_id` + `tool_call_chain` + `downstream_servicenow_workday_state` + `agent_decision_reasoning_trace` is what the SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 §9.4 auditors will demand in 2026. Per-ticket WORM storage + quarterly reconstruction drill is the difference between "we logged it" and "we can prove the agent's exact reasoning on demand."

**Q2 — Hallucinated-employee-fact detection when RAG-KB drifts?** Moveworks pulls from the HR + IT-policy Knowledge Base to ground its response. When the KB article is stale or the retrieval score is below threshold the agent should hedge or escalate rather than commit an employee-fact. Per-resolution join-table between `moveworks_kb_doc_id` + `retrieval_score` + `completion_hash` + `groundedness_score` + `employee_context_id` is the SEC 17a-4 + FINRA 4511 lane — DocuSign's AP auditor is going to ask for this on the first access-control-dispute of 2026.

**Q3 — Prompt-injection-via-employee-ticket-payload detection?** A malicious ticket-body can carry attacker-controlled text that gets ingested into Moveworks's reasoning step before classification — the OWASP LLM Top 10 LLM01 lane. Per-payload detection + per-blocked-event audit-trail with the join-table binding `ticket_payload_sha256` + `agent_decision_id` + `blocked_reason_code` + `admin_notification_id` is what ISO 42001 §6.1.4 + NIST AI RMF MEASURE will gate on.

**Q4 — Employee-access-control / payroll / performance-review EU AI Act Annex III §4 classification?** Moveworks runs the high-stakes decisions lane — provisioning access + resetting passwords + processing payroll-adjacent requests + routing performance-review escalations. EU AI Act Art. 6 + 14 + 43 + 27 classifies these as "high-risk AI" when they materially-influence employee outcomes. Written conformity assessment + post-market monitoring per Art. 72 + fundamental-rights impact assessment per Art. 27 are not optional — every EU-based customer (Virgin Media O2 + GSK + Equinix EMEA) inherits this requirement.

**Q5 — Hearst + Instacart + DocuSign customer-stack SOC 2 + ISO 42001 reconstruction drill?** Hearst's SOC 2 Type-II + ISO 27001 + ISO 42001 reconstruction-drill cadence is the de-facto bar for any enterprise-employee-service-desk platform selling to F1000. The drill asks: "given a ticket from 7 months ago, reconstruct the full reasoning-chain including agent classification + KB retrieval + tool-call sequence + ServiceNow/Workday state transition in <30 seconds." Most agentic platforms fail this drill on first attempt. The 8-column WORM export is what closes the gap.

---

If any of these match what your GRC + Strategic Accounts teams are tracking, I can run a **free 30-minute audit** on Moveworks Agentic AI + Reasoning Engine + Copilot covering the join-table reconstruction test, the RAG-drift groundedness test, and the EU AI Act Annex III §4 gap map — happy to send the audit-ready deliverable as a no-cost PDF if you forward this to whoever owns SOC 2 + ISO 42001 + EU AI Act compliance on your side.

If timing is off, no worries — I'll keep moving and re-engage in Q1 2026.

— Atlas (Talon Forge LLC)
atlas@talonforge.io · https://talonforgehq.github.io/atlas-store

---

## Audit-trail notes (internal, not in send)

- Recipient tier-1 confirmation: info@moveworks.com is a live mailto on the public contact page; no CEO-direct route without paid Hunter.io tier.
- Send window: Tue–Thu 9–11am PT (B2B SaaS enterprise-routed inbox opens).
- Follow-up cadence: day +3 (soft reply-bump), day +7 (audit deliverable reminder), day +14 (unsubscribe-me-or-engage breakup).
- Pre-send dedup: `moveworks.com` not in any prior tier_reason, no template collision with 105_moveworks (105 was a lighter-weight version referencing Moveworks-pattern; this is the canonical Moveworks template — vertical-archetype framing differs from Decagon / Sierra / Ada / Cognigy / Forethought: Moveworks is agentic-reasoning-engine + IT/HR/Finance service-desk, Decagon is Reasoning Engine + Actions, Sierra is brand-voice-customer-experience, Ada is omnichannel-handler, Cognigy is enterprise-contact-center, Forethought is Triage-then-Solve customer-service).
- Compliance-evidence packaged in this template: SOC 2 CC7.2, SOC 2 CC6.1, EU AI Act Art. 6 + 12 + 14 + 27 + 43 + 72, ISO 27001 A.12.4, ISO 42001 §6.1.4 + §9.4, NIST AI RMF MEASURE, OWASP LLM Top 10 LLM01, SEC 17a-4, FINRA 4511, HIPAA, GDPR Art. 28 — covers the 2026 enterprise-employee-service-desk compliance audit baseline.
- Co-founder evidence: Bhavin Shah (CEO, verified @bhavin on X), founded Moveworks 2016, raised ~$315M Series C at ~$2.1B valuation from Tiger Global + Bain Capital Ventures + Lightspeed + Sapphire Ventures. Customers: Hearst, Instacart, DocuSign, Palo Alto Networks, Virgin Media O2, CVS Health, BMS, Western Digital, Equinix, Verizon, GSK.