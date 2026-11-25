---
title: "Scientific coding with LLMs — FEM-Bench and six self-verification failures"
type: source
related:
  - concepts/self-verification-failure-taxonomy.md
  - concepts/agent-verification-patterns.md
  - concepts/agent-completion-verification-gates.md
  - concepts/benchmark-maintenance-debt.md
  - concepts/generation-verification-gap-agent-artifacts.md
updated: 2026-11-22
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Scientific Coding with Large Language Models: Evidence from Finite Element Analysis |
| Author | Erfan Hamdi, Joel Shor, Emma Lejeune (Boston University; Allen Institute) |
| Type | arXiv paper (cs.SE), 2611.21176 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.21176-scientific-coding-with-large-language-models-evi.pdf` |
| Retrieved | 2026-11-22 |
| Pages | 28 |
| Read status | read |

## Narrative

The authors extend FEM-Bench to 17 finite element tasks in nonlinear mechanics and structural dynamics, then evaluate 15 models on implementation and test generation.

Single-pass numbers are strong but inconsistent. The best model succeeds in 87.1% of implementation trials. The leading implementer reaches 49.9% joint test success, while the leading tester reaches 82.6%. Rankings differ between the two tracks.

Six models are then run with two agentic harnesses that allow code execution and revision. Agentic execution solves some tasks that never passed in single pass, and improves consistency on others. It also causes regressions. Claude Opus 5 with SimpleAgent reaches 96.5% Pass@3 (at least one success in three) but only 77.1% Pass3 (all three succeed). No model–harness pair exceeds 78.8% Pass3.

The central contribution is a failure taxonomy from 249 failed agentic trajectories. Six categories appear. The most common are inadequate test coverage (73.1%) and reliance on generic consistency checks (70.3%). In 28.5% of cases the tests share an error with the implementation.

The fix the authors test is separation: a coder agent and a tester agent. This configuration reaches 97.6% Pass@3 and 88.8% Pass3, the best observed.

For Cemini the lesson is concrete. An agent that writes its own tests and then passes them has weak evidence. Independent verification, or at least a different agent for the test, is the difference between Pass@3 and Pass3.

## Snippets

> "To understand why agents submit incorrect code after passing their own checks, we analyze 249 failed agentic trajectories and identify six categories of self-verification failure." [Source: arxiv-2611.21176-scientific-coding-with-large-language-models-evi.pdf p.1]

> "In 28.5% of cases the tests share an error with the implementation." [Source: arxiv-2611.21176-scientific-coding-with-large-language-models-evi.pdf p.1]
