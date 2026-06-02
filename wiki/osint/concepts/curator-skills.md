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
  - sources/trading-posts-compilation-20-2026-05-27.md
  - sources/trading-posts-macro-charts-skills-md-2026-05-28.md
  - concepts/claude-code-skills-md-workflow.md
  - sources/trading-posts-compilation-20-2026-05-27.md
  - concepts/cemini-repository-topology.md
  - concepts/declarative-data-labeling-skills.md
  - entities/tools/skill-seekers.md
  - entities/tools/skillnet.md
  - "@ccc-wiki/concepts/muse-autoskill-skill-lifecycle.md"
maturity: draft
created: 2026-05-05
updated: 2026-06-02
---

## Relations

- @entities/tools/claude-osint.md — primary upstream source: K30 Steal-from of 5,500 lines of OSINT SKILL.md files. This concept page is the destination for skills selectively merged into `~/.claude/skills/`.
- @sources/xskill-2603-12056.md — XSKILL paper documents the SKILL.md Markdown format pattern + cross-rollout-critique discipline; informs how skills should be structured + maintained
- @sources/agriciDaniel-claude-obsidian.md — claude-obsidian's `/autoresearch` Markdown-skills pattern is the Obsidian-flavored predecessor; some skills may be ported from there
- @sources/kepano-obsidian-skills.md — earlier Obsidian-skills source; same architectural family
- @concepts/claude-code-skills-md-workflow.md — K76 Skills.md institutional-memory stub; ccc-wiki expansion pending

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

### MUSE pre-promotion gate [Steal-from 2026-06-02]

From @ccc-wiki/concepts/muse-autoskill-skill-lifecycle.md (arXiv 2605.27366): skills follow **create → store → manage → evaluate → refine**. Before any skill ships to `~/.claude/skills/`, prod finance-skills cache, or server hooks:

1. **Phase-0** license + domain fit (`scripts/skill_audit.py` or manual checklist)
2. **Unit-test / smoke** — one scripted invocation on a fixture task (pass/fail recorded on this page or in `wiki/log.md`)
3. **Promotion** — only after smoke pass; bump `updated:` on upstream entity if mirrored from eval

Aligns with existing `skill_audit.py` veto gates — MUSE adds explicit **evaluate-before-promote** wording.

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

**(none — Claude-OSINT Phase 0 audit 2026-05-05 returned NO-PORT; the page stays empty by design)**

The expected first-merge candidates were Claude-OSINT skills covering:
- Source-page generation conventions
- Cross-link discipline / `@path` resolution
- Citation patterns
- Provenance tracking
- Lint patterns for quality flags

**Audit finding**: Claude-OSINT contains 2 large-format skills (osint-methodology + offensive-osint, ~5,861 lines) targeting **external reconnaissance / red-team OSINT** (subdomain enumeration, SSO mapping, attack-surface analysis, secret scanning). Zero overlap with Cemini's curator workflow. See `@entities/tools/claude-osint.md` Phase 0 audit table for full evidence.

The selectivity hard rule worked: every Claude-OSINT skill fell into the DUPLICATE-DOMAIN category (Cemini's K-series + scripts/ already cover source-side validation; Claude-OSINT covers target-side reconnaissance). Porting any of them would add a parallel "source assessment" framework that doesn't fit the curator workflow's actual problem space.

**Selectivity hard rule (preserved for future skill candidates)**: if Cemini's K-series ingest discipline already covers a skill's domain, don't merge — duplicate coverage adds noise. The merge target is gaps, not parallel implementations.

### Future skill candidates (when they emerge)

This page activates when a candidate skill source genuinely fills a gap in Cemini's curator workflow. Possible sources to watch:
- **Anthropic skill registry** — when official Anthropic-curated skills land in claude-plugins-official, evaluate against the selectivity rule
- **claude-obsidian's `/autoresearch` Markdown-skills** (`@sources/agriciDaniel-claude-obsidian.md`) — Wave 5B Adopt; some of those may be wiki-curator-relevant rather than research-loop-specific. Re-audit when a specific gap emerges.
- **kepano-obsidian-skills** (`@sources/kepano-obsidian-skills.md`) — earlier Obsidian-skills source; same architectural family
- **XSKILL paper's MLLM Skill Library framework** (`@sources/xskill-2603-12056.md`) — academic source; the *pattern* of structured Markdown skill libraries is validated by the paper, but the K30 Conductor-evolution work has been deferred via the audit-trail-subset decision (per K28 #6/#6b → 6c). Skill-library work for Conductor stays paused too.

The **discipline rule stays in force**: any future skill merged into `~/.claude/skills/` requires a corresponding entry on this page with provenance + Cemini adaptation notes + date + active/retired status.

### Cross-skill dependencies

Some skills depend on others (e.g., a "deep-read" skill might invoke a "citation-extraction" skill). When a skill is merged, document any dependencies on other skills — both already-merged and not-yet-merged. This prevents the "merged skill X but it requires unmerged skill Y" failure mode.

## Snippets

*(populate as skills are merged + their upstream descriptions provide quotable framing.)*

## Dead Ends

*(populate when a candidate skill is evaluated and rejected — record why so the same skill isn't re-evaluated next time.)*
