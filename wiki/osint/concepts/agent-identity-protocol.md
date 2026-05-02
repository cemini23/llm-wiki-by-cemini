---
title: Agent Identity Protocol (IBCT)
type: concept
tags: [concept, audit, cryptography, mcp, agent-authorization, cemini-internal]
keywords: [IBCT, invocation-bound capability tokens, verifiable delegation, biscuit tokens, agent authorization, aip]
related:
  - concepts/cryptographic-audit-trail.md
  - sources/3-29-research-6.md
  - entities/frameworks/fastmcp.md
  - entities/frameworks/langgraph.md
  - concepts/ip-sale-readiness.md
  - concepts/scatter-gather-topology.md
maturity: draft
created: 2026-05-01
updated: 2026-05-01
---

## Relations

- @concepts/cryptographic-audit-trail.md — IBCT extends the existing audit trail with agent-to-agent authorization tokens; completion blocks map onto the SHA-256 chain in `services/audit/chain.py`
- @sources/3-29-research-6.md — K15 source: Paper 5 (AIP: Agent Identity Protocol, Prakash) promoted to this concept page
- @entities/frameworks/fastmcp.md — IBCT tokens pass through FastMCP tool invocations via X-AIP-Token header binding; pairs with side_effects enum for defense-in-depth
- @entities/frameworks/langgraph.md — Orchestrator-generated IBCTs define execution scope before LangGraph agent delegation
- @concepts/ip-sale-readiness.md — cryptographically verifiable per-trade authorization chains are the exact artifact an IP acquirer's due diligence would examine
- @concepts/scatter-gather-topology.md — IBCT authorization gates each agent-to-agent delegation in the topology

## Raw Concept

Promoted from K15 deep-read of `@sources/3-29-research-6.md` (Paper 5: "AIP: Agent Identity Protocol for Verifiable Delegation" by Prakash et al.). The paper introduces Invocation-Bound Capability Tokens (IBCTs) to resolve the critical lack of authentication and authorization within existing MCP and A2A frameworks. The protocol fuses identity verification, holder-side attenuated authorization, and provenance binding into an append-only cryptographic token chain, providing mathematical proof of delegation without centralized infrastructure.

## Narrative

### The gap IBCT fills

MCP and A2A have no native mechanism for an orchestrator to delegate authority to a sub-agent with mathematically enforced limits. When the LangGraph Orchestrator tells the Execution Agent "execute a trade," nothing prevents the Execution Agent from exceeding its authorized scope — whether through prompt injection, model hallucination, or a compromised agent. Standard MCP tool calls carry no cryptographically verifiable proof of *who* authorized *what* with *which* constraints.

IBCT solves this with a three-component token chain:

1. **Attenuation Block** — the Orchestrator generates a Biscuit token (Ed25519-signed) defining the exact scope and budget of the delegated operation (e.g., max spend $500, ticker TSLA only, venue Kalshi only). The Execution Agent *cannot* alter or bypass these Datalog-defined caveats.
2. **Invocation Block** — the Execution Agent presents the token to the FastMCP server during tool invocation. The server evaluates the embedded Datalog policy against the requested tool parameters and rejects unauthorized or over-budget calls *before* the payload reaches execution logic.
3. **Completion Block** — appended after execution, permanently recording the result hash, execution status, and resource costs. The completed token chain is published to a Redis Stream and persisted to PostgreSQL.

### Why Biscuit tokens (not JWT)

Biscuit tokens support **holder-side attenuation**: the holder of a token can derive a new token with *fewer* capabilities but cannot add new ones. This is the mathematical property that makes IBCT work — the Orchestrator issues a token with full authority, the Execution Agent can only *narrow* that authority before presenting it. Standard JWTs lack attenuation; they are either valid or invalid, with no mechanism for the holder to add runtime constraints.

Datalog is the policy language. Caveats are expressed as Datalog predicates (e.g., `spend_limit($amount) :- $amount <= 500`) evaluated at the FastMCP server during tool invocation. The server holds the root public key and verifies the full token chain before executing.

