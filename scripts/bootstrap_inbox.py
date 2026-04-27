#!/usr/bin/env python3
"""
Targeted stub bootstrap for the `research to be indexed/` inbox.

Differs from bootstrap_extract.py + generate_stubs.py (which scan the entire
corpus and would re-write all 229 existing stubs): this script processes only
inbox files, moves them into `research for cemini/`, and emits one
`wiki/sources/<slug>.md` stub per file using the same template.

Usage (from workspace root):
    python3 scripts/bootstrap_inbox.py

Skips:
  - .DS_Store and other dotfiles
  - non-PDF/docx/md files (warn and leave in inbox)
  - files whose target stub already exists (idempotent — leaves source in place)
"""
import json
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path("/Users/claudiobarone/Desktop/OSINT WORKSPACE")
INBOX = ROOT / "research to be indexed"
CORPUS = ROOT / "research for cemini"
WIKI_SOURCES = ROOT / "wiki/sources"
TODAY = "2026-04-27"

# --- extractors (mirror bootstrap_extract.py) -------------------------------

def extract_pdf(path):
    try:
        import pypdf
        reader = pypdf.PdfReader(str(path))
        n = len(reader.pages)
        pages_text = []
        for i in range(min(3, n)):
            try:
                pages_text.append(reader.pages[i].extract_text() or "")
            except Exception:
                pages_text.append("")
        return {"pages": n, "text": "\n".join(pages_text)[:6000]}
    except Exception as e:
        return {"pages": None, "text": "", "error": str(e)}

def extract_docx(path):
    try:
        import docx
        d = docx.Document(str(path))
        paras = [p.text for p in d.paragraphs if p.text.strip()]
        return {"pages": None, "text": "\n".join(paras)[:6000]}
    except Exception as e:
        return {"pages": None, "text": "", "error": str(e)}

def extract_md(path):
    try:
        return {"pages": None, "text": path.read_text(encoding="utf-8", errors="ignore")[:6000]}
    except Exception as e:
        return {"pages": None, "text": "", "error": str(e)}

# --- helpers (mirror generate_stubs.py) -------------------------------------

def slugify(stem):
    s = stem.lower()
    s = s.replace(":", "-")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s

def extract_title(text, filename):
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
        if len(l) < 10 or len(l) > 220:
            continue
        candidates.append(l)
        if len(candidates) >= 3:
            break
    if not candidates:
        return filename
    best = candidates[0]
    for c in candidates[1:2]:
        if 30 <= len(c) <= 180 and len(c) > len(best):
            best = c
    if len(candidates) >= 2 and len(candidates[0]) < 80 and not candidates[0].endswith("."):
        joined = candidates[0] + " " + candidates[1]
        if len(joined) < 200 and not candidates[1][0].islower():
            best = joined
    return best.strip().rstrip(".,:;")

def extract_summary(text):
    if not text:
        return ""
    t = text
    m = re.search(r"\bAbstract\b[:\-—\s]*", t, re.IGNORECASE)
    if m:
        t = t[m.end():]
    t = re.sub(r"\s+", " ", t).strip()
    sents = re.split(r"(?<=[.!?])\s+", t)
    return " ".join(sents[:2])[:360].strip()

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
    for name, pat in CLUSTERS:
        if re.search(pat, text or "", re.IGNORECASE):
            return name
    return "uncategorized"

def keywords_for(text, title, max_k=8):
    blob = (title + " " + (text or ""))[:2000]
    words = re.findall(r"\b[A-Z][A-Za-z0-9\-]{2,}\b", blob)
    stop = {"The", "This", "These", "That", "Abstract", "Introduction",
            "Figure", "Table", "Section", "Chapter", "However",
            "Moreover", "Furthermore", "Therefore"}
    seen = []
    for w in words:
        if w in stop or w.lower() in [s.lower() for s in seen]:
            continue
        seen.append(w)
        if len(seen) >= max_k:
            break
    return seen

# --- emit -------------------------------------------------------------------

