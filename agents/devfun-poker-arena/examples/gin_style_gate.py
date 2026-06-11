#!/usr/bin/env python3
"""Deploy gate: gin-style aggression vs simple opponent + VPIP floor.

Usage:
    CEMINI_GIN_STYLE=1 uv run python examples/gin_style_gate.py --gate
    uv run python examples/gin_style_gate.py --hands 300 --gate
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from cemini_selfplay_audit import HeroAudit, _wrap_decide  # noqa: E402
from selfplay import _load_decide_from_path, run_selfplay  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Gin-style self-play deploy gate")
    p.add_argument("--hands", type=int, default=250)
    p.add_argument("--players", type=int, default=6)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--gate", action="store_true")
    p.add_argument("--min-bb", type=float, default=5.0, help="Min bb/100 vs tight-passive")
    p.add_argument("--min-vpip", type=float, default=0.18, help="Min hero VPIP rate")
    p.add_argument("--min-pfr", type=float, default=0.01, help="Min hero PFR rate (vs ~1.4% prod baseline)")
    args = p.parse_args(argv)

    os.environ.setdefault("CEMINI_GIN_STYLE", "1")
    os.environ.setdefault("CEMINI_GIN_STYLE_PREFLOP", "1")
    os.environ.setdefault("CEMINI_GIN_STYLE_POSTFLOP", "1")
    os.environ.setdefault("CEMINI_COLD_START_NO_STEAL", "0")
    os.environ.setdefault("TRAINING_OPPONENT_MODE", "rock")

    decide_path = _EXAMPLES / "cemini_decide.py"
    raw = _load_decide_from_path(str(decide_path))
    audit = HeroAudit()
    decide_fn = _wrap_decide(raw, audit)

    stats = run_selfplay(
        decide_fn=decide_fn,
        n_hands=args.hands,
        opponent_label="tight_passive",
        n_players=args.players,
        starting_stack=500,
        small_blind=10,
        big_blind=20,
        seed=args.seed,
        training_hud=True,
    )

    vpip_rate = audit.vpip / audit.preflop_seen if audit.preflop_seen else 0.0
    pfr_rate = audit.pfr / audit.preflop_seen if audit.preflop_seen else 0.0
    bb = stats["bb_per_100"]

    print("─" * 56)
    print(f"  gin-style gate  ({args.hands}h 6-max vs tight-passive  seed={args.seed})")
    print(f"  bb/100      : {bb:+.1f}  (min {args.min_bb:+.1f})")
    print(f"  VPIP        : {vpip_rate:.1%}  (min {args.min_vpip:.1%})")
    print(f"  PFR         : {pfr_rate:.1%}  (min {args.min_pfr:.1%})")
    print(f"  EP trash opens: {audit.ep_trash_raises}")
    print("─" * 56)

    failures: list[str] = []
    if bb < args.min_bb:
        failures.append(f"bb/100 {bb:+.1f} < {args.min_bb:+.1f}")
    if vpip_rate < args.min_vpip:
        failures.append(f"VPIP {vpip_rate:.1%} < {args.min_vpip:.1%}")
    if pfr_rate < args.min_pfr:
        failures.append(f"PFR {pfr_rate:.1%} < {args.min_pfr:.1%}")

    if failures:
        print("  GATE FAIL:")
        for f in failures:
            print(f"    • {f}")
        return 1 if args.gate else 0

    if args.gate:
        print("  GATE PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
