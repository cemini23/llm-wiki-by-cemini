---
title: "Obscura — Headless Browser for AI Agents (RED-FLAG: aggressive prod-replacement claim)"
type: entity
tags: [tool, headless-browser, playwright-alternative, web-scraping, k39, adopt-tier-flagged, phase-0-pending]
keywords: [obscura, headless browser, playwright replacement, agent web scraping, h4ckf0r0day]
related:
  - sources/evaluating-project-links-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
phase_0_audit: PENDING — Adopt verdict recommends wholesale Playwright + Headless Chrome replacement on production; high scope risk
---

## Relations
- `@sources/evaluating-project-links-stacks.md` — source evaluation brief (URL 16)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied

## Raw Concept

- **Repo / URL** (per source brief): `github.com/h4ckf0r0day/obscura`
- **Tier (per source brief)**: **Adopt** (laptop + production wholesale replacement of Playwright + Headless Chrome)
- **Tier downgrade pending**: **NEEDS Phase-0**
- **License** (per source brief): MIT
- **Stack**: Headless browser optimized for AI-agent context; Markdown extraction; claims to wholesale-replace Playwright/Headless Chrome dependencies

## Narrative — RED FLAG

Eval brief's headline recommendation:

> "Immediately deploy across both the developer laptop (for rapid Markdown extraction) and the production server (wholesale replacing all legacy Headless Chrome and Playwright FastMCP ingestion dependencies). The memory savings alone justify the migration."

Wholesale production replacement on a 24/7 trading stack from a **single-dev project** (h4ckf0r0day) is the **most aggressive recommendation in the K39 batch after DeepSeek-TUI**.

### Integration vector

**Adopt → HOLD pending Phase-0**. Production-stack scraping is critical infrastructure — wholesale replacement requires:
1. **Maturity verification** — single-dev (h4ckf0r0day) project age, stars, contributor count, recent activity
2. **Feature parity** — does Obscura handle the exact set of sites Cemini's existing ingestion pipeline currently scrapes? (JS-heavy sites, login flows, anti-bot measures, etc.)
3. **Failure-mode behavior** — what happens under sustained 24/7 load, memory pressure, network timeouts?
4. **License file** presence
5. **Memory-savings claim** — verify against actual Cemini Playwright RAM baseline

### Why aggressive recommendation triggers caution

Cemini's production scraping is already battle-tested (Playwright + Headless Chrome on 40-container Hetzner stack). Replacing battle-tested infrastructure with single-dev-project software for "memory savings" is **exactly the wrong risk tradeoff** unless Phase-0 demonstrates strictly-better outcomes across all critical surfaces.

**Workflow-laptop adoption** is a reasonable first step (low blast radius) — but **production rollout requires extensive shadow-mode soak** before any switchover.

### NEEDS VERIFICATION

- All items above
- Whether `h4ckf0r0day` username has any historical reputation signal (red flag: leet-speak, unrelated security-themed namespace)

### Phase-0 audit status

**PENDING — HIGH PRIORITY**. Workflow-laptop pilot OK after Phase-0 clears items 1+4. Production rollout requires 4-phase rollout pattern (offline → shadow → 25%-rollback → full) — minimum 4-week soak.

[Source: Evaluating Project Links for Stacks.docx URL 16; retrieved 2026-05-11]
