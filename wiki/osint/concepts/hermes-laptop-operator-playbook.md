---
title: Hermes operator playbook — split laptop + librarian topology
type: concept
tags: [hermes, skillclaw, operator, k113, cadence, telegram]
keywords: [hermes-workspace, honesty-critic, cron, librarian-readonly, always-on]
related:
  - entities/tools/hermes-workspace.md
  - entities/tools/hermes-agent.md
  - entities/tools/skillclaw.md
  - sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md
  - meta/wiki-gap-detect-cadence.md
  - concepts/librarian-server-architecture.md
  - "@ccc-wiki/concepts/claude-honesty-critic-agent.md"
  - "@ccc-wiki/concepts/remote-hermes-access-pattern.md"
  - "@ccc-wiki/concepts/agent-personality-file-hermes-openclaw.md"
maturity: draft
created: 2026-06-12
updated: 2026-06-13
---

## Relations

- @entities/tools/hermes-workspace.md — laptop UI
- @entities/tools/hermes-agent.md — host runtime (K52 reference + always-on framing)
- @entities/tools/skillclaw.md — skill evolution proxy
- @concepts/librarian-server-architecture.md — 24/7 knowledge host
- @ccc-wiki/concepts/claude-honesty-critic-agent.md — honesty protocol
- @ccc-wiki/concepts/remote-hermes-access-pattern.md — K90 gateway pattern now deployed on librarian
- @ccc-wiki/concepts/agent-personality-file-hermes-openclaw.md — SOUL.md deployment

## Raw Concept

K113 pilots A→B→C on laptop; revised 2026-06-12 for **split topology**: laptop = dev/UI/SkillClaw; **cemini-librarian** = always-on gateway + phone (Telegram). Prod remains NO-GO.

## Narrative

### Operational status `[CONFIRMED]` 2026-06-13

| Surface | Status |
|---------|--------|
| Librarian gateway | **GO** — `hermes-gateway.service` active; @Cemini23_bot inbound + outbound |
| Librarian crons | **GO** — `wiki-gap-tier1-due` (weekly), `daily-digest-due` (daily); Telegram deliver; silent when healthy |
| Laptop SkillClaw + workspace | **GO** — dev profile; PRM disabled |
| Prod `/opt/cemini` | **NO-GO** — unchanged |
| picobot | Stopped on prod 2026-06-13 — Hermes owns bot polling until wiki-via-Telegram returns |

**Pre–full-wiki-ingest note:** Hermes operator stack is live. Adoption audit for OSINT + CCC wikis only — other federation wikis unlikely to need Hermes pages unless tool eval surfaces new URLs.

### Wiki map (Hermes-related)

| Page | Role |
|------|------|
| @entities/tools/hermes-agent.md | Nous host runtime; memory/skills/cron/gateway; Cemini **reference** not trading adoption |
| @entities/tools/hermes-workspace.md | Web GUI (laptop only) |
| @entities/tools/skillclaw.md | Collective skill evolution via proxy |
| @entities/tools/hermes-lcm.md | Context-engine **plugin** (not the host) |
| @concepts/hermes-onchain-forensics-pipeline.md | K78 skill-bundle forensics pattern |
| @sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md | K113 tool eval source |
| This page | Operator playbook |

Trading-post mentions of "Hermes" in weather/copy-trading posts refer to **Hermes Agent** as deploy runtime — not CeminiSuite Conductor.

### Placement decision `[CONFIRMED]` 2026-06-12 (revised)

| Host | Verdict | Role |
|------|---------|------|
| **Laptop** | **GO** | Workspace UI, SkillClaw dev, wiki git authoring (Cursor), optional local gateway when awake |
| **cemini-librarian** | **CONDITIONAL-GO** | **Always-on gateway** (systemd); outbound Telegram cron; inbound chat only with **dedicated bot** (not @Cemini23_bot while picobot runs) |
| **cemini-prod** | **NO-GO** | Trading stack; agent+terminal risk; briefs-only boundary |

**Laptop-off truth:** Hermes on laptop **does not run** when the machine sleeps. Cron with `--deliver local` on laptop is **dev-only**. Production reminders must live on librarian with Telegram delivery.

Librarian fit: already 24/7 (kb-server, stash, Ollama); ~3.7 GiB RAM — headless gateway OK; **skip SkillClaw on librarian initially** (saves RAM; direct DeepSeek upstream).

### Optimized laptop profile

| Item | Path / setting |
|------|----------------|
| Memory | `~/.hermes/MEMORY.md`, `USER.md` — Cemini topology + prefs |
| Persona | `~/.hermes/SOUL.md` — honesty + prod boundary |
| Workdir context | `OSINT WORKSPACE/.hermes.md` |
| Skills (custom) | `honesty-critic`, `cemini-librarian-readonly`, `ai-research-*` (laptop cherry-picks) |
| Cron scripts (git) | `scripts/hermes/` → `~/.hermes/scripts/` via `install_hermes_cron_scripts.sh` |
| Trial skills | `~/.hermes/skills/_trial/` — auto-written skills until operator promotes |
| SkillClaw | `~/.skillclaw/config.yaml`; PRM **disabled**; `skillclaw start --daemon` |
| LLM path | Laptop dev: via SkillClaw proxy → DeepSeek |

After reboot (laptop dev):

```bash
hermes gateway run --replace   # optional when laptop awake
cd ~/hermes-workspace && npm run dev
skillclaw start --daemon
```

### Pilot A — SkillClaw + honesty `[CONFIRMED]` 2026-06-12

- `skillclaw doctor hermes` PASS
- Honesty port from K112 CCC concept

### Pilot B — scheduled ops `[CONFIRMED]` laptop; **migrate to librarian**

