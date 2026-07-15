# Cold Email Template 359 — Inngest (hello@inngest.com)

**To:** hello@inngest.com (verified live 2026-07-16 on the official https://www.inngest.com/privacy page)
**From:** Atlas (Talon Forge LLC — Atlas Store)
**Subject:** question for Inngest — reconstructing durable AI workflow runs end to end

---

Hi Inngest team —

Inngest’s durable execution and workflow platform sits at an unusually important point in the AI application stack: it can coordinate events, retries, queues, background work, human approvals, and long-running agent workflows without asking the application team to operate another orchestration layer. That also makes the execution history a natural audit boundary when an AI workflow produces a customer-visible or business-critical side effect.

The evidence gaps we keep seeing in durable-execution platforms are:

1. **Run provenance:** can a reviewer join the event ID, function version, workflow step, retry or replay decision, model/provider, prompt or instruction hash, tool-call arguments, returned-data hash, and final side-effect ID into one reconstruction record? “The function completed” is not enough when an agent made several durable decisions across hours.

2. **Pause, resume, and human oversight:** when a workflow waits for an event, approval, timeout, or human response, is the exact policy version, approver identity, resumed step, and resulting downstream write preserved? This is the evidence procurement teams ask for under SOC 2 CC7.2, ISO 42001, NIST AI RMF, and EU AI Act Article 14.

3. **Tenant and replay isolation:** can customers prove that event payloads, step state, retries, replay data, secrets, and observability records remain isolated across tenants and regions, including deletion propagation and retention exceptions?

4. **Failure and poisoning response:** when an event, tool result, or retrieved document is malicious, can the incident record link the detection, blocked or quarantined step, retry/replay decision, human review, and downstream state-change outcome?

We help AI workflow and infrastructure teams turn those questions into a compact provenance schema and a 48-hour audit-readiness report. If this is relevant to Inngest’s platform or enterprise roadmap, I’d be happy to compare notes and send the field-level checklist.

— Atlas
Talon Forge LLC — Atlas Store

P.S. I verified hello@inngest.com on Inngest’s official privacy page and Tony Holdstock-Brown as CEO & Founder on the official https://www.inngest.com/about page, so I’m sending this to the company inbox rather than guessing a personal address.
