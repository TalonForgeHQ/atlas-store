# Cold outreach — Thinkific

**To:** support@thinkific.com
**From:** Atlas (Talon Forge LLC) — atlas@talonforge.io
**Subject:** 48-hour audit for Thinker + Thinkific's AI course tools ($500 fixed)

---

Hi Greg,

Thinkific's first-party AI page documents three consequential surfaces: the **AI Course Outline Generator**, **AI Quiz Generator**, and **Thinker**, the AI Teaching Assistant that answers learner questions from a creator's own course content. The page says Thinker reached general availability for Thinkific Plus in February 2026 and can surface relevant additional content as an upsell opportunity.

That makes the evidence trail more consequential than a copy assistant: a generated answer can shape a learner's understanding, recommend paid content, or feed creator-authored material back into a live course workflow.

I run a fixed-price, 48-hour AI-agent audit for creator platforms. For Thinkific I would test five questions:

1. Can one record reconstruct **learner question → Thinkific tenant → course and lesson → retrieved creator content → prompt/model/version → Thinker answer → citations → upsell recommendation → learner event**?
2. For outline and quiz generation, can one trace **creator request → source content → generated outline/question/answer → creator approval → published course mutation**, including rollback when a generation is wrong?
3. Can hostile lesson text, uploads, discussion content, URLs, SCORM packages, or integrations inject instructions into Thinker or the course-generation tools?
4. Do tenant and course boundaries prevent one creator's content, assessments, learner data, or paid materials from entering another creator's retrieval or model context?
5. Can Thinkific produce immutable incident evidence linking model/prompt changes, retries, partial failures, human approval, deletion, and per-run cost without stitching together unrelated logs?

The deliverable is a prioritized gap map, reproducible failure cases, and an implementation-ready evidence schema mapped to SOC 2 CC6.1 / CC7.2, EU AI Act Articles 12 and 14, GDPR Article 28, ISO 42001, NIST AI RMF, and OWASP LLM Top 10.

**Price:** $500 fixed. **Delivery:** 48 hours. If this belongs with Trust, Security, Legal, Thinkific Plus, or the Thinker product owner, a redirect is enough.

— Atlas
Talon Forge LLC
atlas@talonforge.io

P.S. I used public first-party Thinkific surfaces only: the About page names Greg Smith as co-founder and CEO (with Matt Smith, Miranda Lievers, and Matt Payne also named as co-founders); the live AI information page documents Thinker plus the outline and quiz generators; and first-party About/Privacy schema exposes support@thinkific.com.
