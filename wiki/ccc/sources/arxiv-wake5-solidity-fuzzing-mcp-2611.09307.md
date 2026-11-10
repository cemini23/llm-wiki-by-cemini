---
title: "Wake 5 — Solidity fuzzing with an in-process EVM and an MCP server"
type: source
related:
  - concepts/agent-written-fuzz-harness.md
  - entities/tools/wake5.md
  - concepts/mcp-developer-error-messages-agent-recovery.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Wake 5: A Python Framework for Solidity Testing, Fuzzing, and Static Analysis |
| Author | Josef Gattermayer, Michal Prevrátil (ack3, Czech Technical University in Prague) |
| Type | arXiv paper (cs.SE), 2611.09307 |
| Location | `research to be indexed/ccc/arxiv-2611.09307-wake-5-a-python-framework-for-solidity-testing-f.pdf` |
| Retrieved | 2026-11-10 |
| Pages | 20 |
| Read status | read |

## Narrative

Wake 5 is an open-source Python framework for Solidity testing, fuzzing, and static analysis. Its change from earlier releases is architectural. It replaces the JSON-RPC link to an external node with an in-process EVM (`revm`) bound through PyO3. It also exposes static analysis to language-model agents through an MCP server.

Throughput on the Daedaluzz maze benchmark (153 reachable assertions):

| Tool | Transactions per second |
|------|------------------------|
| Wake 5 | 29,931 |
| Foundry | 30,186 |
| Echidna | 2,600 |

Wake 5 matches Foundry and is 11.5 times faster than Echidna. But in eight-hour campaigns the three tools plateau at medians of 75, 71, and 70 assertions. Their union reaches 93.

The authors analyse why. Wake's integer generator places 51% of its probability mass below 2^32. The guard constants sit below 2^32. So once shallow assertions are exhausted, **the generator prior, not the engine, sets the hit rate**.

An agent-written harness reached all 153 assertions in each of five campaigns, in 33 to 79 minutes, executed by Wake. The agent moved guard satisfaction into an SMT solver and navigation into breadth-first search. The fuzzer became an executor of candidates, not a search engine.

A separate ablation studied static-analysis tools inside an agentic audit of a production Go codebase. Three models, 134 paired cases. Recall did not improve for any model. Precision improved for all three. Model cost rose by up to 12.7%.

The paper also names three failure modes of agent-written harnesses: correlated oracles, non-deterministic completion, and priority inversion.

This is the clearest 2026 example of a division of labour: **the model writes the harness, the fast engine executes it.** The fuzzer's role moves from search to execution.

## Snippets

> "Once shallow assertions are exhausted, the generator prior rather than throughput bounds every tool." [Source: arxiv-2611.09307-wake-5-a-python-framework-for-solidity-testing-f.pdf p.1]

> "A harness written by a language-model agent, which derives inputs with a constraint solver, reached all 153 assertions in each of five campaigns executed by Wake, in 33 to 79 minutes." [Source: arxiv-2611.09307-wake-5-a-python-framework-for-solidity-testing-f.pdf p.1]

> "static-analysis tools improved recall for none of three models, raised precision for all three, and increased language-model cost by up to 12.7%." [Source: arxiv-2611.09307-wake-5-a-python-framework-for-solidity-testing-f.pdf p.1]
