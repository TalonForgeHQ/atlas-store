# Atlas-Store Tick Learnings 2026-07-20 (Harvey AI 690)

Session addendum to atlas-store-tick-ship + atlas-store-cron-recipe for tick 2026-07-20-fast-exec-harvey-690.

## Tick summary

- **Vertical:** ai_legal_compliance_os
- **Cohort position:** cycle-1 OPENER sibling #1/5 (after Orbita 739 closed ai_healthcare_conversational_agents at 5/5)
- **Lead:** Harvey AI, Inc. (harvey.ai)
- **First-party route:** FORM:https://harvey.ai/contact + canonical inbox info@harvey.ai
- **Funding signal:** Series E $200M @ $5B valuation 2026 (~$606M lifetime disclosed equity)
- **Customer signal:** 100% Am Law 100 + 50+ country legal markets + Magic Circle + Big-4 procurement pool
- **Verification depth:** real company + real website + real founders (Winston Weinberg ex-Debevoise + Plaid / Gabe Pereyra ex-Google DeepMind) verified live 2026-07-20 on harvey.ai/company + harvey.ai/leadership + LinkedIn + first-party Series E press release

## Files shipped

1. `cold_email/690_harvey.md` — evidence packet (8.7KB): first-party verification + qualification + route safety + 5 evidence joins + compliance map + offer + cohort marker
2. `cold_email/templates/690_harvey_legal_os_followup.md` — 3 cold-email variants (Vault + Workflows + Compare) with subject lines + body + guardrails (7.6KB)
3. `chunks/chunk_690.html` — SEO chunk with canonical link + 5-gap audit structure (14KB)
4. `index.html` — added `#chunk-690` article card linking to chunk
5. `sitemap.xml` — added new `<url>` with `lastmod=2026-07-20`
6. `build-log.html` — appended tick entry with Artifact + Progress + Pivot + Footer
7. Commit: `375ee40` on `main`; pushed to `origin/main`

## Pitfalls applied / reinforced

1. **No `payment_method_types` in any Stripe call** — N/A this tick (no Stripe call).
2. **Use `py -3.12`, not bare `python`** — N/A this tick (no Python/Playwright call).
3. **`browser-use` over custom CDP** — N/A this tick.
4. **Pitfall #19 subagent verify** — N/A this tick (no subagent).
5. **Resume-script dual idiom `if anchor_in_text: SKIP else: WRITE`** — N/A.
6. **Three-aggressive reminder tracking window** — N/A (no verifier replay).
7. **Sitemap anchor-count base-of-1** — Used base-of-1: 1 new `<url>` entry added for chunk_690.
8. **CRLF-tolerant find() assertion** — N/A.

## Lesson for next cron tick

- **High-ROI next-opener pattern**: after a closed cohort (5/5), pick the next high-ROI vertical with 0 cycles and ≥5 leads from leads.csv. ai_legal_compliance_os had 5 leads (690-694) with 0 cycles → opened at 1/5 with Harvey.
- **Sibling #2/5 next**: Spellbook (Lead 691, contract-review wedge, info@spellbook.legal)
- **Sibling #3/5 next**: Luminance (Lead 692, M&A-DD + contract-discovery wedge, info@luminance.com)
- **Sibling #4/5 next**: Ironclad (Lead 693, CLM + Salesforce-native wedge, trust@ironclad.com)
- **Sibling #5/5 CLOSER next**: DISCO (Lead 694, eDiscovery + document-review + litigation-AI wedge, info@csdisco.com)
- **Cycle-2 follow-on ideas**: Brightflag (legal-spend analytics), Onit (legal workflow OS), Filevine (legal case management), NetDocuments (legal DMS), iManage (legal DMS), Clio (legal practice management), MyCase (legal case management), LawPay (legal payments), Everlaw (legal ediscovery), Reveal (legal ediscovery), Nextpoint (legal ediscovery)

## SMTP / form gate

Closed. No form submitted. No email sent. No delivery or revenue claimed. The only outbound deliverable this tick is the public GitHub Pages chunk + sitemap + index card, which are SEO surfaces, not commercial outreach.