# Atlas Cold Email System

Pure-Python cold email system with three send paths: SMTP (`sender.py`), Resend HTTP API (`resend_sender.py`), and SendGrid API (`sendgrid_sender.py`).

## Status (2026-07-12)

✅ **133 researched leads by max lead index** in `cold_email/leads.csv`.
✅ **106 send-ready leads with usable public emails** exported to `cold_email/leads_with_emails.csv` and root `leads_with_emails.csv`.
✅ **Provider senders verified in dry-run mode** against the exported CSV (Resend + SendGrid both render lead-specific templates correctly).
⏳ **Needs one sending credential** to actually send: `RESEND_API_KEY`, `SENDGRID_API_KEY`, or SMTP credentials.

## Files

- `sender.py` — SMTP-based sender with rate limiting (stdlib).
- `resend_sender.py` — Resend HTTP API sender; reads `cold_email/leads_with_emails.csv` by default.
- `sendgrid_sender.py` — SendGrid API sender; reads `cold_email/leads_with_emails.csv` by default.
- `export_send_ready.py` — bridge script that exports `cold_email/leads.csv` into send-ready CSVs with `best_email`; missing legacy template references fall back to `01-default.md`.
- `leads.csv` — canonical researched lead ledger.
- `leads_with_emails.csv` — send-ready export for API senders.
- `templates/*.md` — personalized email templates per lead, each with a `**Subject:**` line.
- `.env.example` — copy to `.env` and fill in SMTP credentials if using `sender.py`.
- `README.md` — this file

## Setup (5 minutes)

### Option A: Resend API (fastest for this repo)

1. Create a free API key: https://resend.com/api-keys
2. Add it to `~/.hermes/.env`:
   ```
   RESEND_API_KEY=re_xxxxxxxx
   FROM_EMAIL=onboarding@resend.dev
   FROM_NAME=Atlas (TalonForge)
   REPLY_TO=your-email@example.com
   ```
3. Refresh the send-ready export and dry-run:
   ```
   python cold_email/export_send_ready.py
   python cold_email/resend_sender.py --dry-run --max 5
   ```
4. Send a small batch:
   ```
   python cold_email/resend_sender.py --max 10
   ```

### Option B: SendGrid API

1. Create a SendGrid API key.
2. Add it to `~/.hermes/.env`:
   ```
   SENDGRID_API_KEY=SG.xxxxxxxx
   FROM_EMAIL=atlas@talonforge.io
   FROM_NAME=Atlas (TalonForge)
   REPLY_TO=your-email@example.com
   ```
3. Refresh the export and dry-run:
   ```
   python cold_email/export_send_ready.py
   python cold_email/sendgrid_sender.py --dry-run --max 5
   ```
4. Send a small batch:
   ```
   python cold_email/sendgrid_sender.py --max 10
   ```

### Option C: Gmail SMTP

1. Enable 2FA on your Google account: https://myaccount.google.com/security
2. Generate an App Password: https://myaccount.google.com/apppasswords
   - App name: `atlas-cold-email`
   - Copy the 16-character password
3. Copy `.env.example` to `.env`:
   ```
   cp .env.example .env
   ```
4. Edit `.env` and fill in:
   ```
   SMTP_USERNAME=your-email@gmail.com
   SMTP_PASSWORD=your-16-char-app-password
   FROM_EMAIL=your-email@gmail.com
   ```
5. Test it:
   ```
   python cold_email/sender.py --dry-run --test your-email@gmail.com
   python cold_email/sender.py --test your-email@gmail.com  # actually sends
   ```

### Option D: Other SMTP providers

Set the SMTP credentials in `.env` to your provider's SMTP settings. Sender works with any SMTP relay.

### Option E: Outlook / Office 365

Change `SMTP_HOST=smtp-mail.outlook.com` in `.env`.

## Send-Ready Lead Export

`cold_email/leads.csv` is the canonical research ledger. Run this before any API send:

```bash
python cold_email/export_send_ready.py
```

It writes both:

- `cold_email/leads_with_emails.csv` — canonical send-ready CSV for `resend_sender.py` and `sendgrid_sender.py`.
- `leads_with_emails.csv` — root compatibility copy for older scripts.

The export filters placeholders (`example.invalid`, `name@website.com`, `your@email.here`) and keeps only parseable public email addresses. When a historical `leads.csv` row references a template file that no longer exists, the export keeps the lead sendable by falling back to `01-default.md`.

## Usage

```bash
# Refresh send-ready export
python cold_email/export_send_ready.py

# Resend API dry run (preferred once RESEND_API_KEY exists)
python cold_email/resend_sender.py --dry-run --max 5

# SendGrid API dry run
python cold_email/sendgrid_sender.py --dry-run --max 5

# SMTP dry run (default — safe)
python cold_email/sender.py --dry-run --limit 5

# SMTP send 5 emails
python cold_email/sender.py --send --limit 5

# SMTP send only specific leads (by index)
python cold_email/sender.py --send --only index=05,07

# SMTP send to specific vertical only
python cold_email/sender.py --send --vertical indie_saas

# SMTP test mode — render template 01 and send to your own email
python cold_email/sender.py --test your@email.com

# Default SMTP safety: max 50 emails/hour (configurable via RATE_PER_HOUR)
```

## Safety Features

- **Default dry-run** — you must pass `--send` to actually send
- **Rate limit** — max 50/hour, state persisted across restarts
- **SMTP validation** — refuses to run without SMTP creds
- **Subject prefix** — leave blank or set to `[Atlas]` for tracking
- **CC self** — set `CC_SELF=true` to archive every email

## Expected Results (Honest Estimate)

Cold email to researched AI-agent / SaaS / compliance leads with public contact addresses:
- Open rate: 30-50%
- Click rate: 5-12%
- Reply rate: 2-6%
- Conversion to $500 audit: 1-3%

106 send-ready emails × 1-3% conversion = 1-3 possible audits = $500-$1,500 from this batch once a sending credential is added.

The real value: this builds a template library you can reuse for the next 100 leads. After 2-3 batches you'll have a system that reliably generates 1-3 audits/month from cold outreach alone.

## When to Stop

If after 50 cold emails you have <2% open rate, your subject lines need work. If you have >30% open but <1% reply, your body copy needs work. If you have >5% reply but <1% conversion, your CTA (the audit offer) needs work.

Iterate on the templates in `templates/` based on reply patterns.

## Compliance Note

Sending cold email is legal in the US under CAN-SPAM (you need: real physical address in footer, unsubscribe mechanism, accurate subject lines, honor opt-outs within 10 days). For international recipients, check local laws (GDPR in EU is stricter).

For now: keep volume low (50/day max), include a clear "this is a one-time cold email" line, and reply promptly to any opt-outs.

## Files Updated 2026-07-12

- `export_send_ready.py` — exports 106 usable public-email leads to `leads_with_emails.csv`.
- `resend_sender.py` — default CSV now `cold_email/leads_with_emails.csv`; renders lead-specific markdown templates.
- `sendgrid_sender.py` — default CSV now `cold_email/leads_with_emails.csv`; renders lead-specific markdown templates.
- `README.md` — updated setup and usage for Resend / SendGrid / SMTP.

## Files Created 2026-07-11

- `sender.py` — main script
- `leads.csv` — 19 leads
- `templates/01-19*.md` — 19 personalized templates
- `.env.example` — config template
- `README.md` — this file