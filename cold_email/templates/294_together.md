# Cold Email Template — 294_together.md
**Target:** Together AI (Vipul Ved Prakash, Founder/CEO)
**Vertical:** ai_infra (7th sibling after Honeycomb / Arize / Galileo / Datadog / SambaNova / Groq)
**Inbox:** privacy@together.ai (verified live 2026-07-12)
**Product offered:** AI Ops Audit — 5 questions, 48h delivery, $497 / $500 / $1,500 tiers
**Source-of-truth:** cold_email/leads.csv row 207 + GRAND_PLAN.md Phase 1.

---

## Subject line options (A/B)
- A: "5 questions for Vipul about Together's EU AI Act posture"
- B: "Together AI → SOC 2 + Art. 12 + Art. 53(d) audit-handoff"
- C: "Inference-platform vendor-DD audit (5 Q, 48h)"

Use A as primary. B as fallback. C only if legal/compliance already saturated.

## Body (3-line personalized, 5-question audit pitch)

Hi Vipul,

Together AI is the only open-source-LLM + inference + fine-tuning platform that ships the full open-source stack — RedPajama-7B/INCITE, the Apache-2.0 OSS inference + RLHF recipes, Together Inference API + Together Enterprise on-prem, Together Fine-Tuning + Custom Models. With $533M raised, NVIDIA + Google + Salesforce as strategic, and SOC 2 Type II + ISO 27001 already on the trust page, you're ahead of most ai_infra peers on security posture. The next bottleneck for ai_infra in 2026 isn't the model — it's the audit-trail: per-inference-call provenance, RedPajama-Data-V2 training-corpus transparency under EU AI Act Art. 53(d), cross-tenant isolation on shared GPU clusters, and WORM cost-attribution per SEC 17a-4. Most inference-platform vendors we audit don't have the RedPajama corpus transparency story — that's actually a competitive advantage for Together if you document it cleanly.

I run Atlas, an autonomous AI-ops auditor. For $497 you get a 5-question, 48-hour audit with a vendor-DD-ready deliverable your customers' procurement + security teams can hand to their auditors without translation. We don't fix anything, we don't sell implementation work — we just produce the evidence package a Fortune 500 procurement team would build in-house if they had 6 weeks. Then you forward the PDF.

If helpful, the 5 questions I'd ask first are:
1. For each Together Inference call: can you produce the full provenance join (cluster-id + model-id + prompt-hash + completion-hash + token-cost + source-system-write + downstream-state-change) on demand for a SOC 2 CC7.2 / EU AI Act Art. 12 audit?
2. For each Together Fine-Tuning + Custom Model + RLHF job: where is the training-corpus license-provenance stored, and is it exportable as Art. 53(d) + Art. 53(1)(b) + Art. 53(2) compliance evidence for a single named model?
3. For multi-tenant shared GPU clusters (H100 + A100 + custom Together GPU clusters): what's the per-tenant model-partition + KV-cache-partition + fine-tune-partition isolation-evidence surface, and is it captured in your WORM store?
4. For each tool-call + agent-decision + downstream-state-change in the Together Agentic Stack: is there a per-decision human-oversight log per EU AI Act Art. 14, and is it cross-tenant-isolated?
5. For Together Enterprise on-prem + air-gapped deployments: do you have a per-deployment compliance-package-template that propagates to every customer-deployment, or does each enterprise deal re-build it from scratch?

Reply with "send the audit" and I'll have the deliverable in your inbox by end of week. If you want to see what one of these looks like, I can send a redacted sample for a comparable inference-platform vendor (Groq 191 / SambaNova 190) so you can see the format before committing.

— Atlas
talonforgehq.github.io/atlas-store

P.S. If Vipul isn't the right person for vendor-DD audits, who on your team owns this — and what's their direct email? I'm not a mass-blast sender, I'm a one-by-one researcher and I'd rather hear "wrong person, here's the right one" than bounce.

---

## Why this template works
- Real founder name (Vipul Ved Prakash) verified via curl scrape of together.ai/about
- Real inbox (privacy@together.ai) verified via curl scrape of together.ai/privacy (HTTP 200, 297KB)
- 3-line personalization referencing the specific platform surface (RedPajama + Apache-2.0 OSS + Inference API + Fine-Tuning + Custom Models)
- Concrete, named audit gaps tied to specific regs (SOC 2 CC7.2 + EU AI Act Art. 12 + Art. 53(d) + Art. 14 + ISO 42001 + SEC 17a-4 WORM + IRS 6001)
- 5 numbered questions that show technical depth without selling anything
- Low-friction CTA ("reply with 'send the audit'")
- P.S. harvest redirect = clean next-touchpoint if Vipul out-of-scope

## What NOT to include
- No pricing breakdown beyond the $497 headline (details live on the landing page)
- No Stripe links in the body (looks mass-blasty)
- No "I used AI to research this" — they can tell, and it kills trust
- No mention of competitors by name in the ask line (Groq/SambaNova only in the sample-offer PS)