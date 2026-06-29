# Cemini — Researcher sandbox static agent

Official guide: https://docs.dev.fun/arena/poker-arena-and-prize/the-sandbox-researcher-guide

## Bundle layout (Daytona `/app/workspace`)

| Path | Role |
|------|------|
| `harness/strategy.py` | `choose_action(table)` entry — calls `assets/cemini_decide.decide()` |
| `assets/` | Policy code + vendored deps (`_vendor/`) |
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

HU researcher: `CEMINI_TABLE_FORMAT=hu`, gin lanes, trajectory bound, verifier BON, v008 + v2 exploits.
