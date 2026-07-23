# AI gateway evidence benchmark — security follow-up

Subject A: One SOC 2 evidence row across five AI gateways
Subject B: A 48-hour AI gateway audit-trail replay
Subject C: Before the next virtual-key review

Hi {{first_name}},

Security follow-up on the five-gateway benchmark.

I can normalize one production virtual-key path across Portkey, Helicone, LiteLLM, Unify, and Bifrost: actor + tenant + virtual-key → provider + model + region → prompt-hash + completion-hash → guardrail decision (PII / prompt-injection / jailbreak) → fallback chain → cache hit → status + latency + cost → audit-export row.

The deliverable is one replayable audit row, a prioritized control-gap list mapped to SOC 2 CC6/CC7 + ISO 27001 A.8/A.12 + tenant-isolation evidence, and a reusable audit-export checklist for the next key rotation. Fixed scope: $500, delivered in 48 hours. It uses existing gateway exports, audit logs, and incident records—no production access or rotation required.

Worth sending the blank row?

— Atlas
Talon Forge

P.S. I can scope the first pass to one provider and one virtual-key scope.