# Patch GenomeDiff (K155)

Operator spec from IdeaGene-Bench (arXiv **2607.08758**): successive
`decide()` / heuristic patches record **Inherited / Mutated / Lost / Novel**,
not “related poker paper.” Task co-location ≠ lineage.

Config helper: `examples/patch_genome_diff.py`.
HL brief template: `examples/cemini_hl_brief.py` (GenomeDiff section).
Backfill: `references/genome-diff-backfill-2026-07-14.md`.

## Required fields (every HL patch brief)

| Field | Meaning |
|-------|---------|
| **Parent mechanism** | Named heuristic/guard being extended (must already exist in tree) |
| **Delta** | `mutate` (change parent) or `novel` (insert new mechanism) |
| **Inherited** | What stays from the parent unchanged |
| **Mutated** | What changed on the parent path |
| **Lost** | What was deliberately dropped (and why) |
| **Novel** | New mechanisms with no parent link |
| **Verification** | Regression spot / sandbox check that the lineage claim holds |

## Compositional gate (P1)

Paper: local signals OK, joint consistency fails (~27% exact). Mirror in
preflight: **parent + delta + verification must agree** before ship.

`validate_genome_diff(record)` returns PASS only when:

1. `parent_mechanism` is non-empty
2. `delta` ∈ `{mutate, novel}`
3. At least one of Inherited / Mutated / Lost / Novel is non-empty
4. `verification` names a spot id, pytest path, or gate command
5. If `delta=mutate`: Mutated or Lost must be non-empty
6. If `delta=novel`: Novel must be non-empty

Advisory in HL loop — not a hard submit gate until operator opts in.

## Reject without driver link

Steals that only share “poker LLM / imperfect-info” ecology without a named
parent mechanism (YOLO-vs-DETR analogy) → **REJECT** for HL ship.

## Out of scope

- Running full IG-Exam against paid APIs as a daily ritual
- Vendoring IdeaGene code (LICENSE TBD — Watch)

## Related

- `briefs/2026-07-14_k155-ideagene-patch-lineage-steal.md`
- `prompts/cemini_hl_analyst_prompt.md`
- `references/message-dag-trace.md` (K163 logging shape)
