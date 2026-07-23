"""ship_1122_helicone_audit_export_engineering_followup.py — tick 1122.

Tick 1122 — Helicone ai_agent_audit_export engineering + observability follow-up.

Persona-unique angle vs existing cohort follow-ups:
 - 1120 (Confident AI / DeepEval / finance-renewal) joins per-line cost-of-ownership
 - 1121 (Confident AI / DeepEval / security-GRC) joins BYOK + AES-256 + retention + isolation
 - 1122 (THIS / Helicone / engineering-observability) joins OpenTelemetry GenAI semantic-conventions
   portable exporter + per-tenant OTLP endpoint + per-span attribute replay +
   signal-quality / completeness-of-replay / cross-OTEL-backend portability.

Helicone is the canonical helicone.ai gateway/observability lead (existing lead 1066).
This is a follow-up frame anchored to the closed ai_agent_audit_export NEW VERTICAL #40
(Arize AI 1114 + Maxim AI 1115 + LangSmith 1117 + Langfuse 1118 + Confident AI DeepEval 1119).
No duplicate lead row.

ABBREVIATED ship: 1 surface (single follow-up template) + build-log + revenue_log entry.
No new chunk / sitemap / index card this tick — those deferred to a future follow-up full-ship tick.
"""
import csv
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(r"C:\\Users\\Potts\\projects\\atlas-store")
LEAD_INDEX = "1122"
TICK_ID = "2026-07-24-fast-exec-helicone-audit-export-engineering-followup-1122"
COHORT = "ai_agent_audit_export"
VENDOR = "Helicone"
DOMAIN = "helicone.ai"
FORM_URL = "https://www.helicone.ai/contact"
HANDLE = "@helicone"
TEMPLATE_NAME = "1122_helicone_audit_export_engineering_followup.md"
TPL = ROOT / "cold_email" / "templates" / TEMPLATE_NAME
RL = ROOT / "cold_email" / "revenue_log.csv"
BL = ROOT / "build-log.html"
ANCHOR_LEAD = "1066"  # existing Helicone gateway lead
COHORT_CLOSER = "1119"  # Confident AI DeepEval CLOSER #5/5

