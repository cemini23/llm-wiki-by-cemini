---
title: "karpathy/autoresearch — keep-or-revert agent loop (MIT, needs one NVIDIA GPU)"
type: entity
tags: [tool, agents, autoresearch, hyperparameter, ceminidfs, overfitting]
keywords: [autoresearch, karpathy, program.md, val_bpb, keep or revert, hill climbing, ceminidfs, xsp]
related:
  - sources/eval-multi-wiki-link-revenue-v10.10-batch-a-2026-11-01.md
  - concepts/autoresearch-loop-pattern.md
  - entities/tools/atlas-gic-autoresearch.md
maturity: draft
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

Surfaced by @sources/eval-multi-wiki-link-revenue-v10.10-batch-a-2026-11-01.md, URL 5, **Extract** tier. Routed to CeminiDFS, Collectibles, and xsp-killer.

The question this page answers: **how do you let an agent tune parameters overnight without letting it fool itself?**

## Narrative

### What it is

A public repository, 99.0k stars, **MIT**. An agent runs ML experiments unattended over a small LLM training setup modelled on nanochat.

Three files, and the split is the whole idea:

| File | Who edits it |
|------|--------------|
| `prepare.py` | Nobody. Fixed setup and utilities. |
| `train.py` | **The agent.** |
| `program.md` | **The human.** The agent's instructions. |

The human tunes `program.md`, not the Python. The default `program.md` is intentionally a bare baseline.

### The loop contract

1. The agent proposes a change to `train.py`.
2. A training run executes with a **fixed five-minute wall-clock budget**.
3. The metric is `val_bpb` — validation bits per byte. Lower is better.
4. If the metric improves, keep the change. If not, revert it.

The fixed budget is what makes runs comparable across architectural changes. A change that is slower can still win, because the budget is time, not steps.

### Phase-0, 2026-11-01

| Question | Finding |
|----------|---------|
| Does it exist? | **Yes.** 99.0k stars, 13.7k forks, **MIT**. |
| Runtime requirement | **One NVIDIA GPU** (tested on H100), Python 3.10+, `uv`. |
| Startup | Run `prepare.py` once. Test with `train.py`. |
| Operation | Launch an agent — Claude or Codex — in the repository **with permissions disabled**, and point it at `program.md`. |

**The blocker.** The laptop is Apple Silicon. This harness needs an NVIDIA GPU. The report routed it to three projects without noting that.

**What transfers.** The *contract* — fixed budget, one comparable metric, keep-or-revert, human owns the instruction file, agent owns one file — is hardware-independent. It is the same shape as @concepts/autoresearch-loop-pattern.md and the atlas-gic variant in @entities/tools/atlas-gic-autoresearch.md.

### Applying the contract without the harness

The transferable decision, per target:

| Target | Fixed budget | Comparable metric | Keep rule |
|--------|--------------|-------------------|-----------|
| CeminiDFS | one slate set, fixed projection pipeline | contest ROI on held-out slates | keep only if out-of-sample ROI improves |
| Collectibles | one grading batch | realised spread, raw vs graded | keep only if the cutoff improves on held-out comps |
| xsp-killer | one walk-forward window | out-of-sample Sharpe or drawdown | keep only if the held-out window improves |

The one rule that must not be dropped: **the evaluation must be out-of-sample.** The report names in-sample overfitting as the principal risk, and it is right. An agent that mutates against a static validation set will hill-climb the validation set.

### Status

Extract, **pattern only**. The harness does not run on this hardware.

## Snippets

> "AI agents running research on single-GPU nanochat training automatically" — repository description [fetched 2026-11-01]

> "Rather than editing Python directly, the human tunes `program.md`, which contains the agent's instructions." [README, fetched 2026-11-01]

> "Every run uses a five-minute wall-clock budget. The metric is val_bpb (validation bits per byte), so lower is better and results stay comparable across architectural changes." [README, fetched 2026-11-01]

> "To run it, launch an agent such as Claude or Codex in the repo with permissions disabled, then point it to `program.md`." [README, fetched 2026-11-01]

## Dead Ends

- **Running the harness on the laptop.** It requires an NVIDIA GPU. Only the loop contract transfers.
- **Running the loop against a static validation set.** That is in-sample overfitting with extra steps. The holdout must be out-of-sample.
- **Letting the agent edit the instruction file.** The human owns `program.md`. That separation is the control.