### aip:key — Self-certifying ephemeral identities

The protocol defines `aip:key` as a self-certifying identity scheme: ephemeral sub-agents generate an Ed25519 keypair on the fly, authenticating their actions without DNS, PKI, or external infrastructure. The public key *is* the identity. This is the only identity mechanism Cemini would need — `aip:web` (DNS-based resolution) adds unnecessary DevOps overhead for internal VPS agents.

### Integration with existing audit trail

The existing SHA-256 audit chain in `services/audit/chain.py` records *what happened*. IBCT adds *who authorized it under what constraints*. Together they provide:

- **Ex-ante**: IBCT Datalog policies prevent unauthorized execution (the tool call is rejected before side effects occur)
- **Ex-post**: Completion blocks + SHA-256 chain provide immutable post-execution record

The IBCT token chain itself becomes the cryptographic proof that a specific trade was authorized by the multi-agent debate consensus. Embedding the Ed25519 signature chain into the OpenTimestamps Merkle tree payload ensures the authorization history is cryptographically undeniable.

### Implementation path

Per the source's verdict table: ~27 total engineer-hours estimated across four ADOPT components:
- Verifiable delegation (IBCT token generation + Biscuit integration): 12h
- Completion blocks (Redis Stream publication + PostgreSQL persistence): 6h
- Ephemeral auth via aip:key (Ed25519 keypair generation per sub-agent): 6h
- Header binding middleware (FastAPI `Depends()` intercepting X-AIP-Token): 3h

Dependency: `biscuit-python` (Rust-backed Python cryptography library) must be compiled into Alpine-based Docker images. This is the primary integration friction — Biscuit's Rust toolchain adds build complexity to the otherwise pure-Python container images.

## Snippets

**S1** — Source §2 (Holder-side Attenuation): "The protocol establishes the Holder-side Attenuation & Verifiable Delegation architectural pattern. When the LangGraph Orchestrator delegates a trade execution to the specialized Execution Agent, it must mathematically enforce limits—such as a maximum spend of $500—that the Execution Agent cannot alter or bypass." [Source: 3_29 research 6.docx, Paper 5 §2]

**S2** — Source §3 (Completion Blocks): "This block is appended to the token chain by the executing agent to permanently record the result hash, execution status, and resource costs associated with the operation. This logic can be adapted so that upon successful trade execution, the FastMCP server signs a Completion Block and publishes the entire cryptographic chain to a Redis Stream. A background Polars worker then persists this completed IBCT chain to the PostgreSQL database, creating an immutable, cryptographically secure ledger of every single action taken by the AI." [Source: 3_29 research 6.docx, Paper 5 §3]

**S3** — Source §4 (aip:key Self-certifying Identities): "This tooling allows ephemeral sub-agents to generate an Ed25519 keypair on the fly, authenticating their actions without requiring complex Domain Name System (DNS) configurations or Public Key Infrastructure (PKI). Implementing this workflow enhancement takes approximately six hours but provides a massive value add for the IP sale. It mathematically proves to potential buyers that the system is perfectly secure, fully auditable, and entirely self-contained on a single virtual private server without relying on external dependencies." [Source: 3_29 research 6.docx, Paper 5 §4]

**S4** — Source §5 (X-AIP-Token Header Binding): "The specification mandates passing the IBCT via the X-AIP-Token header during MCP invocations. FastMCP can easily implement this through a FastAPI dependency injection (Depends()) to intercept the header, evaluate the embedded Datalog policy against the requested tool parameters, and automatically reject unauthorized or over-budget LLM tool calls before the payload even reaches the execution logic." [Source: 3_29 research 6.docx, Paper 5 §5]

**S5** — Source §7 (DNS-based aip:web rejection): "The protocol's DNS-based identity resolution mechanism (aip:web), which requires hosting .well-known endpoints and manually managing DNS TXT records, must be skipped, as it adds unnecessary DevOps overhead compared to the elegant simplicity of the self-certifying aip:key approach for internal VPS agents." [Source: 3_29 research 6.docx, Paper 5 §7]
