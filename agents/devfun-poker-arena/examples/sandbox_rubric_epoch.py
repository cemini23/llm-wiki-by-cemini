"""Rubric epoch versioning for tri-verifier (K134 RQGM).

Implements versioned rubric epochs, GT-gated evaluator promotion (advisory),
and selective erasure of stale leaderboard rows.

Stdlib only - no external dependencies.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Import path setup for sandbox_tri_verifier and k134_holdout
_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

_HELPERS = Path(__file__).resolve().parent.parent / "tests" / "helpers"
if str(_HELPERS) not in sys.path:
    sys.path.insert(0, str(_HELPERS))


def _default_config_path() -> Path:
    """Resolve default config path relative to repo root."""
    return Path(__file__).resolve().parents[1] / "config" / "rubric_epoch.json"


def load_rubric_config(path: str | Path | None = None) -> dict:
    """Load rubric_epoch.json; raise FileNotFoundError if missing and no default."""
    config_path = Path(path) if path else _default_config_path()
    if not config_path.is_file():
        raise FileNotFoundError(f"rubric config not found: {config_path}")
    with config_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def current_epoch(config: dict) -> int:
    """Return current epoch from config."""
    return int(config.get("epoch", 1))


def rubric_fingerprint(config: dict) -> str:
    """SHA256 hash over weights+thresholds (deterministic, order-independent)."""
    weights = config.get("weights", {})
    thresholds = config.get("thresholds", {})
    # Canonical JSON with sorted keys
    canonical = json.dumps({"weights": weights, "thresholds": thresholds}, sort_keys=True)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def evaluator_id(config: dict) -> str:
    """Return deterministic evaluator ID: tri-v{rubric_version}-e{epoch}-{fp8}."""
    ver = config.get("rubric_version", 1)
    epoch = current_epoch(config)
    fp = rubric_fingerprint(config)
    return f"tri-v{ver}-e{epoch}-{fp[:8]}"


def annotate_report(report: dict, config: dict) -> dict:
    """Return shallow copy of report with rubric_epoch, rubric_version, evaluator_id added.

    Does not mutate input. Works on both ActionScore and TrajectoryScore shapes.
    """
    out = dict(report)
    out["rubric_epoch"] = current_epoch(config)
    out["rubric_version"] = config.get("rubric_version", 1)
    out["evaluator_id"] = evaluator_id(config)
    return out


def thresholds_from_config(config: dict) -> dict:
    """Return thresholds dict for passing into verifier helpers."""
    thr = config.get("thresholds", {})
    return {
        "deadline_hard_s": thr.get("efficiency_hard_deadline_s", 10.0),
        "soft_ratio": thr.get("efficiency_soft_ratio", 0.9),
        "max_poll_loops": thr.get("max_idle_poll_loops", 3),
    }


def _try_import_sandbox_tri_verifier() -> Any:
    """Try to import sandbox_tri_verifier, return None on failure."""
    try:
        import sandbox_tri_verifier
        return sandbox_tri_verifier
    except Exception:
        return None


def _try_import_holdout_suite() -> list[dict] | None:
    """Try to import holdout_suite_v1, return None on failure."""
    try:
        from k134_holdout import holdout_suite_v1
        return holdout_suite_v1()
    except Exception:
        return None


def score_holdout_suite(config: dict, suite: list[dict] | None = None) -> dict:
    """Score golden-labeled hold-out suite under config's thresholds.

    Returns:
        {"suite": name, "total": int, "passed": int, "pass_rate": float,
         "evaluator_id": str, "epoch": int}
    """
    verifier = _try_import_sandbox_tri_verifier()
    if verifier is None:
        raise ImportError("sandbox_tri_verifier not available")

    if suite is None:
        suite = _try_import_holdout_suite()
        if suite is None:
            raise ImportError("k134_holdout not available")

    thresholds = thresholds_from_config(config)
    passed = 0
    total = len(suite)

    for row in suite:
        # Score with parameterized thresholds
        score = verifier.score_action(
            action=row["action"],
            allowed_actions=row["allowed_actions"],
            elapsed_s=row["elapsed_s"],
            deadline_s=row["deadline_s"],
            action_payload=row["payload"],
            table=row.get("table"),
            poll_loops=row.get("poll_loops", 0),
            thresholds=thresholds,
        )
        # Agreement: evaluator pass matches gt_pass
        evaluator_pass = score.get("pass", False)
        gt_pass = row.get("gt_pass", False)
        if evaluator_pass == gt_pass:
            passed += 1

    return {
        "suite": config.get("promotion", {}).get("holdout_suite", "unknown"),
        "total": total,
        "passed": passed,
        "pass_rate": passed / total if total > 0 else 0.0,
        "evaluator_id": evaluator_id(config),
        "epoch": current_epoch(config),
    }


def promotion_gate(incumbent: dict, challenger: dict, config: dict) -> dict:
    """Compare two score_holdout_suite results; return advisory promotion verdict.

    Returns:
        {"verdict": "PROMOTE"|"HOLD", "advisory": bool, "incumbent_pass_rate": float,
         "challenger_pass_rate": float, "epsilon": float, "delta": float, "reason": str}
    """
    inc_rate = incumbent.get("pass_rate", 0.0)
    chal_rate = challenger.get("pass_rate", 0.0)
    epsilon = config.get("promotion", {}).get("epsilon", 0.0)
    advisory_only = config.get("promotion", {}).get("advisory_only", True)

    delta = chal_rate - inc_rate
    promote = delta > epsilon

    verdict = "PROMOTE" if promote else "HOLD"
    reason = (
        f"challenger {chal_rate:.4f} vs incumbent {inc_rate:.4f}, delta {delta:.4f} > epsilon {epsilon}"
        if promote
        else f"challenger {chal_rate:.4f} vs incumbent {inc_rate:.4f}, delta {delta:.4f} <= epsilon {epsilon}"
    )

    return {
        "verdict": verdict,
        "advisory": advisory_only,
        "incumbent_pass_rate": inc_rate,
        "challenger_pass_rate": chal_rate,
        "epsilon": epsilon,
        "delta": delta,
        "reason": reason,
    }


def promote_epoch(
    config: dict, gate: dict, *, path: str | Path | None = None, dry_run: bool = True
) -> dict:
    """Bump epoch if gate advises PROMOTE (and not advisory-only, and not dry_run).

    Returns updated config (in-memory). Only writes to disk if dry_run=False and
    promotion is not advisory_only.
    """
    if gate.get("verdict") != "PROMOTE":
        return config

    advisory_only = config.get("promotion", {}).get("advisory_only", True)
    if advisory_only or dry_run:
        # Advisory or dry-run: return would-be config without writing
        new_config = dict(config)
        new_epoch = current_epoch(config) + 1
        new_config["epoch"] = new_epoch
        new_config["evaluator_id"] = evaluator_id(new_config)
        history_entry = {
            "epoch": new_epoch,
            "rubric_version": new_config.get("rubric_version", 1),
            "promoted_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "reason": gate.get("reason", "promotion via gate"),
            "evaluator_id": new_config["evaluator_id"],
        }
        new_config["history"] = list(config.get("history", [])) + [history_entry]
        return new_config

    # Actual promotion (non-advisory, dry_run=False)
    config_path = Path(path) if path else _default_config_path()

    new_config = dict(config)
    new_epoch = current_epoch(config) + 1
    new_config["epoch"] = new_epoch

    # Check if weights changed -> bump rubric_version
    # (simplified: always same version for threshold-only changes)
    new_config["evaluator_id"] = evaluator_id(new_config)

    history_entry = {
        "epoch": new_epoch,
        "rubric_version": new_config.get("rubric_version", 1),
        "promoted_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "reason": gate.get("reason", "promotion via gate"),
        "evaluator_id": new_config["evaluator_id"],
    }
    new_config["history"] = list(config.get("history", [])) + [history_entry]

    # Atomic write
    tmp_path = config_path.with_suffix(".tmp")
    with tmp_path.open("w", encoding="utf-8") as f:
        json.dump(new_config, f, indent=2)
    os.replace(tmp_path, config_path)

    return new_config


def mark_superseded(
    index_path: str | Path,
    new_epoch: int,
    *,
    prior_epoch: int | None = None,
    dry_run: bool = True,
) -> int:
    """P1 - Stamp superseded_by_epoch onto prior index rows (never delete trajectories).

    Returns count of rows superseded.
    """
    index_path = Path(index_path)
    if not index_path.is_file():
        return 0

    rows = []
    with index_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
                rows.append(row)
            except json.JSONDecodeError:
                continue

    superseded_count = 0
    updated_rows = []

    for row in rows:
        row_epoch = row.get("rubric_epoch")
        already_superseded = row.get("superseded_by_epoch")

        # Supersede if epoch is absent OR < new_epoch, and not already superseded
        should_supersede = (
            not already_superseded
            and (row_epoch is None or row_epoch < new_epoch)
        )

        if should_supersede:
            row["superseded_by_epoch"] = new_epoch
            superseded_count += 1

            # Also stamp per-bundle axis_summary.json if present
            bundle_dir = row.get("bundle_dir")
            if bundle_dir:
                axis_path = Path(bundle_dir) / "axis_summary.json"
                if axis_path.is_file() and not dry_run:
                    try:
                        with axis_path.open("r", encoding="utf-8") as f:
                            axis_data = json.load(f)
                        axis_data["superseded_by_epoch"] = new_epoch
                        with axis_path.open("w", encoding="utf-8") as f:
                            json.dump(axis_data, f, indent=2)
                    except Exception:
                        pass  # Best effort

        updated_rows.append(row)

    if not dry_run and superseded_count > 0:
        # Atomic rewrite
        tmp_path = index_path.with_suffix(".tmp")
        with tmp_path.open("w", encoding="utf-8") as f:
            for row in updated_rows:
                f.write(json.dumps(row, sort_keys=True) + "\n")
        os.replace(tmp_path, index_path)

    return superseded_count


def adversarial_audit(events: list[dict], config: dict) -> dict:
    """P2 - Detect LLM-judge over-acceptance vs harness legality.

    Heuristic: judge_pass = reasoning not empty (models LLM over-acceptance).
    Count events where judge says OK but harness says hazard.

    Returns:
        {"total": n, "over_accept": k, "over_accept_rate": float,
         "by_hazard": {...}, "recommend_debias_epoch": bool}
    """
    verifier = _try_import_sandbox_tri_verifier()
    thresholds = thresholds_from_config(config)

    total = len(events)
    over_accept = 0
    by_hazard: dict[str, int] = {}

    for evt in events:
        payload = evt.get("payload", {})
        # Judge passes if any reasoning present (heuristic for over-acceptance)
        judge_pass = bool(
            payload.get("reasoning") or payload.get("reasoning_text") or payload.get("message")
        )

        # Harness evaluation
        if verifier is not None:
            score = verifier.score_action(
                action=evt.get("action", ""),
                allowed_actions=evt.get("allowed_actions", []),
                elapsed_s=evt.get("elapsed_s", 0.0),
                deadline_s=evt.get("deadline_s", 10.0),
                action_payload=payload,
                table=evt.get("table"),
                poll_loops=evt.get("poll_loops", 0),
                thresholds=thresholds,
            )
            harness_pass = score.get("pass", False)
            dims = score.get("dimensions", {})
            hazard = None
            for dim_name, dim_data in dims.items():
                if not dim_data.get("pass", False):
                    hazard = dim_data.get("hazard")
                    break
        else:
            # Fallback: assume pass if no verifier
            harness_pass = True
            hazard = None

        if judge_pass and not harness_pass:
            over_accept += 1
            if hazard:
                by_hazard[hazard] = by_hazard.get(hazard, 0) + 1

    over_accept_rate = over_accept / total if total > 0 else 0.0
    recommend_debias = over_accept_rate > 0.2  # Advisory threshold

    return {
        "total": total,
        "over_accept": over_accept,
        "over_accept_rate": over_accept_rate,
        "by_hazard": by_hazard,
        "recommend_debias_epoch": recommend_debias,
    }


def _load_trajectory_jsonl(path: str | Path) -> list[dict]:
    """Load trajectory JSONL file."""
    path = Path(path)
    if not path.is_file():
        return []
    events = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return events


def main(argv: list[str] | None = None) -> int:
    """CLI for rubric epoch operations."""
    p = argparse.ArgumentParser(description="Rubric epoch versioning (K134)")
    p.add_argument("--config", type=Path, default=None, help="Path to rubric_epoch.json")
    p.add_argument("--print", action="store_true", help="Print active epoch + evaluator_id")
    p.add_argument("--holdout", action="store_true", help="Score hold-out suite, print pass_rate")
    p.add_argument("--gate", action="store_true", help="Advisory promotion gate (identity)")
    p.add_argument("--supersede", type=int, metavar="N", help="Stamp superseded_by_epoch=N on index")
    p.add_argument("--adversarial-audit", type=Path, metavar="TRAJ", help="P2 audit on trajectory")
    p.add_argument("--apply", action="store_true", help="Actually write (promotion/supersede)")
    args = p.parse_args(argv)

    # Load config once
    try:
        cfg = load_rubric_config(args.config)
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    if getattr(args, "print"):
        print(f"epoch: {current_epoch(cfg)}")
        print(f"evaluator_id: {evaluator_id(cfg)}")
        print(f"rubric_version: {cfg.get('rubric_version', 1)}")
        print(f"frozen: {cfg.get('frozen', False)}")
        return 0

    if args.holdout:
        try:
            result = score_holdout_suite(cfg)
            print(f"suite: {result['suite']}")
            print(f"total: {result['total']}")
            print(f"passed: {result['passed']}")
            print(f"pass_rate: {result['pass_rate']:.4f}")
            print(f"evaluator_id: {result['evaluator_id']}")
            print(f"epoch: {result['epoch']}")
            return 0
        except ImportError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 1

    if args.gate:
        # Identity gate: incumbent = challenger = current config
        try:
            incumbent = score_holdout_suite(cfg)
            # For identity comparison, challenger is same config
            gate = promotion_gate(incumbent, incumbent, cfg)
            print(f"verdict: {gate['verdict']}")
            print(f"advisory: {gate['advisory']}")
            print(f"incumbent_pass_rate: {gate['incumbent_pass_rate']:.4f}")
            print(f"challenger_pass_rate: {gate['challenger_pass_rate']:.4f}")
            print(f"epsilon: {gate['epsilon']:.4f}")
            print(f"delta: {gate['delta']:.4f}")
            print(f"reason: {gate['reason']}")
            return 0
        except ImportError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 1

    if args.supersede is not None:
        index_path = Path("reports/hl-loop/researcher_trajectory_index.jsonl")
        count = mark_superseded(
            index_path,
            args.supersede,
            dry_run=not args.apply,
        )
        action = "would supersede" if not args.apply else "superseded"
        print(f"{action} {count} rows < epoch {args.supersede} (raw trajectories preserved)")
        return 0

    if args.adversarial_audit:
        events = _load_trajectory_jsonl(args.adversarial_audit)
        if not events:
            print(f"ERROR: no events loaded from {args.adversarial_audit}", file=sys.stderr)
            return 1
        audit = adversarial_audit(events, cfg)
        print(f"total: {audit['total']}")
        print(f"over_accept: {audit['over_accept']}")
        print(f"over_accept_rate: {audit['over_accept_rate']:.4f}")
        print(f"by_hazard: {audit['by_hazard']}")
        print(f"recommend_debias_epoch: {audit['recommend_debias_epoch']}")

        # Write report
        ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        report_path = Path(f"reports/hl-loop/adversarial_audit-{ts}.json")
        report_path.parent.mkdir(parents=True, exist_ok=True)
        with report_path.open("w", encoding="utf-8") as f:
            json.dump(audit, f, indent=2)
        print(f"report: {report_path}")
        return 0

    # Default: --print behavior
    print(f"epoch: {current_epoch(cfg)}")
    print(f"evaluator_id: {evaluator_id(cfg)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
