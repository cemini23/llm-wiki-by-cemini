---
title: "CANON — agent-assisted construction of canonical differential equations (2611.33100)"
type: source
related:
  - concepts/agent-completion-verification-gates.md
  - concepts/subagent-orchestration.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | CANON: Agent-Assisted Construction of Canonical Differential Equations for Feynman Integrals |
| Author | Dong-Shan Jian, Yuanche Liu, Yan-Qing Ma, Bo-Xuan Shi, Yu Wu, Zihao Wu, Yang Zhang (Peking University, USTC, LAPTh) |
| Type | arXiv preprint (high-energy physics, USTC-ICTS/PCFT-26-81) |
| ID | 2611.33100 |
| Location | research to be indexed/ccc/arxiv-2611.33100-canon-agent-assisted-construction-of-canonical-d.pdf |
| Retrieved | 2026-11-25 |
| File | `arxiv-2611.33100-canon-agent-assisted-construction-of-canonical-d.pdf` |
| Pages | 12 |
| Read status | read (abstract, intro) |

## Narrative

**Off-domain.** This is a high-energy physics paper. The subject is a canonical basis for multi-loop Feynman integrals. It is not about `/route` or coding harnesses.

The agent design is the transferable part. No single method for finding a canonical basis works for all cases. So the workflow is search, then verify, then retry.

- The agent picks a method and calls the matching tool. It revises the basis proposal or the differential-equation system.
- Independent programs verify the result. On failure, they ask the agent to retry.
- A dedicated state-management tool supports long-range basis search that needs several sub-agents.
- The architecture is modular, so the framework can extend.

The paper demonstrates two-loop and three-loop integral families.

**Why it matters to this wiki.** It is a clean pattern: the agent proposes, deterministic code decides. The verifier is not the agent and is not an LLM. This is the same shape as `@concepts/agent-completion-verification-gates.md`: a separate program owns the pass/fail decision. The sub-agent state tool also matches the workspace's own long-horizon orchestration problem. [TENTATIVE]
