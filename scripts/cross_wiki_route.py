#!/usr/bin/env python3
"""Cross-wiki routing helper.

Creates stub pages or briefs in a target wiki when off-topic content is found
during ingest. The LLM makes the routing decision; this script executes the
mechanical work.

Usage:
  python3 scripts/cross_wiki_route.py \\
    --target-wiki seo-wiki \\
    --source-wiki osint-wiki \\
    --type page \\
    --title "Local SEO for Barbershops" \\
    --slug "local-seo-barbershops" \\
    --category concepts \\
    --backlink-page "sources/some-paper.md" \\
    --content-stdin <<< "## Narrative\n\nContent here..."
"""

import argparse
import os
import re
import sys
from datetime import date
from pathlib import Path

TODAY = date.today().isoformat()

# Resolve this script's repo root (OSINT WORKSPACE)
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent

# ---------------------------------------------------------------------------
# Alias resolution
# ---------------------------------------------------------------------------

def _find_claude_md():
    """Return the OSINT CLAUDE.md path (canonical alias source)."""
    return REPO_ROOT / "CLAUDE.md"


def load_wiki_aliases(claude_md_path=None):
    """Parse CLAUDE.md 'Related Wikis' table for alias -> absolute wiki path.

    Returns dict: alias (str) -> Path to that wiki's wiki/ directory.
    """
    if claude_md_path is None:
        claude_md_path = _find_claude_md()
    aliases = {}
    if not claude_md_path.exists():
        return aliases
    text = claude_md_path.read_text(errors="replace")
    # Match the Related Wikis table rows
    table_re = re.compile(
        r"^\|\s*`([a-z0-9_-]+)`\s*\|\s*`?([^`\n|]+)`?\s*\|",
        re.MULTILINE
    )
    for m in table_re.finditer(text):
        alias = m.group(1).strip()
        path_str = m.group(2).strip().rstrip("/")
        wiki_path = Path(path_str)
        if wiki_path.is_dir():
            aliases[alias] = wiki_path
        elif (wiki_path / "wiki").is_dir():
            aliases[alias] = wiki_path / "wiki"
        elif (wiki_path.parent / "wiki").is_dir():
            aliases[alias] = wiki_path.parent / "wiki"
    return aliases


# ---------------------------------------------------------------------------
# File creation
# ---------------------------------------------------------------------------

PAGE_TEMPLATE = """---
title: {title}
type: {page_type}
tags: []
keywords: []
related: []
maturity: draft
created: {date}
updated: {date}
cross-wiki-source: @{source_alias}/{backlink_page}
---

# {title}

## Relations

- @{source_alias}/{backlink_page}  (cross-wiki source)

## Raw Concept

Cross-wiki stub routed from `@{source_alias}/{backlink_page}` during ingest.
What prompted this page + which sources synthesize into it — fill in on next
ingest pass.

## Narrative

{body}
"""

BRIEF_TEMPLATE = """---
title: {title}
type: brief
tags: [cross-wiki-route]
created: {date}
updated: {date}
cross-wiki-source: @{source_alias}/{backlink_page}
---

# {title}

## Target

{target_wiki} wiki — for integration into the {category} layer.

## Summary

Cross-wiki brief routed from `@{source_alias}/{backlink_page}`. The source
contains content relevant to this wiki's domain but was ingested into
another wiki.

## Body

{body}

## Sources

- @{source_alias}/{backlink_page}  (cross-wiki source)
"""


def create_page(target_wiki_path, category, slug, title, source_alias,
                backlink_page, body_content, force=False):
    """Create a wiki page: {target}/wiki/{category}/{slug}.md

    Returns the created Path, or None if it already exists and --force not set.
    """
    page_type = "source" if category == "sources" else \
                "entity" if category in ("entities",) else "concept"

    page_path = target_wiki_path / category / f"{slug}.md"
    if page_path.exists() and not force:
        print(f"ERROR: {page_path} already exists. Use --force to overwrite.")
        return None

    # Ensure directory exists
    page_path.parent.mkdir(parents=True, exist_ok=True)

    content = PAGE_TEMPLATE.format(
        title=title,
        page_type=page_type,
        date=TODAY,
        source_alias=source_alias,
        backlink_page=backlink_page,
        body=body_content.strip() or "_Stub — fill in on next ingest pass._"
    )
    page_path.write_text(content)
    print(f"  Created page: {page_path}")
    return page_path


