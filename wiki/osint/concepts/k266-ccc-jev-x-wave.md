---
title: K266 CCC Jev X Wave (Sep 2026)
type: concept
tags: [ccc, k266, jev, harness, x-twitter]
keywords: [Jev, System One, AutoMode, skill classify, TypeSafeClassifier, langchain-typesafe]
related:
  - concepts/k265-ccc-jev-wave.md
  - concepts/k266-ood-stub-wave.md
  - sources/x-article-sydneyrunkle-harness-jev-2026-09-19.md
  - sources/x-article-0xmovez-jev-engineering-2026-09-19.md
  - sources/x-post-parcadei-jev-skill-classify-2026-09-19.md
  - sources/x-article-shreyanshpatni-agent-harness-2026-09-19.md
  - entities/tools/jev-mcp.md
  - entities/tools/openjev.md
  - entities/tools/langchain-typesafe.md
  - concepts/k266-seo-x-voice-wave.md
maturity: draft
created: 2026-09-19
updated: 2026-09-19
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k266-seo-x-voice-wave.md
- @concepts/k265-ccc-jev-wave.md
- @concepts/k266-ood-stub-wave.md
- @sources/x-article-sydneyrunkle-harness-jev-2026-09-19.md
- @sources/x-article-0xmovez-jev-engineering-2026-09-19.md
- @sources/x-post-parcadei-jev-skill-classify-2026-09-19.md
- @sources/x-article-shreyanshpatni-agent-harness-2026-09-19.md
- @entities/tools/jev-mcp.md
- @entities/tools/openjev.md
- @entities/tools/langchain-typesafe.md

## Raw Concept

K266 cluster hub. Dual-ID **OSINT K266**. Four X items on Jev as a decision layer. Parent pulled the extracts (X MCP article `plain_text`); this wave does not re-pull.

## Narrative

X-side material for the Jev decision layer. Four items, one of them the best-performing Jev long-form so far.

| Item | Handle | Likes | Bookmarks | Impressions | Kind |
|------|--------|-------|-----------|-------------|------|
| Building a Harness with Jev | @sydneyrunkle | 4,141 | 9,390 | 1,221,679 | Article — **best Jev long-form** |
| Jev Engineering 10 steps | @0xMovez | 285 | 500 | 49,777 | Article |
| JEV TIP 001 skill classify | @parcadei | 421 | 416 | 32,472 | Short tip |
| Custom Agent Harness | @shreyanshpatni_ | 52 | 89 | 5,665 | Article — little Jev |

Metrics from X MCP 2026-09-19. Do not invent further numbers.

**The convergent pattern.** All four describe the same move in different places: a cheap classifier decides, the main model generates. @sydneyrunkle puts it at the **model boundary** (routing middleware) and the **tool boundary** (`AutoModeMiddleware` blocks risky tool calls before execution). @parcadei puts it at the **skill boundary** (classify the task against skill names plus short descriptions, inject the selected skill before the prompt reaches the main model). @0xMovez states the rule directly: "If the operation creates text, it stays with the LLM. If it picks an option, scores a value, or answers yes/no, it goes to Jev."

**Question types** are consistent with the existing record: **Choice**, **Score**, **Noul** (yes/no). Every question in a request is evaluated in parallel; adding questions barely changes response time and costs only the extra question tokens. Questions cannot read each other's answers.

**Cost.** Jev 1.13 at **$0.042 per MTok input, no output-token charge**. 10,000 decisions at 1,000 billed input tokens each = $0.42. Reported field numbers: Browser Use flight search **$0.0039 / ~7s** (finds flights, does not book); Hassan **1,018 papers for $0.08** at 256ms median; Riley Brown **500 emails for 3.5¢**; Volkov **1 second to compact ~1M → 86K** tokens. All single-source or vendor-reported.

**Claim hygiene.** **200x faster / 400x cheaper** are TypeSafe vendor claims repeated by both articles, not Cemini measurements. The "harness is the difference between 78% and 42% on the same model" line is the @0xMovez author's claim with no source. Vercel fx's **5–18x faster safety classification than GPT-5.6-Luna** compares the classifier, not a full agent run.

**Cemini reading.** **FILE. 0 product Integrate GO. Do not swap `/route`.** Live laptop path remains **jev-mcp** TypeSafe. Two candidate HITL experiments, neither approved to build: an **AutoMode-style claim-ledger / tool-call gate** (GuruWatcher), and a **skill-name classifier before prompt injection** (CCC). Compaction is already K264 (`fast-jev-compaction`) — do not re-open. **No unattended browser-use. No live trading agent.** Do not copy LangChain or Jev skills into `~/.cursor/skills`.
