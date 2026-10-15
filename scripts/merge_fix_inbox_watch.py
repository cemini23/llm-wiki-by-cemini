#!/usr/bin/env python3
"""Point the inbox watcher at the domain-namespaced inbox (plan 5.4).

The merged workspace namespaces the inbox by domain. `com.cemini.inbox-notify` still
watched only the flat directory, so a drop into `research to be indexed/<domain>/`
would not fire the watcher.

  - syncs scripts/inbox_notify.sh to the launchagent bundle copy
  - adds one WatchPaths entry per domain directory
  - creates the eight domain inbox directories

Usage: python3 scripts/merge_fix_inbox_watch.py [--check]
"""

from __future__ import annotations

import plistlib
import shutil
import sys
from pathlib import Path

HOME = Path.home()
WS = HOME / "Projects/OSINT WORKSPACE"
INBOX = WS / "research to be indexed"
BUNDLE = HOME / ".cemini/launchagent/osint/inbox_notify.sh"
PLIST = HOME / "Library/LaunchAgents/com.cemini.inbox-notify.plist"
DOMAINS = ["osint", "ccc", "cybersec", "seo", "image-gen", "gambling", "game-dev", "3d-printing"]


def main() -> int:
    check = "--check" in sys.argv
    actions = []

    src = WS / "scripts/inbox_notify.sh"
    if src.read_bytes() != BUNDLE.read_bytes():
        actions.append(f"sync {src.name} -> {BUNDLE}")
    else:
        actions.append("bundle copy already current")

    data = plistlib.loads(PLIST.read_bytes())
    want = [str(INBOX)] + [str(INBOX / d) for d in DOMAINS]
    have = list(data.get("WatchPaths") or [])
    if have != want:
        missing = [p for p in want if p not in have]
        actions.append(f"WatchPaths: add {len(missing)} entr(y/ies) -> {len(want)} total")
    else:
        actions.append("WatchPaths already complete")

    existing = [d for d in DOMAINS if (INBOX / d).is_dir()]
    actions.append(f"domain inboxes present: {len(existing)}/{len(DOMAINS)}")

    for a in actions:
        print(f"  {a}")
    if check:
        print("--check only; nothing written")
        return 0

    shutil.copy2(src, BUNDLE)
    print(f"  wrote {BUNDLE}")

    data["WatchPaths"] = want
    PLIST.write_bytes(plistlib.dumps(data))
    print(f"  wrote {PLIST}")

    for d in DOMAINS:
        (INBOX / d).mkdir(parents=True, exist_ok=True)
    print(f"  ensured {len(DOMAINS)} domain inboxes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
