# Researcher track — sandbox recon (Cemini)

Operator: **cemini_wiki_poker** · **Researcher Round** (50 seats) · **6-max** sandbox LB + trajectory contribution.

## Working assumptions [operator 2026-06-18]

| Item | Posture |
|------|---------|
| **Table size** | **6-max NLHE** (like Playground / Eval) — not HU-only |
| **Match length** | **500 hands** full benchmark (Eval S5); `pokerkit run --max-hands 50` smoke |
| **Submit cadence** | Same as poker-eval — `benchmark/start` + `pokerkit run`, resume on rerun |
| **Engine + LLM** | **Fixed** per PR [CONFIRMED per PR] — policy `decide()` layer only |

Confirm or override when Researcher competition `skillFile` ships (Jun 21).

## Discord welcome [CONFIRMED 2026-06-18]

Channel: `#researcher-track` — $30K · 50 seats · Jun 21 · trajectory export · how-not-only-win eval.

Wiki: `wiki/sources/devfun-researcher-track-discord-welcome-2026-06-18.md`

## API recon (2026-06-18)

`scripts/list_arena_competitions.sh` — daily until Researcher comp appears.

| competitionId | name | notes |
|---------------|------|-------|
| `cmqf827h30u7dfca3x2aqvzjv` | Playground S3 | 6-max PVP — optional HUD |
| `seed_poker_eval_s1` | Eval S1 | PVE **500h** reference panel — cadence template |

## Local gates (before each submit)

```bash
./scripts/run_hu_sandbox_gate.sh --hands 500   # 6-max regression + selfplay + trajectory
./scripts/export_researcher_trajectory.sh --competition-id "$ARENA_RESEARCHER_COMP_ID"
```

Arena submit (when comp live):

```bash
./pokerkit run --agent examples/cemini_decide.py --max-hands 50   # smoke ~3-5 min
./pokerkit run --agent examples/cemini_decide.py                    # full 500h ~15 min
export ARENA_RESEARCHER_COMP_ID=<id>
./scripts/export_researcher_trajectory.sh --competition-id "$ARENA_RESEARCHER_COMP_ID"
```

## Prod posture

- **Playground S3** — optional field intel; Researcher LB is separate comp.
- Ship same **`cemini_decide.py`** 6-max stack unless beta skill restricts surface.
