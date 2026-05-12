---
title: "Agent Trajectory Triage — Cheap Non-LLM Signals for Sampling"
type: concept
tags: [concept, agent-trajectories, triage, observability, preference-data, signal-taxonomy, conductor, audit-trail, conductor-relevant]
keywords: [trajectory sampling, signal taxonomy, misalignment, stagnation, disengagement, satisfaction, failure, loop, exhaustion, tau-bench, RLHF, preference-data, conductor-audit]
related:
  - sources/signals-trajectory-triage.md
  - concepts/conductor-orchestrator.md
  - concepts/cryptographic-audit-trail.md
  - concepts/agent-memory-critique.md
  - concepts/reviewer-agent-inference-time-feedback.md
  - concepts/verbalized-sampling-llm-diversity.md
  - sources/verbalized-sampling-mode-collapse.md
  - concepts/rlhf-critic-bias.md
  - sources/rlhf-critic-bias-al-zawahreh-2026.md
maturity: validated
created: 2026-05-11
updated: 2026-05-11
---

## Relations

- `@sources/signals-trajectory-triage.md` — primary source (DigitalOcean, Apr 2026)
- `@concepts/conductor-orchestrator.md` — Conductor produces the trajectories these signals would triage
- `@concepts/cryptographic-audit-trail.md` — Cemini's existing audit JSONL is the natural substrate for signal computation
- `@concepts/agent-memory-critique.md` — claude-mem stores observations; signals could grade observation value
- `@concepts/reviewer-agent-inference-time-feedback.md` — complementary inference-time pattern (this concept is post-hoc; reviewer is inline)
- `@concepts/verbalized-sampling-llm-diversity.md` — third orthogonal Conductor layer (inference-time generation diversity; complements this post-hoc triage)
- `@sources/verbalized-sampling-mode-collapse.md` — VS paper source
- `@concepts/rlhf-critic-bias.md` — **sibling forensic taxonomy** (K40). Signals = trajectory-level non-LLM forensics (interaction/execution/environment families). 5-tell scorecard = evaluative-output-level non-LLM forensics (content-independence / evidence-contradiction / catalog-match / prompt-contingent reproducibility / absence-of-novel-insight). Both are cheap audit primitives applicable post-hoc to LLM-produced artifacts.
- `@sources/rlhf-critic-bias-al-zawahreh-2026.md` — RLHF Critic Bias source (Al-Zawahreh April 2026, draft maturity)

## Raw Concept

Extracted from the DigitalOcean "Signals" paper (arXiv 2604.00356v1, Apr 2026). Production agents emit voluminous, non-deterministic trajectories. LLM-as-judge evaluation per trajectory is cost-prohibitive; human review doesn't scale. The paper proposes computing cheap, **non-LLM** signals from live interactions and attaching them as structured attributes for downstream triage. This page captures the taxonomy, the empirical envelope, and Cemini integration paths.

## Narrative

### The signal taxonomy

Three families, all computable without model calls (regex / string-matching / counters):

| Family | Signals | What it detects |
|--------|---------|-----------------|
| **Interaction** | misalignment, stagnation, disengagement, satisfaction | Are user and agent converging? Is the user pushing back, going silent, restating their request? |
| **Execution** | failure, loop | Tool errors, repeated identical actions, infinite-loop traps |
| **Environment** | exhaustion | Context-window limit, token budget burned, retry-cap hit |

The critical engineering claim: signals are **cheap enough to attach to every trajectory** in real time. No sampling. No deferred batch jobs. Just an attribute on each trajectory record.

### Empirical headline

From τ-bench:

| Sampling method | Informativeness rate |
|---|---:|
| Random sampling | 54% |
| Heuristic filtering | 74% |
| **Signal-based sampling** | **82%** |

**1.52× efficiency gain per informative trajectory** vs random. The gain is robust across reward strata and task domains, which rules out the "oversampling obvious failures" explanation. Signals do produce genuine per-trajectory informativeness improvements.

### Cemini integration paths

Four concrete integration vectors:

1. **Conductor audit JSONL signal-attachment** (immediate, low-cost)
   - Cemini writes per-trajectory audit JSONL to `/opt/cemini/audit/*.jsonl` (see `@concepts/cryptographic-audit-trail.md`)
   - Add a `signals: {...}` field at trajectory close-out — populated with the 6-7 signals from the taxonomy
   - Zero LLM cost; computed in the existing audit writer
   - Implementation cost: single Python module, ~200-300 LOC, no external deps

