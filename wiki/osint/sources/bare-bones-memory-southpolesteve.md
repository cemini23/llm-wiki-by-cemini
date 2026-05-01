---
title: southpolesteve/Bare Bones Memory — Session Continuity Protocol (Markdown Gist, Methodology-Only)
type: source
tags: [llm-tooling, memory-protocol, session-continuity, agents-md, markdown-only, claude-code, gist, workflow-adopt, license-unfound]
keywords: [bare-bones-memory, agents-md, active-projects-md, session-logs, southpolesteve, gist-protocol, session-state, durable-memory, no-runtime, methodology-only]
related:
  - sources/gemini-dr-link-eval-2026-04-28.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/context-compression-resume-pattern.md
  - sources/atomicmemory-llm-wiki-compiler.md
maturity: validated
read_status: deep-read
created: 2026-04-28
updated: 2026-04-28
clusters: [llm-agents, librarian-tooling]
---

## Relations

- @sources/gemini-dr-link-eval-2026-04-28.md — parent canonical Gemini DR source
- @concepts/wiki-tooling-evaluation.md — Wave 2 evaluation parent
- @concepts/context-compression-resume-pattern.md — companion concept; cpr-pattern handles in-session compression while Bare Bones Memory handles cross-session continuity. Distinct timescales, complementary protocols
- @sources/atomicmemory-llm-wiki-compiler.md — the bare-bones AGENTS.md structure could be a canonical input shape for the llm-wiki-compiler's index, providing a stable pointer to "what's currently active" alongside `wiki/index.md`

## Raw Concept

- **URL**: https://gist.github.com/southpolesteve/b39a3528790bc99fe3f2c2b9e3263ef8
- **Type**: GitHub Gist / Markdown documentation protocol
- **License**: NOT FOUND (Standard GitHub TOS applies to hosted text; methodology-only, no executable code → IP-taint risk effectively zero)
- **Stack**: Markdown only — no runtime, no daemon, no embeddings
- **Author**: southpolesteve (gist owner)
- **Retrieved**: 2026-04-28 (gist revision histories hidden by GitHub)
- **Read status**: snapshot 2026-04-28

## Narrative

### What it is
A purely text-based, lightweight protocol defining how autonomous AI agents should manage their own state and maintain session continuity across disjointed interactions. Establishes a strict directory hierarchy:
- `active-projects.md` — the current state of in-flight work
- `projects/` — durable per-project files (continuously updated, not regenerated)
- `session-logs/` — chronologically-named log files (e.g., `YYYY-MM-DD-session-NNN.md`)

The protocol dictates a rigid behavioral loop: agents must
1. Read state files on session initiation
2. Continuously update durable project files during execution (rather than generating new documents)
3. Generate chronological log files prior to session termination

### Why Adopt-for-Workflow

This methodology directly addresses the chronic session-to-session memory loss experienced in the Obsidian + Claude Code laptop environment. Reasoning:

1. **Pure methodology, zero runtime** — RAM/disk/compute footprint is functionally zero. No tool to install, no daemon to maintain. Implementation is editing system prompts to enforce the protocol.
2. **Ip-taint risk = 0** — the LICENSE field is not found, but the artefact is documentation/methodology, not executable code. Reading and adopting a folder structure does not transitively contaminate the proprietary codebase.
3. **Solves a known workspace pain point** — the workspace has previously hit context loss across `/compact` boundaries; explicit session-log + active-projects discipline gives Claude Code a deterministic state-recovery path.
4. **Composes with existing wiki structure** — `active-projects.md` slots into the workspace as a sibling of `ROADMAP.md`; `session-logs/YYYY-MM-DD-session-NNN.md` slots into the workspace as a sibling of `wiki/log.md`.

### Where it falls short

1. **Cemini production stack fit: ❌** — production trading agents need ACID-compliant databases (PostgreSQL/Redis), not local filesystem Markdown state. Don't apply this protocol to runtime agent state.
2. **Wiki / librarian server fit: ⚠️** — useful as an organizational hierarchy for the synced Markdown content (could standardize the AGENTS.md root index). But provides no deployable codebase.
3. **Scalability** — plain text chronological log aggregation scales poorly over hundreds of iterations. Without periodic algorithmic compaction (e.g., `wiki_lint.py` truncation), the LLM context window will eventually saturate with irrelevant historical session metadata. Pair with cpr-pattern for compression discipline.

### Integration vector

```
~/Desktop/OSINT WORKSPACE/  (existing structure)
├── ROADMAP.md          (existing — co-aligned with bare-bones)
├── CLAUDE.md           (existing schema)
├── wiki/log.md         (existing — already chronological)
└── memory/             (NEW per Bare Bones)
    ├── AGENTS.md           (root index, lists active projects + protocols)
    ├── active-projects.md  (in-flight work state)
    ├── projects/           (durable per-project files)
    │   ├── librarian-server-migration.md
    │   ├── omc-evaluation.md
    │   └── ...
    └── session-logs/       (per-session terminal logs)
        ├── 2026-04-28-session-001.md
        ├── 2026-04-28-session-002.md
        └── ...
```

The workspace already has a partial implementation: `wiki/log.md` is the canonical session chronology, and `ROADMAP.md` plays the active-projects role. Adopting Bare Bones formally would mean adding the `memory/` subtree and patching the Claude Code session prompt to require session-log writes before every `/compact` boundary.

### License caveat

Gemini's evaluation flagged "License: NOT FOUND" and noted "Verification is required to determine whether the original gist author has appended a formal Unlicense, CC0, or MIT tag in recent revisions to clarify the public domain status of the documentation." Since this is methodology-only, the workspace can adopt without legal exposure — but if the author ever publishes the protocol as installable executable code, the license must be verified before that point.

### Risks & open questions

1. **Long-term scalability without compaction** — file the bare-bones cron pairing with `wiki_lint.py` truncation to bound session-logs growth.
2. **License clarification** [NEEDS VERIFICATION 2026-04-29] — periodic check of the gist for Unlicense/CC0/MIT tag.
3. **Conflict with cpr-pattern boundaries** — cpr handles in-session memory; Bare Bones handles cross-session. Both should coexist; potential adapter work is required to ensure the post-task summary fed to cpr is also written to `session-logs/` per Bare Bones' protocol.

## Snippets

> "Bare Bones Memory" — purely text-based, lightweight protocol defining how autonomous AI agents should manage their own state and maintain session continuity across disjointed interactions. [Source: Gemini DR report, URL 4]

> "Adopt for Workflow. Manually scaffold the AGENTS.md and active-projects.md file structures directly into the canonical Obsidian vault on the laptop. This establishes immediate, reliable state permanence for Claude Code sessions." [Source: Gemini DR report, URL 4]

> "The primary limitation of this pattern involves long-term scalability. Plain text chronological log aggregation scales exceptionally poorly over hundreds of iterations. Without periodic algorithmic compaction or external summarization—such as executing the existing wiki_lint.py script to truncate historical context—the LLM's context window will eventually become saturated with irrelevant historical session metadata." [Source: Gemini DR report, URL 4 — Risks & caveats]
