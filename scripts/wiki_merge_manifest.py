#!/usr/bin/env python3
"""Verification harness for the federation wiki merge.

Replaces five unsound gates. The old plan compared aggregate dangling-link counts
before and after, which lets newly-fixed links mask newly-broken ones at net zero,
counted unique basenames rather than files, and sampled 0.8% of pages. This harness
compares the FILE SET and the RESOLVED EDGE SET, so a link that silently retargets
to a different file is reported even when the total count is unchanged.

Uses scripts/wiki_resolver.py, the same resolver the linter uses. Two resolver
implementations could disagree about whether a link resolves, which would make the
harness measure itself rather than the wiki.

Usage:
  python3 scripts/wiki_merge_manifest.py snapshot --wiki <root> --out <file.json>
  python3 scripts/wiki_merge_manifest.py compare  --before <a.json> --after <b.json>
  python3 scripts/wiki_merge_manifest.py dryrun   --repo <path> --domain <id> --scratch <dir>

Exit codes: 0 pass, 1 verification failure, 2 usage or input error.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wiki_resolver import WikiResolver, iter_refs, load_federation_table  # noqa: E402

SKIP_DIRS = {".git", ".obsidian", "__pycache__", ".pytest_cache", ".ruff_cache"}


def walk_pages(wiki_root):
    """Every markdown page under the wiki root, ordered for a deterministic manifest."""
    root = Path(wiki_root)
    out = []
    for p in sorted(root.rglob("*.md")):
        if SKIP_DIRS & set(p.relative_to(root).parts):
            continue
        if p.is_file():
            out.append(p)
    return out


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def cmd_snapshot(args):
    wiki = Path(args.wiki).resolve()
    if not wiki.is_dir():
        print(f"ERROR: no wiki at {wiki}", file=sys.stderr)
        return 2
    table = load_federation_table(wiki.parent / "CLAUDE.md")
    resolver = WikiResolver(wiki, table)

    pages = walk_pages(wiki)
    keys = {str(p.relative_to(wiki)) for p in pages}

    files = [
        {
            "key": str(p.relative_to(wiki)),
            "sha256": sha256(p),
            "size": p.stat().st_size,
        }
        for p in pages
    ]

    edges = []
    for p in pages:
        src_key = str(p.relative_to(wiki))
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for raw, kind in iter_refs(text):
            result_kind, value = resolver.resolve(src_key, raw, keys)
            if result_kind == "ambiguous":
                target = sorted(value)
            elif result_kind == "out":
                target = str(value)
            elif result_kind == "missing":
                target = str(value)
            else:
                target = value
            edges.append(
                {
                    "src": src_key,
                    "raw": raw,
                    "kind": kind,
                    "result": result_kind,
                    "target": target,
                }
            )
    edges.sort(key=lambda e: (e["src"], e["kind"], e["raw"]))

    payload = {
        "label": args.label or wiki.parent.name,
        "wiki": str(wiki),
        "domains": sorted(resolver.domains),
        "files": files,
        "edges": edges,
    }

    # A pre-merge snapshot keys pages from its own wiki root ("concepts/foo.md").
    # The merged snapshot keys them with the domain ("osint/concepts/foo.md").
    # Without this rewrite every pre-merge file would read as both missing and
    # added, and every edge as retargeted, which measures nothing.
    if args.as_domain:
        dom = args.as_domain.strip("/")
        for f in payload["files"]:
            f["key"] = f"{dom}/{f['key']}"
        for e in payload["edges"]:
            e["src"] = f"{dom}/{e['src']}"
            if e["result"] == "local":
                e["target"] = f"{dom}/{e['target']}"
        payload["label"] = f"{payload['label']} (as {dom})"

    text = json.dumps(payload, indent=1, sort_keys=True)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
        print(f"snapshot: {len(files)} files, {len(edges)} edges -> {args.out}")
    else:
        print(text)
    return 0


def cmd_concat(args):
    """Union several pre-merge snapshots into the set the merged tree must match."""
    files, edges = {}, {}
    labels, domains, wikis = [], set(), []
    for path in args.inputs:
        snap = json.loads(Path(path).read_text(encoding="utf-8"))
        labels.append(snap["label"])
        domains.update(snap.get("domains", []))
        wikis.append(snap["wiki"])
        for f in snap["files"]:
            if f["key"] in files:
                print(f"WARNING: duplicate key across inputs: {f['key']}", file=sys.stderr)
            files[f["key"]] = f
        for e in snap["edges"]:
            edges[(e["src"], e["kind"], e["raw"])] = e
    payload = {
        "label": " + ".join(labels),
        "wiki": wikis,
        "domains": sorted(domains),
        "files": sorted(files.values(), key=lambda f: f["key"]),
        "edges": sorted(edges.values(), key=lambda e: (e["src"], e["kind"], e["raw"])),
    }
    text = json.dumps(payload, indent=1, sort_keys=True)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
        print(f"concat: {len(files)} files, {len(edges)} edges -> {args.out}")
    else:
        print(text)
    return 0


def _edge_map(snap):
    return {(e["src"], e["kind"], e["raw"]): e for e in snap["edges"]}


def cmd_compare(args):
    before = json.loads(Path(args.before).read_text(encoding="utf-8"))
    after = json.loads(Path(args.after).read_text(encoding="utf-8"))

    bf = {f["key"]: f["sha256"] for f in before["files"]}
    af = {f["key"]: f["sha256"] for f in after["files"]}

    missing = sorted(k for k in bf if k not in af)
    added = sorted(k for k in af if k not in bf)
    changed = sorted(k for k in bf if k in af and bf[k] != af[k])

    be, ae = _edge_map(before), _edge_map(after)
    flipped = []    # resolved before, missing after
    retargeted = []  # resolved before, resolves to a DIFFERENT target after
    lost_certainty = []  # resolved before, ambiguous after
    relocated = []  # resolved outside the wiki before, inside it after
    moved = []  # resolved outside the wiki before AND after, at a different path
    for key, e in be.items():
        # "local" and "out" are both resolutions. The gate originally tested only for
        # "local", so every edge that resolved into a peer repo checkout - the 160
        # brief citations in the 2026-10-14 merge - was never compared. The merge
        # dropped all 160 and the gate still printed PASS. Never narrow this filter
        # to the in-tree case again.
        if e["result"] not in ("local", "out"):
            continue
        new = ae.get(key)
        if new is None:
            continue  # page removed; the file check reports that
        if new["result"] == "missing":
            flipped.append((key, e["target"]))
        elif new["result"] == "ambiguous":
            lost_certainty.append((key, e["target"], new["target"]))
        elif e["result"] == "local" and new["result"] == "local":
            # An in-tree key that changes means the link now reaches a DIFFERENT PAGE.
            # That is the hazard this check exists for.
            if new["target"] != e["target"]:
                retargeted.append((key, e["target"], new["target"]))
        elif e["result"] == "out" and new["result"] == "local":
            relocated.append((key, e["target"], new["target"]))
        elif e["result"] == "out" and new["result"] == "out":
            # Both resolve beside the wiki, at different paths. The merge moves whole
            # trees (briefs/ into per-domain directories), so a path change here is
            # expected churn, not a broken link. Report it; do not fail on it.
            if new["target"] != e["target"]:
                moved.append((key, e["target"], new["target"]))

    print("=" * 70)
    print("federation merge — verification comparison")
    print("=" * 70)
    print(f"  before: {before['label']}  ({len(bf)} files, {len(be)} edges)")
    print(f"  after:  {after['label']}  ({len(af)} files, {len(ae)} edges)")

    def block(title, rows, fmt):
        print(f"\n{title} — {len(rows)}")
        for r in rows[:40]:
            print("  " + fmt(r))
        if len(rows) > 40:
            print(f"  ... and {len(rows)-40} more")

    block("FILES MISSING AFTER (hard failure)", missing, lambda k: k)
    block("FILES ADDED AFTER (expected only if the merge adds domains)", added, lambda k: k)
    block("FILE CONTENT CHANGED", changed, lambda k: f"{k}  {bf[k][:12]} -> {af[k][:12]}")
    block(
        "LINKS THAT RESOLVED BEFORE AND DO NOT AFTER (hard failure)",
        flipped,
        lambda r: f"{r[0][0]}  [{r[0][1]}] {r[0][2]}  -> was {r[1]}",
    )
    block(
        "SILENT RETARGETS — same link, different file (hard failure)",
        retargeted,
        lambda r: f"{r[0][0]}  [{r[0][1]}] {r[0][2]}  {r[1]} -> {r[2]}",
    )
    block(
        "CERTAINTY LOST — resolved before, ambiguous after (hard failure)",
        lost_certainty,
        lambda r: f"{r[0][0]}  [{r[0][1]}] {r[0][2]}  was {r[1]}, now {r[2]}",
    )
    block(
        "RELOCATED — resolved beside the wiki before, inside it after (informational)",
        relocated,
        lambda r: f"{r[0][0]}  [{r[0][1]}] {r[0][2]}  {r[1]} -> {r[2]}",
    )
    block(
        "MOVED — still outside the wiki, at a different path (informational)",
        moved,
        lambda r: f"{r[0][0]}  [{r[0][1]}] {r[0][2]}  {r[1]} -> {r[2]}",
    )

    failed = bool(missing or flipped or retargeted or lost_certainty)
    print()
    print("VERDICT: FAIL" if failed else "VERDICT: PASS")
    return 1 if failed else 0


def cmd_dryrun(args):
    """Import one repository into a scratch tree. Never writes to a live repository."""
    repo = Path(args.repo).resolve()
    scratch = Path(args.scratch).resolve()
    if not (repo / ".git").is_dir():
        print(f"ERROR: not a git repository: {repo}", file=sys.stderr)
        return 2
    if scratch.exists():
        print(f"ERROR: scratch path already exists, refusing to overwrite: {scratch}", file=sys.stderr)
        return 2

    subprocess.run(["git", "clone", "-q", str(repo), str(scratch)], check=True)
    # Importing a SOURCE wiki: keep only its wiki/ tree.
    #
    # The TARGET repository must NOT be imported this way. --path wiki/ keeps only
    # wiki/ and drops scripts/, CLAUDE.md and everything else from history; the
    # target needs --path-rename ALONE, which moves wiki/ to wiki/<domain>/ and
    # leaves the rest of the repository in place.
    cmd = [
        "git", "-C", str(scratch), "filter-repo", "--force",
        "--path-rename", f"wiki/:wiki/{args.domain}/",
    ]
    if not args.target:
        cmd[4:4] = ["--path", "wiki/"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"ERROR: filter-repo failed:\n{r.stderr.strip()}", file=sys.stderr)
        return 2
    files = sorted(
        str(p.relative_to(scratch)) for p in (scratch / "wiki").rglob("*") if p.is_file()
    )
    print(f"dryrun: {repo.name} -> {scratch}")
    print(f"  wiki/ files after rename: {len(files)}")
    for f in files[:10]:
        print(f"    {f}")
    if len(files) > 10:
        print(f"    ... and {len(files)-10} more")
    print(f"  live repository untouched: {repo}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("snapshot", help="manifest + resolved edges for one wiki root")
    s.add_argument("--wiki", required=True)
    s.add_argument("--label", default=None)
    s.add_argument("--as-domain", default=None,
                   help="Prefix every key with this domain, to make a pre-merge "
                        "snapshot comparable with a merged one.")
    s.add_argument("--out", default=None)
    s.set_defaults(fn=cmd_snapshot)

    cc = sub.add_parser("concat", help="union several snapshots into one")
    cc.add_argument("--out", default=None)
    cc.add_argument("inputs", nargs="+")
    cc.set_defaults(fn=cmd_concat)

    c = sub.add_parser("compare", help="compare two snapshots")
    c.add_argument("--before", required=True)
    c.add_argument("--after", required=True)
    c.set_defaults(fn=cmd_compare)

    d = sub.add_parser("dryrun", help="import one repo into a scratch tree")
    d.add_argument("--repo", required=True)
    d.add_argument("--domain", required=True)
    d.add_argument("--scratch", required=True)
    d.add_argument("--target", action="store_true",
                   help="This is the TARGET repository, not a source. Keeps "
                        "everything outside wiki/ instead of discarding it.")
    d.set_defaults(fn=cmd_dryrun)

    args = ap.parse_args()
    return int(args.fn(args))


if __name__ == "__main__":
    sys.exit(main())
