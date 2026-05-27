---
title: HL funding-sniper Dune backtest — quarterly cadence
type: brief
tags: [meta, cadence, hyperliquid, backtest]
related:
  - entities/tools/hl-funding-sniper.md
updated: 2026-05-27
---

## Schedule

| Field | Value |
|-------|-------|
| Cadence | **Quarterly** (~90 days) |
| Last run | **2026-05-27** |
| Next due | **2026-08-27** |
| Owner | Laptop only (Dune credits); agent runs on request or when due |
| Prod/egress | **Never** run upstream `main.py` |

## What to run

From OSINT workspace (Dune auth in `~/.config/dune/config.yaml`):

```bash
cd ".local/tools/hl-funding-sniper-reference"
bash scripts/run_dune_backtest.sh
```

Or ask the agent: **“run quarterly HL funding backtest”**.

## After each run

1. Bump `last_run` / `next_run` (+90 days) on this page.
2. One-line note in `wiki/log.md` if results change the steal-from posture.
3. Optional: refresh `briefs/2026-05-27_k72-hl-funding-phase0-cemini.md` summary on prod only if PnL regime materially shifts.

## Relations

- @entities/tools/hl-funding-sniper.md

## References

- @entities/tools/hl-funding-sniper.md
- @briefs/2026-05-27_k72-local-adoption.md (gitignored; laptop)
- Report: `.local/tools/hl-funding-sniper-reference/data/reports/backtest_report.html`
