# WC R16 Ticket Price Monitor

DIY price alert for **FIFA World Cup 2026 Round of 16** tickets. Each hourly scan runs **two sources in parallel**:

1. **[The Great Reviewer WC tracker](https://thegreatreviewer.com/wc-tracker/)** — FIFA **official** resale marketplace (public API)
2. **[TicketWave](https://ticketwave.io/wc/)** — secondary markets (Viagogo, Ticombo, LiveFootballTickets, FootballTicketNet)

Posts Discord alerts when any listing drops **under your threshold** (default **$1,500**).

No paid APIs. Stdlib HTTP + parallel TicketWave fetches; optional Playwright for direct StubHub listing scrape.

## Quick start

```bash
cd agents/wc-r16-ticket-monitor
bash scripts/sync_env.sh          # pulls DISCORD_WEBHOOK_URL from cemini-prod .env
bash scripts/run_once.sh --dry-run   # scan + print hits, no Discord
bash scripts/run_once.sh             # live scan + Discord on new sub-threshold hits
bash scripts/install_launchagent.sh  # hourly macOS LaunchAgent
```

## What it watches

| Source | Data | Buy here |
|--------|------|----------|
| **Great Reviewer** | FIFA official resale floor (incl. 15% buyer fee) | [fifa.com/tickets](https://www.fifa.com/tickets) |
| **TicketWave** | Viagogo, Ticombo, LiveFootballTickets, FootballTicketNet | Respective reseller |

| Match | Date | Venue | TicketWave |
|-------|------|-------|------------|
| 89 W74 vs W77 | Jul 4 | Philadelphia | wc-r16-1 |
| 90 W73 vs W75 | Jul 4 | Houston | wc-r16-2 |
| 91 W76 vs W78 | Jul 5 | MetLife (NJ) | wc-r16-3 |
| 92 W79 vs W80 | Jul 5 | Mexico City | wc-r16-4 |
| 93 W83 vs W84 | Jul 6 | Arlington | wc-r16-5 |
| 94 W81 vs W82 | Jul 6 | Seattle | wc-r16-6 |
| 95 W86 vs W88 | Jul 7 | Atlanta | wc-r16-7 |
| 96 W85 vs W87 | Jul 7 | Vancouver | wc-r16-8 |

## Config

- `config.yaml` — threshold, cooldown, source toggles (`great_reviewer`, `ticketwave`, `stubhub_direct`)
- `events.yaml` — match list + StubHub URLs
- `.env` — `DISCORD_WEBHOOK_URL` (gitignored; sync via `scripts/sync_env.sh`)

Env overrides: `PRICE_THRESHOLD_USD`, `ALERT_COOLDOWN_HOURS`, `POLL_INTERVAL_MINUTES`.

## Optional: direct StubHub (Playwright)

StubHub blocks plain HTTP (AWS WAF). Enable direct listing scrape:

```bash
pip install -r requirements.txt
playwright install chromium
# config.yaml → sources.stubhub_direct: true
```

## Output / state

- `.local/last_scan.json` — latest full scan snapshot
- `.local/alert_state.json` — dedupe state (24h cooldown; re-alert on $50+ drop)
- `.local/logs/` — LaunchAgent stdout/stderr

## Flags

```bash
python3 monitor.py --dry-run      # no Discord
python3 monitor.py --force-alert  # ignore dedupe
python3 monitor.py --json         # dump scan JSON
python3 monitor.py -v             # debug logging
```

## Caveats

- **Great Reviewer FIFA data is crowdsourced** — freshness depends on extension users scanning that match. `scanned_at` is shown in alerts when available. Stale scan ≠ no tickets; check [WC tracker](https://thegreatreviewer.com/wc-tracker/) directly.
- TicketWave refreshes ~hourly; LaunchAgent polls hourly.
- FIFA warns third-party resellers are unauthorized — prefer FIFA official when prices are close.
- Prices are **indicative**; always confirm checkout price on the seller site.

## Discord

Uses `DISCORD_WEBHOOK_URL` from Cemini prod `.env` (same channel as other Cemini alerts). Sync script reads `ssh cemini-prod:/opt/cemini/.env`, falls back to local `CeminiSuite/.env`.
