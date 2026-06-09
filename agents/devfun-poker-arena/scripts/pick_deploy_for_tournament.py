#!/usr/bin/env python3
"""Rank deploy commits for main tournament lock-in.

Usage:
  uv run python scripts/pick_deploy_for_tournament.py
  uv run python scripts/pick_deploy_for_tournament.py --min-eval-bb100 -15 --limit 10
  uv run python scripts/pick_deploy_for_tournament.py --lock --label s1b-final --commit abc1234
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "examples"))

from deploy_registry import (  # noqa: E402
    append_tournament_candidate,
    format_pick_report,
    pick_deploy_for_tournament,
)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Pick tournament deploy candidate")
    p.add_argument("--min-eval-bb100", type=float, default=-17.45)
    p.add_argument("--limit", type=int, default=5)
    p.add_argument("--include-fail", action="store_true", help="Include sub-floor eval commits")
    p.add_argument("--lock", action="store_true", help="Write tournament_candidate.json for commit")
    p.add_argument("--commit", default="", help="Commit to lock (default: top pick)")
    p.add_argument("--label", default="tournament-candidate")
    p.add_argument(
        "--competition-id",
        default="",
        help="Playground comp id for manifest (default: from state.json)",
    )
    p.add_argument("--rationale", default="")
    args = p.parse_args(argv)

    if args.lock:
        picks = pick_deploy_for_tournament(
            min_eval_bb100=args.min_eval_bb100,
            require_eval_pass=not args.include_fail,
            limit=args.limit,
        )
        commit = args.commit or (picks[0]["commit"] if picks else "")
        if not commit:
            print("No commit to lock — deploy and run eval smoke first.", file=sys.stderr)
            return 1
        comp = args.competition_id
        if not comp:
            from deploy_registry import read_state

            comp = read_state(_ROOT).get("competition_id", "")
        row = append_tournament_candidate(
            label=args.label,
            commit=commit,
            competition_id=comp or "",
            rationale=args.rationale,
            lock=True,
        )
        print(f"Locked tournament candidate → reports/hl-loop/tournament_candidate.json")
        print(f"  commit={row['commit']}  eval={row['scorecard'].get('eval_bb100')}")
        return 0

    picks = pick_deploy_for_tournament(
        min_eval_bb100=args.min_eval_bb100,
        require_eval_pass=not args.include_fail,
        limit=args.limit,
    )
    print(format_pick_report(picks, min_eval_bb100=args.min_eval_bb100))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
