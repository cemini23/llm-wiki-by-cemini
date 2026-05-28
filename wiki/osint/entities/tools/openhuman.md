---
title: openhuman — TokenJuice HTML→Markdown compression (Steal-from, GPL-3.0 quarantine)
type: entity
tags: [tool, local-first, knowledge-tree, sqlite, obsidian, gpl-3-0, steal-from, workflow, license-quarantine, html-compression]
keywords: [openhuman, tokenjuice, html to markdown, compression, sqlite memory tree, obsidian vault, 80% token reduction, chromium embedded framework]
related:
  - sources/tool-evaluation-wiki-fit-2026-05-13.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - concepts/paradigm-vs-license-inverse-correlation.md
  - sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md
maturity: draft
created: 2026-05-13
updated: 2026-05-28
---

## Relations

- `@sources/tool-evaluation-wiki-fit-2026-05-13.md` — origin source (Doc 3, K42), Steal-from
- `@concepts/tool-evaluation-framework.md` — methodology
- `@concepts/cemini-license-posture.md` — GPL-3.0 quarantine policy
- `@sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md` — K55 Post 2 (@AlphaSignalAI deep-dive on @senamakel's OpenHuman); v0.54.0 update, agentmemory bridge, +20k stars, Product Hunt #1

## K55 update (2026-05-20)

K55 Posts 2.docx Post 2 documents OpenHuman's v0.54.0 release (2026-05-19) and the Product Hunt #1 ranking — repo crossed +20k stars in days, with 5,000+ users in 7 days. New material relevant to the wiki:
- **v0.54.0 agentmemory backend bridge**: `memory.backend = "agentmemory"` in `config.toml` shares a durable store with Claude Code, Cursor, Codex, and OpenCode. Mirrors Cemini's `librarian-stash` MCP role architecturally.
- **Fully-local STT/TTS via Whisper + Piper** (prior path required ElevenLabs cloud).
- **MCP stdio memory server**, NotebookLM-style folder ingestion.
- **Native auto-ingest**: still only Gmail / Notion / Slack (the 118+ Composio catalog is callable but doesn't auto-feed Memory Tree).
- **"Local-first" caveat**: applies to memory only. Chat, vision, web search, OAuth proxying, TTS streaming stay cloud.
- **Independent measurements**: PrimeAIcenter 5-day test measured ~70% TokenJuice compression (not the project's 80% claim).
- **No published security audit** despite v0.54.0 hardening (path traversal, DNS rebinding, bearer redaction).

Verdict unchanged: **Steal-from / GPL-3.0 quarantine**. Methodology adoption acceptable; codebase remains poison-pill for `/opt/cemini`. The agentmemory + memory-tree pattern is the highest-leverage thing to steal architecturally. Routed to ccc-wiki brief for K55 (see `@sources/multi-wiki-tool-eval-19url-2026-05-20.md` cross-wiki routing).

## Raw Concept

- **URL**: `https://github.com/tinyhumansai/openhuman`
- **License**: GPL-3.0 ← **poison-pill for `/opt/cemini`**
- **Stars**: 3.6k / 72 open issues
- **Stack**: Rust (69.8%), TypeScript (26.3%), SQLite, Obsidian
- **Tier**: Steal-from (methodology only — codebase forbidden)
- **Primary fit**: Workflow

## Narrative

Local-first knowledge tree with 118+ OAuth integrations, Chromium Embedded Framework, SQLite memory + Obsidian sync. Key extractable: **TokenJuice** HTML→Markdown compression claiming ~80% token cost reduction; deterministic chunking ≤3k tokens.

### Steal-from scope

GPL-3.0 forbids any static linking or distribution within proprietary stacks. Extract:
- HTML→Markdown compression heuristics
- SQLite memory tree schema patterns
- Chunking parameter discipline

Never inherit codebase. OSINT cross-route: TokenJuice as academic reference for scraping-context-window optimization.

### Phase-0 audit (2026-05-28)

| Check | Result |
|-------|--------|
| License | **GPL-3.0** confirmed (~29k★) |
| Claimed compression | TokenJuice HTML→Markdown methodology remains reference-only |
| Prod import | **REJECT** for `/opt/cemini` codebase |

**Verdict: REJECT (prod import) / steal-from methodology only** — unchanged posture, now source-verified.

[Source: Tool Evaluation and Wiki Fit.docx URL 11 (retrieved 2026-05-13)]
