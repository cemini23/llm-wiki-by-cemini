#!/usr/bin/env python3
"""Validate wiki/meta/wire-ledger.yaml — WIRE rows only; coverage for runtime_wired pages."""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CCC_WIKI = Path("/Users/claudiobarone/Projects/Cemini claude code CCC/wiki")
KINDS = frozenset({"rule", "script", "skill", "hook", "mcp"})
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]+$")
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def resolve_wiki_page(page: str) -> Path | None:
    if page.startswith("@osint-wiki/"):
        p = ROOT / "wiki" / page.replace("@osint-wiki/", "", 1)
    elif page.startswith("@ccc-wiki/"):
        p = CCC_WIKI / page.replace("@ccc-wiki/", "", 1)
    elif page.startswith(("entities/", "concepts/", "sources/", "meta/")):
        p = ROOT / "wiki" / page
    else:
        p = ROOT / page
    return p if p.is_file() else None


def check_ledger(data: dict, root: Path, *, check_coverage: bool = True) -> list[str]:
    errs: list[str] = []
    if data.get("version") != 1:
        errs.append("version must be 1")
    repos = data.get("repos") or {}
    wires = data.get("wires")
    if not isinstance(wires, list):
        return errs + ["wires must be a list"]

    seen: set[str] = set()
    covered_pages: set[str] = set()
    for i, row in enumerate(wires):
        if not isinstance(row, dict):
            errs.append(f"wires[{i}]: not a mapping")
            continue
        wid = row.get("id", "")
        if not SLUG_RE.match(wid):
            errs.append(f"wires[{i}]: bad id {wid!r}")
        if re.match(r"^k\d+", wid):
            errs.append(f"wires[{i}]: bare K id {wid!r}")
        if wid in seen:
            errs.append(f"duplicate id {wid}")
        seen.add(wid)
        if row.get("verb") != "WIRE":
            errs.append(f"wires[{i}]: verb must be WIRE")
        kind = row.get("kind")
        if kind not in KINDS:
            errs.append(f"wires[{i}]: bad kind {kind!r}")
        repo_key = row.get("repo")
        if repo_key not in repos:
            errs.append(f"wires[{i}]: unknown repo {repo_key!r}")
            continue
        repo_root = Path(repos[repo_key])
        path = row.get("path", "")
        if path != "wiki-only" and not (repo_root / path).exists():
            errs.append(f"wires[{i}]: missing path {repo_root / path}")
        wp = row.get("wiki_page", "")
        if not resolve_wiki_page(wp):
            errs.append(f"wires[{i}]: wiki_page not found {wp!r}")
        else:
            covered_pages.add(wp if not wp.startswith("@") else wp.split("/", 1)[-1])
            if wp.startswith("entities/") or wp.startswith("concepts/"):
                covered_pages.add(wp)
        since = row.get("since", "")
        if not ISO_DATE.match(str(since)):
            errs.append(f"wires[{i}]: bad since {since!r}")

    if check_coverage:
        for md in root.glob("wiki/**/*.md"):
            text = md.read_text(encoding="utf-8", errors="replace")
            if "harness_verb: WIRE" not in text and "wire_status: runtime_wired" not in text and "wire_status: integrate" not in text:
                continue
            rel = str(md.relative_to(root / "wiki"))
            rel_at = f"@osint-wiki/{rel}"
            if rel not in covered_pages and rel_at not in covered_pages:
                found = any(
                    rel in (w.get("wiki_page") or "") for w in wires if isinstance(w, dict)
                )
                if not found:
                    errs.append(f"coverage: runtime_wired page missing from ledger: {rel}")
    return errs


def run_verify(data: dict, *, quiet: bool) -> list[str]:
    errs: list[str] = []
    repos = data.get("repos") or {}
    wires = data.get("wires") or []
    for row in wires:
        if not isinstance(row, dict):
            continue
        wid = row.get("id", "?")
        verify = (row.get("verify") or "").strip()
        if not verify or verify.startswith("wiki-only"):
            if not quiet:
                print(f"  SKIP {wid} (wiki-only or empty)")
            continue
        repo_key = row.get("repo")
        repo_root = Path(repos.get(repo_key, ROOT))
        if not quiet:
            print(f"  RUN {wid}: {verify}")
        try:
            subprocess.run(
                verify,
                shell=True,
                cwd=repo_root,
                check=True,
                capture_output=True,
                text=True,
            )
        except subprocess.CalledProcessError as exc:
            err = (exc.stderr or exc.stdout or str(exc)).strip().splitlines()
            tail = err[-3:] if err else [str(exc)]
            errs.append(f"verify {wid} failed in {repo_root}: {' | '.join(tail)}")
    return errs


def selftest() -> int:
    good = {
        "version": 1,
        "repos": {"osint": str(ROOT), "ccc": str(CCC_WIKI.parent)},
        "wires": [
            {
                "id": "test-wire",
                "verb": "WIRE",
                "kind": "script",
                "repo": "osint",
                "path": "scripts/wire_ledger_check.py",
                "wiki_page": "@osint-wiki/concepts/file-keep-wire-harness.md",
                "since": "2026-09-02",
            }
        ],
    }
    bad = dict(good)
    bad["wires"] = [{"id": "k999", "verb": "FILE", "kind": "x", "repo": "nope", "path": "nope", "wiki_page": "nope", "since": "bad"}]
    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as tf:
        yaml.safe_dump(good, tf)
        good_path = Path(tf.name)
    e1 = check_ledger(good, ROOT, check_coverage=False)
    e2 = check_ledger(bad, ROOT, check_coverage=False)
    good_path.unlink(missing_ok=True)
    if e1:
        print("selftest FAIL: good ledger rejected:", e1)
        return 1
    if not e2:
        print("selftest FAIL: bad ledger accepted")
        return 1
    print("selftest PASS")
    return 0


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--ledger", type=Path, default=ROOT / "wiki/meta/wire-ledger.yaml")
    p.add_argument("--selftest", action="store_true")
    p.add_argument("--run-verify", action="store_true")
    p.add_argument("--quiet", action="store_true")
    args = p.parse_args()
    if args.selftest:
        return selftest()
    data = yaml.safe_load(args.ledger.read_text(encoding="utf-8"))
    errs = check_ledger(data, ROOT)
    if errs:
        if not args.quiet:
            print("FAIL")
            for e in errs:
                print(f"  - {e}")
        return 1
    n = len(data.get("wires") or [])
    if not args.quiet:
        print(f"PASS wires={n}")
    if args.run_verify:
        if not args.quiet:
            print("verify:")
        verr = run_verify(data, quiet=args.quiet)
        if verr:
            if not args.quiet:
                print("VERIFY FAIL")
                for e in verr:
                    print(f"  - {e}")
            return 1
        if not args.quiet:
            print("VERIFY PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
