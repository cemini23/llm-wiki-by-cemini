---
title: K278 Harness Wave (Oct 2026)
type: concept
tags: [agents, harness, k278, ccc]
keywords: [k278, vista, coherence, rlm, durable-state, FILE]
related:
  - concepts/k277-harness-evolution-wave.md
  - sources/arxiv-2610.02200-vista-2026-10-02.md
  - sources/arxiv-2610.02036-global-coherence-2026-10-02.md
  - sources/newsletter-rss-latent-space-2026-10-02-rlm-zhang-2026-10-02.md
  - sources/newsletter-rss-latent-space-2026-10-02-pi-durable-2026-10-02.md
maturity: draft
created: 2026-10-02
updated: 2026-10-02
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k277-harness-evolution-wave.md
- @sources/arxiv-2610.02200-vista-2026-10-02.md
- @sources/arxiv-2610.02036-global-coherence-2026-10-02.md
- @sources/newsletter-rss-latent-space-2026-10-02-rlm-zhang-2026-10-02.md
- @sources/newsletter-rss-latent-space-2026-10-02-pi-durable-2026-10-02.md

## Raw Concept

K278 cluster hub. Dual-ID **OSINT K278**. Prior @concepts/k277-harness-evolution-wave.md.

## Narrative

This wave converges on one rule from four directions: **the harness owns state.** Zero clones. No skill install.

| Source | Contribution | Posture |
|--------|--------------|---------|
| 2610.02200 VISTA | A mechanical harness with visual memory and no trained model | Strongest result. No clone |
| 2610.02036 global coherence | Every agent locally right, team still wrong; a state problem | Read this first |
| RLM interview | Harness whose only tool is code; context offloaded to a file system | Opinion, not measurement |
| Pi Durable | Externalised state: crash checkpoints, hot-swap, shared sync | Tooling headline |

### Three findings worth acting on

1. **Visibility is not enforcement.** The coherence paper gave a team a live count of its remaining budget and the team still overspent in 4 of 5 runs. Commit enforcement took it to 0 of 5. A counter that an agent can ignore is not a gate.
2. **The harness can carry the whole gain.** VISTA changed nothing about the model. It added rendered observations plus addressable full-resolution memory, and took an open-weight model from 1.89 to 66.93 on ARC-AGI-3. The frontier model hit a perfect 100.00 relative human action efficiency using 7,302 actions against a human 17,135.
3. **Images can be cheaper than text.** On the same task, image observations used 30.7M tokens against 71.9M for text grids, at a similar score.

### One caution

The coherence paper's aliasing result is the sharpest single number in the wave. When the deciding event was visible, the model solved 40 of 40 tasks. Hidden, its accuracy was compatible with chance. **One restoring sentence brought it back to 40 of 40.** That is the third time this quarter that a small state fix beat a bigger model.

VISTA's authors admit the obvious confound: the models postdate the public benchmarks, so contamination cannot be ruled out.

**Cemini posture:** FILE and HITL only. Do not swap `/route`. No skill install. **0 product Integrate GO.**
