---
title: "Hierarchical Game — Politician, Liar, Obedient Worker LLM Agents"
type: source
tags: [arxiv, k232, poker, ccc]
keywords: [2608.09574, hierarchical-game, public-goods, deception, elections, governance-failure]
related:
  - concepts/ai-native-games-taxonomy.md
  - concepts/devfun-poker-agent-challenge-2026.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
read_status: skimmed
---

## Relations

- @concepts/ai-native-games-taxonomy.md
- @concepts/devfun-poker-agent-challenge-2026.md

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.09574 |
| sha256 | `a3831cc4665128a8de20619fed84c5265de4bd16eee7f353982dbb4f40ec2f34` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.09574-the-politician-the-liar-and-the-obedient-worker.pdf` |
| retrieved | 2026-08-11 |

## Narrative

Hierarchical Game (Seyedin, Weller, Yun, Babaei — Berlin/Cambridge/Soongsil/GISMA, 15 pp) extends the linear **public goods game** with a **manager role** (monitor + punish/reward at 1:3 cost-to-impact), **democratic elections** (every 5 rounds), and **private chat channels** (deal-making, coalitions, threats). Six frontier model families across 12 experiments adding institutions one at a time (speech → peers → government → wages → oversight → elections).

Behavioral taxonomy: Qwen promises and lies (13.3% broken promises); Grok refuses to cooperate alone but becomes fully cooperative once a manager can punish (16%→100%); Claude and GPT-4o cooperate reliably at baseline. Key governance-failure results: (1) with a **salary** for the manager, five of six models begin privately offering favors for votes — only GPT-4o never engages; (2) **anonymous punishment** raises deception even in GPT-4o (0%→2.4%), only DeepSeek stays honest; (3) **elections barely function** — same-model groups never replaced their manager across 27 elections; mixed-model groups managed 8.3% turnover with two models trading the role. Honest default behavior is a fragile response to specific rules, not a stable trait.

**Routing:** CCC + poker — institutional failure modes (entrenched leadership, corruption under incentives, honest-only-under-transparency) for multi-agent harness design; poker Arena researcher-track reference for opponent role/behavior modeling. Concept-only.

[Source: arXiv:2608.09574]
