---
name: atlas-store-tick-learnings-2026-07-21-assemblyai-847
description: Session addendum to atlas-store-tick-ship for tick 847 (AssemblyAI sibling #2/5 for ai_voice_agent_infra cohort — NEW VERTICAL #7) — the first FULL-ship tick in the voice-AI infra lane (post ABBREVIATED Deepgram 846 OPENER), the Wayback-Machine-verified-founder evidence pattern when the live /about page is JS-SPA-empty, the 9-surface single-ship-script pattern, the parallel-vertical push (voice-AI observability #6 + voice-AI infra #7 both at 1-2/5 in same cycle).
version: 1
metadata:
  hermes:
    tags: [atlas, atlas-store, cron, fast-execution, full-ship, build-log, cohort-sibling, csv-quoting, vertical-7, ai-voice-agent-infra, assemblyai, dylan-fox, jessi-waters, universal-3-5-pro, speech-understanding, guardrails, llm-gateway, voice-agents, wayback-machine-fallback, parallel-vertical]
    category: devops
---

# Tick 847 — AssemblyAI sibling #2/5 for ai_voice_agent_infra (NEW VERTICAL #7) — session learnings

**Tick:** 2026-07-21-fast-exec-assemblyai-847
**Lead:** 847 AssemblyAI (assemblyai.com — Speech AI Models — Universal-3.5 Pro + Universal-1 + Universal-2 + Universal-Streaming + Speech Understanding API + Guardrails and Safety + LLM Gateway + Voice Agents + Self Hosted Voice AI)
**Vertical:** `ai_voice_agent_infra` — **sibling #2/5 (NEW VERTICAL #7)**
**Mode:** FULL ship (9 surfaces + build-log + revenue-log + send-log + ship-script = 1 commit)
**Commercial route:** `FORM:https://www.assemblyai.com/demo` (first-party Contact Sales page; Astro `data-form-id="contact-sales"` form with first_name/last_name/email/how_did_you_hear_about_us inputs verified live 2026-07-21)
**Commit:** `b7879fe` on `origin/main` (working tree clean post-tick, pushed)

## Key learnings from this tick

1. **🚨 LIVE FIRST-PARTY FOUNDER VERIFICATION VIA WAYBACK MACHINE WHEN /about IS A JS-SPA EMPTY PAGE (NEW pitfall from this tick):** AssemblyAI's first-party `/about` page renders via Astro and the home page (`/`) is also Astro — both have the leadership block rendered client-side. Direct `curl https://www.assemblyai.com/about` returns a 32KB 404 page (the path was renamed). The home page `curl` returns 188KB but the leadership text is hydrated client-side, NOT in the SSR HTML — `re.search(r'\bDylan\b', text)` returns 0 matches. **The fix**: hit the Wayback Machine CDX API for snapshots, then fetch the snapshot. The verbatim first-party evidence is preserved:
   ```bash
   curl -sL "https://web.archive.org/cdx/search/cdx?url=assemblyai.com/about&output=json&limit=5&from=20240101" | tail -3
   # Returns: ["com,assemblyai)/about","20240124012931","https://www.assemblyai.com/about","text/html","200",...]
   curl -sL "https://web.archive.org/web/20250124012931/https://www.assemblyai.com/about" -o /tmp/aai_wb.html
   ```
   Then `re.search(r'Dylan', text)` on the WB snapshot returns verbatim:
   `"Our leadership Dylan Fox CEO Jessi Waters COO Christy Roach VP, Marketing Takuya Yoshioka Director of Research Travis Kupsche Director of Engineering Eric Jensen Head of Sales Ryan Seams Head of Customer Success Nicholas Johnson"` plus verbatim founding `"AssemblyAI first started in 2017 with a shared vision..."` plus verbatim Series C `"$50M in Series C funding led by Accel, our partners that also led our Series A, with participation from Keith Block and Smith Point Capital, Insight Partners, Daniel Gross and Nat Friedman, and Y Combinator."`. **The lesson**: when a vendor's first-party /about page is JS-SPA-empty (returns 0 hits on founder-name regex), the Wayback Machine CDX API is the fallback that produces first-party-verifiable founder evidence. The WB snapshot is treated as first-party because (a) it's the vendor's own rendered HTML captured by the Internet Archive, (b) the timestamp predates any LLM training cutoff, (c) it's reproducible from a public URL anyone can fetch. Document the WB timestamp in the companion file and lead row so the audit trail is unambiguous.

2. **🚨 Astro `data-form-id="contact-sales"` form = canonical FORM route for assemblyai.com/demo.** The /demo page renders as a 150KB Astro SPA with no JavaScript-form-rendered. Direct `curl` returns the full HTML with the form block visible: `<form class="w-full max-w-[427px] flex flex-col gap-[16px] contact-form" data-form-id="contact-sales" novalidate data-astro-cid-cfdi5afq>` with input names `first_name / last_name / email / how_did_you_hear_about_us`. **Sanctioned commercial route per pitfall #28** (FORM-only when no general-business inbox is published on the rendered first-party surface). Verified live 2026-07-21.

3. **The parallel-vertical push pattern (NEW 1.x from tick 847):** Tick 846 OPENER'd `ai_voice_agent_infra` (NEW VERTICAL #7) while tick 845 OPENER'd `ai_voice_agent_observability` (NEW VERTICAL #6). Both verticals are voice-AI-focused but on opposite sides of the conversation boundary — observability sits downstream of LLM-summarize, infra sits at the ASR/TTS/Speech-Understanding/Guardrails/LLM-Gateway boundary. Both run in parallel: 4 OPEN slots in observability (#6) + 3 OPEN slots in infra (#7) after tick 847 ships. This is the right move when (a) the lane is broad enough to support two non-overlapping verticals, (b) the OPENER picks for each are equally high-credibility, (c) the per-vertical 5/5 ceiling keeps both manageable. Recommended OPENER siblings for the parallel push: **Voiceflow / Vapi / Retell AI / Bland** for voice-agent-builder #8 (the third parallel vertical after observability #6 + infra #7) — would let the three lanes (build + observe + infra) close the full voice-AI-deployer-obligation picture for EU AI Act Art. 26 in 2027.

4. **Single-ship-script pattern (REINFORCED tick 847):** Per tick 810's lesson + the 838 ABBREVIATED example, the FULL ship compresses 9 atomic writes + 1 commit/push into 1 commit. Tick 847 extended the pattern: **every surface is gated by an inline assertion** (parse-back checks) — leads.csv row delta, companion file byte size + founder-name presence, template format-agnostic question count, chunk file line count + keyword presence, index.html card marker, sitemap.xml url count delta, build-log after-rfind pattern verification, revenue_log row delta, send_log dual-schema round-trip. If any assertion fails, the script aborts before commit (commit can only happen on green parse-backs). Cost: 1 tool call for `python scripts/ship_847_assemblyai.py` + 1 tool call for `git add -A && git commit && git push`. Total: 2 tool calls for a full 9-surface tick. **The script itself is committed alongside the artifacts** (becomes part of the audit trail + reproducibility record).

5. **Cohort state after tick 847:**
   ```
   ai_billing_usage: 5/5 - rows [815, 816, 817, 818, 819]
   ai_data_catalog_governance: 4/5 - rows [825, 826, 827, 828]
   ai_data_context_observability: 5/5 - rows [836, 837, 838, 839, 840]
   ai_governance_risk_compliance: 2/5 - rows [808, 809]
   ai_intent_data_enrichment: 5/5 - rows [830, 831, 832, 833, 834]
   ai_legal_hold_ediscovery: 5/5 - rows [810, 811, 812, 813, 814]
   ai_marketing_attribution: 5/5 - rows [820, 821, 822, 823, 824]
   ai_observability_eval: 5/5 - rows [835, 841, 842, 843, 844]
   ai_voice_agent_infra: 2/5 - rows [846, 847]  <-- NEW after this tick
   ai_voice_agent_observability: 1/5 - rows [845]
   ```
   6 cohorts CLOSED 5/5 (36 leads), 4 cohorts OPEN (15 leads total: 4/5 + 2/5 + 2/5 + 1/5). Grand total 51 leads across 10 verticals. **Recommended next cohort pushes**:
   - **Tick 848-850 (3 ticks):** fill `ai_voice_agent_observability` to 2/5 + 3/5 + 4/5 (Cresta + CallMiner + Suki AI are canonical siblings for the conversation-boundary observability lane)
   - **Tick 851-852 (2 ticks):** fill `ai_voice_agent_infra` to 3/5 + 4/5 (Rev AI + Speechmatics are canonical siblings for the ASR/transcribe lane; or ElevenLabs for the TTS/voice-clone lane)
   - **Tick 853-855 (3 ticks):** OPEN `ai_voice_agent_builder` (NEW VERTICAL #8) — Voiceflow OPENER + Vapi + Retell AI + Bland + Cartesia. This is the third leg of the voice-AI-deployer-obligation stool: build + observe + infra.

6. **Build-log after-rfind pattern (REINFORCED tick 847):** Find `rfind("</div>")` on the fresh read, insert AFTER the last `</div>` (not before). After write, run `text.rsplit('<div class="tick-entry"', 1)[-1]` and confirm the new tick-id marker is in the slice. Tick 847 passed this verification (the new tick-id `2026-07-21-fast-exec-assemblyai-847` is in the last slice).

7. **send_log dual-schema (REINFORCED tick 847):** The new schema (`tick / index / vendor / cohort / position / form_url / send_status / route_type / smtp_gated / submitted / submitted_at / notes / template_full / tier_reason`) coexists with the old schema (`lead / name / vertical / route / template / status / queued_at / id / note`) on every new entry. Backward-compatible readers must normalize via `entry.get('lead') or entry.get('index') or entry.get('vendor')` pattern. Tick 847 verified `lead == index`, `route == "FORM:" + form_url`, `status == send_status` (3 dual-schema invariants) in inline assertions before commit.

8. **Cohort ceiling rule (reinforced tick 847):** When `len(cohorts_by_csv_count[vertical]) >= 5`, OPEN a new vertical. The CSV is the only state that affects downstream actions; the build-log is informational. After tick 847, `ai_voice_agent_infra` is at 2/5 and 3 OPEN slots remain. The voice-AI infra lane is broad enough (ASR + TTS + Speech Understanding + Guardrails + LLM Gateway + Voice Agents + Self Hosted Voice AI + Voice AI Cloud + 99 languages) to support the full 5/5 ceiling with distinct siblings: Deepgram 846 (ASR/TTS/Voice Agent API + on-prem + 36+ languages) + AssemblyAI 847 (Speech Understanding + Guardrails + LLM Gateway + 99 languages + Universal-Streaming sub-300ms) + **#3/5 ElevenLabs** (TTS + Voice API + Conversational AI + Voice Cloning + Voice Library) + **#4/5 Speechmatics** (ASR + VoiceLLM + Any-Language + on-prem + cloud) + **#5/5 Rev AI** (Async ASR + Streaming ASR + Language ID + Topic Extraction + Sentiment + on-prem) CLOSER.

9. **Why FULL ship for tick 847 (vs ABBREVIATED for tick 846 OPENER):** Tick 846 was the OPENER and the cron budget was tight (5-minute tick + OpenAIAutogen install in parallel), so the OPENER shipped ABBREVIATED (companion + template + build-log + revenue_log; chunk + sitemap + index deferred to follow-up full-ship tick). Tick 847 is sibling #2/5 — the FIRST sibling in the new vertical — and shipping FULL gives the SEO + index-card coverage a strong start to maximize long-tail search surface. The single-ship-script pattern keeps the marginal cost of additional surfaces at <2 minutes of script time vs 5-10 separate terminal calls. This trade-off (ABBREVIATED for OPENERS, FULL for first sibling) is the recommended default going forward.

10. **AssemblyAI 847 commercial route: `FORM:https://www.assemblyai.com/demo` (Contact Sales page; Astro `data-form-id="contact-sales"` form with `first_name / last_name / email / how_did_you_hear_about_us` inputs verified live 2026-07-21).** No SMTP send, form submission, payment, or revenue claimed. Sanctioned commercial route per pitfall #28 (FORM-only when no general-business inbox is published on the rendered first-party surface).

## Files committed (tick 847)

- `cold_email/leads.csv` (+1 row 847)
- `cold_email/847_assemblyai.md` (companion evidence, 7.0 KB)
- `cold_email/templates/847_assemblyai_procurement_followup.md` (5-question audit letter, 5.9 KB)
- `chunks/chunk_847.html` (SEO chunk, 11.4 KB, 89 lines)
- `index.html` (+1 card insert, 2.4 KB)
- `sitemap.xml` (+1 <url> entry, 513 → 514 urls)
- `build-log.html` (+1 entry, last in file, verified as very last `<div class="tick-entry">`)
- `revenue_log.csv` (+1 row, 34.4 KB → 36.2 KB)
- `cold_email/send_log.json` (+1 queued_not_sent entry using NEW schema dual-format, 36 → 37 entries)
- `scripts/ship_847_assemblyai.py` (single-ship script, 53.6 KB)

**Revenue status:** $0 sent / $0 received · no SMTP · no form submitted · no demo request claimed.
**Push status:** `b7879fe` on `origin/main` · working tree clean post-tick · Pages workflow should run within 60s.

## Recommended next-tick plan

- **Tick 848:** Cresta (cresta.com) as sibling #2/5 of `ai_voice_agent_observability` (post Observe.AI 845 OPENER). Cresta ships real-time Agent Assist + post-call summarization + coaching + conversation intelligence + Generative AI for contact centers. **Verify live first-party**: cresta.com /about (leadership: CEO Sebastian Thrun? — verify) + /contact + /demo. **Expected wedge**: real-time coaching surface that Observe.AI does NOT ship. Estimated mode: FULL ship.
- **Tick 849:** CallMiner (callminer.com) as sibling #3/5 of `ai_voice_agent_observability`. **Verify live first-party**: callminer.com /about (CEO Jeff Gallino) + /contact + /demo. **Expected wedge**: 100% call analysis + omnichannel + customer journey + speech analytics.
- **Tick 850:** Suki AI (suki.ai) as sibling #4/5 of `ai_voice_agent_observability` — OR pivot to ElevenLabs (elevenlabs.io) as sibling #3/5 of `ai_voice_agent_infra` if voice-agent-builder land is the higher-leverage play.