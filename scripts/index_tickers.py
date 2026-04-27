#!/usr/bin/env python3
"""Convert Gemini Deep Research docx ticker reports into wiki/entities/tickers/<symbol>.md
entity pages. Preserves structure (headings, paragraphs, lists, tables) as markdown."""

import re
import shutil
from pathlib import Path
from datetime import date
import docx

INBOX = Path("/Users/claudiobarone/Desktop/OSINT WORKSPACE/research to be indexed")
CORPUS = Path("/Users/claudiobarone/Desktop/OSINT WORKSPACE/research for cemini")
TICKERS_DIR = Path("/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki/entities/tickers")
TODAY = "2026-04-27"

# ticker metadata (category from ticker-watchlist.md; extended 2026-04-24 for ASTS/GLW/INTC/PL)
CATEGORY = {
    "SPY": "indices", "QQQ": "indices", "IWM": "indices",
    "AAPL": "mega_cap", "MSFT": "mega_cap", "NVDA": "mega_cap",
    "AMZN": "mega_cap", "META": "mega_cap", "GOOGL": "mega_cap",
    "INTC": "mega_cap",
    "TSLA": "high_beta", "AMD": "high_beta", "SMCI": "high_beta",
    "PLTR": "high_beta", "AVGO": "high_beta",
    "COIN": "crypto_proxies", "MSTR": "crypto_proxies", "MARA": "crypto_proxies",
    "JPM": "financials", "BAC": "financials", "GS": "financials",
    "DIS": "consumer_tech", "NFLX": "consumer_tech", "UBER": "consumer_tech",
    "BTC": "crypto_native", "ETH": "crypto_native", "SOL": "crypto_native",
    "DOGE": "crypto_native", "ADA": "crypto_native", "AVAX": "crypto_native", "LINK": "crypto_native",
    "ASTS": "space_tech", "PL": "space_tech",
    "GLW": "industrials",
    "SOFI": "fintech",
}

def para_to_md(p):
    """Convert a docx paragraph to markdown line(s). Style-aware: headings, lists."""
    text = p.text.strip()
    if not text:
        return ""
    style = p.style.name if p.style else "Normal"
    if style == "Heading 1":
        return f"# {text}"
    if style == "Heading 2":
        return f"## {text}"
    if style == "Heading 3":
        return f"### {text}"
    if style == "Heading 4":
        return f"#### {text}"
    if style in ("List Bullet", "List Bullet 2", "List Bullet 3"):
        return f"- {text}"
    if style in ("List Number", "List Number 2", "List Number 3"):
        return f"1. {text}"
    # default: paragraph
    return text

def table_to_md(table):
    """Convert a docx table to markdown pipe table."""
    rows = []
    for row in table.rows:
        cells = [cell.text.strip().replace("\n", " ").replace("|", "\\|") for cell in row.cells]
        rows.append(cells)
    if not rows:
        return ""
    header = rows[0]
    out = ["| " + " | ".join(header) + " |",
           "|" + "|".join("---" for _ in header) + "|"]
    for r in rows[1:]:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out)

def iter_block_items(document):
    """Yield paragraphs + tables in document order (docx API doesn't interleave by default)."""
    from docx.oxml.ns import qn
    from docx.table import Table
    from docx.text.paragraph import Paragraph
    parent = document.element.body
    for child in parent.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, document)
        elif child.tag == qn("w:tbl"):
            yield Table(child, document)

def extract_markdown(docx_path):
    d = docx.Document(str(docx_path))
    parts = []
    for block in iter_block_items(d):
        if hasattr(block, "text") and hasattr(block, "style"):  # paragraph
            md = para_to_md(block)
            if md:
                parts.append(md)
        else:  # table
            md = table_to_md(block)
            if md:
                parts.append("\n" + md + "\n")
    # stitch: blank line between adjacent different-level blocks
    out = []
    prev = ""
    for part in parts:
        if not part:
            continue
        if out:
            out.append("")  # blank line between
        out.append(part)
        prev = part
    return "\n".join(out)

