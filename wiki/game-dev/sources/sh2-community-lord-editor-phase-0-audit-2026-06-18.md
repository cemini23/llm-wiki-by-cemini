---
title: SH2 Community Lord Editor Phase-0 audit — 2026-06-18
type: source
tags: [source, phase-0, stronghold-2, modding, audit]
keywords: [lord-editor, asophix, gamerules, ai]
related:
  - entities/tools/sh2-community-lord-editor.md
  - concepts/stronghold-2-ai-lords.md
  - concepts/stronghold-2-mod-ecosystem-shelf.md
  - sources/sh2-mod-ecosystem-scan-youtube-moddb-2026-06-18.md
  - sources/sh2-nation-fandom-ai-lords-2026-06-18.md
  - entities/projects/castle-sim.md
read_status: read
source_type: operator-audit
source_url: https://www.stronghold-nation.com/downloads/category/stronghold-2/miscellaneous/
maturity: validated
created: 2026-06-18
updated: 2026-06-18
---

## Raw Concept

Phase-0 audit of **Stronghold 2 Community Lord Editor v1.1** (Asophix) — Windows binary editing **`gameRules.dat`** AI lord behaviour.

## Narrative

### Method

Stronghold Nation download listing + forum threads (topic 1182, 1263). Compare to `castle-sim/data/sh2/lord_profiles.json` field coverage.

### Checks

| Gate | Result |
|------|--------|
| License | **None** — closed binary; design reference only |
| Maturity | v1.1 (Aug 2025); 23 KB installer; active Nation hosting |
| Mechanism | GUI over `gameRules.dat` — harass/siege mixes, castle weights, lord packs |
| Failure modes | Steam update may invalidate dat layout; backup vanilla dat before edit |
| castle-sim fit | **STEAL-FROM (schema)** — transcribe experiments to JSON; no runtime dat dependency |

### Steal value

| Extract | Skip |
|---------|------|
| Lord field vocabulary for JSON schema | Shipping editor or dat in public repo |
| Validation loop vs wiki AI lord tables | Expecting source code |
| Rapid retail AI experiments | Importing Firefly dat files |

### Verdict

**STEAL-FROM (design)** — best SH2-native lord tuning UI. Install: gitignored `briefs/sh2-community-lord-editor-install.md`.

## Dead Ends

- Phase-0 clone to `/tmp` — no public source repo; audit is distribution + forum only
