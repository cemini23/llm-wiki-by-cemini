---
title: eugeniughelbur/obsidian-second-brain — 31 Commands + 4 Cron Agents (Python+Shell, MIT)
type: source
tags: [llm-tooling, obsidian, claude-code, second-brain, cron-agents, perplexity-sonar, grok-api, whisper-api, workflow-adopt, ip-sale-clean]
keywords: [obsidian-second-brain, eugeniughelbur, claude-code-skill, vault-first-research, scheduled-agents, emerge-command, nightly-consolidation, perplexity-sonar-pro, grok-api, whisper-api, youtube-data-api, bootstrap-vault]
related:
  - sources/gemini-dr-link-eval-2026-04-28.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - sources/kepano-obsidian-skills.md
  - sources/atomicmemory-llm-wiki-compiler.md
maturity: validated
created: 2026-04-28
updated: 2026-04-28
clusters: [llm-agents, librarian-tooling]
---

## Relations

- @sources/gemini-dr-link-eval-2026-04-28.md — parent canonical Gemini DR source
- @concepts/wiki-tooling-evaluation.md — Wave 2 evaluation parent; the autonomous-rewriting feature collides with the llm-wiki-compiler's static-compiler philosophy on the librarian server (Wave 2 marks this Wiki-fit as ⚠️)
- @concepts/ip-sale-readiness.md — MIT license clears IP-sale checks (Exa-verified 2026-04-28: 402 ★)
- @sources/kepano-obsidian-skills.md — sibling Workflow-Adopt; both target the laptop Obsidian + Claude Code loop. Use kepano's skills for syntax + this for the autonomous-curation loop
- @sources/atomicmemory-llm-wiki-compiler.md — relevant tension: this tool autonomously rewrites Markdown; llm-wiki-compiler treats Markdown as canonical input. Use this on laptop only — never on the librarian server's synced copy

## Raw Concept

- **URL**: https://github.com/eugeniughelbur/obsidian-second-brain
- **Type**: Open-source repository / Claude Code skill
- **License**: MIT (Exa-verified 2026-04-28)
- **Stars / Forks (Exa-verified 2026-04-28)**: 402 ★ / 48 forks / 0 open issues
- **Stack**: Python 84.1%, Shell 14.1%, HTML 1.8%
- **Org**: eugeniughelbur (sole-contributor project; bus factor concern)
- **Created**: 2026-03-24; **Last push**: 2026-04-27; **Latest release**: v0.6.0 (2026-04-26)
- **Releases**: 10 published in ~5 weeks — high velocity
- **Topics**: ai-agent, ai-agents, ai-automation, ai-research, ai-tools, anthropic, claude, claude-ai, claude-code, claude-code-skill, claude-skill, knowledge-management, llm-tools, note-taking, obsidian, obsidian-md, obsidian-plugin, obsidian-skill, personal-knowledge-management, second-brain
- **Homepage**: https://github.com/eugeniughelbur/obsidian-second-brain/releases/latest

## Narrative

### What it does
A programmatic bridge connecting Claude Code CLI directly with local Obsidian Markdown vaults. Injects 31 custom commands and instantiates 4 cron-based automated background agents (Morning, Nightly, Weekly, Health). Operates discrete external Python scripts that query:
- **Grok API** — contextual Twitter/X data
- **Perplexity Sonar API** — cited web research
- **Whisper API** — local audio transcriptions
- **YouTube Data API v3** — video metadata

Output is piped directly into the vault as formatted Markdown notes. **Core operational directive**: enables an AI agent to autonomously rewrite, synthesize, and merge duplicate or contradictory knowledge base entries during nightly consolidation routines.

### Why Adopt-for-Workflow

This tool directly augments the laptop's Obsidian + Claude Code curation methodology. Reasoning:

