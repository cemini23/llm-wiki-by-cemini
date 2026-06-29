## Target

`agents/devfun-poker-arena/` — K132 Fara tri-verifier + K131 ToolBench-X hazard regression.

## Summary

Shipped private **tri-verifier** (correctness / efficiency / critical-point) for static-agent bundle regression. Relaxed NFL DecideTrace schema **deferred** (P1).

## Body

### Shipped (K132 + K131 pairing)

| Artifact | Role |
|----------|------|
| `examples/sandbox_tri_verifier.py` | FaraGen-style scoring API |
| `references/sandbox_tri_verifier_schema.json` | JSON schema for reports |
| `tests/test_sandbox_tri_verifier.py` | Hazard injection tests (6) |
| `scripts/run_sandbox_tri_verifier.sh` | CI/local runner |
| `references/sandbox-hazard-recovery.md` | join → poll → validate → act |

### Deferred

- K131 Relaxed NFL `DecideTrace` schema (`briefs/2026-06-26_k131-relaxed-nfl-verifier-steal.md`)
- Runtime `arena-tool` MCP agent (static `decide()` remains prod path)
- `microsoft/fara` repo install / CUA

### Commands

```bash
bash scripts/run_sandbox_tri_verifier.sh
uv run python examples/sandbox_tri_verifier.py  # demo trajectory
```

### Acceptance

- All `test_sandbox_tri_verifier.py` green
- bad_amount, generic reasoning, timeout hazards fail closed
- No new pip deps

## Sources

- `briefs/2026-06-27_k132-fara-verifier-harness-steal.md`
- `briefs/2026-06-26_k131-toolbench-x-arena-tool-steal.md`
