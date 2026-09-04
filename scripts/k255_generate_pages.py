#!/usr/bin/env python3
"""One-shot K255 ingest page generator — inbox → wiki source stubs + concept hubs."""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "research to be indexed"
WIKI = ROOT / "wiki"
TODAY = "2026-09-04"

# inbox filename stem → (source slug suffix, concept hub)
FILE_MAP: dict[str, tuple[str, str]] = {
    "arxiv-2609.01941-neural-networks-learning-the-radon-nikodym-deriv": (
        "arxiv-2609.01941-radon-nikodym-option-pricing",
        "k255-vol-quant-wave",
    ),
    "arxiv-2609.02014-insights-on-time-consistent-deep-hedging-under-e": (
        "arxiv-2609.02014-time-consistent-deep-hedging",
        "k255-vol-quant-wave",
    ),
    "arxiv-2609.02393-captchas-in-the-agentic-era-solvers-that-learn-f": (
        "arxiv-2609.02393-captchas-agentic-era",
        "k255-cybersec-wave",
    ),
    "arxiv-2609.02730-coral-an-llm-native-harness-for-production-recom": (
        "arxiv-2609.02730-coral-llm-recommender-harness",
        "k255-harness-evolution-wave",
    ),
    "arxiv-2609.02749-repo-to-skill-distilling-github-repositories-int": (
        "arxiv-2609.02749-repo-to-skill",
        "k255-harness-evolution-wave",
    ),
    "arxiv-2609.02750-bilevel-coordinated-reflection-a-game-theoretic": (
        "arxiv-2609.02750-bilevel-coordinated-reflection",
        "k255-harness-evolution-wave",
    ),
    "arxiv-2609.02771-from-reweighting-to-rewriting-unlocking-the-inte": (
        "arxiv-2609.02771-reweighting-to-rewriting",
        "k255-harness-evolution-wave",
    ),
    "arxiv-2609.02786-safeevolve-harness-policy-co-evolution-from-agen": (
        "arxiv-2609.02786-safeevolve",
        "k255-harness-evolution-wave",
    ),
    "arxiv-2609.02960-constituent-tagged-transfer-linking-cluster-dyna": (
        "arxiv-2609.02960-constituent-tagged-transfer",
        "k255-harness-evolution-wave",
    ),
    "arxiv-2609.03660-local-updates-global-learning-lugl-playing-games": (
        "arxiv-2609.03660-lugl-poker-games",
        "k255-poker-game-theory-wave",
    ),
    "arxiv-2609.03718-what-do-cae-simulation-agents-really-need-beyond": (
        "arxiv-2609.03718-cae-simulation-agents-harness",
        "k255-harness-evolution-wave",
    ),
    "arxiv-2609.03871-bioinfoysis-technical-report": (
        "arxiv-2609.03871-bioinfoysis",
        "k255-harness-evolution-wave",
    ),
    "arxiv-2609.03884-a-blind-trust-the-bloody-thrust-when-attacker-co": (
        "arxiv-2609.03884-hook-updates-steer-harness",
        "k255-harness-evolution-wave",
    ),
    "arxiv-2609.04017-a-black-box-for-agentic-processes-blockchain-anc": (
        "arxiv-2609.04017-agentic-process-black-box",
        "k255-cybersec-wave",
    ),
    "arxiv-2609.04043-extending-concurrent-separation-logic-to-the-har": (
        "arxiv-2609.04043-xv6-separation-logic-riscv",
        "k255-cybersec-wave",
    ),
    "arxiv-2609.04128-environment-evolution-for-terminal-agents": (
        "arxiv-2609.04128-environment-evolution-terminal-agents",
        "k255-harness-evolution-wave",
    ),
    "newsletter-rss-latent-space-2026-09-03-ainews-muse-spark-13-matches-gpt-56-sol-confirmi": (
        "newsletter-rss-latent-space-2026-09-03-muse-spark-gpt56-sol",
        "k255-ccc-models-wave",
    ),
    "newsletter-rss-latent-space-2026-09-03-gpt-6-astra-an-automated-ai-engineer-you-can-hir": (
        "newsletter-rss-latent-space-2026-09-03-gpt6-astra",
        "k255-ccc-models-wave",
    ),
    "newsletter-rss-latent-space-2026-09-04-ainews-gpt-6-astra-openais-biggest-llm-launch-of": (
        "newsletter-rss-latent-space-2026-09-04-gpt6-astra-launch",
        "k255-ccc-models-wave",
    ),
    "newsletter-rss-pragmatic-engineer-2026-09-03-the-pulse-tech-companies-move-to-open-ai-models": (
        "newsletter-rss-pragmatic-engineer-2026-09-03-pulse-open-ai-models",
        "k255-ccc-models-wave",
    ),
    "newsletter-rss-sterling-sky-2026-09-02-the-dynamic-serp-update-how-the-may-2026-core-up": (
        "newsletter-rss-sterling-sky-2026-09-02-dynamic-serp-may-2026-core",
        "k255-seo-gbp-wave",
    ),
    "substack-rss-event-horizon-2026-09-03-four-questions-and-answers-about-new-jersey-kals": (
        "substack-rss-event-horizon-2026-09-03-nj-kalshi-scotus",
        "k255-gambling-pm-wave",
    ),
    "substack-rss-event-horizon-2026-09-04-betting-on-prediction-markets-going-to-scotus-do": (
        "substack-rss-event-horizon-2026-09-04-pm-scotus-dont-bet",
        "k255-gambling-pm-wave",
    ),
    "substack-rss-event-horizon-2026-09-04-news-nfl-sends-letter-to-prediction-markets-stop": (
        "substack-rss-event-horizon-2026-09-04-nfl-objectionable-bets",
        "k255-gambling-pm-wave",
    ),
    "substack-rss-klement-2026-09-03-the-costs-and-benefits-of-working-for-a-large-as": (
        "substack-rss-klement-2026-09-03-large-asset-manager-costs",
        "k255-newsletter-macro-wave",
    ),
    "substack-rss-klement-2026-09-04-its-not-me-its-you": (
        "substack-rss-klement-2026-09-04-its-not-me-its-you",
        "k255-newsletter-macro-wave",
    ),
    "substack-rss-secpro-2026-09-04-250-building-an-ai-ready-soc-part-iii": (
        "substack-rss-secpro-2026-09-04-ai-ready-soc-part-iii",
        "k255-cybersec-wave",
    ),
    "substack-rss-wublock-2026-09-03-global-crypto-mining-news-in-august-chinas-first": (
        "substack-rss-wublock-2026-09-03-crypto-mining-august",
        "k255-newsletter-macro-wave",
    ),
    "substack-rss-wublock-2026-09-04-wublockchain-weekly-strategy-resumes-bitcoin-buy": (
        "substack-rss-wublock-2026-09-04-strategy-bitcoin-buys",
        "k255-newsletter-macro-wave",
    ),
    "Multi-Wiki Revenue Batch Plan": (
        "eval-multi-wiki-revenue-batch-plan-2026-09-04",
        "k255-eval-github-wave",
    ),
}

