---
title: "AgriciDaniel/claude-obsidian — Claude + Obsidian Knowledge Companion implementing Karpathy's LLM Wiki Pattern (MIT, Python, 3.6k★)"
type: source
tags: [github, claude-code-skill, knowledge-management, obsidian, second-brain, karpathy-pattern, librarian-tooling, mit-license, gemini-dr-wave5b, steal-from-tier]
keywords: [claude-obsidian, agriciDaniel, karpathy-llm-wiki-pattern, obsidian-vault, persistent-knowledge-engine, autoresearch-multi-round-loop, wiki-lint-py, hot-md-session-memory, wiki-save-slash-command, claude-code-skill, dataview-environment, model-context-protocol, mcp-bridge, second-brain-pattern]
clusters: [librarian-tooling, llm-agents]
related:
  - sources/gemini-dr-wave5b-osint-2026-04-30.md
  - sources/llm-wiki.md
  - sources/atomicmemory-llm-wiki-compiler.md
  - sources/wastedcode-memex.md
  - sources/kepano-obsidian-skills.md
  - sources/obsidian-second-brain-eugeniughelbur.md
  - sources/willynikes2-knowledge-base-server.md
  - sources/alash3al-stash.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/librarian-server-architecture.md
  - concepts/high-signal-paper-patterns.md
  - concepts/ip-sale-readiness.md
  - concepts/mcp-tool-marketplace.md
maturity: validated
read_status: read-skim
created: 2026-04-30
updated: 2026-04-30
---

## Relations

- @sources/gemini-dr-wave5b-osint-2026-04-30.md — Wave 5B canonical brief; URL 2 of the 18-URL evaluation; promoted to dedicated page from Steal-from verdict (Karpathy-pattern adjacency)
- @sources/llm-wiki.md — Karpathy's foundational gist (the workspace is built on this pattern); claude-obsidian explicitly cites Karpathy's pattern in repo description
- @sources/atomicmemory-llm-wiki-compiler.md — Wave 4B Adopt for the librarian server; both implement the Karpathy pattern but in different deployment surfaces. **Three-way Karpathy-pattern stack**: atomicmemory (headless server), claude-obsidian (visual workstation), wastedcode/memex (filesystem-only minimal). Each has a niche.
- @sources/wastedcode-memex.md — sibling Karpathy-pattern implementation (filesystem-only minimal); claude-obsidian sits one tier richer (Obsidian + slash commands + autoresearch loop)
- @sources/kepano-obsidian-skills.md — fellow Obsidian-bridge tooling; orthogonal pattern (skills for note-taking workflow vs wiki compilation)
- @sources/obsidian-second-brain-eugeniughelbur.md — earlier Obsidian-second-brain reference; claude-obsidian is the more code-forward inheritance
- @sources/willynikes2-knowledge-base-server.md — sibling memory-engine + MCP server with three-tier (hot/warm/cold) architecture; claude-obsidian's `wiki/hot.md` schema echoes the hot-tier concept
- @sources/alash3al-stash.md — Wave 5A Adopt for the Wiki/Librarian server; complementary memory layer — stash holds dynamic episodic memory in Postgres, claude-obsidian holds curated Markdown knowledge in Obsidian. Both belong on Cemini's Wiki/Librarian stack pattern map.
- @concepts/wiki-tooling-evaluation.md — adoption decision parent
- @concepts/librarian-server-architecture.md — claude-obsidian's `/autoresearch` + `wiki_lint.py` + `hot.md` patterns inform the Cemini librarian's continuing evolution

## Raw Concept

- **Original title**: "Claude + Obsidian knowledge companion. Persistent, compounding wiki vault based on Karpathy's LLM Wiki pattern. /wiki /save /autoresearch"
- **Author**: AgriciDaniel (sole contributor)
- **Repository**: https://github.com/AgriciDaniel/claude-obsidian
- **Homepage**: https://agricidaniel.com/blog/claude-obsidian-ai-second-brain
- **License**: MIT (file-level + repo-level confirmed via Exa `crawling_exa` 2026-04-30)
- **Primary language**: Python (69.0%) + Shell (29.0%) + Makefile (2.0%)
- **Stars**: 3,581 (as of 2026-04-30) — strong signal for a 23-day-old project
- **Forks**: 416
- **Contributors**: 1
- **Created**: 2026-04-07 (23 days old at evaluation)
- **Last push**: 2026-04-24
- **Releases**: 6 (latest v1.6.0 on 2026-04-24)
- **Topics**: ai, claude-code, claude-code-skill, knowledge-management, obsidian, open-source, second-brain
- **Read status**: read-skim (README + license + repo metadata + topic tags via `crawling_exa`; deeper agents/wiki-lint.md + hot.md schema read pending pre-extraction commit)
- **Discovered via**: User Wave 5B Gemini DR brief (2026-04-30)
- **Primary cluster**: librarian-tooling

