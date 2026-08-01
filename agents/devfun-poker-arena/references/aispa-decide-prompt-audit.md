# AISPA — decide() instruction inventory (K232)

Steal from arXiv 2607.28617. Audit protective vs problematic instruction spans
before shipping any LLM-backed decide path.

## Inventory (cemini_decide primary, 2026-08-01)

| Surface | Present? | Notes |
|---------|----------|-------|
| LLM system prompt in `cemini_decide.py` | **No** | Heuristic stack |
| Arena `reasoning` / `message` strings | Yes | Short structured tags (`vr`/`ke`/`pp`) — not policy prompts |
| Lobby sanitize / claimed-auth | Yes | Tool-output hierarchy; not AISPA spans |
| Hybrid LLM on hard nodes (System7-style) | **Not shipped** | When added: run AISPA span audit + protective-density gate |

## Ops

- Protective-instruction density is a release gate **only** when an LLM prompt path exists.
- Do not invent prompts to satisfy this steal.

## Sources

- `briefs/2026-07-31_k232-system-prompt-audit-steal.md`
- CCC `.cursor/rules/cemini-phase1-policy-wires.mdc` (K232)
