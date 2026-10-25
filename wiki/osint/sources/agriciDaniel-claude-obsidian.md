---
title: "AgriciDaniel/claude-obsidian — Claude + Obsidian Knowledge Companion implementing Karpathy's LLM Wiki Pattern (MIT, Python, 3.6k★)"
type: source
tags: [github, claude-code-skill, knowledge-management, obsidian, second-brain, karpathy-pattern, librarian-tooling, mit-license, gemini-dr-wave5b, steal-from-tier]
keywords: [claude-obsidian, agriciDaniel, karpathy-llm-wiki-pattern, obsidian-vault, persistent-knowledge-engine, autoresearch-multi-round-loop, wiki-lint-py, hot-md-session-memory, wiki-save-slash-command, claude-code-skill, dataview-environment, model-context-protocol, mcp-bridge, second-brain-pattern, hooks-json, session-start-stop, program-md, dragonscale-memory]
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
  - sources/3-26-link-re-3.md
  - concepts/curator-skills.md
  - concepts/autoresearch-loop-pattern.md
  - sources/xskill-2603-12056.md
  - sources/gemini-sci-research-2602-03837.md
  - concepts/cemini-workflow-tooling-audit-2026-05-30.md
  - entities/tools/claude-osint.md
  - entities/tools/atlas-gic-autoresearch.md
  - sources/eval-multi-wiki-resource-plan-k247-2026-08-26.md
maturity: validated
read_status: deep-read
created: 2026-04-30
updated: 2026-04-30
---

## Relations

- @sources/gemini-dr-wave5b-osint-2026-04-30.md — Wave 5B canonical brief; URL 2 of 18; promoted to dedicated page from Steal-from verdict
- @sources/llm-wiki.md — Karpathy's foundational gist; claude-obsidian explicitly cites it in repo description and WIKI.md is a direct implementation
- @sources/atomicmemory-llm-wiki-compiler.md — Wave 4B Adopt for librarian server; three-way Karpathy-pattern stack
- @sources/wastedcode-memex.md — filesystem-only minimal Karpathy implementation
- @sources/alash3al-stash.md — Wave 5A Adopt; stash holds dynamic episodic memory in Postgres, claude-obsidian holds curated Markdown knowledge
- @concepts/wiki-tooling-evaluation.md — adoption decision parent
- @concepts/librarian-server-architecture.md — claude-obsidian's patterns inform the librarian's continuing evolution

## Raw Concept

- **Original title**: "Claude + Obsidian knowledge companion. Persistent, compounding wiki vault based on Karpathy's LLM Wiki pattern. /wiki /save /autoresearch"
- **Author**: AgriciDaniel (sole contributor)
- **Repository**: https://github.com/AgriciDaniel/claude-obsidian
- **Homepage**: https://agricidaniel.com/blog/claude-obsidian-ai-second-brain
- **License**: MIT (confirmed via Exa crawling 2026-04-30)
- **Primary language**: Python (69.0%) + Shell (29.0%) + Makefile (2.0%)
- **Stars**: 3,581 | **Forks**: 416 | **Contributors**: 1
- **Created**: 2026-04-07 (23 days old at evaluation) | **Last push**: 2026-04-24
- **Releases**: 6 (latest v1.6.0 on 2026-04-24)
- **Read status**: deep-read — full README + WIKI.md schema + hooks.json + program.md + wiki-lint.md agent + commands/autoresearch.md + commands/save.md + skills directory structure, all via raw.githubusercontent.com Exa crawling
- **Discovered via**: Wave 5B Gemini DR brief (2026-04-30)
- **Primary cluster**: librarian-tooling

## Narrative

### What it is

claude-obsidian is a Claude Code plugin + Obsidian vault that implements Karpathy's LLM Wiki pattern as a self-maintaining knowledge engine. It is the closest-relative Karpathy-pattern implementation to Cemini's workspace in the entire corpus — same four-page-type taxonomy (source/entity/concept/brief → source/entity/concept/domain), same index.md + log.md navigation, same ingest/query/lint operations. The gap is deployment posture: claude-obsidian is a visual Obsidian workstation; Cemini is a laptop+headless-server hybrid.

