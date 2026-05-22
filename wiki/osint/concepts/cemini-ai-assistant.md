---
title: Cemini AI — user-facing assistant on the wiki-RAG brain
type: concept
tags: [concept, architecture, cemini-ai, chatbot, rag, deepseek, llm-agents, planned-not-built]
keywords: [cemini-ai, assistant, chatbot, wiki-rag, deepseek, kb-server, conductor, action-confirmation, internal-first, gdpr]
related:
  - entities/infrastructure/cemini-egress-fi.md
  - entities/infrastructure/deepseek-api.md
  - concepts/kb-server-retrieval-scaling.md
  - concepts/librarian-server-architecture.md
  - entities/tools/nofx-ai-os.md
  - sources/arxiv-self-healing-llm-agents-2605.06737.md
  - concepts/code-as-agent-harness.md
  - sources/arxiv-code-as-agent-harness-survey-2605.18747.md
  - concepts/polymarket-copy-trading-strategy.md
  - sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md

maturity: draft
created: 2026-05-19
updated: 2026-05-22
---

## Relations

- @entities/infrastructure/cemini-egress-fi.md — recommended host for the assistant gateway during the internal-only phase (Finnish Hetzner box, near-idle, librarian-class spec)
- @entities/infrastructure/deepseek-api.md — the LLM brain; already wired into the production stack, OpenAI-compatible so provider-swappable
- @concepts/kb-server-retrieval-scaling.md — the wiki-RAG retrieval layer the assistant queries for its differentiating knowledge
- @concepts/librarian-server-architecture.md — the librarian (kb-server + stash) that supplies static wiki RAG plus episodic memory; the assistant is a new consumer of it
- @sources/arxiv-self-healing-llm-agents-2605.06737.md — failure detection + corrective replanning patterns for long-running assistant sessions
- @concepts/code-as-agent-harness.md — harness-interface model for executable/verifiable assistant actions
- @sources/arxiv-code-as-agent-harness-survey-2605.18747.md — primary survey for harness-interface + verification layers
- @concepts/polymarket-copy-trading-strategy.md — K57: disclose hybrid CLOB copy limits in assistant answers (see egress-fi posture)
- @sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md — @spottr_trade latency framing

## Raw Concept

`[PROPOSAL 2026-05-19]` User question: add **"Cemini AI"** to the CeminiSuite — a bot the user (later, external users) can converse with, using DeepSeek plus the Cemini wikis as the "brain", so it is meaningfully differentiated from a vanilla DeepSeek deployment.

This page is the architecture-of-record for that proposal. It is **planned, not built**. It synthesizes the 2026-05-19 research conversation; the executable deliverable is `briefs/2026-05-19_cemini-ai-assistant.md`, shipped to cemini-prod for server-Claude review.

## Narrative

### The finding — most of the brain already exists

"DeepSeek + wikis as the brain" is not a new system to build; it is the architecture the production stack already runs internally:

| Layer | Status | Where |
|---|---|---|
| LLM brain | live | DeepSeek-V4 (`flash` + `pro`), OpenAI-compatible — @entities/infrastructure/deepseek-api.md |
| Wiki as knowledge | live | kb-server, ~943-vector RAG over the wiki, MCP `:3838` — @concepts/kb-server-retrieval-scaling.md |
| Episodic memory | live | stash (pgvector) on the librarian — @concepts/librarian-server-architecture.md |
| Query routing | designed | conductor — classifies a query, routes model plus tools |
| Live tools | live | 130+ MCP tools (polymarket / kalshi / alpaca / EDGAR and others) |

What is missing is only the **user-facing surface**. The production analyst orchestrator (4 LangGraph nodes) is internal — no human converses with it. Cemini AI is that missing chat layer, not a new brain.

### What makes it differentiated

The user's instinct — that the wikis are what make this unique — is correct. A vanilla DeepSeek knows generic finance. Cemini AI is differentiated by three assets a competitor cannot copy:

1. **The proprietary wikis** — curated OSINT/finance plus cybersecurity research, served as RAG. The moat.
2. **stash episodic memory** — it remembers prior findings and conversations; generic chatbots are amnesiac.
3. **Live tool access** — it can pull a real quote or a Polymarket order book mid-conversation.

### Scope (user decisions, 2026-05-19)

