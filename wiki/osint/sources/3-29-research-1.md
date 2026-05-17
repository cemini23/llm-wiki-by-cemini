---
title: "Cemini Financial Suite: Targeted Extraction Audit and Architectural Integration Report"
type: source
tags: [docx, rl-marl, llm-agents, cemini-internal, k49]
clusters: [rl-marl, llm-agents, cemini-internal]
related:
  - concepts/rl-marl-research.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-16
---

## Relations

- @concepts/rl-marl-research.md — cluster hub for RL/MARL research in the Cemini corpus

## Raw Concept

- **Original title**: Cemini Financial Suite: Targeted Extraction Audit and Architectural Integration Report
- **Author(s)**: Cemini internal research (commissioned audit + architectural-synthesis brief)
- **Type**: DOCX
- **Location**: research for cemini/3_29 research 1.docx
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: ~9,600 words; ~16 entries + a closing architectural synthesis
- **Read status**: deep-read
- **Primary cluster**: rl-marl
- **All clusters**: rl-marl, llm-agents, cemini-internal

## Narrative

Third of three internal "Targeted Extraction Audit" briefs (companions: @sources/3-27-links-1.md, @sources/3-28-links-1.md). Same fixed per-entry template and same Cemini-integration framing — but **not a duplicate**: this one audits a **distinct set** dominated by **research papers and orchestration frameworks** (3-27 = memory/security infra repos; 3-28 = agent-skill/dev-tooling repos) and uniquely adds a closing **Architectural Synthesis** section that 3-27/3-28 lack.

**Entries audited:** Tessl.io context-file evaluation (AgentBench shows unvalidated LLM-generated context files cut task success ~3% and raise cost ~20% — adopt a Continuous Context Evaluation Loop); Claude Code skills (forked-subagent execution via `context: fork` / `agent: Explore` SKILL.md frontmatter; custom commands + Ruff/Trivy/Semgrep hooks); **Anthropic harness-design** (Generator-Evaluator decoupling to kill self-grading bias; Context Resets vs Automatic Compaction — hard resets with Pydantic handoff artifacts judged safer for trading-epoch transitions); **Caliber** (MIT — config drift detection, 100-point deterministic scoring, Score Regression Guard); **Stokowski** (WORKFLOW.md isolation, parallel Git clones, before/after_run hooks); **Correctless** (MIT — Spec/Test/Implement/QA/Verify multi-agent separation, enforced TDD state machine); **Think-Plan-Execute** (decoupled planning/execution DAG — for async intelligence gathering only, latency-fatal for live execution); **HolyClaude** (MIT — headless-browser containerization, s6-overlay supervision, `shm_size: 2g`, PUID/PGID permission sync); **SEVerA** (Formally Guarded Generative Models — rejection sampling with verified fallback; treats LLM output as an untrusted *proposal*, wrap `execute_trade` in a deterministic `check()`); **LLM-as-online-adaptive-controller** (Direct Numeric Control — LLM emits floats to tune TorchRL hyperparameters / Kelly sizing behind a hard "Volatility Gate"); **BEACOF** (Approximate Perfect Bayesian Equilibrium — coopetition belief-state debate, inverse-variance update, early stopping on belief stabilization); **MARCH** (information-asymmetric blind verification, Zero-Tolerance Reward — Solver/Proposer/Checker triad); **NLAH** (natural-language agent harnesses, file-backed state); **SlopCodeBench** (quantifies code degradation over iteration; Structural Erosion = CC × √SLOC as a CI gate); **Agent Factories / Sketch2Simulation** (ILP two-stage optimization → portfolio allocation across brokers); InfluenceMap & CORE Recommender (explicitly dismissed as irrelevant academic tooling).

**Architectural synthesis:** the platform should shift from heuristic generative orchestration to a **deterministic, cryptographically auditable** execution environment — FGGM + Zero-Tolerance-Reward hashing make the LLM a probabilistic proposal engine while Pydantic v2 validators enforce capital safety; Direct Numeric Control auto-tunes RL hyperparameters; config-drift detection + parallel Git clones protect solo-dev velocity. Rejects formal Alloy modeling, image parsing, and GPL-contaminated tooling (e.g. HolyClaude's CloudCLI) as IP-toxic or over-heavy for the 128GB CPU-only VPS.

## Snippets

> "The FGGM shifts the concept of tool-calling from a trusted, authoritative operation to an untrusted proposal. Under this pattern, the LLM does not execute the tool; it merely proposes arguments to the tool, which are then subjected to unrelenting deterministic scrutiny before the actual invocation is authorized by the system." [Source: 3_29 research 1.docx, §SEVerA]

> "Empirical evaluations utilizing benchmarks such as AgentBench demonstrate that unvalidated, large language model (LLM)-generated context files actively reduce task success rates by an average of three percent while simultaneously increasing inference costs by over twenty percent due to the processing of redundant tokens." [Source: 3_29 research 1.docx, §Tessl.io Evaluation Framework]

> "To secure the IP valuation, the platform must transition from heuristic-based, generative orchestration to a mathematically proven, deterministic execution environment." [Source: 3_29 research 1.docx, Architectural Synthesis and Recommendations]
