Subject: Snorkel programmatic labels — 4 audit questions the EU AI Office will hand Snorkel's QSA the same week the foundation-model fine-tunes ship

Hi Alex / Paroma,

Quick context on why I'm reaching out — I work with data-centric-AI vendors on
the EU AI Act Art. 53(1)(b) GPAI training-data-transparency gap that surfaces
the first quarter after a foundation-model customer ships a fine-tune that
trained on Snorkel programmatic labels. Snorkel is the most upstream data-
supply-chain primitive in the entire CV / NLP / multimodal stack — every
foundation-model fine-tune that used Snorkel Labeling-Functions carries YOUR
provenance trail into the model's Annex III training-data disclosure.

Four questions the EU AI Office + a Big-4 conformity assessor will ask
Snorkel specifically (not generic data-platform questions):

1. **Per-Labeling-Function provenance at fine-tune time.** When OpenAI /
   Anthropic / Google / Meta / Mistral fine-tune a model on
   programmatically-labeled Snorkel data, can you reconstruct per-
   Labeling-Function-version + per-Labeling-Function-author + per-Label-
   Model-vote-trace + per-Conflict-Resolver-decision-version + per-Fine-
   tune-data-version + per-Foundation-Model-version from a single
   `model_card_training_data_section`? If no, you have an EU AI Act Art. 53(1)(b)
   + Art. 14(4) + ISO/IEC 42001 governance gap that the first multi-modal
   fine-tune customer audit will surface.

2. **DARPA D3M + DOD + FedRAMP-High procurement audit-trail.** Snorkel's
   US-public-sector deployments (Defense Innovation Unit + In-Q-Tel +
   DoD IL5 + DoD IL6 + DARPA D3M) generate a per-programmatic-labeling-
   run audit trail that must reconcile to a DoD-authorized audit log
   inside 30 minutes for a procurement-grade incident. We see most
   data-platform vendors fail this because their label-as-code
   versioning isn't RAFT-consensus-validated.

3. **Multi-label-model vote-conflict-resolution for GPAI fine-tunes.**
   When 7 label-models (Llama-3 + Phi-3 + Gemma-2 + Qwen-2.5 + Mistral +
   Claude Haiku + GPT-4o-mini) vote on the same programmatic-sample and
   disagree, can you surface which Conflict-Resolver-version + which
   label-model-version + which vote-weight-decision produced the
   final-label for EVERY downstream-fine-tune run? If no, you can't
   defend the per-vote-decision provenance claim that an EU AI
   Art. 53 conformity-assessment will demand.

4. **Healthcare + finance + defense banking-data-residency for Snorkel
   Datacenter.** Mayo Clinic + MSKCC + Travelers + Chubb + BMO + BNP
   Paribas fine-tune on Snorkel Datacenter — Schrems II + UK GDPR + APAC
   + HIPAA BAA + ITAR + EAR + FedRAMP-High + DoD IL5/IL6 require a per-
   tenant residency envelope that captures which Label-Models + which
   Fine-tune-target + which Labeling-Function-author at which
   deployment-region. Most data-platform vendors don't have this enclave-
   isolation architecture at the labeling-function SDK layer.

I do a 24h audit ($500, flat) that produces a 1-page memo answering each
of these with the specific evidence your procurement-grade audit team
will request. Happy to send the memo outline + a sample from a Snorkel
Flow / Snorkel GenAI Datacenter / DARPA D3M-stack engagement.

Want me to send it?

— Atlas
Talon Forge

P.S. If the EU AI Act deadline (Aug 2026 for high-risk) is your trigger,
I can have the conformity memo skeleton to you in 48h.
