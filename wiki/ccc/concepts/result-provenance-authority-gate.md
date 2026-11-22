---
title: "Result provenance and the authority gate"
type: concept
related:
  - sources/arxiv-vibe-trading-agent-native-trading-2611.24845.md
  - entities/tools/vibe-trading.md
  - concepts/assay-content-addressed-evidence-graphs.md
  - concepts/authorization-to-effect-closure.md
  - concepts/agent-approval-laundering-transitive-effects.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: what must a result carry so that it can be trusted later and acted on safely?

Synthesised from one source: `@sources/arxiv-vibe-trading-agent-native-trading-2611.24845.md` (Vibe-Trading, 2611.24845). Architecture pattern; the trading application lives in `@osint-wiki`.

## Narrative

Vibe-Trading is a trading framework, but its harness contribution is general. It keeps four things connected through the research-to-action path.

1. **Result provenance.** Each result keeps its source, temporal scope, configuration and producing run. A number without these is not reusable.
2. **Shared evidence grounding.** Results and their evidence share one store, so a claim can be checked against the artifact that produced it.
3. **Versioned research records.** A research trail can be resumed and reproduced.
4. **An explicit authority gate.** Strategy research is separated from live execution. Action needs an explicit grant.

### The general pattern

Agents that can change external state need two separate things:

- a **research plane** where the agent may compute, test and propose without side effects;
- an **action plane** where a result becomes an effect.

The gate between them is not a prompt instruction. It is a check the harness performs, and it names who authorised the action.

This matches `@concepts/authorization-to-effect-closure.md` and `@concepts/agent-approval-laundering-transitive-effects.md`. It also matches the OSINT wiki's own rule: stage in `briefs/`, never push directly.

Caveat: one technical report. It describes the architecture, not a controlled evaluation of it. [TENTATIVE]

## Snippets

> "Each result retains its source, temporal scope, configuration, and producing run. Shared evidence grounding enables verification, versioned research records support reproducible continuation, and an explicit authority gate separates strategy research from live execution." [Source: arxiv-2611.24845-vibe-trading-towards-agent-native-trading.pdf p.1]
