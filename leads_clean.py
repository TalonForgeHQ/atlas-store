"""
Quick cleaner for leads_with_emails.csv - removes placeholder emails.
"""
import csv

input_path = "leads_with_emails.csv"
output_path = "leads_clean.csv"

PLACEHOLDERS = ["your@email.here", "name@website.com", "email@example.com", "you@example.com"]

with open(input_path, "r", encoding="utf-8") as f_in, open(output_path, "w", newline="", encoding="utf-8") as f_out:
    reader = csv.DictReader(f_in)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(f_out, fieldnames=fieldnames)
    writer.writeheader()

    kept = 0
    replaced = 0
    removed = 0

    for row in reader:
        email = row.get("best_email", "")
        if any(p in email.lower() for p in PLACEHOLDERS):
            # Replace with founder-based guess
            founder = row.get("founder", "").strip()
            domain = row.get("domain", "").strip()
            if founder and domain:
                parts = founder.lower().split()
                if len(parts) >= 2:
                    # Try first.last@domain
                    guessed = f"{parts[0]}.{parts[-1]}@{domain}"
                    row["best_email"] = guessed
                    row["emails_found"] = ""
                    writer.writerow(row)
                    replaced += 1
                    continue
            # Otherwise skip
            removed += 1
            continue
        writer.writerow(row)
        kept += 1

print(f"Kept: {kept}")
print(f"Replaced (placeholder → founder guess): {replaced}")
print(f"Removed (no email + no founder): {removed}")
print(f"Saved to {output_path}")
