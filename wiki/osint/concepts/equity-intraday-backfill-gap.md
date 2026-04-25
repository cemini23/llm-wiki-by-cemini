---
title: Equity intraday backfill gap — Polygon NOT_AUTHORIZED + yfinance EOD sweep
type: concept
tags: [concept, data-engineering, harvester-doctrine, failure-mode, self-heal]
keywords: [polygon, not_authorized, intraday, yfinance, backfill, equity-ticks, ingestor, market-hours-gate]
related:
  - entities/platforms/polygon.md
  - entities/infrastructure/yfinance.md
  - entities/ticker-watchlist.md
  - concepts/cryptographic-audit-trail.md
maturity: validated
created: 2026-04-24
updated: 2026-04-24
---

## Relations

- @entities/platforms/polygon.md — the upstream vendor returning `NOT_AUTHORIZED` on same-day equity intraday
- @entities/infrastructure/yfinance.md — the fallback source used by the EOD sweep
- @entities/ticker-watchlist.md — per-ticker completeness depends on this self-heal working
- @concepts/cryptographic-audit-trail.md — backfill inserts are chain-logged

## Raw Concept

On 2026-04-24 the Cemini equity harvester missed the full 13:30–20:00 UTC session. Two failure modes stacked:

1. **Polygon plan tier** — on the current plan, Polygon returns `NOT_AUTHORIZED` on same-day equity intraday requests. The ingestor had no branch for that specific error.
2. **Market-hours gate silence** — `polygon_ingestor.py`'s market-hours gate treated the NOT_AUTHORIZED response as "nothing to do" and skipped post-close without alarming. Combined with #1, the full session vanished.

Crypto feed via Coinbase was unaffected — that path runs on a different auth + permission scope and stayed healthy through 21:10 UTC. New tickers (INTC/GLW/PL/ASTS/SOFI) carried Apr 22 startup-backfill data through Apr 23 but nothing for Apr 24 until the fix landed.

## Narrative

### The doctrine — ingestor self-heals on NOT_AUTHORIZED

`polygon_ingestor.py` was patched 2026-04-24 so that after 16:01 ET daily the ingestor checks whether the equity session is missing and, if it is, backfills via `yfinance` as the fallback source. `yfinance` was added to the Dockerfile. Going forward:

- **Primary path**: Polygon live equity ticks during market hours.
- **Fallback (post-close)**: yfinance EOD sweep at 16:01 ET+ fills any gap the Polygon plan-tier refused. 390 1-min bars per symbol for a full session.

This trades live-tick granularity for EOD 1-min bars on the days Polygon refuses — acceptable for the current research/strategy workload, which doesn't require same-day intraday precision at the tick level for historical/backtest use.

### Why this is a **concept page**, not just an incident note

Because it names a **durable failure-mode doctrine** — any future equity feed that similarly refuses same-day intraday (Polygon plan change, vendor swap) will trip the same gap. The fix pattern (EOD fallback via a free-tier alternative with bar-granularity vs tick-granularity) generalizes beyond this specific vendor.

### 2026-04-24 incident — record of action

- **Detected**: data audit 2026-04-24 evening — equities showed zero bars for the session while crypto was healthy.
- **Point fix (commit 1)**: `scripts/backfill_yfinance.py` inserted **13,258 bars** (390 1-min × 34 symbols) for Apr 24's full 13:30–20:00 UTC session.
- **Doctrine fix (commit 2)**: `polygon_ingestor.py` gained the yfinance EOD sweep + `yfinance` in Dockerfile.
- **Verification**: all 5 new watchlist tickers now carry Apr 24 closing-session data — INTC $82.56, GLW $175.92, PL $35.43, ASTS $76.42, SOFI $18.45.
- **Volume note**: GLW had 882 ticks vs ~1,500+ for INTC/SOFI on Apr 23 startup-backfill — consistent with GLW being a thinner, less-liquid intraday name.

### Audit-trail integration

The backfill `INSERT`s hit the same `audit_hash_chain` trigger as any other equity write, so the 13,258-bar backfill event is verifiable end-to-end. See @concepts/cryptographic-audit-trail.md.

### What this **doesn't** do

- **Does not upgrade the Polygon plan.** The same `NOT_AUTHORIZED` returns will trip every trading day going forward until the plan tier changes; the yfinance EOD sweep just ensures the data lands by market-close + 1 minute.
- **Does not restore tick-level granularity for the refused days.** yfinance is 1-min bars, not ticks. Strategies needing sub-minute intraday resolution on equity days Polygon refuses will be blocked until the plan upgrade.
- **Does not cover crypto.** Coinbase is a separate healthy feed; yfinance is equity-only in this wiring.

### Forward watch

- **Weekly sanity check**: if the yfinance EOD sweep fails silently, the same gap re-opens. Add an alert (missing-session detector at 16:15 ET) as a hardening step.
- **Vendor decision**: decide whether tick-level same-day intraday is worth a Polygon plan upgrade or whether the EOD-bar fallback is the permanent posture. Capture as a cost-vs-precision ticket if revisited.
- **Self-heal pattern re-use**: extend the EOD-sweep pattern to any future equity feed that returns vendor-side refusal on same-day intraday.

## Snippets

*(populate if specific error payloads, plan-tier quota numbers, or vendor-response examples become useful for future debugging.)*
