---
title: Cemini Deployment — Two-Server Setup Guide (Hetzner + Ubuntu)
type: concept
tags: [deployment, infrastructure, cemini-internal, operations, hetzner]
keywords: [Hetzner Cloud, CPX21, CPX31, Docker Compose, kb-server, US deployment, EU deployment, Polymarket, Kalshi, regional]
related:
  - entities/infrastructure/cemini-stack.md
  - entities/infrastructure/hetzner.md
  - entities/infrastructure/deepseek-api.md
  - concepts/librarian-server-architecture.md
  - concepts/cemini-license-posture.md
  - concepts/cross-channel-agent-gateway.md
maturity: draft
hub: true
created: 2026-05-03
updated: 2026-05-11
---

## Relations

- @entities/infrastructure/cemini-stack.md — physical topology this guide deploys onto
- @entities/infrastructure/hetzner.md — host provider; SKU + region selection rationale
- @entities/infrastructure/deepseek-api.md — LLM brain (cloud API; no local weights)
- @concepts/librarian-server-architecture.md — librarian-side rationale for the kb-server pattern
- @concepts/cemini-license-posture.md — license obligations attached to the stack being deployed

## Raw Concept

End-to-end install procedure for the Cemini two-server topology, written for a deployer with **minimal dev knowledge**: every required step is explicit, every required secret is named, every required Claude Code plugin / MCP is enumerated. Originated 2026-05-03 from the user's request for a setup document covering server class, RAM/disk requirements, OS choice, US/EU regulatory split, comprehensive API-key inventory, and Claude Code tooling needed to manage the install.

This is **operational documentation** — not Cemini's official runbook (which lives at `/opt/cemini/CLAUDE.md` on the production server and is out-of-scope for this workspace per project doctrine). This guide is the curator's-eye view: enough to get a fresh deployer to a working pair of servers, with explicit links to the server-side docs for everything below the orchestration layer.

## Narrative

### 1. Decide on region (US vs EU)

This is the **first decision** because it affects which trading venues are accessible from the deployment, and it cannot be cleanly changed after the fact (server-IP geo-blocking is enforced).

| Region | Polymarket | Kalshi | Recommended for |
| --- | --- | --- | --- |
| US (e.g. Hetzner Ashburn) | **Geo-blocked** for trading [Source: CFTC Polymarket settlement Jan 2022, retrieved via Exa 2026-05-03 — NEEDS VERIFICATION]. Read-only/data access generally permitted. | ✅ Full access; CFTC-licensed DCM for US persons. | US-resident operators primarily trading Kalshi + equities + crypto; comfortable losing Polymarket *trading* (data-only fine). |
| EU (e.g. Hetzner Falkenstein / Helsinki / Nuremberg) | ✅ Available for EU residents subject to local rules (UK / France / etc. have their own restrictions; verify per-country). | **Inaccessible** — Kalshi onboarding requires US-resident KYC. | EU-resident operators primarily trading Polymarket + equities + crypto; comfortable losing Kalshi entirely. |

**Operator residency vs server region** — what matters legally is the *operator's* residency for KYC/AML and tax purposes, not the server's location. The server region matters for *latency* and for IP-based geo-blocking when the venue checks server IP. Cemini does not endorse VPN-based circumvention of either platform's terms.

**Mixed deployments** — running production in one region and librarian in another is technically possible but adds inter-region private-network cost and latency. Recommend co-locating both in the same region.

**Current Cemini deployment**: both hosts in **Ashburn (US)** per `.local/server.md` [NEEDS VERIFICATION 2026-05-03 for production region]. This biases toward Kalshi-first usage; Polymarket access is limited to data harvesting via the prediction-market-agent containers.

### 2. Provision two Hetzner Cloud VPS

