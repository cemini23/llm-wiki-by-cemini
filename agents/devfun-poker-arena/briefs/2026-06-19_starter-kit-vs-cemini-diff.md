# poker-arena-starter-kit vs `agents/devfun-poker-arena` (2026-06-19)

## Target

Operator / dev — understand drift between dev.fun starter kit and Cemini prod fork before Jun 21 sandbox submit.

## Summary

Cemini keeps starter-kit CLI surfaces but ships HU Researcher track (`cemini_decide.py`, trajectory gates, series match audit) not present upstream.

**Upstream:** https://github.com/devfun-org/poker-arena-starter-kit  
**Cemini fork:** `agents/devfun-poker-arena/` (prod `/opt/devfun-poker-arena`)

## Alignment

| Starter-kit | Cemini |
|-------------|--------|
| `pokerkit` CLI (`test`, `selfplay`, `analyze`) | Same + `scripts/run_hu_sandbox_gate.sh`, researcher recon |
| `examples/agent.py` + `llm_agent.py` | **`cemini_decide.py`** pure-code `decide()` (no runtime LLM) |
| `research_static_chart.py` | Extended `_HU_OPEN_CHART`, table format resolver |
| `selfplay.py` | + `match_win_rate`, `--match-hands` / `--matches` |
| `arena_client.py` | + lobby loop, trajectory export, HL tooling |

## Cemini-only (Researcher track)

- `CEMINI_TABLE_FORMAT=hu`, `CEMINI_RESEARCHER_MODE`, trajectory M₁–M₉ gates
- `session_memory.py` F6, `s1b_exploit.py` HU 3-bet vs LAG
- `researcher_trajectory_summary.py`, `run_researcher_comp_recon.sh`
- Prod systemd: `cemini-devfun-poker-lobby.service` (Researcher PRIMARY posture)

## Sync ritual (when starter-kit updates)

1. Diff `examples/{arena_client,selfplay,research_static_chart}.py`
2. Port non-conflicting fixes; keep `cemini_decide.py` as policy surface
3. Re-run `CEMINI_TABLE_FORMAT=hu bash scripts/run_hu_sandbox_gate.sh --hands 500`

## Jun 21

Researcher HU SDK rubric + Kaggle path expected in starter-kit / rules email — pin `competitionId` then reconcile CLI submit vs `pokerkit run`.

## Sources

- [Source: https://github.com/devfun-org/poker-arena-starter-kit (retrieved 2026-06-19)]
- `@concepts/devfun-researcher-track-readiness-2026-06.md`
