---
title: K241 — self-fictitious-play MFG (MAFP family)
type: brief
tags: [brief, poker, mafp, k241]
created: 2026-08-18
updated: 2026-08-18
---

## Target

Poker Arena (`agents/devfun-poker-arena`). Researcher track. No live betting.

## Summary

Verdict: **real MAFP-family steal.** Self-fictitious-play updates the belief from the **player's own occupation measure**, not the population. For potential monotone ergodic MFG the dynamics are contractive; invariant law is within Wasserstein **√ε** of Nash (ε = belief-update rate). LQ example shows the rate is sharp. Effort: 20 min.

## Body

1. **When the opponent is a black box** (HU sandbox), you cannot observe the population. SFP says: treat your own occupation measure as the belief.
2. **Keep the belief-update rate small.** Error scales like √ε. Fast chasing of a noisy empirical measure is the failure mode.
3. This does **not** replace Shen et al. stance-entangled MAFP (2606.19308). It is a single-trajectory variant for when you only have your own path.
4. Do not drop into live tournaments. Researcher-track note only.

## Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Overfitting own history as "the field" | Medium | Small ε; compare vs MAFP stance play |
| Live-betting misuse | High | Researcher track only |

## Phasing

- **Phase 1:** note in Arena researcher brief. No code required this batch.
- Success: SFP cited next to MAFP; no live wire.

## Shelved

Folded into `references/mafp-fbsde-theory-shelf.md` (K170 + K157 + K167/K241 SFP). Dual-ID note: this is **Poker K241** (SFP / 2608.15258) — **not** CCC K241 (no raw LLM tabular prediction). Researcher-track literacy only; no live wire.

## Sources

- @sources/arxiv-2608.15258-self-fictitious-play-2026-08-18.md
- @concepts/multi-agent-fictitious-play-llm.md
- @sources/arxiv-mafp-fictitious-play-2606.19308-2026-06-20.md
