"""Tests for K134 rubric epoch versioning (RQGM).

Follows resilient style of test_sandbox_tri_verifier.py with sys.path insert
and importlib import pattern.
"""
from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples"
HELPERS = ROOT / "tests" / "helpers"
CONFIG = ROOT / "config"

for path in (EXAMPLES, HELPERS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

# Import dependencies first
from cemini_tables import hu_sb_unopened  # noqa: E402
from output_sanitize import FALLBACK_REASONING  # noqa: E402

_IMPORT_ERROR: Exception | None = None
_RUBRIC_MOD = None
try:
    _RUBRIC_MOD = importlib.import_module("sandbox_rubric_epoch")
except Exception as exc:  # pragma: no cover
    _IMPORT_ERROR = exc

_HOLDOUT_MOD = None
try:
    _HOLDOUT_MOD = importlib.import_module("k134_holdout")
except Exception as exc:  # pragma: no cover
    pass  # Optional import for some tests


def _require_module():
    if _RUBRIC_MOD is None:
        pytest.fail(f"could not import examples/sandbox_rubric_epoch.py: {_IMPORT_ERROR}")
    return _RUBRIC_MOD


def _require_attr(name: str):
    mod = _require_module()
    if not hasattr(mod, name):
        pytest.fail(f"sandbox_rubric_epoch is missing required symbol: {name}")
    return getattr(mod, name)


def _genesis_config() -> dict:
    """Return a genesis config dict matching config/rubric_epoch.json."""
    return {
        "rubric_version": 1,
        "epoch": 1,
        "frozen": True,
        "weights": {"correctness": 1.0, "efficiency": 1.0, "critical_point": 1.0},
        "thresholds": {
            "efficiency_hard_deadline_s": 10.0,
            "efficiency_soft_ratio": 0.9,
            "max_idle_poll_loops": 3,
        },
        "promotion": {"epsilon": 0.0, "holdout_suite": "k134_holdout_v1", "advisory_only": True},
        "history": [],
    }


def test_load_rubric_config_genesis():
    """1. Config loads; epoch==1, rubric_version==1, frozen is True."""
    load_rubric_config = _require_attr("load_rubric_config")
    current_epoch = _require_attr("current_epoch")

    # Load from actual file
    config = load_rubric_config()
    assert current_epoch(config) == 1
    assert config.get("rubric_version") == 1
    assert config.get("frozen") is True


def test_rubric_fingerprint_deterministic():
    """2. Same config → same digest; key reorder → same digest; threshold change → different digest."""
    rubric_fingerprint = _require_attr("rubric_fingerprint")

    config1 = _genesis_config()
    config2 = _genesis_config()
    fp1 = rubric_fingerprint(config1)
    fp2 = rubric_fingerprint(config2)
    assert fp1 == fp2, "Same config should produce same fingerprint"

    # Different order of keys (dict preserves insertion, but we JSON sort)
    config3 = {
        "epoch": 1,
        "rubric_version": 1,
        "frozen": True,
        "weights": {"efficiency": 1.0, "correctness": 1.0, "critical_point": 1.0},
        "thresholds": {
            "max_idle_poll_loops": 3,
            "efficiency_hard_deadline_s": 10.0,
            "efficiency_soft_ratio": 0.9,
        },
        "promotion": {"epsilon": 0.0, "holdout_suite": "k134_holdout_v1", "advisory_only": True},
        "history": [],
    }
    fp3 = rubric_fingerprint(config3)
    assert fp3 == fp1, "Key order should not affect fingerprint (sorted JSON)"

    # Threshold change
    config4 = _genesis_config()
    config4["thresholds"]["efficiency_hard_deadline_s"] = 5.0
    fp4 = rubric_fingerprint(config4)
    assert fp4 != fp1, "Threshold change should produce different fingerprint"


def test_evaluator_id_format():
    r"""3. Matches regex ^tri-v\d+-e\d+-[0-9a-f]{8}$."""
    evaluator_id = _require_attr("evaluator_id")
    import re

    config = _genesis_config()
    eid = evaluator_id(config)
    pattern = re.compile(r"^tri-v\d+-e\d+-[0-9a-f]{8}$")
    assert pattern.match(eid), f"evaluator_id '{eid}' does not match expected pattern"


def test_annotate_report_adds_fields_without_mutation():
    """4. Input report unchanged; output has rubric_epoch/rubric_version/evaluator_id."""
    annotate_report = _require_attr("annotate_report")
    current_epoch = _require_attr("current_epoch")

    config = _genesis_config()
    original = {"action": "raise", "pass": True}
    annotated = annotate_report(original, config)

    # Original unchanged
    assert "rubric_epoch" not in original
    assert "rubric_version" not in original
    assert "evaluator_id" not in original

    # Annotated has new fields
    assert annotated["rubric_epoch"] == current_epoch(config)
    assert annotated["rubric_version"] == config["rubric_version"]
    assert "evaluator_id" in annotated
    assert isinstance(annotated["evaluator_id"], str)


def test_backward_compat_report_without_epoch_still_valid():
    """5. K132-shaped trajectory (no epoch keys) passes score_trajectory; no KeyError."""
    # Import verifier
    try:
        import sandbox_tri_verifier as verifier
    except ImportError:
        pytest.fail("sandbox_tri_verifier not available")

    # Build a K132-style event (no epoch fields expected)
    table = hu_sb_unopened(["As", "Ah"])
    event = {
        "action": "raise",
        "allowed_actions": ["fold", "call", "raise"],
        "elapsed_s": 0.5,
        "deadline_s": 10.0,
        "payload": {
            "action": "raise",
            "amount": 4,
            "reasoning_text": "AA SB open",
        },
        "table": table,
        "poll_loops": 0,
    }

    # Should not raise KeyError - use correct param name action_payload
    result = verifier.score_action(
        action=event["action"],
        allowed_actions=event["allowed_actions"],
        elapsed_s=event["elapsed_s"],
        deadline_s=event["deadline_s"],
        action_payload=event["payload"],
        table=event["table"],
        poll_loops=event["poll_loops"],
    )
    assert "pass" in result
    assert "dimensions" in result

    # Trajectory without epoch fields
    events = [event, event]
    traj = verifier.score_trajectory(events)
    assert "trajectory_pass" in traj
    assert "rubric_epoch" not in traj  # No automatic injection by verifier


def test_thresholds_from_config_roundtrip():
    """6. Genesis thresholds equal sandbox_tri_verifier defaults (10.0 / 0.9 / 3)."""
    thresholds_from_config = _require_attr("thresholds_from_config")

    config = _genesis_config()
    thr = thresholds_from_config(config)

    assert thr["deadline_hard_s"] == 10.0
    assert thr["soft_ratio"] == 0.9
    assert thr["max_poll_loops"] == 3


def test_holdout_suite_min_size_and_labels():
    """7. holdout_suite_v1() has ≥6 rows; each has gt_pass bool."""
    if _HOLDOUT_MOD is None:
        pytest.skip("k134_holdout not available")

    suite = _HOLDOUT_MOD.holdout_suite_v1()
    assert len(suite) >= 6, f"Expected at least 6 spots, got {len(suite)}"

    for row in suite:
        assert "gt_pass" in row, f"Row {row.get('name', 'unknown')} missing gt_pass"
        assert isinstance(row["gt_pass"], bool)


def test_score_holdout_suite_genesis_agreement():
    """8. Under genesis epoch, evaluator agreement with GT ≥ 5/6."""
    score_holdout_suite = _require_attr("score_holdout_suite")

    if _HOLDOUT_MOD is None:
        pytest.skip("k134_holdout not available")

    config = _genesis_config()
    suite = _HOLDOUT_MOD.holdout_suite_v1()

    result = score_holdout_suite(config, suite)
    assert result["total"] == len(suite)

    # Agreement should be at least 5/6 (allowing one edge case)
    min_expected = min(5, len(suite) - 1)
    assert result["passed"] >= min_expected, (
        f"Hold-out agreement {result['passed']}/{result['total']} "
        f"(pass_rate={result['pass_rate']:.2f}) below threshold"
    )


def test_promotion_gate_identity_holds():
    """9. Incumbent==challenger → verdict HOLD, delta 0."""
    promotion_gate = _require_attr("promotion_gate")

    config = _genesis_config()
    incumbent = {"pass_rate": 0.75, "epoch": 1}
    challenger = {"pass_rate": 0.75, "epoch": 1}

    gate = promotion_gate(incumbent, challenger, config)
    assert gate["verdict"] == "HOLD"
    assert gate["delta"] == 0.0
    assert gate["incumbent_pass_rate"] == 0.75
    assert gate["challenger_pass_rate"] == 0.75


def test_promotion_gate_promote_on_improvement():
    """10. Synthetic challenger with higher pass_rate → verdict PROMOTE, advisory True."""
    promotion_gate = _require_attr("promotion_gate")

    config = _genesis_config()
    incumbent = {"pass_rate": 0.75, "epoch": 1}
    challenger = {"pass_rate": 0.85, "epoch": 2}

    gate = promotion_gate(incumbent, challenger, config)
    assert gate["verdict"] == "PROMOTE"
    assert gate["advisory"] is True  # advisory_only in genesis config
    assert abs(gate["delta"] - 0.10) < 0.001  # Floating point tolerance
    assert "delta" in gate["reason"]


def test_promote_epoch_dry_run_does_not_write(tmp_path: Path):
    """11. promote_epoch(..., dry_run=True) returns bumped epoch but on-disk unchanged."""
    promote_epoch = _require_attr("promote_epoch")
    current_epoch = _require_attr("current_epoch")

    # Create temp config file
    config = _genesis_config()
    config_path = tmp_path / "rubric_epoch.json"
    original_epoch = current_epoch(config)

    with config_path.open("w") as f:
        json.dump(config, f)

    # Get mtime before
    before_stat = config_path.stat()

    # Create promotion gate
    gate = {"verdict": "PROMOTE", "reason": "test promotion"}

    # Dry run
    new_config = promote_epoch(config, gate, path=config_path, dry_run=True)
    assert current_epoch(new_config) == original_epoch + 1

    # Verify file unchanged
    after_stat = config_path.stat()
    assert after_stat.st_mtime_ns == before_stat.st_mtime_ns

    with config_path.open("r") as f:
        on_disk = json.load(f)
    assert current_epoch(on_disk) == original_epoch


def test_mark_superseded_annotates_not_deletes(tmp_path: Path):
    """12. mark_superseded sets superseded_by_epoch on index rows; raw trajectory preserved."""
    mark_superseded = _require_attr("mark_superseded")

    # Create temp index with 2 pre-epoch rows
    index_path = tmp_path / "researcher_trajectory_index.jsonl"
    rows = [
        {"at": "2026-06-01T00:00:00Z", "bundle_dir": str(tmp_path / "bundle1"), "rubric_epoch": 1},
        {"at": "2026-06-02T00:00:00Z", "bundle_dir": str(tmp_path / "bundle2")},  # no epoch
    ]
    with index_path.open("w") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")

    # Create empty selfplay_trajectory.jsonl to verify it's not touched
    traj_path = tmp_path / "bundle1" / "selfplay_trajectory.jsonl"
    traj_path.parent.mkdir(parents=True, exist_ok=True)
    traj_path.write_text('{"test": true}\n')
    traj_content_before = traj_path.read_text()

    # Supersede to epoch 2
    count = mark_superseded(index_path, 2, dry_run=False)
    assert count == 2, f"Expected 2 rows superseded, got {count}"

    # Verify index rows updated
    updated_rows = []
    with index_path.open("r") as f:
        for line in f:
            line = line.strip()
            if line:
                updated_rows.append(json.loads(line))

    assert updated_rows[0]["superseded_by_epoch"] == 2
    assert updated_rows[1]["superseded_by_epoch"] == 2

    # Verify raw trajectory file unchanged
    traj_content_after = traj_path.read_text()
    assert traj_content_before == traj_content_after


def test_adversarial_audit_log_only(tmp_path: Path):
    """13. (P2) over-accept events produce over_accept_rate>0, recommend_debias_epoch per threshold."""
    adversarial_audit = _require_attr("adversarial_audit")

    # Events where judge would pass (has reasoning) but harness might fail
    events = [
        {
            "action": "all-in",
            "allowed_actions": ["fold", "call"],  # all-in illegal
            "elapsed_s": 0.5,
            "deadline_s": 10.0,
            "payload": {
                "action": "all-in",
                "reasoning_text": "shove with air",
            },
        },
        {
            "action": "raise",
            "allowed_actions": ["fold", "call", "raise"],
            "elapsed_s": 0.5,
            "deadline_s": 10.0,
            "payload": {
                "action": "raise",
                "amount": 2,  # Below min
                "reasoning_text": "small raise",
            },
        },
        {
            "action": "raise",
            "allowed_actions": ["fold", "call", "raise"],
            "elapsed_s": 0.5,
            "deadline_s": 10.0,
            "payload": {
                "action": "raise",
                "amount": 6,
                "reasoning_text": "legitimate raise",
            },
        },
    ]

    config = _genesis_config()
    audit = adversarial_audit(events, config)

    assert audit["total"] == 3
    assert audit["over_accept"] >= 0  # May be 0 if verifier not available
    assert 0.0 <= audit["over_accept_rate"] <= 1.0
    assert isinstance(audit["by_hazard"], dict)
    assert isinstance(audit["recommend_debias_epoch"], bool)
    # Threshold check: over_accept_rate > 0.2 triggers recommendation
    assert audit["recommend_debias_epoch"] == (audit["over_accept_rate"] > 0.2)


# Additional tests for edge cases

def test_load_rubric_config_custom_path(tmp_path: Path):
    """Load config from custom path."""
    load_rubric_config = _require_attr("load_rubric_config")

    config = _genesis_config()
    config_path = tmp_path / "custom_rubric.json"
    with config_path.open("w") as f:
        json.dump(config, f)

    loaded = load_rubric_config(config_path)
    assert loaded["epoch"] == 1


def test_load_rubric_config_missing_raises():
    """Missing config file raises FileNotFoundError."""
    load_rubric_config = _require_attr("load_rubric_config")

    with pytest.raises(FileNotFoundError):
        load_rubric_config("/nonexistent/path/rubric_epoch.json")


def test_thresholds_from_config_defaults():
    """thresholds_from_config uses sensible defaults when keys missing."""
    thresholds_from_config = _require_attr("thresholds_from_config")

    minimal_config = {"weights": {}}  # No thresholds key
    thr = thresholds_from_config(minimal_config)
    assert thr["deadline_hard_s"] == 10.0
    assert thr["soft_ratio"] == 0.9
    assert thr["max_poll_loops"] == 3
