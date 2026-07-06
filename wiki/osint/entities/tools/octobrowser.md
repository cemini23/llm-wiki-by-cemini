---
title: OctoBrowser — kernel-level Chromium fingerprint obfuscation
type: entity
tags: [entity, tool, osint, browser, k147]
keywords: [OctoBrowser, HoppouAI, anti-detection, Copilot SDK, stealth]
related:
  - sources/eval-github-repo-multi-wiki-copilot-2026-07-06.md
  - entities/tools/brightdata-mcp.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-06
updated: 2026-07-06
---

## Relations

- @sources/eval-github-repo-multi-wiki-copilot-2026-07-06.md — K147 Steal-from
- @entities/tools/brightdata-mcp.md — commercial proxy alternative

## Raw Concept

K147 Phase-0 on [HoppouAI/OctoBrowser](https://github.com/HoppouAI/OctoBrowser).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `HoppouAI/OctoBrowser` |
| **License** | **MIT** |
| **Stars / pushed** | ~130★; pushed 2026-03-25 |
| **Verdict** | **Steal-from** — OSINT stealth browser patterns only |
| **Pattern** | Chromium kernel parameter spoofing + isolated profiles + Copilot SDK agent binding |

No TipDrop/David brief — OSINT wiki literacy for scaled telemetry harvest without bot triggers. `[NEEDS VERIFICATION 2026-07-06]` WebGL spoofing claims need manual code review per docx.

## Snippets

> "Modifies Chromium at the kernel level to deeply obfuscate digital footprints." [Source: eval-github-repo-multi-wiki-copilot-2026-07-06.md]
