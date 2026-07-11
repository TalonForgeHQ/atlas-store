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
import re
from pathlib import Path
from typing import List, Dict, Tuple
from email.utils import parseaddr

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
            if row.get("best_email") or row.get("email"):
                leads.append(normalize_lead(row))
    return leads


def normalize_lead(row: Dict) -> Dict:
    """Normalize either lead_finder export or cold_email/leads.csv rows."""
    email = (row.get("best_email") or row.get("email") or "").strip()
    company = (row.get("company") or row.get("name") or "").strip()
    founder = (row.get("founder") or "there").strip() or "there"
    website = (row.get("website") or "").strip()
    domain = (row.get("domain") or "").strip()
    if not website and domain:
        website = f"https://{domain}"
    normalized = dict(row)
    normalized.update({
        "best_email": email,
        "email": email,
        "company": company,
        "name": company,
        "founder": founder,
        "website": website,
        "domain": domain,
        "vertical": (row.get("vertical") or "your space").strip(),
        "template": (row.get("template") or row.get("source_template") or "").strip(),
        "tier_reason": (row.get("tier_reason") or "").strip(),
    })
    return normalized


SUBJECT_MD_RE = re.compile(r"^\*\*Subject:\*\*\s*(.+?)\s*$", re.MULTILINE)


def render_template(raw: str, lead: Dict) -> Tuple[str, str]:
    """Render both legacy Subject: templates and current **Subject:** markdown templates."""
    subject = f"quick question about {lead.get('company', 'your work')}"
    body = raw

    md_match = SUBJECT_MD_RE.search(body)
    if md_match:
        subject = md_match.group(1).strip()
        body = (body[:md_match.start()] + body[md_match.end():]).strip()
    else:
        lines = raw.split("\n")
        new_lines = []
        in_subject = False
        for line in lines:
            if line.startswith("Subject:"):
                subject = line.replace("Subject:", "").strip()
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

    # Drop metadata comments used by the per-lead templates.
    body_lines = []
    skipping_header = True
    for line in body.splitlines():
        if skipping_header and line.lstrip().startswith("#"):
            continue
        skipping_header = False
        body_lines.append(line)
    body = "\n".join(body_lines).strip()

    for key, val in lead.items():
        replacement = str(val) if val else ""
        subject = subject.replace("{{" + key + "}}", replacement)
        body = body.replace("{{" + key + "}}", replacement)

    for key, fallback in {
        "company": "your company",
        "name": "your company",
        "founder": "there",
        "vertical": "your space",
        "website": "your site",
        "domain": "your domain",
        "best_email": "",
        "email": "",
    }.items():
        subject = subject.replace("{{" + key + "}}", lead.get(key, fallback) or fallback)
        body = body.replace("{{" + key + "}}", lead.get(key, fallback) or fallback)

    return subject, body


def load_template(template_path: str, lead: Dict) -> Tuple[str, str]:
    template = Path(template_path).read_text(encoding="utf-8")
    return render_template(template, lead)


def template_for_lead(lead: Dict, default_template: str) -> str:
    """Use the lead-specific template when present; fall back to the CLI template."""
    candidate = lead.get("template", "")
    if candidate:
        path = Path(candidate)
        if not path.is_absolute():
            if not str(path).startswith("cold_email"):
                path = Path("cold_email") / "templates" / candidate
        if path.exists():
            return str(path)
    return default_template


def parse_recipients(value: str) -> List[str]:
    """Parse comma/semicolon-separated recipient addresses for verification + send."""
    out = []
    for piece in re.split(r"[;,]", value or ""):
        piece = piece.strip()
        if not piece:
            continue
        _, addr = parseaddr(piece)
        if addr and "@" in addr:
            out.append(addr)
    return out


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


def main(csv_path: str = "cold_email/leads_with_emails.csv", template_path: str = "cold_email/templates/01-default.md", dry_run: bool = False, max_emails: int = 50):
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
        template_to_use = template_for_lead(lead, template_path)
        subject, body = load_template(template_to_use, lead)
        recipients = parse_recipients(lead["best_email"])
        if not recipients:
            print(f"  [{i+1}/{min(len(leads), max_emails)}] SKIP {lead.get('company', '')} — invalid email: {lead['best_email']!r}")
            sent_log.append({"to": lead["best_email"], "company": lead["company"], "status": "skipped", "reason": "invalid_email"})
            continue
        to_email = recipients[0]

        if dry_run:
            print(f"\n--- DRY RUN #{i+1} → {to_email} ---")
            print(f"Template: {template_to_use}")
            print(f"Subject: {subject}")
            print(f"Body:\n{body[:500]}")
            sent_log.append({"to": to_email, "company": lead["company"], "template": template_to_use, "status": "dry_run"})
        else:
            result = send_via_sendgrid(to_email, subject, body, from_email, from_name)
            print(f"  [{i+1}/{min(len(leads), max_emails)}] {to_email} → {result['status']}")
            sent_log.append({"to": to_email, "company": lead["company"], "template": template_to_use, **result})
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
    p.add_argument("--csv", default="cold_email/leads_with_emails.csv")
    p.add_argument("--template", default="cold_email/templates/01-default.md")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--max", type=int, default=50)
    args = p.parse_args()

    sys.exit(main(args.csv, args.template, args.dry_run, args.max))
