---
title: "Latent Space — Alex Zhang on recursive language models (2026-10-02)"
type: source
tags: [source, k278, agents, harness, tooling]
keywords: [k278, rlm, harness, subagent, no-route-swap]
related:
  - concepts/k278-harness-wave.md
maturity: draft
created: 2026-10-02
updated: 2026-10-02
read_status: skimmed
---

## Relations

- @concepts/k278-harness-wave.md

## Raw Concept

| File | `newsletter-rss-latent-space-2026-10-02-academia-is-for-ambition-alex-zhang-mit.md` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-latent-space-2026-10-02-academia-is-for-ambition-alex-zhang-mit.md` |
| Archive | egress-fi 2026-10-02 |
| URL | https://www.latent.space/p/rlm |
| Retrieved | 2026-10-02 |
| sha256 | `4161291241685b09436e308cab482147f2ee101f492fd26f54a32fde09e8f74b` |
| Dual-ID | **OSINT K278** |

## Narrative

A long interview with an MIT PhD student, Alex Zhang, who worked in a GPU-focused community and helped create a kernel benchmark. The technical core is recursive language models.

An RLM is a harness whose **only tool is code**. Context is offloaded to a file system, and the model can call itself as a subagent. The argument is that most harnesses are structurally the same, and that a harness acts as a compositional generaliser.

Numbers quoted in the interview:

| Claim | Figure |
|-------|--------|
| RLM trained on short tasks, generalising to longer | 8x to 30x longer |
| An agent run described | 10,000 agents over 88 hours, 130B output tokens |
| Equivalent public pricing for that run | about $40M |
| Kernel improvement quoted | could make two models about 80% cheaper |
| A benchmark saturated | in under a year |

Two claims are the interviewee's own framing, not measurements: that most harnesses are structurally the same, and that harnesses are compositional generalisers. Treat them as opinion.

The structural claim is worth testing against this wave. VISTA is a harness with visual memory and no trained model. The coherence paper argues the harness owns state. Both fit the "portable harness" thesis, which is why the interview sits in this hub.

It does not change `/route`. **Do not swap `/route`.** No level to arm. FILE only.
