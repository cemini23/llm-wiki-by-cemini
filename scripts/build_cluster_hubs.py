#!/usr/bin/env python3
"""
Build 4 corpus-index hub pages for the remaining tagged-but-hub-less clusters
and add bidirectional backlinks across all member sources.

Mirrors the D + D′ task pattern (rl-marl-research.md, llm-agent-systems.md,
ai-ethics-and-governance.md, corpus-overflow-out-of-scope.md): each hub is an
index-only discovery aid listing all cluster members alphabetically with
matching `## Relations` bullets. Source pages get the hub appended to their
`related:` frontmatter + a Relations bullet.

Hub clusters built here:
  options-derivatives — derivatives-pricing literature (Black-Scholes,
    implied vol, gamma/delta hedging, variance swaps, rough-vol models)
  market-microstructure — order-book / market-maker / latency / HFT
  quant-finance — VaR / volatility / backtest / factor / signal generally
  portfolio-strategy — Sharpe / Kelly / risk-parity / mean-variance / allocation

Usage (from workspace root):
    python3 scripts/build_cluster_hubs.py
"""
import re
import sys
import yaml
from collections import defaultdict
from pathlib import Path

ROOT = Path("/Users/claudiobarone/Desktop/OSINT WORKSPACE")
SOURCES = ROOT / "wiki/sources"
CONCEPTS = ROOT / "wiki/concepts"
TODAY = "2026-04-27"

HUBS = {
    "options-derivatives": {
        "slug": "options-derivatives",
        "title": "Options & Derivatives — Corpus Index",
        "tags": ["concept", "options-derivatives", "derivatives", "research-index"],
        "keywords": ["options", "derivatives", "implied-volatility", "delta-hedging",
                     "rough-volatility", "variance-swap", "cemini-corpus"],
        "noun": "Options & Derivatives",
        "narrative_topic": "options and derivatives",
        "narrative_themes": [
            "American/European option pricing models",
            "stochastic volatility (rough-vol, fractional models)",
            "delta / gamma / vega hedging frameworks",
            "variance swaps and volatility-of-volatility",
            "regulatory + audit applications of derivative-pricing math",
        ],
    },
    "market-microstructure": {
        "slug": "market-microstructure",
        "title": "Market Microstructure — Corpus Index",
        "tags": ["concept", "market-microstructure", "order-book", "research-index"],
        "keywords": ["microstructure", "order-book", "limit-order", "market-maker",
                     "bid-ask", "latency", "HFT", "cemini-corpus"],
        "noun": "Market Microstructure",
        "narrative_topic": "market microstructure",
        "narrative_themes": [
            "order-book dynamics and limit-order placement",
            "market-maker inventory and adverse-selection models",
            "high-frequency price-process anomalies",
            "latency-arbitrage and HFT behavior",
            "ETF microstructure and intraday liquidity (QQQ, SPY)",
        ],
    },
    "quant-finance": {
        "slug": "quant-finance",
        "title": "Quantitative Finance — Corpus Index",
        "tags": ["concept", "quant-finance", "volatility", "research-index"],
        "keywords": ["quant-finance", "volatility", "VaR", "drawdown", "backtest",
                     "alpha", "factor", "signal", "cemini-corpus"],
        "noun": "Quantitative Finance",
        "narrative_topic": "quantitative finance",
        "narrative_themes": [
            "volatility forecasting and regime detection",
            "VaR / CVaR / drawdown risk measures",
            "backtesting methodology and look-ahead bias",
            "factor models and signal generation",
            "alpha decay and capacity constraints",
        ],
    },
    "portfolio-strategy": {
        "slug": "portfolio-strategy",
        "title": "Portfolio Strategy — Corpus Index",
        "tags": ["concept", "portfolio-strategy", "allocation", "research-index"],
        "keywords": ["portfolio", "Sharpe", "risk-parity", "factor-model",
                     "mean-variance", "Kelly", "allocation", "rebalanc",
                     "cemini-corpus"],
        "noun": "Portfolio Strategy",
        "narrative_topic": "portfolio strategy",
        "narrative_themes": [
            "Sharpe / Sortino / Calmar ratio optimization",
            "risk parity and equal-risk-contribution allocation",
            "mean-variance + Black-Litterman",
            "Kelly sizing under finite capital",
            "rebalance frequency and turnover control",
        ],
    },
}

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(txt):
    m = FRONTMATTER_RE.match(txt)
    if not m:
        return None, None, txt
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except Exception:
        return None, None, txt
    return fm, m.group(0), txt[m.end():]


