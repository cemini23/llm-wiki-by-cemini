---
title: "K39 — Evaluating Project Links for Stacks (17-URL Three-Surface Batch)"
type: source
tags: [source, evaluation-brief, tooling, three-surface-fit, agents, mcp, claude-alternatives, k39]
keywords: [URL eval, project links, file transfer, agent skills, headless browser, claude alternatives, mac code, polymarket, license audit, EUPL-1.2]
related:
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - entities/tools/drift.md
  - entities/tools/kepano-obsidian-skills.md
  - entities/tools/open-notebook.md
  - entities/tools/nvidia-openshell.md
  - entities/tools/taranis-ai.md
  - entities/tools/x711.md
  - entities/tools/daybreak-openai.md
  - entities/tools/gabagool.md
  - entities/tools/ducky.md
  - entities/tools/meridian.md
  - entities/tools/deepseek-tui.md
  - entities/tools/obscura-headless-browser.md
  - entities/tools/mac-code.md
  - entities/tools/opensourceprojects-dev-99aca206.md
  - entities/tools/opensourceprojects-dev-1a77fca0.md
  - entities/tools/opensourceprojects-dev-c4a3cfc9.md
maturity: validated
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@concepts/tool-evaluation-framework.md` — three-surface methodology
- `@concepts/cemini-license-posture.md` — IP-sale-readiness license clean-list enforcement (EUPL-1.2 added this batch)

## Raw Concept

- **Title**: System Stack & Technology Evaluation Report (Project Links for Stacks)
- **Author**: User-prepared analyst memo (commissioned eval brief)
- **Type**: docx evaluation brief, 17 URLs scored on three-surface fit matrix (Cemini-prod / Wiki-librarian / Workflow-laptop)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Evaluating Project Links for Stacks.docx`
- **Retrieved**: 2026-05-11
- **sha256**: `b52024ec916e58c4…` (preingest verdict: NEW)
- **URLs**: 17 entries — 13 evaluated + 3 UNAVAILABLE (opensourceprojects.dev blocked) + 1 noted duplicate (URL 15 = URL 13)
- **Read-status**: deep-read

## Narrative

K39 batch — 17 URLs evaluated against the three-surface fit matrix. Heavy bias toward Workflow-tier tooling (developer-laptop ergonomics): 6 of 7 Adopt verdicts are Workflow-only, 1 also Cemini-prod. Notable mix of:

- File transfer + agent skills (drift, obsidian-skills)
- Claude/coding-agent alternatives (Meridian, DeepSeek-TUI, mac-code)
- Headless browser replacement claim (Obscura)
- Polymarket arbitrage bot #2 (gabagool, after K38 CloddsBot)
- One enterprise security platform (Daybreak) and one EU-licensed OSINT framework (taranis-ai) — both Reject

### Tier rollup

| Tier | Count | URLs |
|------|------:|------|
| **Adopt** | 6 | drift (URL 1), kepano/obsidian-skills (URL 2), Meridian (URL 11), DeepSeek-TUI (URL 12), Obscura (URL 16), mac-code (URL 17) |
| **Steal-from** | 2 | NVIDIA OpenShell (URL 4), gabagool (URL 8) |
| **Reference-only** | 2 | Open Notebook (URL 3), x711 (URL 6) |
| **Reject** | 3 | taranis-ai (URL 5), Daybreak (URL 7), Ducky (URL 10) |
| **UNAVAILABLE** | 3 | URLs 9, 13, 14 (opensourceprojects.dev blocked) |
| **Duplicate** | 1 | URL 15 = URL 13 (noted, omitted) |

### Domain clustering

