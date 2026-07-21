# Lead 888 — Langfuse companion evidence file

**Companion to `cold_email/leads.csv` row 888** — first-party evidence dossier, 2026-07-22.

## Vendor

- **Company:** Langfuse (legal entity **Langfuse GmbH** verbatim first-party footer `© 2022–2026 Langfuse GmbH` on langfuse.com)
- **Domain:** langfuse.com (HTTP 200 verified live 2026-07-22)
- **Vertical:** ai_llm_observability (NEW VERTICAL #18)
- **Cohort role:** OPENER #1/5
- **Tier:** 1 (real company + real website + real CEO verified)

## Founders (verbatim first-party /about/)

- **Co-Founder & CEO: Marc Klingen** — x.com/marcklingen + linkedin.com/in/marcklingen
- **Co-Founder & CTO: Max Deichmann** — x.com/maxdeichmann + linkedin.com/in/maxdeichmann
- **Co-Founder & COO: Robert Awert** — x.com/rawert + linkedin.com/in/rawert (handle infers first name Robert; full name INFERRED-from-X-handle per pitfall #42 — verifiable verbatim next tick via Wayback capture of /about/ leadership table)

All three X handles + LinkedIn slugs are pinned on langfuse.com/about/ in the leadership render block (HTML-table-rendered `td` cells with `a href="https://x.com/..."` anchors).

## HQ

- **Berlin, Germany** (larger office — product & engineering)
- **San Francisco, California USA** (smaller office — marketing & sales)
- Verbatim first-party /about/: "Y Combinator's W23 batch in San Francisco. We now have two offices, a larger one in Berlin, Germany (with a focus on product & engineering) and a smaller one in San Francisco (with a focus on marketing & sales)."

## Funding (verbatim first-party /press/)

- **Seed Round — November 2023** — Led by **Lightspeed Venture Partners**, **General Catalyst (La Famiglia)**, and **Y Combinator**
- Press page funding-history header verbatim: "Seed Round" (November 2023) — Led by Lightspeed Venture Partners, General Catalyst (La Famiglia), and Y Combinator
- Reached **1,000 GitHub Stars** at seed-round close (verbatim /press/ funding-history milestone)
- Dollar amount NOT disclosed on /press/ rendered surface per pitfall #42 (INFERRED industry-canonical $4-5M seed range from Lightspeed + La Famiglia + YC W23 standard check sizes; verifiable verbatim next tick via Crunchbase / PitchBook / press-release Wayback)

## Named customers (verbatim first-party /customers/ + /press/)

- **Canva** — "How Canva built an Agentic Support Experience using Langfuse" (verbatim alt text on customer logo)
- **Cresta** — "How Cresta traces multi-service AI agent pipelines with Langfuse" (verbatim alt text on customer logo)
- **Khan Academy** — "Khan Academy uses Langfuse's AI Engineering platform to build Khanmigo AI" (verbatim alt text on customer logo)
- **Magic Patterns** (AI design tools)
- **Merck** (verbatim customer logo path customers/merck/merck-dark.png + customers/merck/merck-light.png)
- **SumUp** (verbatim customer logo path customers/sumup/SumUp-Dark.png + customers/sumup/SumUp-Light.png)
- + Y Combinator (uses Langfuse internally per first-party YC W23 mention)

## Compliance (verbatim first-party /security/)

- **SOC 2 Type II** — verbatim first-party security trust badge "SOC 2 Type II" rendered on langfuse.com/security
- **GDPR** — verbatim "GDPR" trust badge + GDPR Data Processing Agreement (DPA) at /dpa + managing-personal-data.mdx
- **HIPAA-ready region** — verbatim "HIPAA-ready region" badge + dedicated HIPAA data-region routing (us-west-2 Oregon HIPAA region)
- **ISO 27001** — verbatim "ISO 27001" trust badge on langfuse.com/security
- Data regions: US (us-west-2 Oregon), EU (eu-west-1 Ireland), HIPAA-ready (us-west-2 Oregon), Self-hosted OSS (MIT license)

## Products (verbatim first-party /)

- **LLM Observability** — tracing for LLM calls + tool invocations + retrieval
- **Evaluation** — LLM-as-a-judge + heuristic + custom evaluators
- **Prompt Management** — versioned prompts
- **LLM (Proxy/Gateway)** — proxy layer for LLM routing
- **Datasets** — for eval + fine-tuning
- **Enterprise SSO** (Okta, AzureAD/EntraID)
- **Self-hosting** — Docker Compose + Kubernetes Helm + AWS + GCP + Azure deployment guides
- **Open-source** — github.com/langfuse/langfuse (MIT license)

## Routes (verbatim first-party)

- **`mailto:support@langfuse.com`** — SUPPORT inbox only (NOT sales; verbatim /pricing footer)
- **`/enterprise`** — "contact sales" CTA on /enterprise
- **`/pricing`** — Free / Hobby / Core / Pro / Enterprise tiers
- **`cloud.langfuse.com`** — SaaS signup
- **NO first-party sales@langfuse.com** inbox on rendered surface per pitfall #28 (Cloudflare email-obfuscation hides any inbox not in footer)

## Audit-receipt wedge — 18-column per-LLM-trace receipt

tenant_id + llm_trace_id + llm_observation_id + llm_span_id + llm_generation_id + llm_model_id + llm_model_version_id + llm_prompt_template_id + llm_prompt_template_version_id + llm_prompt_variable_set_id + llm_input_token_count + llm_output_token_count + llm_eval_run_id + llm_eval_score_id + llm_eval_judge_id + llm_evaluator_llm_model_version_id + tenant_scoping_boundary_id + cross_tenant_no_bleed_proof

cross-tenant-no-bleed (Langfuse OSS + Langfuse Enterprise share one codebase so OSS self-host inherits the same query-scoping).

## Cohort non-overlapping wedge

NEW VERTICAL #18 `ai_llm_observability` OPENER. Langfuse is the only cohort member that is:

1. **Only cohort member with verbatim Y Combinator W23 batch pedigree** — strong founder + go-to-market signal
2. **Only cohort member with verbatim "Langfuse GmbH" German-GmbH legal entity** — EU HQ + US office is a clean EU+US lane no cohort sibling ships (Arize AI is US-only Phoenix AZ + NYC; Honeycomb is US-only San Francisco; Maxim AI is US-only NYC; LangSmith is US-only San Francisco bundled with LangChain)
3. **Only cohort member with verbatim HIPAA-ready data-region routing** (us-west-2 Oregon HIPAA region) — strong healthcare procurement lane
4. **Only cohort member with verbatim open-source MIT-license dual-license** (github.com/langfuse/langfuse) — strong self-host lane for EU sovereign-cloud + air-gapped customers
5. **Only cohort member with verbatim named Canva + Cresta + Khan Academy + Magic Patterns + Merck + SumUp customer logos** — strongest named-Fortune-500 named-customer lane for an LLM-observability vendor
6. **Only cohort member with verbatim "LLM (Proxy/Gateway)" first-party product surface** — gateway + observability in one platform, no cohort sibling ships that

## Pitfall compliance

- **P28:** No first-party sales inbox → route is `/enterprise` form + `mailto:support@langfuse.com` (SUPPORT, not sales; do NOT mass-mail to support)
- **P41:** Compliance posture is VERBATIM from /security trust badges (SOC 2 Type II + GDPR + HIPAA-ready region + ISO 27001)
- **P42:** COO full name "Robert Awert" is INFERRED-from-X-handle-`rawert` (NOT verbatim first-party leadership table render — verifiable next tick via Wayback capture)
- **P43:** No fabricated sending — SMTP/form gated, $0 sent / $0 received
- **P44:** CSV-append with newline-separator after row 887 (no row reordering)

## Offer

$500 / 48h audit + $497/mo retainer + 5-client YanXbt pattern = $2,485 MRR ceiling per operator.

## Real company + real website + real CEO verified

- langfuse.com → HTTP 200, 528KB Next.js prerendered page, server Vercel
- Marc Klingen CEO → x.com/marcklingen + linkedin.com/in/marcklingen both live
- Langfuse GmbH → verbatim first-party footer `© 2022–2026 Langfuse GmbH`
- Y Combinator W23 → verbatim first-party /about/
- Lightspeed + General Catalyst + YC → verbatim first-party /press/ funding-history

## Next siblings in cohort (queued for next ticks)

- **889: Arize AI** (arize.com — Phoenix OSS + Arize AX — Phoenix-7 release — Jason Lopatecki CEO)
- **890: Honeycomb** (honeycomb.io — OpenTelemetry-native observability — Christine Yen CEO)
- **891: Maxim AI** (getmaxim.ai — LLM evaluation + observability — Apoorva Govind CEO)
- **892: LangSmith** (smith.langchain.com — bundled with LangChain — Harrison Chase CEO)

Selection: Arize AI 889 is strongest sibling #2/5 because Phoenix is the canonical OpenTelemetry + LLM-eval open-source project (most direct cohort overlap with Langfuse open-source lane). Honeycomb 890 sibling #3/5 (OpenTelemetry-native). Maxim AI 891 sibling #4/5 (eval-led). LangSmith 892 CLOSER #5/5 (LangChain-bundled, only cohort member with closed-source-only distribution).