Laptop cron (interim): `wiki-gap-tier1-due`, deliver `local` — **replace** when librarian Telegram cron verified.

Librarian target:

```bash
hermes cron add "every 7d" --name wiki-gap-tier1-due \
  --no-agent --script cemini-wiki-gap-due.sh --deliver telegram \
  --workdir /opt/cemini-osint-workspace
```

Script auto-detects `/opt/cemini-osint-workspace` or laptop path.

**Alert discipline:** no-agent cron delivers **stdout only**. Script is **silent when healthy** (no message). Alerts when **degraded** (wiki-gap overdue). No per-minute spam — schedule is weekly (`every 10080m`). Burst during setup was from manual `hermes cron run` tests.

`cron.wrap_response: false` on librarian — no "Cronjob Response:" wrapper prefix.

### Pilot C — librarian read-only `[CONFIRMED]` 2026-06-12

kb_search canonical in **Cursor + lazy-tool**. Hermes uses `cemini-librarian-readonly` skill for SSH inspection.

### Secrets sourcing `[CONFIRMED]` 2026-06-12

| Secret | Source | Bot / provider |
|--------|--------|----------------|
| `DEEPSEEK_API_KEY` | `cemini-librarian:/opt/cemini/.env` | DeepSeek |
| `TELEGRAM_BOT_TOKEN` | `cemini-prod:/opt/cemini/.env` | **@Cemini23_bot** (Cemini) |

Sync: `python3 scripts/configure_hermes_librarian_secrets.py`

### Phone connection — Telegram + picobot conflict `[CONFIRMED]` 2026-06-12

**@Cemini23_bot** is already polled by **picobot** on `cemini-prod` (`getUpdates`). Hermes **cannot** run inbound Telegram on the same token without evicting picobot.

| Mode | Verdict |
|------|---------|
| **Outbound cron/alerts** via same @Cemini23_bot | **GO** — token + `TELEGRAM_HOME_CHANNEL`; script silent unless degraded |
| **Interactive Hermes chat** on @Cemini23_bot | **GO** `[CONFIRMED]` 2026-06-13 — picobot stopped on prod; Hermes owns polling on librarian |

**picobot:** stopped on `cemini-prod` (`docker stop picobot`) 2026-06-13 — operator not using Telegram wiki ingest. Restarts if `docker compose up` redeploys picobot; leave stopped until wiki-via-Telegram returns.

**Telegram allowlist:** `TELEGRAM_ALLOWED_USERS=6652585143` (operator only); `GATEWAY_ALLOW_ALL_USERS=false`.

### Model routing `[CONFIRMED]` 2026-06-13

| Tier | Provider | Model | When |
|------|----------|-------|------|
| Primary | `deepseek` | `deepseek-v4-flash` | Default Telegram + terminal |
| Fallback | `openrouter` | `anthropic/claude-sonnet-4` | Auto on primary failure |
| Manual | `/model` in chat | picker | Operator override per session |

**Not supported:** Cursor subscription API — Hermes has no Cursor provider; Cursor stays laptop-only.

**Failure seen 2026-06-13:** `provider=deepseek` + `model=anthropic/claude-opus-4.6` → HTTP 400. Fixed via `scripts/configure_hermes_librarian_models.py`.

Keys: `DEEPSEEK_API_KEY` from librarian `/opt/cemini/.env`; `OPENROUTER_API_KEY` from prod `/opt/cemini/.env`.

**Identity honesty (SOUL):** Status replies must cite active `/model` or config default — never claim Opus/Claude on DeepSeek unless actually selected.

**SOUL structure (K90 Voxyz + audit 2026-06-13):** Voice, Boundaries, Anti-patterns, Scope-lock, Honesty, Model routing, Skill discipline, Wiki context.

**Auxiliary orchestra:** `title_generation` + `compression` → OpenRouter `google/gemini-2.0-flash-001`; `agent.reasoning_effort: low`. Apply: `python3 scripts/configure_hermes_librarian_models.py` (librarian) + `python3 scripts/patch_hermes_local_models.py` (laptop).

**Model aliases:** `/model fast` (DeepSeek flash), `/model hard` (OpenRouter Sonnet).

**Env:** `WIKI_PATH` + `CEMINI_OSINT_ROOT` in `~/.hermes/.env` — enables bundled `llm-wiki` skill.

Librarian crons (Telegram, silent when healthy):

| Job | Schedule | Script |
|-----|----------|--------|
| `wiki-gap-tier1-due` | weekly | `cemini-wiki-gap-due.sh` |
| `daily-digest-due` | daily | `cemini-daily-digest-due.sh` |

Laptop duplicate cron **removed** — librarian only.

Interactive setup (new bot only):

1. BotFather → new bot → token in `/root/.hermes/.env`
2. `hermes setup gateway` → enable Telegram inbound
3. Message bot from phone

Alternatives: Signal (more setup), Discord. **Not** iMessage/Photon for librarian (requires Mac).

### Bootstrap scripts (laptop → librarian)

```bash
bash scripts/install_hermes_librarian_gateway.sh
bash scripts/sync_hermes_profile_to_librarian.sh   # SOUL, memory, skills, scripts
python3 scripts/configure_hermes_librarian_models.py   # models + WIKI_PATH + aux
bash scripts/hermes/install_hermes_cron_scripts.sh   # laptop ~/.hermes/scripts
```

Remote OSINT mirror: `/opt/cemini-osint-workspace` (rsync from laptop; not `/opt/cemini`).

### What Hermes is not

- Not replacing Cursor for wiki ingest/lint/commit
- Not modifying `/opt/cemini`
- Not replacing kb-server

## Snippets

Hermes entity always-on line (K52): gateway + cron + messaging when deployed on a VPS — applies to **librarian**, not prod. [Source: @entities/tools/hermes-agent.md]
