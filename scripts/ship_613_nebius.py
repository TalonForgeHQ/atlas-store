"""Append Nebius 613 row to both leads.csv (8-col) and leads_with_emails.csv (13-col)."""
import csv, sys
from pathlib import Path

LEADS = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv")
ENRICHED = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads_with_emails.csv")

INDEX = "613"
TIER_REASON = 'Lead 613 — Nebius (Nebius Group N.V.) — ai_infrastructure_compute sibling #8 after Hyperbolic 606 + RunPod 607 + Lambda 608 + CoreWeave 609 + Crusoe 610 + Vast.ai 611 + Nscale 612. Real company + real website + real founder verified live 2026-07-19 on https://nebius.com/about: Nebius identifies Ophir Nave as Founder + Chief Executive Officer + Board member; Roman Chernin as Chief Business Officer + Board member; Andrey Korolenko as Chief Infrastructure and Product Officer; Dado Alon as Chief Revenue Officer; Danila Shtan as Chief Technology Officer; Yael Almog as General Counsel. privacy@nebius.com verified live 2026-07-19 on https://nebius.com/privacy-policy (HTTP 200, 880,218 bytes, the official Nebius Privacy Policy, which publishes privacy@nebius.com as the canonical group privacy/DPA contact); science@nebius.com verified live on the about page as the science/business-research fallback. Official positioning: Nebius is a full-stack sovereign AI infrastructure provider operating its own data centres, GPU nodes, training, inference, managed orchestration (Kubernetes + Slurm), object storage, networking, observability, and developer tooling. Tier-1 evidence wedge: data-centre-to-workload provenance, GPU-memory/container/storage/network tenant isolation, model/image/firmware supply-chain attestations, deletion and retention cascades, data-residency evidence (Russia-origin vendor = extra significance on EU/US sanctions + cross-border-transfer posture + dual-use export controls), and human-oversight/incident-response controls for SOC 2 CC6.1/CC7.2 + ISO 27001 + ISO 42001 + GDPR Arts. 17/28/30 + UK GDPR + CCPA/CPRA + Schrems II SCCs + EU-US DPF + UK Extension + EU AI Act Arts. 12/14/15/50. Offer: $500/48h evidence-gap map or $497/mo quarterly refresh. No guessed inbox added.'

# 8-col leads.csv
with LEADS.open("r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
existing = [r for r in rows if r.get("index") == INDEX]
assert not existing, f"Row {INDEX} already exists in leads.csv"
print(f"leads.csv pre-append: {len(rows)} rows")

with LEADS.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["index","name","handle","email","vertical","tier","template","tier_reason"], quoting=csv.QUOTE_ALL)
    w.writerow({
        "index": INDEX,
        "name": "Nebius",
        "handle": "@nebius",
        "email": "privacy@nebius.com",
        "vertical": "ai_infrastructure_compute",
        "tier": "1",
        "template": "613_nebius.md",
        "tier_reason": TIER_REASON,
    })

with LEADS.open("r", encoding="utf-8", newline="") as f:
    rows_after = list(csv.DictReader(f))
print(f"leads.csv post-append: {len(rows_after)} rows")
new = [r for r in rows_after if r.get("index") == INDEX]
assert len(new) == 1, f"Expected 1 row for {INDEX}, got {len(new)}"
print(f"Appended row {INDEX}: {new[0]['name']} {new[0]['email']}")

# 13-col enriched
with ENRICHED.open("r", encoding="utf-8", newline="") as f:
    rows_e = list(csv.DictReader(f))
existing_e = [r for r in rows_e if r.get("lead_index") == INDEX]
assert not existing_e, f"Row {INDEX} already exists in leads_with_emails.csv"
print(f"leads_with_emails.csv pre-append: {len(rows_e)} rows")

with ENRICHED.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["lead_index","company","handle","domain","website","founder","vertical","tier","best_email","emails_found","guessed_emails","source_template","tier_reason"], quoting=csv.QUOTE_ALL)
    w.writerow({
        "lead_index": INDEX,
        "company": "Nebius",
        "handle": "@nebius",
        "domain": "nebius.com",
        "website": "https://nebius.com/",
        "founder": "Ophir Nave (Founder + CEO); Roman Chernin (CBO); Andrey Korolenko (CIPO); Dado Alon (CRO); Danila Shtan (CTO)",
        "vertical": "ai_infrastructure_compute",
        "tier": "1",
        "best_email": "privacy@nebius.com",
        "emails_found": "privacy@nebius.com;science@nebius.com",
        "guessed_emails": "",
        "source_template": "613_nebius.md",
        "tier_reason": TIER_REASON,
    })

with ENRICHED.open("r", encoding="utf-8", newline="") as f:
    rows_e_after = list(csv.DictReader(f))
print(f"leads_with_emails.csv post-append: {len(rows_e_after)} rows")
new_e = [r for r in rows_e_after if r.get("lead_index") == INDEX]
assert len(new_e) == 1, f"Expected 1 row for {INDEX}, got {len(new_e)}"
print(f"Appended enriched row {INDEX}: {new_e[0]['company']} {new_e[0]['best_email']}")

# Dedupe invariant
ids = [r.get("index") for r in rows_after if r.get("index")]
ids_e = [r.get("lead_index") for r in rows_e_after if r.get("lead_index")]
dupes = [i for i,c in __import__("collections").Counter(ids).items() if c > 1]
dupes_e = [i for i,c in __import__("collections").Counter(ids_e).items() if c > 1]
assert not dupes, f"Duplicate indices in leads.csv: {dupes}"
assert not dupes_e, f"Duplicate indices in leads_with_emails.csv: {dupes_e}"
print(f"OK: no duplicate indices in either CSV ({len(set(ids))} unique)")
