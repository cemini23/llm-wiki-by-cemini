#!/usr/bin/env python3
"""Cross-document duplicate detection for link-aggregate source pages.

Detects when the same paper, repo, or tool is evaluated in multiple
link-aggregate docs. Three passes:

1. GitHub owner/repo pairs in body text (not frontmatter)
2. arXiv / OpenReview IDs in body text
3. H3 content-item headings across docs (fuzzy)
"""

import re
import unicodedata
from collections import defaultdict
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"


def wiki_sources_dirs() -> list[Path]:
    """Every domain's sources/ directory.

    The federation merge put eight domains under one wiki root, so a single
    `wiki/sources` glob matches nothing. Returning the list also keeps the basename
    collisions the merge introduced from being folded together as the same file.
    """
    return sorted(p for p in [WIKI / "sources", *WIKI.glob("*/sources")] if p.is_dir())


def label(path: Path) -> str:
    """Path relative to the wiki root — `osint/sources/foo.md`, not just `foo.md`."""
    try:
        return str(path.relative_to(WIKI))
    except ValueError:
        return str(path)
LINK_PATTERNS = [
    "*link*.md", "*-re-*.md", "*-links*.md",
    "gemini-dr-wave*.md",       # Gemini Deep Research wave summaries
    "wave-*-link-eval*.md",     # Wave link evaluation docs
]

# Topic/cluster/broker pairs that are not individual evaluated items
GENERIC_REFERENCES = {
    'k5/k6', 'k8/k9', 'rl/marl', 'kalshi/alpaca', 'torchrl/pettingzoo',
    'postgresql/timescaledb', 'cemini/captum', 'n/a', '24/7', '0/11',
    '1/2', '2/3', 'i/o', 'pub/sub', 'ci/cd', 'k5/k7', 'k6/k7',
}

# H3 headings that are structural, not evaluated content items
STRUCTURAL_H3_PATTERNS = [
    r'^document (context|framing|register)$',
    r'^(relations|narrative|snippets|raw concept)$',
    r'^(recommendation )?summary( table)?$',
    r'^(cross-?(doc|source|document|wave|cutting))',
    r'^(why|what) this',
    r'^(open questions|follow-?ups?)',
    r'^(risks?|limitations)( &| and)?',
    r'^(anti-?hallucination|spot-?check)',
    r'^(top-?tier|part \d)',
    r'^(pattern|synthesis)',
    r'^(relationship|reference)',
    r'^(items? |repositor(y|ies) )?evaluated$',
    r'^(promotion|skip) (decision|candidate)s?$',
    r'^(cross-?document|extraction-?pipeline)',
    r'^server-state calibration',
    r'^stale-snapshot',
    r'^spectral decomposition',
    r'^license-toxicity',
    r'^stop-hook',
    r'^reject(ion)? ',
    r'^reject[ —]',
    r'^\*\*reject\*\*',
    r'^reference-only',
    r'^wave \d',
]

