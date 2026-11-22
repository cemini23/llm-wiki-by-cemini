---
title: "Turing Agent — agentic formal verification for mathematical research"
type: source
related:
  - concepts/formal-verification-faithfulness-gap.md
  - entities/tools/turing-agent.md
  - entities/tools/claude-code.md
  - entities/tools/openai-codex-cli.md
  - sources/newsletter-rss-latent-space-2026-11-20-the-war-against-slop-and-an-emerging-weapon-to-f.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Turing Agent: Agentic Formal Verification for Mathematical Research |
| Author | Yang Chen, Qianyi Wang et al. (Shanghai AI Lab, UESTC, HKU, SUFE) |
| Type | arXiv paper (cs.AI), 2611.21299 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.21299-turing-agent-agentic-formal-verification-for-mat.pdf` |
| Retrieved | 2026-11-22 |
| Pages | 31 |
| Read status | read |

## Narrative

Turing Agent is a harness for end-to-end Lean formalisation of research-level mathematics. It has a two-scale architecture: theorem-formalisation agents and proof-formalisation agents, with structured proof decomposition, parallel verification, accumulated proof experience, and selective semantic review.

The paper names three failure conditions that any formal-verification harness must address:

- **Faithfulness** — the Lean statement may not capture the natural-language claim.
- **Validity** — syntax, type or elaboration failures prevent a proof term.
- **Completeness** — unresolved gaps such as `sorry` bypass proof obligations.

Evaluation is on theoretical computer science with collaborating TCS researchers. Against direct generation and general-purpose coding harnesses, including Codex CLI and Claude Code, Turing Agent reports about 57–62% faithful formalisation success on Formal TCS Bench and 83% overall pass@1 on a TCS-focused RLMEval subset, using GLM-5.3 and DeepSeek-V4-Pro. The DeepSeek-backed configuration completes three previously unresolved TCS tasks from OpenAI's October 2026 collection; one needed about a hundred verified auxiliary claims. [TENTATIVE] single source; results are author-reported.

The valuable distinction for Cemini is faithfulness versus validity. A harness can produce a proof that the kernel accepts and that proves the wrong theorem. Tooling that checks only compilation does not check meaning.

## Snippets

> "The formal statement must preserve the original claim (faithfulness), the code must pass Lean's syntax and type checks (validity), and the proof must discharge all proof obligations (completeness)." [Source: arxiv-2611.21299-turing-agent-agentic-formal-verification-for-mat.pdf p.2]
