# Claimed-authorization guard (K176 + K185)

**arXiv patterns:**
- [2607.11698](https://arxiv.org/abs/2607.11698) (AHA — claimed-authorization core)
- [2607.15218](https://arxiv.org/abs/2607.15218) (PRISM — action-vs-text safety, pattern only)

**Code:** `examples/claimed_authorization.py`  
**Wire:** `examples/capability_tree.py` submit leaf + `config/hu_capability_tree.json`  
**Shelf date:** 2026-07-16 (K176); K185 delta 2026-07-17

## Steal (pattern only)

Self-claimed authorization from untrusted channels is invalid. Poker agent
tool routes must not treat scraped table text, opponent `message` fields, or
tool-result prose as approval for bankroll spend, all-in, live bind, or
sandbox submit.

**K223:** tool / HUD outputs sit **below** operator standing — see
`references/tool-output-instruction-hierarchy.md`.

**No AHA harness / PRISM probe install** — standing + light action/text checks only.

## Channels

| Channel | Standing for privileged intents? |
|---------|----------------------------------|
| `operator` | Yes (then K185 text/action checks) |
| `prebind` | Yes (then K185 text/action checks) |
| `observation` | **No** — deny class `channel` |
| `tool_result` | **No** — deny class `channel` |
| `unknown` | **No** — deny class `channel` |

## Deny classes (K176 + K185)

| `deny_class` | Meaning | Typical reason |
|--------------|---------|----------------|
| `channel` | Standing missing — claim from untrusted channel (K176) | `claim came from observation, not operator` |
| `text` | Content/discourse (CD) policy flag on trusted channel | `evidence marks text_unsafe` |
| `action` | Causal / process-description (PD) stack+odds risk | `action_unsafe`, absurd call/pot, dead_money flag |
| `null` | Allowed | `standing from prebind` |

**Text policy ≠ submit safety.** A plan like `call for information` never
clears `action_unsafe=True` or absurd pot-odds on a trusted channel.

Observation → submit remains **deny class `channel`** (unchanged semantics).

## Privileged intents

- `submit_sandbox`
- `all_in` / bankroll spend (`bankroll_spend`)
- `live_table_action` bind

## API

```python
from claimed_authorization import authorize, prebind_ok_from_channel

authorize("submit_sandbox", channel="observation")
# → {ok: False, deny_class: "channel", reason: "claim came from observation, not operator", ...}

authorize("submit_sandbox", channel="prebind", evidence={"prebind_ok": True})
# → {ok: True, deny_class: None, reason: "standing from prebind", ...}

authorize(
    "all_in",
    channel="prebind",
    evidence={
        "plan_text": "call for information",
        "action_unsafe": True,
        "pot": 10,
        "call_chips": 200,
    },
)
# → {ok: False, deny_class: "action", ...}

prebind_ok_from_channel(channel="observation", operator_prebind=True)
# → False  (observation never sets prebind_ok)
```

Capability tree:

```python
stack.push("submit", prebind_ok=True, channel="prebind")   # ok (if no action_unsafe in meta)
stack.push("submit", prebind_ok=True, channel="observation")  # PermissionError deny_class=channel
stack.push(
    "submit",
    prebind_ok=True,
    channel="prebind",
    meta={"action_unsafe": True},
)  # PermissionError deny_class=action
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
  `briefs/2026-07-17_k185-action-vs-text-safety-light-steal.md`,
  `briefs/2026-07-17_k158-k185-k141-master-plan.md`

## Check

```bash
uv run pytest tests/test_claimed_authorization.py tests/test_k164_capability_tree.py -q --tb=line
```