HUBS: dict[str, dict] = {
    "k255-harness-evolution-wave": {
        "title": "K255 Harness Evolution Wave (Sep 2026)",
        "tags": "agents, harness, k255, ccc",
        "keywords": "SafeEvolve, Repo-To-Skill, Environment-Evolution, hook-updates",
        "prior": "k254-harness-evolution-wave",
        "narrative": (
            "K255 harness cluster — **SafeEvolve** (harness-policy co-evolution), "
            "**Repo-To-Skill** (GitHub→AI4AI skills), **Environment Evolution** "
            "(terminal agents), **Bilevel Coordinated Reflection**, **hook-update "
            "attack on harnesses** (2609.03884), **CAE simulation agent harness needs**, "
            "**CORAL** recommender harness. Pairs K281 AutoDesign / K313 StarHarness — "
            "**HITL** before harness self-write; **0 Integrate GO** until SPDX verified."
        ),
    },
    "k255-poker-game-theory-wave": {
        "title": "K255 Poker Game Theory Wave (Sep 2026)",
        "tags": "poker, game-theory, k255, gambling",
        "keywords": "LUGL, Deep-CFR, PokerRL, imperfect-information",
        "prior": "k254-harness-evolution-wave",
        "narrative": (
            "**LUGL** (Local Updates Global Learning) — non-incremental learners in "
            "imperfect-information games; Deep-CFR / PokerRL repos cited. Route to "
            "Poker Arena briefs; **no prod scp**."
        ),
    },
    "k255-vol-quant-wave": {
        "title": "K255 Vol Quant Wave (Sep 2026)",
        "tags": "vol, quant, k255, options",
        "keywords": "Radon-Nikodym, deep-hedging, incomplete-markets",
        "prior": "k254-vol-quant-wave",
        "narrative": (
            "Radon–Nikodym derivative NN option pricing + time-consistent deep hedging "
            "under elicitable dynamic risk measures. Wiki-only; pairs K254 VRP nuclear stub."
        ),
    },
    "k255-gambling-pm-wave": {
        "title": "K255 Gambling PM Wave (Sep 2026)",
        "tags": "gambling, prediction-markets, k255",
        "keywords": "Kalshi, SCOTUS, NFL, objectionable-bets",
        "prior": "k254-gambling-pm-wave",
        "narrative": (
            "Event Horizon NJ/Kalshi/SCOTUS Q&A; SCOTUS PM betting skepticism; NFL letter "
            "on objectionable DCM contracts (injuries, mentions, roster). Awareness only; **no pm scp**."
        ),
    },
    "k255-newsletter-macro-wave": {
        "title": "K255 Newsletter Macro Wave (Sep 2026)",
        "tags": "macro, newsletter, k255, guruwatcher",
        "keywords": "Klement, Wu-Blockchain, asset-managers",
        "prior": "k254-newsletter-macro-wave",
        "narrative": (
            "Klement on large-asset-manager economics + marriage-model satire (wiki-only). "
            "Wu crypto mining + Strategy BTC buys → GuruWatcher alert-only awareness."
        ),
    },
    "k255-ccc-models-wave": {
        "title": "K255 CCC Models Wave (Sep 2026)",
        "tags": "ccc, models, k255, routing",
        "keywords": "GPT-6-Astra, Muse-Spark, open-models",
        "prior": "k254-ccc-models-wave",
        "narrative": (
            "Latent Space GPT-6 Astra automated-AE launch + Muse Spark vs GPT-5.6-Sol; "
            "Pragmatic Pulse on tech cos moving to open AI models. FILE awareness; no harness swap."
        ),
    },
    "k255-cybersec-wave": {
        "title": "K255 Cybersec Wave (Sep 2026)",
        "tags": "cybersec, harness, k255, soc",
        "keywords": "AI-SOC, CAPTCHA, xv6, agent-black-box",
        "prior": "k253-auditable-mas-clinical-stub",
        "narrative": (
            "SecPro AI-ready SOC part III (fold with parts I–II); agentic CAPTCHA solvers; "
            "xv6 RISC-V separation logic; blockchain-anchored agent process evidence. "
            "Route cyber briefs; no PoC templates."
        ),
    },
    "k255-eval-github-wave": {
        "title": "K255 Eval GitHub Wave (Sep 2026)",
        "tags": "eval, github, k255, revenue",
        "keywords": "Multi-Wiki-Revenue, FalconFlank, URL-eval",
        "prior": "k254-eval-github-wave",
        "narrative": (
            "Multi-Wiki Revenue Batch Plan docx — URL revenue eval batch. "
            "**FILE** until SPDX `gh api` per URL; FalconFlank flagged for Phase-0 spot-check."
        ),
    },
    "k255-seo-gbp-wave": {
        "title": "K255 SEO GBP Wave (Sep 2026)",
        "tags": "seo, serp, k255, sterling-sky",
        "keywords": "dynamic-SERP, May-2026-core-update",
        "prior": "k254-seo-gbp-wave",
        "narrative": (
            "Sterling Sky dynamic SERP — same keyword, different results by user/time "
            "(May 2026 core update). Route `@seo-wiki` brief stub."
        ),
    },
}


