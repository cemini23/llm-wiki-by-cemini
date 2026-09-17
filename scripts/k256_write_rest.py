#!/usr/bin/env python3
"""Write leftover K256 entity pages + Outlier tungsten source."""
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"
TODAY = "2026-09-07"

SRC = WIKI / "sources" / f"substack-rss-outlier-weekly-2026-09-07-tungsten-furnace-{TODAY}.md"
SRC.write_text(
    """---
title: "Outlier Weekly — The war is a metals furnace. Tungsten is the one that does not grow back fast."
type: source
tags: [source, k256, tungsten, outlier]
keywords: [k256, APT, tungsten, ALM, ELMT]
related:
  - concepts/k256-newsletter-macro-wave.md
  - concepts/western-tungsten-supply-thesis.md
  - entities/tickers/alm.md
  - sources/defense-tungsten-supply-chain-audit-2026-09.md
maturity: draft
created: 2026-09-07
updated: 2026-09-07
read_status: read
---

## Relations

- @concepts/k256-newsletter-macro-wave.md
- @concepts/western-tungsten-supply-thesis.md
- @entities/tickers/alm.md
- @sources/defense-tungsten-supply-chain-audit-2026-09.md

## Raw Concept

| File | `substack-rss-outlier-weekly-2026-09-07-the-war-is-a-metals-furnace-tungsten-is-the-one.md` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-outlier-weekly-2026-09-07-the-war-is-a-metals-furnace-tungsten-is-the-one.md` |
| Retrieved | 2026-09-07 |
| URL | https://outlierweekly.substack.com/p/the-war-is-a-metals-furnace-tungsten |
| Dual-ID | **OSINT K256** |

## Narrative

LIVE Outlier Weekly (7 Sep 2026). Reconfirms the desk-pack forensic: APT chemistry is the choke, not mine tonnes. China about 79 percent of 2025 mine output. NHK 10 Aug 2026: Chinese APT to Japan zero since January. Four products: concentrate / APT / powder-mill / carbide. Non-China APT perimeter: Masan Nui Phao, Wolfram/Sandvik Mittersill-St Martin, GTP Towanda. DFARS 225.7018-2 from 1 Jan 2027 bans China/RU/IR/NK tungsten powder and heavy alloy for DoD. Patriot stocks in Europe beyond critical (AP 27 Aug 2026). ALM and ELMT are mentions, not the lead. No live spots in the letter. Wiki plus SEO notes bump. No xsp scp.

## Snippets

> "A tungsten shortage is the quiet choke under the Western defense build. Mine supply is concentrated in China. The immediate choke is chemical: ore must become ammonium paratungstate, APT, and that step still runs through China." [Source: substack-rss-outlier-weekly-2026-09-07-the-war-is-a-metals-furnace-tungsten-is-the-one.md]
""",
    encoding="utf-8",
)
print("wrote", SRC)

import re

def add_related(path: Path, entries: list[str]) -> None:
    if not path.exists():
        print("missing", path)
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
    print("bumped", path)


add_related(
    WIKI / "concepts" / "k256-newsletter-macro-wave.md",
    [f"sources/substack-rss-outlier-weekly-2026-09-07-tungsten-furnace-{TODAY}.md"],
)
add_related(
    WIKI / "concepts" / "western-tungsten-supply-thesis.md",
    [f"sources/substack-rss-outlier-weekly-2026-09-07-tungsten-furnace-{TODAY}.md"],
)
add_related(
    WIKI / "entities" / "tickers" / "alm.md",
    [f"sources/substack-rss-outlier-weekly-2026-09-07-tungsten-furnace-{TODAY}.md"],
)
add_related(
    WIKI / "sources" / "defense-tungsten-supply-chain-audit-2026-09.md",
    [f"sources/substack-rss-outlier-weekly-2026-09-07-tungsten-furnace-{TODAY}.md"],
)

# index row
index = WIKI / "index.md"
idx = index.read_text(encoding="utf-8")
row = f"| [outlier-tungsten-furnace](sources/substack-rss-outlier-weekly-2026-09-07-tungsten-furnace-{TODAY}.md) | Outlier Weekly tungsten APT choke LIVE | draft |"
needle = "| [eval-url-revenue-analysis]"
if "tungsten-furnace" not in idx and needle in idx:
    # insert after K256 table first data row area — append before desk pack
    idx = idx.replace(
        "| [k256-harness-evolution-wave]",
        row + "\n| [k256-harness-evolution-wave]",
        1,
    )
    index.write_text(idx, encoding="utf-8")
    print("index row added")

E = WIKI / "entities" / "tools"
E.mkdir(parents=True, exist_ok=True)
(E / "magnitude.md").write_text(
    "---\n"
    "title: Magnitude — local GGUF inference coordinator\n"
    "type: entity\n"
    "tags: [tool, k256, local-llm, apache-2.0]\n"
    "keywords: [magnitude, GGUF, local-inference, magnitudedev]\n"
    "related:\n"
    "  - concepts/k256-abliterated-lab-wave.md\n"
    "  - concepts/k256-eval-github-wave.md\n"
    "  - sources/eval-multi-wiki-revenue-2026-09-07.md\n"
    "maturity: draft\n"
    "created: 2026-09-07\n"
    "updated: 2026-09-07\n"
    "phase_0_verdict: GO REFERENCE\n"
    "harness_verb: FILE\n"
    "wire_note: Laptop REFERENCE clone only; local-abliterated lab.\n"
    "---\n\n"
    "## Relations\n\n"
    "- @concepts/k256-abliterated-lab-wave.md\n"
    "- @concepts/k256-eval-github-wave.md\n"
    "- @sources/eval-multi-wiki-revenue-2026-09-07.md\n\n"
    "## Raw Concept\n\n"
    "| Field | Value |\n"
    "|-------|-------|\n"
    "| **Repo** | https://github.com/magnitudedev/magnitude |\n"
    "| **License** | Apache-2.0 `[CONFIRMED]` gh api SPDX 2026-09-07 |\n"
    "| **Local** | `.local/adopts/magnitude` |\n"
    "| **Stars** | 3934 (2026-09-07) |\n"
    "| **Last push** | 2026-09-07 |\n\n"
    "## Narrative\n\n"
    "**Verdict.** **GO REFERENCE** (2026-09-07). FILE. Do not Integrate. Do not federation-sync. Do not point at uncensored weights from 2609.05241.\n\n"
    "## Snippets\n\n"
    '> "Apache-2.0 `[CONFIRMED]` gh api 2026-09-07; 3934 stars." [Source: gh api repos/magnitudedev/magnitude]\n',
    encoding="utf-8",
)
print("wrote magnitude")
