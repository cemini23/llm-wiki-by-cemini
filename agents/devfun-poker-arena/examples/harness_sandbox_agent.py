"""Arena / selfplay wrapper — routes decide() through harness/strategy.py."""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parent.parent
_HARNESS = _ROOT / "harness"
if str(_HARNESS) not in sys.path:
    sys.path.insert(0, str(_HARNESS))


def decide(table: dict, deadline_s: float = 10.0) -> Any:
    from strategy import choose_action  # noqa: WPS433

    return choose_action(table)
