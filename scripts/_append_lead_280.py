"""Append lead 280 (Polytomic) to cold_email/leads.csv and cold_email/leads_with_emails.csv.

Polytomic: data_ops_reverse_etl vertical 5th sibling after Census+Hightouch+Airbyte+Hevo.
Verified inbox support@polytomic.com via curl https://www.polytomic.com/privacy-policy.
"""
import csv
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
LEADS_CSV = REPO / "cold_email" / "leads.csv"
LEADS_WITH_EMAILS_CSV = REPO / "cold_email" / "leads_with_emails.csv"
TIER_REASON_TXT = REPO / "cold_email" / "_tier_reason_280.txt"


def parse_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.reader(f))


def main():
    tier_reason = TIER_REASON_TXT.read_text(encoding="utf-8").rstrip("\n")

    # ===== leads.csv (8 cols: index, name, handle, email, vertical, tier, template, tier_reason) =====
    rows = parse_csv(LEADS_CSV)
    header = rows[0]
    existing_idxs = [int(r[0]) for r in rows[1:] if r and r[0].isdigit()]
    assert 280 not in existing_idxs, f"leads.csv already has index 280"

    new_row_8 = [
        "280",
        "Polytomic",
        "@polytomic",
        "support@polytomic.com",
        "data_ops_reverse_etl",
        "1",
        "280_polytomic.md",
        tier_reason,
    ]
    assert len(new_row_8) == 8, f"leads.csv row must be 8 cols, got {len(new_row_8)}"
    with open(LEADS_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(new_row_8)

    # ===== leads_with_emails.csv (13 cols) =====
    rows2 = parse_csv(LEADS_WITH_EMAILS_CSV)
    existing2 = [int(r[0]) for r in rows2[1:] if r and r[0].isdigit()]
    assert 280 not in existing2, f"leads_with_emails.csv already has index 280"

    new_row_13 = [
        "280",                              # lead_index
        "Polytomic",                        # company
        "@polytomic",                       # handle
        "polytomic.com",                    # domain
        "https://www.polytomic.com",        # website
        "Ghalib Suleiman (Co-Founder + CEO) + Nathan Yergler (Co-Founder + CTO)",  # founder
        "data_ops_reverse_etl",             # vertical
        "1",                                # tier
        "support@polytomic.com",            # best_email
        "support@polytomic.com",            # emails_found
        "support@polytomic.com",            # guessed_emails
        "280_polytomic.md",                 # source_template
        tier_reason,                        # tier_reason
    ]
    assert len(new_row_13) == 13, f"leads_with_emails.csv row must be 13 cols, got {len(new_row_13)}"
    with open(LEADS_WITH_EMAILS_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(new_row_13)

    # ===== parse-back verification =====
    rows_check = parse_csv(LEADS_CSV)
    last = rows_check[-1]
    print(f"leads.csv: appended index={last[0]} name={last[1]} email={last[3]} vertical={last[4]}")
    assert last[0] == "280" and last[1] == "Polytomic" and last[3] == "support@polytomic.com"

    rows_check2 = parse_csv(LEADS_WITH_EMAILS_CSV)
    last2 = rows_check2[-1]
    print(f"leads_with_emails.csv: appended lead_index={last2[0]} company={last2[1]} best_email={last2[8]}")
    assert last2[0] == "280" and last2[1] == "Polytomic" and last2[8] == "support@polytomic.com"

    # dedupe invariant
    from collections import Counter
    dupes1 = [k for k, c in Counter(r[0] for r in rows_check[1:]).items() if c > 1]
    dupes2 = [k for k, c in Counter(r[0] for r in rows_check2[1:]).items() if c > 1]
    assert not dupes1, f"leads.csv dupes: {dupes1}"
    assert not dupes2, f"leads_with_emails.csv dupes: {dupes2}"
    print(f"Total rows: leads.csv={len(rows_check)-1}, leads_with_emails.csv={len(rows_check2)-1}")
    print("OK: lead 280 (Polytomic) appended + parse-back verified + no dupes")


if __name__ == "__main__":
    main()