---
title: "AppFlowy — AGPL-3.0 Notion Alternative (REJECTED on IP Grounds)"
type: entity
tags: [tool, rejected, agpl-3-license, license-blocker, ip-sale-disqualifying]
keywords: [AppFlowy, Notion alternative, AGPL-3.0, ASP loophole, Rust, Flutter, self-host, license blocker]
related:
  - sources/evaluating-code-for-trading-stacks.md
  - concepts/cemini-license-posture.md
  - concepts/ip-sale-readiness.md
maturity: validated
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-code-for-trading-stacks.md` — source evaluation brief (URL 7)
- `@concepts/cemini-license-posture.md` — AGPL-3.0 is on the explicit auto-reject list
- `@concepts/ip-sale-readiness.md` — AGPL would compromise institutional acquisition

## Raw Concept

AI-powered collaborative workspace platform; self-hostable open-source Notion alternative. Rust backend + Flutter multi-platform frontend. Data sovereignty + community-driven extensibility focus.

- **Repo**: `github.com/AppFlowy-IO/AppFlowy`
- **License**: **AGPL-3.0** [VERIFIED 2026-05-10 via source brief]
- **Stack**: Rust backend, Flutter frontend

## Narrative

**Recommendation: REJECT. Terminal license blocker.**

AGPL-3.0 is explicitly on the `@concepts/cemini-license-posture.md` auto-reject list. The license closes the "ASP loophole" — if proprietary Cemini software interacts with AGPL software over a network, the proprietary source must be disclosed. Catastrophic legal risk for institutional acquisition.

### Three-surface fit

- **All surfaces**: ❌ — license terminal blocker. Technological merits irrelevant.

### Why blocking

Any custom Python/Node bridge between AppFlowy's backend and Cemini's PostgreSQL or knowledge-base server would bind the integration layer under AGPL-3.0 terms. Transitive license contamination = compromise of institutional sale value of the entire proprietary codebase.

### Architectural mismatch (secondary, not load-bearing reason)

- Proprietary Rust-backend data formats + binary storage schemas incompatible with Cemini's Markdown-frontmatter + rsync pipeline
- Solo-developer Obsidian workflow gains nothing from AppFlowy's heavier Rust/Flutter compilation stack

### Status

**Closed.** No further verification required. AGPL-3.0 in primary source repo serves as terminal block.

[Source: Evaluating Code for Trading Stacks.docx, URL 7]
