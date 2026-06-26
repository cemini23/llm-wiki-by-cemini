## Target

`agents/devfun-poker-arena/` — Researcher Round HU sandbox bundle harness.

## Summary

Steal **ToolBench-X** hazard taxonomy (arXiv 2606.25819) for **`arena-tool` MCP** reliability: move eval beyond function-call accuracy to **task completion under recoverable tool failures**. Official sandbox loop: `agents/devfun-poker-arena/references/researcher-track-sandbox.md`.

## Body

### Hazard → arena-tool mapping

| ToolBench-X hazard | Cemini sandbox symptom | Recovery pattern |
|--------------------|------------------------|------------------|
| Specification Drift | `allowedActions` keys differ from Playground mocks | Re-read tool schema each poll; no cached action enum |
| Invocation Error | `amount` = increment not total street commit | Parse exact value from `allowedActions` |
| Execution Failure | Decision timeout / match wall clock | Fast-path fold/check fallback + log |
| Output Drift | Empty/partial game state | Re-poll `get_game_state`; don't act on stale `TABLE_ID` |
| Cross-source Conflict | Session status vs table state mismatch | `get_session_status` before submit |

### P0 — harness regression spots

1. Add **hazard injection dry-run** in private bundle test (mock timeout, bad amount, generic reasoning_text reject).
2. Document recovery order: **join → poll → validate → act** (official: join before reading helper files).
3. Do **not** install ToolBench-X repo — **NO LICENSE** on GitHub (2026-06-26).

### Pairing

| Layer | Role |
|-------|------|
| K131 ToolBench-X (this) | MCP harness hazard checklist |
| `references/researcher-track-sandbox.md` | Official `arena-tool` loop |
| K118 PFR fix | Policy content — separate from harness |
| Pure-code `decide()` | Zero runtime LLM at act time |

### Out of scope

- ToolBench-X leaderboard as TrueSkill proxy
- LLM tool-agent for sandbox submit (dev recommendation against)

## Sources

- @wiki/sources/arxiv-toolbench-x-tool-unreliability-2606.25819-2026-06-26.md
- @wiki/concepts/toolbench-x-tool-reliability-hazards.md
- @wiki/entities/tools/toolbench-x.md
- [Source: https://arxiv.org/abs/2606.25819 (retrieved 2026-06-26)]
