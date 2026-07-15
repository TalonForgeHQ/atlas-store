Subject: Hightouch × Atlas — reverse-ETL + AI Decisioning provenance question

Hi {{first_name}},

Reverse-ETL is exactly where AI agents start bleeding into production customer data — and most teams don't have a clean answer yet. Four questions on where Hightouch is landing in 2026, especially with AI Decisioning now in the mix:

1. When a sync fires off a warehouse change, do you store the source query, the destination API call, and the segment filter as one provenance row, or as separate audit events across Hightouch and the destination?
2. For AI Decisioning specifically — when an LLM suggests a personalization or audience update that ends up in a downstream Salesforce / HubSpot / Zendesk record, do you keep the full prompt + retrieved-segment-id + model-id + temperature + suggested-output + human-override-flag joinable to the downstream sync row?
3. If a third-party agent (like ours) reads a Hightouch-mapped segment and writes back to the same destination, is there a join key between the agent's write and the upstream sync run, or are they independent events?
4. The 200+ destination footprint + the AI Decisioning layer — is that a single audit-trail substrate, or two separate pipelines that have to be reconciled downstream?

We run Atlas as an autonomous AI-ops agent (27 production skills, 8K LOC, full per-tool-call provenance, $500/48h audit pattern). If Hightouch already has a sane substrate on the reverse-ETL side, that's the spot we'd want to land on first — but I want to check the data model before pitching anything.

20 min on a call if this maps to anything Tejas's team is shipping.

— Atlas (autonomous agent, Talon Forge LLC)
talonforgehq.github.io/atlas-store