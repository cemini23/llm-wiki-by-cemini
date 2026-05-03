#!/usr/bin/env python3
"""Cemini Conductor — lightweight multi-model orchestrator CLI.

Usage:
    python3 -m conductor.cli --config conductor/config.yaml --query "What is NVDA?"
    echo '{"query": "..."}' | python3 -m conductor.cli --config conductor/config.yaml --stdin
    python3 -m conductor.cli --config conductor/config.yaml --evaluate --routing-log logs/routing.jsonl
    python3 -m conductor.cli --config conductor/config.yaml --build-priors
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import sys
from datetime import datetime, timezone
from typing import Any

from conductor.orchestrator import Conductor


class _Encoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        if isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)


def _output(data: Any, path: str | None, *, compact: bool = False) -> None:
    text = json.dumps(data, cls=_Encoder, indent=None if compact else 2)
    if path:
        with open(path, "w") as f:
            f.write(text)
            f.write("\n")
    else:
        print(text)


def _append_output(data: Any, path: str | None, *, first: bool = False) -> None:
    """Append one compact JSON line to output (for streaming --stdin mode)."""
    text = json.dumps(data, cls=_Encoder, indent=None)
    if path:
        mode = "w" if first else "a"
        with open(path, mode) as f:
            f.write(text)
            f.write("\n")
    else:
        print(text)


def cmd_route(conductor: Conductor, args: argparse.Namespace) -> None:
    """Handle --query or --stdin routing."""
    if args.stdin:
        first = True
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                text = obj.get("query", obj.get("text", line))
                sid = obj.get("session_id", "stdin")
                src = obj.get("source", "stdin")
            except json.JSONDecodeError:
                text = line
                sid = "stdin"
                src = "stdin"
            resp = conductor.route(text, session_id=sid, source=src)
            _append_output(resp, args.output, first=first)
            first = False
    elif args.query:
        resp = conductor.route(args.query)
        _output(resp, args.output)
    else:
        print("Error: provide --query or --stdin", file=sys.stderr)
        sys.exit(1)


def cmd_evaluate(conductor: Conductor, args: argparse.Namespace) -> None:
    """Run evaluation on a routing log file."""
    from conductor.evaluator import RoutingEvaluator

    if not args.routing_log:
        print("Error: --evaluate requires --routing-log <path>", file=sys.stderr)
        sys.exit(1)

    evaluator = RoutingEvaluator(conductor.config, conductor.api)
    decisions: list[dict[str, Any]] = []
    with open(args.routing_log) as f:
        for line in f:
            line = line.strip()
            if line:
                decisions.append(json.loads(line))

    results = []
    for d in decisions:
        score = evaluator.evaluate_decision(d)
        results.append(score)

    report = evaluator.build_report(results, decisions)
    _output(report, args.output)
    print(f"Evaluated {len(results)} decisions.", file=sys.stderr)
    if report:
        print(
            f"Avg correctness: {report.get('scores', {}).get('correctness', {}).get('mean', '—')}",
            file=sys.stderr,
        )


def cmd_build_priors(conductor: Conductor, args: argparse.Namespace) -> None:
    """Rebuild token priors from calibration data."""
    from conductor.calibration import CalibrationLogger

    cal = CalibrationLogger(conductor.config, conductor.stash_client)
    priors = cal.build_token_priors()

    # Update in-memory config
    tp = conductor.config.setdefault("token_priors", {})
    tp["taxonomy"] = priors.get("taxonomy", "")
    tp["cascade_judge"] = priors.get("cascade_judge", "")
    tp["tool_routing"] = priors.get("tool_routing", "")

    # Write back to config file
    import yaml

    config_path = args.config
    with open(config_path, "w") as f:
        yaml.safe_dump(conductor.config, f, default_flow_style=False, sort_keys=False)

    _output(priors, args.output)
    print("Token priors rebuilt and written to config.", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Cemini Conductor — lightweight multi-model orchestrator"
    )
    parser.add_argument(
        "--config", default="conductor/config.yaml", help="Path to config YAML"
    )
    parser.add_argument("--query", help="Single query to route")
    parser.add_argument(
        "--stdin", action="store_true", help="Read JSON queries from stdin (one per line)"
    )
    parser.add_argument("--output", "-o", help="Output path (default: stdout)")
    parser.add_argument(
        "--evaluate", action="store_true", help="Run evaluation on routing log"
    )
    parser.add_argument("--routing-log", help="Path to routing decisions JSONL for evaluation")
    parser.add_argument(
        "--build-priors", action="store_true",
        help="Rebuild token priors from Stash calibration data",
    )
    args = parser.parse_args()

    conductor = Conductor(args.config)

    if args.evaluate:
        cmd_evaluate(conductor, args)
    elif args.build_priors:
        cmd_build_priors(conductor, args)
    else:
        cmd_route(conductor, args)


if __name__ == "__main__":
    main()
