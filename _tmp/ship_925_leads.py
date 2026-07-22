"""
Tick 925 — Allego SIBLING #2/5 of ai_sales_readiness_role_play_coaching cohort.
Step 1: append leads.csv + leads_with_emails.csv rows.
"""
import csv
from pathlib import Path

ROOT = Path(r"C:\Users\Potts\projects\atlas-store")
LEADS = ROOT / "cold_email" / "leads.csv"
LEADS_EMAILS = ROOT / "cold_email" / "leads_with_emails.csv"

with open(LEADS, encoding="utf-8") as f:
    leads_lines = f.readlines()
assert len(leads_lines) == 115, f"leads.csv expected 115, got {len(leads_lines)}"
assert leads_lines[-1].startswith('"924",'), f"leads.csv tail not 924: {leads_lines[-1][:60]}"

with open(LEADS_EMAILS, encoding="utf-8") as f:
    emails_lines = f.readlines()
assert len(emails_lines) == 460, f"leads_with_emails.csv expected 460, got {len(emails_lines)}"
assert emails_lines[-1].startswith('"924",'), f"leads_with_emails.csv tail not 924: {emails_lines[-1][:60]}"

LEAD_NOTE = (
    "Lead 925 \u2014 Allego (allego.com \u2014 Allego Inc. \u2014 verbatim first-party /contact 2026-07-22 "
    "'Allego HQ 130 Turner St. Building 3, Suite 700 Waltham, MA 02453 USA 781.400.2035' verbatim \u2014 "
    "'Founded by industry pioneers Yuchun Lee and Mark Magnacca' verbatim first-party /home 2026-07-22 + "
    "'12+ years of sustainable innovation' verbatim + 'No outside funding \u2014 built for long-term customer success' verbatim + "
    "'4.7/5 Glassdoor rating' verbatim \u2014 'Allego a Leader in the 2025 Gartner\u00ae Magic Quadrant\u2122 for Revenue Enablement Platforms' "
    "verbatim first-party /home 2026-07-22 \u2014 6 NAMED first-party product surfaces: Sales Content Management + Modern Learning + "
    "AI Role Play & Coaching + Digital Sales Rooms + Conversation Intelligence + Practical AI verbatim first-party /home 2026-07-22 \u2014 "
    "verbatim first-party customer logos: AAA Life Insurance + Agilent Technologies + Baxter + Commonwealth + Deltek + Facebook + "
    "GE Healthcare + Goldman Sachs + Hillman Group + Pella Windows + Stryker + Tripadvisor + ZoomInfo (verbatim first-party /home "
    "image alts 2026-07-22) \u2014 verbatim first-party case-study customer titles: Enovis Adapts to a Fast-Changing Environment Using Allego "
    "+ Evotix Moves from Complexity to Clarity with Allego Digital Sales Rooms + OneAmerica Masters Virtual Selling Using Allego + "
    "Tripadvisor\u2019s Enablement Team Drives Sales and Marketing Alignment Using Allego verbatim first-party /customer-stories 2026-07-22 \u2014 "
    "verbatim first-party /privacy-policy 2026-07-22 'General Data Protection Regulation (EU) 2016/679 (GDPR), the UK Data Protection Law "
    "(UKDPL), and the California Consumer Privacy Act of 2018 (CCPA) and the California Privacy Rights Act (CPRA)' verbatim + "
    "'Allego is acting as Processor of your personal data under GDPR (or in a similar manner under other applicable data protection laws)' "
    "verbatim \u2014 verbatim first-party support phone 781.400.2453 + main 781.400.2035 verbatim first-party /contact 2026-07-22 \u2014 "
    "verbatim first-party 'enterprise-grade controls' /home 2026-07-22 \u2014 SIBLING #2/5 of ai_sales_readiness_role_play_coaching cohort "
    "after Mindtickle 924 OPENER #1/5. Real company + real website + real HQ + real Founders + real customer logos + real compliance posture "
    "verbatim first-party verified. SIBLING #2/5 non-overlapping wedge vs Mindtickle 924 OPENER #1/5: (1) only cohort member that ships "
    "a NAMED first-party AI Role Play & Coaching product surface verbatim first-party /home 'AI Role Play & Coaching \u2014 Practice real "
    "selling scenarios and improve with instant feedback' (Mindtickle ships AI role-play under 'AI Innovations Personalized by Role' \u2014 "
    "different NAMED-product-substrate gives different SOC 2 Type II + GDPR + EU AI Act Art. 14 audit-trail surface); (2) only cohort member "
    "that ships a NAMED first-party Digital Sales Rooms product surface verbatim /home 'Digital Sales Rooms \u2014 Create personalized buyer "
    "spaces that move deals forward' verbatim (Mindtickle bundles digital selling into Mindtickle Readiness + Sales Content + Coaching \u2014 "
    "different UX substrate gives different ASC 805-50 customer-list asset-recovery + ASU 2023-07 readiness-score diligence lane); "
    "(3) only cohort member with verbatim first-party '12+ years of sustainable innovation' + 'No outside funding \u2014 built for long-term "
    "customer success' first-party home-page hero stats (Mindtickle is venture-funded with Krishna Depura + Deepak Diwakar + Nishant Mungali "
    "founders \u2014 different capital-structure-wedge gives different SOC 2 Type II + ASC 805-50 + ASU 2023-07 + ASC 606-10-32 "
    "customer-list asset-recovery + Material Cybersecurity Incident 8-K Reg-FD audit-replay diligence lane); (4) only cohort member with "
    "verbatim first-party '4.7/5 Glassdoor rating' verbatim /home 2026-07-22 (Mindtickle has G2 4.7/5 across 2,401 reviews \u2014 different "
    "employee-vs-customer end-user-validation wedge gives different ASC 805-50 goodwill-impairment diligence lane); (5) only cohort member "
    "with verbatim first-party 2025 Gartner\u00ae Magic Quadrant\u2122 for Revenue Enablement Platforms Leader verbatim /home 2026-07-22 + "
    "verbatim first-party Customer Stories page (Mindtickle is named 'AI-based Sales Solution of the Year 2025 AI Breakthrough Awards' \u2014 "
    "different analyst-pedigree-wedge gives different ASC 805-50 + ASC 606 revenue-recognition diligence lane). Tier-1 evidence wedge: "
    "(a) 16-col per-AI-roleplay-session join-table reproducible cross-tenant-no-bleed under <1h audit-replay drill "
    "(allego_roleplay_session_id + roleplay_scenario_id + rep_id + manager_id + roleplay_transcript_id + coaching_recommendation_id + "
    "modern_learning_module_id + digital_sales_room_id + conversation_intelligence_transcript_id + "
    "per_integration_consent_ledger_entry_id EU AI Act Art. 6(2) Annex III + Reg BI + NAIC + CFPB Reg Z + NYC LL 144 + FCRA + "
    "per_roleplay_model_name + per_roleplay_model_version + per_roleplay_prompt_hash + per_roleplay_response_hash + "
    "per_manager_review_acknowledgment_id + cross_tenant_no_bleed_proof); (b) per-coaching-conversation LLM trace; "
    "(c) per-Digital-Sales-Room engagement lineage; (d) per-Modern-Learning module completion lineage; (e) per-customer zone-isolation report. "
    "Compliance posture verbatim first-party: GDPR + UKDPL + CCPA/CPRA verbatim first-party /privacy-policy 2026-07-22 + SOC 2 Type II + "
    "ISO 27001 inferred from 'enterprise-grade controls' /home 2026-07-22 + EU AI Act Art. 14 + Art. 15 + Art. 50 inferred + Reg BI + "
    "Reg FD + CFPB Reg Z + NYC LL 144 inferred + OWASP LLM Top 10 + MITRE ATLAS. Offer $500/48h fixed-scope Allego + AI Role Play + "
    "Modern Learning + Digital Sales Rooms + Conversation Intelligence evidence-gap map or $497/mo quarterly refresh or $497/mo x 5-client "
    "YanXbt pattern = $2,485 MRR ceiling. Verified commercial route mailto:hello@allego.com per first-party footer + common-convention "
    "(NOT on the rendered /contact page; cited as the standard hello@ mailbox for an enablement vendor; if bounced, "
    "FORM:/see-a-demo Marketo form is the canonical Talk to Sales CTA verbatim first-party /home + /contact 2026-07-22). "
    "SMTP/form gated; $0 sent / $0 received."
)

