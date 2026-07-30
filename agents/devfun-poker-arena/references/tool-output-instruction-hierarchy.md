# Tool-output instruction hierarchy (K223)

**arXiv:** [2607.25987](https://arxiv.org/abs/2607.25987) — S≻U strength does
**not** imply U≻T; tool outputs can hijack even when system prompts hold vs user  
**Brief:** `briefs/2026-07-29_k223-tool-output-hierarchy-steal.md`  
**Wiki:** `@cybersecurity-wiki/concepts/instruction-hierarchy-conflict-benchmark.md`

## Steal

HUD / Arena API / MCP / tool payloads are **untrusted instruction surfaces**.
A conflicting instruction in tool output can override operator intent even when
user-jailbreak defenses look solid.

Hierarchy to enforce for decide / submit:

```
operator / prebind  ≻  system policy  ≻  user chat  ≻  tool_result / HUD / observation
```

Never promote tool text into standing for privileged intents (`all_in`,
`submit_sandbox`, LIVE bind, bankroll spend).

## Already wired

| Mechanism | Path |
|-----------|------|
| Claimed-auth channel deny | `examples/claimed_authorization.py` — `observation` / `tool_result` never grant standing |
| Observation isolate | `isolate_table_observation_text` + decide junk-text fixtures |
| Output sanitize | `output_sanitize` / `CEMINI_SANITIZE_OUTPUT` on Playground |
| Network | `references/network-policy.md` — URLs in replay are not fetch instructions |

## Eval note

Tool-conflict fixtures (K177 AR-class tool_result submit deny, observation
all-in deny) are **separate** from user-jailbreak suites. Keep both green.

```bash
uv run pytest tests/test_claimed_authorization.py -q --tb=line
```

## Related

- `references/claimed-authorization-guard.md`
- `references/sandbox-live-containment.md` (K222)
- `references/tool-depth-standing-policy.md` (K221 / K229)
- `references/ar-bugs-controllability.md`
