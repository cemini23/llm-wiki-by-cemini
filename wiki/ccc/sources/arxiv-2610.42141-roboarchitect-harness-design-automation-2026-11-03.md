---
title: "RoboArchitect — automating harness design around a frozen policy"
type: source
tags: [source, arxiv, agents, harness, robotics, persistent-memory]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory |
| Authors | Shengguang Wu, Suning Huang, Cherie Ho, Ria Doshi, Hao Zhu, Serena Yeung-Levy (Stanford) |
| arXiv | 2610.42141 |
| Pages | 21 |
| Read status | skimmed (abstract) |

## Narrative

A frozen robot policy performs far better inside a **harness** — control code that decides when to query the policy, consult a vision tool, or command the arm directly. Today those harnesses are hand-built and redesigned per robot and per benchmark.

RoboArchitect automates the harness. A **coding model observes rollouts, diagnoses failures, and rewrites the harness** around a frozen policy. No model weights are touched.

Results, on held-out scenes and tasks:

| Setting | Before | After | Multiple |
|---------|--------|-------|----------|
| Unseen scenes | 9.7% | **43.3%** | 4.5× |
| Unseen tasks | 12.7% | **40.2%** | 3.2× |

The gains are largest where the benchmark sits far from the policy's training data, and wrapping a general policy this way often beats the finetuned version.

It also **evolves its own persistent memory**, carrying learned experience forward, and produces interpretable control strategies — "lift a jammed arm clear", "reach in horizontally when an obstacle blocks from above".

### Why this generalises beyond robotics

Strip the domain and the loop is: **fixed capability, variable scaffolding, and the scaffolding is what improves.**

That is the same contract as CLEO in this batch, from the opposite direction. CLEO prunes a harness down until only what earns its place remains. RoboArchitect grows one by diagnosing failures. Both leave the model alone.

For this workspace the transferable claim is narrower but real: **when an agent underperforms, the harness is a legitimate and often cheaper thing to change than the model** — and a coding agent can do that revision itself if the failure signal is legible.

### Caveat

Abstract only. The harness revisions are described in natural language; the paper does not establish that they are stable across policies or that they avoid overfitting the optimisation episodes.

## Snippets

> "Without updating any model weights, ROBOARCHITECT raises average success from 9.7% to 43.3% on unseen scenes (4.5×) and from 12.7% to 40.2% on unseen tasks (3.2×), across multiple benchmarks and policies." [Source: arxiv-2610.42141 p.1]

> "The harness also evolves its own persistent memory, carrying learned experience…" [Source: arxiv-2610.42141 p.1]

## Dead Ends

- **Assuming harness revisions transfer across policies.** Not established.
