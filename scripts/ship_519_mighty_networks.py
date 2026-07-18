from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
lead_index = "519"
reason = (
    "Real community-platform company at https://www.mightynetworks.com. "
    "First-party pages verified live 2026-07-18: mightynetworks.com/about returned HTTP 200 and names "
    "Gina Bianchini as CEO and co-founder and Tim Herby as CTO and co-founder; the same About page says the "
    "platform's infrastructure processes 75 million web requests per day and 9 billion data points monthly and "
    "describes human and AI development systems. mightynetworks.com/privacy-policy returned HTTP 200 and exposes "
    "dpo@mightynetworks.com plus help@mightynetworks.com. Tier-1 ai_creator_economy cohort sibling #8 after "
    "Patreon 512, Gumroad 513, Kit 514, Substack 515, Kajabi 516, Thinkific 517, and Memberstack 518. "
    "Audit wedge: member request -> Mighty Network tenant -> space/course/event -> retrieved community context -> "
    "prompt/model/version -> generated recommendation, summary, moderation decision, or answer -> human approval -> "
    "notification, moderation, or commerce side effect, with prompt injection, cross-tenant/space isolation, "
    "rollback, deletion, WORM evidence, SOC 2 CC6.1/CC7.2, EU AI Act Articles 12/14, GDPR Articles 22/28, "
    "ISO 42001, NIST AI RMF, and OWASP LLM Top 10 coverage."
)

simple_path = root / "cold_email" / "leads.csv"
enriched_path = root / "cold_email" / "leads_with_emails.csv"

with simple_path.open(encoding="utf-8", newline="") as f:
    simple_rows = list(csv.DictReader(f))
if any(row["index"] == lead_index for row in simple_rows):
    raise SystemExit(f"lead {lead_index} already exists in leads.csv")

with enriched_path.open(encoding="utf-8", newline="") as f:
    enriched_rows = list(csv.DictReader(f))
if any(row["lead_index"] == lead_index for row in enriched_rows):
    raise SystemExit(f"lead {lead_index} already exists in leads_with_emails.csv")

simple_row = [
    lead_index,
    "Mighty Networks",
    "@MightyNetworks",
    "dpo@mightynetworks.com",
    "ai_creator_economy",
    "1",
    "519_mighty_networks.md",
    reason,
]
enriched_row = [
    lead_index,
    "Mighty Networks",
    "@MightyNetworks",
    "mightynetworks.com",
    "https://www.mightynetworks.com",
    "Gina Bianchini (CEO + Co-Founder); Tim Herby (CTO + Co-Founder)",
    "ai_creator_economy",
    "1",
    "dpo@mightynetworks.com",
    "dpo@mightynetworks.com;help@mightynetworks.com",
    "",
    "519_mighty_networks.md",
    reason,
]

for path, row in ((simple_path, simple_row), (enriched_path, enriched_row)):
    needs_newline = path.stat().st_size > 0 and not path.read_bytes().endswith(b"\n")
    with path.open("a", encoding="utf-8", newline="") as f:
        if needs_newline:
            f.write("\n")
        csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n").writerow(row)

print("appended lead 519 to both CSV schemas")
