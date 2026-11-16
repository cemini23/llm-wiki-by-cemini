---
title: Socratic tutor as an agent skill
type: concept
maturity: draft
related:
  - sources/substack-rss-moontower-2026-11-15-moontower-336.md
updated: 2026-11-16
---

## Raw Concept

Question this page answers: what does a well-built tutoring prompt actually enforce?

From a Jane Street open-source `SKILL.md`, as summarised by Moontower #336 (2026-11-15).

## Narrative

The skill is a prompt contract with five enforced behaviours:

1. **Diagnostic first.** Open by probing what the learner already knows, then score each subskill from 0 to 5.
2. **One question at a time**, with the answer withheld.
3. **Progressive narrowing.** On a wrong answer, ask a narrower question rather than giving the answer, until the learner finds the gap themselves.
4. **Two correct demonstrations to advance**, one of them from cold recall.
5. **Scheduled review** of older material, interleaved without warning.

The pedagogical grounding is Math Academy's: generation effects (produce, do not recognise), reinforcement, and spaced repetition.

Why it is worth recording as a pattern rather than as a curiosity: it is a concrete example of an agent skill that constrains *interaction shape*, not just tone. The escalation rule and the double-proof promotion rule are the load-bearing parts; without them the tutor degrades into an answer dispenser.

[TENTATIVE] Summarised from a newsletter description of a third-party skill file. The file itself was not read here.

## Snippets

> "Levels only go up after you prove it twice, once from cold recall."
