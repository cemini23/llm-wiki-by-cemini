---
title: "K291 — osint wave (2026-10-14)"
type: concept
tags: [wave, k291, ingest, hub]
keywords: [K291, ingest wave, arxiv, desk notes, feeds]
related:
  - sources/arxiv-gromm-risk-neutral-option-market-2610.16732-2026-10-14.md
  - sources/arxiv-diffnash-diffusion-equilibrium-2610.15932-2026-10-14.md
  - sources/arxiv-embodiedevo-self-improving-coding-agents-2610.18867-2026-10-14.md
  - sources/arxiv-autoagent0-agentic-runtime-closed-loop-2610.18866-2026-10-14.md
  - sources/arxiv-longhisdoc-chinese-historical-documents-2610.14531-2026-10-14.md
  - sources/arxiv-ddvr-net-historical-document-recognition-2610.16956-2026-10-14.md
  - sources/arxiv-plaat-learning-to-play-rl-and-games-2610.17391-2026-10-14.md
  - sources/gs-positioning-2026-10-12-week-41.md
  - sources/k291-osint-feeds-2026-10-14.md
  - sources/eval-url-multi-wiki-link-2026-10-14.md
maturity: draft
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @sources/arxiv-gromm-risk-neutral-option-market-2610.16732-2026-10-14.md — arbitrage-free S&P option surface model, >95% inside bid/ask
- @sources/arxiv-diffnash-diffusion-equilibrium-2610.15932-2026-10-14.md — diffusion policies for continuous-action Nash, gap −35.6% / −24.7%
- @sources/arxiv-embodiedevo-self-improving-coding-agents-2610.18867-2026-10-14.md — Skills and Lessons; 53% lower execution cost
- @sources/arxiv-autoagent0-agentic-runtime-closed-loop-2610.18866-2026-10-14.md — propose-verify-recover runtime around an existing expert
- @sources/arxiv-longhisdoc-chinese-historical-documents-2610.14531-2026-10-14.md — full-book benchmark; best LVLM 62.9%
- @sources/arxiv-ddvr-net-historical-document-recognition-2610.16956-2026-10-14.md — visibility gate over restoration
- @sources/arxiv-plaat-learning-to-play-rl-and-games-2610.17391-2026-10-14.md — book stub, no content
- @sources/gs-positioning-2026-10-12-week-41.md — CTA long $43.5bn, down from $125bn a month ago
- @sources/k291-osint-feeds-2026-10-14.md — Substack and newsletter batch
- @sources/eval-url-multi-wiki-link-2026-10-14.md — 20-URL tool eval; docx licence wrong or incomplete on 5 of 17

## Raw Concept

The question this page answers: **what did the K291 osint inbox contain, and which items matter?**

Ingested 2026-10-14. This hub exists so each source page needs one link instead of many, and so the wave can be reviewed as a set.

## Narrative

**Wave composition:** 8 arXiv items, 2 Goldman Sachs desk notes, 11 Substack and newsletter items. One arXiv item (`2610.18802`, Brownian Fleming–Viot) was **skipped** as pure probability theory with no Cemini application.

### What matters

**GROMM is the desk-relevant paper.** An arbitrage-free European option market model where the **option surface is the state variable**, not an output of a price process. Fits >95% of S&P index option quotes inside bid/ask over Jan 2022 – Aug 2025, with P and Q training and new BHW no-arbitrage tests.

**EmbodiedEvo carries the agent-harness lesson.** Skills and Lessons distilled from a single scene give *comparable* task performance at **53% lower execution cost** than raw interaction history — a context-budget result. Experience also transfers: a stronger model's lessons lifted weaker executors by +8.86 and +5.50 points.

**AutoAgent0 is the same architecture as this wiki's tool-call gate.** An LLM or expert proposes; a deterministic verifier admits or refuses *before* execution; a recovery loop runs when the proposal is unreliable. Here the artifact is a trajectory, not a tool call.

**DiffNash supplies a transferable technique** — training a diffusion policy when the target distribution cannot be sampled directly, via a reweighted score-matching objective with an ELBO-difference importance proxy.

**Both document-AI papers converge on a gate.** LongHisDoc includes an *unanswerable* QA class; DDVR-Net adds a per-character *visibility gate* so restoration is not applied uniformly. Both refuse to force an answer where the evidence is absent.

### What does not matter

- **Plaat's book** — front matter only, no extractable content.
- **Fleming–Viot** — skipped, no application.

### Boundary

No install, no scrape, no trade, no xsp/pm scp, no `/route` swap.

## Snippets

> "Compared with raw interaction history, Skills and Lessons achieve comparable task performance at 53.0% lower execution cost." [Source: arxiv-2610.18867 p.1]

> "We address the challenge by treating closed-loop driving safety as a test-time execution problem." [Source: arxiv-2610.18866 p.1]

> "the model's initial state fits within bid/ask for more than 95% of relevant market option prices." [Source: arxiv-2610.16732 p.1]

## Dead Ends

- **Fleming–Viot** (`2610.18802`) — pure probability theory in bounded domains. No Cemini application; not filed as a source page.
