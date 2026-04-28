---
title: Context compression / preserve / resume pattern (long-running LLM agents)
type: concept
tags: [concept, llm-agents, langgraph, state-management, prescribed-not-built, k8-promotion]
keywords: [context-compression, context-death, langgraph-checkpointer, state-serialization, preserve-resume, cpr-pattern]
related:
  - sources/4-5-links.md
  - entities/frameworks/langgraph.md
  - entities/infrastructure/deepseek-api.md
  - concepts/scatter-gather-topology.md
  - concepts/cryptographic-audit-trail.md
  - concepts/llm-agent-systems.md
  - concepts/wiki-tooling-evaluation.md
  - sources/agentmemory-rohitg00-cpr-impl.md
  - sources/willynikes2-knowledge-base-server.md
  - concepts/librarian-server-architecture.md
maturity: draft
created: 2026-04-28
updated: 2026-04-28
---

## Relations

- @sources/4-5-links.md — K8-canonical source. The pattern surfaces in two of the K8 doc's H2 sections — `EliaAlberti/cpr-compress-preserve-resume` (paragraph 36–) AND, in the sibling K9-candidate `4_5 links 2.docx`, the same repository is evaluated AGAIN as Document 3. Cross-doc duplicate is the strongest in-corpus signal that the *pattern* (not the specific repo) is the load-bearing concept worth a wiki page.
- @entities/frameworks/langgraph.md — the operative orchestration framework the pattern is prescribed to integrate against. LangGraph ships built-in PostgreSQL/Memory checkpointers (`langgraph.checkpoint.postgres.PostgresSaver`); the cpr-pattern is a thin layer ON TOP of LangGraph's existing checkpointer to add summarization-before-serialization.
- @entities/infrastructure/deepseek-api.md — the LLM brain the cpr-pattern's "compression node" would call to summarize sprawling debate trajectories into dense strings before persistence to pgvector
- @concepts/scatter-gather-topology.md — the topology the cpr-pattern would serialize/recover. K8 server-probe finding: the prescribed scatter-gather is not deployed (per Track C — only a linear 4-node `StateGraph` ships); cpr-pattern wiring would naturally land alongside any future scatter-gather work
- @concepts/cryptographic-audit-trail.md — adjacent state-persistence concern. The audit trail's SHA-256 chain (`services/audit/chain.py`) is a *forward-only append-with-hash* model; the cpr-pattern's checkpoint+restore is a *bidirectional save/load* model. Both lean on PostgreSQL but answer different questions — the audit chain answers "what did the agent decide and when, immutably?" while cpr-pattern answers "where do we resume from after a crash?". Distinct pages, intentional cross-link.
- @concepts/llm-agent-systems.md — cluster hub; cpr-pattern fits the "long-running agent state management + memory architectures" sub-cluster
- @concepts/wiki-tooling-evaluation.md — 2026-04-28 synthesis evaluating 7 wiki/memory tooling candidates; this concept page is **directly affected**: the recommendation to steal architectural details from `agentmemory` for the Python cpr-pattern wiring (rather than deploy the TS+iii-engine runtime) shifts this page's prescribed-not-built status from "open design" to "port-and-adapt the agentmemory pipeline shape"
- @sources/agentmemory-rohitg00-cpr-impl.md — Apache-2.0 reference implementation: PostToolUse hook → SHA-256 dedup (5min window) → privacy filter → LLM compress → BM25+Vector+Graph RRF fusion. Pipeline is reference-grade for the Python port; runtime architecture (TS + iii-engine) wrong for Cemini's stack — steal-architecturally, don't deploy
- @sources/willynikes2-knowledge-base-server.md — sibling memory-engine candidate; uses three-tier (hot/warm/cold) framing instead of compress-preserve-resume framing — parallel signal-vs-noise technique, different mechanism. Both attempt the same end (retrieval signal-vs-noise in long-running agents)

## Raw Concept

A named architectural pattern surfaced via K8 deep-read of `sources/4-5-links.md` (Cemini-internal evaluation document, 2026-04-05). The pattern is library-agnostic — the concrete reference implementation is `EliaAlberti/cpr-compress-preserve-resume` (a Claude Code skills package exposing `/compress`, `/preserve`, `/resume` slash-commands), but the underlying architectural shape applies to any long-running LLM agent that risks **context death** between sessions or in the face of process crashes.

