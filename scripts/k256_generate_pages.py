#!/usr/bin/env python3
"""K256 ingest page generator — inbox → sources + hubs + index."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "research to be indexed"
WIKI = ROOT / "wiki"
TODAY = "2026-09-07"
META = json.loads(Path("/tmp/k256_arxiv_meta.json").read_text())
DATA = json.loads((Path(__file__).with_name("k256_page_data.json")).read_text())
NARR = json.loads((Path(__file__).with_name("k256_narratives.json")).read_text())
HUBS = DATA["hubs"]
EXTRA_RELATED = DATA["extra_related"]
HUB_ENTITIES = DATA["hub_entities"]

FILE_MAP: list[tuple[str, str, str]] = [
    ("arxiv-2609.03693", "arxiv-2609.03693-alcatraz-jailbreak-defense", "k256-cybersec-wave"),
    ("arxiv-2609.03887", "arxiv-2609.03887-beyond-shallow-alignment", "k256-abliterated-lab-wave"),
    ("arxiv-2609.03960", "arxiv-2609.03960-fimi-banking", "k256-ood-stub-wave"),
    ("arxiv-2609.04542", "arxiv-2609.04542-matched-starts-divergent-objects", "k256-atto-collab-wave"),
    ("arxiv-2609.04721", "arxiv-2609.04721-locating-steering-refusal", "k256-abliterated-lab-wave"),
    ("arxiv-2609.04871", "arxiv-2609.04871-autolr-launch-review", "k256-harness-evolution-wave"),
    ("arxiv-2609.04894", "arxiv-2609.04894-world-acting-systems", "k256-harness-evolution-wave"),
    ("arxiv-2609.04898", "arxiv-2609.04898-refactorplatform", "k256-harness-evolution-wave"),
    ("arxiv-2609.05047", "arxiv-2609.05047-gatheral-conjecture", "k256-vol-quant-wave"),
    ("arxiv-2609.05117", "arxiv-2609.05117-tier-threat-implicitness", "k256-abliterated-lab-wave"),
    ("arxiv-2609.05171", "arxiv-2609.05171-weagent-mmgenedit", "k256-ood-stub-wave"),
    ("arxiv-2609.05241", "arxiv-2609.05241-uncensored-open-weight", "k256-abliterated-lab-wave"),
    ("arxiv-2609.05335", "arxiv-2609.05335-cve-patch-history-detector", "k256-cybersec-wave"),
    ("newsletter-rss-latent-space-2026-09-05", "newsletter-rss-latent-space-2026-09-05-grok-bot-openclaw", "k256-ccc-models-wave"),
    ("substack-rss-capital-flows-2026-09-04", "substack-rss-capital-flows-2026-09-04-complacency-bonds", "k256-newsletter-macro-wave"),
    ("substack-rss-capital-flows-2026-09-07", "substack-rss-capital-flows-2026-09-07-monetary-escalation", "k256-newsletter-macro-wave"),
    ("substack-rss-klement-2026-09-07", "substack-rss-klement-2026-09-07-organic-farming", "k256-newsletter-macro-wave"),
    ("substack-rss-wublock-2026-09-05", "substack-rss-wublock-2026-09-05-kalshi-lifetime-ban", "k256-gambling-pm-wave"),
    ("substack-rss-wublock-2026-09-06", "substack-rss-wublock-2026-09-06-asia-top10", "k256-newsletter-macro-wave"),
    ("substack-rss-wublock-2026-09-07-august-vc", "substack-rss-wublock-2026-09-07-august-vc", "k256-newsletter-macro-wave"),
    ("substack-rss-wublock-2026-09-07-wublockchain-weekly-outlook", "substack-rss-wublock-2026-09-07-weekly-outlook", "k256-newsletter-macro-wave"),
    ("Multi-Wiki Revenue Opportunity Evaluation", "eval-multi-wiki-revenue", "k256-eval-github-wave"),
    ("URL Revenue Opportunity Analysis", "eval-url-revenue-analysis", "k256-eval-github-wave"),
]


def yaml_title(s: str) -> str:
    return s.replace('"', "'")


def snippet(text: str, n: int = 280) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > n:
        return text[:n].rsplit(" ", 1)[0] + "…"
    return text


def parse_md_title(text: str) -> str:
    m = re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", text, re.M)
    if m:
        return m.group(1).strip()
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else "Untitled"


def match_inbox(name: str) -> tuple[str, str] | None:
    stem = Path(name).stem
    for prefix, slug, hub in FILE_MAP:
        if stem.startswith(prefix) or name.startswith(prefix):
            return slug, hub
    return None


def write_source(slug: str, hub: str, inbox_name: str, title: str, body: str, is_pdf: bool) -> None:
    path = WIKI / "sources" / f"{slug}-{TODAY}.md"
    arxiv = None
    m = re.search(r"arxiv-(\d+\.\d+)", inbox_name)
    if m:
        arxiv = m.group(1)
    extra = EXTRA_RELATED.get(slug, [])
    related = [f"  - concepts/{hub}.md"] + [f"  - {e}" for e in extra]
    relations = [f"- @concepts/{hub}.md"] + [f"- @{e}" for e in extra]
    loc = f"cemini-egress-fi:/opt/cemini-bulk/research/osint/{inbox_name}"
    raw = []
    if arxiv:
        raw.append(f"| Paper | arXiv:{arxiv} |")
    raw += [
        f"| File | `{inbox_name}` |",
        f"| Location | `{loc}` |",
        f"| Retrieved | {TODAY} |",
        "| Dual-ID | **OSINT K256** |",
    ]
    snip_src = body
    if arxiv and arxiv in META:
        snip_src = META[arxiv]["summary"]
    tags = "arxiv, source, k256" if is_pdf else "source, k256"
    path.write_text(
        "\n".join(
            [
                "---",
                f'title: "{yaml_title(title)}"',
                "type: source",
                f"tags: [{tags}]",
                "keywords: [k256]",
                "related:",
                *related,
                "maturity: draft",
                f"created: {TODAY}",
                f"updated: {TODAY}",
                f"read_status: {'skimmed' if is_pdf else 'read'}",
                "---",
                "",
                "## Relations",
                "",
                *relations,
                "",
                "## Raw Concept",
                "",
                *raw,
                "",
                "## Narrative",
                "",
                body,
                "",
                "## Snippets",
                "",
                f'> "{snippet(snip_src)}" [Source: {inbox_name}]',
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_hub(slug: str, meta: dict, sources: list[str], extra_entities: list[str]) -> None:
    path = WIKI / "concepts" / f"{slug}.md"
    prior = meta["prior"]
    related = [f"  - concepts/{prior}.md"]
    relations = [f"- @concepts/{prior}.md"]
    for s in sources:
        related.append(f"  - sources/{s}-{TODAY}.md")
        relations.append(f"- @sources/{s}-{TODAY}.md")
    for e in extra_entities:
        related.append(f"  - {e}")
        relations.append(f"- @{e}")
    path.write_text(
        "\n".join(
            [
                "---",
                f"title: {meta['title']}",
                "type: concept",
                f"tags: [{meta['tags']}]",
                f"keywords: [{meta['keywords']}]",
                "related:",
                *related,
                "maturity: draft",
                f"created: {TODAY}",
                f"updated: {TODAY}",
                "harness_verb: FILE",
                "---",
                "",
                "## Relations",
                "",
                *relations,
                "",
                "## Raw Concept",
                "",
                "K256 cluster hub.",
                "",
                "## Narrative",
                "",
                meta["narrative"],
                "",
            ]
        ),
        encoding="utf-8",
    )


def add_related(path: Path, entries: list[str]) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    for entry in entries:
        rel_line = f"  - {entry}"
        at_line = f"- @{entry}"
        if rel_line not in text:
            text = re.sub(
                r"(related:\n(?:  - .+\n)*)",
                lambda m, line=rel_line: m.group(1) + line + "\n",
                text,
                count=1,
            )
        if at_line not in text:
            text = re.sub(
                r"(## Relations\n\n(?:- .+\n)*)",
                lambda m, line=at_line: m.group(1) + line + "\n",
                text,
                count=1,
            )
    text = re.sub(r"^updated: \d{4}-\d{2}-\d{2}$", f"updated: {TODAY}", text, count=1, flags=re.M)
    path.write_text(text, encoding="utf-8")


def insert_index(rows: list[str], blurb: str) -> None:
    index = WIKI / "index.md"
    text = index.read_text(encoding="utf-8")
    if "### K256 ingest" in text:
        return
    block = (
        f"### K256 ingest ({TODAY})\n"
        f"{blurb}\n\n"
        "| Page | Summary | Maturity |\n"
        "|------|---------|----------|\n"
        + "\n".join(rows)
        + "\n\n"
    )
    marker = "### Desk pack ingest (2026-09-04)"
    if marker not in text:
        raise SystemExit("index.md marker missing")
    index.write_text(text.replace(marker, block + marker, 1), encoding="utf-8")


def main() -> None:
    hub_sources: dict[str, list[str]] = {k: [] for k in HUBS}
    index_rows: list[str] = []
    for inbox_path in sorted(INBOX.iterdir()):
        if inbox_path.name.startswith("."):
            continue
        matched = match_inbox(inbox_path.name)
        if not matched:
            print(f"SKIP unmapped: {inbox_path.name}")
            continue
        slug, hub = matched
        is_pdf = inbox_path.suffix.lower() == ".pdf"
        arxiv = None
        m = re.search(r"arxiv-(\d+\.\d+)", inbox_path.name)
        if m:
            arxiv = m.group(1)
        if is_pdf and arxiv and arxiv in META:
            title = META[arxiv]["title"]
        elif inbox_path.suffix.lower() == ".md":
            title = parse_md_title(inbox_path.read_text(encoding="utf-8", errors="replace"))
        else:
            title = inbox_path.stem.replace("-", " ")
        body = NARR.get(slug, "K256 wiki ingest.")
        write_source(slug, hub, inbox_path.name, title, body, is_pdf)
        hub_sources[hub].append(slug)
        index_rows.append(
            f"| [{slug}](sources/{slug}-{TODAY}.md) | {yaml_title(title)[:70]} | draft |"
        )
        print(f"OK source: {slug}")

    hub_index: list[str] = []
    for hub_slug, meta in HUBS.items():
        srcs = hub_sources.get(hub_slug, [])
        if srcs:
            write_hub(hub_slug, meta, srcs, HUB_ENTITIES.get(hub_slug, []))
            hub_index.append(f"| [{hub_slug}](concepts/{hub_slug}.md) | {meta['title']} | draft |")
            print(f"OK hub: {hub_slug} ({len(srcs)} sources)")

    add_related(
        WIKI / "concepts" / "k255-harness-evolution-wave.md",
        [
            "concepts/k256-harness-evolution-wave.md",
            "concepts/k256-atto-collab-wave.md",
            "concepts/k256-ood-stub-wave.md",
        ],
    )
    add_related(
        WIKI / "concepts" / "k255-cybersec-wave.md",
        ["concepts/k256-cybersec-wave.md", "concepts/k256-abliterated-lab-wave.md"],
    )
    add_related(WIKI / "concepts" / "k255-vol-quant-wave.md", ["concepts/k256-vol-quant-wave.md"])
    add_related(WIKI / "concepts" / "k255-ccc-models-wave.md", ["concepts/k256-ccc-models-wave.md"])
    add_related(
        WIKI / "concepts" / "k255-newsletter-macro-wave.md",
        ["concepts/k256-newsletter-macro-wave.md"],
    )
    add_related(
        WIKI / "concepts" / "k255-gambling-pm-wave.md", ["concepts/k256-gambling-pm-wave.md"]
    )
    add_related(
        WIKI / "concepts" / "k255-eval-github-wave.md", ["concepts/k256-eval-github-wave.md"]
    )
    add_related(
        WIKI / "entities" / "tools" / "grok-bot.md",
        [
            "sources/newsletter-rss-latent-space-2026-09-05-grok-bot-openclaw-2026-09-07.md",
            "concepts/k256-ccc-models-wave.md",
        ],
    )
    add_related(
        WIKI / "concepts" / "grok-bot-operator-patterns.md",
        ["sources/newsletter-rss-latent-space-2026-09-05-grok-bot-openclaw-2026-09-07.md"],
    )
    add_related(
        WIKI / "entities" / "tools" / "openai-codex-security.md",
        [
            "sources/eval-url-revenue-analysis-2026-09-07.md",
            "concepts/k256-eval-github-wave.md",
            "concepts/k256-cybersec-wave.md",
        ],
    )
    add_related(
        WIKI / "entities" / "tools" / "addyosmani-agent-skills.md",
        ["sources/eval-url-revenue-analysis-2026-09-07.md", "concepts/k256-eval-github-wave.md"],
    )

    blurb = (
        "OSINT K256: 13 arXiv (11 inbox + 2 skipped-cap fetched) + 2 eval docx + 8 newsletters. "
        "Phase-0 REFERENCE: magnitude (Apache-2.0), RefactorPlatform (MIT), cve-mcp-server "
        "(Apache-2.0). trailofbits/skills CC-BY-SA-4.0 EXTRACT-ONLY. Grok Bot FILE bump. "
        "Kalshi lifetime ban awareness. No xsp/pm scp. 0 Integrate GO."
    )
    insert_index(hub_index + index_rows, blurb)
    print(
        f"Done — {sum(len(v) for v in hub_sources.values())} sources, "
        f"{sum(1 for v in hub_sources.values() if v)} hubs"
    )


if __name__ == "__main__":
    main()
