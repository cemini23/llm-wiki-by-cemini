---
title: "agent-desktop — native OS accessibility control for agents (Apache-2.0)"
type: entity
tags: [tool, agents, desktop-automation, accessibility, vercel]
keywords: [agent-desktop, accessibility api, ax tree, skeleton traversal, c-abi, ffi, native automation]
related:
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md"
maturity: draft
created: 2026-11-02
updated: 2026-11-02
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md, URL 1, **Extract** tier. Routed to Collectibles, Atto, and CCC.

The question this page answers: **can an agent drive a native desktop app without screenshots?**

## Narrative

### What it is

From Vercel Labs. **Apache-2.0.** A Rust CLI with a C-ABI shared library (`libagent_desktop_ffi.dylib`), a native binding later consumable from Node and Python.

It reads each platform's **native accessibility tree** — macOS AX, Windows UIA, Linux AT-SPI2 — rather than pixels, and exposes roughly 60 CLI commands: snapshot, ref-based actions, text entry.

### The ideas worth stealing

**1. Progressive skeleton traversal.** `snapshot --skeleton` returns a shallow view; `--root @ref` descends into one region. This is the answer to the accessibility tree being enormous. A full AX snapshot of a complex app is thousands of nodes and would flood any context window. Fetching a skeleton and drilling into one subtree makes it tractable.

**2. Ref-based addressing.** Elements get a stable reference; actions target the reference. The agent never needs coordinates.

**3. Headless ref actions.** Act on an element without rendering. Faster and steadier than drive-by-screenshot.

### Why accessibility-tree control differs from vision control

A vision agent guesses where a button is and hopes. An AX-tree agent reads the button's role and label from the operating system. The second is deterministic and text-based, which means it degrades gracefully: if the element is absent, it is absent, not misclicked.

The trade: the target app must expose a real accessibility tree. Apps that draw their own canvas expose little, and this approach fails where vision would not.

### Fit

- **Collectibles** — reaching a desktop grader or auction tool that has no API.
- **Atto** — same shape, for local record tools.
- **CCC** — the skeleton-plus-ref traversal pattern applies to any large-tree navigation, not just desktop.

### The caution

**Do not route this to CeminiParlays.** It is general desktop automation. Automating a sportsbook UI is exactly the automated slip interaction that project forbids. The report states this explicitly and the ban stands.

More generally: a tool that can drive any native app is also a tool that can drive an app it should not. Scope the commands it is permitted to run, per project.

### Status

Extract. The traversal pattern is the asset. Scope any actual use narrowly.

## Snippets

> "Introduces progressive skeleton traversal (snapshot --skeleton and --root @ref) and headless accessibility ref actions across 60 CLI commands and a C-ABI shared library (libagent_desktop_ffi.dylib), enabling local Claude Code agents to operate native macOS cat…" — report, URL 1

## Dead Ends

- **Using it on a canvas-drawn app.** No accessibility tree means nothing to read.
