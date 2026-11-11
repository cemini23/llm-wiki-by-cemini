---
title: "deja-vu — local index of every agent session on disk (MIT)"
type: entity
tags: [tool, memory, agents, session-recall, local, ccc]
keywords: [deja-vu, deja, session transcripts, jsonl, sqlite, compaction, rejected decisions, exclude]
related:
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10-11-2026-11-05.md"
maturity: draft
created: 2026-11-05
updated: 2026-11-10
wire_status: runtime_wired
wire_target: "~/.local/bin/deja and ~/.config/deja/exclude"
wire_note: 2026-11-10. Binary v0.24.1 installed after the exclude list. Desktop/family and AttoVault are excluded. deja install was not run. deja embed was not run.
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-link-revenue-v10-11-2026-11-05.md, URL 7, **Integrate** — the only one in the batch.

The question this page answers: **what can you recover from sessions that already happened, without asking a model anything?**

## Narrative

### What it is

`vshulcz/deja-vu`. **MIT**, ~1.4k stars. A local Go binary, `deja`.

It reads the session transcripts your agents **already wrote to disk** and builds an index. It parses JSONL and SQLite stores, and tracks more than chat: **files opened, commands with their exit codes, and the exact spans an `Edit` replaced**.

**43 harnesses** covered, including Claude Code, Codex CLI, Cursor, OpenCode, Gemini CLI, Cline, Windsurf, Copilot CLI, aider, Amp, Goose, and Zed. A few are partial — TRAE IDE is "wired, not read" because its chats sit in an encrypted database.

Published figures: **13.6 s to index 19,195 sessions**, a 232 MB index for a 5.7 GB corpus. Incremental — a file is re-read only when it changes.

### Zero LLM calls

Indexing and search are local. **No cloud account, no model.** That is the entire appeal in this workspace: it recovers context that was never captured anywhere else, at zero token cost, from data that is already sitting on the disk.

The specific thing it fixes is **compaction amnesia**. When a session is compacted, the summary keeps the conclusions and drops the path — which commands failed, which approach was tried and abandoned. An index over the raw transcripts keeps the path.

`deja promote --state rejected` is the mechanism for the second half: marking an approach as rejected so a future session is warned rather than repeating it.

### Phase-0, 2026-11-05 — the caveat that did not make the report

**Redaction happens at index time, not at source.**

> Credentials are redacted at index time, but the original transcripts keep them.

So the index is safer than the corpus it describes, and the corpus is the thing on disk. `deja secrets` lists affected sessions; `deja scrub` rewrites what it can and keeps a backup.

Any session where a key was printed to the terminal has that key in the transcript, and has had it since it ran. `deja` neither caused that nor fixes it — but it does make the corpus **searchable**, which changes how exposed it is.

### The configuration that matters here

- **`~/.config/deja/exclude`** — skip a project per line, or a whole store with `harness:<name>`. Env vars `DEJA_EXCLUDE_PROJECTS` and `DEJA_EXCLUDE_HARNESSES`.
- **`policy.json` `"ignore"`** — shell globs matched against session path and project, excluded from recall and sync.
- **`DEJA_OFFLINE=1`** — disables the update notice and the network paths.
- **`deja forget`** — drops sessions and keeps them dropped across rebuilds.
- **`deja embed`** is the one outbound path: redacted text, about 2k characters, to whichever endpoint is configured. Do not enable it.

For this estate the exclude list must cover `Desktop/family/` and `~/AttoVault/` before the first index — not after.

### The honest limit

It indexes **what exists**. Sessions that were never written to disk, or were deleted, are gone. It is recall, not backup.

### Status

Integrate, with the exclude list configured first.

## Snippets

> "13.6 s to index 19,195 sessions" and a 232 MB index for a 5.7 GB corpus. — README [fetched 2026-11-05]

> "Credentials are redacted at index time, but the original transcripts keep them." — README [fetched 2026-11-05]

> "`~/.config/deja/exclude` skips a project per line, or a whole store with `harness:opencode`" — README [fetched 2026-11-05]

## Dead Ends

- **Treating the index as scrubbed source data.** Redaction is at the index; the transcripts are unchanged.
- **Enabling `deja embed`.** It is the only outbound path.
- **Indexing before writing the exclude list.** The order matters.
