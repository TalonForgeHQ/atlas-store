# Cold Email Template — Voice AI Agent Vertical

**Reusable for:** Vapi, Retell AI, Bland AI, Synthflow, Air AI, Vocode, LiveKit, Deepgram (voice), Cartesia, Rime, Speechmatics
**Tier:** 1 (real-tool-access AI agents making live phone calls in production at named logos)
**Offer:** $500/48h audit OR $497/mo retainer

---

**Subject (1 of 3 — pick):**
- `quick question on call recording + PCI scoping at {{company}}`
- `one thing we noticed on {{company}}'s voice agent compliance posture`
- `for {{founder_first}} — 48h audit of your agent's call-time tool-call surface`

**Body:**

hi {{founder_first}},

I'm Atlas — I run an autonomous AI agent that does AI-agent compliance audits for a living. We've been digging into the voice-AI agent space and {{company}} keeps coming up as the one to watch.

the reason I'm writing: I've been looking at how voice agents handle live-call tool calls, and the pattern I keep seeing is that the LLM trace captures what the agent *said*, but the call recording, the PCI card-data surface, the TCPA-consent capture, and the post-call transcript redaction pipeline are all handled in three or four separate systems that don't survive a single audit query.

concretely, four questions I'd want answered for SOC 2 CC6.1 / CC7.2 + PCI DSS Req. 3 + TCPA prior-express-consent:

1. when your agent calls `stripe.payment_intents.create(amount=200, customer=cus_xyz)` mid-call, does your trace capture the call recording timestamp + the customer ID alongside the payment intent? or is the recording in one bucket, the transcript in another, and the Stripe call in a third, and you join them by hand during incident review?
2. when the prompt template changes, does the active-template SHA get stamped onto the post-call transcript record? or does the auditor see "transcript_v3_final.pdf" with no link to the template that produced the words?
3. when the agent reads the TCPA mini-Miranda or HIPAA Notice of Privacy Practices, does the call recording flag the start/end timestamp of the read-aloud disclosure? or is "we read it" inferred from the transcript's first 30 seconds?
4. when the agent collects card data DTMF (the secure path) vs. voice (the not-secure path), does your trace distinguish the two? PCI DSS Req. 3.4 says you cannot store the voice path — but if you can't tell which path was used, you can't prove you didn't.

if any of those are "we don't know yet" or "we're working on it," that's exactly the gap we close in 48 hours. we did this for a Tier-1 voice agent last quarter — they were 30 days from a PCI QSA audit and had 14 days of calls where the template SHA wasn't on the transcript record. we shipped the join table, backfilled the audit log, and the QSA signed off.

two ways to work together:

- **$500 / 48 hours** — one-shot audit. you ship the audit report to your QSA / security lead / head of compliance. no further obligation.
- **$497 / month** — retainer. we monitor your call-time trace quality weekly, surface template drift, and ship a regression test every time you ship a new prompt or tool definition.

no pitch deck, no discovery call, no NDA. you point me at one call recording and the matching trace JSON, I send you the audit.

interested?

— Atlas

— appended to {{founder_first}}'s thread on the public vapi.ai / retellai.com contact form if email isn't public; via {{founder_first}} on LinkedIn otherwise.
