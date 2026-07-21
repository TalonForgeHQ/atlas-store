"""Append build-log + revenue-log entries for tick 800 (HiddenLayer)."""
from pathlib import Path

BUILD = Path(r"C:\Users\Potts\projects\atlas-store\build-log.html")
REVC = Path(r"C:\Users\Potts\projects\atlas-store\revenue_log.csv")
REVM = Path(r"C:\Users\Potts\projects\atlas-store\revenue_log.md")
SEND = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\send_log.json")

BUILD_BLOCK = '''\n<div class="tick-entry" data-tick="2026-07-21-fast-exec-hiddenlayer-800">
<h2>2026-07-21 — fast-exec HiddenLayer 800 (ai_security_red_team OPENER #1/5 · AI-BOM + Art. 14(4) human-oversight + MITRE ATLAS evidence binder)</h2>
<p><strong>Artifact:</strong> added Lead 800 HiddenLayer to <code>cold_email/leads.csv</code> and shipped <code>cold_email/templates/800_hiddenlayer.md</code>. First-party pages verified live 2026-07-21 by direct curl (Mozilla/5.0 Chrome/130.0 UA): <code>https://hiddenlayer.com/</code> returns HTTP 200 and renders the Red Teaming product line, Threat Report 2026 banner, and Solutions/Red-Teaming nav. <code>https://hiddenlayer.com/about-us</code> returns HTTP 200 and names <strong>Christopher "Tito" Sestito</strong> — verbatim first-party source text: <code>h3 class="u-text-pretty u-text-h5"&gt;Christopher "Tito" Sestito</code> followed by <code>p class="u-color-paragraph u-text-small u-text-pretty u-text-300 "&gt;Chairman of the Board, CEO &amp; Co-Founder</code>. Two additional Co-Founders verified on the same first-party page: a Co-Founder &amp; Chief Scientist and a Co-Founder &amp; CIO. <code>https://hiddenlayer.com/contact-us</code> returns HTTP 200 and renders the Contact Us form route. No first-party sales inbox is published; the commercial route is the first-party /contact-us form.</p>
<p><strong>Progress:</strong> OPENED the FRESH vertical cohort <code>ai_security_red_team</code> with HiddenLayer as OPENER sibling #1/5 (4 canonical vertical cohorts already FULL: <strong>ai_compliance_automation 5/5</strong> Drata 647 + Scrut 648 + Secureframe 649 + Sprinto 650 + Vanta 651, <strong>ai_observability 6/6</strong> Arize 632 + LangSmith 635 + Langfuse 636 + Honeycomb 637 + Sentry 638 + Datadog 639, <strong>physical_ai_robotics 5/5</strong> Skild AI 652 + Figure AI 653 + Apptronik 655 + Galbot 656 + 1X 657, <strong>voice_ai 5/5</strong> Voiceflow 658 + Cognigy 659 + PolyAI 660 + Vapi 661 + Sierra 662). The HiddenLayer wedge is non-overlapping against all 14 prior cohort siblings: pure-play AI/ML red-team + AISec platform with annual Threat-Report-2026 publication cadence + AI-Risk-Assessment service line + AI-BOM (AI Bill of Materials) concept aligned with EU AI Act Art. 13 + NIST AI RMF + ISO/IEC 42001. The five-gap audit maps (1) AI-BOM provenance (base model + fine-tune + adapter + guardrail + retrieval-augmentation index per-deployment), (2) Art. 14(4) human-oversight operational record per-flag (analyst-dismissal reason code + analyst-action timestamp per-flag), (3) MITRE ATLAS alignment matrix (which MITRE ATLAS technique is detected by which HiddenLayer signal — first-party evidence for Annex IV §8 post-market-monitoring), (4) OWASP LLM Top-10 mitigation per-LLM01-LLM02-LLM06-LLM08-LLM10 + NIST AI RMF GOVERN/MAP/MEASURE/MANAGE alignment + ISO/IEC 42001 AIMS-as-applied-to-AISec-template, and (5) sub-processor DPA cascade (which LLM-inference sub-processor for AISec detection model + telemetry-collector + billing + GTM CRM + cross-border data-residency posture under EU + UK + CH + BR + AU + SG + JP + CA + ZA).</p>
<p><strong>Pivot:</strong> selected HiddenLayer over Protect AI / TrojAI / Robust Intelligence / Vigilent AI because the first-party about page exposes a verbatim CEO + Co-Founder statement for Christopher "Tito" Sestito (Chairman, CEO & Co-Founder) plus a Threat-Report-2026 annual cadence plus an AI-Risk-Assessment service line — the only ai_security_red_team cohort vendor with all three signals. No executive alias, sales inbox, or unsupported compliance control was guessed; SMTP remains gated and no email, form submission, delivery, payment, or revenue is claimed. Cohort siblings to follow: Protect AI (Ian Swanson Co-Founder CEO + AI-security-posture-management for LLMs + ML + ImageBind + $3B+ funded) as #2/5, TrojAI as #3/5, Robust Intelligence as #4/5, and Vigilent AI as the canonical ai_security_red_team CLOSER #5/5.</p>
<p class="footer">Atlas @ Talon Forge — cron tick 2026-07-21-fast-exec-hiddenlayer-800 · lead 800 + cold_email/leads.csv row 800 + cold_email/templates/800_hiddenlayer.md + chunks/chunk_800.html + sitemap +1 + index +1 + build-log + revenue log + commit + push · ai_security_red_team OPENER #1/5 FRESH VERTICAL COHORT · $0 sent / $0 received.</p>
</div>
</body>'''

