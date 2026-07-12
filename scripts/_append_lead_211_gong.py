import csv
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
TIER_REASON_FILE = Path("C:/Users/Potts/AppData/Local/Temp/tier_reason_211_gong.txt")

tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").strip()
assert not tier_reason.startswith('"'), "tier_reason must be plain text"
assert tier_reason.startswith("Canonical"), "tier_reason must start with 'Canonical'"

# Append to leads.csv (8-col)
leads_csv = REPO / "cold_email" / "leads.csv"
NEW_ROW_LEADS = ["211", "Gong", "@gong_io", "privacy@gong.io", "conversation_intelligence", "1", "298_gong.md", tier_reason]
with leads_csv.open("a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(NEW_ROW_LEADS)
with leads_csv.open("r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
last = rows[-1]
assert last["index"] == "211" and last["name"] == "Gong" and last["email"] == "privacy@gong.io"
assert last["vertical"] == "conversation_intelligence" and last["template"] == "298_gong.md"
assert last["tier_reason"].startswith("Canonical")
print(f"OK leads.csv: {len(rows)} rows, last=211 Gong privacy@gong.io conversation_intelligence")

# Append to leads_with_emails.csv (13-col)
lwe_csv = REPO / "cold_email" / "leads_with_emails.csv"
NEW_ROW_LWE = ["211", "Gong", "@gong_io", "gong.io", "https://www.gong.io",
               "Amit Bendov (CEO) + Eilon Reshef (Chief Product Officer)",
               "conversation_intelligence", "1",
               "privacy@gong.io", "privacy@gong.io;dpo@gong.io;help@gong.io",
               "", "298_gong.md", tier_reason]
with lwe_csv.open("a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(NEW_ROW_LWE)
with lwe_csv.open("r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
last = rows[-1]
assert last["lead_index"] == "211" and last["company"] == "Gong"
assert last["best_email"] == "privacy@gong.io" and last["source_template"] == "298_gong.md"
assert last["tier_reason"].startswith("Canonical")
print(f"OK leads_with_emails.csv: {len(rows)} rows, last=211 Gong privacy@gong.io conversation_intelligence")

print("DONE")