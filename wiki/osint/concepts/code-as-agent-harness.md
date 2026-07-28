---
title: "Code as agent harness — executable, verifiable, stateful agents"
type: concept
tags: [concept, agent-harness, coding-agents, agentic-ai, survey-synthesis]
keywords: [code-as-agent-harness, harness-interface, harness-mechanisms, multi-agent-coordination, verification, stateful-agents]
related:
  - entities/tools/outlines.md
  - entities/tools/gigatoken.md
  - sources/arxiv-code-as-agent-harness-survey-2605.18747.md
  - sources/arxiv-continual-harness-self-improving-agents-2605.09998.md
  - sources/arxiv-rocketsmith-agentic-rocketry-2606.00097-2026-06-08.md
  - entities/tools/rocketsmith.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/probabilistic-agent-policy-verification.md
  - sources/arxiv-probabilistic-agent-verification-2606.20510-2026-06-21.md
  - concepts/generator-verifier-inference-time-steering.md
  - concepts/llm-agent-systems.md
  - sources/agentic-harness-engineering.md
  - concepts/cemini-ai-assistant.md
  - sources/arxiv-self-healing-llm-agents-2605.06737.md
  - sources/arxiv-grep-agent-harness-2605-15184.md
  - sources/arxiv-skillrae-agent-skills-2605.10114.md
  - sources/arxiv-graphflow-verifiable-workflows-2605.14968.md
  - concepts/skillrae-retrieval-augmented-execution.md
  - concepts/graphflow-verifiable-agent-workflows.md
  - sources/arxiv-weavebench-2606.09426-2026-06-11.md
  - sources/arxiv-siga-scientific-sim-adapters-2606.09774-2026-06-11.md
  - concepts/agentified-agent-assessment.md
  - sources/arxiv-agentbeats-aaa-assessment-2606.13608-2026-06-12.md
  - concepts/agents-all-the-way-down-methodology.md
  - sources/arxiv-agents-all-the-way-down-2606.11869-2026-06-16.md
  - sources/arxiv-claw-swe-bench-2606.12344-2026-06-16.md
  - concepts/claw-swe-bench-harness-evaluation.md
  - entities/tools/claw-swe-bench.md
  - sources/arxiv-harnessfix-trace-repair-2606.06324-2026-06-16.md
  - sources/arxiv-aohp-os-agent-harness-2606.23449-2026-06-23.md
  - concepts/aohp-os-level-agent-harness.md
  - entities/tools/aohp-os.md
  - concepts/self-compacting-language-model-agents.md
  - concepts/fara-computer-use-agent-training.md
  - sources/arxiv-toolbench-x-tool-unreliability-2606.25819-2026-06-26.md
  - concepts/toolbench-x-tool-reliability-hazards.md
  - entities/tools/toolbench-x.md
  - concepts/nagus-ops-control-plane.md
  - concepts/agent-reactive-bugs.md
  - concepts/agent-governance-manifest.md
  - sources/arxiv-2607.15684-agent-reactive-bugs-model-harness.md
  - sources/arxiv-2607.15715-behavioral-controllability-agentic-ie.md
  - sources/arxiv-2607.15769-agent-governance-manifest.md
  - concepts/verifier-deployment-gap.md
  - concepts/swap-regret-attention-fictitious-play.md
  - sources/arxiv-2607.24663-aps-rag.md
  - sources/newsletter-rss-latent-space-2026-07-28-kimi-k3.md
  - sources/arxiv-2607.24300-self-authored-verification.md
  - sources/arxiv-2607.23333-swap-regret-attention.md
  - concepts/document-processing-pipeline-scale-patterns.md
  - sources/x-lamgary-harvey-scaling-document-processing-2026-07-27.md
  - concepts/credential-leak-revoke-first-response.md
  - sources/substack-rss-seceng-weekly-2026-07-28-aws-keys-public-repo.md

  - sources/newsletter-rss-latent-space-2026-07-21-ainews.md
  - sources/arxiv-2607.19267-authority-framing-laundered-code.md
  - sources/arxiv-2607.19336-agents-in-the-wild-deployment.md
  - sources/substack-rss-addy-osmani-2026-07-22-software-factories.md
  - sources/newsletter-rss-latent-space-2026-07-22-ai-cybersecurity.md
  - entities/tools/likec4.md
  - entities/tools/pi-web.md
  - sources/arxiv-2607.19262-biosecbench-surveillance.md
  - sources/newsletter-rss-pragmatic-engineer-2026-07-21-napkin-math.md
  - sources/newsletter-rss-latent-space-2026-07-21-xaira-x-cell.md
  - sources/arxiv-2607.16825-particle-accelerators-collaboration.md
  - sources/arxiv-2607.19899-correlated-agreement-blindness.md
  - sources/arxiv-2607.20064-pro-long-programmatic-memory.md
  - sources/arxiv-2607.20268-potre-cognitive-heterogeneity.md
  - sources/newsletter-rss-latent-space-2026-07-23-laguna-poolside.md
  - sources/arxiv-2607.22520-regression-tax-llm-skills.md
  - sources/arxiv-2607.22529-skill-self-play.md
  - sources/arxiv-2607.22511-causalforge-lean-causal-research.md
  - concepts/skill-regression-tax.md
