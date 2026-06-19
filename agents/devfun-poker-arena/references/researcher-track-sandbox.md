# Researcher track — sandbox recon (Cemini)

Operator: **cemini_wiki_poker** · **Researcher Round** (50 seats) · **heads-up** sandbox LB + trajectory contribution.

## Format [CONFIRMED 2026-06-08]

Researcher sandbox is **HU** (2-player NLHE). Source: `@wiki/sources/devfun-researcher-track-hu-format-2026-06-08.md`.

6-max gates remain for **Playground S3** intel only — not the Researcher optimization target.

## Working assumptions

| Item | Posture |
|------|---------|
| **Table size** | **Heads-up** [CONFIRMED dev.fun 2026-06-08] |
| **Match length** | **Multi-day** season (Playground/Tournament style) — **not** Eval 500h |
| **Submit cadence** | Same arena loop as Playground until skill contradicts |
| **Engine + LLM** | **Fixed** per PR [CONFIRMED per PR] — policy `decide()` layer only |

Still read `skillFile` for hand count, rubric weights, and economics when API ships (Jun 21).

## Challenge funnel (one-pager)

1. Submit → **sandbox LB** (trajectory + multi-axis — BenchFlow eval partner).
2. Top agents → **published champion bots** (“everyone else can come and challenge”).
3. Finale → HU vs Dwan/Jungleman on stream.

**Before first submit:** `bash scripts/run_researcher_comp_recon.sh --competition-id '<id>'` — see `wiki/concepts/devfun-researcher-pre-submit-recon.md`.

## Discord welcome [CONFIRMED 2026-06-18]

Channel: `#researcher-track` — $30K · 50 seats · Jun 21 · trajectory export · how-not-only-win eval.

Wiki: `wiki/sources/devfun-researcher-track-discord-welcome-2026-06-18.md`

## API recon

`scripts/list_arena_competitions.sh` — daily until Researcher comp appears.

| competitionId | name | notes |
|---------------|------|-------|
| `cmqf827h30u7dfca3x2aqvzjv` | Playground S3 | 6-max PVP — optional HUD |
| `seed_poker_eval_s1` | Eval S1 | PVE 500h panel — **wrong cadence template** for Researcher/Tournament |

## Local gates (before each submit)

```bash
CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh --hands 500
./scripts/export_researcher_trajectory.sh --competition-id "$ARENA_RESEARCHER_COMP_ID"
```

`CEMINI_TABLE_FORMAT` controls the local gate shape:

- `hu` (default) — HU regression + 2-player selfplay (Researcher sandbox)
- `6max` — 6-max regression + selfplay (Playground parity)
- `auto` — both bundles merged for combined gate

Current M8/M9 submit thresholds from `examples/researcher_trajectory_summary.py`:

- `M8_hallucination_rate <= 0.05`
- `M8_hole_leak_rate <= 0.02`
- `M9 positional vpip gap >= -0.20` (6-max: BTN–UTG; HU: BTN–BB)

Arena submit (when comp live):

```bash
./pokerkit run --agent examples/cemini_decide.py --max-hands 50   # smoke
./pokerkit run --agent examples/cemini_decide.py                    # full run (length TBD — likely multi-day season)
export ARENA_RESEARCHER_COMP_ID=<id>
./scripts/export_researcher_trajectory.sh --competition-id "$ARENA_RESEARCHER_COMP_ID"
```

## Competitor OSINT

See `wiki/concepts/devfun-poker-competitor-github-recon-2026-06.md` — **gin/poker-bot** v008 ported (`CEMINI_GIN_V008=1` with gin lane).

## Prod posture

- **Researcher Round** — **primary** optimization target (HU gates, trajectory, axis discipline).
- **Playground S3** — optional **background intel** only (`CEMINI_PACE_PHASE=intel`, ~1h join cadence); parallel S3 volume service **disabled** on prod prep apply.
- Ship **`cemini_decide.py`** with `CEMINI_TABLE_FORMAT=hu` for Researcher; 6-max gin lane for incidental Playground hands only.
