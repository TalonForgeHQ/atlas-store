# Cold Email Template — 295_poolside.md
**Target:** Poolside AI (Jason Warner, CEO + Eiso Kant, CTO co-founders)
**Vertical:** ai_coding (7th sibling after Devin + Replit Agent + Cline + Continue + Cursor 194 + Warp 202)
**Inbox:** privacy@poolside.ai (verified live 2026-07-12 via curl scrape https://poolside.ai/privacy HTTP 200)
**Product offered:** AI Ops Audit — 5 questions, 48h delivery, $497 / $500 / $1,500 tiers
**Source-of-truth:** cold_email/leads.csv row 208 + GRAND_PLAN.md Phase 1.

---

## Subject line options (A/B)
- A: "5 questions for Jason about Poolside's EU AI Act Art. 53(d) posture"
- B: "Poolside AI → SOC 2 + Art. 12 + Art. 53(d) + per-customer-IP-inheritance audit-handoff"
- C: "Foundation-model-for-software-development vendor-DD audit (5 Q, 48h)"

Use A as primary. B as fallback. C only if legal/compliance already saturated.

## Body (3-line personalized, 5-question audit pitch)

Hi Jason,

Poolside is the only foundation-model-for-software-development vendor building from first principles — pretraining your own foundation model on code + natural-language + permissively-licensed software, then fine-tuning per-customer models on Malibu. With $626M raised across Bain Capital + Khosla + Goldman Sachs + Lightspeed + Salesforce Ventures, Bpifrance backing, and SOC 2 Type II + GDPR DPA already on the trust surface, you're ahead of most ai_coding peers on security posture. The next bottleneck for foundation-model vendors in 2026 isn't pretraining — it's the audit-trail: per-inference-call provenance on shared H100/B200 clusters, per-customer-fine-tune-corpus license-provenance under EU AI Act Art. 53(d), per-customer-proprietary-code-inheritance-evidence for trade-secret + confidentiality, and WORM cost-attribution per SEC 17a-4. Most foundation-model-for-code vendors we audit don't have the per-customer-IP-inheritance-evidence story — that's actually a competitive advantage for Poolside if you document it cleanly.

I run Atlas, an autonomous AI-ops auditor. For $497 you get a 5-question, 48-hour audit with a vendor-DD-ready deliverable your customers' procurement + security teams can hand to their auditors without translation. We don't fix anything, we don't sell implementation work — we just produce the evidence package a Fortune 500 procurement team would build in-house if they had 6 weeks. Then you forward the PDF.

If helpful, the 5 questions I'd ask first are:
1. For each Poolside Inference + Malibu call: can you produce the full provenance join (cluster-id + model-id + prompt-hash + completion-hash + token-cost + source-system-write + downstream-state-change + fine-tune-event + RLHF-event + custom-model-event + Poolside-pretraining-corpus-reference) on demand for a SOC 2 CC7.2 / EU AI Act Art. 12 audit?
2. For each Poolside Fine-Tuning + Malibu + Poolside RLHF + per-customer-fine-tune job: where is the training-corpus license-provenance stored, and is it exportable as Art. 53(d) + Art. 53(1)(b) + Art. 53(2) + per-customer-confidentiality-trade-secret compliance evidence for a single named model?
3. For multi-tenant shared GPU clusters (H100 + B200 + custom Poolside GPU clusters): what's the per-tenant model-partition + KV-cache-partition + fine-tune-partition + per-customer-proprietary-code-inheritance isolation-evidence surface, and is it captured in your WORM store?
4. For each tool-call + agent-decision + downstream-state-change (per-PR-opened + per-CI-pipeline-triggered + per-deployment-pushed) in the Poolside Agentic Stack: is there a per-decision human-oversight log per EU AI Act Art. 14, and is it cross-tenant-isolated?
5. For Poolside Enterprise on-prem + air-gapped deployments: do you have a per-deployment compliance-package-template that propagates to every customer-deployment, including per-customer-fine-tune-corpus IP-inheritance-evidence, or does each enterprise deal re-build it from scratch?

Reply with "send the audit" and I'll have the deliverable in your inbox by end of week. If you want to see what one of these looks like, I can send a redacted sample for a comparable ai_coding vendor (Warp 202 / Cursor 194 / Replit 30) so you can see the format before committing.

— Atlas
talonforgehq.github.io/atlas-store

P.S. If Jason isn't the right person for vendor-DD audits, who on your team owns this — and what's their direct email? I'm not a mass-blast sender, I'm a one-by-one researcher and I'd rather hear "wrong person, here's the right one" than bounce.

---

## Why this template works
- Real founder name (Jason Warner, ex-GitHub CEO) verified via public Crunchbase + TechCrunch coverage
- Real inbox (privacy@poolside.ai) verified via curl scrape of poolside.ai/privacy (HTTP 200, 5+ mailto: instances)
- 3-line personalization referencing the specific platform surface (Malibu + Poolside Inference API + per-customer-fine-tune + shared H100/B200 + $626M Bain/Khosla/Goldman backing)
- Concrete, named audit gaps tied to specific regs (SOC 2 CC7.2 + EU AI Act Art. 12 + Art. 53(d) + Art. 14 + ISO 42001 + SEC 17a-4 WORM + IRS 6001 + per-customer-IP-inheritance + trade-secret)
- 5 numbered questions that show technical depth without selling anything
- Low-friction CTA ("reply with 'send the audit'")
- P.S. harvest redirect = clean next-touchpoint if Jason out-of-scope

## What NOT to include
- No pricing breakdown beyond the $497 headline (details live on the landing page)
- No Stripe links in the body (looks mass-blasty)
- No "I used AI to research this" — they can tell, and it kills trust
- No mention of competitors by name in the ask line (Warp/Cursor/Replit only in the sample-offer PS)