STOPWORDS = {
    "a", "an", "the", "of", "and", "or", "for", "to", "in", "on", "with",
    "by", "from", "is", "are", "as", "at", "via", "vs", "into", "over",
    "under", "between", "across", "using", "based", "toward", "towards",
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


def normalize_title(t: str) -> str:
    """Strip diacritics, lowercase, collapse whitespace + punctuation."""
    if not t:
        return ""
    nfkd = unicodedata.normalize("NFKD", t)
    ascii_only = "".join(c for c in nfkd if not unicodedata.combining(c))
    ascii_only = ascii_only.lower()
    ascii_only = re.sub(r"[^a-z0-9]+", " ", ascii_only).strip()
    return re.sub(r"\s+", " ", ascii_only)


def token_set(t: str) -> set:
    """Tokenize a normalized string into content-word set (stopwords stripped)."""
    norm = normalize_title(t)
    if not norm:
        return set()
    return {w for w in norm.split() if w not in STOPWORDS and len(w) > 1}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def is_structural_h3(heading: str) -> bool:
    """Return True if this H3 is structural/process, not a content item."""
    norm = normalize_title(heading)
    if not norm:
        return True
    for pat in STRUCTURAL_H3_PATTERNS:
        if re.search(pat, norm):
            return True
    return False


def strip_item_prefixes(heading: str) -> str:
    """Remove 'Document N:', 'Promoted candidate N —', etc. from a heading."""
    h = heading.strip()
    # "Document N: Title" or "Document N — Title"
    h = re.sub(r'^Document\s+\d+\s*[:—\-]\s*', '', h)
    # "Promoted candidate N — Title" / "Promotion Candidate N: Title"
    h = re.sub(r'^(Promoted|Promotion)\s+(Candidate|Item)\s+\d+\s*[:—\-]\s*', '', h)
    # "Skip illustration N — Title"
    h = re.sub(r'^Skip\s+(illustration|item|decision)\s+\d+\s*[:—\-]\s*', '', h)
    # "Target Domain N: Title"
    h = re.sub(r'^Target\s+Domain\s+\d+\s*[:—\-]\s*', '', h)
    return h.strip()


def strip_item_suffixes(heading: str) -> str:
    """Remove '— PROMOTED', '— Adopt rationale', etc. from a heading."""
    h = heading.strip()
    # Decision suffixes
    h = re.sub(r'\s*[—\-]\s*(PROMOTED|REJECTED|SNIPPETS[- ]ONLY|REFERENCE[- ]ONLY)$', '', h, flags=re.IGNORECASE)
    h = re.sub(r'\s*[—\-]\s*(Adopt|Steal[- ]from|Reference[- ]only|Abandonware)[^)]*$', '', h, flags=re.IGNORECASE)
    # Tag suffixes: "— MIT", "— Open-source", "— AGPL-3.0 POISON FLAG", etc.
    h = re.sub(r'\s*[—\-]\s*(MIT|Apache[- ]2\.0|AGPL|GPL|BSD|Open[- ]source|License|Memory|Architectural|Orchestrator)[^)]*$', '', h, flags=re.IGNORECASE)
    # Cross-doc annotation
    h = re.sub(r'\s*\(Cross[- ]doc duplicate[^)]*\)', '', h, flags=re.IGNORECASE)
    # "— Cross-wave reinforcement of ..."
    h = re.sub(r'\s*[—\-]\s*Cross[- ]wave[^)]*$', '', h, flags=re.IGNORECASE)
    return h.strip()


def extract_content_h3s(body: str) -> list[tuple[str, str]]:
    """Return [(raw_heading, normalized_heading), ...] for non-structural H3s."""
    results = []
    for m in re.finditer(r'^### (.+)$', body, re.MULTILINE):
        raw = m.group(1).strip()
        if is_structural_h3(raw):
            continue
        cleaned = strip_item_prefixes(raw)
        cleaned = strip_item_suffixes(cleaned)
        if not cleaned or len(cleaned) < 3:
            continue
        # Still structural after cleaning?
        if is_structural_h3(cleaned):
            continue
        results.append((raw, cleaned))
    return results


def main():
    files = set()
    for pattern in LINK_PATTERNS:
        for src in wiki_sources_dirs():
            files.update(src.glob(pattern))
    files = sorted(files)

    print(f"Cross-doc duplicate detection — {len(files)} link-aggregate pages\n")

    # --- Pass 1: GitHub repos ---
    repo_index = defaultdict(list)
    for fp in files:
        _, body = split_frontmatter_body(fp)
        for repo in extract_repos(body):
            repo_index[repo].append(fp)

    # Separate true duplicates from cross-references
    repo_dupes = {}
    repo_xrefs = {}
    for repo, fnames in repo_index.items():
        if len(fnames) < 2:
            continue
        # If all but one reference are cross-links (not evaluations), flag differently
        full_evals = 0
        for fn in fnames:
            _, body = split_frontmatter_body(fn)
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
                print(f"    → {label(fn)}")

    if repo_xrefs:
        print(f"\n{'=' * 70}")
        print("CROSS-REFERENCES (evaluated in one doc, mentioned in others)")
        print("=" * 70)
        for repo, fnames in sorted(repo_xrefs.items()):
            print(f"\n  {repo}")
            for fn in sorted(fnames):
                print(f"    → {label(fn)}")

    # --- Pass 2: arXiv/OpenReview IDs ---
    arxiv_index = defaultdict(list)
    for fp in files:
        _, body = split_frontmatter_body(fp)
        for aid in extract_arxiv_ids(body):
            arxiv_index[aid].append(fp)
        for oid in extract_openreview_ids(body):
            arxiv_index[oid].append(fp)

    arxiv_dupes = {a: fs for a, fs in arxiv_index.items() if len(fs) > 1}
    if arxiv_dupes:
        print(f"\n{'=' * 70}")
        print("ARXIV / OPENREVIEW ID DUPLICATES")
        print("=" * 70)
        for aid, fnames in sorted(arxiv_dupes.items()):
            print(f"\n  {aid}")
            for fn in sorted(fnames):
                print(f"    → {label(fn)}")
    else:
        print(f"\n  No arXiv/OpenReview ID duplicates found.")

    # --- Pass 3: H3 content-item heading fuzzy matching ---
    # Only considers headings that name a specific project/paper/tool (proper-noun
    # signal), since Pass 1 (GitHub repos) and Pass 2 (arXiv IDs) already catch
    # the common cases. This pass catches items referred to by name only.
    FUZZY_THRESHOLD = 0.50

    # Structural heading tokens (normalized). If a cleaned heading's normalized
    # form contains any of these as a substring, it's structural, not a content item.
    STRUCTURAL_NORM_TERMS = {
        normalize_title(t) for t in [
            'cross-document', 'cross-source', 'cross-wave', 'cross-cutting',
            'snippets-only', 'promotion-vs', 'server-state', 'stale-snapshot',
            'anti-hallucination', 'spot-check', 'reference-only',
            'stop-hook', 'license-toxicity', 'ghost-token',
            'forward-pointer', 'budget-retention', 'extraction-pipeline',
            'steal-from', 'adopt-rationale', 'poison-pill', 'poison-flag',
            'out-of-scope', 'decision-matrix', 'promotion-candidates',
            'promotion-decisions', 'skip-illustration', 'skip-decision',
            'document-context', 'document-register', 'document-framing',
            'synthesis-section', 'recommendation-summary',
            'recommendation-distribution', 'items-evaluated',
            'repositories-evaluated', 'patterns-worth-noting',
            'cross-cluster', 'cross-doc', 'follow-ups', 'open-questions',
            'promotion-vs-snippets-only', 'high-signal', 'link-evaluation',
            'link-eval', 'three-way', 'ex-ante', 'ex-post',
        ]
    }
    # Only check substrings ≥10 chars to avoid short coincidental matches
    STRUCTURAL_NORM_LONG = {t for t in STRUCTURAL_NORM_TERMS if len(t) >= 10}

    def has_content_identifier(heading: str) -> bool:
        """Return True only if the heading names a specific project/paper/tool."""
        norm = normalize_title(heading)
        # Reject if any long structural term appears as substring
        for term in STRUCTURAL_NORM_LONG:
            if term in norm:
                return False
        # arXiv ID or DOI
        if re.search(r'\b\d{4}\.\d{4,5}\b', heading):
            return True
        if re.search(r'\b10\.\d{4,9}/', heading):
            return True
        # GitHub owner/repo
        if re.search(r'(?<!\w)[\w.-]+/[\w.-]+', heading):
            return True
        # Hyphenated project name (kebab-case, ≥3 chars each side)
        if re.search(r'[a-z]{3,}-[a-z]{3,}', heading):
            return True
        # CamelCase compound (DSPy, TimesFM, LangChain, etc.)
        if re.search(r'\b[A-Z][a-z]+[A-Z][a-z]+\b', heading):
            return True
        return False

    # Collect H3 headings per doc, requiring proper-noun signal
    doc_h3s = {}
    for fp in files:
        _, body = split_frontmatter_body(fp)
        items = []
        for raw, cleaned in extract_content_h3s(body):
            if not has_content_identifier(cleaned):
                continue
            items.append((raw, cleaned, token_set(cleaned)))
        if items:
            doc_h3s[fp.name] = items

    # Cross-compare across docs
    fuzzy_dupes = []
    seen_pairs = set()  # (norm_a, norm_b) dedup
    doc_names = sorted(doc_h3s.keys())
    for i in range(len(doc_names)):
        for j in range(i + 1, len(doc_names)):
            d1, d2 = doc_names[i], doc_names[j]
            for raw1, cleaned1, toks1 in doc_h3s[d1]:
                if not toks1:
                    continue
                for raw2, cleaned2, toks2 in doc_h3s[d2]:
                    if not toks2:
                        continue
                    if not (toks1 & toks2):
                        continue
                    score = jaccard(toks1, toks2)
                    if score < FUZZY_THRESHOLD:
                        continue
                    # Skip if both headings contain a GitHub repo (Pass 1 territory)
                    if (re.search(r'(?<!\w)[\w.-]+/[\w.-]+', raw1) and
                            re.search(r'(?<!\w)[\w.-]+/[\w.-]+', raw2)):
                        continue
                    # Normalize both for dedup key
                    n1, n2 = normalize_title(cleaned1), normalize_title(cleaned2)
                    pair_key = tuple(sorted([n1, n2]))
                    if pair_key in seen_pairs:
                        continue
                    seen_pairs.add(pair_key)
                    kind = "exact" if n1 == n2 else "fuzzy"
                    fuzzy_dupes.append((cleaned1, cleaned2, d1, d2, score, kind))

    fuzzy_dupes.sort(key=lambda x: -x[4])

    if fuzzy_dupes:
        print(f"\n{'=' * 70}")
        print("H3 HEADING FUZZY MATCHES (same item under different headings)")
        print("=" * 70)
        for cleaned1, cleaned2, d1, d2, score, kind in fuzzy_dupes:
            tag = "EXACT" if kind == "exact" else f"Jaccard {score:.2f}"
            print(f"\n  [{tag}]")
            print(f"    → {d1}")
            print(f"      \"{cleaned1[:100]}\"")
            print(f"    → {d2}")
            print(f"      \"{cleaned2[:100]}\"")
    else:
        print(f"\n  No H3 heading fuzzy matches found (non-repo, non-arXiv content items).")

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
    print(f"  H3 heading fuzzy matches:    {len(fuzzy_dupes)}")


if __name__ == "__main__":
    main()
