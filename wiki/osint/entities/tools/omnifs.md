---
title: "/omnifs — projected filesystem for APIs and agents"
type: entity
tags: [entity, tool, agent-infrastructure, filesystem, mcp-adjacent, k108]
keywords: [omnifs, 0xff-ai, fuse, wasm-providers, plan9, raulvk]
related:
  - sources/trading-posts-compilation-8-2026-06-09.md
  - concepts/claude-code-skills-md-workflow.md
  - concepts/cemini-repository-topology.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/omnifs.md
  - "@ccc-wiki/briefs/2026-06-09_k108-ccc-hive-ship-omnifs-from-osint.md"
maturity: draft
created: 2026-06-09
updated: 2026-06-09
---

## Relations

- @sources/trading-posts-compilation-8-2026-06-09.md — K108 Post 1 (@raulvk)
- @concepts/claude-code-skills-md-workflow.md — complementary agent substrate (skills vs path namespace)
- @concepts/wiki-tooling-evaluation.md — Phase-0 registry
- @ccc-wiki/briefs/2026-06-09_k108-ccc-hive-ship-omnifs-from-osint.md — setup handoff

## Raw Concept

K108 Posts.docx — @raulvk launch post for **/omnifs** (`omnifs.dev`, `github.com/0xff-ai/omnifs`). Projects external APIs into a FUSE filesystem (`/github`, `/linear`, `/docker`, `/dns`, `/arxiv`, `/db` providers today). Wasm sandboxed providers; host performs capability-gated callouts for network/credentials.

## Narrative

**Problem framed:** every service has its own client/schema/auth; filesystem paths are a universal coordination primitive agents already use (`cat`, `grep`, pipes).

**Security model:** providers suspend with declared callouts; host attaches credentials and executes effects — "providers ask, host acts."

**Status (repo, Jun 2026):** alpha; Rust host + Wasm providers; read-only; FUSE via Docker container (`npm install -g @0xff-ai/omnifs`); v0.2.1; NFSv4/FSKit planned to drop Docker requirement.

### Phase-0 audit (2026-06-09): CONDITIONAL-GO

| Signal | Value |
|--------|-------|
| License | **Apache-2.0** `[CONFIRMED]` — `gh api repos/0xff-ai/omnifs` + `LICENSE-APACHE` in repo |
| Stars / activity | ~57 stars; pushed 2026-06-09; v0.2.1; 26 open issues |
| Layout rigidity | **Pass** — provider plugin model; `OMNIFS_HOME` / `~/.omnifs` config; no wiki path lock-in |
| Overlap vs Cemini | **Partial** — lazy-tool already proxies fetch, exa, github; omnifs adds path-NS + shell ergonomics, not kb-server |
| Failure mode | Alpha + Docker+FUSE ops; credential store under `~/.omnifs`; read-only today |

**Verdict:** **CONDITIONAL-GO** for **CCC laptop eval** — one operator trial (`omnifs setup` + GitHub/arXiv provider) before any conductor integration. **NO-GO** for prod stack, librarian, or kb-server replacement without design brief.

**Steal-from (no install required):** path namespace as agent handoff primitive; Wasm provider / host-callout trust boundary pattern for future MCP hardening.

**Re-check before install:** `bash scripts/adopt_k108_phase0.sh` + `gh api repos/0xff-ai/omnifs/license`

## Snippets

> "The common layer is not a universal schema. The common layer is the path namespace." [Source: Posts.docx K108, @raulvk Post 1]
