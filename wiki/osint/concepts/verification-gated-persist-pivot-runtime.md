---
title: "Verification-gated persist/pivot runtime (Argus pattern)"
type: concept
tags: [agents, memory, k253, k225, verification]
keywords: [Argus, persist, pivot, reviewer, long-horizon]
related:
  - sources/arxiv-2608.05144-argus-agentic-runtime-2026-08-06.md
  - concepts/bidirectional-hai-skill-evolution.md
  - concepts/llm-agent-failure-telemetry-monitors.md
maturity: draft
created: 2026-08-06
updated: 2026-08-06
---

## Relations

- @sources/arxiv-2608.05144-argus-agentic-runtime-2026-08-06.md
- @concepts/bidirectional-hai-skill-evolution.md
- @concepts/llm-agent-failure-telemetry-monitors.md — K242 complementary

## Raw Concept

K253 policy wire — separate planner/engineer from **independent Reviewer**; admit memories/skills only after review + task-native verify when available. `lbx154/Argus` **NO-GO clone** (NULL SPDX).

## Narrative

**Persist while evidence supports; pivot on measured failure** — durable project state across sessions (`hot.md`, ROADMAP, wiki) without verbatim negative transfer (K230 reconstruct-before-inject).

**Harness mapping:**

| Argus role | Cemini analog |
|------------|---------------|
| Manager/Planner | `/goal` architect session |
| Engineer | Grok/Codex implementer lane |
| Reviewer | `ingest_session_gate`, `skill_audit`, Fable advisor at commitment boundaries |
| Memory admit | Post-verify wiki commit only |

**No runtime wire** until SPDX resolved on upstream repo. Use pattern in multi-session Atto/CC prod brief workflows.

## Snippets

> Admit memories/skills only after review (+ task-native verify when available). [Policy K253]
