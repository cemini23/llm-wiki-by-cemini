---
title: "Runtime Monitoring of Distributed Cyber-Physical Systems Without a Global Clock (arXiv 2608.13486)"
type: source
tags: [arxiv, runtime-monitoring, formal-methods, STL, cps, watch, trading-infra, k237]
keywords: [DiSTL, consistent cut, concut, clock skew, STL, runtime monitoring, distributed, epsilon-synchrony]
related:
  - concepts/distributed-clock-drift-monitoring-pattern.md
  - concepts/multi-module-bot-conflict-detector-pattern.md
  - concepts/trading-bot-logging-discipline.md
  - concepts/strategy-half-life-live-monitoring.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
read_status: read
---

## Relations

- @concepts/distributed-clock-drift-monitoring-pattern.md — 2ε concurrency window WATCH concept
- @concepts/multi-module-bot-conflict-detector-pattern.md — cross-process race detection extension
- @concepts/trading-bot-logging-discipline.md — bot log discipline sibling
- @concepts/strategy-half-life-live-monitoring.md — live strategy monitoring

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.13486, "Runtime Monitoring of Distributed Cyber-Physical Systems Without a Global Clock" |
| Authors | Charles Koll, Houssam Abbas (Oregon State University) |
| Retrieved | 2026-08-14 |
| File | `arxiv-2608.13486-runtime-monitoring-of-distributed-cyber-physical.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/` |
| Type | cs.LO preprint, 24pp, NSF-funded |

## Narrative

First theoretical characterization + algorithm for **continuous (dense-time) runtime monitoring** of a distributed CPS against Signal Temporal Logic (STL) when agents have **drifting local clocks** (no global clock; skew bounded by known ε, e.g. via NTP). Defines restricted STL fragment **DiSTL** and a "satisfaction signal" over **consistent cuts (concuts)**; the monitor returns the set of all possible global moments at which the spec could hold — violations detected **conservatively** under clock uncertainty.

### Key ideas

- **Partial synchrony** (Assumption 1): local clock cₙ strictly increasing, |cₙ(χ)−χ| ≤ ε. N events are **concurrent** if |tₙ−tₘ| ≤ 2ε — order unknowable, all must be treated as possibly synchronous.
- **Retimings** ρₙ: |t−ρₙ(t)| ≤ ε; distributed signal satisfies φ iff ∃ retiming making the synchronized trace satisfy it.
- **DiSTL fragment** (Def 4): all temporal operators, but conjunction restricted (right operand atomic) to avoid tracking every witnessing retiming.
- **Satdomain** as non-convex polytopes (NCPs); MoveBackin/MoveBackout (Alg 1) give inner/outer approximations with arbitrary tightness (Theorem 3: mon_in ⊆ satdomain ⊆ mon_out).
- Complexity O(N·P·M^⌊(N+1)/2⌋ + ...) — exponential in number of agents.
- **Scalability**: boolean conjunctions monitor up to ~57 agents real-time; complex temporal formulas drop to 6–9 agents (ε=0.05). Runtime varies hugely with signal content (95s vs 0.2s at N=63).

### Steal-for-WATCH (trading-infra / bot resilience)

Practical steal is the **"set-of-possible-synchronizations" mindset + 2ε concurrency window**, not the STL polytope machinery: events within 2ε on different processes (exchange, adapter, PM lane, egress relay) must all be explored for possible violation. Express bot safety requirements as temporal invariants ("within [a,b] after order-fill on HL adapter, the PM position book must update"), and monitor conservatively so clock drift never produces a false "all clear." This is dense-time offline theory on continuous signals — trading events are discrete, so the 2ε window and conservative-verdict discipline are the transferable core.

**Brief:** wiki-only (WATCH concept). Tier: `[TENTATIVE]` — single preprint; authors established in runtime-verification.
