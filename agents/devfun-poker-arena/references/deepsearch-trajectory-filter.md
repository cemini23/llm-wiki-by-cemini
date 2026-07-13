# DeepSearch trajectory filter (K161)

Operator spec from arXiv **2607.07820** (DeepSearch-Evolve). Config:
`config/hu_deepsearch_trajectory_filter.json`.

## Loop shape (Watch — no env fork)

Steal **generate → filter → mix** only until DeepSearch-World env/data lands:

1. **Generate** — mine sandbox failure units (loss `hand_result` + adjacent decisions)
2. **Filter** — require all three tags; drop teacher-imitation / ungrounded reflection
3. **Mix** — advisory `eligible_pct` + `eligible_hand_ids` for HL epoch corpora

**Do not** vendor DeepSearch code or run teacher distillation.

## Required tags

| Tag | Accept if |
|-----|-----------|
| `progress_verification` | `verified: true` OR next-hand chip delta improves |
| `grounded_reflection` | Reflection cites hole/board tokens from the unit |
| `failure_recovery` | Post-loss action/veto change vs prior same-spot class |

## Drop rules

- `teacher_imitation_only: true` → reject always
- Missing any required tag → reject (`missing_required_tags`)
- Ungrounded reflection → reject

Rejected units **must not** enter training/eval mix manifests. Advisory block only
(`devfun.deepsearch_trajectory_filter.v1`).

## CLI

```bash
uv run python examples/researcher_trajectory_summary.py \
  --selfplay path/to/selfplay_trajectory.jsonl \
  --deepsearch-filter-config config/hu_deepsearch_trajectory_filter.json
```

## Related

- `references/hierarchical-session-memory.md`
- `briefs/2026-07-13_k161-hierarchical-memory-deepsearch-steal.md`