- **File transfer & dev plumbing** (URL 1): drift — single-binary Rust WebSocket encrypted transfer; eval suggests replacing `scp` for laptop→prod brief shipping. **High-bus-factor single-dev project.**
- **Markdown / agent-skill ergonomics** (URL 2): kepano/obsidian-skills — Agent Skills schemas for Obsidian Flavored Markdown. Eval claims 30.5K★ + Claude-Code-compatible. **NEEDS Phase-0 verification on stars and integration claims.**
- **Self-hosted RAG / notebook** (URL 3): Open Notebook (lfnovo) — privacy-focused NotebookLM clone; Next.js + FastAPI + SurrealDB. Reference-only on RAM (3-5 GB baseline) + database paradigm mismatch (SurrealDB vs Cemini's PostgreSQL/TimescaleDB).
- **Agent sandboxing** (URL 4): NVIDIA OpenShell — Apache-2.0, Docker-based agent sandbox with declarative network/file policies. Steal-from the policy schemas; full deployment Docker-in-Docker abstraction too fragile for 24/7 trading.
- **OSINT / threat intel** (URL 5): taranis-ai — **EUPL-1.2 IP-sale poison pill** (SaaS distribution clause = forced source disclosure on remote-network access). New license blocker for the catalog. 16 GB hardware envelope also disqualifying.
- **Agent gas-station / shared memory** (URL 6): x711 — pay-per-use API service for cross-agent shared memory ("The Hive"); reference-only because external API is too immature, but the cross-agent shared-memory pattern is worth modeling in Redis `intel:*` channels.
- **Enterprise security AI** (URL 7): Daybreak — OpenAI cybersecurity platform; rejected on enterprise-only access + proprietary-algo exposure via OpenAI ingestion.
- **Polymarket arbitrage bot** (URL 8): gabagool — extract Python risk-manager schemas + `.env` threshold params (`yes_threshold`, `max_concurrent_arbitrages`) + arbitrage math; port to Kalshi adapter. **2nd Polymarket arb bot pattern after K38 CloddsBot.**
- **Desktop GUI tools — reject** (URL 10): Ducky — Tauri desktop GUI; fundamental headless-infra mismatch.
- **Claude / coding-agent alternatives** (URLs 11, 12, 17):
  - **Meridian** — "Use your Claude Max subscription with…" — strong **Family-C TOS landmine smell** (cf. 9router K38 + finance-skills K36). Adopt verdict marked **NEEDS Phase-0** before any laptop install.
  - **DeepSeek-TUI** (Hmbown) — eval recommends full Claude Code → DeepSeek-TUI migration. **Aggressive Adopt without Phase-0 is the exact mischaracterization pattern caught 6× in K28+K30+K36+K38.**
  - **mac-code** (walter-grace) — MLX-streaming Apple Silicon Claude Code variant; eval brief itself flags SSD wear via `F_NOCACHE` bypassing OS caching. Adopt despite hardware-degradation warning needs verification.
- **Headless browser** (URL 16): Obscura (h4ckf0r0day) — claims to wholesale-replace Playwright/Headless Chrome on laptop + production. **Single-dev project, aggressive scope, needs Phase-0.**

### Cross-wiki routing

No URLs in K39 are strong cross-wiki candidates.
- obsidian-skills is markdown-tooling but the other 3 wikis (image-gen, seo, 3d-printing) are CommonMark-only — Obsidian-specific schemas would mismatch.
- drift / Meridian / Obscura / mac-code / DeepSeek-TUI are dev-stack tools — same applies.
- gabagool is trading-specific.
- **Recommendation: skip cross-wiki routing for K39.**

### License posture warnings (gate before any Phase-0 audit promotion)

- **taranis-ai**: **EUPL-1.2** — hard reject. Article 14.3 + linking-as-distribution clauses force source disclosure on any remote-network reuse. Catalog entry pending.
- **NVIDIA OpenShell**: Apache-2.0 — clean.
- **drift / kepano/obsidian-skills / Open Notebook / gabagool / Meridian / DeepSeek-TUI / Obscura / mac-code**: MIT (per eval brief) — pending Phase-0 verification.
- **Ducky**: license not located in brief — verify before any deeper engagement.
- **x711 (Moltbook)**: closed-source SaaS — Reference-only stance correct.
- **Daybreak**: OpenAI proprietary — Reject stance correct.

### Phase-0 mischaracterization RED-FLAG queue (5 items)

Each requires source-clone + entry-point read + license verification before Adopt-verdict acceptance, per established Phase-0 audit discipline (`@concepts/cemini-license-posture.md`).

1. **Meridian** — "Use your Claude Max subscription with…" — high TOS-landmine risk (Family-C). Verify whether OAuth-grafts onto Anthropic credentials for proxy/resale (same pattern as 9router NO-GO 2026-05-11).
2. **DeepSeek-TUI** — Adopt verdict recommends full Workflow migration off Claude Code. Verify maturity (single-dev, ~Apr 2026 project age), provider lock-in, and MCP-compatibility before any actual workflow change.
3. **Obscura** — wholesale Playwright/Headless Chrome replacement claim across laptop + production. Verify actual scraping API surface vs. claimed coverage.
4. **NVIDIA OpenShell** — Apache-2.0 v0.0.37 plausible but unverified. Confirm NVIDIA-published vs. third-party derivative.
5. **mac-code** — SSD-wear warning in the eval brief itself. Verify whether `F_NOCACHE` opt-out exists or whether the wear is unavoidable; do not install pending hardware-impact assessment.

### Reading method

- 13 reachable URLs read in full
- 3 UNAVAILABLE (URLs 9, 13, 14) flagged for Exa-resolution
- 1 noted duplicate (URL 15 = URL 13) not pursued

[Source: Evaluating Project Links for Stacks.docx, retrieved 2026-05-11]