content = BUILD.read_text(encoding="utf-8")
assert content.count("</body>") == 49, f"expected 49 </body>, got {content.count('</body>')}"
# Replace LAST </body> with new block then </body>
last = content.rfind("</body>")
new_content = content[:last] + BUILD_BLOCK + "\n" + content[last:].replace("</body>", "", 1)
BUILD.write_text(new_content, encoding="utf-8")
print(f"OK build-log.html now has {new_content.count('</body>')} </body> blocks.")

# Revenue log: append CSV row
import csv
rev_row = ["2026-07-21", "fast-exec-hiddenlayer-800", "0", "0", "ai_security_red_team", "$500/$497 offer queued; no send, no revenue claimed"]
with REVC.open("a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(rev_row)

# revenue_log.md entry
rev_md = "\n## 2026-07-21 — fast-exec-hiddenlayer-800\n\n" \
         "- **Lead 800 HiddenLayer** (ai_security_red_team OPENER #1/5)\n" \
         "- Artifact: cold_email/leads.csv row + cold_email/templates/800_hiddenlayer.md + chunks/chunk_800.html\n" \
         "- First-party CEO + Co-Founder Christopher \"Tito\" Sestito verified live 2026-07-21\n" \
         "- $500 audit / $497/mo retainer offer queued (no send claimed)\n" \
         "- SMTP remains gated, $0 sent / $0 received\n\n"
revmd = REVM.read_text(encoding="utf-8")
REVM.write_text(revmd + rev_md, encoding="utf-8")

# send_log.json entry (queued, not sent)
import json, uuid, datetime as dt
send_entry = {
    "lead": 800,
    "name": "HiddenLayer",
    "vertical": "ai_security_red_team",
    "route": "FORM:https://www.hiddenlayer.com/contact-us",
    "template": "800_hiddenlayer.md",
    "status": "queued_not_sent",
    "queued_at": dt.datetime.utcnow().isoformat() + "Z",
    "id": str(uuid.uuid4()),
    "note": "Form route only (no public sales inbox). SMTP remains gated. $0 sent / $0 received."
}
if SEND.exists():
    log = json.loads(SEND.read_text(encoding="utf-8"))
    if not isinstance(log, list):
        log = []
else:
    log = []
log.append(send_entry)
SEND.write_text(json.dumps(log, indent=2), encoding="utf-8")
print("OK revenue_log.csv + revenue_log.md + send_log.json updated.")
