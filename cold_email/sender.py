"""
Atlas cold-email sender — pure Python smtplib + rate limiting.

Usage:
    python sender.py --dry-run                    # default: print, don't send
    python sender.py --send                       # actually send
    python sender.py --send --limit 10            # send first 10 only
    python sender.py --send --only index=05,07    # send specific leads only
    python sender.py --test your@email.com        # send one test email to yourself

Required env (via .env in this directory):
    SMTP_HOST, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD
    FROM_EMAIL, FROM_NAME
    DRY_RUN (true/false)

The 19 leads and templates live in:
    ../leads.csv              — index, name, handle, email, vertical, tier, template
    ./templates/*.md          — markdown with `**Subject:**` line + body

Before sending:
    1. Fill in SMTP credentials in .env (see .env.example)
    2. Fill in `email` column of leads.csv for each recipient (the seed list
       only has Twitter handles, so emails must be researched/provided by you)
    3. Run with --dry-run first to inspect
    4. Run with --send to actually send

Rate limiting:
    Max 50/hour (configurable via RATE_PER_HOUR). State persisted to
    .send_state.json so the cap survives restarts.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import smtplib
import ssl
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timedelta
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
LEADS_CSV = BASE_DIR / "leads.csv"
ENV_PATH = BASE_DIR / ".env"
STATE_PATH = BASE_DIR / ".send_state.json"


# --------------------------------------------------------------------------- env
def load_env() -> dict[str, str]:
    """Tiny .env loader — no python-dotenv dependency."""
    env: dict[str, str] = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            env[k.strip()] = v.strip().strip('"').strip("'")
    # Allow real env vars to override (useful for CI)
    for k in (
        "SMTP_HOST", "SMTP_PORT", "SMTP_USERNAME", "SMTP_PASSWORD",
        "FROM_EMAIL", "FROM_NAME", "REPLY_TO",
        "RATE_PER_HOUR", "SUBJECT_PREFIX", "CC_SELF", "CC_EMAIL",
        "DRY_RUN",
    ):
        if k in os.environ:
            env[k] = os.environ[k]
    return env


def require(env: dict[str, str], key: str) -> str:
    if key not in env or not env[key]:
        print(f"ERROR: missing {key} in .env", file=sys.stderr)
        sys.exit(2)
    return env[key]


# --------------------------------------------------------------------------- leads
@dataclass
class Lead:
    index: str
    name: str
    handle: str
    email: str
    vertical: str
    tier: str
    template: str
    tier_reason: str = ""


def load_leads() -> list[Lead]:
    if not LEADS_CSV.exists():
        print(f"ERROR: {LEADS_CSV} not found", file=sys.stderr)
        sys.exit(2)
    leads: list[Lead] = []
    with LEADS_CSV.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            leads.append(Lead(
                index=row["index"].strip(),
                name=row["name"].strip(),
                handle=row["handle"].strip(),
                email=row["email"].strip(),
                vertical=row["vertical"].strip(),
                tier=row["tier"].strip(),
                template=row["template"].strip(),
                tier_reason=row.get("tier_reason", "").strip(),
            ))
    return leads


# --------------------------------------------------------------------------- template
SUBJECT_RE = re.compile(r"^\*\*Subject:\*\*\s*(.+?)\s*$", re.MULTILINE)


def render_template(lead: Lead) -> tuple[str, str]:
    """Returns (subject, body). Strips metadata header + the Subject line."""
    tpl_path = TEMPLATES_DIR / lead.template
    if not tpl_path.exists():
        raise FileNotFoundError(f"template not found: {tpl_path}")
    raw = tpl_path.read_text(encoding="utf-8")

    # Strip metadata block (leading lines starting with #)
    body_lines = []
    in_meta = True
    for line in raw.splitlines():
        if in_meta and line.lstrip().startswith("#"):
            continue
        in_meta = False
        body_lines.append(line)
    body = "\n".join(body_lines).strip()

    # Extract subject
    m = SUBJECT_RE.search(body)
    if not m:
        raise ValueError(f"no '**Subject:**' line in {tpl_path}")
    subject = m.group(1).strip()
    body = (body[: m.start()] + body[m.end():]).strip()

    return subject, body


# --------------------------------------------------------------------------- rate limit
@dataclass
class SendState:
    sent_at: list[float]  # unix timestamps

    @classmethod
    def load(cls) -> "SendState":
        if STATE_PATH.exists():
            data = json.loads(STATE_PATH.read_text(encoding="utf-8"))
            return cls(sent_at=data.get("sent_at", []))
        return cls(sent_at=[])

    def save(self) -> None:
        STATE_PATH.write_text(
            json.dumps({"sent_at": self.sent_at}, indent=2),
            encoding="utf-8",
        )

    def prune(self, window_seconds: int = 3600) -> None:
        cutoff = time.time() - window_seconds
        self.sent_at = [t for t in self.sent_at if t >= cutoff]

    def can_send(self, max_per_hour: int) -> bool:
        self.prune()
        return len(self.sent_at) < max_per_hour

    def wait_until_next_slot(self, max_per_hour: int) -> float:
        """If at cap, return seconds until oldest send ages out of the window."""
        self.prune()
        if len(self.sent_at) < max_per_hour:
            return 0.0
        oldest = min(self.sent_at)
        return max(0.0, (oldest + 3600) - time.time())

    def record(self) -> None:
        self.sent_at.append(time.time())
        self.save()


# --------------------------------------------------------------------------- smtp
def build_message(env: dict[str, str], to_email: str, to_name: str,
                 subject: str, body: str) -> EmailMessage:
    msg = EmailMessage()
    msg["From"] = formataddr((env.get("FROM_NAME", "Atlas"), env["FROM_EMAIL"]))
    msg["To"] = formataddr((to_name, to_email))
    if env.get("REPLY_TO"):
        msg["Reply-To"] = env["REPLY_TO"]
    if env.get("CC_SELF", "").lower() == "true" and env.get("CC_EMAIL"):
        msg["Cc"] = env["CC_EMAIL"]
    full_subject = f"{env.get('SUBJECT_PREFIX', '')}{subject}".strip()
    msg["Subject"] = full_subject
    msg["Date"] = format_datetime_local(datetime.now())
    msg.set_content(body)
    return msg


def format_datetime_local(dt: datetime) -> str:
    return dt.strftime("%a, %d %b %Y %H:%M:%S %z")


def smtp_send(env: dict[str, str], msg: EmailMessage) -> None:
    host = env["SMTP_HOST"]
    port = int(env.get("SMTP_PORT", "587"))
    user = env["SMTP_USERNAME"]
    pw = env["SMTP_PASSWORD"]

    with smtplib.SMTP(host, port, timeout=30) as s:
        s.ehlo()
        s.starttls(context=ssl.create_default_context())
        s.ehlo()
        s.login(user, pw)
        recipients = [addr for _, addr in (msg["To"].addresses if hasattr(msg["To"], "addresses") else [(None, msg["To"])])]
        # EmailMessage["To"] returns a Header; simpler: use msg.get_all
        to_addrs = []
        for hdr in (msg.get_all("To") or []) + (msg.get_all("Cc") or []):
            for _, addr in [a for a in (s.getaddresses([hdr]) if False else [(None, h.strip()) for h in hdr.split(",")])]:
                if addr:
                    to_addrs.append(addr)
        if not to_addrs:
            to_addrs = [env["FROM_EMAIL"]]
        s.send_message(msg, to_addrs=to_addrs)


# --------------------------------------------------------------------------- main
def parse_only(value: str) -> set[str]:
    """Parse --only index=01,02,07 → {'01','02','07'}"""
    if not value:
        return set()
    if "=" in value:
        _, _, v = value.partition("=")
        return {x.strip() for x in v.split(",") if x.strip()}
    return {x.strip() for x in value.split(",") if x.strip()}


def main() -> None:
    p = argparse.ArgumentParser(description="Atlas cold-email sender")
    p.add_argument("--send", action="store_true", help="actually send (override DRY_RUN)")
    p.add_argument("--dry-run", action="store_true", help="print only, don't send (override DRY_RUN)")
    p.add_argument("--limit", type=int, default=0, help="max emails to send (0=all)")
    p.add_argument("--only", type=str, default="", help="only these lead indexes, e.g. 05,07")
    p.add_argument("--test", type=str, default="", help="send one test email to this address")
    p.add_argument("--vertical", type=str, default="", help="only send to leads in this vertical")
    args = p.parse_args()

    env = load_env()

    # DRY_RUN precedence: CLI flag > env > default True
    if args.send:
        dry_run = False
    elif args.dry_run:
        dry_run = True
    else:
        dry_run = env.get("DRY_RUN", "true").lower() != "false"

    rate_per_hour = int(env.get("RATE_PER_HOUR", "50"))
    state = SendState.load()

    leads = load_leads()
    only = parse_only(args.only)
    if only:
        leads = [l for l in leads if l.index in only]
    if args.vertical:
        leads = [l for l in leads if l.vertical == args.vertical]
    if args.limit:
        leads = leads[: args.limit]

    # Test mode — render template #01, send only to user-provided address
    if args.test:
        if not leads:
            print("ERROR: no leads loaded; can't render template for test", file=sys.stderr)
            sys.exit(2)
        subject, body = render_template(leads[0])
        msg = build_message(env, args.test, "Test Recipient", subject, body)
        print("=" * 70)
        print(f"TEST MODE → {args.test}")
        print(f"Subject: {msg['Subject']}")
        print("-" * 70)
        print(msg.get_content())
        print("=" * 70)
        if not dry_run:
            require(env, "SMTP_HOST"); require(env, "SMTP_PASSWORD")
            smtp_send(env, msg)
            print(f"✓ Sent test email to {args.test}")
        else:
            print("[DRY RUN] would have sent above")
        return

    # Normal send loop
    sent = 0
    skipped_no_email = 0
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] Atlas cold-email sender")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE SEND'}")
    print(f"Rate cap: {rate_per_hour}/hour (state: {len(state.sent_at)} sent in last hour)")
    print(f"Leads loaded: {len(leads)}")
    print()

    for lead in leads:
        if not lead.email:
            print(f"  [{lead.index}] SKIP {lead.name} ({lead.handle}) — no email in leads.csv")
            skipped_no_email += 1
            continue

        if not dry_run and not state.can_send(rate_per_hour):
            wait = state.wait_until_next_slot(rate_per_hour)
            wait = min(wait, 60)  # cap single wait at 60s, then re-check
            print(f"  RATE CAP hit — sleeping {wait:.0f}s...")
            time.sleep(wait)

        try:
            subject, body = render_template(lead)
        except Exception as e:
            print(f"  [{lead.index}] TEMPLATE ERROR {lead.name}: {e}")
            continue

        msg = build_message(env, lead.email, lead.name, subject, body)

        print(f"  [{lead.index}] → {lead.email}  ({lead.name}, {lead.vertical})")
        print(f"      Subject: {msg['Subject']}")

        if dry_run:
            preview = body.replace("\n", "\n      ")[: 400]
            print(f"      Preview: {preview}{'...' if len(body) > 400 else ''}")
            sent += 1
        else:
            try:
                require(env, "SMTP_HOST"); require(env, "SMTP_PASSWORD")
                smtp_send(env, msg)
                state.record()
                sent += 1
                print(f"      ✓ sent")
            except smtplib.SMTPAuthenticationError as e:
                print(f"      ✗ AUTH FAILED — check SMTP_USERNAME / SMTP_PASSWORD: {e}")
                print("      (If Gmail: make sure you're using an App Password, not your real password.)")
                sys.exit(3)
            except Exception as e:
                print(f"      ✗ ERROR: {e}")
                continue

        # Polite pacing in live mode (~72s between sends = 50/hr, ~30s = 120/hr)
        if not dry_run:
            pace = 3600.0 / max(rate_per_hour, 1)
            time.sleep(min(pace, 5))  # never sleep more than 5s per send

    print()
    print(f"Done. sent={sent}  skipped_no_email={skipped_no_email}  total={len(leads)}")


if __name__ == "__main__":
    main()