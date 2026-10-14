#!/usr/bin/env python3
"""Secret scan over the exact surface the federation merge makes public.

The merged repo is public. Only `wiki/` moves from each sibling; osint contributes
its whole repository. So the public surface is:

  * every file under OSINT WORKSPACE/     (all of it)
  * every file under <sibling>/wiki/      (only the wiki tree)

Scans the working tree and, optionally, git history — the merge preserves history,
so a secret committed and later deleted still becomes public.

Usage:
  python3 scripts/secret_scan_merge.py worktree
  python3 scripts/secret_scan_merge.py history
  python3 scripts/secret_scan_merge.py all
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

PROJ = Path.home() / "Projects"
OSINT = PROJ / "OSINT WORKSPACE"

SIBLINGS = [
    ("Cemini claude code CCC", "ccc"),
    ("Cybersecurity wiki", "cybersec"),
    ("SEO:GEO B&M Business", "seo"),
    ("Image gen", "image-gen"),
    ("Gambling wiki", "gambling"),
    ("Game Dev wiki", "game-dev"),
    ("3d printing", "3d-printing"),
]

# Real credential shapes. These are what matters in a public repo.
PATTERNS = [
    (r"sk-ant-[A-Za-z0-9_\-]{20,}", "anthropic-key"),
    (r"sk-proj-[A-Za-z0-9_\-]{20,}", "openai-project-key"),
    (r"\bsk-[A-Za-z0-9]{32,}\b", "openai-style-key"),
    (r"ghp_[A-Za-z0-9]{36}", "github-pat"),
    (r"gho_[A-Za-z0-9]{36}", "github-oauth"),
    (r"ghs_[A-Za-z0-9]{36}", "github-app"),
    (r"github_pat_[A-Za-z0-9_]{20,}", "github-fine-grained-pat"),
    (r"AKIA[0-9A-Z]{16}", "aws-access-key-id"),
    (r"xox[baprs]-[A-Za-z0-9\-]{10,}", "slack-token"),
    (r"https://discord(?:app)?\.com/api/webhooks/\d{15,}/[A-Za-z0-9_\-]{50,}", "discord-webhook"),
    (r"sk_live_[A-Za-z0-9]{20,}", "stripe-live-secret"),
    (r"rk_live_[A-Za-z0-9]{20,}", "stripe-live-restricted"),
    (r"AIza[0-9A-Za-z_\-]{35}", "google-api-key"),
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "private-key-block"),
    (r"\b\d{8,10}:[A-Za-z0-9_\-]{35}\b", "telegram-bot-token"),
    (r"\bBSA[A-Za-z0-9_\-]{20,}\b", "brave-search-key"),
    # Generic assignment of a long literal to a secret-ish name.
    (r"""(?i)\b(?:api[_-]?key|secret|token|passwd|password|passphrase)\b\s*[:=]\s*["'][A-Za-z0-9_\-/+]{24,}["']""",
     "assigned-literal"),
]

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".obsidian", ".pytest_cache",
             ".venv", "venv", "dist", "build", ".next", ".wrangler", "site-packages"}
SKIP_NAMES = {".secrets.baseline", "package-lock.json", "bun.lock", "poetry.lock"}
MAX_BYTES = 2_000_000

COMPILED = [(re.compile(p), label) for p, label in PATTERNS]


def targets():
    yield OSINT, "osint", None
    for repo, dom in SIBLINGS:
        w = PROJ / repo / "wiki"
        if w.is_dir():
            yield PROJ / repo, dom, "wiki"


def tracked_files(repo: Path, pathspec):
    """Files git would publish: those tracked, plus untracked but not ignored.

    Scanning the raw filesystem is wrong twice over: it sweeps in gitignored trees
    (`.local/`, which never leaves the laptop) and misses nothing that matters.
    """
    args = ["-C", str(repo), "ls-files"]
    if pathspec:
        args += ["--", pathspec]
    out = subprocess.run(["git", *args], capture_output=True, text=True).stdout
    files = out.splitlines()

    args = ["-C", str(repo), "ls-files", "--others", "--exclude-standard"]
    if pathspec:
        args += ["--", pathspec]
    out = subprocess.run(["git", *args], capture_output=True, text=True).stdout
    files += out.splitlines()

    for rel in files:
        if Path(rel).name in SKIP_NAMES:
            continue
        p = repo / rel
        try:
            if not p.is_file() or p.is_symlink() or p.stat().st_size > MAX_BYTES:
                continue
        except OSError:
            continue
        yield p


def redact(m: str) -> str:
    m = m.strip()
    if len(m) <= 12:
        return m
    return f"{m[:6]}…{m[-4:]}"


def cmd_worktree() -> int:
    hits = []
    scanned = 0
    roots = list(targets())
    for repo, dom, pathspec in roots:
        n = 0
        for p in tracked_files(repo, pathspec):
            n += 1
            try:
                text = p.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            for i, line in enumerate(text.splitlines(), 1):
                for rx, label in COMPILED:
                    m = rx.search(line)
                    if m:
                        hits.append((dom, label, str(p), i, redact(m.group(0))))
        scanned += n
        print(f"  {dom:<12} {n:>6} files")

    print(f"\nscanned {scanned} files across {len(roots)} roots")
    print("=" * 78)
    if not hits:
        print("NO HITS")
        return 0
    by_label: dict[str, int] = {}
    for dom, label, path, ln, red in hits:
        by_label[label] = by_label.get(label, 0) + 1
    print(f"{len(hits)} hit(s):")
    for label, c in sorted(by_label.items(), key=lambda x: -x[1]):
        print(f"  {c:>4}  {label}")
    print()
    for dom, label, path, ln, red in hits[:80]:
        rel = path.replace(str(PROJ) + "/", "")
        print(f"  [{label}] {rel}:{ln}  {red}")
    if len(hits) > 80:
        print(f"  … {len(hits) - 80} more")
    return 1


def cmd_history() -> int:
    print("history scan — added lines only, restricted to paths that become public")
    print("=" * 78)
    repos = [("OSINT WORKSPACE", ".", "osint")]
    repos += [(repo, "wiki/", dom) for repo, dom in SIBLINGS]

    total = 0
    for repo, pathfilter, dom in repos:
        gitdir = PROJ / repo / ".git"
        if not gitdir.is_dir():
            continue
        try:
            p = subprocess.run(
                ["git", "-C", str(PROJ / repo), "log", "-p", "--all", "--no-color", "--", pathfilter],
                capture_output=True, text=True, errors="ignore", timeout=900,
            )
        except subprocess.TimeoutExpired:
            print(f"  {dom:<12} TIMEOUT")
            continue
        added = [ln for ln in p.stdout.splitlines() if ln.startswith("+") and not ln.startswith("+++")]
        found: dict[str, int] = {}
        for ln in added:
            for rx, label in COMPILED:
                if rx.search(ln):
                    found[label] = found.get(label, 0) + 1
        if found:
            summary = ", ".join(f"{k}×{v}" for k, v in sorted(found.items()))
            print(f"  {dom:<12} HITS  {summary}")
            total += sum(found.values())
        else:
            print(f"  {dom:<12} clean ({len(added)} added lines)")
    print()
    print(f"history hits: {total}")
    return 1 if total else 0


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode in ("worktree", "all"):
        print("WORKING TREE")
        print("=" * 78)
        rc = cmd_worktree()
        print()
    else:
        rc = 0
    if mode in ("history", "all"):
        hrc = cmd_history()
        rc = rc or hrc
    return rc


if __name__ == "__main__":
    sys.exit(main())