def main():
    if not INBOX.exists():
        print(f"Inbox missing: {INBOX}", file=sys.stderr)
        return 1
    WIKI_SOURCES.mkdir(exist_ok=True)
    CORPUS.mkdir(exist_ok=True)

    inbox_files = sorted(f for f in INBOX.iterdir()
                         if f.is_file() and not f.name.startswith("."))
    if not inbox_files:
        print("Inbox is empty.")
        return 0

    rows = []  # (cluster, slug, title, summary, kind, filename)
    skipped = []

    for src in inbox_files:
        ext = src.suffix.lower()
        if ext == ".pdf":
            data, kind = extract_pdf(src), "pdf"
        elif ext == ".docx":
            data, kind = extract_docx(src), "docx"
        elif ext == ".md":
            data, kind = extract_md(src), "md"
        else:
            print(f"  skip non-supported: {src.name}", file=sys.stderr)
            skipped.append(src.name)
            continue

        text = data.get("text", "") or ""
        title = extract_title(text, src.name)
        summary = extract_summary(text)
        cluster = cluster_for(text + " " + title)
        keywords = keywords_for(text, title)
        pages = data.get("pages")
        pages_str = f"{pages}p" if pages else "—"

        stem = src.stem
        slug = slugify(stem) or f"file-{abs(hash(src.name))%100000}"
        target_md = WIKI_SOURCES / f"{slug}.md"
        if target_md.exists():
            print(f"  skip (stub exists): {target_md.name}")
            skipped.append(src.name)
            continue

        tags = [kind, "unread-stub"]
        if cluster != "uncategorized":
            tags.append(cluster)

        # NOTE: we intentionally produce `related: []` here — hub backlinks
        # get added in a follow-up edit (matching the 229-stub precedent).
        frontmatter = (
            "---\n"
            f"title: {json.dumps(title, ensure_ascii=False)[1:-1]}\n"
            "type: source\n"
            f"tags: [{', '.join(tags)}]\n"
            f"keywords: [{', '.join(keywords)}]\n"
            "related: []\n"
            "maturity: draft\n"
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
            f"- **Type**: {kind.upper()}\n"
            f"- **Location**: research for cemini/{src.name}\n"
            f"- **Retrieved**: {TODAY}\n"
            f"- **Length**: {pages_str}\n"
            "- **Read status**: unread-stub\n"
            f"- **Cluster**: {cluster}\n\n"
            "## Narrative\n\n"
            f"{summary if summary else '_First-page extraction yielded no summary text. Read the source to populate._'}\n\n"
            "## Snippets\n\n"
            "*(None yet — populate on first deep read.)*\n"
        )
        target_md.write_text(frontmatter + body)

        # Move source into corpus (matches index_tickers.py convention)
        dest = CORPUS / src.name
        if dest.exists():
            print(f"  WARN: corpus already has {src.name}; not overwriting", file=sys.stderr)
        else:
            shutil.move(str(src), str(dest))

        rows.append((cluster, slug, title, summary, kind, src.name))
        print(f"  + {slug} → {cluster}")

    print(f"\nWrote {len(rows)} new stubs.")
    print(f"Skipped {len(skipped)} files.")

    by_cluster = defaultdict(list)
    for row in rows:
        by_cluster[row[0]].append(row)
    cluster_order = [c for c, _ in CLUSTERS] + ["uncategorized"]
    print("\nCluster distribution:")
    for c in cluster_order:
        if c in by_cluster:
            print(f"  {c}: {len(by_cluster[c])}")

    # Print index fragment for manual paste into wiki/index.md
    print("\n--- index fragment (alphabetical-by-title within cluster) ---")
    for c in cluster_order:
        if c not in by_cluster:
            continue
        rows_c = sorted(by_cluster[c], key=lambda r: r[2].lower())
        print(f"\n### {c}")
        for _, slug, title, summary, kind, _fn in rows_c:
            one = (summary[:140] + "…") if summary and len(summary) > 140 else (summary or "_no summary extracted_")
            print(f"- [{title}](sources/{slug}.md) — {one} — `{kind}`")

    return 0

if __name__ == "__main__":
    sys.exit(main())
