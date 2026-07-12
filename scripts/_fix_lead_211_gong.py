import csv, os
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
TIER_REASON_FILE = Path("C:/Users/Potts/AppData/Local/Temp/tier_reason_211_gong.txt")

tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").strip()
assert not tier_reason.startswith('"'), "tier_reason must be plain text, not a CSV row"
assert tier_reason.startswith("Canonical"), "tier_reason must start with 'Canonical'"

# CORRECT columns matching leads.csv header
HEADER = ["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"]
NEW_ROW = ["211", "Gong", "@gong_io", "privacy@gong.io", "conversation_intelligence", "1", "298_gong.md", tier_reason]

for csv_name in ["cold_email/leads.csv", "cold_email/leads_with_emails.csv"]:
    csv_path = REPO / csv_name
    with csv_path.open("r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    # Verify row 210 last is intact
    if rows[-1].get("index") != "210":
        print(f"FAIL {csv_name}: row[-1] index is {rows[-1].get('index')}, expected 210")
        continue

    # Drop the corrupt 211 if present
    rows = [r for r in rows if r.get("index") != "211"]

    # Rewrite
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HEADER, quoting=csv.QUOTE_ALL)
        w.writeheader()
        for r in rows:
            w.writerow(r)

    # Append correct
    with csv_path.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(NEW_ROW)

    # Verify
    with csv_path.open("r", encoding="utf-8") as f:
        rows2 = list(csv.DictReader(f))
    last = rows2[-1]
    assert last["index"] == "211", f"{csv_name}: last index is {last['index']}"
    assert last["name"] == "Gong", f"{csv_name}: last name is {last['name']}"
    assert last["email"] == "privacy@gong.io", f"{csv_name}: last email is {last['email']}"
    assert last["vertical"] == "conversation_intelligence", f"{csv_name}: last vertical is {last['vertical']}"
    assert last["template"] == "298_gong.md", f"{csv_name}: last template is {last['template']}"
    assert last["tier_reason"].startswith("Canonical"), f"{csv_name}: tier_reason shape FAIL"
    print(f"OK {csv_name}: {len(rows2)} rows, last=211 Gong privacy@gong.io")

print("DONE: lead 211 (Gong) appended correctly to both CSVs")