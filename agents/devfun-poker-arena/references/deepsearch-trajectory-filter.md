# DeepSearch trajectory filter (K161 + K139 delta)

Operator spec from arXiv **2607.07820** (DeepSearch-Evolve). Config:
`config/hu_deepsearch_trajectory_filter.json`.

## Loop shape (Watch — no env fork)

Steal **generate → filter → mix** only until DeepSearch-World env/data lands:

1. **Generate** — mine sandbox failure units (loss `hand_result` + adjacent decisions)
2. **Filter** — require all three tags; drop teacher-imitation / ungrounded reflection
3. **Mix** — advisory `eligible_pct` + `eligible_hand_ids` for HL epoch corpora

**Do not** vendor DeepSearch code or run teacher distillation.

## Required tags (K161 source of truth)

| Tag | Accept if |
|-----|-----------|
| `progress_verification` | `verified: true` OR next-hand chip delta improves |
| `grounded_reflection` | Reflection cites hole/board tokens from the unit |
| `failure_recovery` | Post-loss action/veto change vs prior same-spot class |

## Drop rules

- `teacher_imitation_only: true` → reject always
- Missing any required tag → reject (`missing_required_tags`)
- Ungrounded reflection → reject
- **K139:** missing `experience` after ≥2 same-spot fails →
  `missing_experience_after_repeat_fails`

Rejected units **must not** enter training/eval mix manifests. Advisory block only
(`devfun.deepsearch_trajectory_filter.v1`). `advisory_only` remains **true**.

## Scaffold fields (K139)

Paper scaffold → Arena analog (rename OK; documented in config
`scaffold_fields`):

| Scaffold field | Arena analog |
|----------------|--------------|
| `completed_list` | Verified facts (stack, board class, HUD tag) |
| `todo_list` | Next decide() checks / regression spot |
| `experience` | Lessons from prior losses in same spot class |
| `information` | Evidence tokens (cards/street/action) |

Helpers: `scaffold_block_for_brief`, `staged_reflection_hint` in
`examples/researcher_trajectory_summary.py`. HL template:
`examples/cemini_hl_brief.py`.

## Staged reflection strength (K139)

| Fail count in spot class | Hint strength |
|--------------------------|---------------|
| 1 (first fail) | soft — "recheck sizing vs HUD" |
| ≥2 (repeat) | strong_grounded — cite concrete board/street leak or veto |

No teacher gold actions from a stronger model — self-generated + filter-verified.

## CLI

```bash
uv run python examples/researcher_trajectory_summary.py \
  --selfplay path/to/selfplay_trajectory.jsonl \
  --deepsearch-filter-config config/hu_deepsearch_trajectory_filter.json
```

## Related

- `references/hierarchical-session-memory.md`
- `briefs/2026-07-13_k161-hierarchical-memory-deepsearch-steal.md`
- `briefs/2026-07-15_k139-deepsearch-scaffold-staged-reflection-delta.md`
