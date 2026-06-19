---
title: K118 — Poker agent research gaps (cross-wiki stub)
type: source
tags: [source, brief, poker, devfun, k118, cross-wiki]
keywords: [k118, cemini_decide, PFR, hl-loop]
related:
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/devfun-researcher-track-readiness-2026-06.md
  - entities/platforms/devfun-arena.md
maturity: validated
created: 2026-06-18
updated: 2026-06-18
cross-wiki-source: "@gambling-wiki/sources/brief-k118-poker-agent-research-gaps-2026-06-17.md"
---

## Relations

- @gambling-wiki/sources/brief-k118-poker-agent-research-gaps-2026-06-17.md — canonical K118 source page
- @concepts/devfun-poker-agent-challenge-2026.md — OSINT implementation context
- @entities/platforms/devfun-arena.md
- @gambling-wiki/briefs/2026-06-17_k118-gambling-poker-agent-research-gap-fixes.md — operator fix backlog (private gambling wiki)

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | K118 poker agent research gap analysis |
| **Date** | 2026-06-17 |
| **Implementation** | `agents/devfun-poker-arena/` in OSINT workspace |

## Narrative

Cross-walk of 2025–2026 poker-agent literature vs `cemini_decide`. Primary gap was passive PFR (SB limp inflation, rock steal threshold, no deploy gate). **F1–F8 backlog** tracked in gambling wiki; OSINT agent repo implements fixes (PFR gate, rock steal 0.55, multiway steal block F7, preflop JSONL F8, session memory F6). HL loop R36 (2026-06-18): BB weak ace paired runout, BTN/EP postflop trash folds.

Full tables and literature citations: see gambling wiki canonical page.
