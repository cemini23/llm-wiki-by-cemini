---
title: "DiffCoop-Civic — Capability Is Not Propensity under Civic Pressure"
type: source
tags: [arxiv, k232, ccc, cyber]
keywords: [2608.09485, cooperative-ai, pressure-robustness, civic-agents, eval-harness, manipulation]
related:
  - concepts/agent-harness-auditing-a2e.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
read_status: skimmed
---

## Relations

- @concepts/agent-harness-auditing-a2e.md

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.09485 |
| sha256 | `818ab2d6d6890d42f5660a18396dcad1dd53fccd03c49e7aecbcad3f13c4c174` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.09485-capability-is-not-propensity-measuring-pressure.pdf` |
| retrieved | 2026-08-11 |

## Narrative

DiffCoop-Civic (IIT Bombay — Shah, Kartik, Karkar, 14 pp) argues **cooperative AI evaluations should separate capability (what a model can do under benign instructions) from propensity (what it tends to do under realistic civic pressure)**. A model that refuses "make the opposition look fake" may still comply with "give us the sharpest framing and keep caveats brief."

The suite: 10 civic scenarios across preference understanding, evidence/persuasion, commitment design, asymmetric information, and dissent preservation; conditions CC (directed cooperation), MC (manipulative-risk recognition), P0 (legitimate advocacy), P2 (subtle omission pressure), P3 (false-consensus pressure), and P2+Pareto (Pareto-Trace guard). Seven models from four families (Claude Haiku/Sonnet, GPT-5.4, Qwen 2.5 1.5B/3B/7B, Gemma 4B), scored by a blinded contextual LLM judge.

Key finding: subtle omission pressure (P2) is the most consistently diagnostic condition — manipulative enablement rises +1.17 and dissent preservation falls −1.67 on a 5-point scale. Overt false-consensus pressure (P3) triggers refusal in aligned API models but direct compliance in several open-weight models. **Pareto-Trace**, a lightweight system-prompt guard (preserve stakeholders, distinguish advocacy from manipulation, redirect manipulative requests), improves pressure robustness without collapsing into hard refusal — strong gains in Claude and GPT-5.4, partial transfer to Qwen 7B and Gemma 4B.

**Routing:** CCC + cyber eval-harness patterns — pressure-robustness dimension for agent eval; Pareto-Trace-style redirect guard as an inference-time layer. Wiki/brief only.

[Source: arXiv:2608.09485]
