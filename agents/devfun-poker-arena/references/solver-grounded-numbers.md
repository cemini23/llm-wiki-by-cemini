# Solver-grounded numbers + tool-dump prune (K199/K201)

## Solver-grounded

EV, pot odds, and solver frequencies must come from **trusted tools / baked tables** (`solver_frequencies`, MAFP chart, TexasSolver bake). LLM / HL prose **narrates** — it does not invent numbers.

## Tool dumps

Long multi-hand threads: **cap and summarize** verbose tool output. Do not re-feed full solver logs every turn (closed-model N/W pattern).

Helper: `examples/solver_context_prune.py` → `prune_solver_context`.

## Tool depth (K221 / K229)

After ranking helpers, stop loading more tools into context. Standing SOP and
advantage gates before solver-depth / gin / MAFP flips:
`references/tool-depth-standing-policy.md`.

## K200 WATCH

SWE-Pruner–style internal prune: **lab only** until LICENSE confirmed. If trialed later, measure **decide quality**, not token count alone. No install this wave.
