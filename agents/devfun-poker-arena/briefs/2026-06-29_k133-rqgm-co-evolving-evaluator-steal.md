## Target

`agents/devfun-poker-arena/` — HL loop eval discipline + Researcher Round bundle harness.

## Summary

Steal **RQGM controlled utility evolution** (arXiv 2606.26294): treat private eval gates as **epoch-versioned** and co-evolve lightweight **agent-as-judge** signals with policy patches — complements K132 Fara tri-verifier and K129 CELEUS CIs.

## Body

### Epoch eval contract

| RQGM concept | Private implementation |
|--------------|------------------------|
| Fixed within-epoch utility | Regression weights + PvE panel rubric frozen per HL **eval epoch** ID |
| Utility update at boundary | Changelog entry when adding spots, judge prompts, or verifier weights |
| Co-evolved evaluator | Optional one-shot LLM judge on `reasoning_text` before full bundle dry-run |
| Adversarial epoch | If panel over-accepts AI bundles vs human baselines, add penalty term next epoch |

### P0 — harness addendum

1. Stamp `eval_epoch` in preflight JSON alongside git SHA.
2. After each major `decide()` refactor, audit whether regression corpus still separates good/bad bundles (Red Queen drift check).
3. Pair epoch reports with CELEUS-style agreement monitoring where judge variance matters.

### Pairing

| Layer | Role |
|-------|------|
| K133 RQGM (this) | Non-stationary eval + judge co-evolution |
| K132 Fara | Tri-verifier dimensions |
| K131 ToolBench-X | Hazard taxonomy |
| Pure-code `decide()` | Policy unchanged — eval evolves offline only |

### Out of scope

- RQGM recursive code self-edit on prod during live event
- Public TrueSkill metric manipulation
- Academic MOMDP / commutative-algebra rejects from same batch

## Sources

- [Source: arXiv:2606.26294 (retrieved 2026-06-29)]
- @wiki/sources/arxiv-2606.26294-red-queen-godel-machine-2026-06-29.md
- @wiki/sources/brief-k133-rqgm-evaluator-steals-2026-06-29.md
- @wiki/sources/arxiv-2606.20785-fara-computer-use-agents-2026-06-27.md
