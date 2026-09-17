#!/usr/bin/env python3
from pathlib import Path
p = Path(__file__).resolve().parent.parent / "wiki/entities/tools/trailofbits-skills.md"
p.write_text(
    "---\n"
    "title: trailofbits/skills — security audit skill catalog\n"
    "type: entity\n"
    "tags: [tool, k256, cybersec, cc-by-sa-4.0]\n"
    "keywords: [trailofbits, fp-check, CodeQL]\n"
    "related:\n"
    "  - concepts/k256-eval-github-wave.md\n"
    "  - sources/eval-url-revenue-analysis-2026-09-07.md\n"
    "maturity: draft\n"
    "created: 2026-09-07\n"
    "updated: 2026-09-07\n"
    "phase_0_verdict: EXTRACT-ONLY\n"
    "harness_verb: FILE\n"
    "wire_note: CC-BY-SA-4.0 share-alike — do not import into federation skill dirs.\n"
    "---\n\n"
    "## Relations\n\n"
    "- @concepts/k256-eval-github-wave.md\n"
    "- @sources/eval-url-revenue-analysis-2026-09-07.md\n\n"
    "## Raw Concept\n\n"
    "| Field | Value |\n|-------|-------|\n"
    "| **Repo** | https://github.com/trailofbits/skills |\n"
    "| **License** | CC-BY-SA-4.0 `[CONFIRMED]` gh api SPDX 2026-09-07 |\n"
    "| **Local** | `.local/adopts/trailofbits-skills` |\n"
    "| **Stars** | 6998 (2026-09-07) |\n\n"
    "## Narrative\n\n"
    "Eval docx claimed Integrate. Overridden. Share-alike license plus federation skill-sync collision. EXTRACT-ONLY. No skill auto-evolve.\n\n"
    "**Verdict.** **EXTRACT-ONLY** FILE. **NO-GO Integrate.**\n\n"
    "## Snippets\n\n"
    '> "CC-BY-SA-4.0 `[CONFIRMED]` gh api 2026-09-07; 6998 stars." [Source: gh api repos/trailofbits/skills]\n',
    encoding="utf-8",
)
print("wrote", p)
