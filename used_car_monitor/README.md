# Used-Car Deal Monitor

Evidence-first used-car acquisition funnel, derived from the Instagram reel
`Da5uIuoxgV3` and corrected against Carvana's FY2025 financials, Meta's Terms,
NHTSA recall data, and NMVTIS consumer guidance.

## What it does

```
brief → discover → normalize → dedupe → value → risk → approve → contact → inspect → decide
```

The monitor runs the **read-only** stages autonomously. Outbound contact,
offers, appointments, deposits, and purchases are **always human-gated**.

## Quick start

```bash
# 1. Initialize the DB
py -3.12 -m used_car_monitor init

# 2. Add a buying brief
py -3.12 -m used_car_monitor add-brief \
  --name 'Tacoma TRD 2016-2020 Texas' \
  --geography 'Austin, TX, 150mi' \
  --target '{"make":"Toyota","model":"Tacoma","trim":"TRD","year_min":2016,"year_max":2020,"max_ask_price":30000}' \
  --max-all-in 32000 \
  --min-discount 0.15 \
  --min-confidence medium

# 3. Drop listing JSON files into the discovery feed
#    Default path: used_car_monitor/data/drops/manual_export/*.json
#    See data/drops/manual_export/tacoma-batch-001.json for the schema.

# 4. Run the pipeline
py -3.12 -m used_car_monitor run --brief 1

# 5. Review flagged listings
py -3.12 -m used_car_monitor status
py -3.12 -m used_car_monitor alerts

# 6. Approve or decline
py -3.12 -m used_car_monitor approve --listing-id 6 --max-offer 14500 --who zinou
py -3.12 -m used_car_monitor decline --listing-id 5 --who zinou
```

## Listing schema

Each listing file is a JSON array. Required keys:

```json
{
  "listing_id": "fm-2018-tacoma-trd-001",
  "url": "https://...",
  "year": 2018, "make": "Toyota", "model": "Tacoma", "trim": "TRD",
  "mileage": 58000,
  "ask_price": 22000,
  "location": "Austin, TX",
  "seller_name": "Vlad",
  "seller_type": "private",
  "title_claim": "clean",
  "vin": "5TFCZ5AN8KX171001",
  "description": "Single owner, no accidents.",
  "photos": []
}
```

## Adapters

| Layer | Adapter | Default | Notes |
|---|---|---|---|
| Discover | `FileFeedAdapter` | ON | Reads `data/drops/manual_export/` |
| Discover | `CommunityMCPAdapter` | OFF | Opt-in. Confirm Meta's automation policy. |
| Value | `CarsXEMarketValueAdapter` | ON if `CARSXE_API_KEY` set | Live API, $40.83/mo Starter. Industry standard. |
| Value | `CompsLocalAdapter` | ON | Median of `data/comps.json` weighted comps. |
| Value | `HeuristicValuation` | ON | Local depreciation curves. Floor estimate. |
| Value | `KBBPublicAdapter` | OFF | KBB serves behind Akamai; needs residential proxy. |
| Risk | `NHTSAVinDecodeAdapter` | ON | Hard-stop on VIN mismatch / failed decode. |
| Risk | `NHTSARecallAdapter` | ON | Warns on open recalls. |
| Risk | `ScarcitySignalsAdapter` | ON | Off-platform payment, impossible mileage, branded title. |
| Risk | `CarsXEHistoryAdapter` | ON if `CARSXE_API_KEY` set | Accidents, title brand, owner count, odometer rollback. |
| Risk | `CarGurusDealRatingAdapter` | ON | Reads `cargurus_rating` field from listing dict. |
| Notify | `LocalLogNotifier` | ON | Appends to `data/alerts.jsonl`. |
| Notify | `TelegramNotifier` | OFF | Needs `MONITOR_TG_BOT_TOKEN` + `MONITOR_TG_CHAT_ID`. |

## CarsXE (recommended paid add-on)

The best single-vendor vehicle-data API for personal use in 2026:

