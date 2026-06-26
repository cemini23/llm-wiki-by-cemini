#!/usr/bin/env bash
# K130 Track A — PokerKit stack confirmation smoke.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "==> Verifying pyproject PokerKit pin + import smoke"
uv run python - <<'PY'
from __future__ import annotations

import importlib
import importlib.metadata
from pathlib import Path
import tomllib

root = Path.cwd()
data = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))
deps = data["project"]["dependencies"]
needle = "pokerkit>=0.5"

if needle not in deps:
    raise SystemExit(f"missing required dependency pin: {needle}")

importlib.import_module("pokerkit")
print(f"pyproject pin OK: {needle}")
print(f"installed pokerkit version: {importlib.metadata.version('pokerkit')}")
PY

echo "==> Shell syntax smoke"
bash -n "scripts/verify_pokerkit_stack.sh"

echo "==> Pytest smoke"
uv run pytest tests/test_pokerkit_stack_smoke.py -q

echo "==> Optional Track C timing hint"
uv run python - <<'PY'
from __future__ import annotations

import sys
import time
from pathlib import Path

examples = Path.cwd() / "examples"
if str(examples) not in sys.path:
    sys.path.insert(0, str(examples))

try:
    import agent
except Exception as exc:  # pragma: no cover - advisory only
    print(f"treys timing skipped: {exc}")
else:
    if not getattr(agent, "_HAS_TREYS", False):
        print("treys timing skipped: treys backend unavailable")
        raise SystemExit(0)
    hole = ["Ah", "Kh"]
    board = ["Qs", "Jh", "2c"]
    samples = 50
    sims = 200
    t0 = time.perf_counter()
    for _ in range(samples):
        agent.estimate_equity(hole, board, sims=sims, deadline_s=2.0)
    elapsed_ms = (time.perf_counter() - t0) * 1000.0
    print(
        "estimate_equity timing: "
        f"{elapsed_ms:.1f} ms total "
        f"({elapsed_ms / samples:.2f} ms/call, sims={sims}, samples={samples})"
    )
PY

echo "==> Operator checklist"
echo "Run after each Researcher season: pokerkit run --max-hands 5"
echo "PokerKit stack verification OK"