def parse_company_name_from_h1(md):
    """Extract company name from the first H1 heading."""
    m = re.search(r"^#\s+.*?:\s*(.+?)(?:\s*\((.+?)\))?\s*$", md, re.MULTILINE)
    if m:
        return m.group(1).strip(), (m.group(2).strip() if m.group(2) else None)
    return None, None

def build_entity_page(ticker, docx_path):
    md = extract_markdown(docx_path)
    # extract company name + ticker from first H1 if we can
    company, ticker_parens = parse_company_name_from_h1(md)

    # Preserve the authored content verbatim under "Narrative", wrap with frontmatter + Relations + Raw Concept
    cat = CATEGORY.get(ticker, "unknown")
    tags = ["ticker-report", "gemini-deep-research", "entity", cat, ticker.lower()]

    # tweak the report's H1 down a level since the page has its own implied H1
    # (but leaving it preserves structure; we'll demote all headings by 1)
    # Actually — simpler: keep the original structure inside Narrative and omit a new H1.
    # The frontmatter `title:` field is the page title.

    title = f"{company} ({ticker})" if company else ticker

    frontmatter = (
        "---\n"
        f"title: {title}\n"
        "type: entity\n"
        f"tags: [{', '.join(tags)}]\n"
        f"category: {cat}\n"
        f"ticker: {ticker}\n"
        "related:\n"
        "  - entities/ticker-watchlist.md\n"
        "maturity: validated\n"
        "report_source: gemini-deep-research\n"
        f"report_date: {TODAY}\n"
        f"created: {TODAY}\n"
        f"updated: {TODAY}\n"
        "---\n\n"
    )

    header = (
        "## Relations\n\n"
        "- @entities/ticker-watchlist.md — parent watchlist page\n\n"
        "## Raw Concept\n\n"
        f"- **Ticker**: {ticker}\n"
        f"- **Category**: {cat}\n"
        f"- **Report source**: Gemini Deep Research (user-commissioned template)\n"
        f"- **Report date**: {TODAY}\n"
        f"- **Original file**: research for cemini/{docx_path.name} (moved from inbox)\n"
        "- **Template sections**: Business Overview · Competitive Landscape · Financial Profile · Recent Events · Forward Catalysts · Analyst & Sell-Side Context\n"
        "- **Maturity**: validated (institutional-grade template; content reflects author/model synthesis as of report date)\n\n"
        "## Narrative\n\n"
        "*Full Gemini Deep Research report follows, preserved verbatim. Headings demoted by one level so page TOC is consistent.*\n\n"
    )

    # demote all heading levels by one so the report's H1 becomes H2, etc.
    def demote(match):
        hashes = match.group(1)
        return "#" + hashes + " "
    md_demoted = re.sub(r"^(#+)\s+", demote, md, flags=re.MULTILINE)

    return frontmatter + header + md_demoted + "\n"

# --- run ---
results = []
for f in sorted(INBOX.glob("*.docx")):
    # parse ticker from filename: "AAPL 4_23.docx" -> "AAPL"
    m = re.match(r"([A-Z]+)\s", f.name)
    if not m:
        print(f"  SKIP unknown filename pattern: {f.name}")
        continue
    ticker = m.group(1)
    if ticker not in CATEGORY:
        print(f"  SKIP {f.name} — ticker {ticker} not in watchlist")
        continue
    page_md = build_entity_page(ticker, f)
    out_path = TICKERS_DIR / f"{ticker.lower()}.md"
    out_path.write_text(page_md)
    print(f"  WROTE {out_path.relative_to(Path('/Users/claudiobarone/Desktop/OSINT WORKSPACE'))} ({len(page_md)} bytes)")
    # move source docx to canonical corpus folder
    dest = CORPUS / f.name
    if dest.exists():
        print(f"    (destination exists — not overwriting {dest.name})")
    else:
        shutil.move(str(f), str(dest))
        print(f"    moved source → {dest.relative_to(Path('/Users/claudiobarone/Desktop/OSINT WORKSPACE'))}")
    results.append((ticker, out_path.name))

print(f"\nIndexed {len(results)} tickers: {[t for t, _ in results]}")
