---
title: Claude-OSINT — 5,500 Lines of Specialized OSINT Skills (MIT)
type: entity
tags: [tool, osint, claude-code-skills, mit, steal-from-tier, workspace-side]
keywords: [claude-osint, osint-skills, skill-md, open-source-intelligence, claude-code-skill-library, workspace-curator-tooling]
related:
  - sources/5-5-links-tool-eval.md
  - sources/xskill-2603-12056.md
  - sources/agriciDaniel-claude-obsidian.md
  - sources/kepano-obsidian-skills.md
maturity: draft
created: 2026-05-05
updated: 2026-05-05
---

## Relations

- @sources/5-5-links-tool-eval.md — origin source: 2026-05-05 Gemini DR eval, URL 6, **Steal-from** tier
- @sources/xskill-2603-12056.md — XSKILL's Markdown Skill Library + cross-rollout critique pattern is the academic version of what Claude-OSINT pre-builds for OSINT specifically; both follow the SKILL.md Markdown convention
- @sources/agriciDaniel-claude-obsidian.md — claude-obsidian's `/autoresearch` Markdown-skills pattern is the Obsidian-flavored predecessor
- @sources/kepano-obsidian-skills.md — earlier Obsidian-skills source; same architectural family

## Raw Concept

Repository providing 5,500+ lines of specialized SKILL.md files for Open-Source Intelligence (OSINT) work, formatted for Claude Code. MIT-licensed. Steal-from-tier verdict in K30 5_5-links batch.

## Narrative

- **URL**: per K30 eval URL 6 (verify exact GitHub path)
- **License**: MIT
- **Format**: SKILL.md files (Markdown with structured sections)
- **Scope**: 5,500 lines = substantial library — likely dozens of distinct OSINT skills

### Why Steal-from for the Cemini OSINT workspace

This is **directly mine domain** — the Cemini OSINT workspace is itself an OSINT operation. Claude-OSINT's pre-built skills cover patterns this workspace's curator workflow already handles ad-hoc:
- Source-page generation conventions
- Cross-link discipline
- Citation patterns for OSINT material
- Provenance tracking
- Lint patterns for OSINT-specific quality flags

### Workspace-side integration (NOT prod)

This is a **workspace-side** tool, not Cemini production. The use cases:

1. **Selectively merge skills** into `~/.claude/skills/` for the OSINT workspace — adopt the ones that fit our K-series ingest discipline; skip the ones that conflict with our schema
2. **Cross-reference for ingest workflow** — the K-series ingest discipline (preingest_check → read → discuss → write → cross-link → log → scp → lint → commit) is essentially an OSINT-curation skill; Claude-OSINT may have parallel skills with refinements worth lifting
3. **Train future curator sessions** — drop relevant Claude-OSINT skills into the wiki-share zip (per K28's friend-handoff bundle) so a friend's Claude Code starts with OSINT skills pre-loaded

### Discipline: don't blindly merge 5,500 lines

5,500 lines is too much to wholesale-import without dilution. The Steal-from approach:

1. Phase 0 — clone repo, inspect skill manifest
2. Phase 1 — categorize skills by Cemini-domain-match (financial / prediction-market / generic-OSINT) + curator-workflow-match (ingest / lint / cross-link / etc.)
3. Phase 2 — selectively port the Cemini-relevant subset into `~/.claude/skills/`
4. Phase 3 — document the merged skills in `wiki/concepts/curator-skills.md` (new concept page) for transparency

### Open questions [NEEDS VERIFICATION 2026-05-05]

- Exact GitHub URL
- Star count, commits count, latest update — eval implies active maintenance but doesn't quote specifics
- License terms (MIT confirmed by eval; verify by inspection)
- Skill granularity: 5,500 lines / how-many-skills = average size per skill. Many small focused skills > a few mega-skills.
- Whether skills are designed for the official Anthropic skill format or a custom convention

## Snippets

- **Scope framing** (K30 eval): "paired set of highly structured SKILL.md files containing over 5,500 lines of specialized Open-Source Intelligence." [Source: 5_5 links.docx URL 6]

- **Recommendation tier**: "Steal-from. The primary v[alue is the SKILL.md library]." [Source: 5_5 links.docx URL 6]
