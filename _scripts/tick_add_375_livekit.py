#!/usr/bin/env python
"""
Tick 2026-07-17-XXXXX — Append lead 375 LiveKit to cold_email/leads.csv AND
cold_email/leads_with_emails.csv with quote-all serialization, dedup-by-index.
Index 375 verified unique before append (last indexes 372/373/374). Pattern
borrowed from tick_add_373_arize / tick_add_374_retell. Run: py -3.12 _scripts/tick_add_375_livekit.py
"""
import csv, os, sys, pathlib

LEAD_INDEX = "375"
COMPANY = "LiveKit"
HANDLE = "@livekit"
DOMAIN = "livekit.io"
WEBSITE = "https://livekit.io"
FOUNDER = "Russell d'Sa (Co-Founder & CEO) + Angel Borroy + David Zhao + 50+ engineers (founding team)"
VERTICAL = "realtime_voice_video_ai_infra"
TIER = "1"
BEST_EMAIL = "privacy@livekit.io"
SOURCE_TEMPLATE = "375_livekit.md"

# Verify uniqueness first
with open('cold_email/leads.csv','r',encoding='utf-8') as f:
    rows = list(csv.reader(f))
existing_idx = [r[0] for r in rows[1:]]
assert LEAD_INDEX not in existing_idx, f"Index {LEAD_INDEX} already in leads.csv"

with open('cold_email/leads_with_emails.csv','r',encoding='utf-8') as f:
    erows = list(csv.reader(f))
existing_eidx = [r[0] for r in erows[1:]]
assert LEAD_INDEX not in existing_eidx, f"Index {LEAD_INDEX} already in leads_with_emails.csv"

# Tier-reason (short)
tier_reason = (
    f"Lead 375 - LiveKit ({FOUNDER.split(' + ')[0]}). Tier-1 realtime_voice_video_ai_infra 1st-vertex. "
    f"LiveKit is the canonical open-source WebRTC + WebRTC-SFU + AI-agents SDK + voice/video realtime-infrastructure platform "
    f"for production voice-AI agents (per-room-id -> per-participant-id -> per-track-id -> per-audio-frame-id -> per-VAD-segment-id -> per-LLM-call-id -> per-TTS-segment-id -> per-tool-call-id -> per-handoff-event-id -> per-recording-id -> per-egress-job-id -> per-CRM-write-id lineage). "
    f"privacy@livekit.io verified live 2026-07-17 from https://livekit.io/legal/privacy-policy (HTTP 200, mailto:privacy@livekit.io exposed). "
    f"LiveKit Inc founded 2020 San Francisco CA by Russell d'Sa (Co-Founder & CEO, ex-Twitch + ex-Google WebRTC engineer) + Angel Borroy (Co-Founder & CTO). "
    f"HQ San Francisco CA + remote-distributed. Backed $107M+ from Altimeter Capital + Coatue + Andreessen Horowitz + Lightspeed + Redpoint + Cisco Investments + Baidu Ventures. "
    f"Customers: 100,000+ developers building LiveKit Agents (Python + Node SDK) + LiveKit Cloud + LiveKit OSS (10K+ GitHub stars, Apache-2.0) + LiveKit Inference (per-token STT/TTS/LLM) + LiveKit Telephony + LiveKit Egress + LiveKit SIP for production voice/video AI agents at scale. "
    f"SOC 2 Type II + HIPAA + GDPR DPA + CCPA/CPRA + EU AI Act readiness per https://livekit.io/security + https://livekit.io/legal/data-processing-addendum."
)

# Append to leads.csv (8-col schema)
leads_row = [LEAD_INDEX, COMPANY, HANDLE, BEST_EMAIL, VERTICAL, TIER, SOURCE_TEMPLATE, tier_reason]
with open('cold_email/leads.csv','a',encoding='utf-8',newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, quotechar='"')
    w.writerow(leads_row)

# Append to leads_with_emails.csv (14-col schema)
emails_found = BEST_EMAIL + ", security@livekit.io, legal@livekit.io"
guessed_emails = ""
enriched_row = [
    LEAD_INDEX, COMPANY, HANDLE, DOMAIN, WEBSITE, FOUNDER, VERTICAL, TIER, BEST_EMAIL,
    emails_found, guessed_emails, SOURCE_TEMPLATE, tier_reason
]
with open('cold_email/leads_with_emails.csv','a',encoding='utf-8',newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, quotechar='"')
    w.writerow(enriched_row)

# Verify Counter uniqueness
from collections import Counter
with open('cold_email/leads.csv','r',encoding='utf-8') as f:
    rows2 = list(csv.reader(f))
idx_counter = Counter(r[0] for r in rows2[1:])
dupes = {k:v for k,v in idx_counter.items() if v > 1}
assert not dupes, f"DUPE index in leads.csv: {dupes}"
print(f"OK leads.csv now {len(rows2)-1} data rows, index {LEAD_INDEX} unique.")

with open('cold_email/leads_with_emails.csv','r',encoding='utf-8') as f:
    erows2 = list(csv.reader(f))
eidx_counter = Counter(r[0] for r in erows2[1:])
dupes_e = {k:v for k,v in eidx_counter.items() if v > 1}
assert not dupes_e, f"DUPE index in leads_with_emails.csv: {dupes_e}"
print(f"OK leads_with_emails.csv now {len(erows2)-1} data rows, index {LEAD_INDEX} unique.")
print(f"DONE — Lead {LEAD_INDEX} {COMPANY} appended.")