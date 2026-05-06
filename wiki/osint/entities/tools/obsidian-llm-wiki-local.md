---
title: obsidian-llm-wiki-local — Karpathy LLM Wiki Maintenance Toolkit (Python)
type: entity
tags: [tool, wiki-tooling, karpathy-pattern, mit-license, steal-from-tier, python, laptop-only]
keywords: [olw, obsidian-wiki, llm-wiki-compiler, wiki-lint-upgrade, json-retry-system, orphan-handling, wikilink-normalization, kytmanov]
related:
  - sources/5-6-links-eval-batch.md
  - concepts/cemini-license-posture.md
  - concepts/librarian-server-architecture.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
---

## Relations

- @sources/5-6-links-eval-batch.md — origin source: K32 Gemini DR eval URL 17, **STEAL-FROM** tier (highest action-value of the K32 batch)
- @concepts/cemini-license-posture.md — MIT-licensed, IP-clean
- @concepts/librarian-server-architecture.md — kb-server (the Node.js MCP serving layer described there) STAYS per K30 decision; this tool's value is in lint/maintenance code, NOT serving — STEAL-FROM not REPLACE
- @concepts/wiki-tooling-evaluation.md — sister tool-class evaluation; this is a Python implementation of the same Karpathy LLM Wiki pattern Cemini uses

## Raw Concept

Python-based local-first orchestrator for Obsidian-style markdown knowledge bases following Karpathy's LLM Wiki pattern. Maintained by `kytmanov` at `github.com/kytmanov/obsidian-llm-wiki-local`.

K32 DR verdict: **STEAL-FROM**. Don't install the full CLI globally (it has its own opinions about Git commit prefixes that conflict with Cemini's existing workflow). DO study and port the lint/maintenance code into laptop-side `scripts/wiki_lint.py`.

This is the highest-action-value finding in the K32 batch.

## Narrative

- **URL**: `https://github.com/kytmanov/obsidian-llm-wiki-local` ✓ verified via DR
- **License**: MIT (per DR; needs upstream verification before code-port)
- **Stack**: Python CLI (`olw <command>`)
- **Architecture**: persistent file watcher (`olw watch`), maintenance commands (`olw maintain --fix`), git-integration with `[olw]` commit prefix
- **Maturity**: not extracted from DR; need direct upstream check

### What's worth stealing (concrete code targets)

DR identified four high-value patterns embedded in the upstream code:

**1. Three-tier JSON retry system for malformed LLM outputs**

> "To ensure stability when interacting with smaller local models, it employs a sophisticated 3-tier JSON retry system to gracefully handle occasionally malformed LLM outputs."

This is directly applicable to Cemini's `scripts/preingest_check.py` (when LLM is asked to return frontmatter or graph data) and any future LLM-driven script. The 3-tier pattern likely involves:

- **Tier 1**: parse raw output as JSON; if it parses, accept
- **Tier 2**: extract first JSON-shaped block from prose with regex; retry parse
- **Tier 3**: re-prompt the LLM with the raw bad output and ask "fix this to valid JSON"

Cemini currently has no such pattern; failed JSON outputs from DeepSeek calls are treated as opaque errors.

**2. Programmatic broken-link repair (`olw maintain --fix`)**

> "Robust self-healing maintenance commands (such as olw maintain --fix) designed to programmatically repair broken links, handle orphaned articles, and normalize the wiki structure."

Cemini's `scripts/wiki_lint.py` currently flags broken links as warnings — `olw maintain --fix` likely auto-rewrites them when the LLM can identify the intended target. Risk: false-positive rewrites can corrupt the wiki. Adopt only with explicit human-confirm step.

**3. Orphan handling**

Cemini currently tracks 10 orphans (8 baseline + 2 intentional). `obsidian-llm-wiki-local` likely has logic for:

- Suggesting backlinks for orphans (LLM proposes target page based on body content)
- Auto-creating stub pages for orphan-mentioned-but-nonexistent topics

