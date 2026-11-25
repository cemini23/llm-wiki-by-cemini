---
title: "Evidence-grounded debate stopping — stop when the belief stops moving"
type: concept
related:
  - sources/arxiv-beyond-self-critique-epistemic-convergence-2611.27839.md
  - sources/arxiv-pieq-provenance-isolated-epistemic-quorums-2611.32032.md
  - concepts/agent-completion-verification-gates.md
  - concepts/execution-bound-evidence-certification.md
  - entities/patterns/glasswing-deliberate-disagreement.md
updated: 2026-11-25
---

## Raw Concept

Question this page answers: how many rounds should a multi-agent debate run, and what makes the answer credible? Synthesised from `@sources/arxiv-beyond-self-critique-epistemic-convergence-2611.27839.md` (2611.27839).

## Narrative

Fixed round counts are the common choice and the common defect. Three rounds is either too few or too many. Too few stops before evidence settles. Too many burns inference after convergence.

**Belief-Delta (dΔB) replaces the count.** Measure how much the agents' support for each claim changed in the last round. Stop when the change falls below a threshold. In the paper this cut over-iteration to 0.0%, against 62.5% for a fixed three rounds, and cut LLM calls 2.4 times.

Two supporting choices:

- **Asymmetric roles.** An Advocate, a Skeptic, and an Arbitrator with opposing directives produce lower role similarity (0.852 against 0.918) and surface more contested claims (22.0% against 15.4%). Homogeneous roles in debate reproduce the same blind spots.
- **Verbatim evidence anchoring.** Each supported claim is tied to a quoted snippet. An independent NLI classifier audits the tie.

**The honest result.** Anchoring did not cut hallucination: 21.7% against 25.9% for a self-refine critic, not significant (p = 0.61). What it bought was auditability. Each claim now has a checkable pointer.

**Reading rule.** Separate "did the debate reach a stable conclusion" from "is the conclusion true". The stopping rule answers the first. Only the evidence anchor, and a human or deterministic check, touch the second. A debate that agrees and stops is not a verified result.

**Status.** One paper, one base model (DeepSeek-R1-32B), 200 runs on 40 hypotheses. [TENTATIVE]
