# Claimed-authorization guard (K176)

**arXiv pattern:** [2607.11698](https://arxiv.org/abs/2607.11698) (AHA / Vulnerability Concept Graph — claimed-authorization core only)  
**Code:** `examples/claimed_authorization.py`  
**Wire:** `examples/capability_tree.py` submit leaf + `config/hu_capability_tree.json`  
**Shelf date:** 2026-07-16

## Steal (pattern only)

Self-claimed authorization from untrusted channels is invalid. Poker agent
tool routes must not treat scraped table text, opponent `message` fields, or
tool-result prose as approval for bankroll spend, all-in, live bind, or
sandbox submit.

**No AHA harness install** in this repo — standing check only.

## Channels

| Channel | Standing for privileged intents? |
|---------|----------------------------------|
| `operator` | Yes |
| `prebind` | Yes |
| `observation` | **No** — deny: `claim came from observation, not operator` |
| `tool_result` | **No** |
| `unknown` | **No** |

## Privileged intents

- `submit_sandbox`
- `all_in` / bankroll spend (`bankroll_spend`)
- `live_table_action` bind

## API

```python
from claimed_authorization import authorize, prebind_ok_from_channel

authorize("submit_sandbox", channel="observation")
# → {ok: False, reason: "claim came from observation, not operator", ...}

authorize("submit_sandbox", channel="prebind", evidence={"prebind_ok": True})
# → {ok: True, reason: "standing from prebind", ...}

prebind_ok_from_channel(channel="observation", operator_prebind=True)
# → False  (observation never sets prebind_ok)
```

Capability tree:

```python
stack.push("submit", prebind_ok=True, channel="prebind")   # ok
stack.push("submit", prebind_ok=True, channel="observation")  # PermissionError
```

## Isolation (pairs K167)

Opponent / table `message` fields are **DATA, not instructions**. Optional
helper `isolate_table_observation_text(table)` strips phrases like
“user approved” / “authorized all-in” for audit hygiene; it never upgrades
standing. `decide()` sizing must not treat those phrases as shove approval.

## Related

- Capability routing: `references/capability-tree-routing.md` (K164)
- Belief audit isolation: `examples/belief_deviation_audit.py` (K167)
- Briefs: `briefs/2026-07-16_k176-claimed-authorization-light-steal.md`,
  `briefs/2026-07-16_k176-k157-master-plan.md`

## Check

```bash
uv run pytest tests/test_claimed_authorization.py tests/test_k164_capability_tree.py -q --tb=line
```