def parse_md_title(text: str) -> str:
    m = re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", text, re.M)
    if m:
        return m.group(1).strip()
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else "Untitled"


def parse_arxiv_id(stem: str) -> str | None:
    m = re.search(r"arxiv-(\d+\.\d+)", stem)
    return m.group(1) if m else None


def excerpt_body(text: str, limit: int = 600) -> str:
    if "---" in text:
        parts = text.split("---", 2)
        body = parts[2] if len(parts) > 2 else text
    else:
        body = text
    body = re.sub(r"\n{3,}", "\n\n", body.strip())
    if len(body) > limit:
        body = body[:limit].rsplit(" ", 1)[0] + "…"
    return body


def write_source(slug: str, hub: str, inbox_name: str, title: str, body_excerpt: str, is_pdf: bool) -> Path:
    path = WIKI / "sources" / f"{slug}-{TODAY}.md"
    arxiv = parse_arxiv_id(inbox_name)
    extra_related = []
    if slug.startswith("substack-rss-secpro"):
        extra_related = [
            "  - sources/substack-rss-secpro-2026-08-21-ai-ready-soc.md",
            "  - sources/substack-rss-secpro-2026-08-28-249-ai-ready-soc.md",
        ]
    if "03884" in slug:
        extra_related.append("  - concepts/k255-cybersec-wave.md")

    related_lines = [
        f"  - concepts/{hub}.md",
        *extra_related,
    ]
    relations = [f"- @concepts/{hub}.md"]
    for r in extra_related:
        rel = r.strip().removeprefix("- ").strip()
        relations.append(f"- @{rel}")

    read_status = "skimmed" if is_pdf else "read"
    raw_rows = [
        f"| File | `{inbox_name}` |",
        f"| Retrieved | {TODAY} |",
        "| Dual-ID | **OSINT K255** |",
    ]
    if arxiv:
        raw_rows.insert(0, f"| Paper | arXiv:{arxiv} |")

    content = f"""---
title: "{title.replace('"', "'")}"
type: source
tags: [source, k255]
keywords: [k255]
related:
{chr(10).join(related_lines)}
maturity: draft
created: {TODAY}
updated: {TODAY}
read_status: {read_status}
---

## Relations

{chr(10).join(relations)}

## Raw Concept

{chr(10).join(raw_rows)}

## Narrative

K255 wiki ingest. {"No public SPDX clone at Phase-0." if is_pdf else "Newsletter/substack ingest."}

{body_excerpt}

## Snippets

> "{title[:120]}…" [Source: {inbox_name}]
"""
    path.write_text(content, encoding="utf-8")
    return path


