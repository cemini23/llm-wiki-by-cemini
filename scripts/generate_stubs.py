#!/usr/bin/env python3
"""
Consume /tmp/bootstrap_corpus.json, emit one wiki/sources/<slug>.md stub per record
following the source-page template in CLAUDE.md. Also emit an index fragment grouped
by topic cluster, printed to stdout for review before committing to wiki/index.md.
"""
import json
import re
from pathlib import Path
from datetime import date

CORPUS_JSON = Path("/tmp/bootstrap_corpus.json")
WIKI_SOURCES = Path("/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki/sources")
WIKI_SOURCES.mkdir(exist_ok=True)
TODAY = "2026-04-23"

# --- helpers ---

def slugify(stem):
    s = stem.lower()
    s = s.replace(":", "-")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s

def extract_title(text, filename):
    """Pull the real title from the first meaningful lines. Skip arxiv headers and
    single-word journal lines."""
    if not text:
        return filename
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    skip_prefix = (
        "arxiv:", "ieee", "acm ", "doi:", "http", "www.", "preprint",
        "submitted", "accepted", "published", "volume", "vol.", "page ",
        "chapter", "section",
    )
    skip_exact = {
        "abstract", "introduction", "executive summary", "table of contents",
        "contents", "preface", "acknowledgements", "foreword",
    }
    candidates = []
    for l in lines[:15]:
        ll = l.lower()
        if ll in skip_exact:
            continue
        if any(ll.startswith(p) for p in skip_prefix):
            continue
        if len(l) < 10:
            continue
        if len(l) > 220:
            # long paragraph — not a title
            continue
        candidates.append(l)
        if len(candidates) >= 3:
            break
    if not candidates:
        return filename
    # prefer the longest of first 2 candidates (headline often wraps)
    best = candidates[0]
    for c in candidates[1:2]:
        if 30 <= len(c) <= 180 and len(c) > len(best):
            best = c
    # Collapse title-case fragments split across two lines
    if len(candidates) >= 2 and len(candidates[0]) < 80 and not candidates[0].endswith("."):
        joined = candidates[0] + " " + candidates[1]
        if len(joined) < 200 and not candidates[1][0].islower():
            best = joined
    return best.strip().rstrip(".,:;")

def extract_summary(text):
    """First ~2 sentences, prefer content after an 'Abstract' marker."""
    if not text:
        return ""
    t = text
    m = re.search(r"\bAbstract\b[:\-—\s]*", t, re.IGNORECASE)
    if m:
        t = t[m.end():]
    # collapse whitespace
    t = re.sub(r"\s+", " ", t).strip()
    # first two sentences
    sents = re.split(r"(?<=[.!?])\s+", t)
    out = " ".join(sents[:2])[:360]
    return out.strip()

# topic cluster heuristics — conservative, keyword-based
CLUSTERS = [
    ("rl-marl", r"\b(reinforcement learning|marl|multi-agent|q-learning|policy gradient|PPO|actor-critic|bandit)\b"),
    ("llm-agents", r"\b(large language model|LLM|agentic|transformer|attention|GPT|RAG|retrieval-augmented|prompt)\b"),
    ("portfolio-strategy", r"\b(portfolio|Sharpe|risk parity|factor model|mean-variance|Kelly|allocation|rebalanc)\b"),
    ("options-derivatives", r"\b(option|derivative|Black-Scholes|implied volatility|gamma|delta hedg|variance swap)\b"),
    ("market-microstructure", r"\b(market microstructure|order book|limit order|market maker|bid-ask|latency|HFT)\b"),
    ("quant-finance", r"\b(quantitative finance|volatility|VaR|drawdown|backtest|alpha|factor|signal)\b"),
    ("ml-methods", r"\b(neural network|deep learning|CNN|RNN|LSTM|training|gradient descent|optimization)\b"),
    ("time-series", r"\b(time series|forecast|ARIMA|GARCH|stationary|seasonality|autocorrelation)\b"),
    ("crypto", r"\b(bitcoin|ethereum|blockchain|DeFi|crypto|on-chain|stablecoin)\b"),
    ("osint-geopolitics", r"\b(OSINT|geopolit|intelligence|surveillance|border|detention|ICE|DHS|FOIA|GEO Group)\b"),
    ("cemini-internal", r"\b(Cemini|QuantOS|Hetzner)\b"),
    ("audit-security", r"\b(audit|DevSecOps|security|vulnerabilit|SAST|DAST|CI/CD)\b"),
    ("infrastructure", r"\b(kubernetes|docker|terraform|infrastructure|deployment|DevOps|observability)\b"),
    ("data-engineering", r"\b(ETL|data pipeline|Kafka|Spark|warehouse|ingestion|streaming)\b"),
]

def cluster_for(text):
    t = text or ""
    for name, pat in CLUSTERS:
        if re.search(pat, t, re.IGNORECASE):
            return name
    return "uncategorized"

