---
title: World Cup Bot - egress live layout
type: concept
date: 2026-06-01
updated: 2026-06-01
tags: [world-cup-bot, egress, systemd]
ai-first: true
related:
  - projects/world-cup-bot/CLOB-V2-live/Index.md
  - projects/world-cup-bot/World Cup Bot.md
  - projects/world-cup-bot/CLOB-V2-live/World Cup Bot - CLOB V2 patch spec.md
  - entities/tools/world-cup-bot.md
  - entities/infrastructure/cemini-egress-fi.md
maturity: validated
---

# World Cup Bot — egress live layout (CeminiSuite)

Two-host split per `docs/runbooks/world-cup-bot-cemini-prod-layout.md`.

## Host roles

| Host | IP / location | WC role | `DRY_RUN` | Ledger |
|------|---------------|---------|-----------|--------|
| **cemini-prod** | US (Ashburn) | Shadow monitor, cross-venue alerts | `true` | `/opt/cemini/logs/wc_shadow_ledger.jsonl` |
| **cemini-egress-fi** | `204.168.139.190` (Helsinki) | Watch + live plan POST | `false` for live timer | `/opt/cemini/logs/wc_ledger.jsonl` |

SSH from prod: `ssh root@204.168.139.190` (alias `cemini-poly-fi` in prod `~/.ssh/config`).

## Paths (both hosts after bootstrap)

| Item | Path |
|------|------|
| world-cup-bot clone | `/opt/world-cup-bot/repo` |
| venv | `/opt/world-cup-bot/venv` |
| Cemini wrapper | `/opt/cemini/scripts/wc_run.sh` |
| systemd units | `/opt/cemini/deploy/systemd/cemini-wc-*` → `/etc/systemd/system/` |
| Secrets | `/opt/cemini/.env`, `/opt/cemini/.env-polymarket`, `/opt/cemini/secrets.enc` |

## cemini-prod units (monitor profile)

| Unit | Status 2026-06-01 |
|------|-------------------|
| `cemini-wc-shadow-plan.timer` | enabled (4h dry plan) |
| `cemini-wc-shadow-watch.service` | running (REST reconcile → shadow ledger) |
| `cemini-wc-cross-venue.service` | running |
| `cemini-wc-pnl-daily.timer` | shadow ledger scope |
| `cemini-wc-live-plan.timer` | **disabled** (US — never enable) |

Gate check (always set ledger path):

```bash
WC_LEDGER_PATH=/opt/cemini/logs/wc_shadow_ledger.jsonl \
  /opt/cemini/scripts/wc_run.sh shadow-status --min-phase 1
```

## cemini-egress-fi units (trading profile)

Installed via `deploy/systemd/install-wc-egress.sh`:

| Unit | Purpose | Status 2026-06-01 |
|------|---------|-------------------|
| `cemini-wc-watch.service` | WS + REST fill reconcile → live ledger | **active** |
| `cemini-wc-preflight.timer` | 6h geoblock/creds log | enabled |
| `cemini-wc-calendar-guard.timer` | cancel-window pull (`DRY_RUN=false` drop-in) | enabled |
| `cemini-wc-pnl-daily.timer` | live ledger PnL | enabled |
| `cemini-wc-live-plan.timer` | preflight + live `plan --record` | **disabled** until V2 patch |

Drop-ins created by installer:

- `/etc/systemd/system/cemini-wc-calendar-guard.service.d/egress-live.conf` — `WC_DRY_RUN=false`, vault hydrate
- `/etc/systemd/system/cemini-wc-pnl-daily.service.d/egress-live.conf` — live ledger path

## Env conventions

| Var | Monitor | Egress |
|-----|---------|--------|
| `WC_LOAD_POLYMARKET_ENV` | optional (use for manual preflight) | **1** on watch/live units |
| `WC_DRY_RUN` | `true` | `false` on live-plan + calendar-guard |
| `WC_LEDGER_PATH` | shadow path | live path (or default `wc_ledger.jsonl`) |

`wc_run.sh` unsets HTTP(S)_PROXY — required on hosts with Polymarket SOCKS for Docker LP.

## Bootstrap / refresh egress

```bash
# From cemini-prod — rsync stack (exclude .git, tools, vendor, logs)
rsync -az --delete \
  --exclude '.git/' --exclude 'tools/' --exclude 'vendor/' --exclude 'logs/' \
  /opt/cemini/ root@204.168.139.190:/opt/cemini/
rsync -az /opt/world-cup-bot/ root@204.168.139.190:/opt/world-cup-bot/

# On egress — recreate venv if Python major differs
ssh root@204.168.139.190 'rm -rf /opt/world-cup-bot/venv && python3 -m venv /opt/world-cup-bot/venv && /opt/world-cup-bot/venv/bin/pip install -e "/opt/world-cup-bot/repo[live]"'
apt-get install -y python3-cryptography python3-yaml   # vault hydrate for wc_run

bash /opt/cemini/deploy/systemd/install-wc-egress.sh
```

## Kill switch

```bash
systemctl disable --now cemini-wc-live-plan.timer
# or override: WC_DRY_RUN=true
world-cup-bot cancel --all-wc --record   # with L2 on egress
```
