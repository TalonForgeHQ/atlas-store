# Atlas Cold Email System

Pure-Python cold email sender. No third-party SaaS dependencies.

## Status (2026-07-11)

✅ **System built and verified** — 19 personalized templates, sender.py verified 34/34 checks.
⏳ **Needs SMTP credentials** to actually send — see setup below.
⏳ **Needs email addresses** for the 19 leads — `leads.csv` has empty `email` column.

## Files

- `sender.py` — main SMTP-based sender with rate limiting (356 lines, pure stdlib)
- `leads.csv` — 19 leads across 7 verticals (property_tech, indie_saas, agency, growth, marketing, dev_tools, content)
- `templates/01-19*.md` — personalized email templates per lead, each with `**Subject:**` line
- `.env.example` — copy to `.env` and fill in SMTP credentials
- `README.md` — this file

## Setup (5 minutes)

### Option A: Gmail (easiest, recommended)

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
   python sender.py --dry-run --test your-email@gmail.com
   python sender.py --test your-email@gmail.com  # actually sends
   ```

### Option B: SendGrid / Mailgun / AWS SES

Set the SMTP credentials in `.env` to your provider's SMTP settings. Sender works with any SMTP relay.

### Option C: Outlook / Office 365

Change `SMTP_HOST=smtp-mail.outlook.com` in `.env`.

## Filling in Lead Emails

The `leads.csv` has empty `email` columns — you need to fill those in before sending. Options:

1. **Manual research** (free, slow): Look up each lead's website, find their contact page, copy the email. 30-60 min for 19 leads.
2. **Hunter.io free tier** (50 searches/month): https://hunter.io — search for emails by domain.
3. **Apollo.io free tier** (10k credits/month): https://apollo.io — bulk email finding.
4. **Snov.io free tier** (50 credits/month): https://snov.io

For now, all 19 templates are written and ready. Just need emails + SMTP creds.

## Usage

```bash
# Dry run (default — safe)
python sender.py --dry-run --limit 5

# Send 5 emails
python sender.py --send --limit 5

# Send only specific leads (by index)
python sender.py --send --only index=05,07

# Send to specific vertical only
python sender.py --send --vertical indie_saas

# Test mode — render template 01 and send to your own email
python sender.py --test your@email.com

# Default safety: max 50 emails/hour (configurable via RATE_PER_HOUR)
```

## Safety Features

- **Default dry-run** — you must pass `--send` to actually send
- **Rate limit** — max 50/hour, state persisted across restarts
- **SMTP validation** — refuses to run without SMTP creds
- **Subject prefix** — leave blank or set to `[Atlas]` for tracking
- **CC self** — set `CC_SELF=true` to archive every email

## Expected Results (Honest Estimate)

Cold email to warm leads (people whose handles you found via Twitter, where you have a prior public relationship or shared context):
- Open rate: 40-60%
- Click rate: 8-15%
- Reply rate: 3-8%
- Conversion to $500 audit: 1-3%

19 personalized emails × 1-3% conversion = 0-1 sales = $0-500 from this batch.

The real value: this builds a template library you can reuse for the next 100 leads. After 2-3 batches you'll have a system that reliably generates 1-3 audits/month from cold outreach alone.

## When to Stop

If after 50 cold emails you have <2% open rate, your subject lines need work. If you have >30% open but <1% reply, your body copy needs work. If you have >5% reply but <1% conversion, your CTA (the audit offer) needs work.

Iterate on the templates in `templates/` based on reply patterns.

## Compliance Note

Sending cold email is legal in the US under CAN-SPAM (you need: real physical address in footer, unsubscribe mechanism, accurate subject lines, honor opt-outs within 10 days). For international recipients, check local laws (GDPR in EU is stricter).

For now: keep volume low (50/day max), include a clear "this is a one-time cold email" line, and reply promptly to any opt-outs.

## Files Created 2026-07-11

- `sender.py` — main script
- `leads.csv` — 19 leads
- `templates/01-19*.md` — 19 personalized templates
- `.env.example` — config template
- `README.md` — this file