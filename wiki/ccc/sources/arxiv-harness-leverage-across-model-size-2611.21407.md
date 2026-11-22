---
title: "Harness leverage across model size — five local harnesses from 0.75B to 4.7B"
type: source
related:
  - concepts/harness-completion-gate-progress-effect.md
  - concepts/harness-as-eval-artifact.md
  - concepts/harness-evolution-vs-test-time-scaling-baseline.md
  - concepts/benchmark-maintenance-debt.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Harness Leverage Across Model Size: A Ladder of Five Local Agent Harnesses from 0.75B to 4.7B |
| Author | Hao Wang (USTB), Ting Huang (Honor Device Co.) |
| Type | arXiv paper (cs.AI), 2611.21407 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.21407-harness-leverage-across-model-size-a-ladder-of-f.pdf` |
| Retrieved | 2026-11-22 |
| Pages | 56 |
| Read status | read |

## Narrative

The paper crosses two axes that are usually held fixed: five shipped harnesses and four local open-weight models (0.75B to 4.7B), plus a 35.5B anchor. One deterministic checker scores all 360 ladder cells on 18 artifact-producing tasks.

Main result: the completion-controlling harness **Mingbird** has the highest mean at every model size. Of four pre-registered paired contrasts, two survive Holm correction, at 0.75B and 4.7B.

The more useful finding is the mechanism. The authors call the harness effect a **progress effect**: the harness decides whether a run leaves any declared artifact on disk. Of 357 usable cells, 127 leave none, and 85 of those exit normally. A scorer that reads exit status therefore credits work that was never written.

Disabling the six executable completion checks does **not** explain the gain. The mean moves by +0.080, +0.117, +0.003 and −0.004, and every interval includes zero. Removing one repeat-blocking rule alone costs 0.411 at 0.75B and leaves 8 of 18 tasks with no artifact.

The paper is explicit that four rungs cannot settle whether the harness effect grows or shrinks with model size. A floor arm shows a rise, a ceiling arm a decline, and a cross-family rung a peak.

For Cemini this is a direct lesson for `/route` and for any sweep that compares harnesses: score the artifact, not the exit code. A run that exits zero with nothing on disk is a failure. [TENTATIVE] single source for the specific counts.

## Snippets

> "The harness effect is a progress effect: it decides whether a run leaves anything on disk." [Source: arxiv-2611.21407-harness-leverage-across-model-size-a-ladder-of-f.pdf p.1]

> "Of 357 usable cells, 127 leave none of their declared artifacts and 85 of those exit normally, so a scorer that reads exit status credits work that was never written." [Source: arxiv-2611.21407-harness-leverage-across-model-size-a-ladder-of-f.pdf p.1]
