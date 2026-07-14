# Message-DAG traces (K163)

Steal from Prime Intellect **verifiers v1** (Latent Space AINews 2026-07-14):
store rollout messages **once** and reference by id — O(n) vs O(n²) full-history
copies per turn. Do **not** install the PI stack (Watch only).

Code: `examples/message_dag_trace.py`.
Pairs with K161 hierarchical memory caps (`references/hierarchical-session-memory.md`).

## Env split (logging shape only)

| Layer | Arena mapping | Owns |
|-------|---------------|------|
| **Taskset** | `tests/fixtures/regression_spots.py`, scenario packs | Spot ids / expected actions |
| **Harness** | `decide()` / CLI / `cemini_preflight.sh` | Action selection + gates |
| **Runtime** | `arena_client.py`, lobby, submit | Network / Arena I/O |

Keep these separate in trace metadata (`layer` field). Do not fold Arena
HTTP payloads into decide harness rows.

## DAG schema

```json
{
  "schema": "devfun.message_dag.v1",
  "messages": {"m0": {"role": "system", "content": "..."}},
  "nodes": [
    {"id": "n0", "message_ids": ["m0"], "parent_ids": [], "layer": "harness"}
  ]
}
```

- `messages`: content addressed once (dedupe by hash or explicit id)
- `nodes`: turn/hand steps that **reference** message ids + parent node ids
- Reconstruct path with `materialize_node_history(dag, node_id)` — never store
  a full copy of prior messages on each node

## HL / analyze usage

When writing HL failure traces or trajectory exports:

1. Append each new analyst/hand message via `MessageDag.add_message`
2. Link the turn node with `parent_ids` to prior turns
3. Persist DAG JSON once per session (not per-turn full history)

## Out of scope

- RL trainer / verifiers package install
- Replacing `history.jsonl` monitor metrics (chip deltas stay flat JSONL)

## Related

- `briefs/2026-07-14_k163-verifiers-v1-message-dag-steal.md`
- `briefs/2026-07-13_k161-hierarchical-memory-deepsearch-steal.md`
