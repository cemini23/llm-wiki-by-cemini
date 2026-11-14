---
title: Metal Sandbox — isolated execution and command scheduling for Mac GPU agents
type: entity
related:
  - sources/arxiv-metal-sandbox-gpu-coding-agents-apple-silicon-2611.17294.md
  - concepts/command-level-gpu-sandbox-scheduling.md
  - entities/tools/harbor.md
  - concepts/agent-vm-sandboxing.md
updated: 2026-11-14
---

## Raw Concept

What prompted this page: the 2026-11-14 ingest of Metal Sandbox (2611.17294). The tool is open source and directly relevant to local Apple Silicon agent runs, so it gets a page rather than a paragraph in a concept.

## Narrative

| Field | Value |
|-------|-------|
| Repository | `github.com/WangHaoZhe/metal-sandbox` |
| Harbor fork | `github.com/WangHaoZhe/harbor` |
| License | unknown [NEEDS VERIFICATION 2026-11-14] |
| Hardware tested | four Mac mini M4 nodes, 32 GiB each |
| Status in this wiki | awareness; no Phase-0 audit |

The tool serves three functions:

1. **Per-instance file isolation.** Each agent keeps its own workspace and private development environment. Absolute paths match across nodes, so shared storage and HOME line up.
2. **Native command execution.** Commands run on macOS directly, which keeps Apple tooling and Metal available.
3. **Command-level scheduling.** Parallel commands run at once. Serial commands, such as GPU work and timed runs, share one slot per node. A waiting command can migrate to an idle node and return its output to the original agent.

The migration protocol is reserve, claim, commit, with command IDs and a source-node check before commit. This prevents a duplicate start when a response is lost.

Reported results: 1.68×–2.05× command throughput under concentrated demand, and 18.8% lower mean tool waiting plus 22.3% lower batch elapsed time in a replay of sixteen traces. The replay figures are projections.

Why it matters here: Cemini runs local lanes on Apple hardware. A small cluster of Macs with one serial GPU queue per node is a plausible way to serve several agent sessions without a second datacentre. The isolation model is weaker than a VM. It restricts file access per instance and does not claim a hardware boundary. Treat it as process-level isolation, not a Tier-2 sandbox.

## Snippets

> "Each agent retains its workspace and private development environment." [Source: arxiv-2611.17294-metal-sandbox-isolated-execution-and-command-sch.pdf p.1]

> "Serial commands share one execution slot per node; eligible waiting commands can migrate to available Macs and return results to the original agent." [Source: arxiv-2611.17294-metal-sandbox-isolated-execution-and-command-sch.pdf p.1]
