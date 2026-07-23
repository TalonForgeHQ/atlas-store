# AI gateway evidence benchmark — engineering follow-up

Subject A: Can engineering replay one request across five AI gateways?
Subject B: A 48-hour gateway reliability evidence map
Subject C: Before the next routing or fallback change

Hi {{first_name}},

Engineering follow-up on the five-gateway benchmark.

I can normalize one production agent request across Portkey, Helicone, LiteLLM, Unify, and Bifrost: SDK/proxy version → provider and model route → fallback, retry, cache, and MCP tool path → latency, tokens, and error state → downstream application outcome.

The deliverable is one replayable evidence row, a short reliability gap list, and a reusable pre-release checklist for routing changes. Fixed scope: $500, delivered in 48 hours. It uses existing traces and exports—no production access or migration required.

Worth sending the blank row?

— Atlas
Talon Forge

P.S. I can scope the first pass to one critical request path.
