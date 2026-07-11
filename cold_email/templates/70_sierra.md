# Sierra AI — Customer-Facing Agent Refund Spirals

**To:** hello@sierra.ai (Bret Taylor, Co-founder)
**From:** Atlas @ Talon Forge

---

Hi Sierra team — when a customer-facing CX agent hits an edge case (partial refund, dispute escalation, subscription downgrade with promo credit), a hallucinated action like "refund full amount" or "cancel order" can cascade before a human reviews. We've shipped a $500 / 48h "agent-action audit" specifically for production CX agents: we run 300 scripted conversational paths against your live agent, surface every irreversible action the model can take without confirmation, and ship a single-page remediation list ranked by $$ exposure per conversation. Most teams recoup the audit cost in the first avoided refund-loop incident. Worth a 15-min walkthrough?