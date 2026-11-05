---
title: "Subconscious — speculative decoding is not behaviour-neutral for long-horizon agents"
type: source
tags: [source, arxiv, agents, speculative-decoding, reasoning, long-horizon]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-05
updated: 2026-11-05
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Subconscious: Adversarial Speculative Reasoning Improves Long Horizon Agents |
| Authors | Hongyin Luo, Wei Fang, Lijie Yang, Owen Stepan, Daniel Suit, Jeff Krapf, Dana Wensberg, Jack O'Brien (Subconscious Systems, MIT, Princeton, Northeastern) |
| arXiv | 2611.05345 |
| Pages | 12 |
| Read status | skimmed (abstract) |

## Narrative

**The claim that matters is a correction to an assumption almost everyone holds.**

Speculative decoding has been treated as a pure **systems optimisation**: it speeds up decoding without changing model behaviour. Under that view, work on better draft models has optimised one thing — **acceptance rate**.

The authors argue this stops being true for **long-horizon agent reasoning**. Measuring frontier open-weight models on complex agentic tasks across different speculative approaches, they find:

- **numerical noise grows within verification windows**;
- draft acceptance results in the thinking process **can change the output distribution after about 30 steps**;
- which means it **noticeably influences reasoning accuracy in random directions**.

### Why that is a serious result

If a decoding optimisation shifts a long agent trajectory in an arbitrary direction, then it is a **variance source, not a speedup**. Two runs of the same agent on the same task with different speculative settings are not the same experiment, and any benchmark comparison between them is confounded.

The practical consequence for this estate: **speculative decoding settings belong in the reproducibility record**, next to the model id and temperature. A result produced with one setting does not transfer to another.

### The constructive half

They then improve reasoning by **controlling that noise** rather than eliminating it — the "adversarial speculative reasoning" of the title. The mechanism is not in the abstract.

**Caveat.** Abstract only. No accuracy figures, and the effect size is unknown.

## Snippets

> "The draft acceptance results of the thinking process can change the output distribution of the model after 30 steps, thus noticeably influencing the reasoning accuracy of long-horizon agents in random directions." [Source: arxiv-2611.05345 p.1]

## Dead Ends

- **Assuming a decoding speedup is behaviour-neutral.** It is not, past roughly 30 steps.
