"""
Atlas Cold Email Sender — SendGrid Edition
Sends personalized 3-line emails using the SendGrid API (free tier = 100/day).
Reads leads from leads_with_emails.csv (or any CSV with 'best_email' + 'company' + 'founder' columns).

Env vars needed:
- SENDGRID_API_KEY
- FROM_EMAIL (e.g. atlas@talonforge.io)
- FROM_NAME (e.g. Atlas)
- REPLY_TO (e.g. zinou@potts.io)
"""

import os
import sys
import csv
import time
import json
from pathlib import Path
from typing import List, Dict

try:
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail, Email, To, Content, Personalization
    SENDGRID_AVAILABLE = True
except ImportError:
    SENDGRID_AVAILABLE = False


SENDGRID_FREE_TIER_DAILY_LIMIT = 100
DELAY_BETWEEN_EMAILS_SECONDS = 2  # 2s = 30/min = ~12s/email avg


def load_env():
    env_path = Path.home() / ".hermes" / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, val = line.split("=", 1)
                os.environ[key.strip()] = val.strip().strip('"').strip("'")


def load_leads(csv_path: str) -> List[Dict]:
    leads = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("best_email"):
                leads.append(row)
    return leads


def load_template(template_path: str, lead: Dict) -> str:
    template = Path(template_path).read_text(encoding="utf-8")
    return (
        template
        .replace("{{company}}", lead.get("company", "your company"))
        .replace("{{founder}}", lead.get("founder", "there"))
        .replace("{{vertical}}", lead.get("vertical", "your space"))
        .replace("{{website}}", lead.get("website", "your site"))
    )


def send_via_sendgrid(to_email: str, subject: str, body: str, from_email: str, from_name: str) -> Dict:
    if not SENDGRID_AVAILABLE:
        return {"status": "skipped", "reason": "sendgrid not installed"}
    try:
        message = Mail(
            from_email=Email(from_email, from_name),
            to_emails=To(to_email),
            subject=subject,
            plain_text_content=Content("text/plain", body),
        )
        sg = SendGridAPIClient(os.environ["SENDGRID_API_KEY"])
        response = sg.send(message)
        return {"status": "sent", "code": response.status_code, "to": to_email}
    except Exception as e:
        return {"status": "error", "error": str(e), "to": to_email}


def main(csv_path: str = "leads_with_emails.csv", template_path: str = "cold_email/templates/01-default.md", dry_run: bool = False, max_emails: int = 50):
    load_env()

    if not dry_run:
        if not os.environ.get("SENDGRID_API_KEY"):
            print("[ERROR] SENDGRID_API_KEY not set in ~/.hermes/.env")
            return 1

    leads = load_leads(csv_path)
    if not leads:
        print(f"[ERROR] No leads with emails found in {csv_path}")
        return 1

    print(f"Loaded {len(leads)} leads from {csv_path}")

    from_email = os.environ.get("FROM_EMAIL", "atlas@talonforge.io")
    from_name = os.environ.get("FROM_NAME", "Atlas (TalonForge)")

    # Read template
    if not Path(template_path).exists():
        print(f"[ERROR] Template not found: {template_path}")
        return 1

    sent_log = []
    sent_count = 0

    for i, lead in enumerate(leads[:max_emails]):
        body = load_template(template_path, lead)
        subject = f"quick question about {lead.get('company', 'your work')}"

        if dry_run:
            print(f"\n--- DRY RUN #{i+1} → {lead['best_email']} ---")
            print(f"Subject: {subject}")
            print(f"Body:\n{body[:500]}")
            sent_log.append({"to": lead["best_email"], "company": lead["company"], "status": "dry_run"})
        else:
            result = send_via_sendgrid(lead["best_email"], subject, body, from_email, from_name)
            print(f"  [{i+1}/{min(len(leads), max_emails)}] {lead['best_email']} → {result['status']}")
            sent_log.append({"to": lead["best_email"], "company": lead["company"], **result})
            sent_count += 1

            if sent_count >= SENDGRID_FREE_TIER_DAILY_LIMIT:
                print(f"\n[LIMIT] Hit SendGrid free tier limit ({SENDGRID_FREE_TIER_DAILY_LIMIT}). Stopping.")
                break

            time.sleep(DELAY_BETWEEN_EMAILS_SECONDS)

    log_path = "cold_email/send_log.json"
    with open(log_path, "w") as f:
        json.dump(sent_log, f, indent=2)

    actual_sent = sum(1 for r in sent_log if r.get("status") == "sent")
    print(f"\n=== RESULT: {actual_sent} sent, {len(sent_log) - actual_sent} skipped/error ===")
    print(f"Log saved to {log_path}")
    return 0


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--csv", default="leads_with_emails.csv")
    p.add_argument("--template", default="cold_email/templates/01-default.md")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--max", type=int, default=50)
    args = p.parse_args()

    sys.exit(main(args.csv, args.template, args.dry_run, args.max))
