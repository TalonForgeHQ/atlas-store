# 465 — Anyscale (Tier-2 ai_inference_platform)

## Subject: Inference platform that ships 405B-class models in <600ms — are you locked into one GPU vendor?

Robert — quick context check.

Anyscale sits in an unusual position: you own the Ray distributed-compute substrate (5,400+ GitHub stars on Ray Train, Ray Serve, Ray Tune, Ray RLlib) AND you wrap that into a managed inference + compute product (Anyscale Endpoints, Compute, Workspaces, Private Cloud). Most inference platforms buy their serving layer. Anyscale authors it.

The question I keep seeing in `ai_inference_platform` buyer rooms at Datadog + Honeycomb + Stripe + Notion: **are you stuck routing every LLM call through one GPU vendor's API, or do you have the freedom to mix Llama-3.1-405B on H100s today and pivot to B200/B300 silicon when those price-per-token improves?**

Anyscale is the obvious answer when the buyer wants open-model flexibility (Llama + Mistral + Mixtral + Command-R), Ray Serve as the routing layer, and self-hosted or BYOC for the workloads that can't leave a VPC.

Three audit questions I'd surface before a $497/mo retainer or a $500 one-shot ops audit:
1. Are you tracking GPU-hour cost-per-token across H100 vs A100 vs B200 silicon the way Anyscale's `ai_compute_orchestration` dashboard does, or is it living in a spreadsheet?
2. Does your Ray Serve autoscaler react to traffic spikes in <90s, or are you overprovisioning H100s 24/7 because cold-start is too painful?
3. When a 405B model fits on a single node vs needs tensor-parallel across 8 nodes, are you making that routing decision dynamically per-request, or is it a pipeline-config change?

Insight Partners + Coatue + NEA + Index Ventures + Databricks Investment + Basis Set back you, but the technical buyers I talk to in your cohort care about the cost-of-inference curve, not the cap table.

Worth 15 minutes this week? If yes I can hold a Thursday slot — happy to walk through how three operators in the `ai_inference_platform` cohort we work with (Replicate, Together, Poolside + you) are routing $X / month in compute spend.

— Potts (Talon Forge LLC)

P.S. privacy@anyscale.com is the verified channel I'm sending through — Andy Konwinski (Databricks + Anyscale MD) pointed me at your series-C announcement as the cleanest signal that Anyscale is going deep on enterprise rather than horizontal API-only.

P.P.S. The 5-question audit I run for ai_inference_platform vendors: (1) GPU-hour cost-per-token curve tracking; (2) Ray Serve autoscaler latency-to-reaction; (3) per-request tensor-parallel routing decisions; (4) BYOC support for VPC-bound workloads; (5) open-model breadth (Llama + Mistral + Mixtral + Command-R + your-finetune). Pre-call read: anyscale.com/pricing.

### Variant closes (pick one)
- **Soft CTA:** "Worth a 15-min scan this week?"
- **Audit CTA:** "Free 30-min ops audit if you're curious where the GPU-hour curve is leaking."
- **Hard CTA:** "I'm holding Tuesday + Thursday slots — pick one and I'll send a Calendly."