**11 skills** organized as Claude Code plugin skills: wiki (orchestrator), wiki-ingest, wiki-query, wiki-lint, save, autoresearch, canvas. Each skill has its own directory under `skills/` with a `references/` subdirectory for configuration. The architecture is modular — skills are independently callable, and the orchestrator skill routes user commands to the right sub-skill.

**Three slash commands** are the user-facing surface:
1. `/wiki` — bootstrap, scaffold, or continue where you left off
2. `/save` — persist the current conversation as a structured wiki note
3. `/autoresearch` — run a multi-round autonomous research loop

Additionally: `ingest [file]`, `ingest all of these` (batch), `lint the wiki`, `update hot cache`, and natural-language queries.

### File structure — where the IP lives

```
skills/
  wiki/                    # orchestrator + 7 reference files
  wiki-ingest/             # INGEST operation
  wiki-query/              # QUERY operation
  wiki-lint/               # LINT operation
  save/                    # /save: file conversations to wiki
  autoresearch/            # /autoresearch: autonomous research loop
    references/
      program.md           # ★ configurable research objectives + constraints
  canvas/                  # visual layer
commands/
  wiki.md                  # /wiki bootstrap command
  save.md                  # /save command
  autoresearch.md          # /autoresearch command
agents/
  wiki-ingest.md           # parallel ingestion agent
  wiki-lint.md             # health check agent
hooks/
  hooks.json               # ★ SessionStart + Stop + PostCompact + PostToolUse hooks
WIKI.md                    # ★ full schema reference (the project's CLAUDE.md equivalent)
```

### `/autoresearch` loop — the highest-value extract for Cemini Tier-2.5

The `/autoresearch` command (`commands/autoresearch.md`) dispatches to the `autoresearch` skill, which reads `program.md` for configuration before each run. This is the pattern Cemini should steal for Tier-2.5 sweep automation.

**Loop control structure** (from `program.md`):

| Parameter | Value | Cemini Tier-2.5 mapping |
|---|---|---|
| Max search rounds per topic | **3** | Map to: 1 round per cluster query, max 3 refinement rounds |
| Max wiki pages created per session | **15** | Map to: per-sweep cap on new source pages |
| Max sources fetched per round | **5** | Map to: Exa `numResults` per cluster query |
| Fallback on max-pages | File what you have, note skipped in Open Questions | Same pattern |

**Search objectives** (from `program.md`):
- Prefer .edu, peer-reviewed papers, official docs, primary sources, established publications
- Extract key entities, concepts, frameworks
- **Note contradictions between sources** — this is the refutation-premium signal Cemini already uses in `high-signal-paper-patterns.md`
- Identify open questions and research gaps
- Prefer sources from last 2 years unless foundational

**Confidence scoring** (from `program.md`):
- **high**: multiple independent authoritative sources agree
- **medium**: single good source, or sources partially agree
- **low**: speculation, opinion pieces, single informal source, or claim unverified
- Claims from sources >3 years old flagged as potentially stale

**Output discipline** (from `program.md`):
- Declarative, present tense. No hedging ("it seems", "perhaps", "might be")
- Cite every non-obvious claim inline
- Short pages: under 200 lines. Split if longer
- Flag uncertainty explicitly: `> [!gap] This claim needs verification.`

**DragonScale extension**: The repo includes an optional `docs/dragonscale-guide.md` with Mechanism 4 ("boundary-first, agenda-control, opt-in") that surfaces the top 5 "vault-frontier" pages as research candidates. The boundary score is a heuristic, not authoritative. When DragonScale is active, `/autoresearch` (no topic) offers these candidates but requires user confirmation before proceeding. For Cemini's purposes: the `wiki_gap_detect.py` Type A/D/E output already serves this function — the DragonScale mechanism is conceptually analogous but Obsidian-graph-dependent and not directly portable.

