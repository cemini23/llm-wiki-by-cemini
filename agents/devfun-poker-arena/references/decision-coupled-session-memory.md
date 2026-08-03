# Decision-coupled session memory (K236)

On each `decide()`, also write progress / failure notes into **capped** hierarchical
session state in the **same turn** — do not schedule a second memory-only call.

## Steal

1. Couple action choice with short progress/failure waypoints (street, stack_bb, result tag).
2. Bound recent verbatim context; retrieve older spots by relevance / recency / salience.
3. Before inject: reconstruct for **current** spot (K230) — no verbatim dump of unrelated history.

## Already wired here

- `references/hierarchical-session-memory.md` + `examples/hierarchical_session_state.py`
- Lobby injects `hierarchical_memory_slice` beside `session_villain_memory`

## Do not

- Import HAM-VLN robotics code (no public repo; wont_wire)
- Paste full trajectories / exports into decide context

## Sources

- `briefs/2026-08-03_k235-k236-mutation-memory-steal.md`
- CCC `.cursor/rules/cemini-phase1-policy-wires.mdc` (K236)
- Sibling: `references/hierarchical-session-memory.md`
