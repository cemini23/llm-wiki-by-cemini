---
title: Chachamaru127/claude-code-harness — Plan→Work→Review→Ship Guardrails (Go+Shell, MIT)
type: source
tags: [llm-tooling, claude-code, guardrails, go, hokage-engine, plan-work-review-ship, workflow-adopt, ip-sale-clean]
keywords: [claude-code-harness, hokage-engine, go-native, sub-10ms-hooks, harness-plan, harness-review, verb-skills, branch-protection, force-push-prevention, secret-leak-prevention, claude-opus-4-7]
related:
  - sources/gemini-dr-link-eval-2026-04-28.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - sources/agentic-harness-engineering.md
  - sources/mercurialsolo-claudectl.md
maturity: validated
created: 2026-04-28
updated: 2026-04-30
clusters: [llm-agents, dev-tooling]
---

## Relations

- @sources/gemini-dr-link-eval-2026-04-28.md — parent canonical Gemini DR source; one of 7 Adopt-for-Workflow recommendations
- @concepts/wiki-tooling-evaluation.md — Wave 2 evaluation parent
- @concepts/ip-sale-readiness.md — MIT license clears IP-sale checks (Exa-verified 2026-04-28: 594 ★)
- @sources/agentic-harness-engineering.md — academic generalization of the same family (Lin et al., arXiv 2604.25850, 28 Apr 2026): chachamaru is a *deployed* Plan→Work→Review→Ship harness on Claude Code; AHE formalizes the substrate (7 component types, observability pillars, falsifiable manifest) that any such harness can be evolved over. The Plan/Work/Review/Ship verbs map onto AHE's middleware + skill component types; chachamaru's force-push prevention and secret-leak hooks are the kind of guardrails AHE's Evolve Agent would converge on. Useful pairing: chachamaru = deployment; AHE = optimization framework

## Raw Concept

- **URL**: https://github.com/Chachamaru127/claude-code-harness
- **Type**: Open-source repository / CLI tooling
- **License**: MIT (Exa-verified 2026-04-28)
- **Stars / Forks (Exa-verified 2026-04-28)**: 594 ★ / 63 forks / 4 open issues
- **Stack**: Shell 37.3%, Go 34.6%, JavaScript 16.5%, TypeScript 10.0%, Python 1.5%, Makefile
- **Org**: Chachamaru127 (3 contributors: Chachamaru127, claude, github-actions[bot])
- **Created**: 2025-12-12; **Last push**: 2026-04-26; **Latest release**: v4.4.0 (2026-04-26)
- **Releases**: 143 published — extreme release cadence

## Narrative

### What it does
A structured framework wrapping the Claude CLI to enforce a rigid `Plan → Work → Review → Ship` autonomous development cycle. The Go-native compiled engine "Hokage" injects sub-10ms hooks into the agent's workflow to enforce five "Verb Skills" (e.g., `/harness-plan`, `/harness-review`). Functions as a security perimeter — actively blocks destructive file writes, prevents credential exposure, and intercepts unauthorized force-push attempts to protected Git branches like `main`.

### Why Adopt-for-Workflow

The harness directly addresses the dominant risk in solo-developer Claude Code sessions: an autonomous agent making destructive or insecure commits. Reasoning:

1. **Sub-10ms hook latency** — Hokage Go binary intercepts agent decisions in real-time without perceptible workflow drag. No Node.js runtime overhead.
2. **Branch protection at the agent layer** — main-branch force-push prevention happens before Git even sees the operation. Defends against the "agent hallucinates a force-push" failure mode that has bitten the workspace before.
3. **Secret-leak prevention** — actively scans for credential patterns before commit. Cemini has DeepSeek API keys, Polygon keys, Alpaca keys, OANDA keys; secret-leak prevention is a critical operational guardrail.
4. **MIT license** — clears IP-sale-readiness gates.
5. **Autonomous Plan/Review structure** — enforces discipline that the user might forget under time pressure. Pairs with `mattpocock/skills` `/grill-me` (intent verification) and `southpolesteve` Bare Bones Memory protocol from the same Gemini DR wave.

### Where it falls short

1. **Cemini production stack fit: ❌** — strictly designed for local CLI workflows; no server-side application.
2. **Wiki / librarian server fit: ❌** — the librarian is a headless daemon with no Claude Code sessions running on it. Don't deploy.
3. **Coupling to Claude Code v2.1+ internals** — explicitly relies on Claude Code's hook system and is "heuristically tuned for `claude-opus-4-7`" (per Gemini's evaluation). Anthropic CLI breaking changes could fail silently or require complex upstream patches. Track Anthropic CLI release notes; pin to a known-good Claude Code version if possible.

### Integration vector

```
Local laptop install:
  curl ... | install harness  (or: brew install claude-code-harness)
        ⬇
  binds to ~/.claude/plugins (.claude-plugin directory)
        ⬇
  intercepts Claude Code's hook events
        ⬇
  enforces:
    - Plan verb (forces explicit plan before work)
    - Review verb (forces review checkpoint before ship)
    - Branch-protection (blocks force-push on main)
    - Secret-scanner (blocks commits with credential patterns)
    - Destructive-write-guard (requires confirmation for delete/overwrite)
```

### Risks & open questions

1. **Anthropic CLI architectural changes** — heuristic tuning for `claude-opus-4-7` means future Claude Code versions may not honor the harness's hook contracts. Pin Claude Code version; track upstream.
2. **macOS file permissions binding** [NEEDS VERIFICATION 2026-04-29] — Gemini flagged: "Precise configuration instructions for successfully binding the Go-native engine to the .claude-plugin directory on a macOS file system must be verified, as file permissions often block compiled binaries from intercepting Node.js processes." Test on the actual laptop before committing to the workflow.
3. **Sole-author project** — 3 contributors (Chachamaru127, claude, github-actions[bot]), where 2 are bots. Bus factor concern. The 143-release cadence in 4.5 months suggests engaged maintenance, but verify quarterly.
4. **No license file inspection done** — Exa confirmed MIT badge. Before committing as a hard guardrail, run `gh api repos/Chachamaru127/claude-code-harness/license` to inspect the verbatim LICENSE file content (per the brief's anti-hallucination protocol).

## Snippets

> "Adopt for Workflow. The rigid guardrails protecting the main branch and actively preventing secret exposure align perfectly with mitigating the risks inherent in generating and committing code for the Cemini stack using an autonomous agent." [Source: Gemini DR report, URL 6]

> "Claude Code Dedicated Development Harness - Achieving High-Quality Development Through an Autonomous Plan→Work→Review Cycle" [Source: GitHub repo description, retrieved via Exa crawling_exa 2026-04-28]
