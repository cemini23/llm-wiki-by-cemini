"""Daily / on-demand aggregator for reviewer-agent cost telemetry.

Reads the NDJSON telemetry log produced by
:class:`conductor.reviewer.cost_telemetry.TelemetryWriter` and produces a
dashboard-ready JSON report: per-tool review count, token totals,
estimated cost using configurable DeepSeek-R1 pricing, and an
extrapolated monthly spend estimate.

This module is an offline tool — it is not called on the reviewer-agent
critical path. Run via ``python -m conductor.reviewer.cost_aggregator``.

Spec: openspec/changes/reviewer-agent-selective-trigger/specs/reviewer-agent-selective-trigger/spec.md
Tasks: openspec/changes/reviewer-agent-selective-trigger/tasks.md (3.2 / 3.3)
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

# DeepSeek-R1 public API pricing as of 2025-Q1.
#
#   Input  tokens: $0.55 per million  ->  5.5e-7 USD per token
#   Output tokens: $2.19 per million  ->  2.19e-6 USD per token
#
# These are defaults; operators MUST verify current pricing at
# https://api-docs.deepseek.com/quick_start/pricing before treating
# the dashboard number as a budget commitment. The aggregator surfaces
# the active price in every report so downstream consumers can audit.
DEFAULT_PRICE_INPUT_PER_TOKEN_USD = 0.00000055
DEFAULT_PRICE_OUTPUT_PER_TOKEN_USD = 0.00000219

_PRICING_SOURCE = "DeepSeek-R1 API public pricing 2025-Q1 (verify before budgeting)"


def aggregate(
    log_path: Union[str, Path],
    *,
    price_input_per_token_usd: float = DEFAULT_PRICE_INPUT_PER_TOKEN_USD,
    price_output_per_token_usd: float = DEFAULT_PRICE_OUTPUT_PER_TOKEN_USD,
    extrapolation_days: int = 30,
) -> Dict[str, Any]:
    """Aggregate a telemetry NDJSON log into a dashboard-ready report.

    Args:
        log_path: Path to the NDJSON telemetry log. Missing path yields
            a zero report (not an error — fresh deployments).
        price_input_per_token_usd: Per-token price for reviewer inputs.
        price_output_per_token_usd: Per-token price for reviewer outputs.
        extrapolation_days: Days to extrapolate observed cost for the
            ``monthly_estimate_usd`` field. Default 30.

    Returns:
        Dict with:
            * ``period_start`` / ``period_end`` — ISO timestamps of the
              earliest / latest record (``None`` if no records).
            * ``by_tool`` — ``{tool: {count, in_tokens, out_tokens,
              cost_usd}}``, sorted by tool name for deterministic output.
            * ``total`` — workspace-wide rollup with the same fields.
            * ``monthly_estimate_usd`` — observed cost scaled to a
              ``extrapolation_days``-day window.
            * ``pricing`` — active per-token prices + source string.

    Raises:
        ValueError: If a non-blank line in the log is malformed JSON or
            is missing the required ``tool`` string field.
    """
    log_path = Path(log_path)
    if not log_path.exists():
        return _empty_report(price_input_per_token_usd, price_output_per_token_usd)

    by_tool_raw: Dict[str, Dict[str, int]] = defaultdict(
        lambda: {"count": 0, "in_tokens": 0, "out_tokens": 0},
    )
    timestamps: List[str] = []

    with log_path.open("r", encoding="utf-8") as fh:
        for lineno, raw_line in enumerate(fh, start=1):
            line = raw_line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"malformed telemetry record at {log_path}:{lineno}: {exc}",
                ) from exc
            tool = entry.get("tool")
            if not isinstance(tool, str):
                raise ValueError(
                    f"telemetry record at {log_path}:{lineno} missing "
                    f"'tool' string field",
                )
            agg = by_tool_raw[tool]
            agg["count"] += 1
            agg["in_tokens"] += int(entry.get("in_tokens", 0))
            agg["out_tokens"] += int(entry.get("out_tokens", 0))
            ts = entry.get("ts")
            if isinstance(ts, str):
                timestamps.append(ts)

    if not by_tool_raw:
        return _empty_report(price_input_per_token_usd, price_output_per_token_usd)

    # Per-tool roll-up with cost. Sort by tool name for deterministic
    # JSON output (dashboards consume diffs of these files).
    by_tool_with_cost: Dict[str, Dict[str, Any]] = {}
    total_count = 0
    total_in = 0
    total_out = 0
    for tool in sorted(by_tool_raw.keys()):
        agg = by_tool_raw[tool]
        cost = (
            agg["in_tokens"] * price_input_per_token_usd
            + agg["out_tokens"] * price_output_per_token_usd
        )
        by_tool_with_cost[tool] = {
            "count": agg["count"],
            "in_tokens": agg["in_tokens"],
            "out_tokens": agg["out_tokens"],
            "cost_usd": round(cost, 6),
        }
        total_count += agg["count"]
        total_in += agg["in_tokens"]
        total_out += agg["out_tokens"]

    total_cost = (
        total_in * price_input_per_token_usd
        + total_out * price_output_per_token_usd
    )

    period_start = min(timestamps) if timestamps else None
    period_end = max(timestamps) if timestamps else None
    monthly_estimate = _extrapolate(
        total_cost, period_start, period_end, extrapolation_days,
    )

    return {
        "period_start": period_start,
        "period_end": period_end,
        "by_tool": by_tool_with_cost,
        "total": {
            "count": total_count,
            "in_tokens": total_in,
            "out_tokens": total_out,
            "cost_usd": round(total_cost, 6),
        },
        "monthly_estimate_usd": round(monthly_estimate, 4),
        "pricing": {
            "input_per_token_usd": price_input_per_token_usd,
            "output_per_token_usd": price_output_per_token_usd,
            "source": _PRICING_SOURCE,
        },
    }


def _empty_report(
    price_in: float,
    price_out: float,
) -> Dict[str, Any]:
    return {
        "period_start": None,
        "period_end": None,
        "by_tool": {},
        "total": {"count": 0, "in_tokens": 0, "out_tokens": 0, "cost_usd": 0.0},
        "monthly_estimate_usd": 0.0,
        "pricing": {
            "input_per_token_usd": price_in,
            "output_per_token_usd": price_out,
            "source": _PRICING_SOURCE,
        },
    }


def _extrapolate(
    observed_cost: float,
    period_start: Optional[str],
    period_end: Optional[str],
    days_target: int,
) -> float:
    """Scale observed cost to a ``days_target``-day window.

    Returns the observed cost unchanged if period bounds are missing
    or unparseable (conservative default — operator sees real cost,
    not an inflated estimate).
    """
    if not period_start or not period_end:
        return observed_cost
    try:
        start = datetime.fromisoformat(period_start)
        end = datetime.fromisoformat(period_end)
    except ValueError:
        return observed_cost
    duration_seconds = (end - start).total_seconds()
    # Floor the duration at 1 hour to avoid inflating estimates from
    # a handful of records that all happen to share a timestamp.
    duration_days = max(duration_seconds / 86400.0, 1.0 / 24.0)
    return observed_cost * (days_target / duration_days)


def main(argv: Optional[List[str]] = None) -> int:
    """CLI entry point. Returns a process exit code."""
    parser = argparse.ArgumentParser(
        prog="cost_aggregator",
        description=(
            "Aggregate reviewer-agent cost telemetry into a "
            "dashboard-ready JSON report."
        ),
    )
    parser.add_argument(
        "log_path",
        type=Path,
        help="Path to the NDJSON telemetry log.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Output JSON path (default: stdout).",
    )
    parser.add_argument(
        "--price-input",
        type=float,
        default=DEFAULT_PRICE_INPUT_PER_TOKEN_USD,
        help=(
            f"Input-token price USD "
            f"(default: {DEFAULT_PRICE_INPUT_PER_TOKEN_USD})."
        ),
    )
    parser.add_argument(
        "--price-output",
        type=float,
        default=DEFAULT_PRICE_OUTPUT_PER_TOKEN_USD,
        help=(
            f"Output-token price USD "
            f"(default: {DEFAULT_PRICE_OUTPUT_PER_TOKEN_USD})."
        ),
    )
    parser.add_argument(
        "--extrapolation-days",
        type=int,
        default=30,
        help="Days for the monthly extrapolation window (default: 30).",
    )
    args = parser.parse_args(argv)
    report = aggregate(
        args.log_path,
        price_input_per_token_usd=args.price_input,
        price_output_per_token_usd=args.price_output,
        extrapolation_days=args.extrapolation_days,
    )
    json_str = json.dumps(report, indent=2, sort_keys=False)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json_str + "\n", encoding="utf-8")
    else:
        print(json_str)
    return 0


if __name__ == "__main__":
    sys.exit(main())
