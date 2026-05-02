#!/usr/bin/env python3
"""Cross-document duplicate detection for link-aggregate source pages.

Detects when the same paper, repo, or tool is evaluated in multiple
link-aggregate docs. Three passes:

1. GitHub owner/repo pairs in body text (not frontmatter)
2. arXiv / OpenReview IDs in body text
3. H3 content-item headings across docs (fuzzy)
"""

import re
from collections import defaultdict
from pathlib import Path

WIKI_SOURCES = Path("wiki/sources")
LINK_PATTERNS = ["*link*.md", "*-re-*.md", "*-links*.md"]

# Topic/cluster/broker pairs that are not individual evaluated items
GENERIC_REFERENCES = {
    'k5/k6', 'k8/k9', 'rl/marl', 'kalshi/alpaca', 'torchrl/pettingzoo',
    'postgresql/timescaledb', 'cemini/captum', 'n/a', '24/7', '0/11',
    '1/2', '2/3', 'i/o', 'pub/sub', 'ci/cd', 'k5/k7', 'k6/k7',
}


def split_frontmatter_body(filepath: Path) -> tuple:
    with open(filepath) as f:
        content = f.read()
    parts = content.split("---", 2)
    if len(parts) >= 3:
        return parts[1], parts[2]
    return "", content


def extract_repos(body: str) -> set:
    """GitHub-style owner/repo from body only. Filters wiki paths and generics."""
    repos = set()
    wiki_prefixes = ('concepts/', 'entities/', 'sources/', 'briefs/',
                     'sweeps/', 'scripts/')
    path_segments = ('opt', 'research', 'author', 'services', 'agents',
                     'source', 'concept', 'entity')

    for m in re.finditer(r'(?<!\w)([A-Za-z][\w.-]+)/([A-Za-z][\w.-]+)', body):
        owner = m.group(1)
        repo = m.group(2)
        full = f"{owner}/{repo}"
        full_lower = full.lower()

        if any(full_lower.startswith(p) for p in wiki_prefixes):
            continue
        if '.' in repo and not repo.startswith('.'):
            continue
        if len(owner) < 2 or len(repo) < 2:
            continue
        if full_lower in GENERIC_REFERENCES:
            continue
        if owner.lower() in path_segments:
            continue
        repos.add(full)
    return repos


def extract_arxiv_ids(body: str) -> set:
    ids = set()
    for m in re.finditer(r'arxiv\.org/abs/(\d{4}\.\d{4,5}(?:v\d+)?)', body):
        ids.add(m.group(1).lower())
    for m in re.finditer(r'arXiv:\s*(\d{4}\.\d{4,5})', body, re.IGNORECASE):
        ids.add(m.group(1).lower())
    return ids


def extract_openreview_ids(body: str) -> set:
    ids = set()
    for m in re.finditer(r'openreview\.net/(?:forum|pdf)\?id=([a-f0-9]+)', body):
        ids.add('openreview:' + m.group(1))
    return ids


def main():
    files = set()
    for pattern in LINK_PATTERNS:
        files.update(WIKI_SOURCES.glob(pattern))
    files = sorted(files)

    print(f"Cross-doc duplicate detection — {len(files)} link-aggregate pages\n")

    # --- Pass 1: GitHub repos ---
    repo_index = defaultdict(list)
    for fp in files:
        _, body = split_frontmatter_body(fp)
        for repo in extract_repos(body):
            repo_index[repo].append(fp.name)

    # Separate true duplicates from cross-references
    repo_dupes = {}
    repo_xrefs = {}
    for repo, fnames in repo_index.items():
        if len(fnames) < 2:
            continue
        # If all but one reference are cross-links (not evaluations), flag differently
        full_evals = 0
        for fn in fnames:
            _, body = split_frontmatter_body(WIKI_SOURCES / fn)
            # Count how many times the repo appears as its own heading or table entry
            mentions = body.count(repo)
            if mentions >= 2:  # appears multiple times = likely full evaluation
                full_evals += 1
        if full_evals >= 2:
            repo_dupes[repo] = fnames
        else:
            repo_xrefs[repo] = fnames

    if repo_dupes:
        print("=" * 70)
        print("DUPLICATE EVALUATIONS (same item fully evaluated in ≥2 docs)")
        print("=" * 70)
        for repo, fnames in sorted(repo_dupes.items()):
            print(f"\n  {repo}")
            for fn in sorted(fnames):
                print(f"    → {fn}")

    if repo_xrefs:
        print(f"\n{'=' * 70}")
        print("CROSS-REFERENCES (evaluated in one doc, mentioned in others)")
        print("=" * 70)
        for repo, fnames in sorted(repo_xrefs.items()):
            print(f"\n  {repo}")
            for fn in sorted(fnames):
                print(f"    → {fn}")

    # --- Pass 2: arXiv/OpenReview IDs ---
    arxiv_index = defaultdict(list)
    for fp in files:
        _, body = split_frontmatter_body(fp)
        for aid in extract_arxiv_ids(body):
            arxiv_index[aid].append(fp.name)
        for oid in extract_openreview_ids(body):
            arxiv_index[oid].append(fp.name)

    arxiv_dupes = {a: fs for a, fs in arxiv_index.items() if len(fs) > 1}
    if arxiv_dupes:
        print(f"\n{'=' * 70}")
        print("ARXIV / OPENREVIEW ID DUPLICATES")
        print("=" * 70)
        for aid, fnames in sorted(arxiv_dupes.items()):
            print(f"\n  {aid}")
            for fn in sorted(fnames):
                print(f"    → {fn}")
    else:
        print(f"\n  No arXiv/OpenReview ID duplicates found.")

    # --- Summary ---
    print(f"\n{'=' * 70}")
    print("Summary")
    print("=" * 70)
    print(f"  Files scanned:               {len(files)}")
    print(f"  GitHub repos found (body):   {len(repo_index)}")
    print(f"  Duplicate evaluations:       {len(repo_dupes)}")
    print(f"  Cross-references only:       {len(repo_xrefs)}")
    print(f"  arXiv/OpenReview IDs:        {len(arxiv_index)}")
    print(f"  arXiv duplicates:            {len(arxiv_dupes)}")


if __name__ == "__main__":
    main()
