---
title: "Budget-aware agent rewards — stay inside the stated budget"
type: source
related:
  - concepts/k294-ccc-wave.md
maturity: draft
read_status: skimmed
updated: 2026-10-23
---

## Raw Concept

Title: Rewards for budget-aware multi-turn agents
Authors: Tom A. Lamb and coauthors, Apple and Oxford
Type: arXiv preprint (2610.28409)
Inbox file: `research to be indexed/cybersec/arxiv-2610.28409-rewards-for-budget-aware-multi-turn-agents-that.pdf`
Location: `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.28409-rewards-for-budget-aware-multi-turn-agents-that.pdf`
Retrieved: 2026-10-23
Read status: skimmed (abstract)

## Narrative

The authors train Qwen3.5 at 4B and 9B on AppWorld. Budgets cover tokens, API calls, and environment steps. They also train on BabyAI with turn budgets.

They train one policy per environment and resource type, across budget values. They compare eleven reward objectives.

Penalties for overspending beat task success alone. The gains transfer to unseen budgets. They also transfer zero-shot to a shifted task set and a new benchmark.

No single reward wins everywhere. A sigmoid overspend penalty most often wins within-budget success at one budget. A fixed negative reward generally wins natural compliance. Combining frequency and magnitude penalties gives the smallest average gap to the best method at each budget.

The abstract states no single percent. This page adds none. **No install. No route swap.**
