---
title: K281 Harness Wave (Oct 2026)
type: concept
tags: [agents, harness, skills, k281, basgiath]
keywords: [k281, agent-skills, field-notes, canonical-instructions, FILE]
related:
  - concepts/k279-harness-wave.md
  - sources/universal-modder-2026-10-04.md
  - sources/substack-rss-moontower-2026-10-04-330.md
maturity: draft
created: 2026-10-04
updated: 2026-10-04
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k279-harness-wave.md
- @sources/universal-modder-2026-10-04.md
- @sources/substack-rss-moontower-2026-10-04-330.md

## Raw Concept

K281 cluster hub. Dual-ID **OSINT K281**. Prior @concepts/k279-harness-wave.md.

## Narrative

Two items, and the first is a **layout pattern worth copying.**

### 1. One skill tree, many agent entry points

`rehan-remade/universal-modder` (MIT, 2,919 stars) ships a single canonical `skills/` directory and symlinks every agent's expected path to it:

```
.agents/skills  \
.claude/skills   } -> skills/
.gemini/skills  /
.github/skills /
```

Instructions work the same way: **`AGENTS.md` is canonical**, and `CLAUDE.md` and `GEMINI.md` are thin pointers to it.

That is cleaner than what this workspace does. We ship Cursor rules and Claude skills as separate trees and keep them in sync with a post-commit script — which is exactly the mechanism that reverted a skill edit in K276. **One canonical file, several symlinks** removes the sync step entirely.

**Worth adopting incrementally.** The cost is a symlink change in a few repos; the benefit is that a skill can no longer drift between agents.

### 2. Write down what you learned, for the next agent

The repo requires the agent to record findings in a `knowledge/INDEX.md` so the next run starts ahead. That is this workspace's own ingest discipline, applied per-game instead of per-domain.

The instruction is the transferable part. It says the accumulated notes are an output, not a byproduct.

### 3. The distribution signal

Robinhood's new platform exposes **third-party data providers as subscribable modules inside its own trading agent** — an app store for research feeds. That is a distribution model for exactly the kind of brief this workspace produces, and it is the first time a brokerage has appeared as a channel rather than a counterparty.

**No integration. Note the shape.**

### Boundary

**No install.** The asset pipeline in that repo routes through a paid third-party service — a new spend line we have not agreed to. **Do not swap `/route`. No skill install. 0 product Integrate GO.**
