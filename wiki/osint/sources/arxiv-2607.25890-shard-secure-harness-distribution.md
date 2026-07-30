---
title: "arXiv 2607.25890 — SHarD: distributing security controls via harness"
type: source
tags: [source, arxiv, harness, security, ccc, cybersec, k206]
keywords: [SHarD, OWASP agentic, OS sandbox, skill scanning, tool restriction, Pi harness]
related:
  - sources/newsletter-rss-latent-space-2026-07-29-ai-eating-finance.md
  - entities/tools/openai-codex-security.md
  - entities/tools/agent-security-lab.md
  - sources/newsletter-rss-latent-space-2026-07-29-rsi-hf-agent-attack.md
maturity: draft
created: 2026-07-29
updated: 2026-07-29
read_status: deep-read
---

## Relations

- @sources/newsletter-rss-latent-space-2026-07-29-ai-eating-finance.md — same-day LS

- @entities/tools/openai-codex-security.md — Codex Security CLI

- @entities/tools/agent-security-lab.md — Phase-0 Extract (MIT lab artifacts)
- @sources/newsletter-rss-latent-space-2026-07-29-rsi-hf-agent-attack.md — HF agent-attack IR parallel

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Distributing Security Controls Through Harness Engineering |
| Author | Robbie Gore (Georgia Tech) |
| arXiv | 2607.25890 |
| Filename | `arxiv-2607.25890-distributing-security-controls-through-harness-e.pdf` |
| sha256 | `a1704768ab09e6ad332525eee2552efb44e65e1f4759d7bed0e3085e0aae358b` |
| Retrieved | 2026-07-29 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.25890-distributing-security-controls-through-harness-e.pdf` |
| Repo | https://github.com/wrgore/agent-security-lab (MIT, ~669 KB) |

## Narrative

Security is the #1 barrier to agent adoption; vendor-native controls lock ecosystems. Paper asks whether harnesses can distribute off-the-shelf controls (OS sandboxing, skill scanning, tool restriction) mapped to OWASP Top 10 for Agentic Applications (23-test suite). **SHarD** on Pi harness: single-install distribution; adjusted score **100%**, matching best secured commercial agent; no category regressions. Model non-determinism → inconsistent security outcomes; autonomous agents can cross OS boundaries that sandboxing catches.

**Phase-0:** CONDITIONAL-GO Extract — lab cloned to `.local/adopts/agent-security-lab` (~944 KB). `wrgore/shard` (~52 MB) deferred. Route CCC + cybersec briefs.

## Snippets

> SHarD achieved an adjusted score of 100%, matching the best securely configured commercial agent.

[Source: arXiv:2607.25890]