| Endpoint | Purpose | Cost |
|---|---|---|
| `GET /specs` | VIN decode | free tier |
| `GET /market-value` | Live private-party value | $0.04/call typical |
| `GET /history` | Accidents, title brand, owners, odometer | $0.05/call typical |
| `GET /recalls` | Recalls by VIN | $0.05/call typical |

Plans (verified July 2026):

| Plan | Price | Market-Value/mo | History/mo |
|---|---|---|---|
| Sandbox | $0 | 5 | 1 |
| Starter | $40.83/mo | pay-as-you-go | pay-as-you-go |
| Pro | $207.50/mo | pay-as-you-go | pay-as-you-go |

Set `CARSXE_API_KEY=...` in the environment and the monitor picks it up
automatically. Use `--no-carsxe` to force-disable.

## Approval policy

| Action | Autonomous? |
|---|---|
| Run approved search | YES |
| Normalize/dedupe | YES |
| Calculate valuation, discount, all-in cost, max offer | YES |
| Check VIN decode, recalls, history, scam signals | YES |
| Write to local alert log | YES |
| Send first message to a seller | **NO — requires approval** |
| Make an offer | **NO — requires approval** |
| Schedule a viewing or inspection | **NO — requires approval** |
| Pay, deposit, sign, buy | **NO — requires approval** |

## Tests

```bash
py -3.12 -m unittest used_car_monitor.tests.test_smoke -v
```

## Daily automation

A cron job in Hermes runs `used-car-monitor run` once a day. The job
loads the `used-car-deal-monitor` skill, re-runs the pipeline, and
delivers a summary to the user's Telegram. It does **not** send any
outbound messages to sellers.

## File layout

```
used_car_monitor/
├── __init__.py
├── __main__.py            # CLI entrypoint
├── db.py                  # SQLite schema + helpers
├── pipeline.py            # orchestrator (run_once, evaluate_listing, alert_payload)
├── adapters/
│   ├── discovery.py       # FileFeedAdapter, CommunityMCPAdapter
│   ├── valuation.py       # Heuristic, KBB, CompsLocal, blend()
│   ├── risk.py            # NHTSA VIN, NHTSA recall, scarcity heuristics
│   └── notifier.py        # LocalLog, Telegram
├── data/
│   ├── monitor.db         # SQLite
│   ├── alerts.jsonl       # alert log
│   ├── comps.json         # manual local comps
│   └── drops/manual_export/*.json  # discovery feed
└── tests/
    └── test_smoke.py
```

## What this is NOT

- It does **not** call Facebook Marketplace automatically. The reel's MCP
  flow is exposed via `CommunityMCPAdapter` but is opt-in and disabled by
  default because it conflicts with Meta's current Terms.
- It does **not** pretend to be CarGurus. If you want their deal rating,
  paste it onto a listing with `set-rating --listing-id N --rating "..."`.
- It does **not** pay for KBB, Carfax, or any paid valuation feed by
  default. If you bring a `CARSXE_API_KEY`, it does call CarsXE for
  market value + history + recalls.
- It does **not** message sellers on its own. Approvals are explicit
  commands you run after reviewing the alert.

## Source & evidence

- Original reel: https://www.instagram.com/reel/Da5uIuoxgV3/
- Carvana Q4/FY2025 shareholder letter (total GPU $7,026):
  https://investors.carvana.com/~/media/Files/C/Carvana-IR/documents/cvna-shareholder-letter-q4-2025.pdf
- Meta Terms of Service (no automated access without permission):
  https://www.facebook.com/legal/terms
- NHTSA recall API:
  https://api.nhtsa.gov/recalls/recallsByVehicle
- NHTSA VIN decoder:
  https://vpic.nhtsa.dot.gov/api/
- NMVTIS consumer guidance:
  https://vehiclehistory.bja.ojp.gov/nmvtis_consumers
- Community MCP examined: jdcodes1/facebook-marketplace-mcp,
  jlsookiki/secondhand-mcp