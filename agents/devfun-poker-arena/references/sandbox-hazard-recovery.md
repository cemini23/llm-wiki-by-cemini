# Sandbox hazard recovery

Use this recovery order for sandbox `arena-tool` / static-agent flow:

1. **Join** — establish the session before reading helper files or cached state.
2. **Poll** — fetch fresh session/table state; do not act on stale table ids.
3. **Validate** — confirm allowed actions, amount semantics, reasoning quality, and remaining budget.
4. **Act** — submit one legal action with hand-specific reasoning.

## ToolBench-X hazard map

| Hazard | Sandbox symptom | Recovery |
|---|---|---|
| Specification drift | `allowedActions` shape differs from mocks | Re-read live state each poll; do not cache enums |
| Invocation error | `amount` uses increment instead of total commit | Derive sizing from current `allowedActions` only |
| Execution failure | Timeout or idle poll loop burns match clock | Short-circuit to a safe legal action before budget expires |
| Output drift | Empty or partial table state | Poll again; never act on incomplete state |
| Cross-source conflict | Session status and table disagree | Check session status first, then re-validate table |
