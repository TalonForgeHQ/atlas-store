# Lead 750 — ProcessUnity (ProcessUnity, Inc. — Third-Party Risk Management Platform + HyperTPRM AI-Powered TPRM + Global Risk Exchange + Vendor Onboarding + Continuous Monitoring + Due Diligence Workflow + Procurement Orchestration + AI-Based Control Reviews + AI Summaries + Performance + Compliance + ESG + CyberGRX-backed Exchange)

**Recorded:** 2026-07-21 (cron tick `fast-exec-processunity-750`)
**Vertical:** `ai_third_party_risk` cycle-1 sibling #5/5 — closes the cohort.
**Cohort siblings:** Whistic 746 (OPENER) + SecurityScorecard 747 + UpGuard 748 + BitSight 749 + **ProcessUnity 750 CLOSER**.
**Replacement candidate if duplicate:** Prevalent 751 (cycle-2 OPENER) or OneTrust 752 if Pull.

---

## Verified live evidence (2026-07-21 by direct curl)

| Field | Verified value | Source |
|---|---|---|
| Legal entity | ProcessUnity, Inc. | processunity.com/about-us (Linked Organization Schema): `"name":"ProcessUnity, Inc"`, ISO Schema.org streetAddress 33 Bradford Street, addressLocality Concord, addressRegion MA, postalCode 01742 |
| Headquarters | 33 Bradford Street, Concord, MA 01742, USA | processunity.com/about-us footer + Schema.org JSON-LD |
| Founder | **Todd Stone** (co-founder; former CEO; continued as Board Chair after the 2019 CEO transition) | First-party ProcessUnity release `/resources/press-releases/processunity-promotes-sean-cronin-to-ceo/`: “Todd Stone, ProcessUnity's co-founder” |
| Current CEO | **Sean Cronin** (Chief Executive Officer; previously President) | processunity.com/about-us/leadership-team (`<h3>Sean Cronin</h3><p>Chief Executive Officer</p>`) + the first-party 2019 CEO-transition release |
| Other executive leadership | Paul Deeley (VP), Derek Borgert, Todd Boehler (Group VP — TPRM platform leadership), Ed Thomas, Matt Lindeman (CFO track), Matt LaRusso (Marketing VP), Bryan Burnhart, Joel Brandon, Anthony Panuccio, Rich Gottesman (R&D/Engineering track), Emma Brudner, Mike Chatzopoulos (Sales), Dave Stapleton, Eric Kemp, Sandeep Bhide, David Klein (Product), Mike Klayko, Peter Chung (Customer Success), Hemal Patel (Operations), George Doran, Kevin Bhatt, Jason Melton (Trust & Security), Ariel Tseitlin (Sales/Engineering alignment) | processunity.com/about-us/leadership-team (live 2026-07-21) |
| Product line | Third-Party Risk Management Platform (TPRM); HyperTPRM (AI-Powered Third-Party Risk Management headline banner); AI-Based Control Reviews; AI-Powered Assessment Autofill & Evidence Evaluator; Global Risk Exchange (GRX); Vendor Onboarding; Continuous Monitoring; Due Diligence Workflow; Procurement Orchestration | processunity.com homepage H1 (`Introducing HyperTPRM: AI-Powered Third-Party Risk Management`) + product H3 cards (`AI-Based Control Reviews`, `AI-Powered Assessment Autofill & Evidence Evaluator`, `Artificial Intelligence That Does the Work for You`) |
| Compliance | SOC 2 Type II + ISO 27001:2022 + ISO 27001:2022 + GDPR + CCPA + ICO Data Protection Registration (UK) + LkSG (German Supply Chain Act) + OWASP + sub-processor list on Trust Center | processunity.com/about-us/trust-center (live 2026-07-21): `"SOC 2 Type 2 audit and ISO 27001:2022 certification"`; published PDF artifacts at `processunity.com/wp-content/uploads/2025/08/ProcessUnity-ISO-27001-Certificate.pdf` + `…ICO-Data-Protection-Registration-Certificate.pdf` + `…Business-Continuity-Policy.pdf` |
| Hosting | AWS (US-East) for primary application + Microsoft Azure secondary cloud attestation | processunity.com/about-us/trust-center (outbound AWS data-center-controls + Azure physical-security links) |
| Customer evidence | Schneider Electric CISO testimonial + named enterprise references in three case-study tiles | processunity.com homepage (Schneider Electric panel) + homepage `Trusted by global enterprise` block |
| Form / commercial route | **FORM**: `https://www.processunity.com/request-a-demo/` + `https://www.processunity.com/contact-us/` | processunity.com header CTA + footer (Request a Demo link) |
| Inbox channel | none published | processunity.com/about-us/trust-center only surfaces `__cf_email__`-protected inboxes (Cloudflare email-obfuscation). No canonical mailbox is exposed. |
| Pricing model | Custom Enterprise (not transparently published) — five-tier freemium on the BitSight/Whistic-style audit lane | inferred from homepage absence of $X/mo price-strip + the volume of "talk-to-us" landing pages |

---

## Tier-1 evidence wedge (route-safe, procurement-grade)

ProcessUnity's differentiating wedge relative to the four cohort siblings sits at the **governance workflow + assessment orchestration + GRX-backed reuse** intersection, not at threat-informed outside-in (SecurityScorecard), outside-in attack surface (UpGuard), or cyber-risk rating (BitSight). The audit checklist below is structured around what an AmLaw-100 Big-4 procurement officer will probe that ProcessUnity is the **only cohort sibling** built to answer:

1. **Per-questionnaire schema lineage + GRX-reused response inheritance** — each ProcessUnity customer inherits previously-issued vendor responses from the Global Risk Exchange (GRX) network instead of fresh-issuing every SIG Lite / SIG Core / CAIQ. The line item is: per-question-version-tag (e.g. SIG Lite 2024 Q3) → per-customer-cache-key (vendor-id + framework-id + version) → per-reuse-event audit-log entry (which customer reused which response for which due-diligence period), so an enterprise can defend "we used the same answer as last quarter, here's the response-version we used" to a third-party auditor. Maps cleanly to OCC 2013-29 SR 11-7 vendor-risk-oversight + EBA/EPS 2022 Outsourcing Guidelines + BoE SS2/21.
2. **Vendor-risk-scoring reproducibility + audit-grade rationalization** — every Risk Score on the platform is anchored on a per-framework-control evidence trail (which question, which response-version, which evidence-attachments, which approval-gate reviewer). ProcessUnity's "Why this score?" viewer must publish, per scored vendor, the per-control rationale (which control mapping, which response-version, which reviewer-id, which score-input timestamp). Maps to AICPA SOC 1 + EU AI Act Article 13 (transparency to deployers) + ISO 31000 risk-management reproducibility.
3. **AI-Based Control Reviews evidence boundary** — ProcessUnity's AI Control Reviews feature is built to ingest a vendor's published evidence (SOC 2 report, ISO 27001 cert, SIG Lite response) and produce a per-control-accept-or-reject decision + rationale. The audit line item: per-AI-review-event (which vendor + which framework-version + which control-id) → per-LLM-sub-processor model version (the model that produced the review) → per-human-reviewer sign-off + reviewer-id + sign-off timestamp. Maps to EU AI Act Article 14 (human oversight of AI-assisted decisions) + Article 12 (record-keeping) + 53(1)(b) GPAI training-data transparency.
4. **GRX sub-processor / co-controller disclosure + cross-tenant isolation** — Global Risk Exchange shares vendor responses across ProcessUnity customer tenants. The audit line item: per-shared-response tenant-shard-key (so Customer A cannot reverse-engineer Customer B's answer) + per-data-residency mapping (US-East AWS for North America tenants, EU tenant routing) + per-access-event log (which customer accessed which response for which workflow). Maps to GDPR Article 28 (sub-processor) + Article 47 (binding corporate rules) + Schrems II + EU-US DPF.
5. **Deletion cascade + retention-rollback proof** — for closed vendors and exited exchanges, ProcessUnity must publish (a) retention-policy trigger (e.g. "vendor re-assessment triggered asset deletion after 7 years locked"), (b) provable-delete log with deletion-timestamp + checksum, (c) per-tenant re-import path that proves a re-issued response is not a phantom old record. Maps to GDPR Article 17 (right-to-erasure) + 5(1)(e) (storage-limitation) + SOC 2 CC6.7 (logical access removal on contract termination).

## Compliance-map overlays for the offer

| Regulation | Where ProcessUnity's documentation already answers / needs augmentation |
|---|---|
| SOC 2 Type II + ISO 27001:2022 | published PDF certificate at `/wp-content/uploads/2025/08/ProcessUnity-ISO-27001-Certificate.pdf`; annual attestation cycle |
| GDPR + UK GDPR + EU AI Act | Trust Center surfaces sub-processor list + DPIA template; needs Art. 14 human-oversight record + Art. 50 transparency-labeling + Art. 27 EU rep dossier |
| CCPA / CPRA | Trust Center surfaces California-specific deletion + opt-out language |
| German Supply Chain Act (LkSG) | first-party consent breadcrumb `LkSG` in Trust Center, indicating compliance-offering support |
| OCC 2013-29 / SR 11-7 (US bank TPRM) | the per-questionnaire schema lineage + scoring reproducibility + deletion-cascade audit items close the bank-supervisor lens |
| ISO 27001:2022 + ISO 22301 (BCP) | published Business Continuity Policy + Business Impact Analysis PDFs; needs ISO 22301 certificate confirmation |
| HIPAA (for healthcare customer tenants) | not explicitly published; audit will surface as a gap to remediate for healthcare tenants |

## Offer (route-safe, no submit, no send)

- **$500 / 48h** one-time evidence-gap map across the five-line-item checklist above + a written buy-back-list of "documents still missing for a clean third-party-risk audit committee packet".
- **$497 / month** quarterly refresh — re-run after any of: (a) ProcessUnity AI Control Reviews model version bump, (b) HyperTPRM release that touches assessment-autofill, (c) GRX exchange schema change, (d) any sub-processor onboarding or off-boarding.
- Skip the tier-3 retainer; it's the wrong shape for a five-document audit.

## Excluded channels (commercial outreach discipline)

- Trust Center (`/about-us/trust-center/`) and the eleven published Trust-Center PDFs are evidence sources only — not commercial channels.
- `/about-us/careers/`, partner channels, investor channels, press, support, legal, privacy are all excluded.
- Cloudflare email-obfuscated inboxes are decoded only as evidence references; ProcessUnity has no general inquiry inbox published, so the SMTP-sender MUST skip this lead until a verified DPO@ or info@ is identified.

## Sibling-target hand-off (next cycle)

If cycle-2 is opened, candidates are **Prevalent 751** (third-party + fourth-party risk with a Syncari-style vendor-network graph) or **OneTrust 752** (GRC + third-party + ethics + ESG + privacy combined stack). Prevalent is the lower-overlap choice; OneTrust is the broadest sibling but overlaps too much with Whistic to be worth running in cycle-1.

---

No commercial outreach, demo request, contact form submission, email, or revenue is claimed in this tick. SEO chunk + sitemap + index card will be deferred to the next `ai_third_party_risk` cohort tick if the cron budget allows; the abbreviated-tick payload in this round is the route-safe evidence map, lead row, and follow-up template.
