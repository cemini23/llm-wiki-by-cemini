#!/usr/bin/env python3
"""K254 eval URL SPDX gate — gh api license check before Integrate GO.

Sample URLs from K254 eval docx batches (@concepts/k254-eval-github-wave.md).
Does not clone repos; reports license field for operator Integrate decision.

Usage:
  python3 scripts/spdx_watch_k254_eval.py list
  python3 scripts/spdx_watch_k254_eval.py check
  python3 scripts/spdx_watch_k254_eval.py selftest
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass

# K254 eval batches — update when new eval sources cite URLs
K254_EVAL_URLS: dict[str, list[str]] = {
    "repository-revenue-threat-intel": [
        "https://github.com/Bert-JanP/Open-Source-Threat-Intel-Feeds",
        "https://github.com/DavidCarliez/trustmebro",
    ],
    "multi-wiki-metatron-claude-code": [
        "https://github.com/sooryathejas/METATRON",
        "https://github.com/wesammustafa/Claude-Code-Everything-You-Need-to-Know",
    ],
    "multi-wiki-copy-dfs-gambling": [
        "https://github.com/DIC19milliQ/nfl-gamebook-companion",
        "https://github.com/GiulSposito/DraftWarRoom",
        "https://github.com/Randdalf/fplcache",
    ],
}

GITHUB_RE = re.compile(r"https?://github\.com/([^/]+)/([^/#?]+)")


@dataclass
class RepoRef:
    owner: str
    repo: str
    batch: str
    url: str


def _parse_github(url: str, batch: str) -> RepoRef | None:
    m = GITHUB_RE.match(url.strip())
    if not m:
        return None
    return RepoRef(owner=m.group(1), repo=m.group(2), batch=batch, url=url)


def all_refs() -> list[RepoRef]:
    out: list[RepoRef] = []
    for batch, urls in K254_EVAL_URLS.items():
        for url in urls:
            ref = _parse_github(url, batch)
            if ref:
                out.append(ref)
    return out


def gh_license(owner: str, repo: str) -> dict:
    if not shutil.which("gh"):
        return {"error": "gh not on PATH"}
    cmd = ["gh", "api", f"repos/{owner}/{repo}", "--jq", ".license.spdx_id,.license.key"]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=30)
        parts = proc.stdout.strip().split("\n")
        spdx = parts[0] if parts else "null"
        key = parts[1] if len(parts) > 1 else "null"
        return {"spdx_id": spdx, "license_key": key}
    except subprocess.CalledProcessError as exc:
        return {"error": (exc.stderr or exc.stdout or str(exc)).strip()[:200]}
    except subprocess.TimeoutExpired:
        return {"error": "gh api timeout"}


def list_urls() -> None:
    for ref in all_refs():
        print(f"{ref.batch}\t{ref.owner}/{ref.repo}\t{ref.url}")


def check_all() -> int:
    rows: list[dict] = []
    for ref in all_refs():
        lic = gh_license(ref.owner, ref.repo)
        row = {
            "batch": ref.batch,
            "repo": f"{ref.owner}/{ref.repo}",
            "url": ref.url,
            **lic,
        }
        rows.append(row)
        spdx = lic.get("spdx_id", lic.get("error", "?"))
        print(f"{ref.owner}/{ref.repo}: {spdx}")

    integratable = [
        r
        for r in rows
        if r.get("spdx_id") not in (None, "null", "NOASSERTION") and "error" not in r
    ]
    print("")
    print(f"checked={len(rows)} integratable_spdx={len(integratable)}")
    print(json.dumps(rows, indent=2))
    return 0


def selftest() -> int:
    refs = all_refs()
    if len(refs) < 7:
        print("FAIL expected >=7 repo refs", file=sys.stderr)
        return 1
    if _parse_github("https://github.com/foo/bar", "t") is None:
        print("FAIL parse", file=sys.stderr)
        return 1
    print("spdx_watch_k254_eval selftest: pass")
    return 0


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: spdx_watch_k254_eval.py list|check|selftest", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    if cmd == "list":
        list_urls()
        return 0
    if cmd == "check":
        return check_all()
    if cmd == "selftest":
        return selftest()
    print(f"unknown cmd: {cmd}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
