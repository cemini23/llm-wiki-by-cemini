# Turn-street scores (K191 / K193)

**arXiv pattern:** ToolVerse credit-assignment (2607.15660) — log per-step /
per-street success signals for long-horizon trajectories, not only terminal
session PnL.  
**Code:** `examples/turn_street_scores.py`  
**Wire:** optional key `turn_street_scores` on
`researcher_trajectory_summary.summarize_selfplay_trajectory`  
**Shelf date:** 2026-07-20

## Steal (pattern only)

Multi-street NLHE is long-horizon with sparse terminal reward. When diagnosing
agent trajectories:

1. Score **each decision** with street + facing + action class.
2. Aggregate **per-street tallies** (counts, optional success rates).
3. Do **not** collapse diagnosis to session PnL alone.

No ToolVerse install — methodology only. **Advisory** — never a hard submit
gate or `decide()` threshold.

## API

```python
from turn_street_scores import score_decision_street, aggregate_turn_scores

sc = score_decision_street({
    "street": "Turn",
    "action": "call",
    "call_chips": 10,
    "success": True,
})
# → street=Turn, facing=bet, action_class=passive, success=True

agg = aggregate_turn_scores(trajectory_rows)
# → by_street[Preflop|Flop|Turn|River] tallies
```

## Fields

| Field | Meaning |
|-------|---------|
| `street` | Preflop / Flop / Turn / River (normalized) |
| `facing` | `check` (free) / `bet` / `raise` / `unknown` |
| `action_class` | `fold` / `passive` / `aggressive` / `other` / `unknown` |
| `success` | optional bool from `success` / `won` / positive `chip_delta` |

## Related

- Expert rubric checklist: `references/expert-rubric-checklist.md` (K193)
- Trajectory summary: `examples/researcher_trajectory_summary.py`
