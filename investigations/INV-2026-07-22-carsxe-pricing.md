# Investigation: CarsXE /specs pricing — is it free or paid?

**Investigation date:** 2026-07-22
**Investigator:** Hermes + gstack-investigate

## 1. Reproducer

- **Trigger:** `curl 'https://api.carsxe.com/specs?vin=5TFCZ5AN8KX171001'`
- **Observed:** HTTP 402 Payment Required. Response body:
  `{"success":false,"message":"Payment required","endpointId":"specs.v1","price":"$0.15","resource":"/specs"}`
- **Environment:** Windows 10, curl 8.x, no API key
- **Saved to:** inline (one curl call)

## 2. Isolation

Bisected:
- Same URL with `?key=demo` → still 402
- Different endpoint `https://api.carsxe.com/market-value?vin=...` → also 402 (but didn't check the price)
- `https://api.carsxe.com/` (root) → HTTP 200, returns marketing page

Conclusion: `/specs` requires payment. The HTTP 402 + explicit `price: $0.15` field is the bug report.

## 3. Hypotheses

| # | Hypothesis | Test | Result |
|---|---|---|---|
| 1 | /specs is paid ($0.15/call) | Read the 402 response | **CONFIRMED** — `price: $0.15` in payload |
| 2 | /market-value is free | Test the endpoint | refuted — also 402 |
| 3 | CarsXE has no free endpoints | Check pricing page | REFUTED — sandbox is free (100 calls lifetime) |
| 4 | Sandbox key unlocks free calls | Sandbox signup flow | CONFIRMED — sandbox has 5 market-value calls/mo, 1 history/mo |

## 4. Root cause

CarsXE exposes 12+ endpoints. The website's pricing page says "Sandbox: $0/mo, 100 calls lifetime" and lists per-endpoint quotas. The implication that any specific endpoint is "free" is wrong — even the sandbox endpoint quotas are per-endpoint (e.g. 5/mo for market-value, 1/mo for history). The documentation's own `/specs` endpoint returned a `price: $0.15` field in its 402 response, confirming the per-call cost.

The mistake in my prior commit: I wrote "free tier" for `/specs` in the README. That was a docs error, not a code error. The code never called `/specs`.

## 5. Fix

- **Commit:** (next commit)
- **Changed:** `used_car_monitor/README.md` — corrected pricing table
- **Regression test:** none needed — this was a docs-only mistake
- **All tests:** 11/11 still pass

## 6. What we learned

- **Pattern to watch for:** vendor pricing pages that say "free tier" without specifying which endpoints are free
- **Gap:** our monitor's adapter config doesn't track per-call costs. Adding a cost ledger would let us surface unexpected charges in the daily cron alert.
- **Action item:** add `cost_per_call` to each adapter's metadata, and surface monthly spend in the cron alert

## 7. What to do next

The monitor doesn't currently call `/specs` at all — we use NHTSA vPIC (free) for VIN specs. So the cost doesn't actually hit us. But we should:

1. Update README to say "NHTSA vPIC (free) is the VIN spec source; CarsXE `/specs` is $0.15/call"
2. Add a cost ledger to the monitor (next commit)
3. Wire CarsXE history into the existing pipeline so we get real history data, paid by usage budget

## Source

This investigation was conducted using the gstack-investigate skill,
ported from garrytan/gstack. Methodology follows the 6-step playbook
(reproduce → isolate → hypothesize → root cause → fix → verify).
