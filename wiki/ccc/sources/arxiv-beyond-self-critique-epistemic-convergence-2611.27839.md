---
title: "Beyond Self-Critique — epistemic convergence control for multi-agent verification (2611.27839)"
type: source
related:
  - concepts/evidence-grounded-debate-stopping.md
  - concepts/agent-completion-verification-gates.md
  - entities/patterns/glasswing-deliberate-disagreement.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Beyond Self-Critique: Epistemic Convergence Control for Multi-Agent Research Verification |
| Author | Chrisantus Eze (Oklahoma State University) |
| Type | arXiv preprint (cs.AI) |
| ID | 2611.27839v1, 20 Nov 2026 |
| Location | research to be indexed/ccc/arxiv-2611.27839-beyond-self-critique-epistemic-convergence-contr.pdf |
| Retrieved | 2026-11-25 |
| File | `arxiv-2611.27839-beyond-self-critique-epistemic-convergence-contr.pdf` |
| Pages | unknown (read p.1 only) |
| Read status | read (abstract, intro) |

## Narrative

Multi-agent debate often runs agents from the same base model. The agents then share latent representations, so self-critique bias is structural. A fixed iteration count makes it worse. The debate stops before evidence settles, or it keeps running after convergence.

The paper presents **VerifyAgent**, a verification framework with three changes.

**1. Asymmetric roles.** An Advocate, a Skeptic, and an Arbitrator carry opposing epistemic directives. Role-embedding similarity drops to 0.852, against 0.918 for symmetric multi-agent debate (p = 5.82e-8). The debate surfaces more contested claims: 22.0% against 15.4%.

**2. Belief-Delta convergence.** A stopping rule based on measured change in belief replaces a fixed round count. Over-iteration is 0.0%, against 62.5% for Fixed-3. LLM calls fall 2.4 times.

**3. Verbatim evidence anchoring.** Each supported claim is tied to a literature snippet, and an independent NLI classifier audits the tie. The hallucination rate is 21.7%, against 25.9% for a Self-Refine critic (p = 0.61). The authors describe this as comparable, not better. The gain is auditable grounding, not a lower hallucination rate.

The evaluation covers 200 runs on 40 research hypotheses with DeepSeek-R1-32B.

**Why it matters.** The cost saving comes from the stopping rule, not the debate. A fixed round count is the defect. The second finding is honest: evidence anchoring did not reduce hallucination. It made the support checkable. That distinction matters for any verification gate in this workspace.

One paper, one model. [TENTATIVE]

## Snippets

> "Static fixed-iteration protocols compound this by either halting prematurely before evidence stabilizes or wasting inference compute after convergence." [Source: `arxiv-2611.27839-beyond-self-critique-epistemic-convergence-contr.pdf` p.1, retrieved 2026-11-25]
