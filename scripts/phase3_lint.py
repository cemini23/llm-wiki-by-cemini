#!/usr/bin/env python3
"""Phase 3 lint — orphans, bidirectional gaps, stale maturity."""
import re
from pathlib import Path

WIKI = Path("/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki")

fm_re = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

def parse_page(path: Path) -> dict:
    text = path.read_text()
    m = fm_re.match(text)
    if not m:
        return {"path": path, "related": [], "maturity": None, "type": None, "error": "no-frontmatter"}
    fm = m.group(1)
    related: list[str] = []
    in_related = False
    maturity = None
    type_ = None
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
        if ln.startswith("maturity:"):
            maturity = ln.split(":", 1)[1].strip()
        if ln.startswith("type:"):
            type_ = ln.split(":", 1)[1].strip()
    return {"path": path, "related": related, "maturity": maturity, "type": type_}

# 1. Collect all pages inside wiki/
all_pages: dict[str, dict] = {}  # rel_path_str -> info
for p in WIKI.rglob("*.md"):
    if p.name in {"index.md", "log.md"}:
        continue
    rel = str(p.relative_to(WIKI))
    info = parse_page(p)
    info["rel"] = rel
    all_pages[rel] = info

print(f"Inventoried {len(all_pages)} pages")

# 2. Inbound-link counts + bidirectional check
inbound: dict[str, set[str]] = {p: set() for p in all_pages}
for rel, info in all_pages.items():
    for ref in info["related"]:
        if ref in inbound:
            inbound[ref].add(rel)
        # missing target tracked below

# 3. Orphans: entity/concept pages with no inbound refs
orphan_entities_concepts = []
for rel, info in all_pages.items():
    if info["type"] in ("entity", "concept") and not inbound[rel]:
        orphan_entities_concepts.append(rel)

print(f"\nOrphan entity/concept pages (zero inbound): {len(orphan_entities_concepts)}")
for o in sorted(orphan_entities_concepts):
    print(f"  {o}")

# 4. Bidirectional gaps
gaps = []
for rel, info in all_pages.items():
    for ref in info["related"]:
        if ref in all_pages:
            other_refs = all_pages[ref]["related"]
            if rel not in other_refs:
                gaps.append((rel, ref))

print(f"\nBidirectional gaps (A lists B but B does not list A): {len(gaps)}")
for a, b in gaps[:40]:
    print(f"  {a}  →  {b}")
if len(gaps) > 40:
    print(f"  ... and {len(gaps)-40} more")

# 5. Dangling refs — related targets that don't exist
dangling = []
for rel, info in all_pages.items():
    for ref in info["related"]:
        if ref not in all_pages:
            dangling.append((rel, ref))

print(f"\nDangling refs (related target does not exist): {len(dangling)}")
for a, b in dangling[:40]:
    print(f"  {a}  →  {b}")
if len(dangling) > 40:
    print(f"  ... and {len(dangling)-40} more")

# 6. Stale tags — any page still tagged unread-stub
stale_tag = []
for p in WIKI.rglob("*.md"):
    if p.name in {"index.md", "log.md"}:
        continue
    text = p.read_text()
    m = fm_re.match(text)
    if not m:
        continue
    fm = m.group(1)
    # find tags line
    tags_m = re.search(r"^tags:\s*\[([^\]]*)\]", fm, re.MULTILINE)
    mat_m = re.search(r"^maturity:\s*(\w+)", fm, re.MULTILINE)
    if tags_m and "unread-stub" in tags_m.group(1):
        if mat_m and mat_m.group(1) == "validated":
            stale_tag.append(str(p.relative_to(WIKI)))

print(f"\nValidated pages still tagged 'unread-stub': {len(stale_tag)}")
for s in stale_tag[:20]:
    print(f"  {s}")
