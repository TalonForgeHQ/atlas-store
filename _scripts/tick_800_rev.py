"""Append canonical revenue_log entry in csv schema used by cold_email/revenue_log.csv."""
from pathlib import Path
import csv

p = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\revenue_log.csv")
# Schema = date, lead, template, chunk, cohort, revenue_usd, note (quoted)
row = ["2026-07-21","800","800_hiddenlayer.md","chunk_800.html",
       "ai_security_red_team OPENER #1/5 (NEW VERTICAL #19)",
       "0",
       "HiddenLayer (HiddenLayer, Inc. - hiddenlayer.com AI-security platform purpose-built for AI/ML-model threat-detection + adversarial-input-defense for LLMs + ML-supply-chain-security + model-and-data-poisoning detection + AI-BOM + AI-Risk-Assessment + AI Red Team engagements + named CEO + Co-Founder Christopher 'Tito' Sestito as Chairman of the Board, CEO & Co-Founder verified live 2026-07-21 on first-party https://hiddenlayer.com/about-us; 2nd Co-Founder verified as Chief Scientist; 3rd Co-Founder verified as CIO; commercial route FORM:https://www.hiddenlayer.com/contact-us HTTP 200 verified live 2026-07-21). $500/48h evidence-gap map + $497/mo quarterly refresh staged; SMTP remains gated; no send, delivery, payment, or revenue claimed; cohort OPENER #1/5."]
with p.open("a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow(row)

# verify
with p.open("r", encoding="utf-8", newline="") as f:
    lines = f.readlines()
print(f"OK cold_email/revenue_log.csv now has {len(lines)} lines. Last = {lines[-1][:80]}")
