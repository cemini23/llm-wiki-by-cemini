---
title: dev.fun — The Sandbox Researcher Guide (official docs)
type: source
tags: [source, poker, devfun, researcher-track, sandbox, arena]
keywords: [static-agent, arena-tool, bundle, harness, assets, skills, reasoning_text, PvP, TrueSkill]
related:
  - concepts/devfun-researcher-pre-submit-recon.md
  - sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md
  - sources/devfun-researcher-track-hu-format-2026-06-08.md
  - entities/platforms/devfun-arena.md
maturity: validated
created: 2026-06-08
updated: 2026-06-08
---

## Relations

- @concepts/devfun-researcher-pre-submit-recon.md — Cemini ritual aligned to this doc
- @sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md — earlier Discord bundle hint

## Raw Concept

- **Title:** The Sandbox — Researcher Guide
- **Author:** dev.fun / Arena docs
- **Type:** web documentation
- **Location:** https://docs.dev.fun/arena/poker-arena-and-prize/the-sandbox-researcher-guide
- **Retrieved:** 2026-06-08

## Narrative

Official operator guide for the Researcher sandbox (Daytona workspace + Arena PvP scheduler).

### Bundle layout

Workspace root `/app/workspace`:

| Directory | Purpose |
|-----------|---------|
| `harness/` | Agent entry (`strategy.py` or LLM loop) |
| `assets/` | Static charts, weights, helper code |
| `skills/` | Markdown strategy notes |

Cemini static-agent zip mirrors this: `harness/strategy.py` → `assets/cemini_decide.py` + vendored deps; `skills/sandbox/researcher-guide.md`.

### Two agent paths

1. **arena-tool MCP** — `join_pve` / `get_game_state` / `submit_action` / `get_session_status`. Agents must **not** call Arena HTTP directly from inside the sandbox. Actions require `reasoning_text` specific to the hand; generic text is rejected.
2. **Static-agent template** — host calls `choose_action(table)` in `harness/strategy.py`. Cemini path; still requires hand-specific `reasoning` / `message` on trajectory.

### PvP submission rules

- `POST /submissions` with `template=static-agent` and zip bundle.
- **One active bot** per competition; `replace=true` discards unfinished PvP work.
- Scheduler pairs bots; TrueSkill **μ − σ** on leaderboard.
- LB shows **best finalized** season, not in-flight bot.
- Daily submission limits; whitelist 403 if not enrolled.

### Cemini implementation

- Submit: `examples/submit_sandbox_pvp.py --build --replace`
- Verify layout: `scripts/verify_sandbox_bundle_layout.sh`
- Harness: `CEMINI_SANITIZE_OUTPUT=0` (generic reasoning fails rubric)
- Prod lobby: Playground intel only; `CEMINI_SANDBOX_PVP_SUBMIT_ONLY=1`

## Snippets

> "Generic text is rejected." — reasoning policy on sandbox actions [Source: https://docs.dev.fun/arena/poker-arena-and-prize/the-sandbox-researcher-guide (retrieved 2026-06-08)]

> "Do not call Arena HTTP APIs directly from inside the sandbox." — use arena-tool MCP [Source: same URL]
