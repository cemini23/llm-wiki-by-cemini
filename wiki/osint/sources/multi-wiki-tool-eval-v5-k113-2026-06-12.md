---
title: "Tool Evaluation — 28-URL Hermes + skills batch (K113)"
type: source
tags: [docx, tool-evaluation, multi-wiki, hermes, skillclaw, k113]
keywords: [hermes-workspace, skillclaw, ai-research-skills, wondelai, cloddsbot, convlstm-reject]
related:
  - sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md
  - entities/tools/hermes-workspace.md
  - entities/tools/skillclaw.md
  - entities/tools/ai-research-skills.md
  - entities/tools/wondelai-skills.md
  - entities/tools/all-agentic-architectures.md
  - entities/tools/cloddsbot.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - sources/trading-posts-compilation-9-2026-06-12.md
  - "@ccc-wiki/sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md"
maturity: validated
read_status: deep-read
created: 2026-06-12
updated: 2026-06-12
clusters: [cemini-internal, agent-harness]
---

## Relations

- @sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md — prior 63-URL batch
- @entities/tools/hermes-workspace.md — Adopt CONDITIONAL-GO
- @entities/tools/skillclaw.md — Adopt CONDITIONAL-GO
- @entities/tools/ai-research-skills.md — Adopt CONDITIONAL-GO
- @entities/tools/wondelai-skills.md — Adopt CONDITIONAL-GO (SEO primary)
- @entities/tools/all-agentic-architectures.md — Steal-from
- @entities/tools/cloddsbot.md — Steal-from reaffirmed (WC module 4 gap)
- @sources/trading-posts-compilation-9-2026-06-12.md — ConvLSTM repos cited Post 3 @AlterEgo_eth → Reject here

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Cemini Multi-Wiki Link Evaluation Report (v5, May 2026) |
| **sha256** | `1e2475fca75ebf7768ca44676b26083a46d9b57cc63c9509b8e86715b755c5af` |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/Cemini URL Evaluation Framework.docx` |
| **Retrieved** | 2026-06-12 |
| **URLs** | 28 |
| **License spot-check** | `.local/reports/license-spot-check-2026-06-12-0901.txt` |

## Narrative

Hermes-ecosystem + weather-repo noise batch. Eval prose is LLM-generated — **license and stars verified via `gh api` 2026-06-12** before entity verdicts.

### Tier rollup

| Tier | Count | Repos |
|------|-------|-------|
| **Adopt** | 4 | hermes-workspace, SkillClaw, AI-Research-SKILLs, wondelai/skills |
| **Steal-from** | 2 | CloddsBot, all-agentic-architectures |
| **Reference-only** | 4 | awesome-hermes-skills, awesome-hermes-agent, citadelwire.com, hermes-ecosystem (eval table only — URL 5 **Reject** on null license) |
| **Reject** | 7 | ConvLSTM×2, ML4BC, FinceptTerminal, Nimbus-weather1, weathermaps, IoT weather, tempo |
| **UNAVAILABLE** | 11 | weather hobby repos (404/private) |

### License corrections (eval → `gh api`)

| Repo | Eval claim | Verified 2026-06-12 |
|------|------------|---------------------|
| outsourc-e/hermes-workspace | MIT | **MIT**; **5,652★** (eval said ~500) |
| AMAP-ML/SkillClaw | MIT | **MIT**; **1,880★** |
| Orchestra-Research/AI-Research-SKILLs | MIT | **MIT**; **9,613★** |
| wondelai/skills | MIT | **MIT**; **1,300★** |
| alsk1992/CloddsBot | NO LICENSE | **MIT** `[CONFIRMED]` — steal-from unchanged |
| Fincept-Corporation/FinceptTerminal | AGPL-3.0 | **NOASSERTION** — keep **Reject** (IP-sale) |
| ksimback/hermes-ecosystem | null | **null** — **Reject** |
| tsugumi-sys/SA-ConvLSTM-Pytorch | null | **null** — **Reject** (K112 AlterEgo cites for weather — use arXiv + NOAA paths, not this repo) |
| shinigamixgod/tempo | null | **MIT** but domain Reject |

### World-cup-bot overlap

**CloddsBot** — genuine gap: Solana DEX + Meteora DBC patterns for WC advance module 4 fill handler (steal-only; no Node install).

### Cross-wiki routing (executed this session)

| Wiki | Deliverable |
|------|-------------|
| **CCC** | Entity stubs: hermes-workspace, skillclaw, wondelai; source mirror |
| **Cybersec** | Brief → `google-discovery` sibling + AI-Research-SKILLs ML-security skills brief |
| **SEO** | wondelai-skills entity (CRO/UX skills) |
| **Gambling** | K112 Lutchyn brief ingested (separate Posts route) |

### Phase-0 (`scripts/adopt_k113_phase0.sh`)

Laptop clone smoke for four Adopt repos — **CONDITIONAL-GO** all; no prod install.

## Snippets

> "SkillClaw's automated post-task evolution loop … distills episodic memories into verified skills" — eval URL 2; verify install path on laptop before Hermes coupling.

> "Fincept explicit AGPL-3.0 dual-license" — eval URL 10; `gh api` returns NOASSERTION — treat as **hard Reject** until SPDX resolved.
