---
title: "visual-explainer — Agent Skill for Rich HTML Diagram Generation"
type: entity
tags: [dev-tooling, claude-code, visualization, html, mermaid, chartjs, mit, adopted-tier, laptop-only]
keywords: [visual-explainer, agent-skill, html-diagrams, diff-review, plan-review, css-grid, claude-code]
related:
  - sources/multi-wiki-tool-evaluation-v3.md
maturity: draft
created: 2026-05-14
updated: 2026-05-14
---

## Relations

- @sources/multi-wiki-tool-evaluation-v3.md — v3 batch eval: Adopt tier, CCC wiki primary fit

## Raw Concept

From the Cemini Multi-Wiki Link Evaluation Report v3 (May 2026). MIT-licensed zero-dependency standalone skill that generates rich HTML diagrams from terminal output, compatible across Claude Code, Cursor, Pi, and OpenClaw harnesses.

## Narrative

visual-explainer converts dense terminal outputs into interactive, scrollable HTML diagrams using Mermaid and Chart.js. Key integrations for Cemini: `/diff-review` and `/plan-review` slash commands to visualize code reviews against the algorithmic trading stack. The rendering heuristic auto-triggers HTML generation when an agent outputs a table exceeding three columns.

**Tier: Adopt** — clean MIT license, zero IP-sale risk. Deploy laptop-side in Claude Code CCC workflow. Cross-wiki routing: CSS Grid layout definitions from `css-patterns.md` should seed the SEO wiki's DESIGN.md marketing style guidelines.

**NEEDS VERIFICATION:** Telemetry exfiltration pathways if deployed to external cloud hosting via the included `share.sh` Vercel script — inspect before any cloud deployment.
