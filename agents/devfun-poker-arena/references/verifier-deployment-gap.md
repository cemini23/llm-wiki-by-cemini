# Verifier–deployment gap (K198)

**arXiv:** [2607.24300](https://arxiv.org/abs/2607.24300) — self-authored
verification is unreliable  
**Brief:** `briefs/2026-07-28_k198-swap-regret-verifier-gap-steal.md`  
**Wiki:** `@concepts/verifier-deployment-gap.md`

## Steal

When the same agent authors both the **policy** and the **accept test**, unit
suites can stay green while live deployment fails. Same pattern as skill
regression tax and play-adequacy vs transition-accuracy.

## Arena ops rule

**Do not promote `decide()` / sandbox bundles on self-tests alone.**

Required external surfaces (already in tree):

| Gate | Path |
|------|------|
| Play / search fixtures | `references/play-adequacy-gates.md`, `tests/test_play_adequacy_spots.py` |
| Frozen HU yardsticks | `references/expert-yardstick-pool.md`, `config/hu_yardstick_pool.json` |
| League promotion rubric | `references/league-promotion-rubric.md` (advisory gaps) |
| HU sandbox gate script | `scripts/run_hu_sandbox_gate.sh` |

Self-authored pytest that only asserts “legal action / did not crash” is
**transition-class**, not play-adequate.

## Ties

- K196 skill regression tax — heuristics that self-grade are suspect
- K158 play-adequacy — rare pivotal spots need targeted fixtures
- K198 swap-regret notes — regret-loss cannot self-grade promotions

## Related

- `references/swap-regret-training-notes.md`
- `references/play-adequacy-gates.md`
- `references/skill-regression-tax.md` (if present) / wiki `@concepts/skill-regression-tax.md`
