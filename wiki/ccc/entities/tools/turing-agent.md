---
title: turing-agent — agentic formal-verification harness for mathematics
type: entity
related:
  - sources/arxiv-turing-agent-formal-verification-mathematics-2611.21299.md
  - concepts/formal-verification-faithfulness-gap.md
  - entities/tools/claude-code.md
  - entities/tools/openai-codex-cli.md
maturity: draft
updated: 2026-11-22
---

## Raw Concept

Entity page for the Turing Agent harness. Prompted by `@sources/arxiv-turing-agent-formal-verification-mathematics-2611.21299.md`.

## Narrative

- **Owner:** Agent Center, Shanghai AI Laboratory, with UESTC, HKU and SUFE.
- **Website:** https://wangqy031216-cloud.github.io/turing-agent
- **Scope:** end-to-end Lean formalisation of research-level mathematics. Theorem-formalisation agents and proof-formalisation agents, with structured proof decomposition, parallel verification, accumulated proof experience and selective semantic review.

### Reported results

On theoretical computer science tasks, about 57–62% faithful formalisation success on Formal TCS Bench, and 83% pass@1 on a TCS subset of RLMEval, using GLM-5.3 and DeepSeek-V4-Pro. The authors report beating Codex CLI and Claude Code as general-purpose baselines. [TENTATIVE] author-reported.

### Fit for Cemini

No adoption. The useful artifact is the faithfulness/validity/completeness split in `@concepts/formal-verification-faithfulness-gap.md`. Reference only.

[OPEN QUESTION 2026-11-22] No repository licence was checked. Run a Phase-0 audit before any use.
