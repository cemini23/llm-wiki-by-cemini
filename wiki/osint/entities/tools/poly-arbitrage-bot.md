---
title: zostaff/poly-arbitrage-bot — Polymarket↔Kalshi cross-exchange arbitrage bot
type: entity
tags: [entity, tool, polymarket, kalshi, arbitrage, cross-venue, prediction-markets, reference, k53]
keywords: [poly-arbitrage-bot, zostaff, cross-exchange-arbitrage, polymarket-kalshi, py-clob-client, eip-712, rsa-pss, paper-trading, sqlite-fill-log, mit-license]
related:
  - sources/multi-wiki-link-eval-41url-2026-05-18.md
  - concepts/cross-venue-arbitrage-pattern.md
maturity: draft
created: 2026-05-18
updated: 2026-05-18
---

## Relations

- @sources/multi-wiki-link-eval-41url-2026-05-18.md — K53 eval URL 1; the source that surfaced this bot (and got its license wrong)
- @concepts/cross-venue-arbitrage-pattern.md — this bot is a concrete implementation of that pattern (Polymarket↔Kalshi arb loop)

## Raw Concept

What prompted this page: K53 multi-wiki tool-eval URL 1. The eval Rejected it as "NO LICENSE FOUND" — a verdict **corrected here**: a GitHub API check (2026-05-18) confirms the repo is **MIT-licensed**. The page records the corrected verdict and the tool's relevance to the cross-venue arbitrage workstream.

## Narrative

`zostaff/poly-arbitrage-bot` — a **cross-exchange arbitrage bot for Polymarket and Kalshi**. Verified 2026-05-18 (GitHub API): **MIT**, ~20★, pushed 2026-05-06, not archived. (Author `zostaff` is also the author of the K52 hedge-fund-OSS X post — see @sources/x-posts-quant-oss-polymarket-bots-2026-05.md.)

Documented architecture (per the eval):
- High-fidelity cross-exchange arbitrage calculations exploiting Polymarket↔Kalshi pricing inefficiencies.
- `py-clob-client` + **EIP-712** order signing (Polymarket) and **RSA-PSS** authentication (Kalshi).
- **SQLite-backed simulated-fill paper-trading** subsystem — a clean pattern, portable to the Cemini PostgreSQL backtesting pipeline.
- Explicit **sanity caps** on max position size and **gated live-trading environment variables** — an institutional risk posture.

### Verdict — corrected

The eval Rejected this on "NO LICENSE FOUND." That finding is **wrong** — the repo is MIT (verified). The reject is therefore retracted. Corrected verdict: **Reference / Steal-from** — it is a small (~20★) but on-target, license-clean implementation of @concepts/cross-venue-arbitrage-pattern.md. Cemini should not adopt a 20-star bot wholesale, but the cross-exchange arb calculation, the EIP-712/RSA-PSS dual-venue auth handling, and the SQLite simulated-fill paper-trading subsystem are concrete reference patterns worth reading before building Cemini's own cross-venue arb loop.

This is a K53 instance of the eval's systematic "retrieval-gap reported as no-license" error — see @sources/multi-wiki-link-eval-41url-2026-05-18.md Dead Ends and @concepts/cemini-license-posture.md.

## Snippets

> "The underlying logic of this repository provides high-fidelity, cross-exchange arbitrage calculations designed to exploit pricing inefficiencies between Polymarket and Kalshi. The application leverages the py-clob-client paired with EIP-712 order signing mechanisms and Kalshi RSA-PSS authentication." [Source: Multi-Wiki Tool Evaluation.docx — URL 1]
