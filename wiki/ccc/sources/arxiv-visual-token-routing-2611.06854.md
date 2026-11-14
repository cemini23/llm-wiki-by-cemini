---
title: "Visual Token Routing — keep only the screenshot tokens the next action needs"
type: source
related:
  - concepts/visual-token-routing.md
  - concepts/context-engineering.md
  - concepts/computer-use-agent-harness.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Visual Token Routing: Learning to keep tokens that matter |
| Author | Pranjal Aggarwal, Sean Welleck (Carnegie Mellon University) |
| Type | arXiv preprint (cs.CV), 2611.06854 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.06854-visual-token-routing-learning-to-keep-tokens-tha.pdf` |
| Retrieved | 2026-11-10 |
| Pages | 18 |
| Read status | read |

## Narrative

Computer-use agents (CUAs) read screenshots. Each screenshot becomes thousands of visual tokens. The paper gives the scale: Qwen3.5 encodes one 1080p screenshot into about 2,000 visual tokens. A 100-step task with full history holds more than 200,000 visual tokens by the last step. One minute of 30 fps game play at 640x360 is about 400,000 visual tokens.

The authors observe that most visual tokens are irrelevant to the next action, or redundant with earlier frames. Static regions, taskbars, and empty document areas rarely change a click.

**Visual Token Routing (VTR)** trains a small spatio-temporal router. For each image region, the router reads the same region in the current and the previous K screenshots. It outputs a keep probability. A kept token is scaled by that probability, following mixture-of-experts practice. Dropped tokens leave the sequence entirely, so the language model never processes them.

Two training problems are solved together. Discrete keep/drop gates give no gradient, so kept tokens are scaled. And the right token budget differs per input, so the loss adapts weights instead of fixing a budget.

Results:

- 2,000 training steps.
- Matches full-resolution performance on OSWorld, CUA-World, and video game action prediction.
- Uses 2.5 to 5.8 times fewer visual tokens.
- Cuts inference cost up to 3.3 times and speeds prefill up to 2.9 times.
- Beats image downscaling and hand-written drop rules by up to 12.8 points on OSWorld.

The transferable idea is not the router. It is the framing: **a long-horizon agent should spend context on the parts of the observation that can change the next action.** The same test applies to text tool output in Claude Code sessions.

## Snippets

> "We observe that most of these visual tokens are either semantically irrelevant to the agent's next action or temporally redundant across screenshots." [Source: arxiv-2611.06854-visual-token-routing-learning-to-keep-tokens-tha.pdf p.1]

> "For instance, Qwen3.5 encodes a single 1080p screenshot into about 2,000 visual tokens, so an agent that keeps its full history on a 100-step task has over 200,000 visual tokens in its context by the final step." [Source: arxiv-2611.06854-visual-token-routing-learning-to-keep-tokens-tha.pdf p.1]
