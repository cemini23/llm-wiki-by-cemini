---
title: "wastedcode/memex — file-system-only LLM-driven wiki, wraps `claude -p` programmatic mode in a daemon with Linux mount-namespace isolation"
type: source
tags: [github, npm, claude-code, namespace-isolation, karpathy-pattern, filesystem-only, no-rag, no-embeddings, vannevar-bush-memex]
clusters: [llm-agents]
keywords: [memex, wastedcode, claude-programmatic-mode, mount-namespace, cap-sys-admin, just-files-no-rag, vannevar-bush, three-layers, three-operations]
related:
  - concepts/wiki-tooling-evaluation.md
  - sources/atomicmemory-llm-wiki-compiler.md
  - sources/willynikes2-knowledge-base-server.md
  - sources/llm-wiki.md
  - sources/emtwiki-deployed-example.md
maturity: validated
read_status: read
created: 2026-04-28
updated: 2026-04-28
---

## Relations

- @concepts/wiki-tooling-evaluation.md — synthesis page; **rejected for adoption** (Linux/CAP_SYS_ADMIN friction; 5-of-10 Karpathy coverage vs llm-wiki-compiler's 7-of-10) but kept on the radar as the cleanest minimal Karpathy implementation
- @sources/atomicmemory-llm-wiki-compiler.md — sibling Karpathy implementation; richer (MCP, embeddings, candidate review queue); same filesystem-first preference
- @sources/willynikes2-knowledge-base-server.md — sibling memory engine; opposite architectural axis (database-first, three-tier memory)
- @sources/llm-wiki.md — Karpathy's gist; memex is the most direct "just-files" interpretation of the gist's three-layer raw/wiki/schema architecture
- @sources/emtwiki-deployed-example.md — the EMT-Basic deployed wiki may be built with memex (same author/host pattern at endusergeek.com); demonstrates filesystem-only Karpathy at production scale

## Raw Concept

- **Original title**: Memex — *Stop re-discovering what you already know. […] An LLM runtime that builds and maintains a personal wiki from your raw sources — so the knowledge compounds instead of disappearing into chat history.*
- **Author**: isingh (single contributor)
- **Type**: GitHub repo + npm package (`@wastedcode/memex`)
- **URL**: https://github.com/wastedcode/memex
- **Retrieved**: 2026-04-28 (via Exa `crawling_exa`)
- **Stars**: 56; **License**: MIT 🟢
- **Created**: 2026-04-06; **Last push**: 2026-04-08
- **Stack**: TypeScript (96.5%), Node.js ≥ 20, Linux + mount namespaces (CAP_SYS_ADMIN required)
- **Read status**: read (deep-read README; comparing minimalism vs llm-wiki-compiler's feature breadth)

## Narrative

memex is the **minimal Karpathy-pattern interpretation**: an LLM runtime that wraps `claude -p` (Claude Code's programmatic mode) into a daemon, gives each wiki its own Linux mount namespace + job queue, and operates on plain markdown files via Claude's existing file tools (Read, Write, Edit, Glob, Grep). **No embeddings, no vector DB, no retrieval pipelines** — explicitly framed as a feature, not a limitation:

> "Just files, no RAG. The wiki is a directory of markdown files. […] Claude is already smart enough to grep through files, read what's relevant, and figure out what to update. The simplest architecture that works."

The architectural posture **matches the workspace's filesystem-first preference exactly**. The friction is operational: requires Linux + CAP_SYS_ADMIN (or root) to set up mount namespaces; macOS-incompatible without a Linux VM; single-contributor project at 56 stars (low ecosystem maturity).

**Three layers** (verbatim alignment with Karpathy + with our own `CLAUDE.md`):
1. **Raw sources** — curated articles, papers, images, data files. Immutable. LLM reads, never modifies.
2. **The wiki** — LLM-generated markdown. Summaries, entity pages, concept pages, cross-references, an index. The LLM owns this layer entirely.
3. **The schema** — conventions for how the wiki is structured. Co-evolved by you and the LLM over time.

**Three operations**:
- **Ingest** — drop a source in; the LLM reads it, writes a summary, updates the index, touches every related page across the wiki.
- **Query** — ask a question; the LLM searches the wiki and synthesizes an answer. Good answers get filed back as new pages.
- **Lint** — health-check the wiki. Find contradictions, orphan pages, missing cross-references, stale claims. The LLM fixes what it can and flags what needs your judgment.

This is a **strict subset of llm-wiki-compiler's pattern** — minus MCP server, minus embeddings, minus candidate review queue, minus confidence/contradicted-by metadata, minus multi-provider config (memex is Claude-only via OAuth `memex login`). The minus-list is exactly what makes llm-wiki-compiler more capable; the philosophical case for memex is that those features are unnecessary complexity if "Claude reads files" is sufficient.

**Sandboxing via Linux mount namespaces** (the project's clever-bit):
```
DAEMON (memex serve)                            privileged
unshare -m -- mount --bind .../wikis/acme /workspace \
  claude -p "..." --tools Read,Write,Edit,Glob,Grep

  ┌────────────────────────────────────────────────────────┐
  │  MOUNT NAMESPACE — what Claude sees                    │
  │  /workspace/                                           │
  │    .claude.md        wiki/_schema.md                   │
  │    .claude/          wiki/_index.md                    │
  │    .tools/           wiki/_log.md                      │
  │    wiki/             wiki/raw/                         │
  │                                                        │
  │  No /home. No /etc. No other wikis.                    │
  └────────────────────────────────────────────────────────┘
```

Each wiki gets a private `/workspace` view; Claude can't see the host filesystem, the user's home dir, or other wikis. Tool access is restricted to file ops (Read, Write, Edit, Glob, Grep) unless explicitly opted into more (Bash, WebSearch via `.tools/allowed-tools.txt`). Per-wiki MCP server configs via `.tools/mcp.json`. **Strong security posture** for an LLM-writes-files daemon — comparable to Docker container isolation but without the Docker dependency.

**Job queue per wiki** (serial writes prevent race conditions); independent wikis run in parallel. Wiki registry stored in SQLite (daemon-side, not user-facing). Audit log via `memex logs <wiki>`.

**Vannevar Bush framing** (the project's distinguishing intellectual move):

> "The idea is related in spirit to Vannevar Bush's [Memex](https://en.wikipedia.org/wiki/Memex) (1945) — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that."

This is a more philosophically-grounded framing than llm-wiki-compiler's "wiki instead of a graveyard of tabs" framing. Both are correct; memex's framing is more honest about the *active curation* part of the pattern.

**Customization via `.claude.md`** — same idiom as Claude Code's project-level CLAUDE.md. Per-wiki conventions ("Filing conventions: organize competitors under competitors/{name}.md / Track pricing changes with dates / Flag acquisitions and funding rounds prominently / Things to ignore: Job postings, Social media noise without substance"). The user owns the `.claude.md`; the LLM extends its base system prompt with whatever's there.

**Why-rejected for adoption** (per the concept page):
1. **Linux + CAP_SYS_ADMIN requirement** — the workspace runs on macOS. Adopting memex means Linux VM or remote Linux box. Not impossible, but high friction.
2. **Single-contributor maturity** — 1 contributor, 56 stars, last push 2026-04-08 (so ~3 weeks since any update). Risk of project dormancy.
3. **5-of-10 Karpathy coverage** vs llm-wiki-compiler's 7-of-10. Same minimal core; missing MCP, embeddings, candidate review.
4. **Claude-only** — no multi-provider story. If we wanted to swap to DeepSeek-API-via-OpenAI-compatible-endpoint later, llm-wiki-compiler supports it; memex doesn't (currently).

**Why-still-on-radar** — memex is the **clearest reference for what "minimal Karpathy" looks like**. If llm-wiki-compiler smoke-test fails (overwrites our hand-curated frontmatter, or LLM cost is prohibitive), memex's "just files + Claude reads them" model is a fallback worth re-considering — adapt to macOS via a Linux VM, accept the lower feature ceiling, gain simplicity. Cross-linked from the concept page accordingly.

## Snippets

### S1 — "Just files, no RAG" framing (`README.md`, "Why Memex")

> "Just files, no RAG. The wiki is a directory of markdown files. No vector databases, no embeddings, no retrieval pipelines. Claude is already smart enough to grep through files, read what's relevant, and figure out what to update. The simplest architecture that works."

### S2 — Vannevar Bush 1945 framing (`README.md`, "The idea")

> "The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that."

### S3 — Three layers verbatim alignment (`README.md`, "What Memex does")

> "Three layers: 1. Raw sources — your curated collection of articles, papers, images, data files. Immutable. The LLM reads them but never modifies them. 2. The wiki — LLM-generated markdown. Summaries, entity pages, concept pages, cross-references, an index. The LLM owns this layer entirely. 3. The schema — conventions for how the wiki is structured. Co-evolved by you and the LLM over time."

### S4 — Three operations verbatim alignment (`README.md`, "What Memex does")

> "Three operations: Ingest — drop a source in, the LLM reads it, writes a summary, updates the index, and touches every related page across the wiki. Query — ask a question, the LLM searches the wiki and synthesizes an answer grounded in your accumulated knowledge. Good answers get filed back as new pages. Lint — health-check the wiki. Find contradictions, orphan pages, missing cross-references, stale claims. The LLM fixes what it can and flags what needs your judgment."

### S5 — Karpathy-quote framing (`README.md`, "The idea")

> "The tedious part of maintaining a knowledge base isn't the reading or the thinking — it's the bookkeeping. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass."

### S6 — Mount-namespace security model (`README.md`, "How it works")

> "Each wiki's queue processes jobs serially — no concurrent writes. Independent wikis run in parallel. Mount namespaces provide filesystem isolation without Docker overhead."