**4. Bidirectional `[[wikilink]]` normalization**

> "the sophisticated orphan and wikilink normalization logic"

Cemini uses `@path/to/page.md` syntax (not Obsidian `[[wikilink]]`); the value is in the **bidirectional invariant enforcement** algorithm, not the syntax.

### What NOT to take from this tool

- **`[olw]` commit prefix**: Cemini uses standard conventional-commits via `commit-commands` plugin; an automated tool stamping all wiki commits with `[olw]` would conflict.
- **Watcher mode (`olw watch`)**: Cemini intentionally has manual ingest discipline (preingest_check → human review → write). Auto-watching new files would defeat the duplicate-detection step.
- **Full CLI install globally**: keep code-extracted as `scripts/`-level imports; do NOT add `olw` to PATH.

### Why STEAL-FROM, not ADOPT

This tool reuses kb-server's serving role (it has no built-in MCP server, per DR), so adopting it wholesale would require ditching kb-server. K30 confirmed kb-server is the right serving layer. So we keep kb-server and steal the maintenance/lint patterns into laptop tooling.

The K30/K28/K30 Phase-0 audit pattern says: when a tool overlaps Cemini's existing coverage, prefer to extract the novel parts rather than swap the existing tool out.

### Brief planned

`briefs/2026-05-06_obsidian-llm-wiki-local-steal-from.md` — port plan for laptop-side `scripts/wiki_lint.py` upgrade. Specifically:

1. Phase 1: clone upstream + read code under `/tmp/obsidian-llm-wiki-local-audit/`
2. Phase 2: extract 3-tier JSON retry into `scripts/_llm_retry.py` helper
3. Phase 3: add wiki_lint.py orphan-suggestion mode (LLM-proposed backlinks, human-confirm)
4. Phase 4: bidirectional wikilink normalization (apply to existing `@path` violations flagged by current lint)

Estimated effort: 2-4 hours for Phase 1+2, deferred Phase 3+4 until pain-driven.

### Open questions

- ⚠ Verify MIT license on upstream LICENSE file (DR claim, not directly checked)
- ⚠ Project maturity (commits, last push, star count) — DR didn't surface
- ⚠ How does the 3-tier retry interact with rate limits? Does Tier 3 (re-prompt) consume budget aggressively?
- ⚠ Does `olw maintain --fix` have a `--dry-run` mode for human-review before commit?
- ⚠ How does it handle nested entity directories (`entities/companies/`, `entities/tools/`)? — relevant since K28/K30 flagged hardcoded-flat-layout as failure mode

### Adoption status — STEAL-FROM, NOT ADOPTED

Phase-0 code-port deferred to brief execution (`briefs/2026-05-06_obsidian-llm-wiki-local-steal-from.md`). No package installed; no global `olw` symlink.

## Snippets

### 3-tier JSON retry system (DR direct quote)

> "To ensure stability when interacting with smaller local models, it employs a sophisticated 3-tier JSON retry system to gracefully handle occasionally malformed LLM outputs." [Source: 5_6 links.docx URL 17]

### Self-healing maintenance commands

> "Crucially, it includes robust self-healing maintenance commands (such as olw maintain --fix) designed to programmatically repair broken links, handle orphaned articles, and normalize the wiki structure." [Source: 5_6 links.docx URL 17]

### Why STEAL-FROM not REPLACE (DR's own framing)

> "Retain the atomicmemory/llm-wiki-compiler (Node.js) strategy for the dedicated CPX21 librarian server because of its critical built-in MCP capability. However, deeply study and steal the Python code from obsidian-llm-wiki-local to permanently upgrade the laptop's local wiki_lint.py script — specifically extracting the robust 3-tier JSON retry system and the sophisticated orphan and wikilink normalization logic." [Source: 5_6 links.docx URL 17]

## Dead Ends

*(none — clean steal-from candidate, brief staged for execution.)*