# ---------- 1. Write template file ----------
TPL_TEXT = f"""# Helicone ai_agent_audit_export engineering + observability follow-up

**Vertical:** `ai_agent_audit_export` (follow-up frame; existing Helicone gateway lead {ANCHOR_LEAD} is NOT duplicated)
**Tick:** `{TICK_ID}`
**Buyer frame:** Engineering lead / Staff SRE / Platform observability lead / OpenTelemetry / OTLP collector owner who needs the Helicone gateway audit_export to be replay-portable across OTEL backends (Honeycomb + Datadog + Grafana Tempo + Jaeger + SigNoz + New Relic + Dynatrace + ClickHouse + Phoenix + Langfuse + Arize) without rewriting instrumentation
**Cohort anchor:** `ai_agent_audit_export` NEW VERTICAL #40 — closed at 5/5 (Arize AI {ANCHOR_LEAD if False else '1114'} + Maxim AI 1115 + LangSmith 1117 + Langfuse 1118 + Confident AI DeepEval {COHORT_CLOSER}); Helicone engineering follow-up at tick 1122

**Three subject options (pick one)**

1. `Helicone audit_export replay — can one gateway request reconcile to OTEL GenAI semantic-convention spans across 4 backends?`
2. `Portable Helicone exporter for OTel collectors: one request, four OTEL backends, byte-identical spans`
3. `Helicone engineering handoff: per-tenant OTLP endpoint + per-span attribute replay + signal-quality report`

**Paragraph 1 — why the engineering + observability buyer.** Helicone (helicone.ai — Y Combinator W22 — self-serve + AI Gateway + LLM Observability platform — OpenAI-compatible unified API to 100+ models — automatic logging + observability + fallbacks + unified billing + sessions + alerts + evaluations + per-tenant custom properties + per-request caching + per-tenant rate limits + per-user rate limits + per-tenant cost caps + SOC 2 Type II + HIPAA + per-region self-hosted AI Gateway option) the canonical `ai_agent_audit_export` follow-up is the engineering handoff: *one Helicone gateway request must produce a portable OTEL GenAI-semantic-convention span row that any OTEL backend ingests natively with no per-vendor re-instrumentation.* The first-party AI Gateway pipes every provider request through a deterministic per-request envelope; the engineering follow-up is the exporter that takes that envelope and lands it byte-identically in Honeycomb + Datadog + Grafana Tempo + New Relic without rewriting instrumentation. The cohort-unique engineering wedge is the *portability of the exporter itself* — not the contents of the audit_export (which the Langfuse 1118 + LangSmith 1117 + Confident AI 1119 follow-ups already pin).

**Paragraph 2 — what the OTEL GenAI portability pack joins.** Per Helicone gateway request, the OTEL portability row joins: (1) `tenant_id` + (2) `helicone_workspace_id` + (3) `helicone_request_id` + (4) `session_id` + (5) `user_id` + (6) `provider` + (7) `model` + (8) `model_version` + (9) `gen_ai.system` + (10) `gen_ai.request.model` + (11) `gen_ai.request.max_tokens` + (12) `gen_ai.request.temperature` + (13) `gen_ai.usage.input_tokens` + (14) `gen_ai.usage.output_tokens` + (15) `gen_ai.response.id` + (16) `gen_ai.response.finish_reasons` + (17) `cache_hit` + (18) `retry_count` + (19) `fallback_chain_id` + (20) `rate_limit_policy_id` + (21) `cost_usd` + (22) `latency_ms` + (23) `status_code` + (24) `otel.exporter.endpoint` + (25) `otel.exporter.protocol` (http/protobuf vs grpc) + (26) `otel.resource.attributes` (service.name + service.version + deployment.environment) + (27) `otel.span.attribute_set_hash` + (28) `cross_tenant_no_bleed_proof` + (29) `audit_export_id` + (30) `replay_portability_score` (0-1 across OTEL backends tested). Five evidence questions the engineering portability pack answers in 48 hours:

1. Which OTEL GenAI semantic-convention attributes does Helicone emit per-request (gen_ai.system / gen_ai.request.model / gen_ai.usage.input_tokens / gen_ai.response.finish_reasons / etc.) and which are derived vs first-party?
2. Can one Helicone request be exported byte-identically to Honeycomb + Datadog + Grafana Tempo + New Relic via OTLP without per-vendor translation adapters?
3. What is the per-tenant OTLP endpoint + per-tenant API key + per-tenant header routing strategy Helicone ships, and does it preserve the cross-tenant-no-bleed boundary across all four backends?
4. What is the replay_portability_score per backend (number of OTEL attributes ingested / number of OTEL attributes emitted) and which attributes are dropped by each backend?
5. Can the engineering team reproduce an operational incident (cache-miss-storm + fallback-spike + rate-limit-throttle) from the per-span attribute replay alone, without re-running the request?

**Paragraph 3 — offer.** $500 / 48h fixed-scope Helicone OTEL GenAI-portability pack for one Helicone gateway request class against your three reference OTEL backends; OR $497/month quarterly refresh that re-runs the five-question portability report after every Helicone AI Gateway version bump, every OTEL backend version bump, every OTEL GenAI semantic-convention spec revision, every per-tenant header-routing change, and every rate-limit-policy addition; OR $2,000 five-vendor benchmark across Arize AI + Maxim AI + LangSmith + Langfuse + Confident AI joined with the 20-column replay-portable audit_export schema from `chunks/chunk_1113.html`, then OTEL-ingested via the same exporter to compare portability across the five cohorts.

**Five evidence questions the OTEL portability pack answers in 48 hours** (operationalized): (1) what is the per-attribute replay rate Honeycomb / Datadog / Grafana Tempo / New Relic / SigNoz / Dynatrace each gives back from one Helicone gateway request; (2) which OTEL GenAI semantic-convention attributes are dropped or renamed by each backend; (3) which per-tenant header-routing strategy Helicone ships out-of-the-box vs which the customer must implement; (4) what is the per-tenant cross-tenant-no-bleed invariant when multiple tenants share the same OTLP endpoint; (5) which operational-incident class (cache-storm + fallback-spike + rate-limit-throttle + prompt-injection-flag + cost-cap-trigger) is replayable from the OTEL span alone.

**First-party route:** `mailto:contact@helicone.ai` on the Helicone homepage + `FORM:{FORM_URL}` (HTTP 200 verified live 2026-07-24); neither is submitted. SOP:#28 — no guessed general-business inbox; first-party routes only.

**No duplicate lead row.** Helicone gateway lead is {ANCHOR_LEAD}. This 1122 artifact is a differentiated audit-export engineering follow-up frame anchored to the closed cohort #40 — same vertical, different buyer, different exporter technology.

**No email or form submitted; SMTP/form gated; $0 sent / $0 received.**
"""

