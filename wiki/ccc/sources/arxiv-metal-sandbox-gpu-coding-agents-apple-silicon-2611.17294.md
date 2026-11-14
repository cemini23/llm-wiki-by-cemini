---
title: "Metal Sandbox — isolated execution and command scheduling for GPU coding agents on Apple Silicon"
type: source
related:
  - concepts/command-level-gpu-sandbox-scheduling.md
  - entities/tools/metal-sandbox.md
  - entities/tools/harbor.md
  - concepts/agent-vm-sandboxing.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon |
| Author | Haozhe Wang, Lina Chen, Fanqi Wan, Qi Han, Yinmin Zhang, Zheng Ge, Daxin Jiang, Junchi Yan (SJTU, Beijing Zhongguancun Academy, StepFun) |
| Type | arXiv preprint, 2611.17294 |
| Location | `research to be indexed/ccc/arxiv-2611.17294-metal-sandbox-isolated-execution-and-command-sch.pdf` |
| Retrieved | 2026-11-14 |
| Pages | 16 |
| Read status | read |

## Narrative

Metal Sandbox is infrastructure for GPU coding agents that run on Macs. The problem is idle capacity. An agent session moves between model requests, file work, compilation, and GPU execution. In one measured `metal_nbody` session, Apple Instruments recorded 44.0 seconds of GPU activity over 31.6 minutes, or 2.32% of the session. Most of the rollout waits.

The design has three parts:

1. **Restricted per-instance file access.** Each agent keeps its own workspace and private development environment.
2. **Native command execution.** Commands run on the host, not in an emulator.
3. **Command-level scheduling across Macs.** Parallel commands, such as file inspection and editing, run at once. Serial commands, such as GPU or timed work, share one execution slot per node. An eligible waiting command can migrate to a free Mac and return its result to the original agent.

Migration uses a reserve, claim, and commit handshake with command IDs, so a lost response does not start a command twice. Workspace changes travel through shared storage; logs and temporary files stay on the target node.

Measured results, on four Mac mini M4 nodes with 32 GiB each:

- 1.68×–2.05× gain in command throughput under concentrated demand.
- Sixteen static agent traces give an estimated 2.14× sustained throughput for four sessions per node versus one.
- Replay under dynamic scheduling cuts mean tool waiting by 18.8% and batch elapsed time by 22.3%.

Integration with **Harbor** gives task execution, automatic verification, and rollout collection through one workflow. The code is open source.

For Cemini the transferable idea is the unit of scheduling. The project schedules **commands**, not whole sessions. A shared serial slot per node keeps GPU work correct, and migration fills idle capacity without moving the agent.

## Snippets

> "Apple Instruments' Metal System Trace records 44.0 seconds of GPU activity over 31.6 minutes, or 2.32% of the session." [Source: arxiv-2611.17294-metal-sandbox-isolated-execution-and-command-sch.pdf p.1]

> "Replaying these measured traces under dynamic scheduling reduces mean tool waiting by 18.8% and batch elapsed time by 22.3%" [Source: arxiv-2611.17294-metal-sandbox-isolated-execution-and-command-sch.pdf p.1]
