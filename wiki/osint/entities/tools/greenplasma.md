---
title: GreenPlasma — Windows CTFMON privesc PoC (Steal-from, cybersec primary)
type: entity
tags: [tool, exploit, privesc, ctfmon, windows-kernel, steal-from, cybersec-cross-route, mit]
keywords: [greenplasma, ctfmon, arbitrary section creation, system privilege, windows kernel, blind trust]
related:
  - sources/multi-wiki-link-eval-prompt-2026-05-13.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@sources/multi-wiki-link-eval-prompt-2026-05-13.md` — origin source (Doc 2, K42), Steal-from
- `@concepts/tool-evaluation-framework.md` — methodology

## Raw Concept

- **URL**: `https://github.com/Nightmare-Eclipse/GreenPlasma`
- **License**: MIT
- **Stars**: 285 / 0 open issues
- **Stack**: C++ (100%)
- **Date**: May 2026 (newly released)
- **Tier**: Steal-from
- **Primary fit**: Cybersec-wiki

## Narrative

Windows CTFMON Arbitrary Section Creation vulnerability PoC enabling SYSTEM-level Elevation of Privilege via kernel-driver "blind trust" exploitation. Stripped of full SYSTEM-shell launch logic. **Cross-route to `@cybersecurity-wiki/`** for blue-team behavioral detection rule engineering + red-team memory manipulation primitives.

[NEEDS VERIFICATION 2026-05-13]

[Source: Multi-Wiki Link Evaluation Prompt.docx URL 17 (retrieved 2026-05-13)]
