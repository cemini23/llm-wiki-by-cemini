---

title: "rclone/rclone"
type: entity
tags: [tool, phase-0, k216, atto]
keywords: [rclone]
related:
  - sources/eval-github-url-revenue-infra-cli-2026-08-01.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
created: 2026-08-01
updated: 2026-08-01
harness_verb: FILE
---

## Relations

- @sources/eval-github-url-revenue-infra-cli-2026-08-01.md
- @concepts/wiki-tooling-evaluation.md
- @concepts/gpuology-genealogy-agent-kit.md

## Narrative

| Field | Value |
|-------|--------|
| **Repo** | https://github.com/rclone/rclone |
| **License** | **MIT** [CONFIRMED gh 2026-08-01] |
| **Verdict** | **Extract GO — Atto vault sync/backup patterns** |
| **Local** | `.local/adopts/rclone (~62MB shallow)` |

Shallow clone added post-K216 when disk headroom confirmed (~14GB free). Prefer rclone for offline vault mirror patterns — not unattended cloud sync of PII without human gate.
