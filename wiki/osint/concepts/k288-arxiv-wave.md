---
title: K288 arXiv Wave — deterministic policy gates + perceptually grounded eval (Oct 2026)
type: concept
tags: [k288, arxiv, agents, safety, policy-gate, evaluation, video]
keywords: [k288, nomos, tool-call-gate, static-verification, co-speech-gesture, semantic-gesture-preservation]
related:
  - concepts/k288-eval-wave.md
  - concepts/k288-feeds-wave.md
  - concepts/agent-authorization-stack.md
  - sources/arxiv-2610.11030-nomos-2026-10-10.md
  - sources/arxiv-2610.11669-co-speech-gesture-benchmark-2026-10-10.md
  - concepts/k289-arxiv-wave.md
maturity: draft
created: 2026-10-10
updated: 2026-10-25
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k288-eval-wave.md
- @concepts/k288-feeds-wave.md
- @concepts/agent-authorization-stack.md
- @sources/arxiv-2610.11030-nomos-2026-10-10.md
- @sources/arxiv-2610.11669-co-speech-gesture-benchmark-2026-10-10.md

## Raw Concept

K288 arXiv cluster hub. **2 papers.** Dual-ID **OSINT K288**.

## Narrative

### 1. NOMOS — compile the policy, then gate in code (the important one)

`arXiv 2610.11030`. A four-pass compiler turns a **natural-language agent policy** into a **runtime tool-call gate with no LLM**: PARSE → **EXTRACT** (the only LLM pass) → **RESOLVE** (deterministic static checks) → MATERIALIZE. The runtime gate evaluates each call against **facts from real tool results only**, in **microseconds, zero LLM**.

**Violations 66.3% → 2.6%** (airline) and **30.8% → 6.9%** (retail). **AgentDojo banking ASR 0.0%** vs 46.5% undefended. A PolicyGuard reimplementation costs **+74% wall-clock and 347 LLM calls** vs **3 µs/call and zero**.

**Two things to carry:** (a) this is the **strongest counter to "guardrails are prompt-level"** — compile once, verify statically, enforce deterministically; (b) **RESOLVE repairs/rejects 37%/13% of candidates** — generated policy is wrong about a third of the time, so **extraction must be statically verified, never trusted**. **Implementation not released** (Zenodo DOI only).

### 2. Co-speech gesture benchmark — a metric that measures nothing

`arXiv 2610.11669`. A perceptually grounded benchmark for **co-speech gesture generation**, validated against 101 human participants. 13 objective metrics plus **Semantic Gesture Preservation** (`SGP_cm = 1 − n(beats)/n(semantic intervals)`).

**The finding:** a widely used metric (**SC**) correlates with **no** perceptual dimension, while **SGP** correlates with speech timing and content match (ρ = 0.39). **Composites beat the best single metric** (content match ρ = 0.7824).

### The shared lesson

Both papers are the **"measure the right thing"** doctrine: NOMOS measures enforcement at the **boundary** (not in the prompt), and the gesture benchmark measures **semantics** (not motion plausibility). Same shape as K285's PatchBench (a global metric blind to local damage).

### Boundary

**FILE only. No install.** Route: NOMOS → CCC + cyber; gesture benchmark → Image-gen/video.

### Distribution

- NOMOS → `../Cemini claude code CCC/briefs/2026-10-10_k288-deterministic-policy-gates.md` and `../Cybersecurity wiki/briefs/2026-10-10_k288-nomos-toolcall-gates.md`
- Gesture benchmark → `../Image gen/briefs/2026-10-10_k288-gesture-eval.md`
