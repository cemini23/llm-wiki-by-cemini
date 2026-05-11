---
title: "UI-TARS Desktop — Multimodal GUI Agent (ByteDance)"
type: entity
tags: [tool, gui-agent, multimodal, mcp, bytedance, workflow-laptop-candidate, k37]
keywords: [ui, tars, desktop, adopt, three-surface-eval]
related:
  - sources/evaluating-urls-system-integration.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/evaluating-urls-system-integration.md` — source evaluation brief (URL 9)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/bytedance/UI-TARS-desktop`
- **Tier (per source brief)**: **Adopt**
- **License**: [NEEDS VERIFICATION 2026-05-11] License needs verification (ByteDance-backed; check repo LICENSE before any production reliance).

## Narrative

Open-source multimodal AI Agent framework granting LLMs native GUI interaction across OS + browsers. Built on MCP. Dual strategy: DOM analysis for web + native GUI parsing for desktop. Localized CLI + Web UI.

### Integration vector

Adopt for autonomous Obsidian workflow tasks that cannot be safely addressed by Python text-parsing (e.g., visual diff inspection, plugin UI ops across 400+ wiki files).

### Risks

Vision-GUI automation is brittle (UI updates, OS font scaling, popups). Security posture: granting an agent OS-level GUI control over the workstation is a substantial privilege escalation surface.

[Source: Evaluating Urls System Integration.docx, URL 9]
