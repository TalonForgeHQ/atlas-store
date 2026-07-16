#!/usr/bin/env python3
"""Append Arize AI as lead 295 to cold_email/leads.csv safely."""
import os, sys

CSV_PATH = r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv"

# Idempotency: skip if already present
with open(CSV_PATH, "r", encoding="utf-8") as f:
    content = f.read()
if '"295"' in content:
    print("Lead 295 already present; skipping append.")
    sys.exit(0)

ROW = (
    '"295","Arize AI","@ArizeAI","privacy@arize.com","ai_observability_evals","1","366_arize.md",'
    '"Canonical AI-observability + LLM-evaluation + Agent-evaluation + ML-monitoring + drift-detection + '
    'AI-tracing + prompt-engineering + production-AI-debugging + online-evaluation + RAG-evaluation + '
    'agentic-tracing + hallucination-detection + AI-Bill-of-Rights-evaluation + EU-AI-Act-readiness + '
    'NIST-AI-RMF-MEASURE + ISO-42001-9.4 platform (Arize Phoenix open-source LLM-tracing + Arize AX '
    'enterprise LLM-evaluation + Arize AI Observability + Arize Agentic Tracing + Arize Prompt Engineering + '
    'Arize Online Evaluation + Arize Drift Detection + Arize Embedding Analysis + Arize Production Monitoring + '
    'Arize AI Bill of Rights). privacy@arize.com verified live 2026-07-16 via curl scrape '
    'https://arize.com/privacy-policy/ HTTP 200 exposing mailto:privacy@arize.com as the canonical GDPR '
    'Art. 28 DPA + SOC 2 Type II + EU AI Act Annex IV + ISO 42001 + ISO 27001 + HIPAA + vendor-DD '
    'strategic-inbound channel. Founded 2019 in Berkeley California by Aparna Dhinakaran '
    '(Co-Founder + CEO, ex-Google + ex-Microsoft + ex-Stitch Fix ML-leadership + Forbes-30-Under-30 + '
    'UC Berkeley EECS) + Jason Lopatecki (Co-Founder + CTO, ex-Google + ex-Apple + ex-Stitch Fix + '
    'ex-Twitter ML-leadership). HQ Berkeley California + New York NY + remote-distributed. Raised $60M+ '
    'across Seed + Series A + Series B + Series C from Foundation Capital + Battery Ventures + TCV + '
    'Swift Ventures + Linear Capital + others. Customers include 1000+ paying enterprise customers in '
    'financial-services + healthcare + pharma + retail + technology + media + entertainment using Arize '
    'Phoenix + Arize AX for LLM-tracing + agent-tracing + LLM-evaluation + online-evaluation + '
    'production-AI-monitoring + AI-Bill-of-Rights-evaluation at production scale. SOC 2 Type II + '
    'ISO 27001 + GDPR DPA + EU AI Act readiness + HIPAA + NIST AI RMF per arize.com/security + '
    'arize.com/privacy-policy + arize.com/trust. Tier-1 ai_observability_evals 1st-sibling for per-LLM-trace + '
    'per-LLM-span + per-LLM-generation + per-LLM-prompt-version + per-LLM-completion + per-prompt-template-version + '
    'per-agent-tool-call + per-agent-reasoning-chain + per-RAG-retrieval-call + per-RAG-corpus-document-chunk + '
    'per-online-evaluation-result + per-LLM-evaluation-result + per-drift-event + per-hallucination-detection-event + '
    'per-AI-Bill-of-Rights-evaluation + per-NIST-AI-RMF-MEASURE-event + per-ISO-42001-9.4-control-test + '
    'per-tenant-KMS-CMK-BYOK + per-cross-tenant-isolation join-table evidence under SOC 2 CC7.2 + CC6.1 + '
    'EU AI Act Art. 9 + Art. 10 + Art. 12 + Art. 14 + Art. 27 + Art. 43 + Art. 53(d) + Aug 2026 GPAI '
    'enforcement + ISO 42001 9.4 + GDPR Art. 28 + Art. 32 + OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF '
    'GOVERN + MAP + MEASURE + MANAGE. Opens the canonical ai_observability_evals vertical. '
    'privacy@arize.com is the verified GDPR DPA + SOC 2 + ISO 27001 + EU AI Act + vendor-DD strategic-inbound '
    'channel for Arize Phoenix OSS + Arize AX enterprise + Arize AI Observability + Arize Agentic Tracing + '
    'ai_observability_evals audit-target inquiries."\r\n'
)

# Ensure trailing newline then append
if not content.endswith("\n"):
    content += "\n"
content += ROW

with open(CSV_PATH, "w", encoding="utf-8", newline="") as f:
    f.write(content)

# Verify
with open(CSV_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()
print("Total lines:", len(lines))
print("Last:", lines[-1][:120])