- **Capability**: answer questions **and propose actions** — the bot may *draft* an action (for example a trade) but a human confirms before execution. This honors the LLM corruption-ceiling safety gate: the bot never holds execution credentials; a proposal becomes a structured "confirm card", and only explicit confirmation routes it to an execution tool.
- **Audience**: eventually **external users / customers**, but **not for a while — no users yet**. The build is therefore internal-first; the external-grade work (below) is deferred, not cancelled.
- **Knowledge**: the **finance/OSINT wiki plus the cybersecurity wiki**.

### Architecture

```
User
  | HTTPS
  v
Cemini AI gateway        <-- NEW. FastAPI. internal-only for now.
  |                          (external phase adds: auth, per-user
  |                           rate-limit + cost quota, injection guard)
  v
conductor -- classify (research / action / tool-call), route flash vs pro
  v                         v
RAG context            Action proposer
- kb-server (finance   - drafts a structured action proposal
  + cybersecurity)     - NEVER executes -- emits a confirm card
- stash episodic mem   - user confirms -> separate authorized path
  v
DeepSeek-V4 (flash default; pro / Claude for final synthesis)
  v
Response  (+ optional confirm card)
```

### Hosting

`cemini-egress-fi` — the Finnish order-routing relay (@entities/infrastructure/cemini-egress-fi.md) — is the recommended host for the internal phase: near-idle, librarian-class spec (2 vCPU / 4 GB / 75 GB), ~3.3 GB RAM free. DeepSeek is a cloud API so there are no model weights to host; the gateway footprint is small. `cemini-prod` is unsuitable (90% disk, ~50% swap, 41 containers); `cemini-librarian` is an alternative but loads the box that serves the brain.

Two honest caveats:

- **Transatlantic retrieval lag.** kb-server and stash are in Ashburn; `cemini-egress-fi` is in Helsinki. Every retrieval is a **~118–120 ms** server-to-server hop `[CONFIRMED 2026-05-22 — egress-fi → librarian ping]`. Tolerable for an internal tool; for a polished external product, replicate kb-server + stash to the EU so the brain is co-located.
- **Blast-radius caution for the external phase.** A public chatbot should not share a box with the live order-egress path. Acceptable while internal-only and attack-surface-free; before external launch, Cemini AI moves to its own EU box (or order routing moves off `cemini-egress-fi`).
- **K57 Polymarket copy disclosure.** When the assistant discusses copy-trading or mirror bots, it must state that hybrid-CLOB leaders match off-chain and followers only see fills at settlement/mempool — **"0-block" ≠ zero detection lag** (@concepts/polymarket-copy-trading-strategy.md, @entities/infrastructure/cemini-egress-fi.md). No prod prompt change from this workspace; wiki is the adoption artifact.

### Deferred to the external phase

These were blockers under the original "external from day one" framing; the no-users-yet scope downgrades them to pre-launch tasks:

1. **Wiki confidentiality split** — the OSINT wiki documents server IPs, topology, and infra internals. Before external users, pages need a public/internal `visibility` split so RAG cannot surface operational secrets — prompt injection makes this acute.
2. **Per-user memory scoping** — stash is single-tenant today; external users need partitioned episodic memory.
3. **Prompt-injection hardening** — external input is hostile; draw on the OpenClaw advisory taxonomy plus the Reasoning Safety Monitor already in the wiki.
4. **Auth, rate-limit, cost quotas** — per-user DeepSeek spend control.

### Open considerations

- **Provider-agnostic by design.** DeepSeek is the sound default — already paid-for, empirically validated (@entities/infrastructure/deepseek-api.md). Keep the OpenAI-compatible swap so final synthesis can move to `deepseek-v4-pro` or Claude, and conductor can route per-query.
- **GDPR upside.** A Finnish (EU) host puts customer data — sessions, stash memory — inside the EU, favorable for the eventual external phase. Caveat: DeepSeek inference still leaves the EU; an EU-data-residency requirement on *inference* would argue for an EU-hostable synthesis model.
- **Regulatory.** "Propose financial actions" for paying customers may be financial-advice or brokerage-regulated depending on jurisdiction — must be resolved before external launch, not after.

## Snippets

### User scope decisions — 2026-05-19

> Capability: "Answer + propose actions" — human confirms before execution.
> Audience: external users/customers, but "it wont be external facing for a while we have no users".
> Knowledge: finance/OSINT plus cybersecurity wikis.

## Dead Ends

*(none recorded yet for this page.)*
