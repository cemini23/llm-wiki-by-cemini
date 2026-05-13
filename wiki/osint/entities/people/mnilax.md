---
title: "@Mnilax (X handle)"
type: entity
tags: [entity, person, x-handle, claude-code-prompting, agent-orchestration, technical-writer, k41]
keywords: [mnilax, claude-md-12-rule-template-author, karpathy-extension, agent-orchestration-rules, claude-code-best-practices-may-2026]
related:
  - sources/x-docx-polymarket-claude-md-2026-04-23.md
  - concepts/claude-md-12-rule-template.md
  - entities/people/forrest-chang.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- @sources/x-docx-polymarket-claude-md-2026-04-23.md — primary source (Section 2)
- @concepts/claude-md-12-rule-template.md — primary concept
- @entities/people/forrest-chang.md — author of the 4-rule template Mnilax extends to 12

## Raw Concept

What prompted this page: K41 ingest of X.docx Section 2 — @Mnilax's article extending Forrest Chang's 4-rule CLAUDE.md template to 12 rules covering May 2026 agent-orchestration failure modes.

## Narrative

- **X handle**: @Mnilax
- **Subject expertise**: Claude Code prompting discipline; agent orchestration; CLAUDE.md template design
- **Known contribution**: 8 additional rules (#5-12) extending Karpathy → Forrest Chang's 4-rule CLAUDE.md template
- **Self-reported empirical work**: tracked 50 representative tasks across 30 codebases over 6 weeks across three configurations (no template / Karpathy 4 / Mnilax 12). Reports mistake rate 41% → 3%, compliance 78% → 76%.
- **Methodology not externally documented**: empirical claims author-asserted; not in any peer-reviewed publication or open methodology repo Cemini has visibility on
- Real identity not established

### Cemini posture

- **Structural framework of the 12 rules is operationally portable** to Cemini's CLAUDE.md hygiene (currently 322 lines, over Mnilax's claimed 200-line ceiling)
- **Empirical comparison numbers** (41% → 3%) are illustrative not measured; the rule contents are useful regardless of whether the specific delta is reproducible
- **Cross-paper corroboration**: Rule 10 (checkpoint discipline) is the operational sibling of measured failure mode in @sources/llms-get-lost-multi-turn-laban-2025.md (39% multi-turn perf drop, premature-commitment mechanism)
