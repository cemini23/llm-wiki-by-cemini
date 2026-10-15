---
title: "AutoAgent0 — An Agentic Runtime for Safe Closed-Loop Driving"
type: source
tags: [arxiv, agent, runtime-harness, verification, safety]
keywords: [agentic runtime, trajectory verification, recovery planning, closed-loop, test-time execution, driving]
related:
  - concepts/k291-osint-wave.md
  - concepts/agent-harness-verification-bottleneck.md
  - concepts/agent-tool-use-verification.md
maturity: draft
read_status: read
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @concepts/k291-osint-wave.md — K291 osint wave hub
- @concepts/agent-harness-verification-bottleneck.md — a runtime that adds verification around an existing expert
- @concepts/agent-tool-use-verification.md — verify-before-execute, applied to trajectories

## Raw Concept

Title: AutoAgent0 — An Agentic Runtime for Safe Closed-Loop Driving
Authors: Jiageng Liu, Seth Z. Zhao, Zewei Zhou et al. (UCLA, CMU, UT Dallas, Stanford)
Type: arXiv preprint (2610.18866)
Location: `research to be indexed/osint/arxiv-2610.18866-autoagent0-an-agentic-runtime-for-safe-closed-lo.pdf`
Retrieved: 2026-10-14
Read status: read

## Narrative

**The reframing:** closed-loop driving safety treated as a **test-time execution problem**, not a training problem. End-to-end policies accumulate closed-loop errors and land in states they cannot recover from.

**AutoAgent0 augments an existing driving expert** — it does not replace it — with three additions:

1. **Complementary detection skills** — an independent module builds scene context where perception is inaccurate.
2. **Rule-based action verification** — proposed trajectories are checked against that context *before execution*.
3. **Recovery planning** — when nominal trajectories are unreliable, an agentic loop constructs alternatives.

### Why it is filed here

This is the **same shape** as this wiki's tool-call gate pattern: an LLM (or expert policy) proposes, a **deterministic verifier admits or refuses before the action executes**. Here the proposed artifact is a trajectory rather than a tool call. The transferable claim is that **runtime supervision covers off-nominal states a policy was never trained on**.

**No install, no wire.**

## Snippets

> "We address the challenge by treating closed-loop driving safety as a test-time execution problem." [Source: arxiv-2610.18866 p.1]

> "When the nominal trajectories are unreliable, the orchestrator of the runtime activates Recovery Planning, where an agentic loop constructs alter[natives]." [Source: arxiv-2610.18866 p.1]

## Dead Ends

- Reading this as a driving-technology item. The filing is for the **runtime/verifier architecture**; the domain is incidental.
