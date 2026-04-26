---
title: "Architectural Forensic Analysis: Accelerating the Cemini Financial Suite"
type: source
tags: [docx, rl-marl, llm-agents, portfolio-strategy, options-derivatives, cemini-internal, kelly, bayesian, devil-s-advocate, mcp, spiffe, skill-topology]
clusters: [rl-marl, llm-agents, portfolio-strategy, options-derivatives, cemini-internal]
related:
  - concepts/rl-marl-research.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @concepts/rl-marl-research.md — cluster hub for RL/MARL research in the Cemini corpus

## Raw Concept

- **Original title**: Architectural Forensic Analysis: Accelerating the Cemini Financial Suite
- **Author(s)**: Cemini internal research (no attributed author)
- **Type**: DOCX (internal architectural audit)
- **Location**: research for cemini/github analysis.docx
- **Length**: ~4959 words, 128 paragraphs
- **Retrieved**: 2026-04-23
- **Read status**: read-skim
- **Primary cluster**: cemini-internal (misclustered — partition assigned `options-derivatives` home, but document is a dev-tool / architecture audit, see flags)
- **All clusters**: rl-marl, llm-agents, portfolio-strategy, options-derivatives, cemini-internal

## Narrative

"Light Year" forensic analysis of the Cemini Financial Suite against its v5.0 roadmap, identifying five architectural discoveries plus a systematic breakdown of ~12 external GitHub repositories, mapping each to a concrete Cemini roadmap step. The document is positioned as IP-valuation-oriented and assumes an acquiring-firm audit mindset.

**Five "Light Year" discoveries:**

1. **Sequential Bayesian-Kelly Engine (§2.1)** — Replace static risk_engine.py thresholds and naive Fractional Kelly with continuous Bayesian updating of win-probability p across the Redis `intel:*` bus, recomputing Kelly fraction at every information event. Enforces half-Kelly (f* = 0.5) to trade ~42% of theoretical growth for ~93% variance reduction. Explicit architectural claim: "the edge is in p̂, not the odds."
2. **PCA + fat-tail risk (§2.2)** — First 5 eigenvectors explain ~70% of variance (signal); remainder is noise to be filtered before agent ingestion. Replace normal-distribution CVaR with Student-t df=4. For Step 30 logit-space contract pricing: GBM + Itô's lemma; for Step 9 options, BSM + Monte Carlo ≥500k paths.
3. **Devil's Advocate Refutation Matrix (§2.3)** — Extracted from sc-auditor's "Map-Hunt-Attack" methodology. The Trader/Arbiter agent is reprogrammed with a strict refutation matrix: Bull Advocate's entry signal must be algorithmically attacked by Bear Advocate + Risk Assessor before execution. Enforces Pydantic v2 contract validation across `intel:*` bus.
4. **Zero-Trust Vibe Coding / ToxicSkills mitigation (§2.4)** — mcp-scan + claudit for MCP-server behavioral scanning (covert tool invocations, resource theft, conversation hijacking); SPIFFE JIT ephemeral identities replacing static env-var secrets; aggressive prompt-injection scanning of third-party SKILL.md files.
5. **Command → Agent → Skill topology + Node.js hooks (§2.5)** — Formal separation: Command = entry, Agent = specialized data fetcher, Skill = modular output generator. PreCompact/Stop lifecycle hooks persist session state before context-window compaction → zero momentum loss across multi-day refactors.

