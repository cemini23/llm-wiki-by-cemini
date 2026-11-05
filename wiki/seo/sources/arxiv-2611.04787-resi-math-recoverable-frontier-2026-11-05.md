---
title: "ReSI-Math — failure does not mean inability"
type: source
tags: [source, arxiv, reasoning, rl, capability, search]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-05
updated: 2026-11-05
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | ReSI-Math: Exploring Recoverable Capability Frontiers for Efficient Reasoning Improvement |
| Authors | Yao Cui, Zhen Yang, Yuandong Wang, Yangfu Zhu, Tianyu Wo, Zhenzhou Shao (Capital Normal University, Tsinghua) |
| arXiv | 2611.04787 |
| Pages | 20 |
| Read status | skimmed (abstract) |

## Narrative

**A short claim with wide reach: when a model fails a problem, it may not lack the capability.**

They call the space between "fails on direct decoding" and "can be elicited by search" the **recoverable capability frontier** — a policy-dependent region where the answer is reachable through trajectory-level search but not through ordinary sampling.

### The method

**Self-Judge-guided evolutionary search** identifies recoverable failures under a fixed policy, then **frontier problems are selected adaptively** for sequential RLVR as the policy evolves. Recovered capabilities become data-efficient supervision.

### Why the reframing is the contribution

Most evaluation treats a single failed sample as a capability verdict. If the frontier is real and large, then **an evaluation that samples once is measuring decoding luck as much as ability**, and a training pipeline that only learns from successes is discarding the cases where the model was closest.

This bears directly on how this workspace reads benchmarks. A reported score is a decoding-and-sampling result, not a capability statement — and the same model with search may sit well above it.

### The measurement

On Qwen3-VL-8B, correct–incorrect trajectory crossover produced 272 verifiable problems. That number is the frontier made concrete: problems the model can solve, that it does not solve by default.

**Caveat.** Abstract only. The 272 is one model on one benchmark family; the frontier is explicitly policy-dependent.

## Snippets

> "Direct failure does not necessarily imply inability. Some reasoning failures can be recovered by exploring the model's own trajectories, exposing a recoverable capability frontier." [Source: arxiv-2611.04787 p.1]

## Dead Ends

- **Reading a single failed sample as a capability verdict.** Search may recover it.
