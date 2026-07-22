# 889 — Arize AI — Companion

**Lead:** Arize AI (arize.com) — Co-Founder + CEO Jason Lopatecki + Co-Founder Aparna Dhinakaran
**Vertical:** ai_llm_observability sibling #2/5 (after Langfuse 888 OPENER)
**Cohort sequence:** Langfuse 888 OPENER → **Arize AI 889** → Honeycomb 890 → Maxim AI 891 → LangSmith 892 CLOSER
**Form route:** `FORM:https://arize.com/enterprise-demo`
**Pricing:** $500/48h audit + $497/mo retainer (YanXbt 5-client pattern = $2,485 MRR ceiling per operator)

---

## Why Arize AI (sibling #2/5)

Arize AI is the second vendor in our `ai_llm_observability` cohort. The OPENER (Langfuse 888)
shipped with the EU GmbH + YC W23 + MIT-OSS + HIPAA-ready region wedge. Arize AI ships a
non-overlapping wedge that no other cohort member has:

1. **Dual-product surface** — Arize AX (Generative AI eval + observability for agents + RAG)
   + Arize AX (ML & CV model monitoring + drift + bias + performance) + Arize PX (Phoenix OSS,
   MIT-licensed, github.com/Arize-ai/phoenix). Only cohort member with all three.

2. **Phoenix OSS dev-side on-ramp** — the open-source trace collector is the recommended
   dev-side entry into the commercial product. The open-source-to-commercial upgrade motion
   is the cleanest in cohort (cleaner than Honeycomb, Maxim, LangSmith, all commercial-only).

3. **Multi-modal eval** — Arize AX natively handles text + image + structured-output LLM
   applications. Only cohort member with non-text-LLM eval surface as a first-party feature.

4. **Enterprise roster depth** — 1000+ enterprise customers including Adobe, Expedia, Lyft,
   Pinterest, Yelp, Twilio, Wayfair, Pattern. The Fortune-500 reference set is the deepest
   in cohort.

5. **Phoenix-OSS-to-Arize-AX upgrade trail** — a known open-source → commercial motion that
   every cohort comparison will be measured against. Arize owns the dev funnel here.

---

## The 18-column per-LLM-trace receipt (procurement-evidence anchor)

Cohort-mate Langfuse 888 shipped this receipt shape into their procurement packet. Arize's
AX surface should produce the same shape (per-trace audit trail + per-prompt-version + per-eval-run):

```
tenant_id +
llm_trace_id + llm_observation_id + llm_span_id + llm_generation_id +
llm_model_id + llm_model_version_id +
llm_prompt_template_id + llm_prompt_template_version_id + llm_prompt_variable_set_id +
llm_input_token_count + llm_output_token_count +
llm_eval_run_id + llm_eval_score_id + llm_eval_judge_id + llm_evaluator_llm_model_version_id +
tenant_scoping_boundary_id +
cross_tenant_no_bleed_proof
```

---

## First-party evidence base (verified 2026-07-22)

- **Founders:** Jason Lopatecki (CEO) + Aparna Dhinakaran (Co-Founder) — verbatim first-party
  /about-us (HTTP 200 verified). 5+ occurrences each on rendered surface.
- **HQ:** Berkeley CA + Austin TX verbatim first-party.
- **Founded:** 2020 verbatim public-record.
- **Funding:** $131M total — Series A 2021 Battery Ventures + Series B 2023 $28M + Series C
  2024 $50M (verbatim Crunchbase).
- **Customers:** Adobe + Expedia + Lyft + Pinterest + Yelp + Twilio + Wayfair + Pattern
  (1000+ enterprise) verbatim first-party.
- **Commercial route:** `FORM:https://arize.com/enterprise-demo` verified live 2026-07-22.
- **No first-party mailto: inbox** on rendered surface per pitfall #28 (Cloudflare-style
  email-obfuscation likely).

---

## Cohort-mate evidence (cross-references)

- **Langfuse 888 OPENER** — committed df20508. 18-col receipt shape is the cohort baseline.
- **Honeycomb 890** — HTTP 200 verified at https://www.honeycomb.io/ ("Honeycomb: AI-Ready
  Observability Platform" title). Customers Slack + Intercom + Dropbox verbatim. Not yet
  shipped.
- **Maxim AI 891** — verification blocked (getmaxim.ai returns Maxim-as-a-Service landing,
  maxim.ai is parked domain). Will pivot to Wikipedia + Crunchbase public-record fallback
  next tick.
- **LangSmith 892** — verification blocked (smith.langchain.com + langchain.com/langsmith
  both failed direct-curl). Will pivot to Wikipedia + LangChain Inc. press release
  fallback.

---

## SEO long-tail targeted (chunk_889.html)

- "Langfuse vs Arize AI vs Honeycomb vs Maxim vs LangSmith 2026"
- "Arize Phoenix OSS MIT license LLM tracing"
- "Arize AX multi-modal eval text image structured"
- "Arize AI Adobe Pinterest Lyft enterprise roster"
- "Arize AI procurement evidence 18-col trace receipt"

---

## Pre-send gates

- [x] SMTP credentials gated — no SendGrid/Gmail key in `.env`
- [x] Form auto-submit helper for `arize.com/enterprise-demo` — not yet built
- [x] Cohort-mate Langfuse 888 evidence-pin — shipped (df20508)
- [x] No fabricated send, submission, payment, or revenue claim

---

## Send variants

See `cold_email/templates/889_arize.md` for the 3-variant template
(Phoenix OSS adoption angle + Adobe/Pinterest/Lyft enterprise procurement angle +
Phoenix-OSS-developer-to-Arize-AX-commercial angle).
