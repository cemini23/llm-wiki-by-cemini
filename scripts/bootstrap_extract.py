#!/usr/bin/env python3
"""
Extract first ~3 pages / first ~2000 chars of each PDF/docx/md in the research corpus.
Dump JSON with filename + extracted text to /tmp/bootstrap_corpus.json so we can
process stubs in batches without re-reading files.
"""
import json
import os
import re
from pathlib import Path

CORPUS = Path("/Users/claudiobarone/Desktop/OSINT WORKSPACE/research for cemini")
OUT = Path("/tmp/bootstrap_corpus.json")

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
        text = "\n".join(paras)
        return {"pages": None, "text": text[:6000]}
    except Exception as e:
        return {"pages": None, "text": "", "error": str(e)}

def extract_md(path):
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
        return {"pages": None, "text": text[:6000]}
    except Exception as e:
        return {"pages": None, "text": "", "error": str(e)}

results = []
files = sorted(CORPUS.iterdir())
for i, f in enumerate(files):
    if not f.is_file():
        continue
    ext = f.suffix.lower()
    if ext == ".pdf":
        data = extract_pdf(f)
        kind = "pdf"
    elif ext == ".docx":
        data = extract_docx(f)
        kind = "docx"
    elif ext == ".md":
        data = extract_md(f)
        kind = "md"
    else:
        continue
    results.append({
        "filename": f.name,
        "kind": kind,
        "size": f.stat().st_size,
        "pages": data.get("pages"),
        "text": data.get("text", ""),
        "error": data.get("error"),
    })
    if (i+1) % 25 == 0:
        print(f"  processed {i+1}/{len(files)}")

OUT.write_text(json.dumps(results, indent=2, ensure_ascii=False))
print(f"Wrote {len(results)} records to {OUT}")
