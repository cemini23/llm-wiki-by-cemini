---
title: "Readme.skill — Personal Developer-Profile Generator (eval-brief MISCHARACTERIZED as repo-stats tool)"
type: entity
tags: [tool, claude-skill, personal-profile, workflow, k38, phase-0-no-go, eval-brief-mischaracterization, license-gap]
keywords: [readme, skill, defer, three-surface-eval, developer-profile, anonymized, chinese-readme]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - concepts/mcp-tool-marketplace.md
maturity: validated
created: 2026-05-11
updated: 2026-05-11
phase_0_audit: NO-GO 2026-05-11 — eval-brief framing mischaracterizes the skill function; LICENSE file missing
adoption_status: REJECT 2026-05-11 (potential Steal-from later for workforce-analytics 10-dimension framework only)
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 3)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context (LICENSE-file-missing pattern: same as finance-skills K36)
- `@concepts/mcp-tool-marketplace.md` — single-author skill profile (bus-factor + project-age rubric)

## Raw Concept

- **Repo / URL** [VERIFIED 2026-05-11]: `github.com/study8677/Readme.skill`
- **Tier (per source brief)**: Adopt → **DOWNGRADED 2026-05-11 to NO-GO** on Phase-0 audit
- **License** [VERIFIED 2026-05-11]: README footer claims "协议 — MIT"; **GitHub repo has NO LICENSE file**. Under default copyright, "no LICENSE = all rights reserved." Same pattern as `finance-skills` K36 (LICENSE-missing despite README MIT claim, upstream issue #64 filed). Upstream issue required before adoption.
- **Phase-0 audit** [VERIFIED 2026-05-11]: 68★ / 4 forks / single-author / 0 open issues. Created 2026-04-16 (25 days old at audit); last push 2026-05-08 (3 days fresh). Single SKILL.md artifact at `skills/readme-skill/SKILL.md`.

## Narrative — eval-brief mischaracterization

The K38 eval brief framed Readme.skill as an "agent skill for repo-stats auto-gen" augmenting "wiki-curation toolchain with structured repo-stats auto-gen." Phase-0 audit reveals:

1. **It generates personal developer-profile artifacts**, not repository statistics. The skill reads `~/.claude/stats-cache.json`, `~/.claude/history.jsonl`, `~/.codex/state_5.sqlite`, GitHub contribution graphs, + local git commits to synthesize a **3-5K-word Chinese-language Markdown profile** quantifying the user's Claude Code + Codex CLI usage across 10 dimensions (activity span, velocity, AI practices, collaboration style, token economics, etc.). Optional SVG poster output.
2. **The intended audience is individual developers sharing their AI-native work style with colleagues/recruiters** (anonymized via project-name redaction). The README is Chinese; the README.en.md keywords ("repo", "skill", "stats") evidently misled the DR sweep into the wrong product category.
3. **No wiki-curation, no repo-statistics, no librarian-server value.** The skill is domain-misaligned for Cemini's actual use cases (wiki curation, trading stack, librarian server).
4. **Cemini's existing skill discipline stack is unrelated**: `academic-paper-skills` (peer-review framework, ported to `scripts/skill_audit.py` v0.3), `research-paper-writing-skills` (claim-evidence + abstract synthesis, ported v0.4), `codex-startup-pressure-test-skill` (4-mode pressure-test, ported v0.5), `agent-skills-eval` (SKILL.md validator, DEFER). Zero overlap; Readme.skill does not extend any of these.

### Integration vector

**NO-GO 2026-05-11**. Adopt verdict is not justified — this is the **6th eval-brief mischaracterization** caught by Phase-0 across K28+K30+K38 (see `LESSONS.md` 2026-05-11 entry). No prod path; no laptop-workflow path either, because there is no current Cemini need for personal-Claude-usage portfolio reports.

### Possible Steal-from (deferred)

The 10-dimension developer-profile framework (activity span / velocity / AI practices / collaboration / project distribution / interests / rhythm / output density / leverage / token economics) is the only artifact with potential downstream value — and only IF a future workstream surfaces a workforce-analytics need (e.g., team-onboarding incentive measurement, individual-contributor skill mapping). That workstream is not on the K-series roadmap. File under Steal-from-with-trigger.

### Risks (if adopted anyway)

1. **LICENSE-file-missing landmine** — under default copyright, prose+SKILL.md is "all rights reserved." README MIT claim is unenforceable absent a LICENSE file. Same blocking pattern as `finance-skills` K36 (upstream issue #64 still open).
2. **Domain mismatch** — skill scope is personal-developer-profile, not wiki/trading-stack tooling. Adopting it pollutes the `~/.claude/skills/` namespace with off-domain artifact.
3. **Bus factor + project age** — single-author, 25 days old, 68 stars, 4 forks. Per `concepts/mcp-tool-marketplace.md` Pattern 2 (single-day-dev/early-stage), would require fork-and-pin if adopted now.

### Activation trigger (if ever — for Steal-from-only path)

Charter a workstream on workforce analytics / team-skill-mapping (NOT chartered here). Only then revisit the 10-dimension framework for extraction. Cemini-prod adoption remains permanently rejected.

[Source: Link Evaluation Brief Trading Stack.docx, URL 3; Phase-0 audit 2026-05-11]