## Narrative

### What it is

claude-obsidian is a Claude+Obsidian persistent knowledge engine. Rather than functioning as a conventional conversational interface, it operates **autonomously to curate a Karpathy-pattern wiki vault** — explicitly cited in the repo description.

**Three slash commands** drive the workflow:

1. **`/wiki`** — query the existing knowledge vault from inside a Claude conversation
2. **`/save`** — persist a meaningful insight from the current session to the vault as a structured Markdown page
3. **`/autoresearch`** — run a multi-round research loop autonomously: question → search → synthesize → cross-reference → file

The repo bundles:
- **Predefined Markdown schemas** for source / entity / concept / brief pages (parallel to the Cemini workspace's own four-page-type taxonomy)
- **`wiki_lint.py` reference implementation** — quality checks for orphans, bidirectional `related:` gaps, citation completeness
- **`wiki/hot.md` session memory architecture** — a hot-tier ephemeral context cache that spans sessions
- **Claude Code skill bundle** — registers as a Skill so the slash commands trigger the right behaviors

The deployment surface is **Obsidian + Claude Code on a workstation** — the project relies on Obsidian's "Bases" plugin and the "Local REST API" plugin to wire MCP connectivity into the vault.

### Why this matters for Cemini

This is **the closest-relative Karpathy-pattern implementation to the workspace's own design** in the corpus. The methodology is direct lineage; the gap is in deployment posture (claude-obsidian = visual workstation; Cemini workspace = laptop+server hybrid feeding atomicmemory's headless compilation).

**Workflow — ✅ Yes-fit**:
- Direct relevance to the solo-dev Obsidian/Dataview environment.
- Three slash commands map directly to existing workspace operations: `/wiki` ≈ index.md query; `/save` ≈ the ingest workflow; **`/autoresearch` is the most operationally interesting extract** — it formalizes a multi-round research loop pattern that could augment the existing Tier-2 sweep workflow.

**Wiki / Librarian server — ⚠️ Partial-fit**:
- The `wiki_lint.py` and `wiki-query` patterns conceptually map to atomicmemory/llm-wiki-compiler operations. The `wiki/hot.md` session-memory architecture could be specifically mirrored for Cemini's solo-developer-context-resume needs.
- **But**: the full Obsidian-runtime dependency makes it incompatible with the headless CPX21 server. **Steal the patterns, not the runtime.**

**Cemini production stack — ❌ No-fit**:
- Obsidian Local REST API + visual environment is incompatible with headless trading deployment. Clear mismatch.

### Cross-paper / cross-tool synthesis

