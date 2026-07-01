# Cemini — Researcher sandbox static agent

Official guide: https://docs.dev.fun/arena/poker-arena-and-prize/the-sandbox-researcher-guide

## Bundle layout (Daytona `/app/workspace`)

| Path | Role |
|------|------|
| `harness/strategy.py` | `choose_action(table)` — default `CEMINI_SANDBOX_ENGINE=cemini` → `cemini_decide` |
| `assets/cemini_decide.py` | Cemini K131b stack (live sandbox default) |
| `assets/gin_hu004_bridge.py` | Optional gin v3 `hu004` adapter when `CEMINI_SANDBOX_ENGINE=gin_hu004` |
| `assets/_vendor/gin_hu004/` | Vendored gin/poker-bot v3 HU brain (optional; pin omits when engine=cemini) |
| `skills/` | Operator notes (this file) — optional for Arena runner |

Submit via `examples/submit_sandbox_pvp.py --build --replace` (static-agent template), **not** `pokerkit run` on the Researcher PvP comp.

## Reasoning policy

Arena rejects **generic** `reasoning` / `reasoning_text` on actions. Harness defaults `CEMINI_SANITIZE_OUTPUT=0` so `cemini_decide` hand-specific reasoning ships on trajectory.

Playground lobby intel may still use `CEMINI_SANITIZE_OUTPUT=1` for anti-profiling.

## PvP scheduler

- One active bot per competition; `--replace` discards unfinished PvP work.
- Leaderboard ranks **best finalized** season (TrueSkill μ−σ), not the in-flight bot.
- Poll: `submit_sandbox_pvp.py --poll <submissionId>`

## Env posture (harness setdefaults)

**Sandbox default:** `CEMINI_SANDBOX_ENGINE=cemini`, `CEMINI_SANITIZE_OUTPUT=0` (reverted 2026-07-02 — gin +7.3 TS vs cemini +19 TS on S2).

**Optional gin engine:** `CEMINI_SANDBOX_ENGINE=gin_hu004`, `POKER_BOT_STRATEGY=hu004` — vendored via pin when explicitly enabled; local gate villain only when pin omits hu004.

S2 public LB may stay empty until **>20k hands** — poll submission + agent page.
