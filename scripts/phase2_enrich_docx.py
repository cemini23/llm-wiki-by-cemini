#!/usr/bin/env python3
"""Enrich 9 promoted docx source stubs with real narrative + clean stale tags."""
import json
import re
from datetime import date
from pathlib import Path

WIKI = Path("/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki")
TODAY = date.today().isoformat()

manifest = json.loads(Path("/tmp/phase1_agent4_unblocked_docx.json").read_text())
by_slug = {e["slug"]: e for e in manifest.get("completed_sources", [])}

UNBLOCKED = [
    "3-10-cryptographic-research",
    "3-18-crypto-integration-technical-audit",
    "3-19-langgraph-scatter-gather-financial-analysis",
    "3-19-ip-sale-research",
    "3-19-telegram-discord-research",
    "3-19-compliance-research",
    "3-19-kalshi-trading-strategy-research",
    "trading-playbook-research",
    "forex-research-3-18",
]

for slug in UNBLOCKED:
    path = WIKI / "sources" / f"{slug}.md"
    if not path.exists():
        print(f"MISSING: {slug}")
        continue
    entry = by_slug.get(slug)
    if not entry:
        print(f"NO MANIFEST ENTRY: {slug}")
        continue

    text = path.read_text()

    # 1. Remove unread-stub from tags
    text = re.sub(r"\bunread-stub,\s*", "", text)
    text = re.sub(r",\s*unread-stub\b", "", text)
    text = re.sub(r"\bunread-stub\b", "", text)

    # 2. Replace Narrative section with synthesized content
    abstract = entry.get("abstract", "").strip()
    findings = entry.get("key_findings", []) or []
    entities_list = entry.get("entities", []) or []
    concepts_list = entry.get("concepts", []) or []

    findings_md = "\n".join(f"- {f}" for f in findings) if findings else "- *(none captured)*"
    entities_str = ", ".join(entities_list) if entities_list else "*(none)*"
    concepts_str = ", ".join(concepts_list) if concepts_list else "*(none)*"

    new_narrative = f"""## Narrative

### Abstract
{abstract}

### Key findings
{findings_md}

### Entities referenced
{entities_str}

### Concepts covered
{concepts_str}
"""

    # Replace existing Narrative block
    nar_re = re.compile(r"## Narrative\n.*?(?=\n## |\Z)", re.DOTALL)
    text = nar_re.sub(new_narrative.rstrip() + "\n", text, count=1)

    # 3. Bump updated
    text = re.sub(r"^updated: .*$", f"updated: {TODAY}", text, count=1, flags=re.MULTILINE)

    path.write_text(text)
    print(f"enriched: {slug}")

print("Done.")
