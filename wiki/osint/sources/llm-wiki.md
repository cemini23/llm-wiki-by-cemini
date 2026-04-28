---
title: "LLM Wiki: a pattern for building personal knowledge bases using LLMs"
type: source
tags: [md, llm-agents, schema-pattern-source, karpathy]
clusters: [llm-agents]
related:
  - concepts/llm-agent-systems.md
  - sources/4-6-links.md
  - concepts/wiki-tooling-evaluation.md
  - sources/atomicmemory-llm-wiki-compiler.md
  - sources/emtwiki-deployed-example.md
  - sources/wastedcode-memex.md
  - sources/willynikes2-knowledge-base-server.md
  - concepts/librarian-server-architecture.md
maturity: validated
read_status: validated
created: 2026-04-23
updated: 2026-04-28
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research in the Cemini corpus
- @sources/4-6-links.md — Cemini-internal docx that evaluates `nvk/llm-wiki` + Karpathy's LLM Wiki Pattern alongside other links
- @concepts/wiki-tooling-evaluation.md — synthesis page evaluating 7 candidates (incl. 4 Karpathy-pattern implementations) against the workspace librarian's current 4-of-10 Karpathy-coverage gap; this gist is the foundational pattern source the synthesis is grounded in
- @sources/atomicmemory-llm-wiki-compiler.md — open-source compiler that implements 7-of-10 of this gist's operations off-the-shelf (MIT, Node, MCP server); **primary adoption candidate** for the workspace librarian
- @sources/emtwiki-deployed-example.md — deployed example wiki (San Juan College EMT-Basic curriculum, NM EMS Bureau aligned) demonstrating the gist's pattern at production scale in a high-stakes domain
- @sources/wastedcode-memex.md — sibling Karpathy-pattern implementation; minimal "just files, no RAG" interpretation wrapping `claude -p` programmatic mode in Linux mount-namespace daemons
- @sources/willynikes2-knowledge-base-server.md — sibling memory engine + 16-tool MCP server; database-first variant of the gist's pattern (SQLite + FTS5 + embeddings; Obsidian sync bidirectional)

## Raw Concept

- **Original title**: LLM Wiki: a pattern for building personal knowledge bases using LLMs
- **Author**: Andrej Karpathy
- **Type**: MD (GitHub Gist)
- **URL**: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- **Location**: research for cemini/llm-wiki.md (local copy, retrieved 2026-04-23)
- **Length**: 75 lines, ~1,500 words, ~12 KB
- **Read status**: validated (deep-read 2026-04-26)
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents
- **Schema role**: this gist is one of the two foundational pattern sources cited by `CLAUDE.md` ("Pattern sources" section); the other is the ByteRover Context Tree paper. The architecture decisions in this workspace — three-layer (raw / wiki / schema), three-op (ingest / query / lint), `index.md` + parseable-prefix `log.md`, "good answers filed back into the wiki" — all trace directly to this document.

## Narrative

Karpathy's central distinction: **persistent compounding wiki vs. RAG-on-every-query**. Most LLM-document workflows (NotebookLM, ChatGPT file uploads, generic RAG) re-derive answers from raw chunks on each question — nothing accumulates. The Wiki Pattern instead has the LLM *incrementally build and maintain* a structured, interlinked markdown knowledge base that sits between you and the raw sources. New material is read once, integrated into entity/concept pages, cross-referenced, contradiction-flagged. The wiki *is* the artifact; queries hit it, not the raw corpus.

**Three layers**: raw sources (immutable) → wiki (LLM-owned markdown) → schema (e.g. `CLAUDE.md`, defines structure + workflows + conventions; co-evolved with the LLM over time). **Three ops**: ingest (drop a source → LLM updates 10–15 pages), query (search the index → synthesize → optionally file back), lint (periodic health-check for contradictions / orphans / stale claims / missing cross-refs). **Two index files**: `index.md` (content-oriented catalog) + `log.md` (chronological, parseable prefix `## [YYYY-MM-DD] op | Title`).

**Operational metaphor** (used verbatim in our `CLAUDE.md` rationale): "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase." User curates sources + asks questions; LLM does all the bookkeeping — summaries, cross-references, file maintenance, the work that historically caused human-maintained wikis to be abandoned. Optional CLI tooling: `qmd` for hybrid BM25 + vector + LLM-rerank search; Obsidian Web Clipper for browser-to-markdown ingest; Marp for slide decks; Dataview for frontmatter queries; the `.git` repo gives free version history.

