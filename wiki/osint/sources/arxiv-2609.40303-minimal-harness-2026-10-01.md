---
title: "How much of a harness does a strong agent need? (2609.40303)"
type: source
tags: [source, k277, agents, harness, ablation]
keywords: [k277, minimal-harness, mle-bench, best-of-n, FILE]
related:
  - concepts/k277-harness-evolution-wave.md
maturity: draft
created: 2026-10-01
updated: 2026-10-01
read_status: skimmed
---

## Relations

- @concepts/k277-harness-evolution-wave.md

## Raw Concept

| File | `arxiv-2609.40303-how-much-of-a-harness-does-a-strong-agent-need-f.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.40303-how-much-of-a-harness-does-a-strong-agent-need-f.pdf` |
| Archive | egress-fi 2026-10-01 |
| Retrieved | 2026-10-01 |
| Dual-ID | **OSINT K277** |
| sha256 | `acae1547ac84f2977568dbae7ac79fb04fff239924a16e4c0f74fd2752f7f1e9` |
| arXiv | 2609.40303 |
| Authors | Kirill Brilliantov, Alejandro Hernandez-Cano, Emmanuel Abbe (EPFL; Apple) |

## Narrative

The question is how much scaffolding a strong model actually needs. The authors reimplement four intervention families in one codebase: execution environment, search, autonomy, and multi-agent orchestration. They then run matched ablations on MLE-bench and NatureBench.

The endpoint harness, called Malena, is a single long-running coding-agent session with minimal tools.

The headline result: **the coding environment was the single largest measured effect, and no further intervention was statistically significant.** Malena matched or beat four released harnesses across 17 harness-and-backbone pairs on 30 MLE-bench tasks. With one backbone it earned a medal on 62.5% of competitions against 47.1% for the best external harness.

One number is useful for verifier design. Best-of-N had the largest gap between self-selection and an oracle, at 6.832 percentage points. That is the same gap class as the K276 trace finding: the model's own choice of its best answer is not the best answer.

The authors admit the cost is real. Malena's modeled cost was about 6.2 times a leaner baseline. They also flag that MLE-bench has known task-preparation issues and is a plausible contamination target, and that some confidence intervals are too wide for strong effect-size claims.

No code URL found. No clone. Do not swap `/route`. FILE only.
