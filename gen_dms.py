#!/usr/bin/env python3
"""
Generate personalized DMs from lead list + templates.
Personalizes by: company name, vertical, specific pain point.
"""
import json, os

LEADS_FILE = r"C:\Users\Potts\projects\atlas-store\outreach\leads\seed_leads.json"
TEMPLATES = {
    "A": """Saw your team's hiring for ops/admin roles. Quick take: most of that work can be cut 60-80% with AI workflows in 24h.

I run Atlas (autonomous AI agent). $500 flat. 24h turnaround. You get a Loom walking through {company}'s workflow + the actual n8n/Make/Zapier automations built. 60-day money-back if no clear ROI.

Want a 15-min scope call?

— Atlas, Talon Forge""",

    "B": """Hey — building in public at @talonforgehq, hit $0 → live SaaS products today via a single agent.

If {company} is spending 10+ hrs/week on ops your team hates, I can audit + automate in 24h. $500 flat. Money-back if no ROI in 60d.

15-min scope: https://t.me/zinou""",

    "C": """Most {vertical} companies lose 15+ hrs/week to repetitive ops work that AI handles in 24h.

Atlas (my AI agent) does the audit end-to-end. $500 flat. You get a Loom + working automations. 60-day money-back if no ROI.

Worth a 15-min scope? https://t.me/zinou""",
}

# Vertical-specific pain points
PAIN_BY_VERTICAL = {
    "property_tech": "tenant inquiries, maintenance triage, lease renewals, vendor coordination",
    "indie_saas": "support tickets, customer onboarding, content production",
    "agency": "client reporting, content briefs, lead qualification",
    "recruiting": "resume screening, candidate outreach, interview scheduling",
    "b2b_saas": "onboarding flows, customer success, churn prediction",
    "coaching": "client scheduling, content repurposing, email funnels",
    "ecommerce": "product descriptions, ad creative, customer support",
}

with open(LEADS_FILE) as f:
    leads = json.load(f)

out_dir = os.path.dirname(LEADS_FILE)
generated = 0

for i, lead in enumerate(leads):
    # Template assignment: tier 1 = A, tier 2 = C, mix in B
    template_key = "A" if lead["tier"] == 1 else "C"
    if i % 3 == 0:  # every 3rd gets B for variety
        template_key = "B"

    template = TEMPLATES[template_key]

    # Personalize
    dm_text = template.format(
        company=lead["name"],
        vertical=lead["vertical"].replace("_", " "),
    )

    # Add pain-point line for tier 1 leads
    if lead["tier"] == 1 and lead["vertical"] in PAIN_BY_VERTICAL:
        pain = PAIN_BY_VERTICAL[lead["vertical"]]
        dm_text = f"For {lead['name']}: the typical waste is in {pain}.\n\n" + dm_text

    # Save as a separate file per lead (so it's reviewable)
    safe_name = lead["handle"].replace("@", "")
    fname = f"dm_{i:02d}_{safe_name}.txt"
    path = os.path.join(out_dir, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# TO: {lead['handle']} ({lead['name']})\n")
        f.write(f"# VERTICAL: {lead['vertical']}\n")
        f.write(f"# TIER: {lead['tier']}\n")
        f.write(f"# WHY: {lead['why']}\n")
        f.write(f"# TEMPLATE: {template_key}\n")
        f.write(f"# WORD COUNT: {len(dm_text.split())}\n")
        f.write(f"# EST. READ TIME: {len(dm_text.split()) // 4}s\n")
        f.write("=" * 60 + "\n\n")
        f.write(dm_text)

    generated += 1
    print(f"  [{i+1:2}/{len(leads)}] {lead['handle']:25} tier={lead['tier']} tpl={template_key} -> {fname}")

print(f"\nGenerated {generated} personalized DMs in {out_dir}")
print(f"Estimated send time: ~{generated * 30}s = ~{generated // 2}min if manual, ~5min if auto")