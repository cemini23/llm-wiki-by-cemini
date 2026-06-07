#!/usr/bin/env python3
"""Research harvest — four strategies for S1a gap archive completeness.

Not for live ops. Benchmark hosts, run fastest path, rsync to laptop.

Strategies:
  A  crawl_until_complete  — batched full-field submissions (Tier-2, primary)
  B  top500_snapshot       — one-shot top-500 submissions + stats
  C  stats_full_field       — all agent-stats in one pass (fast VPIP/PFR corpus)
  D  mode_full              — export_competition_hands --mode full (single run)

Usage:
  uv run python scripts/research_harvest.py benchmark --host prod --probe 5
  uv run python scripts/research_harvest.py run --strategy crawl --until-complete
  uv run python scripts/research_harvest.py run-all --out-dir reports/exports/playground-s1-live
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples"
if str(EXAMPLES) not in sys.path:
    sys.path.insert(0, str(EXAMPLES))

from dotenv import load_dotenv

from arena_client import ArenaClient, CREDS_PATH, DEFAULT_BASE  # noqa: E402
from export_competition_hands import export_competition  # noqa: E402
from export_field_crawl import crawl_batch, _load_creds  # noqa: E402


def _venv_python() -> str:
    venv = ROOT / "venv" / "bin" / "python"
    if venv.is_file():
        return str(venv)
    return sys.executable


def _competition_id(explicit: str | None) -> str:
    return (
        explicit
        or os.environ.get("ARENA_LOBBY_COMPETITION_ID")
        or "cmpy2qy65002ud9ej6b7jjq0l"
    )


def _client() -> ArenaClient:
    load_dotenv(ROOT / ".env")
    api_key = _load_creds()
    if not api_key:
        raise SystemExit("ERROR: need ARENA_API_KEY or .arena-credentials")
    return ArenaClient(os.environ.get("ARENA_API_BASE", DEFAULT_BASE), api_key=api_key)


def strategy_crawl_probe(client: ArenaClient, competition_id: str, out_dir: Path, n: int) -> float:
    t0 = time.perf_counter()
    crawl_batch(
        client,
        competition_id,
        out_dir,
        batch_size=n,
        sleep_s=0.04,
        fetch_submissions=True,
        fetch_stats=True,
        fetch_tables=False,
    )
    return time.perf_counter() - t0


def strategy_top500_probe(client: ArenaClient, competition_id: str, n: int) -> float:
    t0 = time.perf_counter()
    export_competition(
        client,
        competition_id,
        mode="recent",
        top_agents=n,
        fetch_stats=True,
        stats_top=n,
        sleep_s=0.04,
    )
    return time.perf_counter() - t0


def strategy_stats_probe(client: ArenaClient, competition_id: str, out_dir: Path, n: int) -> float:
    t0 = time.perf_counter()
    crawl_batch(
        client,
        competition_id,
        out_dir,
        batch_size=n,
        sleep_s=0.03,
        fetch_submissions=False,
        fetch_stats=True,
        fetch_tables=False,
    )
    return time.perf_counter() - t0


def cmd_benchmark(args: argparse.Namespace) -> int:
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    probe = args.probe
    competition_id = _competition_id(args.match)

    if args.host == "prod":
        remote = f"""
