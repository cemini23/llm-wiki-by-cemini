---
title: "AIP: Agent Identity Protocol for Verifiable Delegation Across"
type: source
tags: [pdf, rl-marl, llm-agents, crypto, audit-security]
clusters: [rl-marl, llm-agents, crypto, audit-security]
related: []
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

*(Cross-references will be added in Phase 2.)*

## Raw Concept

- Original title: AIP: Agent Identity Protocol for Verifiable Delegation Across (full subtitle truncated in extract)
- Authors: Sunil Prakash (ISB — Indian School of Business)
- Affiliation: Indian School of Business
- Type: PDF, research paper (preprint)
- Location: research for cemini/protocol 5 3:29.pdf
- Length: ~25 pages
- Retrieved: 2026-04-23
- Publication date: 2025
- Read status: deep-read
- Primary cluster: audit-security
- All clusters: rl-marl, llm-agents, crypto, audit-security

## Narrative

AIP defines an Agent Identity Protocol using Inter-Agent Bearer Capability Tokens (IBCTs). Tokens are Biscuit-based with embedded Datalog authorization logic. The protocol lets agent A delegate a bounded subset of its authority to agent B (with attenuation on scope, time, and counter) such that downstream services can verify B's authority by evaluating the Biscuit+Datalog block without calling back to A. The paper builds on SPIFFE/SVID identity for the root identity layer.

An empirical section scans 2,000 public MCP servers and finds **0% implement authentication** — a striking industry snapshot showing the MCP ecosystem has no auth story today. The paper positions AIP as the missing delegation layer for agent-to-agent and agent-to-tool calls. The Biscuit+Datalog combination is sensible (Datalog authorization is well-studied), and attenuation semantics are formally defined.

For Cemini the relevance is architectural: if the suite deploys MCP servers or agent-to-agent delegation at any scale, it needs an authentication/authorization layer, and AIP-style Biscuit tokens are a credible approach. ISB is not a top-tier CS security venue so the peer-review floor is moderate, but the engineering content is solid and the 2,000-server empirical scan is a valuable artifact.

## Key findings

- AIP = Biscuit-based IBCTs with Datalog authorization for agent delegation.
- Built on SPIFFE/SVID root identity.
- Formal attenuation semantics (scope, time, counter).
- Empirical scan: **0 of 2,000 public MCP servers implement authentication**.
- Applicable to Cemini if MCP or agent-to-agent delegation is deployed at scale.

## Snippets

- **abstract** — "AIP defines an Agent Identity Protocol for verifiable delegation using Inter-Agent Bearer Capability Tokens" — the contribution.
- **empirical** — "We scanned 2,000 public MCP servers; none implement authentication" — industry snapshot.
- **design** — Biscuit + Datalog gives offline verifiability; attenuation is formally specified.
