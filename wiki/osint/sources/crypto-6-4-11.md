---
title: "Governing Dynamic Capabilities: Cryptographic Binding and Reproducibility Verification for AI Agent Tool Use"
type: source
tags: [pdf, k49, llm-agents]
clusters: [llm-agents]
related:
  - concepts/llm-agent-systems.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-16
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research in the Cemini corpus

## Raw Concept

- **Original title**: Governing Dynamic Capabilities: Cryptographic Binding and Reproducibility Verification for AI Agent Tool Use
- **Author(s)**: Ziling Zhou (Genupixel Technology Pte. Ltd.). arXiv:2603.14332v2, Mar 2026.
- **Type**: PDF
- **Location**: research for cemini/crypto 6 4:11.pdf
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 23p
- **Read status**: deep-read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents

## Narrative

This paper addresses a **governance vacuum** in AI-agent ecosystems: agents that dynamically acquire tools (via MCP, A2A) and orchestrate sub-agents have no security layer that can verify *what* an agent is capable of, *whether* it executed what it claims, or *what actually happened* in a multi-agent interaction. The diagnosis is a missing architectural distinction — **capability-context separation**: inside a transformer's forward pass tool definitions and user context are indistinguishable token sequences, but at the orchestration layer tool definitions (the capability envelope, which changes rarely) and runtime context (which changes per interaction) have different security semantics. Conflating them enables **silent capability escalation** — agents acquiring tools without invalidating credentials.

From this principle the author derives three **Agent Governance Requirements**: **G1 capability integrity**, **G2 behavioral verifiability**, **G3 interaction auditability**, and shows via a 12-attack analysis that all three must hold simultaneously. Two structural results: the **Chain Verifiability Theorem** (one unverifiable interior agent breaks end-to-end verification for all downstream nodes) and the **Bounded Divergence Theorem** (replay verification becomes a probabilistic safety certificate, ϵ ≤ 1 − α^(1/n)). Two crypto-agnostic instantiations are validated: a basic one (Ed25519, SHA-256, hash chains; 97 µs verify) and an enhanced one (BBS+ selective disclosure, Groth16 DV-SNARK; 13.8 ms verify). A 9-model/7-provider study finds **5.8× variance in inference determinism**; end-to-end runs over 5–20 agent pipelines show **<0.02% governance overhead** and real-time detection of 7 attack scenarios with zero false positives.

**Cemini relevance**: directly applicable to the **conductor** — the MCP router that fans queries across wikis and tools is exactly the multi-agent, dynamic-tool-acquisition setting this paper governs. The capability-bound certificate + tamper-evident interaction ledger pattern is a candidate design for verifiable, auditable conductor tool-use, especially as it transacts with the prod stack.

## Snippets

> "no existing security layer can verify what an agent is capable of, whether it executed what it claims, or what actually happened in a multi-agent interaction. We trace this governance vacuum to a missing architectural distinction: the capability-context separation." [Source: crypto 6 4:11.pdf p.1]

> "the Chain Verifiability Theorem, establishing that behavioral verification is a chain property (one unverifiable interior agent breaks end-to-end verification for all downstream nodes), and the Bounded Divergence Theorem, which transforms replay-based verification into a probabilistic safety certificate (ϵ ≤ 1 − α^1/n)." [Source: crypto 6 4:11.pdf p.1]
