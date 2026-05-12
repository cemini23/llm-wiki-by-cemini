---
title: "AI-Trader (HKUDS) — Brokerage API Agent Bridge"
type: entity
tags: [tool, trading-agent, fastapi, ibkr, steal-from, k38, license-gap]
keywords: [ai, trader, hkuds, steal-from, three-surface-eval, no-license-file]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: validated
created: 2026-05-11
updated: 2026-05-11
license_verified: NO-LICENSE-FILE
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 10)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL** [VERIFIED 2026-05-11]: `github.com/HKUDS/AI-Trader`
- **Tier (per source brief)**: **Steal-from** → **DOWNGRADED 2026-05-11 to pseudocode-only pattern extraction** on license gap
- **License** [VERIFIED 2026-05-11]: **NO LICENSE FILE** despite README MIT claim. Root listing (`.env.example, .gitignore, README.md, README_ZH.md, assets, docs, impeccable.context.tmp, package-lock.json, package.json, service, skills, tsconfig.json`) has zero `LICENSE` / `LICENSE.md` / `LICENSE.txt` / `COPYING` file; GitHub `license` API field returns null. Under default copyright, all rights reserved — README MIT assertion is legally unbacked. Maturity: 16,123★ / last push 2026-05-06 / ~6.6 months old. **3rd occurrence of this pattern** after `finance-skills` K36 (upstream issue #64) and `Readme.skill` K38.

## Narrative

Multi-layer trading app: FastAPI Python backend + React frontend. Background workers decouple user-facing latency from settlement/intelligence tasks. Bridges Claude Code / OpenClaw to major brokerage APIs (incl. Interactive Brokers).

### Integration vector — DOWNGRADED 2026-05-11

Original Steal-from: extract Python FastAPI **Interactive Brokers integration logic** + **background-worker isolation pattern**.

**Downgraded scope (no-LICENSE constraint)**: pseudocode-level pattern extraction only — read the source as a **design reference**, write a clean-room independent reimplementation in Cemini's stack. **NO direct code copy** of any kind (no copy/paste, no derivative-translation of identifiers/comments/structure beyond the public-API-defined surface). Claude IBKR API integration is itself MIT/Apache-licensed; the patterns AI-Trader uses are reproducible from first principles + the public IBKR docs without needing the AI-Trader codebase as source material. Discard the React frontend (Cemini is headless).

**Pre-extraction action**: file upstream GitHub issue requesting AI-Trader add a `LICENSE` file matching their README MIT claim. Same upstream-issue pattern as `finance-skills` K36 issue #64. Until LICENSE is added, treat the codebase as inspection-only.

### Risks

1. **License-gap landmine** (HIGH) — under default copyright, any direct code derivative of AI-Trader is a copyright violation regardless of README MIT claim. The 16k star count + dual README (English + Chinese) does not change this — copyright defaults govern absent a written license grant.
2. **Brokerage API drift** (MEDIUM) — IBKR APIs are notoriously volatile; integration patterns extracted now require cross-check against current official IBKR API docs before any port.
3. **Pattern-extraction discipline** (MEDIUM) — pseudocode-only extraction discipline is hard to maintain in practice; clean-room reimplementation requires explicit separation between "read AI-Trader" sessions and "write Cemini code" sessions.

[Source: Link Evaluation Brief Trading Stack.docx, URL 10; Phase-0 license-gap audit 2026-05-11]
