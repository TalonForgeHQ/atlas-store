"""
Export Atlas' researched leads into provider-ready lead CSVs.

Input:  cold_email/leads.csv (canonical researched lead ledger)
Output: cold_email/leads_with_emails.csv and root leads_with_emails.csv

Why this exists: the SMTP sender reads cold_email/leads.csv directly, while
Resend/SendGrid sender paths expect a `best_email` column. This bridge makes
the researched 133-lead ledger immediately usable by API senders once the user
adds RESEND_API_KEY or SENDGRID_API_KEY.
"""
from __future__ import annotations

import csv
import re
from email.utils import parseaddr
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "cold_email" / "leads.csv"
OUTPUTS = [
    ROOT / "cold_email" / "leads_with_emails.csv",
    ROOT / "leads_with_emails.csv",
]

FIELDNAMES = [
    "lead_index",
    "company",
    "handle",
    "domain",
    "website",
    "founder",
    "vertical",
    "tier",
    "best_email",
    "emails_found",
    "guessed_emails",
    "source_template",
    "tier_reason",
]

BAD_EMAIL_PARTS = (
    "example.",
    "example@",
    "@example",
    ".invalid",
    "your@email",
    "name@website",
    "youremail",
    "email.com",
    "domain.com",
)


def clean_email(value: str) -> str:
    """Return the first usable email from a cell that may contain commas/semicolons."""
    for piece in re.split(r"[;,\s]+", value or ""):
        piece = piece.strip().strip('"').strip("'")
        if not piece:
            continue
        _, addr = parseaddr(piece)
        addr = addr.strip().lower()
        if not addr or "@" not in addr:
            continue
        if any(bad in addr for bad in BAD_EMAIL_PARTS):
            continue
        # Basic, conservative public-email shape check.
        if not re.fullmatch(r"[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}", addr):
            continue
        return addr
    return ""


def domain_from(email: str, handle: str = "") -> str:
    if email and "@" in email:
        return email.split("@", 1)[1].lower()
    handle = (handle or "").lstrip("@").strip().lower()
    return f"{handle}.com" if handle else ""


def website_from(domain: str) -> str:
    if not domain:
        return ""
    parsed = urlparse(domain if "://" in domain else f"https://{domain}")
    host = parsed.netloc or parsed.path
    return f"https://{host}" if host else ""


def extract_founder(row: dict[str, str]) -> str:
    """Best-effort founder/CEO extraction from the researched tier_reason text."""
    text = row.get("tier_reason", "") or ""
    patterns = [
        r"CEO\s+([A-Z][A-Za-zÀ-ÖØ-öø-ÿ'\-]+(?:\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'\-]+){0,3})",
        r"founder/CEO\s+([A-Z][A-Za-zÀ-ÖØ-öø-ÿ'\-]+(?:\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'\-]+){0,3})",
        r"founder\s+([A-Z][A-Za-zÀ-ÖØ-öø-ÿ'\-]+(?:\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'\-]+){0,3})",
        r"founders?\s+([A-Z][A-Za-zÀ-ÖØ-öø-ÿ'\-]+(?:\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'\-]+){0,3})",
        r"co-founders?\s+([A-Z][A-Za-zÀ-ÖØ-öø-ÿ'\-]+(?:\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'\-]+){0,3})",
    ]
    for pat in patterns:
        m = re.search(pat, text)
        if m:
            name = re.split(r"\s+(?:and|\+|ex-|with|verified|co-founder|founder|CEO)\b", m.group(1).strip())[0]
            return name.strip(" ,.;:-") or "there"
    return "there"


def existing_template_or_default(template_name: str) -> str:
    """Keep source_template sendable even when the research ledger points at an old/missing file."""
    template_name = (template_name or "").strip()
    if template_name and (ROOT / "cold_email" / "templates" / template_name).exists():
        return template_name
    return "01-default.md"


def build_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with INPUT.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            email = clean_email(row.get("email", ""))
            if not email:
                continue
            domain = domain_from(email, row.get("handle", ""))
            rows.append({
                "lead_index": (row.get("index") or "").strip(),
                "company": (row.get("name") or "").strip(),
                "handle": (row.get("handle") or "").strip(),
                "domain": domain,
                "website": website_from(domain),
                "founder": extract_founder(row),
                "vertical": (row.get("vertical") or "").strip(),
                "tier": (row.get("tier") or "").strip(),
                "best_email": email,
                "emails_found": email,
                "guessed_emails": "",
                "source_template": existing_template_or_default(row.get("template", "")),
                "tier_reason": (row.get("tier_reason") or "").strip(),
            })
    return rows


def write_rows(rows: list[dict[str, str]]) -> None:
    for output in OUTPUTS:
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)


def main() -> int:
    rows = build_rows()
    write_rows(rows)
    print(f"Exported {len(rows)} send-ready leads from {INPUT}")
    for output in OUTPUTS:
        print(f"- {output}")
    fallback_count = sum(1 for r in rows if r.get("source_template") == "01-default.md")
    if fallback_count:
        print(f"Fallback templates: {fallback_count} rows use 01-default.md")
    if rows:
        print(f"First: {rows[0]['lead_index']} {rows[0]['company']} -> {rows[0]['best_email']}")
        print(f"Last:  {rows[-1]['lead_index']} {rows[-1]['company']} -> {rows[-1]['best_email']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
