---
title: obsidian-llm-wiki-local — Karpathy LLM Wiki Maintenance Toolkit (Python)
type: entity
tags: [tool, wiki-tooling, karpathy-pattern, mit-license, steal-from-tier, python, laptop-only, phase1-audited, partial-adopted]
keywords: [olw, obsidian-wiki, llm-wiki-compiler, wiki-lint-upgrade, json-retry-system, orphan-handling, wikilink-normalization, kytmanov]
related:
  - sources/5-6-links-eval-batch.md
  - concepts/cemini-license-posture.md
  - concepts/librarian-server-architecture.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/academic-paper-skills.md
  - entities/tools/codex-startup-pressure-test-skill.md
  - entities/tools/research-paper-writing-skills.md
maturity: validated
phase2_ported_as: scripts/_llm_retry.py (2026-05-10)
created: 2026-05-06
updated: 2026-05-11
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

- **URL**: `https://github.com/kytmanov/obsidian-llm-wiki-local` ✓ verified via DR + Phase 1 audit 2026-05-06
- **License**: ✓ **MIT confirmed** Phase 1 audit (`/tmp/olw-audit/LICENSE`, "Copyright (c) 2026 kytmanov")
- **Stack**: Python package `obsidian_llm_wiki` under `pyproject.toml`; CLI entrypoint `olw`. Pydantic + OpenAI-compat / Ollama clients
- **Architecture**: persistent file watcher (`olw watch`), maintenance commands (`olw maintain --fix`), git-integration with `[olw]` commit prefix
- **Code layout**: ~30 source modules + ~30 test modules. Proper Python project, not a script collection.
- **Maturity**: indicators not extracted from gh API in this audit pass; proper Phase-0 maintenance-velocity check deferred — code-port is the value, not adoption.

### What's worth stealing (concrete code targets)

DR identified four high-value patterns embedded in the upstream code:

**1. Three-tier JSON retry system for malformed LLM outputs**

> "To ensure stability when interacting with smaller local models, it employs a sophisticated 3-tier JSON retry system to gracefully handle occasionally malformed LLM outputs."

✓ **Phase 1 audit located at** `/tmp/olw-audit/src/obsidian_llm_wiki/structured_output.py:195-311` (`request_structured()`). Implementation richer than the brief originally sketched:

- **Tier 1**: LLM call with `format="json"` mode + Pydantic-template-based system prompt (`_make_template()` builds a fill-in JSON example from the model schema; small models echo less than they would for raw JSON Schema). Direct `json.loads()` + Pydantic validation.
- **Tier 2**: `_extract_json()` tries 3 sub-patterns in order: ` ```json` fenced block → bare ` ``` ` block with `{...}` → first `{...}` substring of any kind. Then `_try_parse()`.
- **Tier 3**: Re-prompt the model with `f"Your previous response was invalid.\nError: {last_error}\n\nOriginal request:\n{prompt}\n\nRespond with ONLY valid JSON matching the schema. Nothing else."`. Loop up to `max_retries=2`.
- **Bonus**: `_unwrap()` post-processor handles 3 common LLM mis-wrappings (single-key dict, single-key string-encoded JSON, JSON-Schema-echo with `properties` wrapper). Invalid-escape recovery in `_try_parse()` re-escapes backslashes when the parse fails on `Invalid \escape`. Telemetry per tier/attempt via `LLMCallEvent`.

**Workspace-side Phase 1 audit findings (revised port plan)**:

Phase 1 also found that `scripts/preingest_check.py` is pure-Python heuristic dedup — it makes **zero LLM calls**. Grep confirmed no file under `scripts/` calls DeepSeek/OpenAI APIs. So the workspace-laptop side has no LLM-call path to retrofit today. The Cemini-prod side does (LangGraph orchestrator, FastMCP tools), but those live at `/opt/cemini/`, not in this workspace.

Decision recorded 2026-05-06: **defer Phase 2 port** (`scripts/_llm_retry.py`) until the brief-audit-upgrade sprint introduces `scripts/skill_audit.py --llm-mode` as the first real consumer. Building the helper preemptively against an imagined consumer would yield a wrong-shape API. See `briefs/2026-05-06_obsidian-llm-wiki-local-steal-from.md` for full rollout plan.

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

