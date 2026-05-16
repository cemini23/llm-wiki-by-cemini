---
title: "garden-skills (ConardLi) — Claude Code skill collection (Adopt-tier)"
type: entity
tags: [tool, claude-code, skills, npx, ccc-wiki, adopt-tier, image-gen, seo]
keywords: [garden-skills, ConardLi, npx skills, Claude Code skills, web-design, image-generation, knowledge-retrieval]
related:
  - sources/tool-evaluation-multi-wiki-audit-may-2026.md
maturity: draft
created: 2026-05-16
updated: 2026-05-16
---

## Relations

- `@sources/tool-evaluation-multi-wiki-audit-may-2026.md` — source evaluation that classified this as Adopt-tier

## Raw Concept

Identified in the May 2026 44-tool multi-wiki audit. MIT-licensed repository of production-grade Claude Code skills installed via `npx skills add`. 4,900 stars, last commit 2026-04-30. Primary fit: CCC wiki. Cross-routes: Image-gen wiki (gpt-image-2 persona-ops), SEO wiki (web-design-engineer templates).

## Narrative

Centralized skill repository for AI coding agents (Claude Code, Cursor). Deployment model: `npx skills add` fetches pinned, immutable `.zip` artifacts from GitHub release tags — eliminating CI environment drift.

**Skill categories**: web design engineering, knowledge retrieval, image generation (gpt-image-2 persona operations), and more. Each skill follows a structured manifest format.

**Why Adopt**: The immutable-release-fetch pattern aligns with CCC wiki's SKILL.md specification protocols. MIT license permits safe integration into both laptop-side dev environments and corporate knowledge bases.

**Cross-wiki impact**:
- **Image-gen wiki**: gpt-image-2 persona-ops tooling for character image generation workflows
- **SEO wiki**: web-design-engineer template skills for standardized visual output in GEO/AEO campaigns

**Open question** [NEEDS VERIFICATION 2026-05-16]: Localized code review of grep and pandas source-aware formatting workflows to ensure compatibility with existing Cemini data extraction scripts.
