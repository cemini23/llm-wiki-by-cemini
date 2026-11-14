---
title: "Command-level sandbox scheduling — schedule commands, not sessions"
type: concept
related:
  - sources/arxiv-metal-sandbox-gpu-coding-agents-apple-silicon-2611.17294.md
  - entities/tools/metal-sandbox.md
  - concepts/agent-vm-sandboxing.md
updated: 2026-11-14
---

## Raw Concept

What question does this page answer: when several coding agents share a small pool of GPU machines, where does the idle time go, and what is the right unit of scheduling? Source: Metal Sandbox (2611.17294).

## Narrative

An agent session is not a busy loop. It alternates between model requests, file edits, compilation, and execution. On one measured Metal session, the GPU was active for 2.32% of the wall clock. The rest is waiting.

Two scheduling choices follow.

**Split commands by resource class.** Parallel commands, such as reading and editing files, need no GPU and can run at once. Serial commands, such as GPU execution or timed work, enter one queue per node. This keeps accelerator use correct without blocking the rest of the session.

**Allow migration of waiting commands.** A command that waits for a busy node can move to an idle node. Metal Sandbox uses a reserve, claim, and commit handshake with command IDs. A lost response cannot start the same command twice. Workspace changes arrive through shared storage; logs stay on the executing node.

Measured gains on four Mac mini M4 nodes:

- 1.68×–2.05× more command throughput under concentrated demand.
- 2.14× estimated sustained throughput for four sessions per node versus one.
- 18.8% less mean tool waiting and 22.3% less batch elapsed time under replay.

The last figure is an estimate from replayed traces, not a live measurement. Treat it as a projection. [TENTATIVE]

**Isolation stays per instance.** Each agent keeps its own workspace and private environment. Restricted file access applies per instance, so a shared scheduler does not become a shared trust boundary.

For Cemini this is a design hint for any local model farm or CI runner that serves several agent lanes. Do not bind a session to one machine. Bind a command, and keep the serial resource under one queue.

## Snippets

> "This combination … has 2.32% of the session [in GPU execution]. Most of the session is spent outside GPU execution." [Source: arxiv-2611.17294-metal-sandbox-isolated-execution-and-command-sch.pdf p.1]

> "Parallel commands can run concurrently, while serial commands share one execution slot per node" [Source: arxiv-2611.17294-metal-sandbox-isolated-execution-and-command-sch.pdf p.1]
