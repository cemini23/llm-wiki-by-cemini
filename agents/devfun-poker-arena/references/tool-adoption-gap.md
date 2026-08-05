# Tool-adoption gap (K245)

Adding more MCP/tools does not automatically raise instruction-only helper
quality. Measure whether tools are actually **called** on tool-reachable
spots before expecting uplift.

## Steal

1. Track solver/text tool adoption on tool-reachable spots; do not dump
   tools onto instruction-only helpers expecting uplift.
2. After a successful solver/text tool call, skip redundant screenshot /
   table dumps on the next turn when the observation is consistent —
   `should_skip_redundant_table_dump(last_obs_hash, new_obs_hash,
   solver_ok)` in `examples/solver_preflight.py`.

## Do not

- Blindly grow the MCP tool surface expecting helper uplift
- Re-dump a screenshot/table when the last solver output is consistent

## Sources

- arXiv 2608.03327 (K245)
- `examples/solver_preflight.py`
- `examples/solver_context_prune.py` (K199 — existing prune)
- `briefs/2026-08-05_k244-k245-steal.md`
