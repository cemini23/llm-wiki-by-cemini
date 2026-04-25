#!/usr/bin/env python3
"""Phase 3 lint-fix — close bidirectional gaps; create stubs for dangling refs."""
import re
from datetime import date
from pathlib import Path

WIKI = Path("/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki")
TODAY = date.today().isoformat()

fm_re = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_page(path: Path) -> dict:
    text = path.read_text()
    m = fm_re.match(text)
    if not m:
        return {}
    fm = m.group(1)
    related: list[str] = []
    in_related = False
    for ln in fm.splitlines():
        if ln.startswith("related:"):
            in_related = True
            if ln.strip() == "related: []":
                in_related = False
            continue
        if in_related:
            if ln.startswith("  - "):
                related.append(ln[4:].strip())
            elif ln.strip() == "" or (ln and not ln.startswith(" ")):
                in_related = False
    return {"related": related, "text": text, "fm": fm}


def add_related_ref(path: Path, new_ref: str) -> bool:
    info = parse_page(path)
    if not info:
        return False
    if new_ref in info["related"]:
        return False
    text = info["text"]
    m = fm_re.match(text)
    fm_body = m.group(1)
    rest = text[m.end():]

    lines = fm_body.splitlines()
    out: list[str] = []
    i = 0
    inserted = False
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("related:"):
            if ln.strip() == "related: []":
                out.append("related:")
                out.append(f"  - {new_ref}")
                inserted = True
                i += 1
                continue
            out.append(ln)
            i += 1
            # copy existing refs
            while i < len(lines) and lines[i].startswith("  - "):
                out.append(lines[i])
                i += 1
            out.append(f"  - {new_ref}")
            inserted = True
            continue
        out.append(ln)
        i += 1

    if not inserted:
        return False

    # bump updated
    out2 = []
    for ln in out:
        if ln.startswith("updated:"):
            out2.append(f"updated: {TODAY}")
        else:
            out2.append(ln)

    new_fm = "\n".join(out2)

    # Update Relations section
    new_related_full = info["related"] + [new_ref]
    rel_lines = "\n".join(f"- @{r}" for r in new_related_full)
    new_relations_block = f"## Relations\n\n{rel_lines}\n"
    rel_pattern = re.compile(r"## Relations\n.*?(?=\n## |\Z)", re.DOTALL)
    if rel_pattern.search(rest):
        new_rest = rel_pattern.sub(new_relations_block.rstrip() + "\n", rest, count=1)
    else:
        new_rest = "\n" + new_relations_block + rest

    path.write_text(f"---\n{new_fm}\n---\n{new_rest}")
    return True


# 1. Build full inventory of (rel_path, related) pairs
pages: dict[str, list[str]] = {}
for p in WIKI.rglob("*.md"):
    if p.name in {"index.md", "log.md"}:
        continue
    rel = str(p.relative_to(WIKI))
    info = parse_page(p)
    if info:
        pages[rel] = info["related"]

# 2. Compute gaps
gaps = []
for rel, refs in pages.items():
    for ref in refs:
        if ref in pages and rel not in pages[ref]:
            gaps.append((rel, ref))

print(f"Gaps to fix: {len(gaps)}")

# 3. Close each gap (add rel to ref's related list)
fixed = 0
for src, target in gaps:
    target_path = WIKI / target
    if add_related_ref(target_path, src):
        fixed += 1
        pages[target].append(src)  # keep local state in sync
print(f"Closed {fixed}/{len(gaps)} gaps")

# 4. Create concept stubs for dangling refs: carry-trade, cameo-codes, goldstein-scale
STUBS = {
    "carry-trade": dict(
        title="Carry trade",
        tags=["concept", "forex", "strategy", "stub"],
        related=["entities/platforms/oanda.md"],
        narrative="""A **carry trade** borrows in a low-interest-rate currency and invests in a
higher-yielding one, harvesting the interest-rate differential. In Cemini's
FX stack, carry-trade variants on G10 crosses (notably EUR/USD, AUD/JPY)
are gated by the Macro Weather regime — disabled in RED, half-sized in
YELLOW — because carry trades historically unwind violently in risk-off
episodes. See the forex-research-3-18 deep read for specific pair-level
parameterization and risk-engine integration.""",
    ),
    "cameo-codes": dict(
        title="CAMEO codes (Conflict and Mediation Event Observations)",
        tags=["concept", "alt-data", "events", "schema", "stub"],
        related=["entities/data-sources/gdelt.md"],
        narrative="""**CAMEO** (Conflict and Mediation Event Observations) is the event-type
taxonomy used by GDELT to classify news events. ~300 codes organized
hierarchically from 01 (public statements) to 20 (unconventional mass
violence). Cemini aggregates CAMEO event counts per country-window and
correlates with asset-price moves to generate macro-regime features.
Combined with the Goldstein scale for intensity, CAMEO codes form the
event-structure backbone of GDELT-derived signals.""",
    ),
    "goldstein-scale": dict(
        title="Goldstein scale",
        tags=["concept", "alt-data", "events", "intensity-metric", "stub"],
        related=["entities/data-sources/gdelt.md"],
        narrative="""The **Goldstein scale** is a -10 to +10 conflict/cooperation intensity
metric assigned to each CAMEO-coded event in GDELT. Negative values
indicate conflict (up to -10 for military attack); positive values
indicate cooperation (up to +10 for formal alliance). Cemini uses rolling
per-country Goldstein aggregates as a country-instability predictor and
as a feature in the 3-29-research-4 Bayesian-deep-learning model for
macro-regime classification.""",
    ),
}

created_stubs = 0
for slug, meta in STUBS.items():
    path = WIKI / "concepts" / f"{slug}.md"
    if path.exists():
        continue
    tags_str = ", ".join(meta["tags"])
    fm_rel = "\n".join(f"  - {r}" for r in meta["related"])
    rel_lines = "\n".join(f"- @{r}" for r in meta["related"])
    content = f"""---
title: {meta['title']}
type: concept
tags: [{tags_str}]
keywords: []
related:
{fm_rel}
maturity: draft
created: {TODAY}
updated: {TODAY}
---

## Relations

{rel_lines}

## Raw Concept

Stub created during Phase 3 lint to close dangling ref from an entity page. Expand on deep-read.

## Narrative

{meta['narrative'].strip()}

## Snippets

*(none yet — populate on first deep read.)*
"""
    path.write_text(content)
    created_stubs += 1

    # Add bidirectional backlink to the parent entity
    for parent in meta["related"]:
        parent_path = WIKI / parent
        if parent_path.exists():
            add_related_ref(parent_path, f"concepts/{slug}.md")

print(f"Created {created_stubs} concept stubs for dangling refs")
print("Done.")