def write_hub(slug: str, meta: dict, sources: list[str]) -> Path:
    path = WIKI / "concepts" / f"{slug}.md"
    prior = meta["prior"]
    related = [f"  - concepts/{prior}.md"] + [f"  - sources/{s}-{TODAY}.md" for s in sources]
    relations = [f"- @concepts/{prior}.md"] + [f"- @sources/{s}-{TODAY}.md" for s in sources]

    content = f"""---
title: {meta["title"]}
type: concept
tags: [{meta["tags"]}]
keywords: [{meta["keywords"]}]
related:
{chr(10).join(related)}
maturity: draft
created: {TODAY}
updated: {TODAY}
harness_verb: FILE
---

## Relations

{chr(10).join(relations)}

## Raw Concept

K255 cluster hub.

## Narrative

{meta["narrative"]}
"""
    path.write_text(content, encoding="utf-8")
    return path


def main() -> None:
    hub_sources: dict[str, list[str]] = {k: [] for k in HUBS}

    for inbox_path in sorted(INBOX.iterdir()):
        if inbox_path.name.startswith("."):
            continue
        stem = inbox_path.stem
        if stem.endswith(".pdf"):
            stem = stem  # noqa: PLW0127 — pdf stem without .pdf
        key = stem
        if inbox_path.suffix == ".docx":
            key = inbox_path.stem
        if key not in FILE_MAP and inbox_path.stem in FILE_MAP:
            key = inbox_path.stem
        if key not in FILE_MAP:
            print(f"SKIP unmapped: {inbox_path.name}")
            continue

        slug, hub = FILE_MAP[key]
        is_pdf = inbox_path.suffix.lower() == ".pdf"

        if is_pdf:
            title = stem.replace("arxiv-", "arXiv ").replace("-", " ").title()
            body = "ArXiv PDF — abstract skim at ingest; deep-read optional."
        else:
            text = inbox_path.read_text(encoding="utf-8", errors="replace")
            title = parse_md_title(text)
            body = excerpt_body(text)

        write_source(slug, hub, inbox_path.name, title, body, is_pdf)
        hub_sources[hub].append(slug)
        print(f"OK source: {slug}")

    for hub_slug, meta in HUBS.items():
        srcs = hub_sources.get(hub_slug, [])
        if srcs:
            write_hub(hub_slug, meta, srcs)
            print(f"OK hub: {hub_slug} ({len(srcs)} sources)")

    print(f"Done — {sum(len(v) for v in hub_sources.values())} sources, {len(HUBS)} hubs")


if __name__ == "__main__":
    main()
