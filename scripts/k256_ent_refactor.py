#!/usr/bin/env python3
from pathlib import Path
p = Path(__file__).resolve().parent.parent / "wiki/entities/tools/refactor-platform.md"
p.write_text(
    "---\n"
    "title: RefactorPlatform — repo-scale refactoring agent harness\n"
    "type: entity\n"
    "tags: [tool, k256, harness, mit, ccc]\n"
    "keywords: [RefactorPlatform, PiSchool, AST-chunking]\n"
    "related:\n"
    "  - concepts/k256-harness-evolution-wave.md\n"
    "  - concepts/k256-eval-github-wave.md\n"
    "  - sources/arxiv-2609.04898-refactorplatform-2026-09-07.md\n"
    "maturity: draft\n"
    "created: 2026-09-07\n"
    "updated: 2026-09-07\n"
    "phase_0_verdict: GO REFERENCE\n"
    "harness_verb: FILE\n"
    "wire_note: Laptop REFERENCE clone; do not replace Cursor or /route.\n"
    "---\n\n"
    "## Relations\n\n"
    "- @concepts/k256-harness-evolution-wave.md\n"
    "- @concepts/k256-eval-github-wave.md\n"
    "- @sources/arxiv-2609.04898-refactorplatform-2026-09-07.md\n\n"
    "## Raw Concept\n\n"
    "| Field | Value |\n|-------|-------|\n"
    "| **Repo** | https://github.com/PiSchool/refactor-platform |\n"
    "| **License** | MIT `[CONFIRMED]` gh api SPDX 2026-09-07 |\n"
    "| **Local** | `.local/adopts/refactor-platform` |\n"
    "| **Stars** | 2 (2026-09-07) |\n"
    "| **Paper** | arXiv:2609.04898 |\n\n"
    "## Narrative\n\n"
    "Official companion. AST chunking plus 25-30 percent vs token windows. Lean retrieval single agent 86 percent vs sub-agent 66 percent. Harness eval yardstick, not a Cemini worker.\n\n"
    "**Verdict.** **GO REFERENCE** FILE. Do not Integrate. Do not swap `/route`.\n\n"
    "## Snippets\n\n"
    '> "RefactorPlatform is open-sourced to make refactoring-agent evaluation reproducible and auditable." [Source: arxiv-2609.04898]\n',
    encoding="utf-8",
)
print("wrote", p)
