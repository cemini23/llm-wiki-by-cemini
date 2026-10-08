---
title: "Latent Space — Can a cloud-native harness make agents reliable beyond the desktop? (2026-10-07)"
type: source
tags: [source, k285, agents, harness, cloud-native, ccc]
keywords: [stacklok, mecatl, toolhive, kubernetes, cloud-native-harness, ai-gateway, mcluckie, beda, pi-harness]
related:
  - concepts/k285-feeds-wave.md
  - concepts/agent-harness-auditing-a2e.md
maturity: draft
created: 2026-10-08
updated: 2026-10-08
read_status: read
---

## Relations

- @concepts/k285-feeds-wave.md
- @concepts/agent-harness-auditing-a2e.md

## Raw Concept

| Title | Can a Cloud-Native Harness Make Agents Reliable Beyond the Desktop? |
| Source | Latent Space (Substack) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-latent-space-2026-10-07-can-a-cloud-native-harness-make-agents-reliable.md` |
| Retrieved | 2026-10-07 |
| URL | https://www.latent.space/p/stacklok |
| Tier | free (RSS) |
| cross-wiki | ccc-wiki |
| read-status | read |

## Narrative

**Stacklok** — founded by two Kubernetes creators, **Craig McLuckie** and **Joe Beda** — is betting that agent harnesses need the Kubernetes treatment. The article contrasts today's **desktop-first harnesses** (Claude Code, Codex, Cursor) with a **cloud-native harness**.

### The core claim

In a desktop-first harness, the **agent loop, local execution, and session state begin in the same process**, and session data sits as **JSONL files on disk**. Stacklok argues that is why enterprise agent reliability is hard: you cannot quiesce an agent, isolate execution, or govern its state.

### Mecatl — the cloud-native harness

**Mecatl** (an Aztec word for "cord"; open source) **separates the agent loop from execution**: the loop is independent of the client, model provider, state store, and execution environment. Tool calling and bash move out of the loop; session management and memory leave disk for manageable systems.

Their framing: *"interactions you have with an agent while you're working for an enterprise belong to that enterprise"* — govern them like email.

### ToolHive + the AI Gateway

- **ToolHive** — open-source platform for running and governing **MCP servers** (Docker → Kubernetes gateway, registry, operator).
- **AI Gateway** (not yet open source) — **access control, budgets, reporting, provider routing**. Notably, it does **not** choose a model by task; Stacklok argues **semantic routing belongs in the harness**, where the context is.

### Why it matters here

Two transferable ideas:

1. **Separate the agent loop from execution and state.** That is the same lesson as the K283 "interpreter over tool-loop" and the K284 Recursive Game Creator's coding-native player — the loop should not own the sensitive operations.
2. **The harness is where routing context lives**, not the gateway. Directly relevant to the wiki's `/route` design.

Also names **Pi**, the "minimal agent harness" the wiki already tracks. Route: CCC. **No `/route` swap.**

## Snippets

> "What if we take that and we separate that out from the more sensitive operations, like tool calling and bash, and then also separate out things like session management and memory, so that these things are no longer stored as JSONL files sitting on disk." [Source: newsletter-rss-latent-space-2026-10-07-can-a-cloud-native-harness-make-agents-reliable.md]

> "We prefer to see the semantic-routing model choice happening in an intelligent system that's honed in the harness, because there's just more context there." [Source: newsletter-rss-latent-space-2026-10-07-can-a-cloud-native-harness-make-agents-reliable.md]
