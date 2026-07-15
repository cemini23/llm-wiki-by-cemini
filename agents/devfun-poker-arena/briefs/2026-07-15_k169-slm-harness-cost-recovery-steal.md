# K169 — SLM harness-adaptation cost recovery (devfun-poker-arena steal)

## Target

devfun-poker-arena — hand-decision agent cost/latency.

## Summary

K169 **steal-from** arXiv 2607.08938 (CMU) — a cheap open-weight SLM paired with a harness adapted to its specific failure modes (filtered tool set, fixed step-by-step plan, anti-loop guard) recovered ~90% of frontier-LLM decision quality at 4–8% of per-query cost on repetitive agentic tasks. Per-hand poker decisions are exactly the "low task diversity, high recurrence" profile the paper identifies as the sweet spot for this pattern (Spearman ρ = −0.96 between task diversity and adaptation payoff). Paired with a caution paper (arXiv 2607.12227, AI2/UW) on not over-crediting harness-tuning wins without a repeated-sampling control.

## Body

### Applicability check for poker arena

| Check | Pass |
|-------|------|
| Per-hand decision workflow is structurally repetitive (same decision tree shape, different cards/pot/opponent state) | ☐ |
| Ground-truth/solver check exists to validate a cheaper-model harness before trusting it in real hands | ☐ |
| Base model capability (if swapping to cheaper tier) benchmarks reasonably close to current tier — harnesses can't fix a fundamentally weaker model | ☐ |

### Concrete steal — five-axis failure diagnosis before any model downgrade

If considering a cheaper model for routine/low-stakes hand decisions: diagnose failures against the paper's five axes (tool-use, instruction-following, knowledge, long-context, planning) rather than reflexively reverting to the expensive model. E.g., a cheap model missing pot-odds knowledge is a **knowledge** failure (fix: externalize the pot-odds formula into the prompt/tool), not necessarily a **planning** failure (which harnesses can't fully offload).

### Caution — evaluation rigor before trusting a harness win

arXiv 2607.12227 (AI2/UW): harness-tuning gains measured only on the same task set used to tune them are unreliable — they found near-zero generalization to held-out tasks in a controlled test. Before adopting any cheap-model-plus-harness combo for real-money hands, validate against a **held-out** hand set (not the tuning set) and compare against a simple repeated-sampling baseline at the same compute budget — don't credit the harness for a gain that repeated sampling alone would produce.

### Wiki

- CCC concepts/failure-mode-harness-adaptation-mapping.md
- CCC concepts/harness-evolution-vs-test-time-scaling-baseline.md
  (plain paths — skill_audit does not resolve `@ccc-wiki/` aliases)

## Sources

- arXiv 2607.08938
- arXiv 2607.12227