def render_frontmatter(fm):
    # Custom render to keep `related:` block formatted as YAML list
    lines = ["---"]
    for k in ("title", "type", "tags", "keywords", "related", "maturity", "created", "updated", "read_status"):
        if k not in fm:
            continue
        v = fm[k]
        if isinstance(v, list):
            if k == "tags" or k == "keywords":
                lines.append(f"{k}: [{', '.join(v)}]")
            else:
                if v:
                    lines.append(f"{k}:")
                    for item in v:
                        lines.append(f"  - {item}")
                else:
                    lines.append(f"{k}: []")
        else:
            lines.append(f"{k}: {v}")
    # Preserve any extra keys
    extra = [k for k in fm if k not in {"title", "type", "tags", "keywords", "related",
                                         "maturity", "created", "updated", "read_status"}]
    for k in extra:
        v = fm[k]
        if isinstance(v, list):
            if v:
                lines.append(f"{k}:")
                for item in v:
                    lines.append(f"  - {item}")
            else:
                lines.append(f"{k}: []")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def collect_members():
    """Returns dict {hub_tag: sorted [source_filename, ...]}"""
    members = defaultdict(list)
    for f in sorted(SOURCES.glob("*.md")):
        txt = f.read_text()
        fm, _, _ = parse_frontmatter(txt)
        if not fm:
            continue
        tags = fm.get("tags", []) or []
        for hub_tag in HUBS:
            if hub_tag in tags:
                members[hub_tag].append(f.name)
    return members


def build_hub(hub_tag, member_files):
    """Write the hub page."""
    cfg = HUBS[hub_tag]
    slug = cfg["slug"]
    target = CONCEPTS / f"{slug}.md"

    related = sorted(f"sources/{m}" for m in member_files)

    fm_lines = [
        "---",
        f"title: {cfg['title']}",
        "type: concept",
        f"tags: [{', '.join(cfg['tags'])}]",
        f"keywords: [{', '.join(cfg['keywords'])}]",
        "related:",
    ]
    for r in related:
        fm_lines.append(f"  - {r}")
    fm_lines += [
        "maturity: draft",
        f"created: {TODAY}",
        f"updated: {TODAY}",
        "---",
    ]
    frontmatter = "\n".join(fm_lines) + "\n"

    relations_lines = ["", "## Relations", ""]
    for r in related:
        relations_lines.append(f"- @{r} — {cfg['noun']} source in the Cemini research corpus")

    raw_concept = [
        "",
        "## Raw Concept",
        "",
        f"Hub page for the {hub_tag} cluster of the Cemini research corpus "
        f"({len(member_files)} sources at bootstrap from the Q 2026-04-27 sweep). "
        f"Sources cover {cfg['narrative_topic']}-related research surfaced by the "
        f"corpus-bootstrap cluster router (first-keyword-wins regex match against "
        f"`{hub_tag}` keyword set).",
        "",
        "This page is a discovery index — it gives the tagged sources at least one "
        "inbound reference and makes the cluster navigable. Pages should be "
        "individually deep-read before their findings are promoted to entity or concept pages.",
        "",
    ]

    themes = "\n".join(f"- {t}" for t in cfg["narrative_themes"])
    narrative = [
        "## Narrative",
        "",
        f"The {hub_tag} cluster covers (non-exhaustively):",
        "",
        themes,
        "",
        "Cluster membership is established by the corpus-bootstrap router's regex "
        f"matching against `{hub_tag}` keywords (see `scripts/bootstrap_extract.py` "
        "and `scripts/bootstrap_inbox.py`). False-positives are expected: "
        "first-keyword-wins routing matches surface-level vocabulary, not topical "
        "intent. Manual re-cluster on deep read is acceptable.",
        "",
        "Cross-cluster overlap with other hubs is explicit (a single source can be "
        "tagged into multiple of: options-derivatives, market-microstructure, "
        "quant-finance, portfolio-strategy). Each hub lists every member regardless "
        "of overlap — the hubs are discovery aids, not partitioning categories.",
        "",
        "## Snippets",
        "",
        "*(None yet — index-only hub page.)*",
        "",
    ]

    body = "\n".join(relations_lines + raw_concept + narrative)
    target.write_text(frontmatter + body)
    print(f"  wrote hub: {target.relative_to(ROOT)}  ({len(member_files)} members)")


