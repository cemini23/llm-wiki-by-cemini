---

title: agent-security-lab (SHarD / Gore) — harness security artifacts
type: entity
tags: [entity, tool, harness, security, ccc, cybersec, phase-0, k206]
keywords: [wrgore/agent-security-lab, SHarD, Pi harness, OWASP agentic, MIT]
related:
  - entities/tools/openai-codex-security.md
  - sources/arxiv-2607.25890-shard-secure-harness-distribution.md
  - sources/newsletter-rss-latent-space-2026-07-29-rsi-hf-agent-attack.md
  - sources/arxiv-2607.27080-memsecbench-agent-memory-poisoning-2026-07-30.md
maturity: draft
created: 2026-07-29
updated: 2026-07-30
---

## Relations

- @sources/arxiv-2607.27080-memsecbench-agent-memory-poisoning-2026-07-30.md — MemSecBench

- @entities/tools/openai-codex-security.md — Codex Security parallel

- @sources/arxiv-2607.25890-shard-secure-harness-distribution.md — paper + lab
- @sources/newsletter-rss-latent-space-2026-07-29-rsi-hf-agent-attack.md — HF agent-attack parallel

## Raw Concept

Phase-0 on Georgia Tech practicum artifacts for distributing OS sandboxing / skill scanning / tool restriction via a Pi-based harness (SHarD).

## Narrative

| Field | Value |
|-------|--------|
| Repo | https://github.com/wrgore/agent-security-lab |
| License | **MIT** (`gh api` 2026-07-29) |
| Size | ~669 KB GitHub / ~944 KB shallow clone |
| Local | `.local/adopts/agent-security-lab` |
| Verdict | **CONDITIONAL-GO Extract** — study tests + control mapping; do **not** wire into Atto |
| Deferred | `wrgore/shard` (~52 MB) / `shard-demo` — re-eval if CCC adopts Pi harness distribution |

Contains paper PDF, 23-test suite markdown, benign injection fixtures under `prod/`, JSON results under `data/`. Related early beta: github.com/wrgore/shard.

**Route briefs:** CCC + Cybersecurity wiki. TipDrop only if Discord skill-scan ops reopen.

## Dead Ends

- Cloning `shard` (~52 MB) without a concrete CCC install ticket.
- Treating 100% lab score as production Cursor/Auto-run equivalence.