**Repo breakdown (selective):** rohitg00/pro-workflow (SQLite+FTS5 Cmd→Agent→Skill, 18-event hook lifecycle, git worktrees → maps to Step 11 shadow testing + Step 29 ChromaDB precursor); googleworkspace/cli (two-phase parsing, Model Armor → Step 27 MCP server); wshobson/commands (dynamic agent routing → anomaly handling in Step 26); peteromallet/desloppify (anti-gaming code-quality loop → IP-valuation prerequisite); tinyfish-io/tinyfish-cookbook (HTTP-API web-agent recipes → alt-data fallback); njbrake/agent-of-empires (tmux + Rust parallel session manager → Step 22/28/32 concurrent refactor); AlexsJones/llmfit (hardware-aware model-fit scoring → Step 31 OpenFang rightsizing on Hetzner); marchev/claudit (supply-chain scanning → Step 20 skill-vetting); shanraisshan/claude-code-best-practice (Progressive Disclosure → Step 26 context hygiene); anthropics/skills skill-creator (pass@k eval, "pushy" YAML → Step 21 Cemini skill packaging); shareAI-lab/learn-claude-code (file-based JSONL mailboxes + Autonomous Claiming → decouples Step 7 MAPPO synchronous orchestrator); ethskills.com (frontend safety rules → Step 3 dashboard).

Relevant to Cemini as a compact cross-reference of dev-infrastructure patterns explicitly mapped to roadmap step numbers. Honest limits: document is promotional in register ("light year", "weaponize", "leapfrog"); cost/effort savings are asserted not measured; the "42% growth / 93% variance" Kelly numbers are stated as practitioner consensus without citation; five of the twelve repo mappings are not verifiable against Cemini's actual roadmap without cross-referencing the primary v5.0 spec.

## Key findings

- **FLAG: MISCLUSTERED** — home cluster `options-derivatives` per partition is wrong; this is an architectural/dev-tools audit, not an options paper. Correct home is `cemini-internal` or `infrastructure`.
- Sequential Bayesian-Kelly: continuous posterior update on Redis `intel:*` events → half-Kelly position sizing; explicit claim that edge lives in p̂.
- PCA signal extraction: first 5 eigenvectors ≈ 70% variance; prescribe Student-t(df=4) over normal for CVaR.
- Devil's Advocate Protocol (Map-Hunt-Attack from sc-auditor) replaces CIO-debate linear path with mandatory refutation workflow in Step 7 MAPPO.
- Zero-Trust posture: mcp-scan + claudit + SPIFFE JIT identities replacing static env secrets; mandatory SKILL.md prompt-injection scanning.
- Command→Agent→Skill topology with PreCompact/Stop Node.js hooks for context-rot mitigation in long refactors.
- Concrete repo-to-step mappings: git worktrees → Step 11; FTS5 SQLite → Step 29 precursor; JSONL mailbox mailing → Step 7 decoupling; llmfit → Step 31 OpenFang memory fit.
- Explicit IP-sale framing: desloppify anti-gaming loop is positioned as mandatory pre-acquisition code hygiene.

## Snippets

- **§2.1 (Bayesian-Kelly)** — "the trading edge is located exclusively in the accurate estimation of [p], not in the market odds… sacrificing approximately forty-two percent of theoretical maximum growth to achieve a ninety-three percent reduction in portfolio variance."
- **§2.2 (fat tails)** — "Reality is modeled not by a standard normal curve, but by a Student-t distribution with four degrees of freedom, where market crashes and extreme systemic shocks reside precisely in the heavy tails."
- **§2.3 (Devil's Advocate)** — "the Arbiter does not passively evaluate the signal's strength. Instead, it executes the Devil's Advocate Protocol, algorithmically commanding the Bear Advocate and Risk Assessor to attack and falsify the entry hypothesis."
- **§2.4 (Zero-Trust)** — "transition entirely from static environment variables to Just-In-Time (JIT) provisioning utilizing the SPIFFE standard for ephemeral, task-scoped verifiable identity documents."
- **§2.5 (Hooks)** — "deploy PreCompact and Stop lifecycle hooks. These hooks automatically save critical session state… immediately before the context window is compacted or the session terminates."
- **pro-workflow mapping** — "The deployment of parallel git worktrees directly automates and accelerates Step 11 (Shadow Testing)."
- **learn-claude-code mapping** — "Autonomous Claiming, where decentralized teammates asynchronously scan shared, file-based JSONL mailboxes to claim tasks… entirely eliminates the bottleneck of a single, synchronous orchestrator in the Step 7 reinforcement learning loop."
