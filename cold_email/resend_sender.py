"""
Atlas Cold Email Sender — Resend Edition
Sends cold emails via Resend HTTP API (no SMTP needed, no infrastructure).
Resend free tier = 100 emails/day, 3,000/month.

Env vars needed:
- RESEND_API_KEY (get from https://resend.com/api-keys)
- FROM_EMAIL (must be verified domain, OR use onboarding@resend.dev for testing)
- FROM_NAME (e.g. "Atlas (TalonForge)")
- REPLY_TO (optional, e.g. zinou@potts.io)

Usage:
  python resend_sender.py --csv leads_clean.csv --template cold_email/templates/01-default.md --max 50
  python resend_sender.py --dry-run --csv leads_clean.csv --template cold_email/templates/01-default.md
"""

import os
import sys
import csv
import json
import time
import argparse
from pathlib import Path
from typing import List, Dict

import urllib.request
import urllib.error


RESEND_FREE_TIER_DAILY_LIMIT = 100
DELAY_BETWEEN_EMAILS_SECONDS = 2


def load_env():
    """Load env vars from ~/.hermes/.env (KEY=VALUE format, # comments)."""
    env_path = Path.home() / ".hermes" / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, val = line.split("=", 1)
            os.environ[key.strip()] = val.strip().strip('"').strip("'")


def load_leads(csv_path: str) -> List[Dict]:
    leads = []
    with open(csv_path, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("best_email"):
                leads.append(row)
    return leads


def load_template(template_path: str, lead: Dict) -> tuple:
    """Returns (subject, body). Template can use {{var}} placeholders."""
    raw = Path(template_path).read_text(encoding="utf-8")

    # Try to split on first blank line after a "Subject:" line
    subject = f"quick question about {lead.get('company', 'your work')}"
    body = raw

    # Look for explicit Subject: in template
    lines = raw.split("\n")
    new_lines = []
    in_subject = False
    for line in lines:
        if line.startswith("Subject:"):
            subject = line.replace("Subject:", "").strip()
            subject = subject.replace("{{company}}", lead.get("company", "your work"))
            subject = subject.replace("{{founder}}", lead.get("founder", "there"))
            in_subject = True
            continue
        if in_subject and line.strip() == "":
            in_subject = False
            continue
        if in_subject:
            subject += " " + line.strip()
            continue
        new_lines.append(line)
    body = "\n".join(new_lines)

    # Substitute placeholders
    for key, val in lead.items():
        body = body.replace("{{" + key + "}}", str(val) if val else "")

    # Also support common placeholders with fallbacks
    body = body.replace("{{company}}", lead.get("company", "your company"))
    body = body.replace("{{founder}}", lead.get("founder", "there"))
    body = body.replace("{{vertical}}", lead.get("vertical", "your space"))
    body = body.replace("{{website}}", lead.get("website", "your site"))

    return subject, body


def send_via_resend(to_email: str, subject: str, body: str, from_email: str, from_name: str, reply_to: str = None) -> Dict:
    """Send via Resend HTTP API."""
    payload = {
        "from": f"{from_name} <{from_email}>",
        "to": [to_email],
        "subject": subject,
        "text": body,
    }
    if reply_to:
        payload["reply_to"] = [reply_to]

    try:
        req = urllib.request.Request(
            "https://api.resend.com/emails",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {os.environ['RESEND_API_KEY']}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            return {"status": "sent", "code": resp.status, "to": to_email, "resend_id": data.get("id")}
    except urllib.error.HTTPError as e:
        return {"status": "error", "code": e.code, "to": to_email, "error": e.read().decode()[:300]}
    except Exception as e:
        return {"status": "error", "to": to_email, "error": str(e)[:300]}


def main(csv_path: str, template_path: str, dry_run: bool, max_emails: int):
    load_env()

    if not dry_run and not os.environ.get("RESEND_API_KEY"):
        print("[ERROR] RESEND_API_KEY not set in ~/.hermes/.env")
        print("[FIX] Sign up at https://resend.com (free, just email), then:")
        print("       1. Go to https://resend.com/api-keys")
        print("       2. Create API key")
        print("       3. Add to ~/.hermes/.env:  RESEND_API_KEY=re_xxxxxxxx")
        return 1

    leads = load_leads(csv_path)
    if not leads:
        print(f"[ERROR] No leads with emails in {csv_path}")
        return 1

    print(f"Loaded {len(leads)} leads. Will send to up to {max_emails}.")
    if dry_run:
        print("(DRY RUN — no actual emails sent)")

    from_email = os.environ.get("FROM_EMAIL", "onboarding@resend.dev")
    from_name = os.environ.get("FROM_NAME", "Atlas (TalonForge)")
    reply_to = os.environ.get("REPLY_TO")

    sent_log = []
    sent_count = 0

    for i, lead in enumerate(leads[:max_emails]):
        subject, body = load_template(template_path, lead)

        if dry_run:
            print(f"\n--- DRY RUN #{i+1} → {lead['best_email']} ---")
            print(f"Subject: {subject}")
            print(f"Body:\n{body[:400]}...")
            sent_log.append({"to": lead["best_email"], "company": lead["company"], "status": "dry_run"})
        else:
            result = send_via_resend(lead["best_email"], subject, body, from_email, from_name, reply_to)
            sent_log.append({"to": lead["best_email"], "company": lead["company"], **result})
            sent_count += 1
            status_icon = "[OK]" if result.get("status") == "sent" else "[ERR]"
            print(f"  [{i+1}/{min(len(leads), max_emails)}] {status_icon} {lead['best_email']} → {result.get('status')} {result.get('code', '')}")

            if sent_count >= RESEND_FREE_TIER_DAILY_LIMIT:
                print(f"\n[LIMIT] Hit Resend free tier ({RESEND_FREE_TIER_DAILY_LIMIT}). Stopping.")
                break

            time.sleep(DELAY_BETWEEN_EMAILS_SECONDS)

    log_path = "cold_email/send_log_resend.json"
    Path(log_path).parent.mkdir(exist_ok=True)
    with open(log_path, "w") as f:
        json.dump(sent_log, f, indent=2)

    actual_sent = sum(1 for r in sent_log if r.get("status") == "sent")
    print(f"\n=== RESULT: {actual_sent} sent, {len(sent_log) - actual_sent} skipped/error ===")
    print(f"Log saved to {log_path}")
    return 0


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--csv", default="leads_clean.csv")
    p.add_argument("--template", default="cold_email/templates/01-default.md")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--max", type=int, default=50)
    args = p.parse_args()
    sys.exit(main(args.csv, args.template, args.dry_run, args.max))