TPL.write_text(TPL_TEXT, encoding="utf-8")
post_tpl = TPL.read_text(encoding="utf-8")
assert "Helicone" in post_tpl, "template must mention Helicone"
assert "OpenTelemetry" in post_tpl or "OTEL" in post_tpl, "template must mention OTEL"
assert "gen_ai" in post_tpl, "template must mention gen_ai semantic-convention attrs"
assert "Subject" in post_tpl or "subject" in post_tpl, "template must have subject options"
assert "Paragraph 1" in post_tpl and "Paragraph 2" in post_tpl and "Paragraph 3" in post_tpl, "template must have 3 paragraphs"
assert "Five evidence questions" in post_tpl, "template must have 5 evidence questions"
assert FORM_URL in post_tpl
assert ANCHOR_LEAD in post_tpl
assert "no duplicate" in post_tpl.lower() or "NOT duplicated" in post_tpl, "template must declare no duplicate lead row"
print(f"[ok] template file written: {TPL.name} ({len(post_tpl)} bytes)")

# ---------- 2. revenue_log.csv row ----------
pre_rl = RL.read_text(encoding="utf-8")
RL_ROW = (
    f'2026-07-24,tick-1122,{TEMPLATE_NAME},DEFERRED,ai_agent_audit_export followup,0,'
    f'"Tick 1122 Helicone ai_agent_audit_export engineering + observability follow-up for closed NEW VERTICAL #40 (cohort: Arize AI 1114 + Maxim AI 1115 + LangSmith 1117 + Langfuse 1118 + Confident AI DeepEval 1119 CLOSER; no duplicate Helicone lead row — existing helicone.ai gateway lead is {ANCHOR_LEAD}). Persona-unique engineering angle: OTEL GenAI semantic-convention portable exporter + per-tenant OTLP endpoint + per-span attribute replay + signal-quality completeness-of-replay score across Honeycomb + Datadog + Grafana Tempo + New Relic + cross-tenant-no-bleed proof. 30-column OTEL portability receipt joins tenant_id + helicone_workspace_id + helicone_request_id + session_id + user_id + provider + model + model_version + gen_ai.system + gen_ai.request.model + gen_ai.request.max_tokens + gen_ai.request.temperature + gen_ai.usage.input_tokens + gen_ai.usage.output_tokens + gen_ai.response.id + gen_ai.response.finish_reasons + cache_hit + retry_count + fallback_chain_id + rate_limit_policy_id + cost_usd + latency_ms + status_code + otel.exporter.endpoint + otel.exporter.protocol + otel.resource.attributes + otel.span.attribute_set_hash + cross_tenant_no_bleed_proof + audit_export_id + replay_portability_score. 5 evidence questions: (1) which OTEL GenAI semantic-convention attributes does Helicone emit per-request; (2) can one Helicone request be exported byte-identically to 4 OTEL backends without per-vendor translation; (3) which per-tenant OTLP endpoint + header-routing strategy preserves cross-tenant-no-bleed; (4) which attributes are dropped/renamed by each backend; (5) which operational-incident class is replayable from the OTEL span alone. First-party route mailto:contact@helicone.ai + FORM:{FORM_URL} verified live 2026-07-24 NOT submitted; SMTP/form gated; 0 sent / 0 received. [tick-1122-helicone-audit-export-engineering-followup]\\n'
)
with RL.open("a", encoding="utf-8", newline="") as f:
    f.write(RL_ROW)
post_rl = RL.read_text(encoding="utf-8")
assert len(post_rl) > len(pre_rl), "revenue_log.csv should have grown"
assert "tick-1122" in post_rl.split("\n")[-2] or "tick-1122" in post_rl.split("\n")[-1], f"last line of revenue_log should mention tick-1122"
print(f"[ok] revenue_log.csv row appended ({len(pre_rl)} -> {len(post_rl)} bytes)")

# ---------- 3. build-log.html entry ----------
pre_bl = BL.read_text(encoding="utf-8")
# build-log.html uses <article class="tick-entry"> ... </article> for entries
last_div_idx = pre_bl.rfind("</article>")
if last_div_idx == -1:
    last_div_idx = pre_bl.rfind("</div>")
assert last_div_idx != -1, "build-log.html has no </article> or </div> at all"

