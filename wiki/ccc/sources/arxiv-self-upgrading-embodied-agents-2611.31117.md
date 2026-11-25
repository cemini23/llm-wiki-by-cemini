---
title: "Self-Upgrading Embodied Agents — weight edits between tasks (2611.31117)"
type: source
related:
  - concepts/continual-harness-online-self-improvement.md
  - concepts/agentic-robotics-harness.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Self-Upgrading Embodied Agents |
| Author | Jiajun Fan, Neil He, Qinglong Zheng et al. (UIUC, CMU, Brown, Stanford, Northeastern, Harvard, UW, Rutgers, Princeton, UMich, Columbia, NYU, UC Berkeley, Yale) |
| Type | arXiv preprint (cs.AI) |
| ID | 2611.31117v1, 24 Nov 2026. Dated 21 Nov 2026 |
| Location | research to be indexed/ccc/arxiv-2611.31117-self-upgrading-embodied-agents.pdf |
| Retrieved | 2026-11-25 |
| File | `arxiv-2611.31117-self-upgrading-embodied-agents.pdf` |
| Pages | unknown (read p.1 only) |
| Read status | read (abstract, intro) |

## Narrative

**Off-domain.** This is a robotics-embodied paper. It does not address `/route`, Claude Code, or MCP.

The claim is weight-space self-improvement with no training loop. A 27B embodied agent works in a household environment by day. At night it reads its own record. It finds that many steps waste the token limit before any action. It traces the habit to one direction in its hidden states. It rewrites one tensor of its own weights.

The agent also acts as its own examiner. It tests each change against its unchanged self on practice tasks. It keeps only changes that hold. Reported gain: more tasks completed, in fewer steps, with fewer wasted tokens, over thousands of held-out episodes with 48 fresh seeds per task.

The authors report the improvement is multi-round, stable, and continual, without collapse. Of four sizes in the family, only the 27B model does this.

**Why it matters to this wiki.** It is a different lever from harness editing. This workspace improves agents by editing prompts, skills, and tool loops. This paper improves the weights, between tasks, without gradient updates. It is a data point for the argument that harness edits and weight edits are separate paths, not substitutes. Treat as single-source and self-reported. [TENTATIVE]
