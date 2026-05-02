---
title: "Frontier Coding Agents Can Now Implement an AlphaZero Self-Play ML Pipeline for Connect Four"
type: source
tags: [llm-agents, coding-agents, alphazero, self-play, ml-engineering]
keywords: [coding-agents, AlphaZero, self-play, Connect-Four, MCTS, reinforcement-learning, code-generation, GitHub]
related:
  - concepts/coding-agents-alphazero.md
maturity: draft
read_status: deep-read
created: 2026-05-02
updated: 2026-05-02
arxiv: "2604.25067"
---

## Raw Concept

- Original title: Frontier Coding Agents Can Now Implement an AlphaZero Self-Play Machine Learning Pipeline For Connect Four That Performs Comparably to an External Solver
- Type: PDF (arXiv preprint)
- Location: cemini-librarian:/opt/cemini-bulk/research/Frontier Coding Agents Can Now Implement an AlphaZero Self-Play Machine Learning Pipeline For Connect Four That Performs Comparably to an External Solver.pdf
- Retrieved: 2026-05-02
- Pages: ~15p
- Read status: deep-read
- GitHub: https://github.com/jsherwood00/C4AI

## Narrative

This paper demonstrates that frontier coding agents (Claude Code, Codex, etc.) can now implement a complete AlphaZero self-play reinforcement learning pipeline — MCTS tree search, neural network training, self-play data generation, iterative improvement loop — for the game Connect Four, with performance comparable to an external solver. The agents handled architecture design, hyperparameter selection, debugging, and iterative refinement with minimal human intervention.

For Cemini/Conductor, this is a capability signal rather than a direct integration target. It validates that coding agents are now capable of implementing the RL training infrastructure that Conductor Path A would require (GRPO training loops, evaluation harnesses, reward modeling). The GitHub repo provides a reference implementation pattern for agent-generated RL pipelines.

The paper also demonstrates the "agent as ML engineer" paradigm: the coding agent doesn't just write code, it runs experiments, interprets results, and adjusts hyperparameters — closing the loop that Conductor's calibration system (Stash → token-prior rebuild → config.yaml) currently handles manually.

## Snippets

- Frontier coding agents successfully implemented a complete AlphaZero pipeline (MCTS + neural net training + self-play + iterative improvement) for Connect Four at performance parity with an external solver. [Source: Frontier Coding Agents...pdf]
- The agent handled architecture design, hyperparameter selection, debugging, and iterative refinement — functioning as an ML engineer rather than just a code generator. [Source: Frontier Coding Agents...pdf]
- GitHub repository at https://github.com/jsherwood00/C4AI contains the full agent-generated implementation. [Source: Frontier Coding Agents...pdf]