K8 promoted this to a *concept* page rather than an *entity* page (under `entities/skills/cpr.md` or similar) because:
1. The K8 source's framing emphasizes the *pattern* (state serialization + recovery + compression-before-persist), not the specific Claude Code skills implementation
2. The same repository is evaluated **twice** in the Cemini-internal eval lineage (once in `4_5 links .docx` H2 section 9, again in `4_5 links 2.docx` H2 section 3) — the duplicate signals the user views this as a reusable architectural concept worth referencing across multiple eval contexts
3. K8 server-probe finding (2026-04-28): zero references to `PostgresSaver` / `MemorySaver` / `checkpointer` in `*.py` under `/opt/cemini/`. **The pattern is an active prescribed-not-built gap** — not a deployed feature the K8 doc was documenting

## Narrative

### The pattern (3 phases)

**1. Compress** — when the active context window approaches some threshold (hard token cap or end-of-execution-cycle), trigger an LLM summarization pass that distills the sprawling session log into a high-level "learnings" string. The compression is lossy by design — verbatim trajectory is discarded, *what was learned* is preserved.

**2. Preserve** — write the compressed learnings to durable storage. The reference implementation writes to a `CLAUDE.md` markdown file; the K8 source's prescription for Cemini is **PostgreSQL via LangGraph's PostgresSaver checkpointer** (and pgvector for the compressed strings, so semantic retrieval works at resume time). The K8 source explicitly rejects the markdown-file path as fundamentally unsafe for a concurrent financial-execution environment (no ACID compliance, no transaction safety, no concurrent-write protection).

**3. Resume** — on a new session start (or after a crash), reload the most recent compressed learnings into the context window before the fresh agent begins work. The resume step is the load-bearing user-facing surface — the agent must feel continuous-from-the-user's-perspective even though its raw context window has been wiped.

### What the K8 source flags as wrong about the reference implementation

The reference cpr-skills package relies on **manual human triggers** — the user types `/compress` or `/resume` to invoke the lifecycle. The K8 source flags this as fundamentally incompatible with a fully autonomous, high-frequency algorithmic trading platform:

> [...] this process must be completely headless and automated. The orchestrator cannot wait for a human prompt; it must trigger state compression and persistence automatically at the conclusion of every trading loop or when the token count breaches a defined threshold.

So the pattern's translation into the Cemini stack means: same three phases, but every trigger is automated. Compression fires at end-of-debate-cycle (no human in the loop); preserve writes to PostgreSQL synchronously; resume runs at boot/startup as part of the FastAPI lifespan-event handler.

### Why this pattern is a real prescribed-not-built gap on the Cemini stack (K8 server probe)

The K8 server probe (2026-04-28) ran:

```bash
ssh root@<server> "cd /opt/cemini && grep -lr 'PostgresSaver\|MemorySaver\|checkpointer' --include='*.py' . | head -5"
```

Result: **zero matches**. LangGraph's built-in checkpointer family is not imported anywhere in the Python codebase. The 5-agent debate protocol (`debate_protocol/` directory present per server probe) does NOT serialize its state between executions — every cycle starts fresh.

This means:
- A process crash mid-debate loses the entire reasoning trajectory
- A server reboot loses the reasoning context that informed the last several routing decisions
- The cryptographic audit trail (`services/audit/chain.py`, deployed per the J pass) captures the *output* of each debate cycle but **not the intermediate state** — so a post-hoc audit can verify "this trade was the result of debate cycle X" but cannot reconstruct *what each agent said during cycle X* without separate logging

Promoting this concept page makes the gap discoverable. A future deep-read pass (K9 or later) can cite back to this page when wiring `langgraph.checkpoint.postgres.PostgresSaver` into the orchestrator.

### Cemini integration roadmap (K8 source's verbatim Top-3 Steal-Immediately)

