---
title: Internal benchmark & backtest — where tasks run
type: concept
tags: [meta, cadence, deployment, laptop, librarian, prod]
keywords: [backtest, benchmark, arcticdb, ssh, prod-boundary]
related:
  - concepts/cemini-deployment.md
  - concepts/librarian-server-architecture.md
  - meta/equity-signal-backtest-cadence.md
  - meta/pta-backtest-cadence.md
  - meta/hl-funding-backtest-cadence.md
  - meta/pm-lp-backtest-cadence.md
  - sources/pta-metric-anchoring-ssrn-4549819.md
maturity: core
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @concepts/cemini-deployment.md — prod vs laptop vs librarian boundary
- @concepts/librarian-server-architecture.md — ArcticDB + stash serving host
- @meta/equity-signal-backtest-cadence.md — equity momentum lab
- @meta/pta-backtest-cadence.md — PTA reproduction gate
- @sources/pta-metric-anchoring-ssrn-4549819.md — adopt candidate gated on pilot

## Rule of thumb

| Surface | Role |
|---------|------|
| **Laptop (OSINT workspace)** | Run scripts, generate HTML/MD reports under `.local/reports/`, stage briefs |
| **cemini-librarian** | Canonical **read-only** data for backtests (ArcticDB `equity_bars`, bulk research); stash MCP memory; **never** run ingest sweeps or prod trading |
| **cemini-prod (`/opt/cemini`)** | 24/7 trading stack — receives **briefs only** from this workspace; **no** backtest/benchmark jobs |
| **cemini-egress-fi** | Egress proxy for prod API calls — **not** a backtest compute host |

**Never** run Dune queries, PM/Kalshi sweeps, PTA pilots, MCP soak harnesses, or wiki lint commits on prod or egress.

## Task routing table

| Gate / ritual | Command | Compute | Data source | Prod? |
|---------------|---------|---------|-------------|-------|
| **PTA reproduction** | `bash scripts/run_pta_backtest.sh` | Laptop | Librarian ArcticDB via SSH | Brief only after pass |
| **Equity momentum lab** | `bash scripts/run_equity_signal_backtest.sh` | Laptop | Librarian ArcticDB via SSH | Brief only |
| **PM LP spread** | `bash scripts/run_pm_lp_backtest.sh` | Laptop | Public Gamma + CLOB | Brief only |
| **Kalshi LP spread** | `bash scripts/run_kalshi_lp_backtest.sh` | Laptop | Public Kalshi trade API | Brief only |
| **Cross-venue PM×Kalshi** | `bash scripts/run_cross_venue_backtest.sh` | Laptop | Public APIs | Brief only |
| **HL funding Dune** | `.local/tools/hl-funding-sniper-reference/scripts/run_dune_backtest.sh` | Laptop | Dune (`~/.config/dune/`) | Brief only |
| **MCP rate-limiter soak** | `pytest tests/test_performance.py` on forked `polymarket-mcp-server` | Laptop dev | Live Polymarket APIs (read) | Deploy brief → prod |
| **stash token-cost ratio** | Measure on **librarian** stash instance | Librarian | Local Ollama + Postgres | Adopt gate for librarian MCP |
| **firnflow RAM / 130-MCP soak** | Not scheduled — Reference-only architecture | — | — | No deploy |
| **Kronos CPU P99** | Optional laptop torch micro-bench | Laptop | HF model download | Steal tokenizer only |
| **K79 SMB sleeve backtests** | Future per-playbook scripts | Laptop | Vendor-defined / Polygon when built | Policy briefs only |
| **NEEDS VERIFICATION sweeps** | Wiki edits + Exa/GitHub/SSH probes | Laptop | External + read-only SSH | N/A |

## PTA gate (explicit)

1. **Pilot** — `bash scripts/run_pta_backtest.sh` (laptop + librarian SSH). Report → `.local/reports/pta-pilot-YYYY-MM-DD.md`.
2. **52-week vs micro-anchor** — same script; `--anchor-days 252` and `--micro-days 52`.
3. **Pass criterion (draft)** — mean high-minus-low PTA quintile spread among past winners **> 0** on ≥3 symbols with ≥252 daily bars (directional replication, not full paper econometrics).
4. **2026-05-29 pilot result** — **FAIL** on librarian ArcticDB slice (7 symbols, bars through ~2017-11): 252d spread **−0.16%**, 52d micro **−0.22%**. Keep adoption blocked; re-run when equity_bars corpus is fresher.
5. **Fail / inconclusive** — keep `[TENTATIVE]` on wiki; do not brief MAPPO feature injection.
6. **Prod path** — only after pilot pass + TimescaleDB implementation brief to server Claude (prod implements; laptop does not).

## Ingest-asked tasks (same routing)

Questions raised during ingests map here — do not re-ask "prod or laptop?":

- **Schadner BSIV reproduction** — laptop Python on librarian/Polygon-shaped data → brief
- **Polymarket MCP pip-licenses / soak** — laptop → fork-and-maintain brief → prod docker-compose
- **SMB playbook backtests** — laptop labs; prod only after promotion rubric + brief
- **Tier-2 arXiv sweep** — laptop agent + Exa; commit wiki on user GO
- **Quarterly cadence rituals** — laptop; bump `wiki/meta/*-cadence.md` + `wiki/log.md`