Recommended SKUs (matched to Cemini's measured workload):

| Role | Hetzner SKU | vCPU | RAM | Disk | Approx monthly cost (2026-05-03) |
| --- | --- | --- | --- | --- | --- |
| Librarian | **CPX21** | 3 | 4 GB | 80 GB NVMe | [NEEDS VERIFICATION 2026-05-03 — check current pricing at hetzner.com/cloud] |
| Production | **CPX31** | 2 | 8 GB | 80 GB NVMe + add 25 GB volume | [NEEDS VERIFICATION 2026-05-03] |

**Why these SKUs**:
- CPX21 (librarian): 3 vCPU is *enough* for embedding generation + kb-server + stash without contention; 4 GB RAM matches the Node + Postgres + Ollama working set without swap.
- CPX31 (production): 8 GB RAM is the *minimum* for 41 containers; the deployed system is at ~50% swap utilization during normal probe (see @entities/infrastructure/cemini-stack.md "Known operational findings"). Bigger SKUs are recommended if your deployment will grow the container count.
- Volume on production: detached 25 GB block storage for Postgres data dir or container backups, separating it from OS-disk pressure.

**Provisioning steps** (Hetzner Cloud Console, no CLI required):
1. Create project → Add server → choose Ubuntu 24.04 → CPX21 → enable backups → name `cemini-librarian` → add SSH key → Create.
2. Repeat for `cemini-prod` with CPX31 → add 25 GB volume → mount at provisioning time as `/var/lib/cemini-data` (or similar).
3. Network → Create network → name `cemini-private` → CIDR `10.0.0.0/16` → attach both servers.
4. Note the public IPs and private IPs; record them in `.local/server.md` (gitignored).

### 3. OS choice

**Recommended: Ubuntu 24.04 LTS** for both hosts. Cemini's current production runs 22.04.5 (deployed earlier); 24.04 is the librarian baseline and the recommended target for fresh installs and future production rebuilds. Both are LTS releases supported through 2027/2029 respectively.

Avoid: non-LTS Ubuntu, Debian (untested), AlmaLinux/Rocky (untested).

### 4. Pre-flight: domain + Cloudflare (production only)

Production is exposed via a **Cloudflare Tunnel** (no inbound public ports on the VPS itself; all traffic enters through Cloudflare's edge). This requires:
- A domain registered with any registrar (cloudflare.com is fine).
- Cloudflare account with the domain added (Free tier sufficient).
- A Cloudflare Tunnel created via dash.cloudflare.com/zero-trust → Tunnels → Create. Copy the resulting tunnel token (long opaque string).

Librarian does NOT need a tunnel — it's queried from production over the private network only.

### 5. Install — librarian (cemini-librarian)

```bash
# SSH in as root (Hetzner default). For each command block, run on the librarian.
ssh root@<librarian-public-ip>

# System hygiene
apt update && apt upgrade -y
apt install -y rsync git curl ca-certificates build-essential

# Node 20+ for kb-server
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt install -y nodejs

# kb-server
mkdir -p /opt/kb-server && cd /opt/kb-server
git clone <kb-server-repo-url> .   # [NEEDS VERIFICATION — replace with actual repo URL]
npm install
# Apply the KB_TOOL_ALLOWLIST patch documented in .local/server.md (kb-server "MCP allowlist" section).

# Wiki target directory
mkdir -p /opt/cemini-wiki/wiki
mkdir -p /opt/cemini-bulk/research /opt/cemini-bulk/market-dataset
chown -R root:root /opt/cemini-wiki /opt/cemini-bulk

# Ollama for embeddings
curl -fsSL https://ollama.com/install.sh | sh
ollama pull nomic-embed-text

# stash (episodic memory) — see sources/alash3al-stash.md
# Install per the upstream alash3al/stash README; deploy MCP on :8080 (SSE) and :9090 (HTTP).

# kb-server systemd service (sketch — adapt to actual entrypoint)
# Set KB_TOOL_ALLOWLIST=kb_search,kb_search_smart,kb_context,kb_read,kb_list,kb_vault_status,kb_safety_check
# in the unit file's Environment= directives.
```

### 6. Install — production (cemini-prod)

```bash
ssh root@<production-public-ip>

# System hygiene
apt update && apt upgrade -y
apt install -y git curl ca-certificates

# Docker (official installer)
curl -fsSL https://get.docker.com | sh

# Cloudflare tunnel daemon
curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb -o /tmp/cloudflared.deb
apt install -y /tmp/cloudflared.deb
cloudflared service install <CLOUDFLARE_TUNNEL_TOKEN>   # token from step 4

# Cemini repo
mkdir -p /opt && cd /opt
git clone <cemini-repo-url> cemini      # [NEEDS VERIFICATION — repo location]
cd /opt/cemini
cp dotenv.example .env
# Edit .env to populate every key in the "API & secret keys checklist" below.
nano .env

# Bring up the stack
docker compose up -d
docker compose ps    # verify all 41 containers are healthy
```

### 7. Initial wiki sync (laptop → librarian)

From the curator's laptop (this workspace):

```bash
# Add SSH config aliases
cat >> ~/.ssh/config <<'EOF'
Host cemini-prod
  HostName <production-public-ip>
  User root
  IdentityFile ~/.ssh/id_ed25519

Host cemini-librarian
  HostName <librarian-public-ip>
  User root
  IdentityFile ~/.ssh/id_ed25519
EOF

# First wiki sync
cd "/Users/<you>/Desktop/OSINT WORKSPACE"
./scripts/sync_wiki_to_librarian.sh

# Set up hourly cron (macOS)
crontab -e
# Add: 0 * * * * /Users/<you>/Desktop/OSINT\ WORKSPACE/scripts/sync_wiki_to_librarian.sh >> ~/Library/Logs/cemini-wiki-sync.log 2>&1
```

### 8. API & secret keys checklist

Cemini's `/opt/cemini/.env` declares **66 environment variables** as of 2026-05-03 probe. Categorized below — every name listed must be populated in `.env` before `docker compose up` succeeds reliably. Values are obtained from each vendor's developer portal.

**Trading venues (broker / exchange APIs)**:
- `ALPACA_API_KEY`, `ALPACA_API_SECRET`, `ALPACA_SECRET_KEY` — equity broker (US). Get at alpaca.markets/dashboard.
- `COINBASE_API_KEY`, `COINBASE_API_SECRET` — crypto. Get at cloud.coinbase.com.
- `KALSHI_API_KEY`, `KALSHI_EMAIL`, `KALSHI_PASSWORD`, `KALSHI_SENDER_ID`, `KALSHI_TARGET_ID` — US prediction markets (US deployment only). Get at kalshi.com after KYC.
- `OANDA_API_KEY`, `OANDA_ACCOUNT_ID`, `OANDA_PRACTICE` — forex. Get at oanda.com.
- `POLYGON_API_KEY` — equity market data. polygon.io. Note: paid tier required for same-day intraday; falls back to yfinance per Polygon doctrine memory.
- `RH_USERNAME`, `RH_PASSWORD` — Robinhood (use a dedicated account; 2FA-incompatible automation).
- *(Polymarket uses wallet-based authentication; no API key in `.env`. Wallet config lives elsewhere in the prod tree.)*

**LLM / brain**:
- `DEEPSEEK_API_KEY`, `DEEPSEEK_BASE_URL`, `DEEPSEEK_MODEL` — Cemini's brain. Get at platform.deepseek.com.
- `LIBRARIAN_API_KEY`, `LIBRARIAN_BASE_URL`, `LIBRARIAN_TIMEOUT_S` — internal handle to librarian's MCP endpoint. Generate and set; LIBRARIAN_BASE_URL points to the librarian's private IP.

**Data sources / news / macro**:
- `FINNHUB_API_KEY` — earnings calendar. finnhub.io.
- `FRED_API_KEY` — Federal Reserve economic data. research.stlouisfed.org/docs/api.
- `GNEWS_KEY` — news. gnews.io.
- `NEWSAPI_KEY` — news. newsapi.org.
- `OPENWEATHER_API_KEY` — weather. openweathermap.org.
- `BQ_PROJECT_ID`, `BQ_DATASET_ID`, `BQ_TABLE_ID`, `GOOGLE_APPLICATION_CREDENTIALS` — BigQuery. Cloud Console → IAM → service account JSON.
- `GITHUB_PERSONAL_ACCESS_TOKEN` — GitHub API access. github.com/settings/tokens (fine-grained, read-only repo).
- `X_API_KEY`, `X_API_SECRET`, `X_BEARER_TOKEN`, `X_API_MONTHLY_BUDGET`, `X_API_HARD_SKIP_PCT` — Twitter/X API. developer.x.com.

**Infrastructure / databases**:
- `POSTGRES_PASSWORD` — set to a strong random value at install time.
- `DB_HOST` — typically `postgres` (the docker-compose service name).
- `REDIS_HOST`, `REDIS_PASSWORD` — set at install.
- `PGADMIN_DEFAULT_PASSWORD` — pgAdmin web UI login.
- `GRAFANA_PASS` — Grafana admin login.
- `CLOUDFLARE_TUNNEL_TOKEN` — from step 4 above.

**Notifications**:
- `DISCORD_WEBHOOK_URL` — generic alerts. Discord channel → Edit → Integrations → Webhooks.
- `DISCORD_ALERTMANAGER_WEBHOOK` — Alertmanager-specific channel webhook.

**Feature flags / governance** (boolean / numeric, set per deployment policy — these are *not secrets* but are required to be set, often to `0`/`1`/`false`/`true`):
- `DEBATE_ENABLED`, `EXECUTION_CARD_ENABLED`, `INTEL_LOG_TO_POSTGRES`, `KL_SHADOW_LOGGER_ENABLED`, `KL_SHADOW_MODE`, `LLM_ANALYST_LIVE`, `LLM_ANALYST_SYMBOLS`, `MONTE_CARLO_POR_ENABLED`, `PAPER_MODE`, `PAPER_TRADING`, `PLAYBOOK_EMS_ROUTING_ENABLED`, `PM_INTEL_ENABLED`, `PM_SHADOW_LOGGER_ENABLED`, `PM_SHADOW_MODE`, `PRM_LLM_MAX_DAILY_COST`, `PRM_LLM_RESEARCH_ENABLED`, `RL_ENSEMBLE_ENABLED`, `SOCIAL_ALPHA_LIVE`, `SOCIAL_HARVESTER_ENABLED`, `SOCIAL_SCRAPER_INTERVAL_MINUTES`, `GOVERNOR_UNKILL_TOKEN`.

Defaults: start every flag in **shadow / paper mode** (`PAPER_TRADING=true`, all `*_SHADOW_MODE=true`, all `*_LIVE=false`) and only flip to live after end-to-end validation.

**Recommended `.env` source-of-truth pattern**: keep `dotenv.example` checked into the repo with empty values; keep populated `.env` gitignored on the production server only; back up the populated `.env` to a password manager (1Password / Bitwarden) — losing it requires re-issuing every API key.

### 9. Laptop-side: Claude Code plugins & MCPs

Claude Code is the recommended interface for managing this deployment. Install Claude Code (claude.ai/code), then enable the following plugins via `claude plugin install <name>` or by editing `~/.claude/settings.json`:

**Required plugins** (the 13 currently enabled in this workspace, observed 2026-05-03):

| Plugin | Marketplace | Purpose |
| --- | --- | --- |
| `exa@claude-plugins-official` | official | External research (Exa search). API key required: `EXA_API_KEY` in user settings. |
| `context7@claude-plugins-official` | official | Up-to-date library/SDK docs (React, Postgres, Docker, etc.). |
| `superpowers@claude-plugins-official` | official | Process skills (TDD, debugging, planning, code review). |
| `claude-md-management@claude-plugins-official` | official | CLAUDE.md authoring + auditing. |
| `commit-commands@claude-plugins-official` | official | One-shot `/commit`, `/commit-push-pr` flows. |
| `github@claude-plugins-official` | official | gh-CLI integration; PR + issue workflows. |
| `code-review@claude-plugins-official` | official | Structured PR review. |
| `code-simplifier@claude-plugins-official` | official | Refactor recently-modified code for clarity. |
| `skill-creator@claude-plugins-official` | official | Author new skills locally. |
| `hookify@claude-plugins-official` | official | Author hook rules for safe-by-default behavior. |
| `ralph-loop@claude-plugins-official` | official | Long-running autonomous loops. |
| `token-optimizer@alexgreensh-token-optimizer` | community (alexgreensh/token-optimizer) | Context health + status line. Adds `extraKnownMarketplaces` entry. |
| `codex@openai-codex` | openai-codex marketplace | Second-opinion / hand-off to Codex CLI for stuck tasks. |

**Required MCP servers** (laptop user-scope, in `~/.claude.json` `mcpServers`):

| MCP | Purpose | Required keys / config |
| --- | --- | --- |
| `playwright` | Browser automation (npx `@playwright/mcp@latest`) | none |
| `brave-search` | Web search alternative to Exa (npx `@brave/brave-search-mcp-server`) | `BRAVE_API_KEY` env |
| `cemini-mcp` (remote) | Cemini's own MCP exposed by the production stack | SSH access to `cemini-prod`; tunnel config |
| `kb-server` (remote) | Librarian's RAG MCP | SSH access to `cemini-librarian`; tunnel config; `KB_TOOL_ALLOWLIST` already set server-side |
| `stash` (remote) | Episodic-memory MCP | SSH access to `cemini-librarian`; SSE :8080 / HTTP :9090 |
| `polymarket-trading-mcp`, `polymarket-predictions-mcp` (remote) | Polymarket-side MCP exposed by prod containers | already deployed in prod stack |

The remote MCPs are reached via **SSH local-port-forwarding** — the librarian's stash + kb-server are bound to `localhost` (or to all-interfaces but firewalled at Hetzner Cloud), so direct internet exposure is not relied on. Each MCP gets its own SSH tunnel mapping a laptop port to a librarian local port.

**Worked example — stash MCP** (wired 2026-05-04):

```bash
# 1. Open SSH tunnel (laptop:8088 → cemini-librarian:localhost:8080)
ssh -f -N -L 8088:localhost:8080 -o ServerAliveInterval=60 -o ExitOnForwardFailure=yes cemini-librarian

# 2. Verify SSE endpoint responds locally
curl -sv -H "Accept: text/event-stream" --max-time 3 http://localhost:8088/sse | head -10
# Expect: HTTP/1.1 200 OK + Content-Type: text/event-stream

# 3. Add to ~/.claude.json mcpServers (use Python to edit safely — file is large)
python3 -c "
import json, pathlib
p = pathlib.Path.home() / '.claude.json'
d = json.loads(p.read_text())
d.setdefault('mcpServers', {})['stash'] = {'type': 'sse', 'url': 'http://localhost:8088/sse'}
p.write_text(json.dumps(d, indent=2))
"

# 4. Restart Claude Code to pick up the new MCP entry.
```

**Persistence** — `ssh -f -N` exits if the laptop sleeps or the connection drops. Two options for durable tunnels:

- **launchd plist** (chosen 2026-05-04 — macOS-native, no extra deps). Drop the plist below at `~/Library/LaunchAgents/com.cemini.stash-tunnel.plist`, then `launchctl load -w ~/Library/LaunchAgents/com.cemini.stash-tunnel.plist`. `RunAtLoad: true` brings the tunnel up at login; `KeepAlive: true` + `ThrottleInterval: 10` respawn within 10s of any drop. Verified by killing the ssh PID and watching launchd respawn it.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key><string>com.cemini.stash-tunnel</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/ssh</string>
        <string>-N</string>
        <string>-L</string><string>8088:localhost:8080</string>
        <string>-o</string><string>ServerAliveInterval=30</string>
        <string>-o</string><string>ServerAliveCountMax=3</string>
        <string>-o</string><string>ExitOnForwardFailure=yes</string>
        <string>-o</string><string>StrictHostKeyChecking=accept-new</string>
        <string>cemini-librarian</string>
    </array>
    <key>RunAtLoad</key><true/>
    <key>KeepAlive</key><true/>
    <key>ThrottleInterval</key><integer>10</integer>
    <key>StandardOutPath</key><string>/Users/claudiobarone/Library/Logs/cemini-stash-tunnel.log</string>
    <key>StandardErrorPath</key><string>/Users/claudiobarone/Library/Logs/cemini-stash-tunnel.log</string>
</dict>
</plist>
```

  Status check: `launchctl list | grep stash`. Logs: `tail ~/Library/Logs/cemini-stash-tunnel.log`. Stop: `launchctl unload ~/Library/LaunchAgents/com.cemini.stash-tunnel.plist`. Note `-N` not `-f -N` — launchd manages the process lifecycle, so ssh stays in the foreground from launchd's perspective.

- **autossh** (`brew install autossh`): `autossh -M 0 -f -N -L 8088:localhost:8080 -o ServerAliveInterval=30 -o ServerAliveCountMax=3 cemini-librarian`. Auto-restarts on drop. Alternative if Homebrew is already installed; otherwise launchd is cheaper.

**Apply the same pattern to other librarian MCPs**: kb-server (`-L 8083:localhost:3838`), and to Cemini-prod MCPs once Cloudflare-tunnel-side wiring is decided. `cemini-mcp` and the polymarket MCPs reach over the prod-side Cloudflare tunnel rather than SSH local-port-forward — exact pattern TBD.

#### 9a. Multi-context Claude Code wiring (laptop + librarian + prod)

The user runs Claude Code in **three** contexts, each with its own `~/.claude.json` and its own connection-string considerations. As of **2026-05-04** all three are wired with the same MCP toolkit (stash + brave-search). The differences are network-topology-driven:

| Context | `mcpServers.stash.url` | Why | Tunnel needed |
| --- | --- | --- | --- |
| Laptop Claude Code | `http://localhost:8088/sse` | Laptop sits *outside* the Hetzner private network. Stash's :8080 is firewalled at the cloud edge — the SSH local-port-forward (`-L 8088:localhost:8080`) is the only valid path. | **Yes** — bare `ssh -f -N` (or autossh for persistence). |
| `ssh cemini-librarian` Claude Code | `http://localhost:8080/sse` | Stash binds to all interfaces on the librarian itself — direct localhost connection. | No. |
| `ssh cemini-prod` Claude Code | `http://10.0.0.2:8080/sse` | Prod (`10.0.0.3`) and librarian (`10.0.0.2`) share the Hetzner private network `enp7s0`. Verified `curl -sv http://10.0.0.2:8080/sse` returns `HTTP/1.1 200 OK` from prod. | No. |

The brave-search entry is identical across all three (`stdio` + `npx -y @brave/brave-search-mcp-server` + `BRAVE_API_KEY` in env). Both servers have Node 20+ and `npx` already installed (librarian has Node from kb-server; prod has Node from various ingest-layer containers).

**Conductor MCP on prod** is pre-wired at the project level via `/opt/cemini/.mcp.json` (`type: stdio`, `command: python3`, `args: ["/opt/cemini/conductor/mcp_server.py"]`). When Claude Code is invoked from `/opt/cemini/`, conductor auto-loads. Not needed in `~/.claude.json` on prod.

**Backups**: each `~/.claude.json` edit was preceded by `cp ~/.claude.json ~/.claude.json.bak-2026-05-04` on the host being edited. Roll back by `mv` if a wiring change goes bad.

**Activation gate**: Claude Code reads `~/.claude.json` only at process start. Each context requires a Claude Code restart in that context to pick up new MCP entries. Sessions already running keep their old config.

**Playwright is laptop-only.** Headless servers don't have a browser to drive — adding it on librarian/prod would just produce launch errors. Same logic for any other GUI-bound MCP.

**Required external API keys** for the laptop side (separate from server `.env`):
- `EXA_API_KEY` — Exa research. Set in `~/.claude/settings.json` user env. exa.ai/dashboard.
- `BRAVE_API_KEY` — Brave search MCP. Set in MCP env block.
- `ANTHROPIC_API_KEY` — Claude Code itself. console.anthropic.com (if not using Claude.ai subscription billing).
- `OPENAI_API_KEY` — only if using the codex plugin's GPT-5 hand-off. platform.openai.com.

### 10. First-run validation (smoke tests)

After step 6 + 7 complete:

1. **Container health** — `ssh cemini-prod "docker compose ps --format json | jq '.State'"` — every container reports `running`.
2. **Wiki sync** — `tail -20 ~/Library/Logs/cemini-wiki-sync.log` on laptop — last entry is recent and shows `kb ingest` success.
3. **MCP reach** — from laptop, ask Claude Code: "list pages in the wiki" — kb-server should respond with the wiki page list.
4. **Trading dry-run** — confirm `PAPER_TRADING=true` in prod `.env`, then check `cemini-prod` Grafana dashboard (via Cloudflare tunnel hostname) for paper-mode trade fills over a market session.
5. **Brain heartbeat** — `ssh cemini-prod "docker logs --tail 50 brain"` — recent log lines show DeepSeek API calls succeeding.

If any of the five fail, fix before flipping live flags.

### 11. Ongoing operations (out-of-scope here)

This guide stops at "first working deployment." Day-2 operations — backups, log rotation, certificate renewal, container updates, alert routing, incident response — live in `/opt/cemini/CLAUDE.md` on the production server (read-only from this workspace per project doctrine).

## Snippets

*(populate as setup-experience reports accumulate.)*

## Dead Ends

*(none yet — guide is freshly drafted 2026-05-03.)*