> 1. Implement automatic state serialization to PostgreSQL using LangGraph checkpointers to survive system restarts.
> 2. Develop a "compression node" in the graph that summarizes the 5-agent debate into a dense string before saving it to pgvector.
> 3. Create a "resume" initialization step that retrieves the last known market state and compressed debate history upon system boot.

K8 calibration: all three are 🟢 LOW effort per the K8 source's solo-dev filter, AND all three are currently 🔴 NOT-WIRED per server probe. The combined "natural next sprint" sizing would be 1–3 engineer-days based on the source's estimates. Whether this lands as part of an Option A / Option B / Option C resolution of the @concepts/scatter-gather-topology.md P1 ticket or as standalone wiring is an open architecture decision.

### Cross-source signal — appears in both `4_5 links .docx` and `4_5 links 2.docx`

The K8 source corpus has the cpr-pattern surfacing **twice** in two sibling docs from the same authoring date (2026-04-05):

| Document | H2 section | Framing emphasis |
|---|---|---|
| `4_5 links .docx` (K8) | Section 9: `EliaAlberti/cpr-compress-preserve-resume` | State serialization & recovery, LangGraph checkpointer mapping |
| `4_5 links 2.docx` (K9 candidate) | Document 3: `cpr-compress-preserve-resume` | (deferred to K9 deep-read; framing emphasis to be captured then) |

Cross-doc duplicate evaluation of the same repo is rare in the Cemini-internal eval lineage — it signals the user revisited and re-evaluated, which usually means the pattern is on an active integration shortlist. K8 promotes the concept on the strength of this signal; the K9 deep-read will calibrate whether the second evaluation reinforces or contradicts the first.

## Snippets

### Architecture pattern verbatim (K8 source paragraph ~ 256–260)

> The architecture mandates strict "State Serialization and Recovery." It ensures that the agent never loses operational state between sessions; context is explicitly saved to disk before termination and reloaded at initialization. This pattern maps perfectly to the LangGraph checkpointer functionality utilizing PostgreSQL. The exact state of the 5-agent debate protocol must be serialized to the database after every execution cycle. This ensures that if the 128GB VPS experiences a hard reboot or a process crash, the system can gracefully resume processing without losing the complex, token-heavy debate history that led to a specific routing decision.

**K8 calibration**: "128GB VPS" is the ~18× over-stated claim caught by the server probe (actual: 7 GB). Drift doesn't change the pattern's logic — it intensifies it. At 7 GB, OOM-on-debate-cycle is a *real* failure mode the cpr-pattern would directly address.

### Algorithm verbatim — context compression (K8 source paragraph ~ 261–262)

> The core technique is "Context Compression," which utilizes the LLM to summarize a lengthy, token-heavy session log into concise, high-level learnings before intentionally clearing the active context window. On the CPU-only server, computational memory and processing speed are strictly limited. After the 5-agent heterogeneous ensemble completes a debate, a background process should automatically trigger a compression pass, reducing the sprawling trajectory into a dense summary string. This summary is then stored in pgvector for future retrieval, thereby keeping the active context window aggressively small and subsequent inference cycles fast.

### What they got wrong (K8 source paragraph ~ 264 — the "manual triggers" rejection)

> The system fundamentally relies on manual human triggers—typing `/compress` or `/resume`—to manage memory and prevent context exhaustion. In a fully autonomous, high-frequency algorithmic trading platform, this process must be completely headless and automated. The orchestrator cannot wait for a human prompt; it must trigger state compression and persistence automatically at the conclusion of every trading loop or when the token count breaches a defined threshold.

### IP sale relevance (K8 source paragraph ~ 266)

> Demonstrating robust, automated state management and algorithmic context compression proves to an acquirer that the trading platform can operate continuously over months or years without degrading due to context window exhaustion or "context death". This highlights the system's stability, maturity, and production-readiness, which are highly valued metrics during technical due diligence.

K8 cross-link: the IP-sale framing here aligns with the K6/K7-trio "headline-claim-verifiability problem" — a continuous-run claim that the audit trail can defend post-hoc. The cpr-pattern wired to LangGraph checkpointer + cryptographic audit trail anchoring would let an acquirer's technical-due-diligence pass replay arbitrary historical debate cycles. Strong IP-sale-prep entry.
