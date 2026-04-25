#!/usr/bin/env python3
"""Extract a docx as plain text + heading map for deep-reading.

Prints the document with heading-level annotations ([H1], [H2], etc.) so
the calling LLM can navigate sections + cite by section name. Tables get
rendered as pipe-tables. Lists keep their bullets.
"""

import sys
from pathlib import Path
import docx
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph

def iter_block_items(document):
    parent = document.element.body
    for child in parent.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, document)
        elif child.tag == qn("w:tbl"):
            yield Table(child, document)

def emit_paragraph(p):
    text = p.text.strip()
    if not text:
        return ""
    style = p.style.name if p.style else "Normal"
    if style == "Title":
        return f"[TITLE] {text}"
    if style.startswith("Heading "):
        level = style.replace("Heading ", "")
        return f"[H{level}] {text}"
    if style in ("List Bullet", "List Bullet 2", "List Bullet 3"):
        return f"  - {text}"
    if style in ("List Number", "List Number 2", "List Number 3"):
        return f"  1. {text}"
    return text

def emit_table(t):
    rows = []
    for row in t.rows:
        cells = [c.text.strip().replace("\n", " ") for c in row.cells]
        rows.append(cells)
    if not rows:
        return ""
    out = ["[TABLE START]"]
    for r in rows:
        out.append("  | " + " | ".join(r) + " |")
    out.append("[TABLE END]")
    return "\n".join(out)

def main(path):
    d = docx.Document(path)
    parts = []
    for block in iter_block_items(d):
        if isinstance(block, Paragraph):
            t = emit_paragraph(block)
            if t:
                parts.append(t)
        elif isinstance(block, Table):
            t = emit_table(block)
            if t:
                parts.append(t)
    print("\n".join(parts))

if __name__ == "__main__":
    main(sys.argv[1])