### Adoption status — Phase 2 PORTED as `scripts/_llm_retry.py` (2026-05-10)

**Shipped 2026-05-10** alongside `scripts/skill_audit.py` v0.5 (the brief-audit-upgrade sprint produced the first real consumer, validating the deferred-port decision from 2026-05-06).

**What was ported**:
- All 3 tiers of the retry system (`request_structured()` in `scripts/_llm_retry.py:201-307`)
- Helpers preserved: `_resolve_ref`, `_render_example`, `_make_template`, `_schema_system`, `_extract_json`, `_unwrap`, `_try_parse`
- New helpers: `_get_client` (creates `openai.OpenAI(api_key, base_url)` from `DEEPSEEK_API_KEY` env var), `_emit_telemetry` (single stderr log line per call)
- Custom `StructuredOutputError` exception preserved

**What was changed from upstream**:
- Stripped Ollama-specific bits (upstream supports both Ollama and OpenAI-compat; we only need DeepSeek)
- Replaced `LLMCallEvent` telemetry infrastructure with a simple stderr log line — the workspace has no LLMCallEvent consumer, building one preemptively would add infrastructure with no consumer
- Tier 1 prompt is unchanged (fill-in-template approach — small-model discipline carried over even though DeepSeek is a frontier model, since the technique is harmless on big models and we plan to retain optionality for cheaper models later)
- Module-level defaults `DEFAULT_MODEL = "deepseek-chat"` + `DEFAULT_BASE_URL = "https://api.deepseek.com/v1"` for ergonomics

**Calibration** (`scripts/skill_audit.py --llm-mode` against `briefs/2026-05-10_aris-adoption.md`):
- Tier 1 success in 14805ms on first try
- No Tier 2 fallback needed (DeepSeek returned clean JSON via `response_format={"type": "json_object"}`)
- 4-mode combined Pydantic schema validated cleanly
- Telemetry line: `[_llm_retry] stage=skill_audit_dynamic model=deepseek-chat tier=1 retries=0 latency_ms=14805 status=ok`

**Phases 3-4 NOT ported**:
- Phase 3 (orphan-suggestion mode in `wiki_lint.py`): deferred — pain-driven; current 10 orphans are manageable
- Phase 4 (bidirectional wikilink normalization auto-rewrite): deferred — risk of false-positive rewrites; manual lint flags are sufficient today

**Risk assessment**:
- `_llm_retry.py` is a clean library file (no global state, no I/O beyond stderr telemetry, fully testable). Maintenance burden minimal — DeepSeek's JSON mode is now stable enough that Tier 1 catches everything in practice; Tier 2/3 are paranoia for legacy clients.
- The decision to port-on-demand (rather than preemptively) was correct: the helper's API shape was driven by `skill_audit.py`'s actual needs (e.g., `stage=` parameter for telemetry tagging, `api_key=` override for tests), not invented.

Phase-0 audit clone retained at `/tmp/olw-audit/` for reference. No package installed; no global `olw` symlink. Brief `briefs/2026-05-06_obsidian-llm-wiki-local-steal-from.md` now in DONE status for Phase 1+2.

## Snippets

### 3-tier JSON retry system (DR direct quote)

> "To ensure stability when interacting with smaller local models, it employs a sophisticated 3-tier JSON retry system to gracefully handle occasionally malformed LLM outputs." [Source: 5_6 links.docx URL 17]

### Self-healing maintenance commands

> "Crucially, it includes robust self-healing maintenance commands (such as olw maintain --fix) designed to programmatically repair broken links, handle orphaned articles, and normalize the wiki structure." [Source: 5_6 links.docx URL 17]

### Why STEAL-FROM not REPLACE (DR's own framing)

> "Retain the atomicmemory/llm-wiki-compiler (Node.js) strategy for the dedicated CPX21 librarian server because of its critical built-in MCP capability. However, deeply study and steal the Python code from obsidian-llm-wiki-local to permanently upgrade the laptop's local wiki_lint.py script — specifically extracting the robust 3-tier JSON retry system and the sophisticated orphan and wikilink normalization logic." [Source: 5_6 links.docx URL 17]

## Dead Ends

*(none — clean steal-from candidate, brief staged for execution.)*