### `hooks.json` — session-state architecture (directly portable to Cemini)

This is the second-highest-value extract. The hooks file defines four lifecycle events:

```
SessionStart:
  1. cat wiki/hot.md (shell command)
  2. Prompt: silently read hot.md to restore context; don't announce it

PostCompact:
  Prompt: re-read hot.md after context compaction (hook-injected context doesn't survive compaction)

PostToolUse (matcher: Write|Edit):
  git add wiki/ .raw/ .vault-meta/ && auto-commit if changes detected

Stop:
  If wiki/ changed this session: prompt to update hot.md with summary (~500 words)
  Format: Last Updated, Key Recent Facts, Recent Changes, Active Threads
  "It is a cache, not a journal. Overwrite it completely."
```

**Cemini porting assessment**:
- **SessionStart hot.md read**: The Cemini workspace already has a `## Session-start ritual` in CLAUDE.md, but it's manual (check sweep cadence + inbox). The hot.md automatic-context-restore pattern would eliminate the "recap what I was doing" friction. This is the `cpr-pattern` extension the ROADMAP references.
- **PostCompact re-read**: Currently Cemini has no PostCompact hook. This would be a new capability — after context compaction, silently re-read the session-state file.
- **PostToolUse auto-commit**: Cemini already does this manually after each operation. Automating via hook would reduce the manual commit step but risks committing incomplete work. **Verdict**: keep manual commits for now; the hook pattern is noted but not adopted.
- **Stop hot.md update**: Cemini's log.md serves this function but is append-only and chronological. A hot.md-style overwrite cache would complement it — log.md for the audit trail, hot.md for fast context resumption.

### `wiki/hot.md` format — the session-resume cache

From `WIKI.md §2`:

```markdown
---
type: meta
title: "Hot Cache"
updated: 2026-04-07T14:30:00
---

# Recent Context

## Last Updated
2026-04-07 — Ingested 3 new YouTube transcripts

## Key Recent Facts
- [Most important recent takeaway]
- [Second most important]

## Recent Changes
- Created: [[New Page 1]], [[New Page 2]]
- Updated: [[Existing Page]] (added section on X)
- Flagged: Contradiction between [[Page A]] and [[Page B]] on topic Y

## Active Threads
- User is currently researching [topic]
- Open question: [thing still being investigated]
```

Rules: ~500 words max. Overwritten completely each time. It's a cache, not a journal.

**Cemini adoption**: This maps cleanly onto the workspace. Cemini's `log.md` is the journal (append-only, chronological). A `wiki/hot.md` would be the cache (overwrite, ~500 words, fast context restore). The two serve different purposes and don't conflict. The SessionStart hook reading hot.md would eliminate the current "check sweep cadence + inbox" manual ritual — those checks would still run, but the context of *what was being worked on* would be restored automatically.

### `wiki-lint.md` — 8 checks, 3 we're missing

The claude-obsidian lint agent (`agents/wiki-lint.md`) runs 8 checks. Cemini's `scripts/wiki_lint.py` covers 5 of them. Three are novel:

| Check | claude-obsidian | Cemini wiki_lint.py |
|---|---|---|
| Orphan pages | Yes | Yes |
| Dead wikilinks | Yes (wikilink resolution) | Yes (dangling refs) |
| Bidirectional gaps | — | Yes |
| Missing pages for mentioned concepts | Yes | Partially (Type A stubs) |
| Frontmatter quality | Yes (type, status, created, updated, tags) | Yes (type, maturity, created, updated) |
| Stale index entries | Yes | — |
| **Unlinked mentions** | **Yes** — entity names appearing without `[[ ]]` brackets | **No** |
| **Headings without content** | **Yes** | **No** |
| **Seed-page staleness** | **Yes** — pages with status `seed` not updated in 30+ days | **No** (analogous: thin-concept-pages Type E, but different threshold) |

