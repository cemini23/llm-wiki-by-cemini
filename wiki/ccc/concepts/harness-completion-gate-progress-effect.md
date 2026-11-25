---
title: "Harness completion gate — the harness effect is a progress effect"
type: concept
related:
  - sources/arxiv-harness-leverage-across-model-size-2611.21407.md
  - concepts/harness-as-eval-artifact.md
  - concepts/agent-completion-verification-gates.md
  - concepts/harness-evolution-vs-test-time-scaling-baseline.md
  - concepts/benchmark-maintenance-debt.md
updated: 2026-11-22
maturity: draft
---

## Raw Concept

Question this page answers: when a harness beats another harness, what is it actually doing?

Synthesised from one source: `@sources/arxiv-harness-leverage-across-model-size-2611.21407.md` (2611.21407).

## Narrative

A five-harness by five-model ladder study isolates the mechanism behind harness wins. The finding is blunt: the harness effect is a **progress effect**. The harness decides whether a run leaves a declared artifact on disk.

The numbers carry the claim. Of 357 usable cells, 127 left no declared artifact, and 85 of those exited normally. A scorer that reads exit status credits work that was never written.

This also rules out the obvious explanation. Disabling all six executable completion checks does not reproduce the gain. The mean moves by +0.080, +0.117, +0.003 and −0.004 across four models, and every interval includes zero. What does matter is a repeat-blocking rule: remove one, and 8 of 18 tasks produce no artifact at 0.75B, at a cost of 0.411.

### Operating rules

1. **Score the artifact, not the exit code.** A zero exit with no output is a failure.
2. **Count empty runs explicitly.** Report them beside the score, or they vanish into the mean.
3. **Check the gate, not the checks.** A stack of validators can be inert; what counts is whether the run is allowed to end without output.

For Cemini the rule applies to every `run_*` script and to agent turns. A session that ends with "done" and no diff, no file and no log has not done the work.

Caveat: this is one source with pre-registered contrasts, and only two of four survive Holm correction. The mechanism claim is stronger than the ranking claim. [TENTATIVE]

## Snippets

> "The harness effect is a progress effect: it decides whether a run leaves anything on disk." [Source: arxiv-2611.21407-harness-leverage-across-model-size-a-ladder-of-f.pdf p.1]

> "Of 357 usable cells, 127 leave none of their declared artifacts and 85 of those exit normally, so a scorer that reads exit status credits work that was never written." [Source: arxiv-2611.21407-harness-leverage-across-model-size-a-ladder-of-f.pdf p.1]
