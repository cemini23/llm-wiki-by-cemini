---
title: "Wake 5 — Python Solidity testing, fuzzing, and static analysis with an MCP server"
type: entity
related:
  - concepts/agent-written-fuzz-harness.md
  - sources/arxiv-wake5-solidity-fuzzing-mcp-2611.09307.md
  - entities/tools/claude-code.md
updated: 2026-11-10
---

## Raw Concept

Prompted by arXiv 2611.09307 (2026-11-10 ingest). A mature commercial-adjacent security framework that exposes static analysis over MCP, which is the pattern Cemini cares about. No Phase-0 audit has been run; this page records the published claims only.

## Narrative

| Field | Value |
|-------|-------|
| Publisher | ack3 (ACK3 LTD) |
| Language | Python, with an in-process `revm` EVM bound through PyO3 |
| Domain | Solidity testing, property-based fuzzing, static analysis |
| Interface | Python test API, language server, and a Model Context Protocol server |
| Licence | Open source, per the paper's own description [NEEDS VERIFICATION 2026-11-10: exact SPDX id not stated in the pages read] |

Reported properties:

- 29,931 transactions per second on Daedaluzz, matching Foundry (30,186) and 11.5 times Echidna (2,600).
- A bounded block-history window keeps multi-hour campaigns memory-stable.
- Two-phase stateful shrinking.
- Static analysis exposed to agents over MCP; the server exposes static facts only.
- Version-normalising intermediate representation over the Solidity AST, which merges compilation units.

### Why it is in the ccc wiki and not only cybersec

The MCP surface is the ccc-relevant part. Wake 5 shows the pattern **expose a static analyser to an agent, keep execution in the engine**. The agent writes the harness; the framework only executes and replays.

### Adoption posture

REFERENCE only. Cemini has no Solidity workload. Use it as a design exemplar for agent-facing analysis servers, and only revisit if a contract-audit task appears.

## Snippets

> "exposes its static analysis to language-model agents through a Model Context Protocol (MCP) server" [Source: arxiv-2611.09307-wake-5-a-python-framework-for-solidity-testing-f.pdf p.1]
