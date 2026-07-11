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
  python resend_sender.py --csv cold_email/leads_with_emails.csv --max 50
  python resend_sender.py --dry-run --csv cold_email/leads_with_emails.csv --max 5
"""

import os
import sys
import csv
import json
import time
import argparse
import re
from pathlib import Path
from typing import List, Dict, Tuple
from email.utils import parseaddr

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
    """Returns (subject, body). Supports legacy Subject: and current **Subject:** markdown."""
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


def load_template(template_path: str, lead: Dict) -> tuple:
    """Returns (subject, body). Template can use {{var}} placeholders."""
    raw = Path(template_path).read_text(encoding="utf-8")
    return render_template(raw, lead)


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
            print(f"Body:\n{body[:400]}...")
            sent_log.append({"to": to_email, "company": lead["company"], "template": template_to_use, "status": "dry_run"})
        else:
            result = send_via_resend(to_email, subject, body, from_email, from_name, reply_to)
            sent_log.append({"to": to_email, "company": lead["company"], "template": template_to_use, **result})
            sent_count += 1
            status_icon = "[OK]" if result.get("status") == "sent" else "[ERR]"
            print(f"  [{i+1}/{min(len(leads), max_emails)}] {status_icon} {to_email} → {result.get('status')} {result.get('code', '')}")

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
    p.add_argument("--csv", default="cold_email/leads_with_emails.csv")
    p.add_argument("--template", default="cold_email/templates/01-default.md")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--max", type=int, default=50)
    args = p.parse_args()
    sys.exit(main(args.csv, args.template, args.dry_run, args.max))
