---
title: "Terax AI — Tauri 2 + Rust Terminal Emulator with LLM (Reference-Only)"
type: entity
tags: [tool, reference-only, terminal-emulator, tauri, rust, apache-2-license]
keywords: [Terax, AI Development Environment, ADE, Tauri 2, Rust, Vercel AI SDK, OS keyring, xterm.js, CodeMirror 6]
related:
  - sources/evaluating-code-for-trading-stacks.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-code-for-trading-stacks.md` — source evaluation brief (URL 2)

## Raw Concept

Cross-platform lightweight "AI Development Environment" (ADE) and terminal emulator. Bundles integrated PTY (portable-pty) + AI interface (Vercel AI SDK). Local-only, no telemetry, no mandatory accounts. Credentials in OS keychain.

- **Repo**: `github.com/crynta/terax-ai`
- **License**: Apache-2.0 [NEEDS VERIFICATION 2026-05-10]
- **Stack**: Tauri 2 (Rust), React 19, Tailwind, xterm.js, CodeMirror 6
- **Bundle**: ~7 MB; disk 10 MB

## Narrative

**Recommendation: Reference-only.** Strong architectural patterns (Tauri 2 + Rust for lightweight cross-platform, OS keychain for credentials) but the solo developer's existing Obsidian + iTerm2 + Claude Code workflow gains nothing material from another UI layer.

### Three-surface fit

- **Workflow (⚠️)**: replaces iTerm2/Terminal with Terax → run Claude Code in xterm.js. Apache-2.0 clean. But no compelling gain over current setup.
- **Cemini prod (❌)**: GUI desktop app — cannot containerize, cannot run headless in Hetzner Docker.
- **Wiki server (❌)**: same — headless servers don't run GUI terminal emulators.

### What's worth referencing

- OS-keyring credential management pattern (avoids `.env` plaintext API keys)
- Tauri 2 architecture for lightweight cross-platform agents (vs Electron bloat)

### Risks / caveats

- **Maturity signal**: no code-signing certificate (Windows SmartScreen flagged) → early-stage
- **Resident memory under load [NEEDS VERIFICATION 2026-05-10]**: Tauri WebView GC behavior on long Claude Code sessions with large diffs unknown
- **License verification**: confirm Apache-2.0 before any code reference

[Source: Evaluating Code for Trading Stacks.docx, URL 2]
