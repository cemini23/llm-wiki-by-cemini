# Capability tree routing (K164)

Config: `config/hu_capability_tree.json`. Helper: `examples/capability_tree.py`.

## Steal

From arXiv **2607.11138** (hierarchical skill stack): replace flat tool/schema dumps with a **capability tree**. Top domains must be **mutually exclusive**. Lazy-load only the active node's children. Nested sub-analysis uses **push/pop** return. Binding leaves (`submit`) go through Prebind.

## Top domains (poker arena)

| Domain | Role |
|--------|------|
| `table` | HUD / spot memory / action context |
| `policy` | preflop / postflop / skill-binding |
| `memory` | hierarchical session, GenomeDiff, message DAG, yardstick |
| `eval` | self-play bb/100 (informational), rule graders, Researcher Round |
| `submit` | sandbox submit + prebind pin (executable leaf) |

## Nested frames (LIFO)

`CapabilityFrameStack.push` / `.pop` / `.visible_slice`:

1. Enter HU session on `eval` / `researcher_round`
2. Push `policy` for MAFP / leak lane
3. Push nested `memory` (yardstick / GenomeDiff) — then **pop** to return
4. `submit` only with `prebind_ok=True`

Smoke: `simulate_hu_researcher_nested_session()` (also written by `cemini_hl_brief.py` as `*.capability-session.json`).

## Rules

1. Do not dump all child schemas into a single `decide()` / HL prompt.
2. Cap visible children at `max_visible_children_per_call` (default 6).
3. Eval graders prefer **execution / rule-based** over model self-score (pairs K162).
4. `submit` never shares a root with `vendors`-style fetch domains — keep exclusive.

## Check

```bash
uv run pytest tests/test_k164_capability_tree.py -q
uv run python -c "from capability_tree import simulate_hu_researcher_nested_session; print(simulate_hu_researcher_nested_session()['ok'])"
```
