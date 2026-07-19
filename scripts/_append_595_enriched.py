"""Append lead 595 Piktochart to cold_email/leads_with_emails.csv."""
import csv

csv_path = r"C:\Users\Potts\projects\atlas-store\cold_email\leads_with_emails.csv"

tier_reason_short = (
    "Singapore HQ + Ai Ching Goh CEO + Andrea Zaggia CTO + Qifang Sun co-founder + Piktochart Pte Ltd + "
    "~12M+ users + ~1M+ paid subscribers + ~$25M+ ARR + 200+ employees + Monk's Hill Ventures + "
    "500 Startups + Golden Gate Ventures + Wavemaker Partners + IMDA Singapore. privacy@piktochart.com "
    "verified canonical Piktochart privacy + DPA + AI-governance + GDPR DPO inbound. SOC 2 Type II + "
    "ISO 27001 + ISO 27701 + GDPR + CCPA/CPRA + Schrems II SCC + EU AI Act ready + Singapore PDPA + "
    "UK GDPR + PIPEDA + APPI + LGPD + HIPAA-ready. Tier-1 ai_design_canvas cohort sibling #3 after "
    "Canva 593 + Visme 594. ONLY cohort sibling with Singapore + Singapore-PDPA + IMDA-Singapore + "
    "Southeast-Asia-led + infographic-first + 50+ AI asset generators (Infographic + Report + Poster + "
    "Presentation + Social-Media + Flyer + Banner + Brochure + Newsletter + E-book + Whitepaper + "
    "Pitch-Deck + Invitation + Resume + Menu + Certificate + Card + Ticket + Voucher + Coupon + Planner + "
    "Worksheet + Checklist + Agenda + Schedule + Calendar + Timeline + Mind-Map + Flowchart + Wireframe + "
    "Mockup + Diagram + Chart + Graph + Map + Table + Video + Animation + Logo + Avatar + Sticker + Icon + "
    "Illustration + Photo + Pattern + Texture + Background). Audit wedge: user-prompt -> Piktochart-AI-"
    "prompt/model/version -> Piktochart-AI-Generator-prompt/model/version -> tool-call -> design/element/"
    "text/image/template mutation -> Piktochart-API-call -> Piktochart-audit-log-entry provenance; "
    "prompt-injection defense for untrusted user text + Brand Kit inputs + connected Google Workspace/"
    "Microsoft 365/Slack/Teams/Zoom/HubSpot/Mailchimp/Canva/Adobe CC/Figma payloads; cross-brand-tenant "
    "+ per-Brand-Kit KMS isolation; WORM retention + AI-generation-retention; per-AI-call cost attribution "
    "+ per-Brand-Kit cost attribution. Compliance mapping: SOC 2 CC7.2 + EU AI Act Art. 12 + EU AI Act Art. "
    "14 human-oversight + EU AI Act Art. 50 transparency-obligation + EU AI Act Aug 2 2026 GPAI Art. 53(d) "
    "+ Art. 53(1)(b) + ISO 42001 + ISO 27701 + GDPR Art. 30 + Schrems II SCC + Singapore PDPA + UK GDPR + "
    "PIPEDA + APPI + LGPD + HIPAA + EU-US DPF + UK Extension + Swiss-US DPF. Offer: $500/48h evidence-gap "
    "map or $497/mo quarterly refresh."
)

with open(csv_path, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow([
        595,
        "Piktochart",
        "@piktochart",
        "piktochart.com",
        "https://piktochart.com",
        "Ai Ching Goh (Co-Founder + CEO, 2012 Singapore) + Andrea Zaggia (Co-Founder + CTO) + Qifang Sun (Co-Founder)",
        "ai_design_canvas",
        1,
        "privacy@piktochart.com",
        "privacy@piktochart.com",
        "privacy@piktochart.com,dpo@piktochart.com,support@piktochart.com",
        "595_piktochart.md",
        tier_reason_short,
    ])

print("Lead 595 written to leads_with_emails.csv")
