---
title: "mercurialsolo/claudectl — Mission Control for Claude Code (Rust, MIT, 11★ but 44 releases)"
type: source
tags: [github, rust, claude-code, agent-orchestration, multi-session, local-llm-autopilot, mit-license, ip-sale-clean, gemini-dr-wave4, workflow-adopt]
keywords: [claudectl, mercurialsolo, claude-code-mission-control, rust-tui, multi-session-orchestration, local-llm-autopilot, ollama-integration, llama-cpp, vllm, file-ownership-leases, hive-mind-relay, sub-50ms-startup, tmux-iterm2-ghostty-warp, claude-code-plugin]
clusters: [llm-agents, dev-tooling]
related:
  - sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md
  - sources/claude-code-harness-chachamaru.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - concepts/high-signal-paper-patterns.md
  - concepts/mcp-tool-marketplace.md
maturity: validated
read_status: read-skim
created: 2026-04-30
updated: 2026-04-30
---

## Relations

- @sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md — Wave 4A URL 9 Adopt-Workflow; promoted to dedicated source in Phase 2 (2026-04-30)
- @sources/claude-code-harness-chachamaru.md — sibling **Plan→Work→Review→Ship guardrails** project; both wrap Claude Code with operator-layer controls. claudectl is the *orchestrator* layer (multi-session); chachamaru is the *guardrail* layer (within-session safety). Complementary in laptop workflow.
- @concepts/wiki-tooling-evaluation.md — Wave 4 evaluation parent
- @concepts/ip-sale-readiness.md — MIT license clears IP-sale checks; no Family A/B/C concerns
- @concepts/high-signal-paper-patterns.md — rubric: 11 stars / 1 contributor / **44 releases in ~12 days** = solo author burning down feature backlog at extreme velocity. Bus-factor risk, but the release cadence is itself a maturity signal (active development > popular stagnant)

## Raw Concept

- **URL**: https://github.com/mercurialsolo/claudectl
- **Type**: Open-source Rust binary + CLI + TUI + Claude Code plugin
- **License**: MIT (Exa-verified 2026-04-30)
- **Stars / Forks**: 11 ★ / 1 fork (small but very recent)
- **Releases**: **44 published** (latest GitHub: v0.18.2 2026-04-15; latest crates.io: **v0.32.0** 2026-04-20)
- **Stack**: Rust 98.6% / Shell 1.2% / Nix 0.2%
- **Org**: mercurialsolo (solo author)
- **Created**: 2026-04-03; **Last push**: 2026-04-15 (GitHub) / 2026-04-20 (crates.io)
- **Topics**: agent-ops, ai-agents, claude, claude-code, cost-tracking, developer-tools, observability, rust, rust-cli, terminal, terminal-dashboard, tmux, tui, workflow-automation
- **Homepage**: https://mercurialsolo.github.io/claudectl/
- **Discovered via**: Gemini DR Wave 4A 2026-04-29 (URL 9); promoted to dedicated source 2026-04-30
- **Read status**: read-skim (Exa-fetched README + crates.io page + Gemini DR brief evaluation)

## Narrative

### What it is

A **Rust binary + TUI + Claude Code plugin** functioning as **"mission control" for multiple concurrent Claude Code sessions**. Solves the "tab hunting" problem when running 3-8 parallel Claude Code agents — knows which agent is blocked, burning budget, waiting for approval, or stalled, and lets you intervene from one terminal dashboard.

Three integrated capabilities:

1. **Multi-session orchestration** — run dependency-ordered task graphs across parallel Claude Code agents; route data between sessions; resume from failure points.
2. **Local LLM auto-pilot** — Ollama / llama.cpp / vLLM passively observes agent actions; auto-approves safe operations (file reads, greps); blocks dangerous ones (force pushes, secret leaks). **No cloud API, no telemetry**.
3. **TUI dashboard** — status / burn rate / context usage / activity / CPU / memory / subagent rows. Approve prompts, send input, kill sessions.

Terminal support: GNOME Terminal, tmux, iTerm2, Ghostty, Warp, Kitty, Terminal.app, WezTerm.

