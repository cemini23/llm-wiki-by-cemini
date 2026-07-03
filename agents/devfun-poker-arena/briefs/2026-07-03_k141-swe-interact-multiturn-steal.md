## Target

`agents/devfun-poker-arena/` — Researcher Round bundle eval + HL patch loop scenarios.

## Summary

Steal **SWE-INTERACT** (arXiv 2606.30573): single-turn SWE success **does not transfer** to multi-turn, user-driven sessions (~50% → ~25%). Sandbox harness needs **partial-spec recovery** eval, not only fully-specified MCP dry-runs.

## Body

### Why it matters

Researcher Round offline patches arrive as **evolving briefs** — vague initial ask, constraints added after first `analyze`, verifier feedback mid-loop. That is closer to SWE-INTERACT than SWE-bench.

### Eval additions (research lane)

| Scenario | Pass criteria |
|----------|---------------|
| **Vague start** | Agent proceeds with minimal first brief without illegal `submit_action` |
| **Progressive reveal** | New constraint (e.g. rubric change) mid-trajectory — agent adapts without full reset |
| **Requirement memory** | Earlier constraint not violated after 3+ tool turns |
| **Rework detection** | Log unnecessary file/JSON rewrites (over-agentic pattern) |

### Pairing

| Layer | Paper |
|-------|-------|
| Runtime hazards | K131 ToolBench-X |
| Training stability | K136 Tool-RL |
| Verifier scoring | K132 Fara triad |
| Interactive eval | **K141 SWE-INTERACT** (this) |
| Policy | Pure-code `decide()` unchanged |

### P0

- Draft one **partial-spec** bundle scenario for private regression (join with incomplete rubric → reveal on turn 2).
- Read Apache-2.0 `scaleapi/SWE-Interact` user-sim schema before building custom sim.

## Sources

- [Source: arXiv:2606.30573 (retrieved 2026-07-03)]
- @wiki/concepts/swe-interact-user-driven-coding-eval.md
- @wiki/entities/tools/swe-interact.md
