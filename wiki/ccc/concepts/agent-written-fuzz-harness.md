---
title: "Agent-written fuzz harnesses — the model searches, the engine executes"
type: concept
related:
  - sources/arxiv-wake5-solidity-fuzzing-mcp-2611.09307.md
  - entities/tools/wake5.md
  - concepts/mcp-developer-error-messages-agent-recovery.md
  - concepts/schema-free-cli-tool-eval.md
updated: 2026-11-10
---

## Raw Concept

Question this page answers: when a language model writes the fuzz harness, what does the fuzzer still do?

Synthesised from `@sources/arxiv-wake5-solidity-fuzzing-mcp-2611.09307.md`.

## Narrative

Wake 5 is a Python framework for Solidity testing, fuzzing, and static analysis. It runs an EVM in-process instead of over JSON-RPC, and exposes its static analysis to agents through an MCP server.

Throughput is not the binding constraint. Wake 5 reaches 29,931 transactions per second, on par with Foundry at 30,186 and 11.5 times faster than Echidna at 2,600. Yet in eight-hour campaigns the three tools plateau at medians of 75, 71, and 70 assertions out of 153.

The cause is the **generator prior**. Wake places 51% of its integer probability mass below 2^32, and the guard constants sit below 2^32. Once the shallow guards are satisfied, more throughput finds nothing new.

An agent-written harness reached all 153 assertions in each of five campaigns, in 33 to 79 minutes. The agent moved guard satisfaction into an SMT solver and navigation into breadth-first search. The fuzzer only executed candidates.

### The division of labour

| Party | Job |
|-------|-----|
| Model | Find the structure of the problem; write the generator strategy |
| Engine | Execute candidates fast and deterministically |
| Verifier | Decide pass or fail |

This is the same split BOXBOX uses and the same split the wiki already assumes for architect and implementer lanes.

### Three failure modes to expect

- **Correlated oracles** — the harness's test oracle shares the bug in the implementation.
- **Non-deterministic completion** — the harness passes on some runs and not others, so the result is a coin flip.
- **Priority inversion** — the generator optimises a proxy that is easier than the real goal.

### Secondary result

In an agentic audit of a production Go codebase (three models, 134 paired cases), static-analysis tools did not raise recall for any model, raised precision for all three, and raised model cost by up to 12.7%. Add tools for precision, not coverage, and expect to pay.

## Snippets

> "once shallow assertions are exhausted, the generator prior rather than throughput bounds every tool." [Source: arxiv-2611.09307-wake-5-a-python-framework-for-solidity-testing-f.pdf p.1]

> "argue that the fuzzer's role is shifting from search to execution." [Source: arxiv-2611.09307-wake-5-a-python-framework-for-solidity-testing-f.pdf p.1]
