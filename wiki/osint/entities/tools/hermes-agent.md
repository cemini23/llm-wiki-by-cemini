---
title: Hermes Agent — Nous Research self-hosted self-improving agent
type: entity
tags: [entity, tool, llm-agent, agent-runtime, self-hosted, nous-research, self-improving, k52]
keywords: [hermes-agent, nous-research, self-hosted-agent, self-improving-skills, persistent-memory, memory-md, user-md, cron-scheduling, messaging-gateway, openclaw-successor]
related:
  - sources/x-kimi-k2.6-hermes-routing-playbook-2026-05.md
  - concepts/agent-cost-routing-model-orchestra.md
  - sources/x-posts-quant-oss-polymarket-bots-2026-05.md
  - sources/trading-posts-farxxxxx-hermes-koroush-2026-05-24.md
  - sources/trading-posts-compilation-20-2026-05-27.md
  - sources/trading-posts-macro-charts-skills-md-2026-05-28.md
  - sources/trading-posts-compilation-6-2026-05-29.md
  - sources/trading-posts-compilation-42-2026-05-31.md
  - sources/trading-posts-compilation-12-2026-06-01.md
  - sources/trading-posts-compilation-16-2026-05-31.md
  - concepts/hermes-onchain-forensics-pipeline.md
  - concepts/x402-agent-micropayments-data-access.md
  - concepts/claude-code-skills-md-workflow.md
  - entities/tools/hermes-lcm.md
  - concepts/openclaw-security-taxonomy.md
  - concepts/polymarket-weather-trading-strategy.md
  - concepts/polymarket-weather-bot-methodology-taxonomy.md
  - sources/alterego-eth-five-weather-methodologies-2026-05-27.md
  - "@ccc-wiki/entities/tools/hermes-agent.md"
  - entities/people/damidefi.md
  - sources/trading-posts-compilation-17-2026-06-03.md
maturity: draft
created: 2026-05-18
updated: 2026-06-03
---

## Relations

- @sources/x-kimi-k2.6-hermes-routing-playbook-2026-05.md — K40 Kimi cost-routing thread; **`[CONFIRMED 2026-05-29]`** "Hermes" billing dashboard = this repo
- @concepts/agent-cost-routing-model-orchestra.md — auxiliary-model orchestra distilled from Kimi/Hermes playbook
- @sources/x-posts-quant-oss-polymarket-bots-2026-05.md — Post 5 (@0xMovez), the source that surfaced Hermes Agent
- @entities/tools/hermes-lcm.md — Lossless Context Management is a context-engine *plugin* for the Hermes Agent ecosystem; this page is the host runtime
- @concepts/openclaw-security-taxonomy.md — Hermes Agent is positioned as the successor to OpenClaw (formerly Clawdbot / Moltbot); the security taxonomy there is the comparison frame
- @concepts/polymarket-weather-trading-strategy.md — Post 5 uses Hermes Agent as the runtime to deploy a Polymarket weather-trading bot
- @concepts/polymarket-weather-bot-methodology-taxonomy.md — K70 type 5 (AI-agent weather bots) cites Hermes
- @sources/alterego-eth-five-weather-methodologies-2026-05-27.md — K70 source
- @sources/trading-posts-farxxxxx-hermes-koroush-2026-05-24.md — K64 Post 2: community catalog of 276+ production use cases
- @sources/trading-posts-compilation-20-2026-05-27.md — K69 Post 11 (@NainsiDwiv50980 persistent memory emphasis)
- @sources/trading-posts-compilation-6-2026-05-29.md — K78: x402 forensics bundle + skill bundling (@AlphaCartell / @0xJeff)
- @concepts/hermes-onchain-forensics-pipeline.md — K78 pipeline synthesis
- @concepts/x402-agent-micropayments-data-access.md — K78 payment layer
- @ccc-wiki/entities/tools/hermes-agent.md — CCC routing stub

## Raw Concept

What prompted this page: K52 ingest of @0xMovez's X post deploying a Polymarket weather-trading bot on Hermes Agent. K64 adds @Shruti_0810 community deployment taxonomy (not new repo audit). The existing @entities/tools/hermes-lcm.md page referenced "the Hermes Agent ecosystem" without a host-runtime page — this fills that gap.

## Narrative

### What it is

Hermes Agent is an **open-source, self-hosted AI agent** built by **Nous Research** (the team behind YaRN, Nomos, and the Psyche model families). It is pitched not as a chatbot but as a persistent staff member: it remembers what you tell it, improves at recurring tasks, and stays reachable 24/7 even when your own machine is off. Supports Linux, macOS, and WSL2 (no native Windows).

**Verified 2026-05-18** (GitHub API): `NousResearch/hermes-agent` — **MIT license**, **~156,554★**, repo created **2025-07-22**, last pushed 2026-05-19 (actively maintained), not archived, description "The agent that grows with you." The post's install path (`raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh`) resolves (HTTP 200). Note: the post's "released February 25, 2026" refers to a major version/announcement, not the repo's birth — the project predates that by seven months. Nous Research ships a real ecosystem around it (`hermes-agent-self-evolution`, `hermes-compression-eval`, `hermes-example-plugins`, `Hermes-Function-Calling`). At ~156k★ it is a top-tier project — maturity is not in question; the posture below is about *fit*, not credibility.

