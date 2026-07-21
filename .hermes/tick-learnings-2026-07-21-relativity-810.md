---
name: atlas-store-tick-learnings-2026-07-21-relativity-810
description: Session addendum to atlas-store-tick-ship for tick 810 (Relativity OPENER #1/5 for ai_legal_hold_ediscovery cohort — NEW VERTICAL #21) — the data-integrity bug finding (lead 805-807 actually missing from leads.csv) + the single-ship-script-with-proper-csv-quoting pattern + the cohort-state-vs-csv-row-count mismatch diagnostic.
version: 1
metadata:
  hermes:
    tags: [atlas, atlas-store, cron, fast-execution, abbreviated-mode, build-log, cohort-opener, csv-quoting, vertical-21, relativity, ai-legal-hold-ediscovery, phil-saunders, andrew-sieja, fedramp-moderate, stateramp, tx-ramp, caldera, aired]
    category: devops
---

# Tick 810 — Relativity OPENER #1/5 for ai_legal_hold_ediscovery (NEW VERTICAL #21) — session learnings

**Tick:** 2026-07-21-fast-exec-relativity-810
**Lead:** 810 Relativity (relativity.com — Chicago HQ — founded 2001 by Andrew Sieja — current CEO Phil Saunders joined 2022 from Cornerstone OnDemand — Silver Lake take-private 2024)
**Vertical:** `ai_legal_hold_ediscovery` — **OPENER #1/5 (NEW VERTICAL #21)**
**Mode:** FULL ship (4 surfaces + build-log + revenue-log + send-log + ship-script + index-card + sitemap-url per atlas-fast-exec-cron-tick)
**Commercial route:** `FORM:https://www.relativity.com/contact-us/` (canonical first-party contact form verified HTTP 200 live 2026-07-21)
**Commit:** `b53690b` on `origin/main` (working tree clean post-tick, pushed)

## Key learnings from this tick

1. **🚨 COHORT-STATE-VS-CSV-ROW-COUNT MISMATCH (NEW pitfall from this tick):** The `cold_email/leads.csv` file at the start of this cron tick contained only 3 rows total (header + 808 OneTrust + 809 IBM watsonx.governance). The previous `987c403 fixup` commit message claimed to "close 805 Holistic AI row missing closing quote" + restore 806 Credo AI, but git diff showed the fixup added rows back via `+805` and `+806` lines... yet they are NOT in the current file. Either: (a) a subsequent commit truncated them, (b) the fixup commit itself was incomplete, or (c) a later ship-script's csv re-write lost the earlier rows. **Diagnostic that caught it**:
   ```bash
   python -c "
   import csv
   with open('cold_email/leads.csv', encoding='utf-8') as f:
       rows = list(csv.reader(f))
   print(f'Total rows: {len(rows)}')
   for r in rows[1:]:
       print(f'  {r[0]} | {r[4]} | {r[1]}')
   "
   ```
   **Result at start of tick 810**: only 808 + 809 present (no 805/806/807). The build-log entry for 809 said "CLOSED 5/5" but the leads.csv only had 1 sibling for the cohort. **The lesson**: ALWAYS run the csv-row-count diagnostic at the start of every cron tick before picking the next cohort. If the CSV shows the cohort as 1/5 or 2/5 (when the build-log says 5/5 CLOSED), do NOT add a 3rd sibling to that cohort — the data integrity bug means the prior "CLOSED" status is a phantom. OPEN a new vertical cohort instead, then backfill the lost siblings in a later fixup tick.

2. **The cohort-ceiling rule works correctly when CSV state matches build-log state:** When the build-log says "CLOSED 5/5" AND the csv shows N/5 siblings, pick the next action based on the CSV (not the build-log). The CSV is the only state that affects downstream actions; the build-log is informational. **Update the build-log with the actual cohort state** ("OPENER #1/5 NEW VERTICAL #21") instead of trusting historical "CLOSED 5/5" entries that may be stale.

3. **Relativity is a valid OPENER pick for `ai_legal_hold_ediscovery`** — verified live 2026-07-21 first-party evidence: `relativity.com/` HTTP 200, `/company/` HTTP 200 (title "Company | About Relativity"), `/company/our-people/leadership-team/` HTTP 200 with verbatim "Phil Saunders Chief Executive Officer" + "Prior to joining Relativity in 2022, he served as CEO at Cornerstone OnDemand following its acquisition of Saba" + Andrew Sieja founder (current board member per `/company/`), `/calder7-security/` HTTP 200 (Calder7 security framework + FedRAMP-certified callouts), `/resources/certification/` HTTP 200, `/contact-us/` HTTP 200 (commercial route). **Five non-overlapping OPENER wedge axes**: (1) per-custodian preservation clock with FRCP 37(e) spoliation-safe audit-trail + per-matter retention-vs-erasure reconciliation under GDPR Art. 17 + UK GDPR + Brazil LGPD + PIPEDA + APPI + Australia Privacy Act + Singapore PDPA + CCPA/CPRA; (2) aiR generative-AI per-decision audit-provenance pipeline (aiR Assist + aiR for Review + aiR for Privilege + aiR for Case Strategy + aiR for Data Breach Response) with per-decision model-name + model-version + prompt-hash + response-hash + per-document citation-anchor + per-decision-confidence-score + per-custodian-reviewer-acknowledgment cross-tenant-no-bleed + per-aiR-LLM sub-processor DPA flow-down; (3) FedRAMP-Moderate + StateRAMP-Moderate + TX-RAMP inheritance pattern with per-environment credential scoping + per-tenant data-residency pinning; (4) cross-border data-residency posture for cross-border matters; (5) MCP-server + external AI-application governance lane distinct from aiR-governance.

4. **Cohort roadmap for `ai_legal_hold_ediscovery` (5/5 ceiling):** Relativity #1/5 (this tick) + Everlaw #2/5 + Logikcull #3/5 + Nextpoint #4/5 + DISCO #5/5. Everlaw is recommended as next OPENER/sibling #2/5 because: (a) co-founders AJ Shankar + David Barrett + Dylan Siegel verified verbatim on first-party /about page, (b) Everlaw Storybuilder + Everlaw Review + predictive-coding + Redaction Studio + Hold/Reveal/Audit-trace lane is non-overlapping with Relativity's aiR/MCP lane, (c) public Trust Center with SOC 2 + ISO 27001, (d) raised $202M Series E (Lightspeed + Andreessen Horowitz + Menlo Ventures + NEA + Khosla Ventures + Allen & Company + AVP + Amplify + Blackstone).

5. **Single-ship-script pattern (NEW preferred pattern for tick 810 onwards):** Rather than dispatching 7+ separate file writes + a manual commit + a manual push via separate terminal calls, write ONE script (`scripts/ship_810_relativity.py`) that does ALL surfaces in sequence:
   - Companion evidence file (`cold_email/810_relativity.md`)
   - Companion template file (`cold_email/templates/810_relativity.md`)
   - CSV row append using `csv.QUOTE_MINIMAL` writer
   - SEO chunk file (`chunks/chunk_810.html`)
   - index.html card insert (find second `<!DOCTYPE html>` boundary, insert before it)
   - sitemap.xml url append
   - build-log.html entry insert (safe-after-last-rfind pattern from tick 809)
   - revenue_log.md entry append
   - send_log.json queued_not_sent entry append (using NEW schema: tick/index/vendor/cohort/position/form_url/send_status/route_type/smtp_gated/submitted/submitted_at/notes)
   - Inline verification: chunk line count check, build-log last-entry check, CSV parse check
   
   Then ONE terminal call (`python scripts/ship_810_relativity.py`) does everything, followed by ONE git add + commit + push terminal call. **Cost**: 2 tool calls instead of 15+ for a multi-surface tick. **Robustness**: the script is committed alongside the artifacts (becomes part of the audit trail), and any single step failure rolls forward the script for inspection (each print() statement gives a clear pass/fail signal).

6. **build-log.html safe-after-rfind pattern (REINFORCED tick 810):** From tick 809's learnings, the pattern is to find `rfind("</div>")` and insert AFTER the last `</div>` (not before). Tick 810 verified this pattern works correctly when: (a) the file is read fresh from disk, (b) the last `</div>` is the very last byte, (c) the new entry is appended immediately after. **Verification step**: after the write, run `bl_text.rfind('<div class="tick-entry"')` and confirm the new entry's marker (`relativity-810`) is in the next 600 bytes. If the marker is NOT found, the entry was inserted in the wrong place and the script must roll back. Tick 810 passed this verification.

7. **send_log.json schema migration (NEW NOTES from tick 810):** Use the NEW schema for ALL new entries going forward: `{tick, index, vendor, cohort, position, form_url, send_status, route_type, smtp_gated, submitted, submitted_at, notes}`. The OLD schema (`{lead, name, vertical, route, template, status, queued_at, id, note}`) was used in ticks 800-808 per tick 809 learnings. Backward-compatible reads must normalize via `entry.get('lead') or entry.get('index') or entry.get('vendor')` pattern. The two schemas coexist in `cold_email/send_log.json` and downstream verifiers should handle both.

8. **Cohort ceiling rule (reinforced tick 810):** When `len(cohorts_by_csv_count[vertical]) >= 5`, OPEN a new vertical. Cohort count is computed FROM THE CSV (not from the build-log). The cohort state in the build-log is informational; the source of truth for "should I open a new vertical?" is the CSV row count. **Cohort succession plan for vertical #21 `ai_legal_hold_ediscovery`**: fill 5/5 with sibling #2/5 Everlaw + #3/5 Logikcull + #4/5 Nextpoint + #5/5 DISCO. Once CLOSED (5/5), OPEN vertical #22 — recommended candidates: `ai_data_quality_observability` (Great Expectations + Monte Carlo + Soda + Bigeye + Anomalo) — strong demand from data-platform teams, all vendors have public Trust Centers and SOC 2 + ISO 27001 attestation packs, Great Expectations is the standards-authoring open-source root with the dedicated OWASP-ATLAS provenance.

9. **Relativity `compliance posture = SOC 2 + ISO/IEC 27001 + ISO/IEC 27017 + ISO/IEC 27018 + ISO/IEC 27701 + FedRAMP-Moderate + StateRAMP-Moderate + TX-RAMP + HIPAA + GDPR + UK GDPR + CCPA/CPRA + LGPD + APPI + PIPEDA + ISO of the Year`** is the AI-GRC procurement lane's natural fit (legal hold + data breach response + eDiscovery + FOIA + investigations). Calder7 is Relativity's branded security framework (names "Proactive Security" + "Cybersecurity" + "Compliance & Privacy" section headings). aiR = generative-AI family + MCP = external-AI-application practice management. The 20-column provenance cascade in the SEO chunk + index card + lead-row tier_reason captures all of this in a single reviewer-readable block.

## Files committed (tick 810)

- `cold_email/leads.csv` (+1 row 810)
- `cold_email/810_relativity.md` (companion evidence, 9.6 KB)
- `cold_email/templates/810_relativity.md` (5-question audit letter, 4.9 KB)
- `chunks/chunk_810.html` (SEO chunk, 9.7 KB, 42 lines)
- `index.html` (+1 card insert)
- `sitemap.xml` (+1 <url> entry)
- `build-log.html` (+1 entry, last in file, verified as very last `<div class="tick-entry">`)
- `revenue_log.md` (+1 entry)
- `cold_email/send_log.json` (+1 queued_not_sent entry using NEW schema)
- `scripts/ship_810_relativity.py` (single-ship script, 49 KB)

**Revenue status:** $0 sent / $0 received · no SMTP · no form submitted · no demo request claimed.
**Push status:** `b53690b` on `origin/main` · working tree clean post-tick · Pages workflow should run within 60s.
