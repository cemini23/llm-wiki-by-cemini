---
title: "Agent Identity URI Scheme: Topology-Independent Naming and Capability-Based Discovery"
type: source
tags: [pdf, k49, llm-agents]
clusters: [llm-agents]
related:
  - concepts/llm-agent-systems.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-17
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research in the Cemini corpus

## Raw Concept

- **Original title**: Agent Identity URI Scheme: Topology-Independent Naming and Capability-Based Discovery for Multi-Agent Systems
- **Author(s)**: Roland R. Rodriguez, Jr. (Independent Researcher) — arXiv:2601.14567v1
- **Type**: PDF
- **Location**: research for cemini/forex 2 4:4.pdf (filename `forex` is a misnomer — content is agent identity/discovery)
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 19p
- **Read status**: deep-read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents

## Narrative

The paper identifies a structural flaw in multi-agent systems: **agent identity is bound to network location**. When an agent migrates providers, scales across instances, or federates across organizations, URI-based identities break references, fragment audit trails, and force centralized coordination — the same naming-vs-addressing conflation Saltzer flagged in 1982 and that DNS later fixed for network hosts. Existing approaches each fail one axis: FIPA's Directory Facilitator assumes a single centralized platform; the A2A protocol binds identity to Agent Card URIs; Decentralized Identifiers (DIDs) lack capability semantics for discovery.

The proposal is the **`agent://` URI scheme**, decoupling identity from topology via three orthogonal components: a **trust root** (e.g. `acme.com`) establishing organizational authority; a **hierarchical capability path** (e.g. `/workflow/approval`) enabling semantic discovery; and a **sortable unique identifier** (ULID-style) for stable reference. Capability-based discovery works through **DHT key derivation** from the capability path, so queries return agents by *what they do* rather than *where they are*, with O(log N) lookup and no central registry. **PASETO** tokens issued by trust roots cryptographically bind capability claims to identity, verifiable with only the trust root's public key. The four-axis evaluation: the grammar covers **100% of 369 production tools** across LangChain, CrewAI, MCP, AutoGen, and smolagents with zero namespace collision; trust-scoped prefix matching achieves **F1=1.0 across 10,000 agents**; migration provably preserves identity with O(log N) resolution; and all URI operations complete in **under 5 microseconds**.

**Cemini relevance**: directly relevant to the conductor — a topology-independent identity and capability-based discovery layer is the substrate for routing queries to wiki/agent services without hardcoding network locations or central registries.

## Snippets

> "Multi-agent systems face a fundamental architectural flaw: agent identity is bound to network location... We propose the agent:// uri scheme, which decouples identity from topology through three orthogonal components: a trust root establishing organizational authority, a hierarchical capability path enabling semantic discovery, and a sortable unique identifier providing stable reference." [Source: forex 2 4:4.pdf p.1]

> "The capability path grammar represents 100% of 369 production tools from LangChain, CrewAI, MCP, AutoGen, and smolagents with zero namespace collision." [Source: forex 2 4:4.pdf p.1]