**Wave 10 refresh (2026-05-29):** ~172k★; TUI documents slash-command autocomplete + `hermes model` provider switching (OpenRouter, Moonshot/Kimi, etc.). Resolves K40 open question — Hermes is **not** a Kilo Code / Augment alias.

### Three-layer model (per the @0xMovez / blockmates framing)

- **Knowledge layer** — built-in memory, session search, an LLM-Wiki skill, optional Honcho integration. Accumulates knowledge over time rather than just answering.
- **Execution layer** — multi-agent profiles, child agents, a tool system, MCP support, persistent dedicated-machine access. Decomposes tasks, runs them in parallel, delegates.
- **Output layer** — cron jobs, gateway delivery to Telegram/Slack/Discord/etc., a Web UI, file output. Results flow into a real workflow, not a chat window.

### Three differentiators

1. **Persistent memory.** Two core files — `MEMORY.md` (environment facts, conventions, experiences) and `USER.md` (preferences, communication style) — are loaded as a frozen snapshot into every new session. Full conversation history is kept in a SQLite database with full-text search.
2. **Self-improving skills.** After a complex task (~5+ tool calls) Hermes writes a "skill" — a structured markdown file capturing the procedure, pitfalls, and verification steps — to `~/.hermes/skills/`. Next time it loads that skill and executes faster. Skills are human-readable and editable.
3. **Always-on execution.** Runs on a server 24/7; connects to Telegram, Discord, Slack, WhatsApp, Signal, Email, and 15+ platforms through one gateway. Built-in cron accepts natural-language schedules.

### vs OpenClaw

The post frames Hermes as the successor to **OpenClaw** (formerly Clawdbot, then Moltbot — the breakout early-2026 agent, 145k+ GitHub stars). Two claimed advantages: (1) a **closed learning loop** — OpenClaw skills are static and manually installed; Hermes reviews its work every ~15 tool calls and writes reusable skills automatically; (2) **bounded curated memory** — OpenClaw needs third-party add-ons (QMD) for cross-session memory; Hermes ships bounded memory with on-demand full-text retrieval and context compression. The post concedes OpenClaw still has broader platform coverage (50+ integrations). See @concepts/openclaw-security-taxonomy.md for the security-posture comparison.

**K69 addendum (Post 11, @NainsiDwiv50980):** reframes persistent memory as the primary differentiator for long-running agent workflows — aligns with the `MEMORY.md` / `USER.md` model above; no new repo mechanics beyond existing Hermes docs [TENTATIVE — promotional post].

### Install (per the post)

One-line installer: `curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash`, choose a model (Anthropic Claude or OpenAI Codex recommended), run `hermes gateway setup` to bind a messaging platform, then `hermes`. The post deploys it on a Hetzner VPS for 24/7 operation.

### Cemini posture

- **Not an adoption candidate for the trading stack.** Cemini already has its own agent orchestration (Conductor / librarian; LangGraph). Hermes Agent is a *consumer-grade personal-agent runtime* — a parallel implementation of capability Cemini already has, which the Phase-0 pattern says not to adopt.
- **Reference value is real.** The self-improving-skill loop (write a markdown skill after N tool calls, reload it next time) and the `MEMORY.md` / `USER.md` frozen-snapshot pattern are clean ideas worth comparing against Cemini's own memory/skill handling — and against the related @entities/tools/hermes-lcm.md context engine.
- **Security note.** The post's deployment hands an agent a funded Polygon wallet's private key and runs unattended trading via copy-pasted prompts. That is a high-trust configuration; flagged here, not endorsed. The standard install also pipes a remote script straight into `bash`.
- **Verified, mature, MIT.** The K52 source was one creator post, but the project itself is confirmed (see above): `NousResearch/hermes-agent`, MIT, ~172k★ (May 2026), actively maintained. The "not a Cemini adoption" verdict is therefore a *fit* decision (it duplicates Conductor), not a credibility one — and if Cemini's orchestration ever needs replacing, Hermes Agent is a serious, license-clean reference rather than a speculative one.

### K64 community catalog (@Shruti_0810) [TENTATIVE]

Post 2 groups **276+** claimed production uses: dev swarms (“zero human company”), messaging + device integrations, business automation, autonomous content pipelines, research briefings, K8s enterprise. Framing: shift from “AI answers questions” (2024) → “AI helps work” (2025) → **persistent autonomous workers** (2026). No new technical artifact beyond reinforcing Hermes as **infrastructure-layer** competitor/reference to Conductor — compare @concepts/openclaw-security-taxonomy.md.

### K78 forensics + x402 addendum (2026-05-29)

Posts 3 + 5 document **skill-bundled on-chain forensics** (~$0.10/run): DexScreener → Nansen via x402 → RPC → Tokenomist → Cookie MCP. See @concepts/hermes-onchain-forensics-pipeline.md. Still reference-only for prod (Conductor owns orchestration).

## Snippets

> "Hermes Agent remembers what it learns and gets more capable over time, with a multi-level memory system and persistent dedicated machine access." [Source: posts-2026-05-18.docx — Post 5, @0xMovez, quoting @NousResearch, Feb 25]

> "It stores two core memory files: MEMORY.md (environment facts, conventions, experiences) and USER.md (your preferences, communication style, expectations). These are loaded as a frozen snapshot into every new session." [Source: posts-2026-05-18.docx — Post 5, @0xMovez]
