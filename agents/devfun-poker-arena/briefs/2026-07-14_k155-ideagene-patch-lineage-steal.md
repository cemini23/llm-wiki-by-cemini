---
title: K155 — IdeaGene patch lineage (poker sandbox)
type: brief
target: Poker Arena
created: 2026-07-14
updated: 2026-07-14
---

## Target

`agents/devfun-poker-arena/` — HL analyst loop / Researcher Round HU sandbox.

## Summary

Steal **GenomeDiff** thinking from IdeaGene-Bench (arXiv 2607.08758): successive `decide()` / heuristic patches should record which mechanisms were **Inherited / Mutated / Lost / Novel**, not just “related poker paper.” Task co-location ≠ lineage.

**Shipped (2026-07-14):** GenomeDiff fields in HL brief + analyst prompt; compositional gate helper; backfill of last 3 shipped patches. Advisory only — no hard submit gate. IdeaGene code remains Watch (LICENSE TBD).

## Body

### P0 — patch GenomeDiff log

For each HL patch brief, require:

1. **Parent mechanism** — named heuristic or guard being extended
2. **Delta** — what changed (mutate vs novel insert)
3. **Lost** — what was deliberately dropped (and why)
4. **Verification** — regression spot / sandbox check that the lineage claim holds

Reject steals that only share “poker LLM / imperfect-info” ecology without a driver mechanism link (YOLO-vs-DETR analogy from the paper).

### P1 — compositional gate

Paper: local signals OK, joint consistency fails (~27% exact). Mirror in preflight: parent + delta + regression must agree before ship.

### Out of scope

- Running full IG-Exam against paid APIs as a daily ritual
- Contravariance NeuroAI (2607.08561)
- Vendoring IdeaGene code into arena package while LICENSE = TBD

### Operator checklist

- [x] Add GenomeDiff fields to next HL patch template
- [x] One backfill: last 3 shipped patches → Inherited/Mutated/Lost table
- [ ] Revisit when VisionXLab adds SPDX

## Shipped

| Artifact | Notes |
|----------|-------|
| `config/hu_patch_genome_diff.json` | Schema + advisory gate knobs |
| `examples/patch_genome_diff.py` | `validate_genome_diff` + markdown table |
| `examples/cemini_hl_brief.py` | GenomeDiff section in generated briefs |
| `prompts/cemini_hl_analyst_prompt.md` | GenomeDiff in discipline + deliverables |
| `references/patch-genome-diff.md` | Operator spec |
| `references/genome-diff-backfill-2026-07-14.md` | S1 ladder / K150 / K151 lineage table |
| `tests/test_k155_genome_diff.py` | Gate unit tests |

```bash
uv run pytest tests/test_k155_genome_diff.py -q
```

## Sources

- arXiv [2607.08758](https://arxiv.org/abs/2607.08758)
- `references/patch-genome-diff.md`
- `references/genome-diff-backfill-2026-07-14.md`
- gambling-wiki source (sibling): `arxiv-2607.08758-ideas-have-genomes-ig-bench-2026-07-14.md`
