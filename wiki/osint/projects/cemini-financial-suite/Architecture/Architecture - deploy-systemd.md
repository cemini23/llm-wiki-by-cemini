---
title: Architecture - deploy-systemd (prod)
type: architecture-module
module: deploy-systemd
path: deploy/systemd/
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, gap-close]
keywords: [Cemini-Financial-Suite, /opt/cemini, de5ad93]
deploy-root: /opt/cemini
scanned-commit: de5ad93
provenance: prod-briefs-out-architecture-2026-06-01-gap-close
ai-first: true
related:
  - projects/cemini-financial-suite/Cemini Financial Suite.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Architecture/Architecture - Index.md
maturity: validated
---

## Relations

- @projects/cemini-financial-suite/Cemini Financial Suite.md — project hub
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @projects/cemini-financial-suite/Architecture/Architecture - Index.md — MOC

## For future Claude

Prod module `deploy-systemd` @ de5ad93; gap-close handoff.

# deploy/systemd — Host timers (prod ops)

**29 timers** / **33 services** on prod (`deploy/systemd/`). These run **on the host** (not inside the main compose loop) for Polymarket, weather calibration, world-cup (WC) sleeves, and hygiene.

## Categories

<!-- @generated:start -->
| Prefix | Examples | Purpose |
|--------|----------|---------|
| `cemini-pm-*` | `cemini-pm-weather-emos-promote`, `cemini-pm-btc-updown-paper`, `cemini-pm-kl-align`, `cemini-pm-mcp-shadow-probe` | Polymarket discovery, paper, LP, alignment |
| `cemini-wc-*` | `cemini-wc-discover`, `cemini-wc-scan`, `cemini-wc-cross-venue-reconcile`, `cemini-wc-pnl-daily` | WC / cross-venue sleeves |
| `cemini-weather-*` | `cemini-weather-nwp-stack`, `cemini-weather-nwp-train` | NWP stack harvest + train |
| `cemini-ops-*` | `cemini-ops-daily`, `cemini-health-snapshot`, `cemini-kalshi-daily-report` | Ops reports |
| `cemini-*-cleanup` | `cemini-disk-cleanup`, `cemini-chaos-cleanup` | Hygiene |
| `cemini-ots-upgrade` | — | OTS upgrade window |
<!-- @generated:end -->

## vs Docker

| Host systemd | Docker compose |
|--------------|----------------|
| Scheduled scripts, brief JSON refresh, PM/WC loops | Long-running containers (brain, ems, MCP) |
| Often invokes `scripts/*.sh` or `python3 scripts/*` | `docker compose` from `/opt/cemini` |

## Safety

Timers must not be enabled/disabled for trading gates without operator brief GO (same rule as `conviction.yaml`).

## Related

- @projects/cemini-financial-suite/Architecture/Architecture - Polymarket.md
- @projects/cemini-financial-suite/Architecture/Architecture - Docker services.md
- `docs/runbooks/` — operator procedures

## @user notes
