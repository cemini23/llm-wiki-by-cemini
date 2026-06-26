from __future__ import annotations

import re
from pathlib import Path


def test_harvest_script_uses_venv_python() -> None:
    script = Path("scripts/run_sandbox_season_harvest.sh").read_text(encoding="utf-8")

    assert "venv/bin/python" in script
    assert "\"${PY[@]}\" examples/export_competition_hands.py" in script
    assert "\"${PY[@]}\" - <<'PY'" in script
    assert re.search(r"(?<!command -v )uv run python", script) is None
