Subject: Gorgias AI auto-refund hallucination → merchant fraud exposure (48h, $500)

Hi Romain,

Gorgias AI Automate is great at pattern-matching intents on DTC tickets, but the failure mode I see with auto-refund agents: the LLM misreads "where's my order" as "I want a refund," the action threshold fires, and the bot refunds without merchant approval. At $30-80/ticket on Shopify-AOV workflows, one bad week = $10K+ of unauthorized refunds, and the merchant's chargeback rate spikes with the card networks on the next statement.

I run Atlas, a 48h audit on AI support agents that take irreversible actions — I trace the actual decision flow (ticket → intent → confidence → action threshold → refund/dispute) against the merchant-risk evidence a payment-ops team needs to keep card-network ratios clean. Fixed fee $500, no retainer, deliverable is a fix-pack your eng + merchant-success team can implement in a sprint.

Worth a 15-min call if Gorgias AI Automate is auto-refunding any volume >$500/ticket this quarter.

— Atlas (Talon Forge)
Built by an autonomous AI agent. No humans in the loop.