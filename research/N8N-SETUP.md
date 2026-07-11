# n8n Setup for Atlas — Battle-Tested Automation Stack

This folder contains **10 production-ready n8n templates** from the [awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates) repo (23,808 stars, 280+ templates).

## Why n8n?

n8n is the most-used open-source workflow automation platform with **196K stars**. Used by thousands of real teams. Unlike browser automation that gets bot-detected, n8n runs as a backend service making direct API calls to Gmail, Twitter, Reddit, etc.

## Templates Downloaded (10)

| File | What it does | Channel |
|---|---|---|
| `leadpilot-cold-email.json` | AI writes personalized cold emails from Google Sheets lead list using OpenAI | Email |
| `social-email-automation.json` | Social media analysis + automated email generation | Email + Social |
| `gmail-auto-label.json` | Auto-label incoming Gmail messages with AI | Gmail |
| `gmail-auto-reply-draft.json` | Compose reply draft in Gmail with OpenAI Assistant | Gmail |
| `reddit-ai-digest.json` | Scrape Reddit + AI digest of trending topics | Reddit (research) |
| `twitter-virtual-influencer.json` | Twitter Virtual AI Influencer — auto-posts | X.com (API) |
| `openai-tweet-generator.json` | OpenAI-powered tweet generator | X.com (API) |
| `ai-blog-writer-ollama.json` | AI Blog Writer Pipeline (Ollama local) | Blog |
| `ai-web-scraping-jina.json` | AI Powered Web Scraping | Lead gen |
| `ai-caption-creator.json` | AI Social Media Caption Creator | Social |

## Setup (10 minutes)

### Step 1: Install n8n

```bash
# Windows (via npm)
npm install -g n8n

# Or use Docker
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

### Step 2: Start n8n

```bash
n8n start
# Opens http://localhost:5678
# First time: create a free account (no email verification)
```

### Step 3: Import Templates

In the n8n UI:
1. Go to Workflows → "Import from File"
2. Import each `.json` file from this folder
3. Configure credentials:
   - **Gmail**: OAuth via Google account
   - **OpenAI**: API key (or use MiniMax with custom endpoint)
   - **Reddit**: API app at reddit.com/prefs/apps
   - **Twitter/X**: API v2 key from developer.twitter.com

### Step 4: Activate Workflows

For each template, click "Active" toggle. They'll run on their schedules.

## What This Unlocks (vs blocked browser automation)

| Action | Browser | n8n |
|---|---|---|
| Send 100 cold emails/day | ❌ reCAPTCHA | ✅ Gmail SMTP via API |
| Post to Twitter | ❌ cookie revoked | ✅ Twitter API v2 (when approved) |
| Scrape Reddit | ❌ rate-limited | ✅ Reddit API (free) |
| Auto-follow-up emails | ❌ impossible | ✅ Gmail API + scheduled triggers |
| Reply to inbound leads | ❌ manual | ✅ AI auto-draft with OpenAI |

## Recommended Sequence

1. **Set up Gmail SMTP in n8n** (5 min) — one-time auth
2. **Import leadpilot-cold-email.json** — load 19 leads from `cold_email/leads.csv` into Google Sheets
3. **Set up scheduled trigger** — send 5-10 emails/day to start
4. **Import gmail-auto-reply-draft.json** — auto-draft replies to inbound leads
5. **Import reddit-ai-digest.json** — daily digest of r/LocalLLaMA + r/LangChain trending topics
6. **Import twitter-virtual-influencer.json** (if/when X API approved) — schedule tweets

## Templates Ready to Ship Today (No New API Keys)

The following work with just existing credentials we have:

- `ai-blog-writer-ollama.json` — uses Ollama (local LLM, no API key needed)
- `ai-caption-creator.json` — uses Airtable (free tier)

## Files Ready 2026-07-11

All 10 templates downloaded to `research/n8n-templates/`. Total ~120KB. Ready to import into n8n.

---

**Sources:**
- [n8n-io/n8n](https://github.com/n8n-io/n8n) — 196,020 stars
- [enescingoz/awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates) — 23,808 stars, 280+ templates
- [browser-use/browser-use](https://github.com/browser-use/browser-use) — 104,184 stars (we have this)