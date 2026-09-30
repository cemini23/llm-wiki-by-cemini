---
title: LLM-driven BT↔FSM conversion — behaviour model transforms (2026-09-30)
type: source
tags: [source, arxiv, game-ai, behavior-tree, fsm, harness]
keywords: [bt-fsm, loop-bt, depth-compression, behavior-model-conversion]
related:
  - concepts/game-ai-rl-augmentation-shelf.md
  - concepts/stronghold-2-ai-lords.md
  - concepts/rts-siege-ai-reference.md
  - entities/projects/castle-sim.md
  - sources/inbox-arxiv-reject-batch-2026-09-30.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2609.29228
maturity: validated
created: 2026-09-30
updated: 2026-09-30
---

## Raw Concept

**arXiv:2609.29228** — LLMDUCF, an LLM-driven unified conversion framework for bidirectional FSM↔BT transformation.

- FSM and behavior trees (BT) are widely used behaviour-modelling paradigms for autonomous systems. [CONFIRMED]
- Both are functionally equivalent and in principle inter-convertible. [CONFIRMED]
- Existing transforms break behavioural completeness, or explode model complexity. [CONFIRMED]
- Two mechanisms: a loop-execution BT structure (LEBT) so the LLM captures FSM loop structure and preserves completeness. [CONFIRMED]
- A depth-compression strategy with LLM prompts removes redundant control nodes and mitigates state explosion. [CONFIRMED]
- Differentiated hierarchical conversion rules cut the number of required sub-FSMs. [CONFIRMED]
- Simulation across autonomous decision-making scenarios shows accurate automated bidirectional conversion, plus better scalability and maintainability. [CONFIRMED]
- Stated target: consumer-grade autonomous systems — service robots, game agents, smart home devices. [CONFIRMED]
- Authors are at the National University of Defense Technology (NUDT). [CONFIRMED]
- Referenced repos: github.com/NUDTQI/PartoPrey-BT-RL, github.com/zhoupeng-0425/FSM2BT, github.com/ethz-asl/bt_fsm_comparison. [CONFIRMED]

## Narrative

### castle-sim / lord-AI relevance [CONFIRMED]

- The wiki plans a hand-coded lord director (FSM/BT/GOAP) with JSON-tunable weights, see @concepts/stronghold-2-ai-lords.md and @concepts/rts-siege-ai-reference.md.
- FSM↔BT conversion matters when refactoring lord scripts or porting Crusader `.aic`/AIV weight categories into a BT.
- Maintenance angle: fewer sub-FSMs and redundant nodes mean a smaller director.
- Cross-link @concepts/game-ai-rl-augmentation-shelf.md and @entities/projects/castle-sim.md.

### Phase-0 / adoption [CONFIRMED]

- Phase-0 audit 2026-09-30: `github.com/zhoupeng-0425/FSM2BT` and `github.com/NUDTQI/PartoPrey-BT-RL` both have **no LICENSE file** and no licence badge → **NO-GO clone**.
- Batch verdict: **STEAL-FROM** — reuse the loop-BT and depth-compression ideas in the castle-sim director; do not vendor the repos.
- `github.com/ethz-asl/bt_fsm_comparison` is cited as prior art only.

## Dead Ends

- Generating lord AI end-to-end with an LLM instead of converting an authored model.
- Assuming conversion preserves behaviour without a completeness check.
- Treating the paper's game-AI scenario as a shipped system; it is a simulation test. [TENTATIVE]