**Why it works**: "the tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. […] LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass." Karpathy positions the pattern as the practical resolution of Vannevar Bush's 1945 Memex vision (private, curated, associative-trail-rich knowledge stores), where the missing piece had always been *who does the maintenance*.

**Cemini-side adaptations** (where our schema goes beyond the gist):
- We added a **distribution layer** (`briefs/` → `/opt/cemini/briefs/`) — the gist is single-corpus / personal-use; we have a downstream consumer (CeminiSuite dev stack) with explicit boundary rules.
- We added a **cluster taxonomy** (`clusters: []` in frontmatter; cluster-hub concept pages like `@concepts/rl-marl-research.md`, `@concepts/llm-agent-systems.md`) — orphan-prevention by topology rather than by lint after-the-fact.
- We added a **maturity lifecycle** (`draft → validated → core` + `retracted`) the gist doesn't formalize.
- We added a **prescribed-vs-deployed pattern** (J / K passes, see `@concepts/scatter-gather-topology.md`, `@concepts/cryptographic-audit-trail.md`) — specific to Cemini's blueprint-heavy source corpus where prescriptive engineering audits would otherwise get collapsed into present-tense as-built claims.
- We added **bidirectional `related:` enforcement** + a CI lint pipeline (`scripts/wiki_lint.py`, GitHub Actions) — the gist mentions lint as an LLM-driven periodic check, we made it both manual-trigger and weekly-cron.

The gist's core advice is intentionally abstract — "your LLM agent will figure out the specifics in collaboration with you." This source page exists to make the pattern's lineage explicit and to anchor any future schema evolution against the original.

## Snippets

> **The thesis — wiki as compounding artifact (the line our schema's grounded in)**
>
> "The idea here is different. Instead of just retrieving from raw documents at query time, the LLM **incrementally builds and maintains a persistent wiki** — a structured, interlinked collection of markdown files that sits between you and the raw sources. […] This is the key difference: **the wiki is a persistent, compounding artifact.** The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read. The wiki keeps getting richer with every source you add and every question you ask."

> **The operational metaphor**
>
> "You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it. You're in charge of sourcing, exploration, and asking the right questions. The LLM does all the grunt work — the summarizing, cross-referencing, filing, and bookkeeping that makes a knowledge base actually useful over time. In practice, I have the LLM agent open on one side and Obsidian open on the other. The LLM makes edits based on our conversation, and I browse the results in real time — following links, checking the graph view, reading the updated pages. Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

> **Three layers (architecture grounding for our `research for cemini/` + `wiki/` + `CLAUDE.md` triad)**
>
> "**Raw sources** — your curated collection of source documents. […] These are immutable — the LLM reads from them but never modifies them. This is your source of truth.
>
> **The wiki** — a directory of LLM-generated markdown files. […] The LLM owns this layer entirely. It creates pages, updates them when new sources arrive, maintains cross-references, and keeps everything consistent. You read it; the LLM writes it.
>
> **The schema** — a document (e.g. CLAUDE.md for Claude Code or AGENTS.md for Codex) that tells the LLM how the wiki is structured, what the conventions are, and what workflows to follow. […] This is the key configuration file — it's what makes the LLM a disciplined wiki maintainer rather than a generic chatbot."

> **Filed-back-answers (the pattern Cemini uses for C → G+H ingest-back of Exa briefs)**
>
> "**Query.** You ask questions against the wiki. The LLM searches for relevant pages, reads them, and synthesizes an answer with citations. […] The important insight: **good answers can be filed back into the wiki as new pages.** A comparison you asked for, an analysis, a connection you discovered — these are valuable and shouldn't disappear into chat history. This way your explorations compound in the knowledge base just like ingested sources do."

> **`index.md` + `log.md` (we adopted both verbatim, including the parseable prefix)**
>
> "**index.md** is content-oriented. […] Organized by category (entities, concepts, sources, etc.). The LLM updates it on every ingest. […] This works surprisingly well at moderate scale (~100 sources, ~hundreds of pages) and avoids the need for embedding-based RAG infrastructure.
>
> **log.md** is chronological. It's an append-only record of what happened and when — ingests, queries, lint passes. A useful tip: if each entry starts with a consistent prefix (e.g. `## [2026-04-02] ingest | Article Title`), the log becomes parseable with simple unix tools — `grep \"^## \\[\" log.md | tail -5` gives you the last 5 entries."

> **Why it works (the line that justifies the entire enterprise)**
>
> "The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero."

> **Memex lineage**
>
> "The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that."
