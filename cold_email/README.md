# Atlas Cold Email System

Pure-Python SMTP-based outreach for the **$500 AI Workflow Audit** and **$49 Atlas Playbook** offers. No SaaS signup, no third-party trackers, no Python deps beyond the stdlib.

## What's here

```
cold_email/
├── sender.py           — SMTP-based sender, rate-limited (50/hr default), dry-run safe
├── leads.csv           — 19 leads adapted from outreach/leads/ (Twitter handles + email column TBD)
├── templates/          — 19 personalized email templates (01_RentRedi.md … 19_convertica.md)
├── .env.example        — credential template (copy to .env, fill in)
├── .env                — local config (gitignored — DO NOT COMMIT)
└── README.md           — this file
```

## Quick start

### 1. Get SMTP credentials

**Easiest path: Gmail SMTP**

1. Enable 2FA on the Google account you'll send from (e.g. `atlas@talonforge.io`)
2. Go to https://myaccount.google.com/apppasswords
3. Create an App Password (Mail / Other → "Atlas Cold Outreach")
4. Google shows a 16-character password. Paste it into `.env` as `SMTP_PASSWORD`.

**Outlook / Office 365** also works — set `SMTP_HOST=smtp-mail.outlook.com`. Use your normal Outlook password (or an App Password if MFA is on).

**For 50–200 emails/day, dedicated transactional SMTP is safer long-term** (Mailgun, Postmark, Amazon SES). All three speak the same SMTP protocol — just swap `SMTP_HOST` / `SMTP_USERNAME` / `SMTP_PASSWORD`.

### 2. Fill in `.env`

Copy `.env.example` to `.env` (already done) and replace:

- `SMTP_USERNAME` — your sending email address
- `SMTP_PASSWORD` — the App Password from step 1
- `FROM_EMAIL` / `FROM_NAME` — what recipients see
- `DRY_RUN=true` — KEEP THIS until you've verified

### 3. Fill in `leads.csv` `email` column

The seed list only has Twitter handles. You need real email addresses for each recipient. Sources:

- Hunter.io / Apollo.io / Snov.io for B2B lookup
- Manual website scraping
- LinkedIn Sales Navigator (export with email)

Columns:

```
index,name,handle,email,vertical,tier,template,tier_reason
```

Only the `email` column needs editing. The 19 templates in `templates/` already match each row.

### 4. Dry-run first

```bash
cd cold_email
python sender.py --dry-run
```

Prints subject + body for every lead. Confirms templates render and you don't have typos.

### 5. Send

```bash
python sender.py --send --limit 5      # first 5 only, live
python sender.py --send                # all 19
python sender.py --send --only 05,07   # only specific indexes
python sender.py --send --vertical b2b_saas   # only one vertical
python sender.py --test your@email.com         # one test email to yourself
```

The sender:

- Connects via STARTTLS on port 587
- Rate-limits to **50 emails/hour** by default (configurable via `RATE_PER_HOUR`)
- Persists send state to `.send_state.json` so the cap survives restarts
- Sleeps between sends in live mode (~72s between at 50/hr, scales down for higher caps)
- Exits cleanly on auth failure (no half-sent batches)

## Cadence rules

From the original DM campaign, carried over:

- **One touch per prospect per channel** — these 19 are the first wave only
- Wait **48h before follow-up**
- Max **3 touches total**
- **No sending on weekends** (Sat/Sun recipients hate cold pitches)
- **Always personalize the first line** — these templates do that (named company + their vertical pain)

To scale past 19, you'll need more leads with real emails. Two paths:

1. **Build a per-vertical scraper** (Hunter.io domain search, Apollo bulk export, LinkedIn scraping)
2. **Buy a list** — $0.10–$0.50/lead from Apollo / Instantly / Lemlist
3. **Hand-research** — for the top 50 prospects, manual email discovery beats any scraper

## Files you need to edit before sending

| File | What to change |
|---|---|
| `cold_email/.env` | SMTP_HOST, SMTP_USERNAME, SMTP_PASSWORD, FROM_EMAIL |
| `cold_email/leads.csv` | Fill `email` column for every row |

Everything else is content you can iterate on.

## Files NOT to commit

- `.env` (real credentials)
- `.send_state.json` (cap-tracking — harmless, but local noise)

## Limitations

- **Gmail free tier caps at ~500 emails/day** before spam flags. For 50–200/day you're fine.
- **Outlook free tier caps at ~300/day**.
- For **500+/day**, switch to Mailgun ($0.80/1k) or Postmark ($1.25/100 emails) — same protocol, higher limits, better deliverability.
- No open/click tracking. If you need that, swap in a SaaS tool (Instantly, Lemlist). The protocol layer this script uses is identical — drop-in compatible.

## Tested

- ✅ Python imports cleanly (no external deps)
- ✅ Dry-run renders all 19 templates with correct subject + body + personalization
- ✅ CSV ingestion (19 leads parsed)
- ✅ `.env` loading (no python-dotenv needed)
- ✅ Rate-limit state persistence
- ⏸ Live send (waiting on SMTP credentials from user)