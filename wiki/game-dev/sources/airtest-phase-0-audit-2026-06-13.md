---
title: Airtest Phase-0 audit — 2026-06-13
type: source
tags: [source, phase-0, automation, ui-test, audit]
keywords: [airtest, netease, image-recognition]
related:
  - entities/tools/airtest.md
  - concepts/tool-evaluation-cross-wiki-batch-2026-06-13.md
  - entities/tools/godot-stagehand.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - sources/tool-evaluation-cross-wiki-routing-2026-06-13.md
read_status: read
source_type: operator-audit
source_url: https://github.com/AirtestProject/Airtest
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Raw Concept

Phase-0 audit of **AirtestProject/Airtest** — Apache-2.0 cross-platform UI automation via image recognition.

## Narrative

### Method

Clone @ main (2025-12-04 merge v1.4.3) to `/tmp/phase0-audit/Airtest`. Read `setup.py`, README, package layout.

### Checks

| Gate | Result |
|------|--------|
| License | **Apache-2.0** [CONFIRMED — LICENSE] |
| Maturity | NetEase-backed; active Dec 2025; Travis CI badge; pip `airtest` distribution |
| Architecture | Image template matching + optional Poco hierarchy; Android/iOS/Windows |
| Install | `pip install -U airtest`; bundles adb static binaries |
| vs godot-stagehand | Screen-space vs Godot WebSocket in-engine — **different layer** |
| castle-sim fit | **NO-GO primary** — use stagehand for game CI; Airtest for editor chrome / non-Godot UIs |

### Adoption surface

| Wiki | Verdict |
|------|---------|
| @ccc-wiki | **CONDITIONAL-GO** — lazy-tool visual fallback after sandbox eval |
| game-dev-wiki | **Reference-only** stub |

### Failure modes

- Template images brittle on resolution/UI skin changes
- adb permission chmod on Mac/Linux install path
- Not a substitute for headless Godot export tests

### Verdict

**CONDITIONAL-GO** on @ccc-wiki (Adopt tier from tool eval). **NO-GO** as castle-sim default — @entities/tools/godot-stagehand.md wins W2.

## Snippets

Core API pattern: `connect_device` → touch/template → assert_exists — see airtest.readthedocs.io.
