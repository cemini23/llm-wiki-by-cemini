---
title: "Signals — Trajectory Sampling and Triage for Agentic Interactions (DigitalOcean, Apr 2026)"
type: source
tags: [source, agent-trajectories, triage, observability, preference-data, llm-as-judge, digitalocean, conductor-relevant]
keywords: [trajectory sampling, signal taxonomy, misalignment, stagnation, disengagement, loop detection, tau-bench, RLHF preference data]
related:
  - concepts/agent-trajectory-triage-signals.md
  - concepts/conductor-orchestrator.md
  - concepts/cryptographic-audit-trail.md
  - concepts/agent-memory-critique.md
maturity: validated
read_status: deep-read
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@concepts/agent-trajectory-triage-signals.md` — taxonomy + sampling pattern extracted from this paper
- `@concepts/conductor-orchestrator.md` — Conductor produces the trajectories these signals would triage
- `@concepts/cryptographic-audit-trail.md` — Cemini's existing audit JSONL is the natural substrate for signal computation
- `@concepts/agent-memory-critique.md` — claude-mem stores observations; signals could grade which observations are worth keeping

## Raw Concept

- **Title**: Signals: Trajectory Sampling and Triage for Agentic Interactions
- **Authors**: Shuguang Chen, Adil Hafeez, Salman Paracha (DigitalOcean Holdings, Inc.)
- **Type**: Academic paper (cs.AI)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Signals- Trajectory Sampling and Triage for Agentic Interactions.pdf`
- **arXiv**: 2604.00356v1 (1 Apr 2026)
- **sha256**: `ca8f534c6a5702d5…` (preingest verdict: NEW)
- **Pages**: 10
- **Read-status**: deep-read

## Narrative

Production-deployed agents emit voluminous, non-deterministic trajectories. LLM-as-judge evaluation of every trajectory is cost-prohibitive. Human review doesn't scale. The paper proposes computing cheap, **non-LLM** signals from live interactions and attaching them as structured attributes for downstream triage — converting raw trajectory data into a substrate that *can* be fed into preference learning (RLHF / DPO) or developer review.

### Signal taxonomy (computed without LLM calls)

| Family | Signals | What it detects |
|--------|---------|-----------------|
| **Interaction** | misalignment, stagnation, disengagement, satisfaction | Are user and agent converging? Is the user pushing back, going silent, restating? |
| **Execution** | failure, loop | Tool errors, repeated identical actions, infinite-loop traps |
| **Environment** | exhaustion | Context-window limit approached, token budget burned, retry-cap hit |

All signals are computed with regex / string-matching / counters — no model calls. That's the critical engineering claim: signals are **cheap enough to attach to every trajectory** in real time.

### Headline empirical result (τ-bench)

| Sampling method | Informativeness rate |
|---|---:|
| Random sampling | 54% |
| Heuristic filtering | 74% |
| **Signal-based sampling** | **82%** |

**1.52× efficiency gain per informative trajectory** vs random. Result is robust across reward strata and task domains (i.e., not just oversampling obvious failures — genuine per-trajectory informativeness gains).

### Cemini significance

**HIGH-fit** for Conductor audit-trail + claude-mem. Direct integration paths:

1. **Conductor audit JSONL** (`/opt/cemini/audit/*.jsonl` per the conductor-audit-trail-phase1 brief): Add a `signals: {...}` field at trajectory close-out. Compute the 6-7 signals defined in the paper's taxonomy. Zero LLM cost.
2. **claude-mem observation budget**: claude-mem v13 currently injects top-5 observations per session via embedding similarity. Augment with signal-based filtering — observations from `misalignment` or `failure` trajectories likely carry higher learning value than `satisfaction` trajectories.
3. **Preference-data construction**: When Cemini accumulates enough trajectories to fine-tune a model on its own data (the paper's longer-term motivation), signal-based sampling gives a 1.5× efficient curation pipeline vs naive random.
4. **Operator dashboard**: A simple "show me misaligned/looping trajectories this hour" filter is immediately useful for production debugging, regardless of any RL plans.

**Implementation cost**: Single Python module, ~200-300 LOC, no external dependencies. Drop-in on top of the existing audit JSONL writer.

### Snippets

> "We propose a lightweight, signal-based framework for triaging agentic interaction trajectories. Our approach computes cheap, broadly applicable signals from live interactions and attaches them as structured attributes for trajectory triage, identifying interactions likely to be informative without affecting online agent behavior." [Source: Signals.pdf p.1 (Abstract)]

> "We organize signals into a coarse-grained taxonomy spanning interaction (misalignment, stagnation, disengagement, satisfaction), execution (failure, loop), and environment (exhaustion), designed for computation without model calls." [Source: Signals.pdf p.1 (Abstract)]

> "Signal-based sampling achieves an 82% informativeness rate compared to 74% for heuristic filtering and 54% for random sampling, with a 1.52× efficiency gain per informative trajectory." [Source: Signals.pdf p.1 (Abstract)]

> "The advantage is robust across reward strata and task domains, confirming that signals provide genuine per-trajectory informativeness gains rather than merely oversampling obvious failures." [Source: Signals.pdf p.1 (Abstract)]

### Pairing with Reinforced Agent (2604.27233)

The two arXiv papers in this ingest batch (Signals + Reinforced Agent) are architecturally **complementary**:

- **Reinforced Agent**: improves trajectories *while they happen* (inference-time review)
- **Signals**: improves *which trajectories matter* (post-hoc triage)

A complete Conductor v2 design uses both: reviewer-agent gates risky calls inline; signals triage the resulting trajectory stream for downstream learning and observability.

[Source: Signals- Trajectory Sampling and Triage for Agentic Interactions.pdf, arXiv:2604.00356v1]