1. **Vault-first design** — operates on the canonical Obsidian vault directly, not via an intermediate index. Matches the workspace pattern.
2. **Perplexity Sonar Pro bridge** — eliminates manual context-gathering during research curation. The `/emerge` command identifies hidden cross-links between ML papers and financial models — exactly the kind of synthesis the workspace librarian role demands.
3. **Nightly consolidation cron** — companion to the existing `wiki_lint.py`. Where lint enforces structural correctness, the consolidation cron synthesizes content.
4. **MIT license** — clears IP-sale-readiness.
5. **Python + Shell** — matches the workspace's primary development languages. No JS runtime needed for the agent itself (cloud APIs handle inference).

### Where it falls short / requires extreme care

**Wiki / librarian server fit: ⚠️ (Gemini's caveat)** — the dedicated CPX21 librarian server assumes the laptop provides canonical, human-curated truth. Allowing background agents to autonomously alter the synced Markdown on the server invites catastrophic state desynchronisation. **Action**: only run on the laptop, never on the librarian server. Configure cron schedules to operate ONLY on `~/Desktop/OSINT WORKSPACE/` and not on any rsync'd server-side copy.

**Cemini production stack fit: ❌** — domain mismatch (knowledge management vs algorithmic trading).

### Critical risks (from Gemini's evaluation + workspace constraints)

1. **API cost proliferation** — mandates Grok + Perplexity + Whisper + YouTube API keys. Separate, decentralised billing logic from the primary DeepSeek infrastructure. Estimate monthly spend before adopting; consider gating on user-provided budget envelope.
2. **Data destruction risk** — autonomous agent with root permission to rewrite/consolidate proprietary Markdown carries severe data-loss risk if it misjudges a "duplicate" merge or "contradiction" resolution. **Mandatory mitigation**: vaults must be rigorously git-tracked BEFORE every agent execution. The workspace already has `wiki/` git-tracked; consolidation runs must be atomic and reversible via `git reset`.
3. **Concurrent edit conflict** [NEEDS VERIFICATION] — Gemini flagged: "Intensive verification is required to understand exactly how the internal context engine handles conflict resolution if a file is being actively edited by the human user concurrently during a background agent consolidation operation." Test by editing a wiki page during a nightly cron run and observing what happens.
4. **Sole-contributor project** (eugeniughelbur) — bus factor concern. 10 releases in 5 weeks indicates engaged maintenance, but track quarterly.

### Integration vector (laptop only)

```
1. Clone the repo to laptop
2. Run bootstrap_vault.py to install framework into ~/Desktop/OSINT WORKSPACE/.claude/
3. Provision API keys for Grok / Perplexity / Whisper / YouTube → .env
4. Configure cron schedules:
   - Morning agent: 0 8 * * * (review yesterday's research; queue today's)
   - Nightly agent: 0 22 * * * (consolidate, lint, propose merges — review-required)
   - Weekly agent: 0 9 * * 0 (cross-link gaps, emerge new concept stubs)
   - Health agent: 0 0 * * * (orphan detection, bidir-gap detection — pairs with wiki_lint.py)
5. Configure agents to operate in /tmp/proposed-changes/ first (NOT directly on wiki/)
6. Require human review (git diff + accept/reject) before merging proposals into wiki/
```

The "review-required" mode is the workspace's required adaptation — the upstream tool defaults to autonomous merge; this is too risky for a 380-page hand-curated wiki. Patch the cron scripts to write proposals to `/tmp/` and require manual `git apply`.

## Snippets

> "Claude Code skill for Obsidian. Turn your vault into a living AI-first second brain. 31 commands, vault-first research, scheduled agents." [Source: GitHub repo description, retrieved via Exa crawling_exa 2026-04-28]

> "Adopt for Workflow. The built-in commands—specifically those seamlessly bridging Perplexity Sonar Pro to execute cited web research—eliminate tedious manual context-gathering steps. The 'Nightly consolidation' feature acts as an incredibly powerful companion to the existing wiki_lint.py script." [Source: Gemini DR report, URL 19]

> "Data Destruction is a critical risk; granting an autonomous agent root permission to rewrite and consolidate proprietary Markdown files without a human-in-the-loop review carries a severe risk of catastrophic data loss. The vaults must be rigorously git-tracked prior to agent execution." [Source: Gemini DR report, URL 19 — Risks & caveats]