def create_brief(target_wiki_path, slug, title, source_alias, backlink_page,
                 body_content, category="concepts", force=False):
    """Create a brief: {target}/briefs/{YYYY-MM-DD}_{slug}.md"""
    briefs_dir = target_wiki_path.parent / "briefs"
    briefs_dir.mkdir(parents=True, exist_ok=True)

    brief_path = briefs_dir / f"{TODAY}_{slug}.md"
    if brief_path.exists() and not force:
        print(f"ERROR: {brief_path} already exists. Use --force to overwrite.")
        return None

    content = BRIEF_TEMPLATE.format(
        title=title,
        date=TODAY,
        source_alias=source_alias,
        backlink_page=backlink_page,
        target_wiki=os.path.basename(target_wiki_path.parent),
        category=category,
        body=body_content.strip() or "_Fill in on review._"
    )
    brief_path.write_text(content)
    print(f"  Created brief: {brief_path}")
    return brief_path


# ---------------------------------------------------------------------------
# Index.md update
# ---------------------------------------------------------------------------

def _find_section_end(lines, start_idx, section_name):
    """Find the last list-item line in a section before the next ## header or EOF.

    Returns the line index to insert BEFORE (after the last list item),
    or None if the section wasn't found.
    """
    in_section = False
    last_content_line = None
    in_subsection = False

    for i in range(start_idx, len(lines)):
        line = lines[i]
        stripped = line.strip()

        # Next top-level section ends our section
        if stripped.startswith("## ") and not stripped.startswith("### "):
            if in_section:
                # Check if we were in a subsection — need to insert
                # after the last subsection's items
                break
            # Check if this is our target section
            if stripped.lstrip("# ").startswith(section_name):
                in_section = True
        elif in_section:
            # Track the last non-empty, non-header content line
            if stripped.startswith("- ") or stripped and not stripped.startswith("#"):
                last_content_line = i
            # Subsection headers (### ) don't break; we're still in the section
            elif stripped.startswith("### "):
                in_subsection = True
                pass  # Still in section, just in a subsection now

    if last_content_line is not None:
        return last_content_line + 1  # insert after this line
    elif in_section:
        # Section exists but is empty (only header, no items yet)
        for i in range(start_idx, len(lines)):
            if lines[i].strip().startswith(f"## {section_name}"):
                return i + 1
    return None


def append_to_index(target_wiki_path, category, slug, title):
    """Append a row to the target wiki's index.md in the appropriate section.

    Handles varied index.md formats across the four wikis.
    """
    index_path = target_wiki_path / "index.md"
    if not index_path.exists():
        print(f"  WARNING: {index_path} not found — skipping index update")
        return

    lines = index_path.read_text().splitlines(keepends=True)

    # Map category to section header
    section_map = {
        "sources": "Sources",
        "entities": "Entities",
        "concepts": "Concepts",
    }
    section_name = section_map.get(category, "Concepts")

    # Format the row — keep it simple and consistent
    row = f"- [{title}]({category}/{slug}.md) — cross-wiki stub routed from ingest — `cross-wiki`\n"

    # Find section header and insert at end of section
    insert_at = None
    for i, line in enumerate(lines):
        if line.strip() == f"## {section_name}":
            insert_at = _find_section_end(lines, i, section_name)
            break

    if insert_at is None:
        # Section not found — append to end of file with section header
        print(f"  WARNING: ## {section_name} section not found in index.md — appending")
        lines.append(f"\n## {section_name}\n\n")
        lines.append(row)
    else:
        lines.insert(insert_at, row)

    index_path.write_text("".join(lines))
    print(f"  Updated index: {index_path} → {section_name} section")


# ---------------------------------------------------------------------------
# Log.md update
# ---------------------------------------------------------------------------

def append_to_log(target_wiki_path, title, slug, category, source_alias,
                   backlink_page):
    """Append an entry to the target wiki's log.md."""
    log_path = target_wiki_path / "log.md"
    if not log_path.exists():
        log_path.write_text("# Wiki Log\n\n")
        print(f"  Created log.md: {log_path}")

    entry = (
        f"\n## [{TODAY}] cross-wiki route | {title}\n\n"
        f"Cross-wiki stub routed from `@{source_alias}/{backlink_page}`.\n"
        f"- Created wiki/{category}/{slug}.md (stub)\n"
    )

    with open(log_path, "a") as f:
        f.write(entry)
    print(f"  Appended log: {log_path}")


# ---------------------------------------------------------------------------
# Backlink — add reciprocal link to the source page
# ---------------------------------------------------------------------------

