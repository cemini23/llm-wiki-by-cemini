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
  - concepts/curator-skills.md
maturity: validated
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

### Phase 0 audit — completed 2026-05-05, verdict NO-PORT

Cloned `https://github.com/elementalsouls/Claude-OSINT` to `/tmp/claude-osint-audit/`. Eval claim accurate on lines (~5,861 confirmed) and license (MIT). But the eval's *framing* was misleading: I expected "many small focused skills"; reality is **2 large skills totalling 5,861 lines**.

Resolved Phase 0 questions:

| # | Question | Finding |
|---|----------|---------|
| Q1 | License + maturity | MIT ✓; 476 stars; latest commit 2026-04-27; skills declare `version: 2.1` / `2.1.1`; CHANGELOG documents 32-test smoke-run battle-testing. **Active and reputable.** |
| Q2 | Skill inventory | **2 skills (not many small ones)**: `osint-methodology` (1,693 lines, "how to think") + `offensive-osint` (4,168 lines, "what to reach for"). Both are reference-document-shaped, not tactical micro-skills. Format: Anthropic's official Claude Code skill format (YAML frontmatter `name`/`description`/`version`/`triggers` + Markdown body). |
| Q3 | Cemini-relevance | **0 PORT-DIRECTLY, 0 PORT-WITH-ADAPTATION, 2 DUPLICATE-DOMAIN.** Both skills target *external reconnaissance / red-team OSINT* (subdomain enumeration, SSO/SAML mapping, GraphQL/Swagger attack surface, secret scanning, mobile/cloud attack surface, vulnerability prioritization, threat-actor investigation). |
| Q4 | Format compat | **DIRECTLY COMPATIBLE technically.** Skills load into `~/.claude/skills/` without modification. But "compatible" ≠ "useful." |
| Q5 | Recommended port list | **EMPTY.** No skills mapped to Cemini's curator workflow. |

### Why NO-PORT — domain mismatch, not technical mismatch

Claude-OSINT skills exist to help a user **conduct reconnaissance** against a target (find subdomains, validate credentials, identify attack paths, generate red-team reports). Cemini's curator workflow exists to help **ingest and organize research sources** (validate provenance, extract takeaways, cross-link concepts, build indexes). These are orthogonal problem spaces.

Concrete example: if a Cemini curator session pulls `offensive-osint` because the user mentions "secret scanning," Claude would receive a 4,168-line reference on how to find leaked AWS keys in a target's GitHub repos — not how to validate and cite a source that *discusses* AWS secret-management best practices. The skill would fire on the keyword and add 4k+ lines of irrelevant context.

Cemini already covers source-side validation via:
- `scripts/preingest_check.py` (SHA256 + arXiv-ID + DOI dedup)
- `scripts/skill_audit.py` (brief structure + crosslinks + citations + NV freshness)
- `scripts/wiki_gap_detect.py` (Type-A/D/E gap detection)
- `scripts/cross_doc_dedup.py` (content fingerprinting)

These are wiki-style (ingest-source → lint → cross-link → archive). Claude-OSINT is OSINT-style (find-target → enumerate → validate-findings → report). The **selectivity discipline** documented in `@concepts/curator-skills.md` ("no skill merged into ~/.claude/skills/ without an entry on this page" + "merge target is gaps, not parallel implementations") makes this a clean reject.

### Eval-quality footnote

The K30 Gemini DR eval (`@sources/5-5-links-tool-eval.md` URL 6) used the phrasing "5,500 lines of specialized SKILL.md files" (plural) which **misled the evaluator (me) about granularity**. The accurate framing is "2 specialized large-format SKILL.md reference documents totalling 5,861 lines." Volume claim correct; granularity claim ambiguous.

This is a real evaluator-quality lesson: **future Gemini DR sweeps should ask "how many distinct skills" not just "how many lines"** when evaluating skill libraries. Logged for the K-series ingest discipline.

### When this verdict could flip

NOT generic-rejection. Re-evaluation triggers:
- If Cemini ever needs **OSINT-style external reconnaissance capabilities** (e.g., investigating a counterparty's tech stack for risk-assessment purposes, or monitoring competitor product launches via subdomain enumeration), the offensive-osint skill becomes directly applicable. Currently out-of-scope per Cemini's financial/prediction-market focus.
- If a future Claude-OSINT version adds **curator-workflow skills** (source ingestion, citation management, wiki page generation) — currently absent.

Until one of those triggers, Claude-OSINT stays shelved.

### Cleanup

`/tmp/claude-osint-audit/` removed post-audit.

## Snippets

- **Scope framing** (K30 eval): "paired set of highly structured SKILL.md files containing over 5,500 lines of specialized Open-Source Intelligence." [Source: 5_5 links.docx URL 6]

- **Recommendation tier**: "Steal-from. The primary v[alue is the SKILL.md library]." [Source: 5_5 links.docx URL 6]
