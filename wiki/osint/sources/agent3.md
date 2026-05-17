---
title: "Agent Factories for High Level Synthesis: How Far Can General-Purpose Coding Agents Go"
type: source
tags: [pdf, out-of-scope]
clusters: [out-of-scope]
related:
  - concepts/corpus-overflow-out-of-scope.md
maturity: draft
read_status: skimmed
created: 2026-04-23
updated: 2026-05-16
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — out-of-scope corpus-overflow hub

## Raw Concept

- **Original title**: Agent Factories for High Level Synthesis: How Far Can General-Purpose Coding Agents Go in Hardware Optimization?
- **Author(s)**: Abhishek Bhandwaldar, Mihir Choudhury, Ruchir Puri, Akash Srivastava (IBM Corporation)
- **Type**: PDF
- **Location**: research for cemini/agent3.pdf
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 8p
- **Read status**: skimmed
- **Primary cluster**: out-of-scope
- **All clusters**: out-of-scope

## Narrative

Empirical study of how far general-purpose coding agents (no hardware-specific training) can optimize hardware designs from high-level algorithmic specs. The "agent factory" is a two-stage pipeline that decomposes a design into sub-kernels, solves an Integer Linear Program for area-constrained configurations, then spawns N expert agents to explore cross-function optimizations; scaling 1→10 agents yields a mean 8.27× speedup on HLS-Eval/Rodinia-HLS kernels. Out-of-scope for Cemini: this is hardware-design / High-Level-Synthesis domain work with no transfer path to a software-only trading stack.

## Snippets

*(None — out-of-scope, skimmed only.)*
