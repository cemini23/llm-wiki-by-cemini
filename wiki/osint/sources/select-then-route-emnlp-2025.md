---
title: "Select-Then-Route: Taxonomy-Guided Routing for LLMs"
type: source
tags: [source, llm-agents, model-routing, cascade, taxonomy, production-routing, conductor-relevant]
keywords: [select-then-route, llm-router, taxonomy-guided, model-cascade, multi-judge, cost-optimization, emnlp-2025]
related:
  - concepts/llm-agent-systems.md
  - concepts/conductor-orchestrator.md
  - sources/toolorchestra-2511.21689.md
  - sources/masrouter-acl-2025.md
  - sources/meta-router-2509.25535.md
maturity: validated
created: 2026-05-01
updated: 2026-05-01
---

## Relations

- @concepts/llm-agent-systems.md — StR is the production routing layer for Conductor's model-selection decision.
- @sources/toolorchestra-2511.21689.md — ToolOrchestra provides the orchestrator; StR provides the routing mechanism it can use.
- @concepts/conductor-orchestrator.md — Conductor is the synthesis concept; StR provides the routing layer (taxonomy + cascade + confidence gate).
- @sources/masrouter-acl-2025.md — MasRouter extends routing to multi-agent collaboration mode selection; StR handles single-query routing.
- @sources/meta-router-2509.25535.md — Meta-Router provides the causal evaluation framework for training StR's routing decisions.

## Raw Concept

- Original title: SELECT-THEN-ROUTE: Taxonomy guided Routing for LLMs
- Author(s): Soham Shah, Kumar Shridhar (Ema Unlimited, Inc.)
- Type: EMNLP 2025 Industry Track
- Location: https://aclanthology.org/2025.emnlp-industry.28.pdf
- Retrieved: 2026-05-01 (K25 Conductor sweep)
- Read status: deep-read

## Narrative

Select-Then-Route (StR) is a two-stage LLM routing framework that addresses the core scaling problem: deciding among ALL available LLMs per query is prohibitively expensive. StR first narrows the decision space via a lightweight taxonomy-guided selector, then routes within the selected pool via an adaptive cascade with multi-judge confidence gating.

### Architecture

**Stage 1 — Select**: A lightweight taxonomy classifier maps each query to its semantic class (e.g., reasoning, code, summarization) and selects a small pool of models proven proficient for that class. This narrows the decision space from "all models" to "2-4 relevant models."

**Stage 2 — Route**: Within the selected pool, a confidence-based cascade begins with the cheapest model and escalates only when a multi-judge agreement test signals low reliability. If judges disagree on response quality, the query escalates to the next model in the pool.

### Results

- End-to-end accuracy: 91.7% (best single model) → **94.3% (StR)**
- Inference cost: **4× reduction** vs. always using the best model
- Both taxonomy and multi-judge thresholds are tunable — exposes a smooth cost/quality Pareto frontier
- Tested across 6 public benchmarks of various domains

### Why this matters for Conductor

StR provides the routing mechanism for Conductor's model-selection decision. Key design elements to adopt:

1. **Two-stage architecture** — narrow then route. Prevents the combinatorics problem of evaluating all models.
2. **Taxonomy-guided selection** — semantic classification of queries into task types. Cemini's analyst already has query types (ticker lookup, options analysis, sentiment, etc.) — this maps directly.
3. **Multi-judge confidence gating** — escalates only when needed. This is the operationalization of "route to cheap model unless confidence is low."
4. **Tunable cost/quality tradeoff** — exposes explicit knobs for the operator to dial.

Production-grade (EMNLP Industry track), tested on 6 benchmarks. Ema Unlimited is a commercial AI company — the pattern is battle-tested.

## Snippets

**S1 — Core problem**:
> "Sending each query to the most suitable model mitigates this limitation, but deciding among all available LLMs for each query is prohibitively expensive."

**S2 — Two-stage solution**:
> "StR first employs a lightweight, taxonomy-guided selector that maps each query to models proven proficient for its semantic class. Within the selected pool, a confidence-based cascade begins with the cheapest model and escalates only when a multi-judge agreement test signals low reliability."

**S3 — Results**:
> "StR improves the end-to-end accuracy from 91.7% (best single model) to 94.3% while reducing inference cost by 4×."

**S4 — Tunability**:
> "Because both the taxonomy and multi-judge evaluation thresholds are tunable, StR exposes a smooth cost/quality Pareto frontier."
