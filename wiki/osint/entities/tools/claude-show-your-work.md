---
title: claude-show-your-work — terminal image/video rendering for Claude Code
type: entity
tags: [tools, claude-code, plugin, terminal, verification]
keywords: [claude-show-your-work, claude-code-plugin, ghostty, kitty, playwright, ffmpeg, tmux-passthrough, mit]
related:
  - sources/newsletter-rss-latent-space-2026-10-13-ainews-meta-muse-wonder.md
  - concepts/k290-feeds-wave.md
  - concepts/agent-tool-use-verification.md
maturity: draft
created: 2026-10-13
updated: 2026-10-13
---

## Relations

- @sources/newsletter-rss-latent-space-2026-10-13-ainews-meta-muse-wonder.md
- @concepts/k290-feeds-wave.md
- @concepts/agent-tool-use-verification.md

## Raw Concept

**What prompted this page:** the Latent Space AINews issue for 2026-10-10 to 2026-10-12.

## Narrative

An **MIT-licensed Claude Code plugin** that renders **screenshots, inline video and synced before/after QA recordings** directly in supported terminals (**Ghostty**, **kitty**). It runs **locally on macOS**, uses **Playwright** for browser interaction and recording, and **ffmpeg** for video. Install via the **Claude plugin marketplace** plus `brew install ffmpeg`.

**The practical caveat:** terminal media depends on **terminal image protocols**, and **under `tmux` you may need `set -g allow-passthrough on`** because multiplexers block or rewrite graphics escape sequences.

**Why it matters here:** it closes the loop on the workspace rule that **UI changes must be seen, not asserted**. Until now a Claude Code session could only *claim* a front-end change rendered correctly; an inline before/after recording in the same terminal makes the evidence visible to the operator. It pairs with `@concepts/agent-tool-use-verification.md` — visual evidence is a verification step, not an aesthetic one.

Community reservations worth noting: the terminal-graphics approach is **finicky across emulators**, and there is a genuine UX argument that **editor extensions render media better than a CLI**.

## Snippets

> A new MIT-licensed Claude Code plugin, claude-show-your-work, renders screenshots, inline videos, and synced before/after QA recordings directly in supported terminals such as Ghostty and kitty. [Source: https://www.latent.space/p/ainews-meta-muse-wonder-and-wonder (retrieved 2026-10-13)]
