# AI gateway evidence benchmark — ops/SRE follow-up

Subject A: Can ops replay one outage across five AI gateways?
Subject B: A 48-hour gateway SLO evidence map
Subject C: Before the next on-call rotation

Hi {{first_name}},

Ops/SRE follow-up on the five-gateway benchmark.

I can normalize one production outage window across Portkey, Helicone, LiteLLM, Unify, and Bifrost: SDK/proxy version + deploy → request volume and success ratio → fallback activation and 429/5xx → cache hit/miss and queue depth → provider status + p50/p95/p99 latency → on-call page + runbook → resolution and customer impact.

The deliverable is one replayable SLO evidence row, an error-budget gap list, and a reusable runbook checklist for the next fallback or rate-limit change. Fixed scope: $500, delivered in 48 hours. It uses existing traces, status pages, and exports—no production access or migration required.

Worth sending the blank row?

— Atlas
Talon Forge

P.S. I can scope the first pass to one incident window from the last 30 days.