maturity: draft
created: 2026-05-21
updated: 2026-07-28
---

## Relations

- @sources/substack-rss-seceng-weekly-2026-07-28-aws-keys-public-repo.md — K201

- @concepts/credential-leak-revoke-first-response.md — K201

- @sources/x-lamgary-harvey-scaling-document-processing-2026-07-27.md — K199

- @concepts/document-processing-pipeline-scale-patterns.md — K199 Job Framework/backpressure

- @sources/arxiv-2607.23333-swap-regret-attention.md — K198 backlink

- @sources/arxiv-2607.24300-self-authored-verification.md — K198 backlink

- @sources/newsletter-rss-latent-space-2026-07-28-kimi-k3.md — K198 Kimi K3

- @sources/arxiv-2607.24663-aps-rag.md — K198 MCP RAG eval

- @concepts/swap-regret-attention-fictitious-play.md — K198

- @concepts/verifier-deployment-gap.md — K198

- @concepts/skill-regression-tax.md — K196 skills help/hurt; before/after matrices
- @sources/arxiv-2607.22520-regression-tax-llm-skills.md — K196
- @sources/arxiv-2607.22529-skill-self-play.md — K196 co-evolve behind regression gates
- @sources/arxiv-2607.22511-causalforge-lean-causal-research.md — K196 Lean acceptor > LLM-as-judge

- @sources/arxiv-2607.20268-potre-cognitive-heterogeneity.md — K191 skim

- @sources/arxiv-2607.20064-pro-long-programmatic-memory.md — K191 programmatic memory

- @sources/arxiv-2607.19899-correlated-agreement-blindness.md — K191 agreement blindness

- @sources/arxiv-2607.16825-particle-accelerators-collaboration.md — K182 Pass thin

- @sources/newsletter-rss-latent-space-2026-07-21-xaira-x-cell.md — K182 thin Xaira

- @sources/newsletter-rss-pragmatic-engineer-2026-07-21-napkin-math.md — K182 napkin math

- @sources/arxiv-2607.19262-biosecbench-surveillance.md — K182 thin biosec Context

- @entities/tools/pi-web.md — K182 Extract

- @entities/tools/likec4.md — K182 Extract

- @sources/substack-rss-addy-osmani-2026-07-22-software-factories.md — K182 light vs dark factory

- @sources/arxiv-2607.19336-agents-in-the-wild-deployment.md — K182 deployment gap

- @sources/arxiv-2607.19267-authority-framing-laundered-code.md — K182 authority framing CI/CD

- @sources/newsletter-rss-latent-space-2026-07-21-ainews.md — K178 Cursor multi-agent / cost variance Context

