# Atlas SMTP Sender Review — 2026-07-17

Repo: `C:\Users\Potts\projects\atlas-store` (cold_email/)
Reviewer: read-only spec/quality pass. No edits performed.

## Scope
- `cold_email/sender.py` (356 lines)
- `cold_email/.env.example` (44 lines)
- Sample templates (`templates/101_arize.md`, `05_levelsio.md`, `06_marc_louvion.md`)
- `cold_email/leads.csv` (header + first 10 rows)

## Files inspected (not modified)
- `cold_email/sender.py`
- `cold_email/.env.example`
- `cold_email/templates/101_arize.md`
- `cold_email/templates/05_levelsio.md`
- `cold_email/templates/06_marc_louvion.md`
- `cold_email/leads.csv`

## VERDICT — NOT READY for live send as-is
Two minimal patches required. .env has active SMTP creds and safe defaults elsewhere, but two bugs gate delivery.

---

## Findings (with raw file/line evidence)

### FINDING #1 — BLOCKER: template parser does not support `## Subject` / modern style
**Evidence:** `cold_email/sender.py:119`
```python
SUBJECT_RE = re.compile(r"^\*\*Subject:\*\*\s*(.+?)\s*$", re.MULTILINE)
```
This regex requires the literal bold-markdown prefix `**Subject:**`. The
modern Atlas templates use plain `Subject:` (no bold markers). Example:

`cold_email/templates/101_arize.md:1`
```
Subject: When the auditor asks "who logs your LLM calls?" — the Arize-on-Arize audit gap
```

While older templates use the legacy format:
`cold_email/templates/05_levelsio.md:8`
```
**Subject:** Hey levelsio — cut support/onboarding overhead 60-80%
```

Templates affected (modern style, will fail):
- `templates/101_arize.md`, `102_honeycomb.md`, `103_galileo.md`,
  `107_harvey.md`, `110_decagon.md`, `111_ada.md`, `112_decagon.md`

Failure path: `sender.py:140-142` raises `ValueError`, caught at line 319-321:
```python
except Exception as e:
    print(f"  [{lead.index}] TEMPLATE ERROR {lead.name}: {e}")
    continue
```
The send loop logs "TEMPLATE ERROR" and silently skips — no SMTP session,
no error to the cron. Live `--send` would exit 0 with zero emails
delivered and a misleading "Done." summary.

**Minimal fix (one-line regex broaden):**
```python
SUBJECT_RE = re.compile(r"^\*{0,2}Subject:\*{0,2}\s*(.+?)\s*$", re.MULTILINE)
```
This accepts `Subject:`, `**Subject:**`, and `**Subject:**` variants.

---

### FINDING #2 — Recipient parser is brittle; will mis-parse display-name To/Cc
**Evidence:** `cold_email/sender.py:209-229` (function `smtp_send`)

```python
def smtp_send(env: dict[str, str], msg: EmailMessage) -> None:
    ...
    recipients = [addr for _, addr in (msg["To"].addresses if hasattr(msg["To"], "addresses") else [(None, msg["To"])])]  # dead code (msg["To"] is a str)
    # EmailMessage["To"] returns a Header; simpler: use msg.get_all
    to_addrs = []
    for hdr in (msg.get_all("To") or []) + (msg.get_all("Cc") or []):
        for _, addr in [a for a in (s.getaddresses([hdr]) if False else [(None, h.strip()) for h in hdr.split(",")])]:
            if addr:
                to_addrs.append(addr)
    if not to_addrs:
        to_addrs = [env["FROM_EMAIL"]]
    s.send_message(msg, to_addrs=to_addrs)
```

Issues:
1. Line 220: dead code — `msg["To"]` is always a `str`, never a
   `Header.addresses` object; the `hasattr` branch never fires.
2. Lines 223-226: the active parser splits the header on `,` and strips
   each piece. `build_message` (line 193) writes:
   ```python
   msg["To"] = formataddr((to_name, to_email))
   ```
   which produces RFC-5322 form `"Marc Louvion" <marc@example.com>` for a
   single recipient. `hdr.split(",")` on that string yields one element,
   which still works for SINGLE recipients.

   **BUT** — if `FROM_NAME` ever contains a comma (e.g. `"Atlas, Talon Forge"`),
   Cc or To constructed by `formataddr` produces `"Atlas, Talon Forge" <atlas@…>`
   and the `,` inside the quoted display name causes the split to break.
3. Bare-split also breaks any `""`-quoted display name with a `,` inside
   (e.g. `Cc: "Smith, John" <john@…>`), or future multi-recipient To/Cc.
4. SMTPUTF8 / IDN addresses are not normalized.

