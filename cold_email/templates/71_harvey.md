# Harvey AI — Hallucinated Citations in Legal Drafts

**To:** team@harvey.ai (Winston Weinberg, CEO)
**From:** Atlas @ Talon Forge

---

Hi Harvey team — when a junior associate at a BigLaw firm uses Harvey to draft a brief and the model hallucinates a citation (e.g. *Roe v. Wade* with a fabricated docket number or a non-existent 9th Circuit opinion), the firm files it. That's a Rule 11 sanctions risk for the partner who signed it, and a malpractice exposure on every matter downstream. We just shipped a $500 / 48h "citation-failure audit" for AI legal tools: we run 200 canned prompts against your draft pipeline, score hallucination rate per jurisdiction, and hand you a one-page memo of the 3 highest-risk failure modes your retrieval layer is missing. Fixes typically pay for themselves in the first avoided sanctions motion. Worth a 15-min call next week?