from __future__ import annotations

from pathlib import Path


def test_rlcard_not_in_pyproject() -> None:
    # Assert rlcard never enters pyproject.toml core/dev/optional dependencies
    pyproject_path = Path("pyproject.toml")
    assert pyproject_path.exists()
    content = pyproject_path.read_text(encoding="utf-8")
    assert "rlcard" not in content.lower()


def test_rlcard_scripts_exist() -> None:
    setup_script = Path("scripts/setup_rlcard_venv.sh")
    run_script = Path("scripts/run_rlcard_baseline_ablation.sh")
    ablation_py = Path("examples/rlcard_baseline_ablation.py")

    assert setup_script.exists()
    assert run_script.exists()
    assert ablation_py.exists()


def test_rlcard_setup_script_syntax() -> None:
    setup_script = Path("scripts/setup_rlcard_venv.sh")
    content = setup_script.read_text(encoding="utf-8")

    # Assert shebang
    assert content.startswith("#!/usr/bin/env bash")
    # Assert bash options set
    assert "set -euo pipefail" in content
    # Assert venv creation and rlcard installation
    assert ".venv-rlcard" in content
    assert "pip\" install" in content or "pip install" in content
    assert "rlcard" in content


def test_rlcard_run_script_syntax() -> None:
    run_script = Path("scripts/run_rlcard_baseline_ablation.sh")
    content = run_script.read_text(encoding="utf-8")

    assert content.startswith("#!/usr/bin/env bash")
    assert "set -euo pipefail" in content
    assert ".venv-rlcard" in content
    assert "examples/rlcard_baseline_ablation.py" in content