- **Pair with `@sources/llm-wiki.md`** (Karpathy's foundational gist): claude-obsidian is a literal implementation of Karpathy's pattern — the closest in spirit to the workspace's own implementation. Worth deep-reading the agents/wiki-lint.md definitions for any quality-rule additions Cemini hasn't surfaced yet.
- **Pair with `@sources/atomicmemory-llm-wiki-compiler.md`**: atomicmemory is the **headless-server flavor** of the same Karpathy pattern; claude-obsidian is the **visual-workstation flavor**. The Cemini workspace's design is closer to a hybrid — laptop-curated content compiled by atomicmemory on the server. claude-obsidian's `/autoresearch` slash command gives a third **active-research-loop flavor** worth steal-froming.
- **Pair with `@sources/alash3al-stash.md`** (Wave 5A Adopt): stash holds *dynamic episodic memory* in Postgres+pgvector; claude-obsidian holds *curated Markdown knowledge* in Obsidian. Together they form a complete persistent-knowledge stack — short-term episodic via stash + long-term curated via wiki-pattern.

### The /autoresearch pattern — the highest-value extract

The `/autoresearch` slash command appears to be the wave's most operationally novel feature. Pseudocode reconstruction (pre-deep-read):

```
/autoresearch <question>
  →  decompose into sub-questions (rounds)
  →  for each round:
       →  search wiki vault locally
       →  if insufficient, search externally (Exa-equivalent)
       →  synthesize partial answer
       →  identify cross-references / next-round questions
  →  file structured output to vault as new page(s)
  →  append to log.md / index.md
```

This pattern formalizes what the Cemini workspace currently does manually as the Tier-2 weekly sweep. Steal-from extract: **the loop control structure** — termination conditions, depth limits, deduplication checks. The wiki-content-generation logic itself can stay Cemini-bespoke; only the loop scaffolding is what's worth lifting.

### Risks & open questions

1. **Bus-factor: 1 contributor** — same fork-and-maintain caveat as other Wave 5 projects. **Mitigation**: extract patterns into Cemini-bespoke implementations; do NOT depend on upstream binary code.

2. **Obsidian-plugin lock-in** — the project mandates "Bases" plugin + "Local REST API" plugin. Both are community-maintained. If either is deprecated, the entire MCP connectivity story collapses. **Risk acceptable** for the workflow-tier extraction; not acceptable for any deeper integration.

3. **`/autoresearch` token cost** [NEEDS VERIFICATION 2026-04-30] — measure exact token-consumption rate of the multi-round loop on a representative Cemini session. Required to model API cost over a monthly research cycle.

4. **Repository freshness** — created 2026-04-07, 23 days old at evaluation. Strong star growth (3.6k stars in ~3 weeks) but very young. Re-evaluate at next wave touch — adoption tier may move.

5. **Schema compatibility with Cemini's existing wiki** — claude-obsidian's predefined Markdown schemas are not necessarily byte-compatible with Cemini's four-page-type frontmatter. Audit before any pattern import.

### Cemini-side adoption assessment

**Decision**: **Steal-from the patterns. Do not adopt the runtime.**

Concrete next-steps:

1. **Read agents/wiki-lint.md and hot.md schema** in depth via direct repo clone or `crawling_exa`. ~1 hour.
2. **Reconstruct `/autoresearch` loop logic** from the source — extract the loop control structure. Cemini-bespoke implementation in Python. ~3-4 hours.
3. **Append `/autoresearch` slash to Cemini workspace** as a Tier-2 sweep automation tool. Replace the current manual weekly cadence with a parameterized loop. ~1 day.
4. **Compare hot.md session-memory schema** to Cemini's existing session-resume pattern (cpr-pattern). Adopt the hot-tier concept if it fills a gap.
5. **Re-evaluate at next wave touch** — if claude-obsidian gains a multi-contributor base + 6+ months track record, the adoption tier may rise.

License + IP-sale-readiness disposition: **clean for Steal-from**. MIT is on the clean license list; pattern extraction with Cemini-bespoke reimplementation is unambiguously safe.

### Citation

> AgriciDaniel. (2026). *claude-obsidian — Claude + Obsidian knowledge companion*. v1.6.0. GitHub. https://github.com/AgriciDaniel/claude-obsidian (License: MIT; retrieved 2026-04-30 via Exa `crawling_exa`)

## Snippets

> **The repo's identity statement**:
>
> "Claude + Obsidian knowledge companion. Persistent, compounding wiki vault based on Karpathy's LLM Wiki pattern. /wiki /save /autoresearch" [Source: github.com/AgriciDaniel/claude-obsidian repo description, retrieved 2026-04-30]

> **Wave 5B Steal-from rationale (URL 2 evaluation excerpt)**:
>
> "Steal-from. While the full installation relies heavily on a visual Obsidian environment unsuited for the CPX21 headless transition, the overarching architectural logic embedded inside the agents/wiki-lint.md definitions and the hot.md caching schema are highly valuable. These specific patterns should be lifted, structurally adapted, and reimplemented natively." [Source: another Evaluating Code for Trading & Wiki Stacks 4_30.docx URL 2]

> **Wave 5B integration vector (URL 2 evaluation excerpt)**:
>
> "For the Workflow category, the concrete integration vector involves adopting the /autoresearch multi-round research loop and the specific wiki_lint.py implementation, which map perfectly to the solo developer's existing Obsidian and Dataview environment. The project's predefined markdown schemas, structured frontmatter logic, and explicit cross-linking conventions provide an off-the-shelf blueprint." [Source: another Evaluating Code for Trading & Wiki Stacks 4_30.docx URL 2]

> **Wave 5B risk caveat — Obsidian-plugin lock-in (URL 2 evaluation excerpt)**:
>
> "Adoption of this system introduces a significant risk of ecosystem lock-in, as it mandates the use of highly specific, third-party Obsidian plugins like 'Bases' and 'Local REST API'. If these community-maintained plugins are deprecated or abandoned, the entire Model Context Protocol connectivity stack will collapse." [Source: another Evaluating Code for Trading & Wiki Stacks 4_30.docx URL 2]