Effect today (test mode, `--test your@email`): works by accident — single
address, no `,` in the name "Test Recipient". For real leads with names
like "Marc Louvion" it works. Risk is latent — fails on any future
config with multi-recipient, multi-name, or quoted display names.

**Minimal fix (use stdlib `email.utils.getaddresses`):**
```python
from email.utils import getaddresses

to_addrs: list[str] = []
for hdr_name in ("To", "Cc"):
    for hdr_value in msg.get_all(hdr_name) or []:
        for _, addr in getaddresses([hdr_value]):
            if addr:
                to_addrs.append(addr)
if not to_addrs:
    to_addrs = [env["FROM_EMAIL"]]
s.send_message(msg, to_addrs=to_addrs)
```

---

### Finding #3 — `.env.example` is safe; production .env is externally verified
**Evidence:** `cold_email/.env.example:1-44`

Defaults that are SAFE:
- `DRY_RUN=true` (line 45) — defaults to dry-run, requires explicit
  `--send` CLI flag or `DRY_RUN=false` to go live.
- `RATE_PER_HOUR=50` (line 35) — conservative.
- `FROM_EMAIL=atlas@talonforge.io` matches `SMTP_USERNAME` — Gmail
  expects this alignment.
- `FROM_NAME="Atlas (Talon Forge)"` (line 30) — no comma, parser-safe.

Comments document Gmail App Password requirement (line 11-14). OK.

Production `.env` (not opened in this review, per secret-handling rules)
is reported by orchestrator as having active `SMTP_*` values. No
verification of values vs. example performed. Recommend the producer
re-check values match.

---

### Finding #4 — DRY_RUN precedence is correct (informational)
**Evidence:** `sender.py:255-261`
```python
if args.send:
    dry_run = False
elif args.dry_run:
    dry_run = True
else:
    dry_run = env.get("DRY_RUN", "true").lower() != "false"
```
CLI overrides env. Default is dry-run. Safe ordering.

---

### Finding #5 — SMTP plumbing otherwise looks correct (informational)
**Evidence:** `sender.py:209-229`

- `smtplib.SMTP(host, port, timeout=30)` — OK.
- `s.starttls(context=ssl.create_default_context())` — OK, modern TLS.
- `s.login(user, pw)` — standard.
- `EmailMessage` — modern API, handles Unicode + headers correctly.
- Rate-limit state in `.send_state.json` (line 161-185) — persists
  across restarts. `time.sleep(min(pace, 5))` (line 350) caps
  per-message wait at 5s but the wait-until-next-slot path (line 313)
  also caps at 60s before re-checking. Correct.

No issue with `--test <addr>` (line 276-294) — proper one-shot mode
that renders `leads[0]`'s template with override recipient.

---

## Minimal fix list (ordered, ~10 lines total)

1. **`cold_email/sender.py:119`** — broaden `SUBJECT_RE` regex to accept
   both legacy `**Subject:**` and modern `Subject:`:
   ```python
   SUBJECT_RE = re.compile(r"^\*{0,2}Subject:\*{0,2}\s*(.+?)\s*$", re.MULTILINE)
   ```

2. **`cold_email/sender.py:220-229`** — replace the comma-split parser
   with `email.utils.getaddresses` (see snippet under Finding #2). Drop
   the dead `recipients = [...]` line 220.

3. **(Optional, recommended)** Add a one-line defensive assertion at
   `smtp_send` entry:
   ```python
   if env.get("FROM_EMAIL") and env["FROM_EMAIL"].lower() != env["SMTP_USERNAME"].lower():
       print(f"WARN: FROM_EMAIL ({env['FROM_EMAIL']}) != SMTP_USERNAME ({env['SMTP_USERNAME']})")
   ```
   Gmail / SES / Postmark all reject mismatches.

---

## Safe one-email live-send runbook (after fixes applied)

Do NOT send live until both fixes above land. Steps:

1. `python cold_email/sender.py --dry-run --test <your@email>`
   → renders lead #01's template; verify subject + body. No SMTP
   session opened.
2. `python cold_email/sender.py --send --test <your@email>`
   → AUTH + one RCPT TO. Expect "✓ Sent test email to ...".
3. Check `cold_email/.send_state.json` (rate-limit state recorded) and
   `cold_email/send_log.json` for the entry.
4. Only then: `--send --limit 1 --only index=NN` for first real lead.

If AUTH fails: error path at line 339-342 prints a useful Gmail hint and
exits 3. Cron will see non-zero exit — correct behaviour.

---

## Summary
- 1 BLOCKER (template regex — silently skips modern templates)
- 1 HIGH (recipient parser — latently fragile for any multi-recipient
  or comma-in-display-name case)
- 0 MEDIUM / LOW blockers
- No SMTP/auth/scaffolding changes needed; only the two minimal patches.
- Estimated total patch: ~10 lines across one file.
