---
title: "Latent Space AINews 2026-11-25 — Gemini 4 Neon, MCP turns two, harness comparison"
type: source
related:
  - entities/tools/claude-code.md
  - concepts/frontier-model-release-cadence.md
  - concepts/model-vs-harness-performance-variance.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | [AINews] Gemini 4 Neon marks GDM's full return as a Frontier Lab |
| Author | Latent Space (AINews) |
| Type | Newsletter (RSS, free tier) |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/ccc/newsletter-rss-latent-space-2026-11-25-ainews-gemini-4-neon-marks-gdms-full-return-as-a.mdnewsletter-rss-latent-space-2026-11-25-ainews-gemini-4-neon-marks-gdms-full-return-as-a.md
| Retrieved | 2026-11-25 |
| File | `newsletter-rss-latent-space-2026-11-25-ainews-gemini-4-neon-marks-gdms-full-return-as-a.md` |
| URL | https://latent.space/p/ainews-gemini-4-neon-marks-gdm-s-full-return-as-a-frontier-lab/ |
| Read status | read |

## Narrative

An AI-news digest. Four items bear on harness work.

**MCP turns two.** MCP Tasks is now generally available for long-running server operations. Skills over MCP is shipping. File uploads are coming. Claude now has more than 10,000 connectors. This changes what a long tool call can look like: a server can accept a task and return later, without holding the session.

**Artificial Analysis harness comparison.** The same model scores very differently across harnesses. GPT-6 Luna scores best in Codex at 26, where GLM-5.3-Flash ranks last. GLM scores best in Claude Code at 39. Cost varies more than score: $0.11 to $0.62 per task for Luna. GLM reasons in terse fragments inside Codex, producing 52k output tokens against 97k to 202k elsewhere. This is a direct counterexample to a flat "harness does not matter" reading.

**Agent swarms.** Vals Swarm Speed finds four-agent teams only slightly faster than a single agent, at about three times the tokens.

**Harness-adapted models.** Hugging Face released a reusable harness-adaptation recipe. Qwen3.8-27B-think-pi-adapted keeps scores flat with 38% fewer output tokens. RL on short tasks generalises to tasks 2 to 64 times longer (MIT CSAIL).

**Why it matters.** The harness comparison item gives a within-model spread of about 13 points on one benchmark, against the near-flat harness means that ShellBench reports for everyday tasks. Both are single-source. The difference is the task class: coding and tool-heavy work amplify harness effects. [TENTATIVE]

## Snippets

> "No universal best harness: GPT-6 Luna scores best in Codex (26), where GLM-5.3-Flash ranks last. GLM scores best in Claude Code (39)." [Source: `newsletter-rss-latent-space-2026-11-25-ainews-gemini-4-neon-marks-gdms-full-return-as-a.md`, retrieved 2026-11-25]
