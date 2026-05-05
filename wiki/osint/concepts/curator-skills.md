---
title: Curator Skills — Claude Code Skill Library for the OSINT Workspace
type: concept
tags: [workspace-meta, curator-tooling, claude-code-skills, skill-md, accumulator-page]
keywords: [curator-skills, claude-osint, skill-md, workspace-side-skills, ingest-discipline-skills]
related:
  - entities/tools/claude-osint.md
  - sources/xskill-2603-12056.md
  - sources/agriciDaniel-claude-obsidian.md
  - sources/kepano-obsidian-skills.md
maturity: draft
created: 2026-05-05
updated: 2026-05-05
---

## Relations

- @entities/tools/claude-osint.md — primary upstream source: K30 Steal-from of 5,500 lines of OSINT SKILL.md files. This concept page is the destination for skills selectively merged into `~/.claude/skills/`.
- @sources/xskill-2603-12056.md — XSKILL paper documents the SKILL.md Markdown format pattern + cross-rollout-critique discipline; informs how skills should be structured + maintained
- @sources/agriciDaniel-claude-obsidian.md — claude-obsidian's `/autoresearch` Markdown-skills pattern is the Obsidian-flavored predecessor; some skills may be ported from there
- @sources/kepano-obsidian-skills.md — earlier Obsidian-skills source; same architectural family

## Raw Concept

This page is a **stub accumulator**. Its purpose is to track which Claude Code skills get merged into the OSINT workspace's `~/.claude/skills/` directory over time, with provenance + Cemini-specific adaptation notes for each.

The page is intentionally empty at creation (2026-05-05). Content arrives as ROADMAP item #15 (Claude-OSINT skill merge) executes. **No skill is merged into `~/.claude/skills/` without a corresponding entry on this page.** This is the audit-trail discipline that prevents skill-drift (untracked skills accumulating with no provenance).

## Narrative

### Why this page exists

The OSINT workspace is itself an OSINT operation (per `@CLAUDE.md`). Cemini's K-series research keeps surfacing high-quality SKILL.md libraries — Claude-OSINT (5,500 lines, K30), claude-obsidian's `/autoresearch` skills (Wave 5B), kepano's Obsidian skills, XSKILL's academic Skill Library framework. Each contains skills that, ported into `~/.claude/skills/`, would augment the curator workflow.

But blindly merging 5,500 lines of upstream skills dilutes the workflow. The discipline:

1. **Phase 0**: inspect the upstream skill library; categorize skills by relevance
2. **Phase 1**: selectively port the Cemini-relevant subset
3. **Phase 2**: document each ported skill on this page with:
   - Skill name + path in `~/.claude/skills/`
   - Upstream source + license
   - Cemini-specific adaptation notes (if any)
   - Date merged + curator who merged it
4. **Phase 3**: periodic review — if a merged skill stops being used, retire it (and note the retirement here)

### Format for each merged skill

```markdown
### <skill name>

- **Path**: `~/.claude/skills/<skill-name>.md` (or per Anthropic's skill format)
- **Upstream**: `@entities/tools/<source>.md` (e.g. `claude-osint.md`)
- **License**: MIT / Apache-2.0 / etc.
- **Cemini adaptation**: <if any text was changed from upstream; if no changes, write "verbatim port">
- **Use case**: <when this skill fires; trigger conditions>
- **Date merged**: YYYY-MM-DD
- **Status**: active | retired YYYY-MM-DD (with reason)
```

### Currently merged skills

*(none — this page is in stub state until ROADMAP item #15 executes.)*

When item #15 ships, the first batch of merged skills will be documented here with the format above. The expected first-merge candidates from Claude-OSINT (per `@entities/tools/claude-osint.md`) are skills covering:

- Source-page generation conventions
- Cross-link discipline / `@path` resolution
- Citation patterns for OSINT material
- Provenance tracking
- Lint patterns for OSINT-specific quality flags

**Selectivity hard rule**: if Cemini's K-series ingest discipline already covers a skill's domain, don't merge — duplicate coverage adds noise. The merge target is gaps, not parallel implementations.

### Cross-skill dependencies

Some skills depend on others (e.g., a "deep-read" skill might invoke a "citation-extraction" skill). When a skill is merged, document any dependencies on other skills — both already-merged and not-yet-merged. This prevents the "merged skill X but it requires unmerged skill Y" failure mode.

## Snippets

*(populate as skills are merged + their upstream descriptions provide quotable framing.)*

## Dead Ends

*(populate when a candidate skill is evaluated and rejected — record why so the same skill isn't re-evaluated next time.)*
