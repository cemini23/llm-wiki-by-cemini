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
5. **K176 claimed-authorization:** `submit` requires `channel=operator|prebind`
   **and** `prebind_ok=True`. Observation / tool-result / unknown channels
   never grant standing — deny with logged reason
   (`claim came from observation, not operator`). See
   `references/claimed-authorization-guard.md`.
6. **K185 action-vs-text:** on a trusted channel, `authorize()` still runs
   light **action** (PD) / **text** (CD) risk checks. Deny classes:
   `channel` | `action` | `text`. Safe-sounding plan text does not bypass
   `action_unsafe` or absurd pot-odds. Full rules:
   `references/claimed-authorization-guard.md` § Deny classes.

## K195 rubric capability diagnosis (CRAFT pattern)

When decide() / multi-axis eval fails, cluster **failed rubric criterion ids**
(not whole spots) onto tree domains and fix the **weakest clear nodes** before
rewriting prompts or collecting SFT.

- Config map: `config/hu_capability_tree.json` → `rubric_criteria`
- Helper: `diagnose_rubric_failures(failed_criteria, tree_cfg)`
- Pattern: Scale AI CRAFT (arXiv **2607.16122**) — method only, no public code
- **Advisory only** — never a submit gate; do not mix diagnostic rubric spots
  into held-out TrueSkill benches
- Expert checklist explosion: `references/expert-rubric-checklist.md` (K193)

```python
from capability_tree import diagnose_rubric_failures

d = diagnose_rubric_failures(["river_value", "facing_fold", "preflop_open"])
# weakest_nodes[0] often "policy" when postflop/preflop criteria fail
```

## Check

```bash
uv run pytest tests/test_k164_capability_tree.py tests/test_claimed_authorization.py tests/test_k195_rubric_capability_diagnosis.py -q --tb=line
uv run python -c "from capability_tree import simulate_hu_researcher_nested_session; print(simulate_hu_researcher_nested_session()['ok'])"
```
