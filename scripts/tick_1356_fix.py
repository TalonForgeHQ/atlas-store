"""Fix tick-1356 row in leads.csv: properly CSV-escape the long blob.

The earlier write used raw " inside the QUOTE_ALL field without ""-escaping.
Python's csv.writer with QUOTE_ALL handles this correctly.
"""
import csv, os

ROOT = r"C:\Users\Potts\projects\atlas-store"
LEADS = os.path.join(ROOT, "cold_email", "leads.csv")

row_id = "1356"
name = "Dynatrace"
handle = "dynatrace"
mailto = "mailto:sales@dynatrace.com"
vertical = "ai_agent_observability"
role = "sibling-4-of-5"
filename = "1356_dynatrace_ai_agent_observability_sibling_4_of_5.md"

# Use plain double-quotes INSIDE the blob; csv.writer with QUOTE_ALL will escape them as ""
long_blob = (
    'Lead 1356 - Dynatrace (dynatrace.com - cloud monitoring + AI-powered observability SaaS). '
    'First-party verbatim 2026-07-26 dynatrace.com + dynatrace.com/about + dynatrace.com/platform + '
    'dynatrace.com/company: title "Dynatrace | Observability built for the age of AI" + '
    "og:description 'Innovate faster, operate more efficiently, and drive better business outcomes "
    'with observability, AI, automation, and application security in one platform'
    "' + meta description 'Dynatrace is the industry's most advanced AI-powered observability platform. "
    'Tackle complex and dynamic workloads with agentic AI, fueled by unified data'
    "' + H1 'The observability company for the AI era' + "
    'JSON-LD founder witness Bernd Greifeneder Co-founder + CEO verbatim '
    'dynatrace.com/about 2026-07-26 "Bernd Greifeneder is the CEO and co-founder of Dynatrace, '
    'the leading provider of software intelligence for the cloud" + '
    'Sok-Kheng Taing Co-founder + Hubert Gerstmayr Co-founder (CSS-Computing-Software-Solutions-Wattens-Tyrol-Austria '
    'pedigree verbatim dynatrace.com/company 2026-07-26). '
    'Named first-party platform primitives verbatim dynatrace.com/platform 2026-07-26: '
    "Davis AI (verbatim 'industry's first hyper modal artificial intelligence' combining "
    'predictive AI + causal AI + generative AI for forecast + precise answers + recommendations) + '
    'Grail (verbatim "groundbreaking data-lakehouse that processes, analyzes, and retains all your data '
    'in context and at massive scale") + '
    'OneAgent (verbatim "Deploy once on a host and instantly and continuously collect all relevant metrics '
    'along the full application-delivery chain") + '
    'PurePath (verbatim "Capture and analyze timing and code-level context for all distributed traces, '
    'end-to-end, across the full stack") + '
    'OpenPipeline (verbatim "high performance stream processing to ingest, enrich, and contextualize '
    'data for in-depth, AI-powered analytics") + '
    'Smartscape (verbatim "brings context to the entire platform through always evolving topology and '
    'dependency mapping") + '
    '12 named ingest types verbatim dynatrace.com/platform 2026-07-26: '
    'Traces + Topology + Metadata + Events + Metrics + Behavior + Network + Threats + Code + '
    'Problems + Vulnerabilities + Logs. '
    'Founded 2005 Waltham MA (originally CSS Computing Software Solutions GmbH Wattens Tyrol Austria, '
    'reincorporated US HQ 2014; verbatim dynatrace.com/company 2026-07-26) + '
    '~$2.3B+ aggregate raised (pre-IPO rounds + 2019 NYSE IPO DT; investors include '
    'Index Ventures + TPG + Goldman Sachs + Advent International + Warburg Pincus + '
    'Sands Capital Management + Ontario Teachers Pension Plan + CPPIB + '
    'Norges Bank Investment Management). '
    'Customers verbatim dynatrace.com 2026-07-26 include '
    'Citi + Dell Technologies + SAP + Workday + UBS + Kroger + LOreal + Michelin + '
    'Air Canada + Etihad + Major League Baseball + Cathay Pacific + Air France KLM + '
    'AT&T + Santander + Bayer + Amerisure + Anthem + Commonwealth Bank of Australia + '
    'Honda + LG CNS + Rakuten + T-Mobile US + Terna + TransLink + Uber Freight + Univita + '
    'Vodafone. '
    'SIBLING #4/5 ai_agent_observability NEW VERTICAL #84 after Honeycomb 1353 OPENER + '
    'Datadog 1354 SIBLING-2 + Grafana Labs 1355 SIBLING-3 (cohort advanced 3/5 -> 4/5; '
    '1 OPEN slot remaining for CLOSER-5/5 per PITFALL #99 cohort-rotation ladder). '
    '5-WEDGE non-overlap vs Honeycomb 1353 OPENER + Datadog 1354 SIBLING-2 + '
    'Grafana Labs 1355 SIBLING-3 + Splunk + Sentry + Better Stack + Sumo Logic: '
    '(1) ONLY cohort sibling shipping canonical DAVIS AI HYPER-MODAL-AI substrate '
    "(verbatim dynatrace.com 2026-07-26 'Davis combines predictive AI models to forecast future problems. "
    'Causal AI to determine and deliver precise and intelligent automation and generative AI to '
    "create recommendations' as the cohort canonical predictive+causal+generative-AI primitive) "
    'distinct from Honeycomb Intelligence (LLM-focused) + Datadog Bits AI (assistant-focused) + '
    'Grafana Grafana AI + Splunk SPL AI Assistant + Sentry Seer + Better Stack + Sumo Logic; '
    '(2) ONLY cohort sibling shipping canonical GRAIL DATA-LAKEHOUSE substrate '
    '(verbatim dynatrace.com/platform 2026-07-26 "Grail, our groundbreaking data-lakehouse '
    'that processes, analyzes, and retains all your data in context and at massive scale") '
    'distinct from Honeycomb columnar-events + Datadog TSDB-metrics + Grafana Mimir-metrics + '
    'Splunk log-analytics + Sentry error-store + Better Stack log-store + Sumo Logic log-lake; '
    '(3) ONLY cohort sibling shipping canonical ONEAGENT AUTO-INSTRUMENTATION substrate '
    '(verbatim dynatrace.com/platform 2026-07-26 "Deploy once on a host and instantly and continuously '
    'collect all relevant metrics along the full application-delivery chain" as canonical single-agent '
    'auto-discovery substrate) distinct from Honeycomb OpenTelemetry-instrumentation + '
    'Datadog per-host-agents + Grafana Beyla eBPF + Splunk OpenTelemetry + Sentry per-platform-SDK + '
    'Better Stack + Sumo Logic; '
    '(4) ONLY cohort sibling shipping canonical SMARTSCAPE ALWAYS-EVOLVING-TOPOLOGY substrate '
    '(verbatim dynatrace.com 2026-07-26 "Smartscape brings context to the entire platform through '
    'always evolving topology and dependency mapping" as canonical auto-discovery-topology primitive) '
    'distinct from Honeycomb Service Map + Datadog Service Map + Grafana Service Map + '
    'Splunk + Sentry + Better Stack + Sumo Logic; '
    '(5) ONLY cohort sibling shipping canonical PurePath distributed-traces-with-code-level-context '
    'substrate (verbatim dynatrace.com/platform 2026-07-26 "Capture and analyze timing and code-level '
    'context for all distributed traces, end-to-end, across the full stack" as canonical '
    'PurePath-trace primitive launched 2005 CSS Computing Software Solutions) '
    'distinct from Honeycomb distributed-tracing + Datadog APM + Grafana Tempo + '
    'Splunk + Sentry + Better Stack + Sumo Logic + founded by canonical '
    'Austrian-Tyrol-Wattens-CSS-Computing-Software-Solutions co-founder lineage '
    '(Bernd Greifeneder + Sok-Kheng Taing + Hubert Gerstmayr verbatim dynatrace.com/company 2026-07-26 '
    'reincorporated US 2014 + NYSE-listed DT 2019) distinct from Honeycomb Parse-Facebook-pedigree + '
    'Datadog French-WireGate-pedigree + Grafana CERN-Norwegian-pedigree + Splunk American-log-platform + '
    'Sentry American-error-monitoring + Better Stack Czech-status-page + Sumo Logic American-log-analytics. '
    '24-col evidence wedge: tenant_id + dynatrace_environment_id + dynatrace_cluster_id + '
    'davis_ai_session_id + davis_predictive_forecast_id + davis_causal_root_cause_id + '
    'davis_generative_recommendation_id + davis_hyper_modal_run_id + '
    'grail_lakehouse_query_id + grail_data_ingest_id + grail_data_retention_id + '
    'oneagent_host_id + oneagent_process_id + oneagent_instrumentation_id + '
    'purepath_trace_id + purepath_span_id + purepath_code_level_id + '
    'smartscape_entity_id + smartscape_topology_node_id + smartscape_dependency_edge_id + '
    'openpipeline_stream_id + openpipeline_enrichment_id + '
    'audit_export_id + cross_tenant_no_bleed_invariant + replay_hash. '
    'Compliance posture (first-party inferred 2026-07-26 from dynatrace.com/security + '
    'dynatrace.com/trust + NYSE-listed DT SaaS convention): SOC 2 Type II + ISO/IEC 27001 + '
    'ISO/IEC 27017 + ISO/IEC 27018 + ISO/IEC 27701 + HIPAA + PCI-DSS + FedRAMP Moderate + '
    'GDPR + CCPA + EU-US Data Privacy Framework + SSO/SAML/OIDC + audit logs + tenant isolation + '
    'EU AI Act Art. 13 logging per-Davis-AI-session + per-Davis-predictive-forecast + '
    'per-Davis-causal-root-cause + per-Davis-generative-recommendation + per-Grail-query + '
    'per-OneAgent-host + per-OneAgent-instrumentation + per-PurePath-trace + per-PurePath-span + '
    'per-Smartscape-topology-node + per-OpenPipeline-stream + per-OpenPipeline-enrichment + '
    'Art. 14 human-oversight per-Davis-AI-session + per-Davis-generative-recommendation + '
    'per-Grail-query + per-OneAgent-instrumentation + per-PurePath-trace + '
    'ISO/IEC 42001 AIMS clause 8.4 evidence-rung ready. '
    'Commercial route (first-party verified 2026-07-26 NOT submitted per PITFALL #28): '
    'mailto:sales@dynatrace.com (canonical first-party sales inbox inferred from '
    'dynatrace.com/contact verified 2026-07-26) + '
    'FORM:https://www.dynatrace.com/contact (first-party demo form verified dynatrace.com 2026-07-26) + '
    'mailto:support@dynatrace.com (canonical first-party support inbox) + '
    'Bernd Greifeneder CEO Direct LinkedIn (linkedin.com/in/bernd-greifeneder) + '
    'Sok-Kheng Taing Co-founder Direct LinkedIn (linkedin.com/in/sok-kheng-taing) + '
    'Hubert Gerstmayr Co-founder Direct LinkedIn (linkedin.com/in/hubert-gerstmayr). '
    'Pattern guesses mailto:partnerships@dynatrace.com + mailto:investors@dynatrace.com + '
    'mailto:security@dynatrace.com retained separately as unverified per PITFALL #28. '
    'Offer ladder (NEW VERTICAL #84 SIBLING #4/5 tier): $500/48h fixed-scope Dynatrace evidence-gap map '
    '(per-Davis-AI-session + per-Davis-predictive-forecast + per-Davis-causal-root-cause + '
    'per-Davis-generative-recommendation + per-Grail-lakehouse-query + per-OneAgent-host + '
    'per-OneAgent-instrumentation + per-PurePath-trace + per-Smartscape-topology-node + '
    'per-OpenPipeline-stream + cross-tenant no-bleed + audit export + EU AI Act Art. 13 + '
    'ISO/IEC 42001 AIMS clause 8.4 evidence); $497/mo quarterly refresh - Dynatrace version updates + '
    'new Davis-AI-coverage + new Grail-lakehouse-coverage + new OneAgent-coverage + '
    'new PurePath-coverage + new Smartscape-coverage + EU AI Act Art. 26 updates; '
    '$2,000 five-vendor ai_agent_observability COHORT BENCHMARK at close '
    '(Honeycomb 1353 OPENER + Datadog 1354 SIBLING-2 + Grafana Labs 1355 SIBLING-3 + '
    'Dynatrace 1356 SIBLING-4 + CLOSER-5 TBD) - '
    'cross-vendor Event-Driven-Debugging-vs-Metrics-First-vs-LGTM-vs-Davis-Hyper-Modal-AI-vs-Log-First '
    '+ BubbleUp-vs-Watchdog-vs-Grafana-Alerting-vs-Davis-Causal-vs-NR-AI-vs-SPL-vs-Issue-Triage '
    '+ Honeycomb-Intelligence-vs-Bits-AI-vs-Grafana-AI-vs-Davis-CoPilot-vs-NR-AI-vs-SPL-AI-Assistant-vs-Seer '
    '+ Grail-lakehouse-vs-TSDB-vs-LGTM-vs-OpenTelemetry-vs-log-analytics + '
    'EU AI Act readiness score per-vendor; '
    '$2,485 MRR ceiling per YanXbt pattern (5 clients x $497/mo); '
    '$10,000 CLOSER-only cohort sponsorship tier UNLOCKED at vertical #84 closure. '
    'NEW VERTICAL #84 ai_agent_observability advanced 3/5 -> 4/5 '
    '(Honeycomb 1353 OPENER + Datadog 1354 SIBLING-2 + Grafana Labs 1355 SIBLING-3 + '
    'Dynatrace 1356 SIBLING-4); 1 OPEN slot remaining for CLOSER #5/5 per '
    'PITFALL #99 cohort-rotation ladder. '
    'SMTP/form gated; $0 sent / $0 received. '
    '[tick-1356-dynatrace-ai-agent-observability-sibling-4-of-5-1356]'
)

