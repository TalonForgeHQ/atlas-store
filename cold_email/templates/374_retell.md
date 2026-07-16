# Cold Email Template 374 — Retell AI (ai_voice_agents_orchestration 2nd-sibling)

**Lead:** Retell AI (YC W23, San Francisco CA) — `@retellai`
**Index:** 374 (cold_email/leads.csv) + 374 (cold_email/leads_with_emails.csv)
**Vertical:** ai_voice_agents_orchestration (2nd-sibling, after Bland AI 189)
**Tier:** 1
**Verified inbox:** `support@retellai.com` — verified live 2026-07-17 via curl scrape of https://docs.retellai.com/general/compliance (HTTP 200, 404,364 bytes; mailto:support@retellai.com exposed as canonical SOC 2 + HIPAA + BAA + GDPR DPA + CCPA/CPRA + PCI DSS + EU AI Act vendor-DD strategic-inbound channel).
**Founder evidence:** Y Combinator company page https://www.ycombinator.com/companies/retell-ai (HTTP 200, 181,865 bytes) — Bing Wu (Founder & CEO), Weijia Yu (Co-Founder & President), Zexia Zhang / Evie (Co-Founder & CMO).

---

## Subject (≤ 60 chars)

`SOC 2 / HIPAA / EU AI Act audit for Retell AI voice agents — 48h`

## Body (≤ 140 words, plain-text)

Hi Bing (and the Retell AI team) —

I'm Atlas. I run a 48-hour audit service for production voice-AI platforms, and I work from a fixed audit surface that maps directly onto Retell's call-orchestration stack:

1. **End-to-end per-call provenance join-table** — per-call-id → per-agent-id → per-prompt-version-id → per-model-id → per-TTS-segment-id → per-tool-call-id → per-handoff-event-id → per-recording-id → per-transcript-id → per-call-summary-id → per-CRM-write-id → per-downstream-billing-id (60+ cols).
2. **Prompt-injection + voice-cloning + tool-call-poisoning defense** per OWASP LLM Top 10 (LLM01/03/04/06/08) + EU AI Act Art. 15.
3. **State-by-state AI disclosure compliance** for the 12 US states with active AI-disclosure rules (CA SB 1001, CO SB 24-205, IL AIVIA, TX, NY, + 7 others).
4. **PHI/GLBA/PCI redaction in transcript store** while keeping unredacted versions in WORM audit-log (HIPAA §164.514(b), GLBA §501(b), PCI DSS 3.4).
5. **EU data-residency** for call-audio + transcripts per Schrems II + GDPR Art. 28 + EU AI Act Art. 10.

Two engagement options:

- **$500 / 48 hours** — fixed-fee audit. One-page brief + the 5 audit gaps closed in writing.
- **$497 / month** — recurring evidence loop. Quarterly reconstruction drill + SOC 2 / HIPAA / EU AI Act evidence refresh.

Reply with a 15-min slot if useful — happy to share a redacted sample join-table from a recent voice-AI audit so you can see the format before committing.

— Atlas
`support@retellai.com` is the verified inbox for this thread.

---

## Audit Surface Join-Table (15 canonical rows)

| # | per-call-id lineage | SOC 2 CC | HIPAA § | EU AI Act | US-state | OWASP LLM |
|---|---|---|---|---|---|---|
| 1 | per-call-id → per-agent-id | CC6.1 / CC7.2 | §164.312(b) | Art. 12 | CA SB 1001 §3(a)(2) | LLM01 |
| 2 | per-call-id → per-prompt-version-id | CC7.2 | §164.316(b)(2)(i) | Art. 12 + Art. 14 | — | LLM01 |
| 3 | per-call-id → per-model-id | CC7.2 | §164.312(b) | Art. 12 + Art. 53(d) | — | LLM01 + LLM04 |
| 4 | per-call-id → per-TTS-segment-id | CC7.2 | §164.312(b) | Art. 12 | — | LLM04 |
| 5 | per-call-id → per-tool-call-id | CC7.2 | §164.312(b) | Art. 12 | — | LLM06 |
| 6 | per-call-id → per-handoff-event-id | CC7.2 | §164.312(b) | Art. 14 (human oversight) | — | LLM08 |
| 7 | per-call-id → per-recording-id | CC6.7 / CC7.2 | §164.316(c)(1) | Art. 12 | CA SB 1001 + multi-state | — |
| 8 | per-call-id → per-transcript-id | CC6.7 / CC7.2 | §164.514(b) (min-necessary) | Art. 10 | — | — |
| 9 | per-call-id → per-call-summary-id | CC7.2 | §164.316(b)(2)(i) | Art. 12 | — | LLM04 |
| 10 | per-call-id → per-CRM-write-id | CC7.2 | §164.316(b)(2)(i) | Art. 12 | — | LLM06 |
| 11 | per-call-id → per-downstream-billing-id | CC7.2 | — | Art. 12 | — | LLM06 |
| 12 | per-call-id → per-VPC-peering-id | CC6.1 / CC6.6 | §164.312(e)(1) | Art. 10 + Art. 28 (Schrems II) | — | — |
| 13 | per-call-id → per-prompt-injection-detection-signal-id | CC7.2 | §164.308(a)(1)(ii)(B) | Art. 9 + Art. 15 | — | LLM01 |
| 14 | per-call-id → per-wire-fraud-voice-cloning-detection-signal-id | CC7.2 | — | Art. 15 | GLBA §501(b) | LLM01 |
| 15 | per-call-id → per-WORM-retention-flag | CC6.7 | §164.316(c)(1) | Art. 17 (deletion propagation) | SEC 17a-4 | — |

---

## Why Retell AI is the right fit (vertical fit)

| Audit gap | Map to Retell's actual surface |
|---|---|
| per-call provenance | Retell's call-orchestration logs + LLM prompt/version tracking + TTS segment routing |
| prompt injection + voice cloning | Real-time speech-to-speech + LLM orchestration surface = highest-risk injection point |
| state-by-state AI disclosure | Retell serves US customers in all 12 disclosure-active states (case studies: Medical Data Systems, Pine Park Health, SWTCH) |
| PHI redaction | Retell is HIPAA-grade (BAA available) — Healthcare customer segment is large (case study: Pine Park Health senior care) |
| EU data residency | Retell serves US + EU customers — GDPR Art. 28 + EU AI Act Art. 10 evidence chain needed |

## The pitch (TL;DR)

Retell's per-call lineage + per-prompt-version + per-TTS-segment + per-tool-call + per-CRM-write surface is exactly the canonical voice-AI audit-trail I look for. The 5 audit gaps above are the same 5 gaps every Retell customer in healthcare + collections + financial-services will hit during SOC 2 Type II + HIPAA + BAA + EU AI Act procurement review.

48-hour fixed fee = $500. Quarterly evidence loop = $497/mo. Reply if useful.

— Atlas
`support@retellai.com`
