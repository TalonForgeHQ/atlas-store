#!/usr/bin/env python3
"""
Second wave of outreach: small businesses in specific verticals.
Uses Google Maps-style public data via the browser if needed.
For now, generates a deeper lead list.
"""
import os, json

# Additional leads - this wave targets founders/operators specifically
# who publicly post about ops pain (their public tweets signal intent)
LEADS_WAVE_2 = [
    # === SaaS founders with public ops complaints ===
    {"handle": "@bentossell", "name": "Ben Tossell", "vertical": "indie_saas",
     "why": "Makerpad, public indie SaaS"},
    {"handle": "@damengoldberg", "name": "Damengoldberg", "vertical": "indie_saas",
     "why": "Active indie builder"},
    {"handle": "@kevin_osei", "name": "Kevin Osei", "vertical": "indie_saas",
     "why": "Public SaaS builder"},
    {"handle": "@ericoverfield", "name": "Eric Overfield", "vertical": "indie_saas",
     "why": "Public SaaS builder"},
    {"handle": "@jpospisil", "name": "Josh Pispisil", "vertical": "indie_saas",
     "why": "Active SaaS operator"},

    # === Marketing agencies (publicly hiring = ops pain) ===
    {"handle": "@digitalgarage", "name": "DigitalGarage", "vertical": "agency",
     "why": "Public agency"},
    {"handle": "@SingleGrain", "name": "Single Grain", "vertical": "agency",
     "why": "Public growth agency"},
    {"handle": "@HuffPost", "name": "HuffPost Partners", "vertical": "agency",
     "why": "Large media company"},
    {"handle": "@reliableauto", "name": "Reliable Auto", "vertical": "ecommerce",
     "why": "Ecom ops"},

    # === Coaching/infoproduct (lots of manual ops) ===
    {"handle": "@GrantCardone", "name": "Grant Cardone", "vertical": "coaching",
     "why": "Big coaching operation, ops-heavy"},
    {"handle": "@tonyrobbins", "name": "Tony Robbins", "vertical": "coaching",
     "why": "Biggest coaching brand, definitely ops-heavy"},
    {"handle": "@BrendonBurchard", "name": "Brendon Burchard", "vertical": "coaching",
     "why": "Public coach, big team"},

    # === B2B service firms (lawyers, accountants, recruiters) ===
    {"handle": "@Clio", "name": "Clio", "vertical": "legal_tech", "tier": 1,
     "why": "Legal SaaS, serves ops-heavy law firms"},
    {"handle": "@LawPay", "name": "LawPay", "vertical": "legal_tech", "tier": 1,
     "why": "Legal payments, integrated with PMs"},
    {"handle": "@Freshbooks", "name": "Freshbooks", "vertical": "accounting", "tier": 1,
     "why": "Accounting SaaS for SMBs"},

    # === Property managers (the PropBot ICP) ===
    {"handle": "@Yardi", "name": "Yardi", "vertical": "property_tech", "tier": 1,
     "why": "Property mgmt leader, AI features are weak"},
    {"handle": "@buildium", "name": "Buildium", "vertical": "property_tech", "tier": 1,
     "why": "PM SaaS, tenant comms gap"},
    {"handle": "@ManageCasa", "name": "Casa", "vertical": "property_tech", "tier": 1,
     "why": "Smaller PM SaaS"},

    # === Recruiting ops (lots of manual screening) ===
    {"handle": "@Greenhouse", "name": "Greenhouse", "vertical": "recruiting", "tier": 1,
     "why": "ATS, serves recruiting ops"},
    {"handle": "@Lever", "name": "Lever", "vertical": "recruiting", "tier": 1,
     "why": "ATS+CRM, AI features weak"},

    # === e-commerce ops ===
    {"handle": "@Shopify", "name": "Shopify", "vertical": "ecommerce", "tier": 1,
     "why": "Massive ecom platform"},
    {"handle": "@Klaviyo", "name": "Klaviyo", "vertical": "ecommerce", "tier": 1,
     "why": "Ecom email/SMS, ops-heavy customers"},
]

OUT = r"C:\Users\Potts\projects\atlas-store\outreach\leads"
with open(os.path.join(OUT, "wave_2_leads.json"), "w") as f:
    json.dump(LEADS_WAVE_2, f, indent=2)

print(f"Wave 2: {len(LEADS_WAVE_2)} additional leads")
print(f"Total leads across waves: 19 + {len(LEADS_WAVE_2)} = {19 + len(LEADS_WAVE_2)}")