def tags_for(cluster, kind):
    base = [kind, "unread-stub"]
    if cluster != "uncategorized":
        base.append(cluster)
    return base

def keywords_for(text, title, max_k=8):
    """Pick capitalized or domain-distinctive words from title + first text."""
    blob = (title + " " + (text or ""))[:2000]
    # simple: find multi-letter capitalized tokens + known acronyms
    words = re.findall(r"\b[A-Z][A-Za-z0-9\-]{2,}\b", blob)
    stop = {"The", "This", "These", "That", "Abstract", "Introduction",
            "Figure", "Table", "Section", "Chapter", "However",
            "Moreover", "Furthermore", "Therefore"}
    seen = []
    for w in words:
        if w in stop:
            continue
        if w.lower() in [s.lower() for s in seen]:
            continue
        seen.append(w)
        if len(seen) >= max_k:
            break
    return seen

# --- emit ---

data = json.loads(CORPUS_JSON.read_text())
index_rows = []  # (cluster, slug, title, summary, kind)

for rec in data:
    filename = rec["filename"]
    stem = Path(filename).stem
    slug = slugify(stem)
    if not slug:
        slug = f"file-{abs(hash(filename))%100000}"
    text = rec.get("text", "") or ""
    title = extract_title(text, filename)
    summary = extract_summary(text)
    cluster = cluster_for(text + " " + title)
    tags = tags_for(cluster, rec["kind"])
    keywords = keywords_for(text, title)
    pages = rec.get("pages")
    pages_str = f"{pages}p" if pages else "—"

    # YAML-safe title: wrap in single quotes (escape internal `'` by doubling
    # per YAML spec). Necessary because raw extracted titles often contain
    # `:` characters; plain-scalar YAML interprets the second colon as a
    # mapping-key delimiter and breaks frontmatter parsing. Single-quote YAML
    # preserves smart quotes / unicode / colons verbatim.
    title_yaml = "'" + title.replace("'", "''") + "'"

    # `read_status: unread-stub` is mirrored into frontmatter (in addition to
    # the body bullet) so wiki_lint.py's section-5 ("cited but unread") check
    # sees an authoritative status without parsing free-form body.
    frontmatter = (
        "---\n"
        f"title: {title_yaml}\n"
        "type: source\n"
        f"tags: [{', '.join(tags)}]\n"
        f"keywords: [{', '.join(keywords)}]\n"
        "related: []\n"
        "maturity: draft\n"
        "read_status: unread-stub\n"
        f"created: {TODAY}\n"
        f"updated: {TODAY}\n"
        "---\n\n"
    )
    body = (
        "## Relations\n\n"
        "*(No cross-references yet — stub.)*\n\n"
        "## Raw Concept\n\n"
        f"- **Original title**: {title}\n"
        "- **Author(s)**: _unknown (stub — not yet read)_\n"
        f"- **Type**: {rec['kind'].upper()}\n"
        f"- **Location**: research for cemini/{filename}\n"
        f"- **Retrieved**: {TODAY} (date extracted from filename stem is download date, not publication date)\n"
        f"- **Length**: {pages_str}\n"
        "- **Read status**: unread-stub\n"
        f"- **Cluster**: {cluster}\n\n"
        "## Narrative\n\n"
        f"{summary if summary else '_First-page extraction yielded no summary text. Read the source to populate._'}\n\n"
        "## Snippets\n\n"
        "*(None yet — populate on first deep read.)*\n"
    )

    (WIKI_SOURCES / f"{slug}.md").write_text(frontmatter + body)
    index_rows.append((cluster, slug, title, summary, rec["kind"]))

# emit an index fragment to /tmp/index_fragment.md
from collections import defaultdict
by_cluster = defaultdict(list)
for row in index_rows:
    by_cluster[row[0]].append(row)

cluster_order = [c for c, _ in CLUSTERS] + ["uncategorized"]
fragment_lines = ["# Sources — generated fragment\n"]
for c in cluster_order:
    if c not in by_cluster:
        continue
    rows = sorted(by_cluster[c], key=lambda r: r[2].lower())
    fragment_lines.append(f"\n### {c} ({len(rows)})\n")
    for _, slug, title, summary, kind in rows:
        one_liner = (summary[:140] + "…") if summary and len(summary) > 140 else (summary or "_no summary extracted_")
        fragment_lines.append(f"- [{title}](sources/{slug}.md) — {one_liner} — `{kind}`")

Path("/tmp/index_fragment.md").write_text("\n".join(fragment_lines))

print(f"Wrote {len(index_rows)} stubs to {WIKI_SOURCES}")
print(f"Cluster distribution:")
for c in cluster_order:
    if c in by_cluster:
        print(f"  {c}: {len(by_cluster[c])}")
print(f"Index fragment → /tmp/index_fragment.md")
