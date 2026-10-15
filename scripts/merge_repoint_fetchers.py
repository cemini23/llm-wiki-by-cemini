#!/usr/bin/env python3
"""Re-point the daily fetchers at the merged federation wiki (plan 5.4).

Before the merge each domain had its own repo, so a fetcher's output path was
`<repo>/wiki/sweeps/<date>-daily.md`. After the merge all eight domains share one
repo, so the path must carry the domain: `<repo>/wiki/<domain>/sweeps/<date>-daily.md`.
Until this runs the fetchers would write into the archived sibling repos.

Changes, all idempotent:

  scripts/daily_research_config.yaml      path_template gains {domain}
  scripts/daily_research_digest_run.py    renders {domain} from CEMINI_WIKI_ID
  scripts/run_daily_research_digest.sh    report path carries the domain
  scripts/run_wiki_gap_detect.sh          cadence meta lives at wiki/osint/meta/
  ~/bin/cemini-daily-research-digest      base wrapper: WIKI_ID=osint, domain path
  ~/bin/cemini-daily-research-digest-*    domain wrappers: export CEMINI_WIKI_ID
  ~/.cemini/wiki-paths/*.path             all eight point at the merged repo

Usage: python3 scripts/merge_repoint_fetchers.py [--check]
"""

from __future__ import annotations

import sys
from pathlib import Path

HOME = Path.home()
WS = HOME / "Projects/OSINT WORKSPACE"
DOMAINS = ["3d-printing", "ccc", "cybersec", "gambling", "game-dev", "image-gen", "seo"]

OLD_REPORT = 'REPORT="${ROOT}/wiki/sweeps/${TODAY}-daily.md"'
NEW_REPORT = 'REPORT="${ROOT}/wiki/${WIKI_ID}/sweeps/${TODAY}-daily.md"'
OLD_ROOT_EXPORT = 'export CEMINI_WIKI_ROOT="${ROOT}"'
NEW_ROOT_EXPORT = 'export CEMINI_WIKI_ROOT="${ROOT}"\nexport CEMINI_WIKI_ID="${WIKI_ID}"'


class Patcher:
    def __init__(self, check: bool):
        self.check = check
        self.n_ok = 0
        self.n_skip = 0
        self.n_fail = 0

    def sub(self, path: Path, old: str, new: str, label: str, optional=False):
        if not path.is_file():
            print(f"  FAIL  {label}: missing {path}")
            self.n_fail += 1
            return
        text = path.read_text(encoding="utf-8")
        if new in text and old not in text:
            print(f"  --    {label}: already done")
            self.n_skip += 1
            return
        n = text.count(old)
        if n != 1:
            if optional and n == 0:
                print(f"  --    {label}: pattern absent, skipped")
                self.n_skip += 1
                return
            print(f"  FAIL  {label}: matched {n}x (expected 1)")
            self.n_fail += 1
            return
        if not self.check:
            path.write_text(text.replace(old, new, 1), encoding="utf-8")
        print(f"  ok    {label}")
        self.n_ok += 1

    def write(self, path: Path, content: str, label: str):
        if path.is_file() and path.read_text(encoding="utf-8").strip() == content.strip():
            print(f"  --    {label}: already correct")
            self.n_skip += 1
            return
        if not self.check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content + "\n", encoding="utf-8")
        print(f"  ok    {label}")
        self.n_ok += 1


def main() -> int:
    check = "--check" in sys.argv
    p = Patcher(check)

    print("1. runner + config carry the domain")
    p.sub(WS / "scripts/daily_research_config.yaml",
          'path_template: "wiki/sweeps/{date}-daily.md"',
          'path_template: "wiki/{domain}/sweeps/{date}-daily.md"',
          "config path_template")
    p.sub(WS / "scripts/daily_research_digest_run.py",
          "    report = repo / out_tpl.format(date=today.isoformat())",
          "    # The merged wiki holds all eight domains in one repo, so the template must\n"
          "    # carry the domain. CEMINI_WIKI_ID is exported by the ~/bin wrappers.\n"
          "    domain = os.environ.get(\"CEMINI_WIKI_ID\") or \"osint\"\n"
          "    report = repo / out_tpl.format(date=today.isoformat(), domain=domain)",
          "digest runner renders {domain}")

    print()
    print("2. shell runners")
    p.sub(WS / "scripts/run_daily_research_digest.sh",
          'REPORT="$ROOT/wiki/sweeps/${TODAY}-daily.md"',
          'REPORT="$ROOT/wiki/${CEMINI_WIKI_ID:-osint}/sweeps/${TODAY}-daily.md"',
          "run_daily_research_digest.sh")
    p.sub(WS / "scripts/run_wiki_gap_detect.sh",
          'META="$ROOT/wiki/meta/wiki-gap-detect-cadence.md"',
          'META="$ROOT/wiki/osint/meta/wiki-gap-detect-cadence.md"',
          "run_wiki_gap_detect.sh cadence meta")

    print()
    print("3. LaunchAgent wrappers")
    base = HOME / "bin/cemini-daily-research-digest"
    p.sub(base, OLD_REPORT, NEW_REPORT, "base wrapper report path")
    p.sub(base, "REPO_FILE=", 'WIKI_ID="osint"\nREPO_FILE=', "base wrapper WIKI_ID")
    p.sub(base, OLD_ROOT_EXPORT, NEW_ROOT_EXPORT, "base wrapper CEMINI_WIKI_ID")
    for dom in DOMAINS:
        w = HOME / f"bin/cemini-daily-research-digest-{dom}"
        p.sub(w, OLD_REPORT, NEW_REPORT, f"wrapper {dom} report path")
        p.sub(w, OLD_ROOT_EXPORT, NEW_ROOT_EXPORT, f"wrapper {dom} CEMINI_WIKI_ID")

    print()
    print("4. wiki path registry")
    for dom in DOMAINS:
        p.write(HOME / f".cemini/wiki-paths/{dom}.path", str(WS), f"wiki-paths/{dom}.path")

    print()
    print(f"{'would change' if check else 'changed'}: {p.n_ok}  "
          f"already done: {p.n_skip}  failed: {p.n_fail}")
    if check:
        print("--check only; nothing written")
    return 1 if p.n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
