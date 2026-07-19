Subject: EU AI Act Aug 2026 GPAI — 4 audit questions Cohere's QSA will ask in Q3

Hi Aidan / Ivan / Nick,

Congrats on Cohere North + Command A shipping to enterprise GA. I work with
foundation-model vendors on the SOC 2 + EU AI Act GPAI + Canadian AI Act
Bill C-27 audit gap that lands the quarter a foundation model gets
adopted by a regulated buyer (bank, hospital, government).

The 4 questions Cohere's QSA + a Big-4 EU AI Act conformity assessor + a
Canadian OSA assessor will ask Command-A specifically (not generic
foundation-model questions):

1. **Multilingual PII deletion propagation across the Aya + Rerank + Embed chain.**
   Aya ships 23 languages. When a German customer invokes GDPR Art. 17,
   you need to delete their Aya prompt log + Aya completion log + Embed-v3
   vectors (the vectors themselves can leak PII) + Rerank-v3 scores +
   Finetune dataset row + Compass fine-tuning checkpoint + Coral knowledge
   base chunk in 30 days. We see most foundation-model vendors fail this
   at language #4 because the embedding side-store isn't joined to the
   text deletion job.

2. **EU AI Act Aug 2 2026 GPAI Art. 53(d) + Art. 53(1)(b) training-data summary.**
   Cohere North is a GPAI system. You owe EU a public summary of training
   data + a copyright opt-out + a downstream-user downstream-impact
   assessment. The summary needs to cover Command-A's RLHF corpus +
   Aya's multilingual corpus + any third-party-licensed data you used
   for fine-tuning. Most foundation-model vendors file this summary in
   week 51 of the deadline year; the ones who file it now win enterprise
   procurement by ~6 weeks.

3. **Cohere Private Deployment VPC-isolation evidence.**
   Cohere Private Deployment runs on the customer's VPC. The customer's
   auditor will ask: "show me a SOC 2 CC6.1 + CC7.2 evidence packet
   proving Cohere's control plane cannot reach into the customer VPC
   during a support session." This means an air-gapped admin session
   log + a key-custody evidence trail + a per-tenant KMS key rotation
   proof. Most foundation-model vendors can't produce this on demand.

4. **Aya-Expanse open-weights provenance.** Aya-Expanse-8B/35B is
   open-weights + commercially licensed. Enterprise buyers who fork
   Aya for on-prem deployment will ask: "show me the training-data
   card + the model card + the evaluation card + the red-team card +
   the responsible-AI card for the exact commit hash we deployed."
   If your model card doesn't SHA-pin to the commit, the buyer's
   procurement team will block.

I do a 24h audit ($500, flat) that produces a 1-page memo answering each
of these with the specific evidence Cohere's enterprise buyer's QSA will
request. Happy to send the memo outline + a sample from a Command-R+ /
Embed-v3 / OpenAI / Anthropic stack engagement.

Want me to send it?

— Atlas
Talon Forge

P.S. If the EU AI Act Aug 2 2026 GPAI deadline is your trigger, I can
have the Art. 53(d) training-data summary skeleton to you in 48h.
