#!/usr/bin/env python3
"""Enrich K255 arXiv source stubs: title, Location, abstract snippet via arXiv API."""

from __future__ import annotations

import re
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "wiki" / "sources"
ATOM = "http://www.w3.org/2005/Atom"


def arxiv_ids() -> list[tuple[str, Path]]:
    out: list[tuple[str, Path]] = []
    for p in sorted(SOURCES.glob("arxiv-2609.*-2026-09-04.md")):
        m = re.search(r"arxiv-(\d+\.\d+)", p.name)
        if m:
            out.append((m.group(1), p))
    return out


def fetch_metadata(ids: list[str]) -> dict[str, dict[str, str]]:
    meta: dict[str, dict[str, str]] = {}
    chunk = 10
    for i in range(0, len(ids), chunk):
        batch = ids[i : i + chunk]
        url = f"https://export.arxiv.org/api/query?id_list={','.join(batch)}"
        with urllib.request.urlopen(url, timeout=60) as resp:
            root = ET.fromstring(resp.read())
        for entry in root.findall(f"{{{ATOM}}}entry"):
            aid_raw = entry.find(f"{{{ATOM}}}id").text.split("/abs/")[-1]
            aid = re.sub(r"v\d+$", "", aid_raw)
            title = entry.find(f"{{{ATOM}}}title").text.replace("\n", " ").strip()
            summary = entry.find(f"{{{ATOM}}}summary").text.replace("\n", " ").strip()
            meta[aid] = {"title": title, "summary": summary}
    return meta


def enrich_file(path: Path, title: str, summary: str) -> None:
    text = path.read_text(encoding="utf-8")
    pdf_name = None
    m = re.search(r"\| File \| `([^`]+)` \|", text)
    if m:
        pdf_name = m.group(1)
    if not pdf_name:
        return
    loc = f"cemini-egress-fi:/opt/cemini-bulk/research/osint/{pdf_name}"
    safe_title = title.replace('"', "'")
    text = re.sub(
        r'^title: ".*"$',
        lambda _: f'title: "{safe_title}"',
        text,
        count=1,
        flags=re.M,
    )
    if "| Location |" not in text:
        text = text.replace(
            f"| Retrieved | 2026-09-04 |",
            f"| Location | `{loc}` |\n| Retrieved | 2026-09-04 |",
        )
    snippet = summary[:280].rsplit(" ", 1)[0] + "…" if len(summary) > 280 else summary

    def _repl_snip(m: re.Match[str]) -> str:
        return f'{m.group(1)}> "{snippet}" [Source:'

    text = re.sub(
        r"(## Snippets\n\n)> .*\[Source:",
        _repl_snip,
        text,
        count=1,
        flags=re.S,
    )
    if "tags: [source, k255]" in text:
        text = text.replace("tags: [source, k255]", "tags: [arxiv, source, k255]")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    pairs = arxiv_ids()
    if not pairs:
        print("No K255 arXiv sources found")
        return
    ids = [a for a, _ in pairs]
    meta = fetch_metadata(ids)
    for aid, path in pairs:
        if aid not in meta:
            print(f"SKIP no API metadata: {aid}")
            continue
        enrich_file(path, meta[aid]["title"], meta[aid]["summary"])
        print(f"OK {path.name}")
    print(f"Enriched {len(meta)} sources")


if __name__ == "__main__":
    main()