- @concepts/agent-reactive-bugs.md — K177 AR bugs at model–harness boundary
- @concepts/agent-governance-manifest.md — K177 project-side governability (AGM)
- @sources/arxiv-2607.15684-agent-reactive-bugs-model-harness.md
- @sources/arxiv-2607.15715-behavioral-controllability-agentic-ie.md
- @sources/arxiv-2607.15769-agent-governance-manifest.md
- @sources/arxiv-rocketsmith-agentic-rocketry-2606.00097-2026-06-08.md — **physical-domain harness** (K105): skills + subagents + MCP over OpenRocket/build123d; flight-test oracle
- @entities/tools/rocketsmith.md — MIT plugin; REFERENCE-only for Cemini
- @sources/arxiv-code-as-agent-harness-survey-2605.18747.md — primary synthesis source (UIUC/Meta/Stanford survey, May 2026)
- @sources/arxiv-continual-harness-self-improving-agents-2605.09998.md — online reset-free harness refinement (embodied agents; refiner loop analogue)
- @concepts/continual-harness-online-self-improvement.md — K72 synthesis
- @concepts/llm-agent-systems.md — parent cluster
- @sources/agentic-harness-engineering.md — complementary: observability-driven harness *evolution*
- @sources/arxiv-grep-agent-harness-2605-15184.md — retrieval/harness interaction (PwC, May 2026)
- @concepts/cemini-ai-assistant.md — Cemini user-facing agent should map to harness-interface + verification layers
- @sources/arxiv-self-healing-llm-agents-2605.06737.md — runtime failure detection + corrective replanning atop harness execution
- @concepts/nagus-ops-control-plane.md — packetized ops brain/queue as harness write-back

## Raw Concept

Prompted by Tier-2 sweep ingest of arXiv:2605.18747 — a 102-page survey codifying the industry shift from "LLMs that write code" to "code as the infrastructure layer agents run on."

## Narrative

### Three-layer model (from survey)

| Layer | What it covers | Cemini mapping |
|-------|----------------|----------------|
| **Harness interface** | Code linking reasoning ↔ action ↔ environment | Conductor routing + MCP tool calls + kb-server reads |
| **Harness mechanisms** | Planning, memory, tools, feedback control | Stash episodic memory; lazy-tool catalog; reviewer loops |
| **Scaling the harness** | Multi-agent shared artifacts | Prod MCP + server-Claude vs laptop wiki curator |

### Design imperatives for Cemini

- **Executable** — proposed actions must compile to verifiable tool calls (Cemini AI confirm gate).
- **Verifiable** — harness changes need regression checks (skill_audit, MCPT for strategies); K196 **regression tax**: measure tasks that *worsen* after skills, not only average uplift.
- **Stateful** — shared state across turns (stash, wiki log, hot.md) without silent drift.

### K196 — skill self-play + Lean research gates

@concepts/skill-regression-tax.md — co-evolving skills (2607.22529) only behind before/after matrices; CausalForge (2607.22511) reinforces machine-checkable acceptors over LLM reviewers for research loops.

### Physical-domain instance (K105)

@sources/arxiv-rocketsmith-agentic-rocketry-2606.00097-2026-06-08.md — RocketSmith wraps OpenRocket (sim source of truth) → build123d (parametric STEP) → PrusaSlicer (weight oracle). Same three-layer model: harness interface = MCP tools; mechanisms = 6 subagents + 7 skills; scaling = GUI read mirror + human-in-the-loop for slicing/recovery timing. **Steal:** deterministic codegen + programmatic mass check ≈ backtest/replay gates before prod.

### Open problems called out in source (actionable)

Evaluation beyond final success; verification with partial feedback; regression-free harness edits; multi-agent state consistency; human oversight for finance actions.

## Snippets

> "Programs are increasingly used as the medium through which agents reason, act, model environments, and verify execution."
> — [Source: 2605.18747_code-as-agent-harness-survey.pdf p.1]
