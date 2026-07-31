---


title: OpenAI Codex Security CLI
type: entity
tags: [entity, tool, security, codex, ccc, cybersec, phase-0, k211]
keywords: [openai/codex-security, @openai/codex-security, CI scanner, Apache-2.0]
related:
  - entities/tools/agentenv.md
  - sources/newsletter-rss-latent-space-2026-07-29-ai-eating-finance.md
  - sources/arxiv-2607.25890-shard-secure-harness-distribution.md
  - entities/tools/agent-security-lab.md
  - sources/arxiv-2607.26819-coding-agents-ai-contribution-rules-2026-07-30.md
maturity: draft
created: 2026-07-29
updated: 2026-07-31
wire_status: policy_wired
wire_target: .cursor/rules/osint-phase1-adopt-wires.mdc
---

## Relations

- @sources/arxiv-2607.26819-coding-agents-ai-contribution-rules-2026-07-30.md — OSS AI contribution rules

- @entities/tools/agentenv.md — Watch microVM isolation

- @sources/newsletter-rss-latent-space-2026-07-29-ai-eating-finance.md — announcement ingest
- @sources/arxiv-2607.25890-shard-secure-harness-distribution.md — harness control distribution
- @entities/tools/agent-security-lab.md — SHarD lab parallel

## Narrative

| Field | Value |
|-------|--------|
| Repo | https://github.com/openai/codex-security |
| License | **Apache-2.0** |
| npm | `@openai/codex-security` |
| Local | `.local/adopts/codex-security` (~4.2MB) |
| Verdict | **CONDITIONAL-GO Extract** — CI/repo vuln scan patterns for CCC + cybersec; compare to cursor-security-preflight |

Scan codebases, track findings across runs, verify fixes. Do not replace federation preflight — complementary.