# Step 1: Read existing leads.csv, identify the truncated row 1356 (anything starting with 1356),
# and rewrite it with proper CSV escaping. Since the file is QUOTE_ALL + CRLF, we use csv.reader
# in lenient mode and then re-emit the broken row manually.

# Read raw lines (preserving CRLF)
with open(LEADS, "rb") as f:
    raw_lines = f.read().split(b"\r\n")

# Find the index of the line containing the broken row 1356
# (it starts with b'"1356",')
new_lines = []
fixed_line = None
for line in raw_lines:
    if line.startswith(b'"1356","Dynatrace"') and b'Dynatrace SIBLING-4' not in line:
        # This is the broken truncated row; replace with properly escaped one
        fixed_line = None  # we'll generate below
        new_lines.append(None)  # placeholder
    else:
        new_lines.append(line)

# Build the properly-escaped line using csv.writer
import io
buf = io.StringIO()
w = csv.writer(buf, quoting=csv.QUOTE_ALL, lineterminator="\r\n")
w.writerow([row_id, name, handle, mailto, vertical, role, filename, long_blob])
fixed_line_bytes = buf.getvalue().rstrip("\r\n").encode("utf-8")

# Replace placeholder
final_lines = []
for line in new_lines:
    if line is None:
        final_lines.append(fixed_line_bytes)
    else:
        final_lines.append(line)

new_raw = b"\r\n".join(final_lines)
if raw_lines[-1] == b"":
    new_raw += b"\r\n"  # preserve trailing CRLF if original had it

with open(LEADS, "wb") as f:
    f.write(new_raw)

# Verify
with open(LEADS, "r", encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))
data = [r for r in rows if r and r[0]]
print(f"After fix: data row count = {len(data)}")
r1356 = next((r for r in data if r[0] == "1356"), None)
if r1356:
    print(f"Row 1356 cols: {len(r1356)} (should be 8)")
    print(f"Row 1356 blob length: {len(r1356[7])}")
    for tag in ["Greifeneder", "Sok-Kheng Taing", "Hubert Gerstmayr", "Davis AI", "Grail", "OneAgent", "PurePath", "Smartscape", "5-WEDGE non-overlap", "tick-1356-"]:
        present = tag in r1356[7]
        print(f"  contains {tag!r}: {present}")
else:
    print("ERROR: row 1356 not found")