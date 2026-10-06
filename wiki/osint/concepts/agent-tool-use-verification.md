---
title: Agent Tool-Use Verification — deciding when tools are necessary and checking their evidence
type: concept
tags: [concept, agents, tool-use, verification, k233]
keywords: [tool-use-verification, mcts, reflective-principles, evidence-check, agent-reasoning]
related:
  - sources/arxiv-2608.10827-mira-2026-08-12.md
  - sources/arxiv-2610.06829-clift-web-agent-verification-2026-10-06.md
  - sources/arxiv-2610.06650-wikidata-search-traces-2026-10-06.md
  - sources/arxiv-2610.06782-t-search-agentic-retriever-2026-10-06.md
  - concepts/k283-arxiv-wave.md
  - entities/tools/t-search.md
  - entities/tools/tester-army-e2e.md
maturity: draft
created: 2026-08-12
updated: 2026-10-06
---

## Relations

- @sources/arxiv-2608.10827-mira-2026-08-12.md

## Raw Concept

What this page answers: when should an agent call an external tool, and how does it verify that the acquired evidence supports its hypothesis? From MIRA (arXiv 2608.10827), medical-domain example.

## Narrative

Indiscriminate tool use adds noise, propagates misleading evidence, and raises cost. The transferable pattern from MIRA: (1) a tool-augmented MCTS data engine that verifies grounding + reasoning consistency per node, (2) an online reflective-principle loop distilling failure cases into principles injected into later rollouts. Domain is medical (OOD) — the *loop* generalizes, the weights don't.

[Source: arXiv:2608.10827]

## K283 additions — judge-free verification, interpreter over tool-loop (2026-10-06)

Three K283 papers extend this thread:

- **CLIFT (@sources/arxiv-2610.06829-clift-web-agent-verification-2026-10-06.md).** Replace an expensive LLM judge with a **conformal-rectified bank of URL-scoped verification questions**. A Mondrian-ACI tracker per URL tier assigns a trust weight; the training reward is **additive-only** (r̃ = r_judge + β·max(0, R^VQ)) — the verifier never subtracts. Result: **+11.3 pp on OM2W at K=4 with zero policy training.** Recipe: a certified question bank + a lift-weighted score + conservative test-time selection.
- **Wikidata Search Traces (@sources/arxiv-2610.06650-wikidata-search-traces-2026-10-06.md).** A **persistent-Python-state RLM harness beats stateless tool-calling** (gpt-6-luna 49→61; Qwen3.8-27B 60→74). Verification improves when the agent can *hold* intermediate state, not just issue isolated calls.
- **T-Search (@sources/arxiv-2610.06782-t-search-agentic-retriever-2026-10-06.md).** Return **ranked evidence chunks with reasons, not answers** — so the verifier and the generator stay swappable. Apache-2.0.

Pattern across all three: **verification is cheaper and more reliable when it is external, certified, and separate from the generator.**
