---
title: EnterpriseBench — strategic reasoning and decision-making agents (2026-09-30)
type: source
tags: [source, arxiv, benchmark, agents, harness, simulation]
keywords: [enterprisebench, beer-game, digital-twin, long-horizon, delayed-feedback]
related:
  - concepts/agent-harness-castle-project.md
  - entities/tools/gamedevbench.md
  - concepts/game-ai-rl-augmentation-shelf.md
  - sources/arxiv-2609.35928-prompted-identity-factionalism-2026-09-30.md
  - sources/inbox-arxiv-reject-batch-2026-09-30.md
  - entities/tools/firmbench.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2609.37658
maturity: validated
created: 2026-09-30
updated: 2026-09-30
---

## Raw Concept

**arXiv:2609.37658** — **EnterpriseBench** evaluates LLM agents on enterprise-level strategic reasoning and decision-making. [CONFIRMED]

The authors argue existing enterprise and financial benchmarks test static capabilities only: information extraction, numerical calculation, domain knowledge, and financial QA. Interactive long-horizon decision-making stays underexplored. [CONFIRMED]

The benchmark reorganizes existing enterprise and financial QA datasets into a unified foundational suite, annotated by capability and difficulty. It adds three professional interactive settings: Consulting (management-consulting-style business cases, multi-turn information seeking for client problem diagnosis); the Beer Game (adapted from the classic supply-chain management simulation, inventory control under delayed feedback); and Enterprise Digital Twin (a project-based business simulator for workforce, risk, and project planning). [CONFIRMED]

Experiments use nine agent methods under four backbone models. The authors find current agents are not yet stable, comprehensive, or cross-task reliable in enterprise scenarios. Code and benchmark are public at https://github.com/sduyangmin/FirmBench. [CONFIRMED]

## Narrative

### castle-sim / harness relevance [CONFIRMED]

- This is another agent-capability bench in the same family as @entities/tools/gamedevbench.md and GameLogicBench, so it belongs in the eval bench ladder.
- The Beer Game is a supply-chain simulation with delayed feedback. That shape is close to a castle-sim production chain: player and AI both order resources before they see the effect. Oscillation or bullwhip behaviour then follows. The delayed-feedback framing is a usable design lens for the Stronghold 2 storage and production chains.

### Caveat [TENTATIVE]

- The enterprise framing is a distant analogy to a hobby castle sim. Only the delayed-feedback simulation shape transfers.

## Dead Ends

- Treating enterprise QA scores as evidence of lord-AI quality.
- Running a 9-method x 4-backbone eval grid in a solo project.