cd /opt/devfun-poker-arena
PROBE={probe}
OUT="{out_dir}"
./venv/bin/python scripts/research_harvest.py benchmark --host local --probe $PROBE --out-dir "$OUT" --match {competition_id}
"""
        t0 = time.perf_counter()
        r = subprocess.run(["ssh", "-q", "cemini-prod", remote], capture_output=True, text=True)
        elapsed = time.perf_counter() - t0
        print(r.stdout)
        if r.stderr:
            print(r.stderr, file=sys.stderr)
        print(json.dumps({"host": "prod", "wall_s": round(elapsed, 2), "exit": r.returncode}, indent=2))
        return r.returncode

    client = _client()
    try:
        results = {}
        for name, fn in (
            ("A_crawl_submissions", lambda: strategy_crawl_probe(client, competition_id, out_dir, probe)),
            ("B_topN_submissions", lambda: strategy_top500_probe(client, competition_id, probe)),
            ("C_stats_only", lambda: strategy_stats_probe(client, competition_id, out_dir, probe)),
        ):
            try:
                sec = fn()
                results[name] = {"probe_agents": probe, "seconds": round(sec, 2), "sec_per_agent": round(sec / max(probe, 1), 2)}
            except Exception as e:
                results[name] = {"error": str(e)}
        per_agent = {
            k: v["sec_per_agent"]
            for k, v in results.items()
            if "sec_per_agent" in v
        }
        winner = min(per_agent, key=per_agent.get) if per_agent else None
        print(json.dumps({"host": args.host, "competition_id": competition_id, "results": results, "fastest_probe": winner}, indent=2))
        return 0
    finally:
        client.close()


def cmd_run(args: argparse.Namespace) -> int:
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    competition_id = _competition_id(args.match)
    py = _venv_python()

    if args.strategy in ("crawl", "A"):
        cmd = [
            py,
            str(EXAMPLES / "export_field_crawl.py"),
            "--out-dir",
            str(out_dir),
            "--batch-size",
            str(args.batch_size),
            "--sleep",
            str(args.sleep),
            "--no-tables",
        ]
        if args.until_complete:
            cmd.append("--until-complete")
        if args.match:
            cmd.extend(["--match", competition_id])
        return subprocess.call(cmd)

    if args.strategy in ("top500", "B"):
        cmd = [
            py,
            str(EXAMPLES / "export_competition_hands.py"),
            "--append",
            "--top-agents",
            "500",
            "--stats-top",
            "500",
            "--out-dir",
            str(out_dir),
        ]
        if args.match:
            cmd.extend(["--match", competition_id])
        return subprocess.call(cmd)

    if args.strategy in ("stats", "C"):
        client = _client()
        try:
            from export_competition_hands import fetch_leaderboard
            from export_field_crawl import _stable_leaderboard

            total = len(_stable_leaderboard(fetch_leaderboard(client, competition_id)))
            manifest = crawl_batch(
                client,
                competition_id,
                out_dir,
                batch_size=total or 5000,
                sleep_s=0.03,
                fetch_submissions=False,
                fetch_stats=True,
                fetch_tables=False,
            )
            print(json.dumps(manifest, indent=2))
            return 0
        finally:
            client.close()

    if args.strategy in ("full", "D"):
        cmd = [
            py,
            str(EXAMPLES / "export_competition_hands.py"),
            "--mode",
            "full",
            "--out-dir",
            str(out_dir),
        ]
        if args.match:
            cmd.extend(["--match", competition_id])
        return subprocess.call(cmd)

    print(f"Unknown strategy {args.strategy}", file=sys.stderr)
    return 2


def cmd_run_all(args: argparse.Namespace) -> int:
    """Run complementary harvest paths for gap archive (research, not live ops)."""
    out_dir = Path(args.out_dir)
    steps = [
        ("C stats_full_field", ["run", "--strategy", "stats", "--out-dir", str(out_dir)]),
        ("B top500_snapshot", ["run", "--strategy", "top500", "--out-dir", str(out_dir)]),
        ("A crawl_until_complete", [
            "run", "--strategy", "crawl", "--out-dir", str(out_dir),
            "--batch-size", str(args.batch_size), "--sleep", str(args.sleep),
            "--until-complete",
        ]),
    ]
    if args.include_full:
        steps.append(("D mode_full", ["run", "--strategy", "full", "--out-dir", str(out_dir)]))

    rc = 0
    for label, sub in steps:
        print(f"\n=== {label} ===", file=sys.stderr)
        ns = argparse.Namespace(
            strategy=sub[2],
            out_dir=str(out_dir),
            match=args.match,
            batch_size=args.batch_size,
            sleep=args.sleep,
            until_complete="until-complete" in sub,
        )
        step_rc = cmd_run(ns)
        if step_rc != 0:
            print(f"WARN: {label} exit {step_rc}", file=sys.stderr)
            rc = step_rc
    return rc


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Research harvest for S1a gap audit")
    sub = p.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("benchmark", help="Probe 3 strategies on N agents")
    b.add_argument("--host", choices=("local", "prod"), default="local")
    b.add_argument("--probe", type=int, default=5)
    b.add_argument("--out-dir", default=str(ROOT / "reports/exports/playground-s1-live"))
    b.add_argument("--match", default=None)
    b.set_defaults(func=cmd_benchmark)

    r = sub.add_parser("run", help="Run one strategy")
    r.add_argument("--strategy", required=True, help="crawl|top500|stats|full or A|B|C|D")
    r.add_argument("--out-dir", default=str(ROOT / "reports/exports/playground-s1-live"))
    r.add_argument("--match", default=None)
    r.add_argument("--batch-size", type=int, default=500)
    r.add_argument("--sleep", type=float, default=0.03)
    r.add_argument("--until-complete", action="store_true")
    r.set_defaults(func=cmd_run)

    a = sub.add_parser("run-all", help="Stats + top500 + crawl until complete")
    a.add_argument("--out-dir", default=str(ROOT / "reports/exports/playground-s1-live"))
    a.add_argument("--match", default=None)
    a.add_argument("--batch-size", type=int, default=500)
    a.add_argument("--sleep", type=float, default=0.03)
    a.add_argument("--include-full", action="store_true", help="Also run mode full (slow)")
    a.set_defaults(func=cmd_run_all)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