def add_hub_to_source(src_path, hub_slugs_for_source):
    """Update a source page's frontmatter `related:` and Relations bullets."""
    txt = src_path.read_text()
    fm, fm_block, body = parse_frontmatter(txt)
    if fm is None:
        return False

    related = fm.get("related") or []
    if isinstance(related, list) is False:
        related = []
    new_paths = [f"concepts/{slug}.md" for slug in hub_slugs_for_source]
    added = []
    for p in new_paths:
        if p not in related:
            related.append(p)
            added.append(p)

    if not added:
        return False

    fm["related"] = sorted(related)
    new_fm_block = render_frontmatter(fm)

    # Update Relations section
    relations_re = re.compile(r"(## Relations\n)(.*?)(\n##|\Z)", re.DOTALL)
    m = relations_re.search(body)
    if m:
        old_relations_body = m.group(2).rstrip()
        # Strip placeholder text
        if "*(No cross-references yet — stub.)*" in old_relations_body:
            existing_lines = []
        else:
            existing_lines = [l for l in old_relations_body.splitlines()
                              if l.strip().startswith("- @")]

        new_lines = list(existing_lines)
        for slug in hub_slugs_for_source:
            link_path = f"concepts/{slug}.md"
            label = HUBS[slug]["noun"]
            bullet = f"- @{link_path} — {label} corpus-index hub (Q 2026-04-27)"
            if not any(link_path in l for l in new_lines):
                new_lines.append(bullet)

        # Sort by path within the bullets (canonical D-style alphabetical)
        new_lines_sorted = sorted(new_lines, key=lambda l: l.lower())
        new_body = "\n".join(new_lines_sorted) + "\n"
        new_relations = m.group(1) + "\n" + new_body
        body = body[:m.start()] + new_relations + body[m.end()-len(m.group(3)):]
    else:
        # No Relations section — prepend one
        body = "\n## Relations\n\n" + "\n".join(
            f"- @concepts/{slug}.md — {HUBS[slug]['noun']} corpus-index hub (Q 2026-04-27)"
            for slug in hub_slugs_for_source
        ) + "\n\n" + body.lstrip()

    src_path.write_text(new_fm_block + body)
    return True


def main():
    members = collect_members()
    print("Members per hub:")
    for hub, files in members.items():
        print(f"  {hub}: {len(files)}")

    # Build hubs
    print("\nWriting hub pages:")
    for hub_tag, files in members.items():
        build_hub(hub_tag, files)

    # Build inverse map: source -> [hub_slugs]
    src_to_hubs = defaultdict(list)
    for hub_tag, files in members.items():
        for f in files:
            src_to_hubs[f].append(HUBS[hub_tag]["slug"])

    print(f"\nUpdating {len(src_to_hubs)} source pages with bidirectional backlinks:")
    updated = 0
    for src_name, slugs in sorted(src_to_hubs.items()):
        path = SOURCES / src_name
        if add_hub_to_source(path, slugs):
            updated += 1
    print(f"Updated {updated} sources.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