**The three additions worth porting to Cemini**:

1. **Unlinked mentions**: Scan for entity/concept names appearing in body text without a wikilink or `@path` reference. This catches pages that *should* cross-reference but don't. Cemini's bidir-gap check catches A→B links where B doesn't link back, but doesn't catch "B is mentioned in A's text with no link at all."

2. **Headings without content**: Headings followed immediately by another heading with no body text between them. Simple structural check, cheap to implement.

3. **Seed-page staleness** (30-day threshold): Cemini's equivalent would be `maturity: draft` pages with `read_status: unread-stub` that haven't been updated in 30+ days. The existing Type A (cited-unread stubs) and Type E (thin concept pages) checks in `wiki_gap_detect.py` partially cover this, but don't have a staleness dimension.

### WIKI.md — the schema reference

`WIKI.md` is claude-obsidian's equivalent of Cemini's `CLAUDE.md`. It's 13 sections covering architecture, frontmatter schema, operations (scaffold/ingest/query/lint), hot cache, cross-project referencing, visual customization, git setup, Dataview dashboards, context-window management, REST API reference, canvas maps, and conventions.

**Structural comparison with Cemini's CLAUDE.md**:

| Dimension | claude-obsidian WIKI.md | Cemini CLAUDE.md |
|---|---|---|
| Architecture | 3 layers (raw/wiki/schema) | 3 layers (raw/wiki/schema) — identical |
| Page types | 7 (source/entity/concept/domain/comparison/question/meta) | 4 (source/entity/concept/brief) |
| Frontmatter | `type, status, created, updated, tags, related, sources` | `type, maturity, created, updated, tags, keywords, related, clusters` |
| Ingest flow | 11 steps (read → discuss → source page → entities → concepts → domain pages → overview → index → hot → log → contradictions) | 11 steps (preingest_check → read → discuss → source page → entities → concepts → index → log → scp → lint → commit) |
| Lint | 8 checks, report-only (no auto-fix) | 7 mechanical checks + human-read pass for contradictions |
| Session memory | hot.md (overwrite cache, ~500 words) | log.md (append-only journal) + CLAUDE.md session-start ritual |
| Cross-project ref | CLAUDE.md snippet for external projects | `briefs/` staging for claude.ai and Cemini distribution |
| External research | — (not specified; relies on Claude's built-in search) | Exa MCP (8 tools, scoped by purpose) |

The architectures are convergent — both derived from Karpathy's pattern. The differences are deployment-surface-driven: claude-obsidian adds Obsidian-specific features (canvas, Dataview, CSS, graph view); Cemini adds server-distribution features (scp to librarian, briefs staging, Exa MCP integration, preingest_check.py).

### Cross-project referencing pattern

claude-obsidian's "Cross-Project Power Move" (`WIKI.md §6`) lets any Claude Code project read the vault without duplicating context. Cemini's equivalent is the `briefs/` → claude.ai / Cemini distribution pipeline, but claude-obsidian does it differently — external projects read the vault *live* rather than receiving staged exports:

```markdown
## Wiki Knowledge Base
Path: ~/path/to/vault

When you need context not already in this project:
1. Read wiki/hot.md first (recent context cache)
2. If not enough, read wiki/index.md
3. If you need domain details, read the relevant domain sub-index
4. Only then drill into specific wiki pages
```

Token cost: hot.md ~500 tokens, index ~1,000 tokens, individual pages 100-300 each. This is a read-optimized pattern — the external project queries the vault on-demand rather than receiving pre-staged briefs. For Cemini: the `briefs/` pipeline is better for the server (no live vault read during trading hours), but the hot.md-first pattern would improve the laptop-side session-resume flow.

### Why this matters for Cemini

**Workflow tier — three directly portable extracts:**

1. **`/autoresearch` loop → Tier-2.5 sweep automation**: The loop control parameters (3 rounds, 15 pages max, 5 sources/round) + confidence scoring (high/medium/low) + output discipline (declarative, no hedging, cite everything) form a complete specification for porting the current manual Tier-2 sweep into a parameterized automated loop. The `program.md` file is the configuration surface — Cemini would create its own `scripts/tier25_sweep_config.yaml` with domain-specific constraints (prefer arXiv q-fin + cs-CL + cs-AI categories, prefer last 14 days, etc.).

2. **`hooks.json` → session-resume pattern**: SessionStart (silently read hot.md) + Stop (update hot.md if changes) + PostCompact (re-read hot.md). This directly extends the cpr-pattern the ROADMAP references. The existing CLAUDE.md session-start ritual (check sweep cadence + inbox) would remain but be supplemented by automatic context restore.

3. **`wiki-lint` additions → `scripts/wiki_lint.py` v2**: Three new checks — unlinked mentions, headings without content, seed-page staleness (30-day threshold). The unlinked-mentions check is the highest-value addition.

**Wiki/Librarian server tier — partial fit:**

- The `hot.md` cache pattern maps cleanly to the librarian's need for fast context resumption across sessions. If Cemini's librarian were a Claude Code session rather than the current atomicmemory headless compiler, the hooks.json pattern would be drop-in.
- The REST API reference (`WIKI.md §11`) is Obsidian-specific (Local REST API plugin on port 27124) and not portable to the headless CPX21 server. The MCP bridge patterns (Option A: REST API, Option B: filesystem via mcpvault) are noted but not adopted.

**Cemini production stack — no-fit.** Obsidian visual environment + Local REST API plugin dependency are incompatible with headless trading deployment.

### Risks & open questions

1. **Bus-factor: 1 contributor** — same fork-and-maintain caveat as other Wave 5 projects. Mitigation: extract patterns into Cemini-bespoke implementations.
2. **Obsidian-plugin lock-in**: "Bases" + "Local REST API" plugins are community-maintained. Risk acceptable for workflow-tier extraction.
3. **Project age**: 23 days old at evaluation. 3.6k stars in ~3 weeks is strong signal, but the project could pivot or be abandoned. Re-evaluate at next wave touch.
4. **`/autoresearch` token cost** [OPEN QUESTION 2026-04-30] — measure exact token-consumption rate of the multi-round loop on a representative Cemini session.

### Cemini-side adoption assessment

**Decision**: **Steal-from the patterns. Do not adopt the runtime.**

Three concrete extracts, ordered by implementation priority:

1. **Port `/autoresearch` loop → `scripts/tier25_sweep.py`** (3-4 hours). Configuration in `scripts/tier25_sweep_config.yaml`. Parameters: 3 rounds, 15 pages max, 5 sources/round, confidence scoring. Replace the current manual Tier-2 weekly cadence with a parameterized loop. The existing `wiki_gap_detect.py` Type A/D/E output serves as the candidate-source function (analogous to DragonScale Mechanism 4).

2. **Implement `wiki/hot.md` session-resume cache** (1-2 hours). Create `wiki/hot.md` with the claude-obsidian format. Add SessionStart hook logic (silently read hot.md) to CLAUDE.md session-start ritual. Add manual "update hot cache" step to the ingest workflow closeout. The hot.md is a cache, not a journal — overwrite completely each time, keep under 500 words.

3. **Add three lint checks to `scripts/wiki_lint.py`** (1-2 hours). Unlinked mentions (entity names without @refs), headings without content, stale-draft-page detection (maturity=draft + updated >30 days ago).

License + IP-sale-readiness disposition: **clean for Steal-from**. MIT license. Pattern extraction with Cemini-bespoke reimplementation is unambiguously safe.

### Citation

> AgriciDaniel. (2026). *claude-obsidian — Claude + Obsidian knowledge companion*. v1.6.0. GitHub. https://github.com/AgriciDaniel/claude-obsidian (License: MIT; deep-read 2026-04-30 via Exa crawling of README.md, WIKI.md, hooks.json, commands/autoresearch.md, skills/autoresearch/references/program.md, agents/wiki-lint.md)

## Snippets

> **Repo identity**
>
> "Claude + Obsidian knowledge companion. Persistent, compounding wiki vault based on Karpathy's LLM Wiki pattern. /wiki /save /autoresearch" [Source: github.com/AgriciDaniel/claude-obsidian README]

> **Loop constraints — the exact parameters from program.md**
>
> "Max search rounds per topic: 3. Max wiki pages created per session: 15. Max sources fetched per round: 5. If max pages is reached before the loop completes: file what you have, note what was skipped in Open Questions." [Source: skills/autoresearch/references/program.md]

> **Confidence scoring**
>
> "Label every claim with confidence when filing: high — multiple independent authoritative sources agree; medium — single good source, or sources partially agree; low — speculation, opinion pieces, single informal source, or claim not verified. Always note the source date for factual claims. Mark claims from sources older than 3 years as potentially stale." [Source: skills/autoresearch/references/program.md]

> **Output discipline**
>
> "Declarative, present tense. Cite every non-obvious claim. Short pages: under 200 lines. Split if longer. No hedging language ('it seems', 'perhaps', 'might be'). Flag uncertainty explicitly: `> [!gap] This claim needs verification.`" [Source: skills/autoresearch/references/program.md]

> **SessionStart hook — automatic context restore**
>
> "If a vault is configured for this session (check CLAUDE.md for VAULT_PATH or a wiki/ folder in the current directory), silently read wiki/hot.md to restore recent context. If wiki/hot.md does not exist, do nothing. This is a non-vault session. Do not announce this. Do not report what you read. Just have the context available." [Source: hooks.json SessionStart prompt hook]

> **PostCompact hook — re-restore after compaction**
>
> "Hook-injected context does not survive context compaction. If wiki/hot.md exists in the current directory, silently re-read it now to restore the hot cache. Do not announce this." [Source: hooks.json PostCompact prompt hook]

> **Stop hook — update hot cache**
>
> "If wiki pages were modified this session: update wiki/hot.md with a brief summary of what changed (under 500 words). Use the hot cache format: Last Updated, Key Recent Facts, Recent Changes, Active Threads. Keep it factual. Overwrite the file completely. It is a cache, not a journal." [Source: hooks.json Stop command hook]

> **Hot cache format**
>
> "hot.md is a ~500-word summary of the most recent context. It exists so that other projects pointing at this vault can get recent context without crawling the full wiki. Update hot.md after every ingest, after any significant query exchange, and at the end of every session." [Source: WIKI.md §2]

> **Wiki lint — 8-category check**
>
> "For each wiki page, check: frontmatter has required fields (type, status, created, updated, tags); all wikilinks in the page resolve to real files; all headings have content underneath them; page is linked from at least one other page (no orphans). Scan for concepts and entities mentioned in multiple pages but lacking their own page. Scan for unlinked mentions (entity names appearing without [[ ]] brackets). Check index.md for stale entries pointing to renamed/deleted files. Identify pages with status 'seed' that have not been updated in over 30 days." [Source: agents/wiki-lint.md]

> **Wave 5B Steal-from rationale**
>
> "Steal-from. While the full installation relies heavily on a visual Obsidian environment unsuited for the CPX21 headless transition, the overarching architectural logic embedded inside the agents/wiki-lint.md definitions and the hot.md caching schema are highly valuable. These specific patterns should be lifted, structurally adapted, and reimplemented natively." [Source: Gemini DR Wave 5B brief, URL 2 evaluation]

> **Wave 5B integration vector**
>
> "For the Workflow category, the concrete integration vector involves adopting the /autoresearch multi-round research loop and the specific wiki_lint.py implementation, which map perfectly to the solo developer's existing Obsidian and Dataview environment." [Source: Gemini DR Wave 5B brief, URL 2 evaluation]