2. **claude-mem observation prioritization** (moderate-cost integration)
   - claude-mem v13 injects top-5 observations per session via embedding similarity
   - Augment ranking with signal-based weighting: observations from `misalignment` or `failure` trajectories should rank higher than `satisfaction` trajectories (more learning value per byte)
   - Requires touching claude-mem's observation-ranking step, not just the audit writer

3. **Operator dashboard filter** (immediate, UX-only)
   - "Show me misaligned/looping trajectories this hour" is immediately useful for production debugging
   - No model dependency; just a filter on the audit JSONL
   - The cheapest possible win — signals attached, simple filter UI, demonstrable value before any RL ambitions

4. **Preference-data construction** (longer-horizon, future RL)
   - When Cemini accumulates enough trajectories to fine-tune (DPO / RLHF) on its own data, signal-based sampling gives a 1.5× curation efficiency over naive random
   - Roadmap-level; the paper's longer-term motivation

### Implementation order (Cemini-specific)

Recommended sequence:

1. **Phase 0**: Add `signals` field to audit JSONL schema. Compute the 6-7 signals at trajectory close-out. Backfill on historical trajectories. (~1-2 days)
2. **Phase 1**: Build operator dashboard filter. Validate signals against operator intuition on real trajectories. (~1 week)
3. **Phase 2**: Integrate signal weighting into claude-mem observation ranking. Measure recall@k on a held-out task set. (~1 week)
4. **Phase 3**: Begin preference-data construction for downstream RL once trajectory volume justifies it.

### Architectural complement to reviewer agents

The Signals paper and the Apple Reinforced Agent paper (`@concepts/reviewer-agent-inference-time-feedback.md`) are **architecturally complementary**:

- **Reviewer agent**: improves trajectories *while they happen* (inference-time gating)
- **Signals**: improves *which trajectories matter* (post-hoc triage)

A complete Conductor v2 design uses both: reviewer-agent gates risky calls inline; signals triage the resulting trajectory stream for downstream learning, debugging, and observability. They share no implementation surface and can be developed in parallel.

### Why this matters for the IP-sale-readiness thesis

Trajectory triage is the kind of low-glamour, high-leverage instrumentation that signals (sorry) stack maturity. A buyer evaluating Cemini's prospectus can see:

- Every trajectory is tagged with structured failure / progress signals at close-out
- Operator dashboards expose drift modes in real time
- A clear data-curation pipeline is positioned to feed future model fine-tuning

This is observability infrastructure that compounds with every trajectory the system ever runs. It's a 200-300 LOC Phase-0 investment that future-proofs the audit substrate.

### Open questions

1. **Signal calibration on finance tasks**: τ-bench is a general benchmark. What does `misalignment` look like on a Kalshi weather thesis? Likely needs domain-specific regex / counter tuning before the 82% number transfers.
2. **Signal overlap**: are some signals strongly correlated (e.g., `failure` and `loop`)? Need an empirical correlation matrix on Cemini's audit corpus before deciding whether all 7 are independent value-adds.
3. **Adversarial robustness**: can a tool author game the signals (e.g., emit fake "satisfaction" tokens)? Low priority for an internal stack, but worth documenting before exposing signals externally.

## Snippets

> "We propose a lightweight, signal-based framework for triaging agentic interaction trajectories. Our approach computes cheap, broadly applicable signals from live interactions and attaches them as structured attributes for trajectory triage, identifying interactions likely to be informative without affecting online agent behavior." [Source: Signals.pdf p.1]

> "We organize signals into a coarse-grained taxonomy spanning interaction (misalignment, stagnation, disengagement, satisfaction), execution (failure, loop), and environment (exhaustion), designed for computation without model calls." [Source: Signals.pdf p.1]

> "Signal-based sampling achieves an 82% informativeness rate compared to 74% for heuristic filtering and 54% for random sampling, with a 1.52× efficiency gain per informative trajectory." [Source: Signals.pdf p.1]

> "The advantage is robust across reward strata and task domains, confirming that signals provide genuine per-trajectory informativeness gains rather than merely oversampling obvious failures." [Source: Signals.pdf p.1]

[Sources: @sources/signals-trajectory-triage.md (arXiv 2604.00356v1)]
