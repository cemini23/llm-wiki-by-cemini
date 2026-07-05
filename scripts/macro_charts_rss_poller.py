#!/usr/bin/env python3
"""Backward-compat wrapper — polls Macro Charts via unified Substack RSS poller."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from substack_rss_poller import load_config, poll_all  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Macro Charts RSS → inbox (wrapper)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    cfg = load_config()
    feed = next((f for f in cfg.get("feeds") or [] if f.get("id") == "macrocharts"), {})
    max_age = feed.get("max_age_days")
    return poll_all(
        cfg,
        dry_run=args.dry_run,
        feed_id="macrocharts",
        max_age_days=int(max_age) if max_age is not None else None,
    )


if __name__ == "__main__":
    sys.exit(main())