### Why Cemini-direct (Workflow only)

**Adopt for laptop workflow only**. NOT for Cemini production stack (claudectl is interactive-terminal-orchestrated; cemini-prod is headless 24/7).

The local-LLM-auto-pilot pattern is the load-bearing innovation — it taps the laptop's existing Ollama instance (which already runs nomic-embed-text on cemini-librarian for embeddings) to provide auto-approval / auto-block for Claude Code sessions. **Cemini's Workflow already runs Claude Code intensively for wiki curation + research drafting; claudectl makes that workflow more reliable + cost-bounded**.

Concrete laptop-side deployment:
1. `brew install mercurialsolo/tap/claudectl` (or `cargo install claudectl`)
2. Configure Ollama as the auto-pilot brain (the laptop already has nomic-embed-text loaded)
3. Wrap existing Claude Code sessions during research/curation cycles
4. Set per-session budget caps + auto-kill thresholds

### Bus-factor + maturity reading

**11 stars + 1 contributor** = small project. **BUT 44 releases in ~12 days** is an unusual signal — the solo author is shipping features at extreme velocity. Two ways to read this:

- **Pessimistic**: solo-author-feature-thrashing; project may stabilize at any time or be abandoned in 6 months
- **Optimistic**: very rapid product-market-fit iteration; this is what high-quality solo-developer projects look like in their first month

Either reading argues for **fork-and-pin pattern at adoption time** (clone repo, pin commit hash; benefit from current state, don't depend on upstream maintenance long-term). Same pattern as `dune-analytics-mcp` and `polymarket-predictions-mcp`.

### Risks & open questions

1. **Solo-author bus-factor** — already covered above. Mitigated by fork-and-pin.
2. **Local LLM resource contention** [NEEDS VERIFICATION 2026-04-30] — the laptop runs Ollama for nomic-embed-text + potentially other models. Adding another local-LLM consumer may stress unified memory. Pre-deployment test: run claudectl + 3 concurrent Claude Code sessions + nomic-embed-text simultaneously; observe thermal throttling.
3. **TUI thermal throttling under heavy load** (per Gemini brief) — sustained TUI rendering + multi-session monitoring + local LLM inference can heat the laptop into throttle territory.
4. **Trade-off vs simpler workflows** — for genuinely linear workflows (one Claude Code session at a time), claudectl adds overhead without benefit. The value comes specifically from 3+ parallel sessions.
5. **Crates.io vs GitHub version drift** — crates.io shows v0.32.0; GitHub aggregator shows v0.18.2. Verify before adoption which is the canonical "latest" — likely crates.io is fresher.

### Cemini-side adoption assessment

**Decision: Adopt for laptop workflow** — small commit, large quality-of-life improvement during research/curation sessions where the user runs multiple Claude Code instances. Concrete next-steps:

1. License audit (~5 min) ✅ already done via Exa
2. `brew install mercurialsolo/tap/claudectl` + verify Ollama integration ~15 min
3. Try with one real research session (next time the user runs 2+ Claude Code sessions) — observe TUI ergonomics + auto-pilot quality
4. If first impressions are good: configure as the default Claude Code wrapper for wiki-curation sessions

### Citation

> mercurialsolo. (2026). *claudectl: Mission Control for Claude Code*. https://github.com/mercurialsolo/claudectl (MIT License; v0.32.0 latest crates.io 2026-04-20; 44 releases since 2026-04-03)

## Snippets

> **Project mission (from homepage)**:
>
> "Supervise every Claude Code session from one terminal. Know which agent is blocked, burning budget, waiting for approval, or stalled, and intervene without tab hunting." [Source: https://mercurialsolo.github.io/claudectl/, retrieved 2026-04-30 via Exa]

> **Local-LLM-auto-pilot framing (from crates.io)**:
>
> "Auto-pilot for Claude Code. A local on-device model that learns what to approve, deny, and improve — no cloud API, no telemetry. Local LLM auto-pilot — a brain that learns your preferences and auto-approves/denies tool calls. No cloud API." [Source: https://crates.io/crates/claudectl, retrieved 2026-04-30 via Exa]
