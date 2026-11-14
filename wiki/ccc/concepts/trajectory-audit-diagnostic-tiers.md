---
title: "Trajectory audit diagnostic tiers — six questions an auditor must answer"
type: concept
related:
  - sources/arxiv-rea-bench-responsible-agent-auditing-2611.16493.md
  - concepts/trajectory-driven-safety-harness-evolution.md
  - concepts/agent-trace-tampering-audit-gap.md
  - concepts/tracekit-tamper-evident-agent-audit.md
updated: 2026-11-14
---

## Raw Concept

What question does this page answer: when an agent reviews another agent's execution trajectory, what makes the review hard, and how should we measure it? Source: ReA-Bench (2611.16493).

## Narrative

A trajectory audit has more than one failure mode. A single recall score mixes them. ReA-Bench separates six tiers by what the auditor needs:

| Tier | The auditor needs | Fails when |
|------|-------------------|------------|
| L1 Internal knowledge | Know the harm of an action and its target | The model lacks the security knowledge |
| L2 Contradictions | Compare distant steps | A later step contradicts an earlier instruction |
| L3 Evidence dilution | Find a needle in a long trajectory | The evidence is buried in huge tool output |
| L4 Provenance and logic | Check that cited sources support the claim | The conclusion outruns the evidence |
| L5 Indirect steering | Notice that the task was steered | The risk arrives through the task text |
| L6 Missing information | Obtain rules or runtime state | The trajectory never recorded what matters |

Three design lessons carry beyond the paper.

**Report by tier, not by risk type.** Risk categories do not explain why an auditor fails. The tier does, because it names the missing capability: knowledge, reading, verification, or access.

**Score hard benign cases.** Legitimate actions can look risky. ReA-Bench includes benign trajectories that pass DRC-like checks and satisfy authorisation. An auditor that flags them has learned to pattern-match, not to judge.

**Separate recall from false positives.** For post-hoc review, high recall justifies cost. For a runtime blocker, false positives interrupt real work. The paper shows the trade directly: the global-summary method raises Grok-low recall from 69.6% to 87.5% and its false-positive rate from 8.5% to 13.6%.

**Shortening is not a fix.** When the same trajectory was shortened, 87.1%–89.2% of judgements stayed where they were. Some errors belong to reading, not to context length. This limits the value of a pure compaction fix on a review lane.

For Cemini this maps to the audited work in `@concepts/bounded-authority-auditable-trajectories.md`: say which tier a review covers, and keep a benign control set beside the risky cases.

## Snippets

> "it does not show which risks are missed, or whether higher recall comes at the cost of more false positives on legitimate behavior" [Source: arxiv-2611.16493-rea-bench-benchmarking-responsible-agent-auditin.pdf p.1]
