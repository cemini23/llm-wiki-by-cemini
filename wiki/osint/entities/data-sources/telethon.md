---
title: Telethon
type: entity
tags: [library, data-source, alt-data, messaging]
keywords: []
related:
  - sources/3-19-alternative-data-for-prediction-markets-research.md
  - sources/3-19-telegram-discord-research.md
  - entities/frameworks/finbert.md
  - entities/infrastructure/deepseek-r1-14b.md
  - concepts/publishers-exclusion-apa.md
  - concepts/ip-sale-readiness.md
  - concepts/scatter-gather-topology.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @sources/3-19-alternative-data-for-prediction-markets-research.md
- @sources/3-19-telegram-discord-research.md — primary source; deep-read 2026-04-26 (K3)
- @entities/frameworks/finbert.md — sibling alt-data scoring lib that the previous (now-retracted) narrative on this page incorrectly claimed was wired to Telethon
- @entities/infrastructure/deepseek-r1-14b.md — sibling page that captures the parallel local-LLM retraction in the same Cemini-internal blueprint
- @concepts/publishers-exclusion-apa.md
- @concepts/ip-sale-readiness.md — Telegram alt-data is on the deal-killer ledger (publisher's-exclusion candidate); IP-sale framing is what makes the prescribed/deployed gap matter
- @concepts/scatter-gather-topology.md — sibling K-style reframe (prescribed-vs-deployed reset on a Cemini-internal blueprint, same source family)

## Raw Concept

`[RESOLVED — 2026-04-26 K3 deep-read]` — This page previously claimed *"Cemini uses Telethon to subscribe to curated crypto-signal, macro-news, and sports/politics-commentary channels whose message streams are tagged, de-duplicated, and scored by FinBERT before being written to TimescaleDB as alt-data features."* That synthesis collapsed two distinct things into one false assertion:

1. **The library is real.** Telethon is the optimal Python MTProto library for the Telegram ingester that the source @sources/3-19-telegram-discord-research.md prescribes for Cemini. Its technical merits (asynchronous, comprehensive MTProto coverage, ~708 GitHub contributions, deep edge-case docs) are correctly captured.
2. **The Cemini deployment is not.** Ground-truth `ssh root@hetzner` probe on 2026-04-26 returned: zero containers matching `telegram|telethon|social|signal` (out of 40 running); zero references to `telethon` in any `requirements.txt`, `pyproject.toml`, `Dockerfile`, or `docker-compose*.yml` under `/opt/cemini/`; zero `cemini:streams:social_intel` Redis-channel references in any service code; zero `vader|spacy|finbert` references in deps. **The Cemini Telegram ingester does not exist.**

The page is reframed as the **library reference + IP-sale-readiness build spec**, not as documentation of a deployed pipeline. See @sources/3-19-telegram-discord-research.md "Prescribed-vs-deployed gap" section for the full evidence trail and @concepts/scatter-gather-topology.md for the sibling reframe on the LangGraph scatter-gather concept page (same Cemini-internal-blueprint pattern).

## Narrative

### What Telethon actually is
Telethon is the dominant Python implementation of the **MTProto API**, Telegram's binary cryptographic protocol — the canonical interface (versus the more limited HTTP Bot API) for any application that needs to read messages from third-party public channels using a standard user account rather than an invited Bot account. Asynchronous, supports both user and bot accounts, handles entity resolution, session persistence, and the full surface of Telegram functionality.

For passive monitoring of crypto / macro / signals channels (the use case Cemini's IP-sale-blueprint targets), Telethon is the right tool. The Bot API can't see uninvited public channels at all; Pyrogram is a viable second-place but smaller community (~556 GitHub contributions vs Telethon's ~708, per @sources/3-19-telegram-discord-research.md para 75-79).

### Prescribed Cemini deployment (build spec — NOT shipped)
Per @sources/3-19-telegram-discord-research.md:

- **Account model**: single user account joining ≤ 200 channels (hard Telegram cap; source mandates **selectivity within 200**, never rotation across accounts — that's the "swarms" violation pattern Telegram bans).
- **Memory fix**: `client.session.save_entities = False` at initialization is non-optional. Default behavior caches all encountered user/chat entities into the session SQLite + memory; on a high-volume passive stream this is unbounded growth (Telethon Issue #3235) that OOM-kills the container after a few days. With `save_entities=False`, the container holds at ~100-150 MB.
- **NLP pipeline** (the source's actual prescription): deterministic Regex → spaCy `en_core_web_sm` for intent verification → VADER for sentiment scoring. **Explicitly NOT FinBERT or any transformer-class model** — source rejects them as too CPU-expensive for real-time stream processing (para 123). The FinBERT scoring claim in the prior version of this page was a wiki fabrication contradicting the source.
- **TOS isolation** (the load-bearing legal constraint): Telegram TOS §1.5 prohibits using platform data to "train, fine-tune or otherwise engage in the development, enhancement or deployment of artificial intelligence, machine learning models." The architecture must extract structured features (numerical sentiment, regex'd tickers, contract addresses) and **discard the raw text** so no archive exists that could be used for RL fine-tuning. This is the IP-sale defensibility argument: a buyer's compliance audit must find no Telegram-derived training corpus on disk.
- **Output contract**: unified Pydantic v2 envelope (`SocialIntelligenceSignal`) covering source, channel, timestamp, extracted tickers, sentiment compound score, inferred direction, optional execution parameters. Published to Redis pub/sub channel `cemini:streams:social_intel`. Subscriber is the TorchRL observation builder, mapping `sentiment_compound_score` and `nlp_confidence_score` columns into the (also-not-yet-built) Polars feature DataFrame.

### Why this matters for IP sale
The prescribed pipeline is a **publisher's-exclusion candidate** on the deal-killer ledger (@concepts/ip-sale-readiness.md). Two angles:

1. **Compliance angle**: getting §1.5 isolation provably right — inference-not-training separation, raw text discarded, no archive — turns Telegram alt-data from a deal-killer into a clean feature. The MkDocs compliance section the source recommends (para 33) is the deliverable that makes due diligence land soft.
2. **Carve-out angle**: even if compliance is clean, some institutional buyers will refuse to inherit Telegram-derived signal feeds for reputational reasons. Cemini's IP-sale plan therefore gates the feature behind a flag that can be shipped or stripped at APA-execution time. (Note: the **flag** mechanism was wiki-asserted prior to K3 without server evidence; since the feature itself doesn't exist, neither does the flag. Tracking this as a downstream cleanup.)

### What the previous narrative got wrong (and why)
The pre-K3 page said *"Cemini uses Telethon..., scored by FinBERT..., stays under limits via channel-rotation and cached join-state."* All four clauses were synthesis errors:

| Pre-K3 claim | Server reality / source reality |
|---|---|
| "Cemini uses Telethon" | Not deployed (zero containers, zero deps, zero compose refs) |
| "scored by FinBERT" | FinBERT not deployed; source explicitly rejects FinBERT-class transformers |
| "channel-rotation" | Source forbids rotation across accounts as the very TOS violation Telegram bans |
| "cached join-state" | Fabricated; not in source |

This is the same prescribed-vs-deployed collapse pattern documented in @concepts/scatter-gather-topology.md (the K reframe) and @entities/infrastructure/deepseek-r1-14b.md (the local-LLM retraction). Cause: bootstrap-time synthesis read Cemini-internal blueprints as as-built descriptions because the documents adopt confident "the platform relies on" / "the system uses" prose. Fix: ground every Cemini-deployment claim against a server probe before promoting from `draft` → `validated`. Source pages can stay validated as references; entity pages must reflect actual deployment state.

## Snippets

> Telethon … Optimal. Industry standard for data extraction. Massive contributor base (over 708 GitHub contributions) ensures rapid updates to schema changes.
>
> *— @sources/3-19-telegram-discord-research.md para 79. The library-selection finding stands; Telethon is the right tool. The error was inferring deployment from selection.*

> By default, Telethon caches all of these entities into a local SQLite .session file and maintains a corresponding in-memory representation. … in a passive monitoring scenario involving a high-volume stream of messages across multiple heavily trafficked public channels, this entity cache grows continuously. … Over a period of several days, this memory leak will eventually trigger the Linux Out-Of-Memory (OOM) killer, terminating the Docker container and severing the data feed.
>
> *— @sources/3-19-telegram-discord-research.md para 83-84. Operational gotcha that any future Cemini Telethon deployment must account for via `client.session.save_entities = False`.*
