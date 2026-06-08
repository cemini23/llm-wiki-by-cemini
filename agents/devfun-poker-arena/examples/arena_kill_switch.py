#!/usr/bin/env python3
"""Kill switch control for dev.fun poker lobby."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from hl_runtime_config import (  # noqa: E402
    activate_kill_switch,
    clear_kill_switch,
    kill_switch_status,
)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Arena poker kill switch")
    sub = p.add_subparsers(dest="cmd", required=True)

    st = sub.add_parser("status", help="Show kill switch state")
    st.set_defaults(cmd="status")

    act = sub.add_parser("activate", help="Stop aggressive play (fold/check only)")
    act.add_argument("--reason", required=True)
    act.add_argument("--severity", default="catastrophic")
    act.set_defaults(cmd="activate")

    clr = sub.add_parser("clear", help="Resume normal play")
    clr.add_argument("--reason", default="operator clear")
    clr.set_defaults(cmd="clear")

    args = p.parse_args(argv)

    if args.cmd == "status":
        print(json.dumps(kill_switch_status(), indent=2))
        return 0
    if args.cmd == "activate":
        out = activate_kill_switch(reason=args.reason, severity=args.severity, source="cli")
        print(json.dumps(out, indent=2))
        print("Lobby will fold/check only until cleared.")
        return 0
    if args.cmd == "clear":
        out = clear_kill_switch(reason=args.reason, source="cli")
        print(json.dumps(out, indent=2))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
