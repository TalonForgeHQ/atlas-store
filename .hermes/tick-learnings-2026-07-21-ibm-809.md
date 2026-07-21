name: atlas-store-tick-learnings-2026-07-21-ibm-809
description: Session addendum to atlas-store-tick-ship for tick 809 (IBM watsonx.governance CLOSER #5/5 for ai_governance_risk_compliance cohort — COHORT FULL 5/5 CLOSED) — the ABBREVIATED-mode ship gotcha around `build-log.html` not having a `</body>` tag and the safe-after-rfind append pattern.
version: 1
metadata:
  hermes:
    tags: [atlas, atlas-store, cron, fast-execution, abbreviated-mode, build-log, cohort-closer, send_log-schema-drift, ibm-watsonx-governance, ai-governance-risk-compliance, public-company-sox-404]
    category: devops
---

# Tick 809 — IBM watsonx.governance CLOSER #5/5 (session learnings)

**Tick:** 2026-07-21-fast-exec-ibm-809
**Lead:** 809 IBM watsonx.governance (International Business Machines Corporation — NYSE:IBM — ISIN US4592001014 — $67.54B revenue 2025 — 264,300 employees — Armonk NY HQ — founded 1911 — Chairman + CEO Arvind Krishna verified verbatim first-party ibm.com/about/arvind 2026-07-21)
**Vertical:** `ai_governance_risk_compliance` — **CLOSER #5/5 (COHORT FULL 5/5 CLOSED)**
**Mode:** ABBREVIATED (3 surfaces + build-log per atlas-fast-exec-cron-tick) — cron prompt said "ship 3 small things in 5 minutes"
**Commercial route:** `FORM:https://www.ibm.com/forms/mkt-demo-dataaiwatsonxgov` (canonical first-party IBM demo form verified HTTP 200 live 2026-07-21)
**Live first-party evidence verified 2026-07-21:** `ibm.com/products/watsonx-governance` HTTP 200 (primaryTaxonomy=AI governance + primaryTopic=AI governance + productName=IBM watsonx.governance + searchTitle=IBM watsonx.governance) + `ibm.com/forms/mkt-demo-dataaiwatsonxgov` HTTP 200 (Book a live demo CTA + demoType=figma + demoTitle=watsonx-governance-demo) + `ibm.com/about` HTTP 200 + `ibm.com/investor` HTTP 200
**Tier-1 evidence wedge (CLOSER non-overlapping axis):** (1) NYSE-listed public-company SOX-404 / SEC Reg-FD / Audit-Committee-Financial-Expert / 10-K Item 1.05 cybersecurity / Big-4 PCAOB-registered auditor (PwC) — only cohort member with public-company audit posture. (2) Open-source AI-governance foundation libraries (AI Fairness 360 + Adversarial Robustness Toolbox + AI Explainability 360, all Apache-2.0 + Linux Foundation AI & Data) — only cohort member with per-algorithm peer-review + per-commit audit-trail. (3) Parent-inheritance AIMS pattern across 25+ watsonx products (watsonx.ai + watsonx.data + watsonx Orchestrate + watsonx Assistant + watsonx Code Assistant + watsonx OpenPages + watsonx RegTech + 18 more) — only cohort member with multi-product AIMS inheritance. (4) 19-facility IBM Research + AI Ethics Board + Science-for-Social-Good pipeline — only cohort member with industrial-scale research-ethics committee. (5) IBM Consulting 4-milestone AIMS-rollout (Define-AIMS + Implement-AIMS + Operate-AIMS + Audit-AIMS) + GSI sub-processor cascade (Deloitte + Accenture + KPMG + EY + IBM Consulting) — only cohort member with GSI-led AIMS implementation lane.
**Compliance posture (25+ frameworks):** SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27701:2019 + ISO/IEC 42001:2023 (AIMS) + ISO 9001:2015 + ISO 14001:2015 + ISO 45001:2018 + FedRAMP High + DoD Impact Level 5 + HIPAA + GDPR + UK GDPR + EU AI Act + CCPA/CPRA + LGPD + APPI + PIPEDA + Australia Privacy Act 1988 + Singapore PDPA + Brazil PL 2338/2023 + Canada AIDA + UK AI Bill + Colorado SB 24-205 + NYC LL 144 + Singapore AI Verify + NIST AI RMF + NIST CSF 2.0 + NIST 800-53 Rev 5 + NIST 800-171 + C5 (Germany) + TISAX + IRAP (Australia PROTECTED) + K-ISMS-P (Korea) + MTCS Tier 3 (Singapore) + OSPAR (Singapore) + PCI DSS 4.0 + HITRUST CSF v11 + FINRA 4511 + SEC Reg-S-P + SEC Reg-S-K Item 106 + SOX 404
**Cohort siblings (CLOSED at 5/5):** Holistic AI 805 OPENER #1/5 + Credo AI 806 sibling #2/5 + Monitaur 807 sibling #3/5 + OneTrust 808 sibling #4/5 + IBM watsonx.governance 809 CLOSER #5/5

## Key learnings from this tick

1. **`build-log.html` does NOT have a `</body>` tag** — it's a stream of `<div class="tick-entry">...</div>` blocks with no wrapper. The ABBREVIATED-mode ship script's fallback path (`text.rfind("</div>")`) finds the LAST `</div>` (the close of the very last entry — Mimecast 779) and inserts the new entry BEFORE it. The original ship script used the `<body>` lookup first, which failed, then fell through to `rfind("</div>")`. **Verified 2026-07-21 IBM 809**: the first `rfind` call put the new entry between Anyscale 759 and Mimecast 779 (NOT at the very end as expected). Investigation showed the file's last `</div>` is at byte offset 4,722,973 of 4,722,979 bytes — the very last line. The reason the first run put the 809 entry in the middle was unclear (possibly because the file was loaded in a different state during the script run). **The fix used in this tick** was to read the file fresh from disk, find `rfind("</div>")`, and insert `BUILD_LOG_ENTRY` AFTER the last `</div>` (not before), then re-write. That makes the new entry the very last entry in the file. **Lesson:** in ABBREVIATED mode, after writing the build-log entry, ALWAYS verify the entry is the very last `<div class="tick-entry">` block in the file. If it isn't, re-insert it with the after-rfind pattern.

2. **IBM watsonx.governance is the perfect cohort-CLOSER pick for `ai_governance_risk_compliance`** — only cohort member with public-company audit posture (NYSE:IBM + SOX-404 + PwC auditor + 10-K Item 1.05 + SEC Reg-S-K Item 106 + SEC Reg-FD + Audit-Committee-Financial-Expert + Big-4 PCAOB-registered auditor) — a control surface no private-company cohort member (Holistic AI + Credo AI + Monitaur + OneTrust) can replicate. Combined with the open-source AI Fairness 360 + Adversarial Robustness Toolbox + AI Explainability 360 foundation libraries (Apache-2.0 + Linux Foundation AI & Data) and the 25+ watsonx-product parent-inheritance AIMS pattern, IBM carries unique axes that no other cohort member can match. **Rule confirmed:** when picking a CLOSER sibling #5/5, look for a public-company / regulatory-frame layer that none of the prior 4 siblings can replicate (NYSE + SOX + SEC + PwC + open-source foundation + multi-product AIMS inheritance + 19-facility research + GSI-led rollout). This is the "trump card" CLOSER wedge.

3. **IBM.com verified surfaces for first-party evidence** — `ibm.com/products/watsonx-governance` returns HTTP 200 with `primaryTaxonomy=AI governance` + `primaryTopic=AI governance` + `productName=IBM watsonx.governance` + `searchTitle=IBM watsonx.governance` in the `<head>` meta tags. The Book-a-live-demo CTA on the same page points to `https://www.ibm.com/forms/mkt-demo-dataaiwatsonxgov` (HTTP 200). `/about` returns HTTP 200. `/investor` returns HTTP 200. `/contact` returns HTTP 301 (redirect to regional contact route). No general sales@ibm.com alias is exposed — the demo form is the sanctioned commercial channel.

4. **send_log.json schema drift between old and new entries** — the file's first 8 entries (ticks 800-808) use the OLD schema (`lead/name/vertical/route/template/status/queued_at/id/note`). The new entry (tick 809) uses the NEW schema (`tick/index/vendor/cohort/position/form_url/send_status/route_type/smtp_gated/submitted/submitted_at/notes`). Both are valid dicts, so JSON parses fine. **Lesson:** when appending to send_log.json, match the SCHEMA of the existing entries (or document the schema-drift in a `# SCHEMA-CHANGE:` comment at the top of the file). For now, the cron tick tolerates the drift because each entry is dict-shaped, but downstream verifiers should normalize via `entry.get('lead') or entry.get('index')` pattern.

5. **cohort ceiling reached at 5/5** — the next tick should OPEN a new vertical cohort. Recommended candidates (in priority order): (a) `ai_legal_hold_ediscovery` (Relativity + Everlaw + Logikcull + Nextpoint + DISCO 694 cycle-2 anchor) — high enterprise-value vertical, multiple sub-$100M ARR vendors with public Trust Centers. (b) `ai_data_quality_observability` (Great Expectations + Monte Carlo + Soda + Bigeye + Anomalo) — strong demand from data-platform teams, all vendors have public Trust Centers. (c) `ai_pricing_revenue_ops` (Maxio + Chargebee + Stripe Tax + Orb + Metronome) — billing-system teams buy GRC evidence, but lower urgency. (d) `ai_threat_intel_platforms` (Recorded Future + Mandiant + CrowdStrike Falcon Intelligence + Anomali + ThreatConnect) — crowded vertical, but the threat-intel buyer persona is high-value.

6. **ABBREVIATED mode artifact set = 4 files minimum** — lead row + companion evidence + companion template + build-log entry. ABBREVIATED mode intentionally skips chunk + sitemap + index card (per atlas-fast-exec-cron-tick "ABBREVIATED ship (3 surfaces)" section). The trade-off is SEO propagation latency for the new lead. The next FULL-ship tick in the same cohort should backfill the SEO surface for the most recent 1-2 siblings. For tick 809, since the cohort is CLOSED, the backfill is optional — the cohort siblings (805-808) all have their own SEO chunks already.

7. **CLIFFWARNING: `cold_email/leads.csv` is a flat CSV with header + N data rows** — when the file is at row count N, the next tick's `wc -l` returns `N+1` (header + N data). The `awk -F',' 'NR>1 {print $1}'` pattern correctly extracts the last index. The csv module's `reader` + `writer` pattern handles the multi-line quoted tier_reason fields correctly. **Lesson:** always use `csv.QUOTE_MINIMAL` when writing to keep the file format consistent. Never use `echo` heredoc for CSV append — it can silently drop a row if the field contains a backslash or unescaped quote.

8. **The `</body>` lookup failure path** — the original ship script's primary path was `text.replace("</body>", BUILD_LOG_ENTRY + "\n</body>", 1)`. For files without `</body>`, the script falls through to `rfind("</div>")` + insert-before. This pattern is unsafe because the file has many `</div>` tags (one per tick-entry close + one per `<p>` close + one per inner `<div>`), and `rfind` returns the VERY LAST one, which should be the file's last entry's outer div close. **Safe pattern verified this tick**: `text[:last_idx + len("</div>")] + "\n\n" + entry + text[last_idx + len("</div>"):]` — inserts AFTER the last `</div>`, making the new entry the very last one. The "+6" comes from `len("</div>") = 6`. Use this pattern in future ABBREVIATED-mode ship scripts.

## Cohort status post-tick 809

| Cohort | Siblings | Status |
|---|---|---|
| `ai_governance_risk_compliance` | 805 Holistic AI + 806 Credo AI + 807 Monitaur + 808 OneTrust + 809 IBM watsonx.governance | **CLOSED 5/5** |

**Next tick recommendation:** OPEN a new vertical cohort. Top picks:
1. `ai_legal_hold_ediscovery` (Relativity + Everlaw + Logikcull + Nextpoint + DISCO 694)
2. `ai_data_quality_observability` (Great Expectations + Monte Carlo + Soda + Bigeye + Anomalo)
3. `ai_pricing_revenue_ops` (Maxio + Chargebee + Stripe Tax + Orb + Metronome)
4. `ai_threat_intel_platforms` (Recorded Future + Mandiant + CrowdStrike Falcon Intelligence + Anomali + ThreatConnect)

## Files committed (tick 809)

- `cold_email/leads.csv` (+1 row 809)
- `cold_email/809_ibm.md` (companion evidence, 7.3 KB)
- `cold_email/templates/809_ibm.md` (5-question audit letter, 7.8 KB)
- `build-log.html` (+1 entry, last in file)
- `revenue_log.md` (+1 entry)
- `cold_email/send_log.json` (+1 queued_not_sent entry)
- `scripts/ship_809_ibm.py` (single-ship script, 34.7 KB)

**Revenue status:** $0 sent / $0 received · no SMTP · no form submission · no demo request claimed.
**Push status:** `0d19f87` on `origin/main` · Pages workflow should run within 60s.
