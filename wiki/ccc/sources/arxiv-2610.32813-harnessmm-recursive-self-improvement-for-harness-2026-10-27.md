---
title: "HarnessMM: Recursive Self-Improvement for Harness Token Efficiency"
type: source
tags: [source, arxiv, harness-efficiency, token-cost]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | HarnessMM: Recursive Self-Improvement for Harness Token Efficiency |
| Authors | Yuhua Jiang, Chang Xu, Feifei Gao, Li Zhao (Tsinghua University; Microsoft Research Asia) |
| arXiv | 2610.32813 |
| File | `arxiv-2610.32813-harnessmm-recursive-self-improvement-for-harness.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.32813 |
| Read status | skimmed (abstract + intro) |

## Narrative

Agent harnesses call the model again after every tool result, even when an earlier call already settled the next action. This wastes tokens.

**HarnessMM** ("Harness Minus Minus") reuses resolved decisions instead of re-reasoning. Four parts:

- **Executable Decision Graphs** store exact actions, literal arguments, causal dependencies, and public guards.
- **Guarded Decision Reuse** replays a stored decision when the observed receipt matches its guard.
- **Certified Callback Substitution** runs the decision through the native interface and records removal of the slow callback.
- **Recursive self-improvement (RSI)** refines harness configurations from training feedback, with a validation split choosing what ships.

The actor weights stay fixed. New semantic decisions, unsupported evidence, or selector abstention call the original model again.

Results:

- On HumanEval with Codex, success holds at 90.82% while tokens per task fall from 66.72k to 47.02k — a 29.54% saving.
- On the DeepSeek harness, success rises from 71.43% to 85.71% while tokens per task fall from 96.28k to 11.62k — an 87.93% saving.
- An MBPP ablation measures 26.91% lower cost than single-use graphs and 19.52% lower than retained callbacks.

**Why it matters.** Most agent cost is repeated reasoning over identical situations. Caching the decision, guarded by the observed state, is a cheap saving. The risk is real too: a stale guard that fires on a changed environment would replay a wrong action. The paper's answer is to abstain when the guard does not match.

## Snippets

> "A controller at the model–tool boundary reuses resolved decisions to replace later reasoning callbacks while actor weights remain fixed." [Source: `arxiv-2610.32813-harnessmm-recursive-self-improvement-for-harness.pdf` p.1 (arXiv 2610.32813), retrieved 2026-10-27]
