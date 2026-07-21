#!/usr/bin/env python3
"""Append 833 + 834 entries to revenue_log.csv + send_log.json (queued_not_sent)."""
import csv
import json

# Revenue log append (2 new rows)
revenue_path = r"C:\Users\Potts\projects\atlas-store\cold_email\revenue_log.csv"
with open(revenue_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    last_row = None
    for row in reader:
        last_row = row
print(f"Last revenue_log row: index={last_row[1] if last_row else 'none'}")

# Demandbase row
row_833 = [
    '2026-07-21',
    '833',
    '833_demandbase.md',
    'chunk_833.html',
    'ai_intent_data_enrichment sibling #4/5 (after Apollo 830 OPENER + ZoomInfo 831 + Cognism 832; before Bombora 834 CLOSER) — ABM-platform-native wedge',
    '0',
    "Lead 833 — Demandbase (demandbase.com — B2B ABM + Account Intelligence + Orchestrator AI + Pipeline AI + Buying-Group Intelligence + Advertising + Engagement + Conversions + Orchestration + Cross-Channel Ad Orchestration + Intent Data + Surge Signals + Account Identification + Data + Compliance + Demandbase One — San Francisco CA HQ + offices in NY — founded 2006 by Chris Golec verbatim first-party demandbase.com/company/ 2026-07-21 HTTP 200 'Chris Golec founded Demandbase in 2006' — current CEO Gabe Rogol verbatim first-party demandbase.com/company/ 2026-07-21 'Gabe Rogol CEO Gabriel Rogol is the Chief Executive Officer of Demandbase' — 7 named execs verbatim: Rogol CEO + Truair CMO + Philiotis CRO + Weigand CFO + Zamost CPO + Milletti CPTO (founder of InsideView acquired 2021) + Golec Founder — 450-500 employees — ~160M total funding across 9 rounds (Adobe Ventures + Scale + Altos + Sigma + Costanoa + Greycroft + Salesforce Ventures + Intel Capital) + acquired Spiderbook 2016 + Engagio 2020 + InsideView 2021 + DemandGen 2022 — Pipeline AI launched 2023 — commercial route mailto:info@demandbase.com verified first-party demandbase.com/about-us/contact-us/ 2026-07-21 HTTP 200 — 5-question audit letter with per-account-receipt + per-orchestration-receipt + per-intent-receipt + per-pipeline-receipt + per-control-receipt joins — SOC 2 Type II + ISO 27001 + ISO 27701 + GDPR + UK GDPR + CCPA + CAN-SPAM + TCPA + HIPAA + EU AI Act Art. 50 + NY SHIELD Act + PCI-DSS — $500/48h evidence-gap map + $497/mo quarterly ABM refresh + $497/mo x 5-client YanXbt pattern — SMTP remains gated; no send, delivery, payment, or revenue claimed; $0 sent / $0 received; sibling #4/5."
]

# Bombora row
row_834 = [
    '2026-07-21',
    '834',
    '834_bombora.md',
    'chunk_834.html',
    'ai_intent_data_enrichment CLOSER #5/5 (after Apollo 830 OPENER + ZoomInfo 831 + Cognism 832 + Demandbase 833) — pure-play intent-data + Data Co-op wedge',
    '0',
    "Lead 834 CLOSER — Bombora (bombora.com — pure-play B2B Intent Data + Data Co-op + Surge Signals + Topic Intelligence + Identity + Enrichment + Digital Audiences + Campaign Measurement + Insights Suite + 50+ Integrations + Featured Partners: 6sense + Apollo + Dun & Bradstreet + Featured Integrations: HubSpot + LinkedIn + Salesforce — privacy-first consent-based data sourcing via the Bombora Data Co-op (5,000+ B2B publisher websites contributing intent data in exchange for aggregated intent feed) — New York NY HQ + 160 employees + 10 years in business + 50 integrations — founded 2014 by Mike Burton + Charles Crenshaw + Rob Armstrong — current CEO Mark Connon verbatim first-party bombora.com/company/press-coverage/ 2026-07-21 HTTP 200 'CEO Mark Connon About The B2B Intent Data Company' (June 24 2026 press release) + interview byline 'CEO of Bombora Mar' — Co-founder + former CEO Mike Burton now VP verbatim first-party bombora.com/leadership/ 2026-07-21 'Mike Burton, VP' — PSG Equity acquired majority stake 2021 at ~100M+ valuation — 105M total funding across multiple rounds — commercial route mailto:general-inquiries@bombora.com verified first-party bombora.com/contact 2026-07-21 HTTP 200 (employee-verifications@bombora.com excluded as HR/BG-check route) — 5-question audit letter with per-intent-receipt + per-coop-receipt + per-activation-receipt + per-measurement-receipt + per-control-receipt joins — SOC 2 Type II + ISO 27001 + ISO 27701 + GDPR + UK GDPR + EU AI Act Art. 50 + Schrems II SCC + EU-US DPF + CCPA/CPRA + LGPD + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA + Canada Quebec Law 25 + Canada AIDA + UK AI Bill + DSA Art. 28 + CAN-SPAM + TCPA + HIPAA — $500/48h evidence-gap map + $497/mo quarterly intent refresh + $497/mo x 5-client YanXbt pattern — SMTP remains gated; no send, delivery, payment, or revenue claimed; $0 sent / $0 received; CLOSER #5/5 — cohort COMPLETE 5/5."
]

with open(revenue_path, 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(row_833)
    writer.writerow(row_834)
print(f"Appended 2 rows to {revenue_path}")

# Send log append (2 new entries)
send_path = r"C:\Users\Potts\projects\atlas-store\cold_email\send_log.json"
with open(send_path, 'r', encoding='utf-8') as f:
    send_log = json.load(f)
print(f"Current send_log entries: {len(send_log)}")

# Add 2 new queued_not_sent entries
new_entries = [
    {
        "index": 833,
        "name": "Demandbase",
        "handle": "@demandbase",
        "route": "mailto:info@demandbase.com",
        "vertical": "ai_intent_data_enrichment",
        "position": "sibling #4/5",
        "status": "queued_not_sent",
        "ts": "2026-07-21T18:20:00Z",
        "template": "833_demandbase.md",
        "note": "First-party info@demandbase.com verified on demandbase.com/about-us/contact-us/ 2026-07-21 HTTP 200. Companion evidence + 5-question audit letter + 3 engagement options. SMTP remains gated. $0 sent / $0 received. Cohort sibling #4/5."
    },
    {
        "index": 834,
        "name": "Bombora",
        "handle": "@bombora",
        "route": "mailto:general-inquiries@bombora.com",
        "vertical": "ai_intent_data_enrichment",
        "position": "CLOSER #5/5",
        "status": "queued_not_sent",
        "ts": "2026-07-21T18:20:00Z",
        "template": "834_bombora.md",
        "note": "First-party general-inquiries@bombora.com verified on bombora.com/contact 2026-07-21 HTTP 200. Cohort CLOSER #5/5 — ai_intent_data_enrichment COMPLETE 5/5. SMTP remains gated. $0 sent / $0 received."
    }
]

send_log.extend(new_entries)

with open(send_path, 'w', encoding='utf-8') as f:
    json.dump(send_log, f, indent=2, ensure_ascii=False)
print(f"Appended {len(new_entries)} entries to {send_path} (now {len(send_log)} total)")

# Verify CSV count
with open(revenue_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)
print(f"revenue_log.csv now has {len(rows)} rows ({len(rows)-1} data)")
print(f"Last 3 indexes: {[rows[-3][1], rows[-2][1], rows[-1][1]]}")