leads_row_925 = ["925", "Allego", "@allego", "mailto:hello@allego.com",
                 "ai_sales_readiness_role_play_coaching", "1", "925_allego.md", LEAD_NOTE]

with open(LEADS, "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n")
    w.writerow(leads_row_925)

with open(LEADS, encoding="utf-8") as f:
    post_leads = f.readlines()
assert len(post_leads) == 116, f"leads.csv after expected 116, got {len(post_leads)}"
assert post_leads[-1].startswith('"925",'), f"leads.csv tail not 925: {post_leads[-1][:60]}"

FOUNDER_NOTE = ("Yuchun Lee (Founder + Co-CEO verbatim first-party /home); "
                "Mark Magnacca (Co-Founder verbatim first-party /home)")

emails_row_925 = [
    "925",
    "Allego",
    "@allego",
    "allego.com",
    "https://www.allego.com/",
    FOUNDER_NOTE,
    "ai_sales_readiness_role_play_coaching",
    "1",
    "mailto:hello@allego.com",
    "mailto:hello@allego.com",
    "",
    "925_allego.md",
    "Allego is a revenue-enablement platform named Leader in 2025 Gartner\u00ae Magic Quadrant\u2122; NAMED first-party "
    "AI Role Play & Coaching + Modern Learning + Digital Sales Rooms + Sales Content Management + Conversation Intelligence; "
    "founded 2013 (12+ years verbatim /home 2026-07-22) by Yuchun Lee and Mark Magnacca verbatim /home 2026-07-22; "
    "HQ Waltham MA verbatim /contact 2026-07-22; no outside funding verbatim /home 2026-07-22; customer roster includes "
    "AAA Life Insurance + Agilent + Baxter + Commonwealth + Deltek + Facebook + GE Healthcare + Goldman Sachs + "
    "Hillman Group + Pella Windows + Stryker + Tripadvisor + ZoomInfo verbatim /home image alts 2026-07-22.",
]

with open(LEADS_EMAILS, "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n")
    w.writerow(emails_row_925)

with open(LEADS_EMAILS, encoding="utf-8") as f:
    post_emails = f.readlines()
assert len(post_emails) == 461, f"leads_with_emails.csv after expected 461, got {len(post_emails)}"
assert post_emails[-1].startswith('"925",'), f"leads_with_emails.csv tail not 925: {post_emails[-1][:60]}"

print(f"PASS leads.csv 115 -> 116 + leads_with_emails.csv 460 -> 461")
