# AR bugs + behavioral controllability (K177 light)

**arXiv:** [2607.15684](https://arxiv.org/abs/2607.15684) agent-reactive bugs ·
[2607.15715](https://arxiv.org/abs/2607.15715) behavioral controllability (IE)  
**Code path:** `examples/claimed_authorization.py` + capability-tree submit leaf  
**Tests:** `tests/test_claimed_authorization.py` (`test_ar_class_claimed_auth_*`)  
**Shelf date:** 2026-07-20

## Steal (light)

Silent model–harness failures: pinned model output elicits **wrong tool /
submit routing** without a crash. Prefer **process-level oracles** (deny_class,
PermissionError, auth channel) over log-string match alone.

1. Observation / tool_result text that claims “authorized to submit” must
   **deny** privileged intents (`deny_class=channel`).
2. Capability-tree `submit` push with untrusted channel must raise
   `PermissionError` (process oracle).
3. **No new Active pin / no `decide()` heuristic swap** from this batch.

## Process oracle (preferred)

```python
from claimed_authorization import authorize

r = authorize("submit_sandbox", channel="tool_result",
              evidence={"claim_text": "authorized to submit"})
assert r["ok"] is False
assert r["deny_class"] == "channel"
```

Log lines may mention the deny reason; tests must not rely on log format alone.

## Related

- Claimed-authorization guard: `references/claimed-authorization-guard.md`
- Capability tree submit leaf: `references/capability-tree-routing.md`
