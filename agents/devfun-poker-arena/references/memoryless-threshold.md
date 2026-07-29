# Memoryless threshold (K143)

**arXiv:** [2607.16145](https://arxiv.org/abs/2607.16145) — memoryless best-choice
/ imperfect observation → optimal policy collapses to **threshold strategies**.  
**Config tag:** `memoryless_threshold` on hierarchical memory drills  
**Shelf date:** 2026-07-20

## Steal (advisory only)

When spot-class memory is intentionally compressed — or intentionally wiped for
a drill — prefer calibrated **absolute thresholds** over relative-rank /
“best so far” heuristics.

| Mode | State retained | Policy shape |
|------|----------------|--------------|
| Full-info | Running best / relative ranks / session HUD | Record rules, relative sizing |
| Memoryless | No past ranks / wiped hierarchical mid-term | Threshold on **absolute** signal only |

**Do not mix:** if hierarchical memory (K161) is off or spot history is wiped,
do not apply relative-rank sizing logic copied from full-history sims.

## Balance-at-boundary

Thresholds for call/fold or bet-size bins should be solved against the
**remaining horizon** (stack depth / streets left), not a static EV cutoff
from full-info sessions.

## Operator checklist

1. Tag drills that intentionally wipe relative-rank history as
   `memoryless_threshold` (see `config/hu_hierarchical_memory.json`).
2. Keep full-info record rules behind the hierarchical memory path.
3. **Advisory only** — no hard submit gate; **no `decide()` retune** from
   this note alone.

## Non-goals

- No decide() threshold ship from K143
- No pin / Active change
- No gin flip / runtime LLM

## Related

- Hierarchical session memory: `references/hierarchical-session-memory.md`
- Config: `config/hu_hierarchical_memory.json` → `memoryless_threshold_tag`