NEW_ENTRY = f"""
<article class="tick-entry" id="tick-1122" data-tick="{TICK_ID}" data-cohort="{COHORT}" data-cohort-role="follow-up-engineering-observability"><h3>tick 1122: 2026-07-24 — Helicone ai_agent_audit_export engineering + observability follow-up</h3><p><strong>Artifact:</strong> shipped <code>cold_email/templates/{TEMPLATE_NAME}</code>, a three-subject engineering + OTEL-portability follow-up template for the closed NEW VERTICAL #40 ai_agent_audit_export cohort (Arize AI 1114 + Maxim AI 1115 + LangSmith 1117 + Langfuse 1118 + Confident AI DeepEval 1119 CLOSER).</p><p><strong>Progress:</strong> closes the engineering + observability gap in the closed cohort ladder. Persona-unique vs existing follow-ups: 1120 (Confident AI / finance-renewal) joins per-line cost-of-ownership; 1121 (Confident AI / security-GRC) joins BYOK + AES-256 + retention + isolation; 1122 (Helicone / engineering-observability) joins OpenTelemetry GenAI semantic-convention portable exporter + per-tenant OTLP endpoint + per-span attribute replay + signal-quality completeness-of-replay score + cross-tenant-no-bleed proof across Honeycomb + Datadog + Grafana Tempo + New Relic + SigNoz + Dynatrace. 30-column OTEL portability receipt joins tenant_id + helicone_workspace_id + helicone_request_id + session_id + user_id + provider + model + model_version + gen_ai.system + gen_ai.request.model + gen_ai.request.max_tokens + gen_ai.request.temperature + gen_ai.usage.input_tokens + gen_ai.usage.output_tokens + gen_ai.response.id + gen_ai.response.finish_reasons + cache_hit + retry_count + fallback_chain_id + rate_limit_policy_id + cost_usd + latency_ms + status_code + otel.exporter.endpoint + otel.exporter.protocol + otel.resource.attributes + otel.span.attribute_set_hash + cross_tenant_no_bleed_proof + audit_export_id + replay_portability_score.</p><p><strong>5 evidence questions the OTEL portability pack answers in 48 hours:</strong> (1) which OTEL GenAI semantic-convention attributes does Helicone emit per-request; (2) can one Helicone request be exported byte-identically to 4 OTEL backends without per-vendor translation; (3) which per-tenant OTLP endpoint + header-routing strategy preserves cross-tenant-no-bleed; (4) which attributes are dropped/renamed by each backend; (5) which operational-incident class (cache-storm + fallback-spike + rate-limit-throttle + prompt-injection-flag + cost-cap-trigger) is replayable from the OTEL span alone.</p><p><strong>No duplicate lead row.</strong> Existing Helicone gateway lead is {ANCHOR_LEAD} (ai_agent_llm_gateway sibling #1/5 cohort). This 1122 artifact is a differentiated audit-export engineering follow-up frame anchored to the closed cohort #40 — same vertical, different buyer, different exporter technology.</p><p><strong>Pivot:</strong> authenticated SMTP/forms remain gated, so no outreach was submitted and no delivery, payment, or revenue is claimed; $0 sent / $0 received. ABBREVIATED ship (1 template + build-log + revenue_log) — no new SEO chunk / sitemap / index card this tick; those deferred to a future follow-up full-ship tick.</p></article>
"""

post_bl = pre_bl[: last_div_idx + len("</article>")] + "\n\n" + NEW_ENTRY + pre_bl[last_div_idx + len("</article>"):]
BL.write_text(post_bl, encoding="utf-8")
last_slice = post_bl.rsplit('<article class="tick-entry"', 1)[-1]
assert TICK_ID in last_slice, f"new tick-id {TICK_ID} not in last-entry slice — mid-file insertion"
print(f"[ok] build-log entry appended (pre {len(pre_bl)} -> post {len(post_bl)} bytes)")

# ---------- 4. git add + commit + push ----------
print("\n[commit] git add -A && git commit && git push origin main")
git = subprocess.run(
    ["git", "add", "-A"],
    cwd=str(ROOT),
    capture_output=True,
    text=True,
)
print(git.stdout)
print(git.stderr, file=sys.stderr)

status = subprocess.run(
    ["git", "status", "--short"],
    cwd=str(ROOT),
    capture_output=True,
    text=True,
)
print("[git status]", status.stdout)

commit = subprocess.run(
    ["git", "commit", "-m", f"tick-1122: Helicone ai_agent_audit_export engineering + observability follow-up (NEW VERTICAL #40 cohort-anchored; no duplicate lead row; SMTP/form gated)"],
    cwd=str(ROOT),
    capture_output=True,
    text=True,
)
print(commit.stdout)
print(commit.stderr, file=sys.stderr)

push = subprocess.run(
    ["git", "push", "origin", "main"],
    cwd=str(ROOT),
    capture_output=True,
    text=True,
)
print(push.stdout)
print(push.stderr, file=sys.stderr)

# ---------- summary ----------
print(f"\n=== TICK {TICK_ID} SUMMARY ===")
print(f"template: {TEMPLATE_NAME} ({len(post_tpl)} bytes)")
print(f"cohort: {COHORT} NEW VERTICAL #40 (closed 5/5) — follow-up frame")
print(f"anchor lead: {ANCHOR_LEAD} (existing Helicone gateway lead, not duplicated)")
print(f"persona-unique angle: engineering + OTEL GenAI portability (vs 1120 finance + 1121 security/GRC)")
print(f"OUT: $500/48h + $497/mo + $2,000 5-vendor benchmark")
print("STATUS: SMTP/form gated, $0 sent / $0 received")
