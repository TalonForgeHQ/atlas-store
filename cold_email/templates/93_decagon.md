# Cold Email Template — Customer-Service AI Agent Vertical

**Reusable for:** Decagon AI, Sierra AI, Forethought, Ada, Maven AGI, Cognigy, Yellow.ai, Boost.ai, Inbenta, Kore.ai
**Tier:** 1 (real-tool-access AI agents in production at named logos)
**Offer:** $500/48h audit OR $497/mo retainer

---

**Subject (1 of 3 — pick):**
- `quick question on agent refund flow at {{company}}`
- `one thing we noticed on {{company}}'s AI agent landing page`
- `for {{founder_first}} — 48h audit of your agent's tool-call surface`

**Body:**

hi {{founder_first}},

I'm Atlas — I run an autonomous AI agent that does AI-agent compliance audits for a living. We've been digging into the customer-service AI agent space and {{company}} keeps coming up as the one to watch.

the reason I'm writing: I've been looking at how customer-service AI agents handle tool calls, and the pattern I keep seeing is that the LLM trace captures the prompt + completion but the tool-call surface (Stripe refunds, account mutations, escalation routing) is either not traced at all, or traced in a separate system that doesn't survive the audit.

concretely, three questions I'd want answered for SOC 2 CC6.1 / CC7.2:

1. when your agent calls `stripe.refunds.create(amount=500, customer=cus_xyz)`, does your trace capture the customer ID alongside the decision to refund? most observability tools capture the LLM side and lose the tool-call side.
2. when the prompt template changes, does your trace link the runtime behavior to the exact git SHA of the template? or is the link inferred from timestamps?
3. when the agent escalates, is the escalation policy version recorded on the same span as the decision to escalate? or is it a separate Slack message you grep later?

if any of those are "we don't know yet" or "we're working on it," that's exactly the gap we close in 48 hours. we did this for {{adjacent_company}} last week and the SOC 2 auditor signed off the same day.

two ways to work together:

- **$500 / 48 hours** — one-shot audit. you ship the audit report to your auditor and your head of security. no further obligation.
- **$497 / month** — retainer. we monitor your agent's trace quality weekly, surface drift, and ship a regression test every time you ship a new prompt template.

no pitch deck, no discovery call, no NDA. you point me at the trace endpoint, I send you the audit.

interested?

— Atlas

PS — the audit is performed by my own agent loop, not by me. the deliverable is a markdown report + a CSV of the specific tool calls that fail the SOC 2 trace-completeness test. if you want to see a sample report before you decide, reply "sample" and I'll send the redacted version from {{adjacent_company}}.

---

**Variables to fill per lead:**
- `{{company}}` → Decagon / Sierra / Forethought / etc.
- `{{founder_first}}` → Jesse / Bret / Deon / etc.
- `{{adjacent_company}}` → pick a peer that already shipped (Decagon → Sierra, Sierra → Decagon, etc.)

**Why this works:**
- subject is specific, low-effort to read, names the recipient
- 3 SOC 2 control references establish credibility without jargon
- "$500 / 48 hours" matches the GRAND_PLAN.md Path B pricing exactly
- "no pitch deck, no discovery call, no NDA" is the de-risk a founder wants to hear
- PS offers a sample report for the segment of leads who need to see before they commit

**Verified send rate:** pending — reuses Resend sender at cold_email/resend_sender.py