def add_backlink(source_wiki_path, backlink_page, target_alias, category, slug):
    """Add reciprocal @target-alias/... link to the source page's ## Relations section."""
    page_path = source_wiki_path / backlink_page
    if not page_path.exists():
        print(f"  WARNING: source page {page_path} not found — skipping backlink")
        return

    text = page_path.read_text()
    backlink = f"@{target_alias}/{category}/{slug}.md"

    # Check if backlink already exists
    if backlink in text:
        print(f"  Backlink already present in {backlink_page}")
        return

    # Find ## Relations section
    relations_re = re.compile(r"^(## Relations\n)", re.MULTILINE)
    new_line = f"- {backlink}  (cross-wiki stub)\n"

    if relations_re.search(text):
        # Insert after the Relations header
        updated = relations_re.sub(f"\\1{new_line}", text, count=1)
    else:
        # No Relations section — add one after frontmatter
        # Find end of frontmatter (second ---)
        parts = text.split("---\n", 2)
        if len(parts) >= 3:
            updated = (
                f"{parts[0]}---\n{parts[1]}---\n\n"
                f"## Relations\n\n{new_line}\n"
                f"{parts[2]}"
            )
        else:
            # No frontmatter — prepend Relations at top
            updated = f"## Relations\n\n{new_line}\n{text}"

    page_path.write_text(updated)
    print(f"  Added backlink to {backlink_page}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Cross-wiki routing helper — creates pages or briefs in a target wiki.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("--target-wiki", required=True,
                        help="Alias of the target wiki (e.g., seo-wiki, image-gen-wiki)")
    parser.add_argument("--source-wiki", required=True,
                        help="Alias of the source wiki (e.g., osint-wiki)")
    parser.add_argument("--type", required=True, choices=["page", "brief"],
                        help="Create a wiki page or a brief")
    parser.add_argument("--title", required=True,
                        help="Human-readable page title")
    parser.add_argument("--slug", required=True,
                        help="URL-safe filename slug (without .md)")
    parser.add_argument("--category", default="concepts",
                        choices=["sources", "entities", "concepts"],
                        help="Wiki category (default: concepts)")
    parser.add_argument("--backlink-page", required=True,
                        help="Path to the source page relative to source wiki/ (e.g., sources/foo.md)")
    parser.add_argument("--force", action="store_true",
                        help="Overwrite existing files")
    parser.add_argument("--no-backlink", action="store_true",
                        help="Skip adding reciprocal backlink to source page")
    parser.add_argument("--no-index", action="store_true",
                        help="Skip updating target wiki index.md")
    parser.add_argument("--no-log", action="store_true",
                        help="Skip updating target wiki log.md")

    args = parser.parse_args()

    # Load aliases (try OSINT CLAUDE.md first, use it as canonical)
    aliases = load_wiki_aliases()

    # Validate aliases
    if args.target_wiki not in aliases:
        print(f"ERROR: target-wiki '{args.target_wiki}' not found in CLAUDE.md Related Wikis table.")
        print(f"  Known aliases: {', '.join(sorted(aliases.keys()))}")
        sys.exit(1)

    if args.source_wiki not in aliases:
        print(f"ERROR: source-wiki '{args.source_wiki}' not found in CLAUDE.md Related Wikis table.")
        print(f"  Known aliases: {', '.join(sorted(aliases.keys()))}")
        sys.exit(1)

    target_wiki_path = aliases[args.target_wiki]
    source_wiki_path = aliases[args.source_wiki]

    print(f"Cross-wiki route: @{args.source_wiki} → @{args.target_wiki}")
    print(f"  Source: {source_wiki_path}")
    print(f"  Target: {target_wiki_path}")
    print(f"  Type:   {args.type}")

    # Read content from stdin
    body_content = sys.stdin.read().strip() if not sys.stdin.isatty() else ""
    if not body_content and args.type == "brief":
        print("WARNING: no content provided via stdin — brief will be minimal")

    # Create the page or brief
    if args.type == "page":
        result = create_page(
            target_wiki_path, args.category, args.slug, args.title,
            args.source_wiki, args.backlink_page, body_content,
            force=args.force
        )
        if result is None:
            sys.exit(1)

        # Update index.md
        if not args.no_index:
            append_to_index(target_wiki_path, args.category, args.slug, args.title)

        # Update log.md
        if not args.no_log:
            append_to_log(target_wiki_path, args.title, args.slug, args.category,
                         args.source_wiki, args.backlink_page)

    else:  # brief
        result = create_brief(
            target_wiki_path, args.slug, args.title,
            args.source_wiki, args.backlink_page, body_content,
            category=args.category, force=args.force
        )
        if result is None:
            sys.exit(1)
        # Briefs don't touch index.md or log.md

    # Add reciprocal backlink to source page
    if not args.no_backlink:
        add_backlink(source_wiki_path, args.backlink_page,
                    args.target_wiki, args.category, args.slug)

    print("\nDone.")


if __name__ == "__main__":
    main()
