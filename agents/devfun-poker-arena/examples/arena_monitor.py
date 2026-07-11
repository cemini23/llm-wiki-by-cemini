#!/usr/bin/env python3
"""Periodic Playground analyze + Poker Eval / Tournament availability monitor.

Runs on cemini-prod via systemd timer (every 30 min). Writes:
  reports/analyze/YYYY-MM-DDTHHMMSSZ.txt   — full failure report
  reports/analyze/history.jsonl            — hand + position metrics over time
  reports/eval_poll.jsonl                  — competition availability log
  reports/alerts.txt                       — newly active Eval / Tournament IDs

Usage:
  uv run examples/arena_monitor.py once          # analyze + poll (default)
  uv run examples/arena_monitor.py analyze       # Playground analyze only
  uv run examples/arena_monitor.py poll-eval       # competition poll only
  uv run examples/arena_monitor.py watch --interval 1800   # loop forever
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from dotenv import load_dotenv

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from analyze import (  # noqa: E402
    _collect_hand_rows,
    _fetch_recent_tables,
    _fetch_replays,
    _load_creds,
    analyze,
    analyze_metrics,
)
from arena_client import ArenaClient, ArenaError, DEFAULT_BASE  # noqa: E402

DEFAULT_REPORTS = Path("/opt/devfun-poker-arena/reports")
LOCAL_REPORTS = _EXAMPLES.parent / "reports"

# Poker Eval competition IDs to watch (500-hand + 5000-hand).
_DEFAULT_EVAL_IDS = (
    "cmpdk0pt00eawvcaf1es8plw2",
    "cmpkdus9200syw8do5644oymp",
)

_PIN_PATH = _EXAMPLES.parent / "config" / "researcher_sandbox_submit.pin.json"
_PVP_ALERT_STATUSES = frozenset(
    {"failed", "discarded", "error", "cancelled", "canceled"}
)
_PVP_ACTIVE_STATUSES = frozenset({"active", "running", "pending", "paused", "queued"})


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _reports_dir() -> Path:
    env = os.environ.get("ARENA_MONITOR_REPORTS_DIR")
    if env:
        return Path(env)
    if DEFAULT_REPORTS.parent.exists() and DEFAULT_REPORTS.parent.name == "devfun-poker-arena":
        return DEFAULT_REPORTS
    return LOCAL_REPORTS


def _append_jsonl(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, sort_keys=True) + "\n")


def _load_state(path: Path) -> dict:
    if not path.is_file():
        return {"active_ids": [], "eval_ids": []}
    try:
        return json.loads(path.read_text())
    except Exception:
        return {"active_ids": [], "eval_ids": []}


def _save_state(path: Path, state: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")


def _resolve_agent_id(client: ArenaClient, agent_id: Optional[str]) -> Optional[str]:
    if agent_id:
        return agent_id
    try:
        me = client.get("/agent/me")
        if isinstance(me, dict):
            return me.get("id") or me.get("agentId")
    except ArenaError as e:
        print(f"[monitor] /agent/me failed: {e}", file=sys.stderr)
    return None


def poll_pinned_ladder_pvp(*, reports: Path) -> Optional[dict[str, Any]]:
    """Alert when pinned ladder submission PvP is Failed/Discarded (not lobby analyze)."""
    if not _PIN_PATH.is_file():
        return None
    try:
        pin = json.loads(_PIN_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    sid = str(pin.get("activeSubmissionId") or "").strip()
    if not sid:
        return None
    try:
        from submit_sandbox_pvp import poll_submission  # noqa: WPS433
        from researcher_sandbox_auto_submit import pvp_progress  # noqa: WPS433

        rec = poll_submission(sid)
    except Exception as exc:
        print(f"[monitor] ladder pvp poll failed: {exc}", file=sys.stderr)
        return None

    ch, th, pvp_status = pvp_progress(rec)
    pvp = rec.get("pvp") if isinstance(rec.get("pvp"), dict) else {}
    st = str(pvp_status or "").lower()
    record = {
        "ts": _utc_now(),
        "submissionId": sid,
        "competitionId": pin.get("competitionId"),
        "submissionStatus": rec.get("status"),
        "pvpStatus": pvp_status,
        "completedHands": ch,
        "targetHands": th,
        "adjustedBbPer100": pvp.get("adjustedBbPer100"),
        "error": pvp.get("error") or rec.get("error"),
    }
    _append_jsonl(reports / "ladder_pvp_poll.jsonl", record)

    state_path = reports / "monitor_state.json"
    state = _load_state(state_path)
    prev = state.get("ladder_pvp") or {}
    prev_status = str(prev.get("pvpStatus") or "").lower()
    prev_sid = str(prev.get("submissionId") or "")

    alert_lines: list[str] = []
    if st in _PVP_ALERT_STATUSES:
        err = (pvp.get("error") or rec.get("error") or "")[:200]
        line = (
            f"[{_utc_now()}] LADDER PVP {pvp_status.upper()}: submission={sid[:8]}… "
            f"hands={ch} bb/100={pvp.get('adjustedBbPer100')} err={err}"
        )
        if st != prev_status or prev_sid != sid or not prev:
            alert_lines.append(line)
            print(f"[monitor] *** ALERT {line}")

    if alert_lines:
        alert_path = reports / "alerts.txt"
        alert_path.parent.mkdir(parents=True, exist_ok=True)
        with alert_path.open("a", encoding="utf-8") as f:
            f.write("\n".join(alert_lines) + "\n")

    state["ladder_pvp"] = {
        "submissionId": sid,
        "pvpStatus": pvp_status,
        "completedHands": ch,
        "last_poll_ts": _utc_now(),
        "last_alert_key": f"{sid}:{st}" if alert_lines else prev.get("last_alert_key"),
    }
    _save_state(state_path, state)

    if st in _PVP_ACTIVE_STATUSES:
        print(
            f"[monitor] ladder pvp: {pvp_status} hands={ch} "
            f"bb/100={pvp.get('adjustedBbPer100')}"
        )
    elif st not in _PVP_ALERT_STATUSES:
        print(f"[monitor] ladder pvp: {pvp_status or 'unknown'} hands={ch}")

    return record


def run_analyze_pass(
    client: ArenaClient,
    agent_id: str,
    *,
    competition_id: str,
    reports: Path,
    limit: int = 100,
    top: int = 10,
) -> dict:
    """Fetch Arena hands, write report + history line. Returns metrics dict."""
    tables = _fetch_recent_tables(client, agent_id, competition_id, limit)
    chip_deltas = _fetch_replays(
        client, agent_id, limit, competition_id=competition_id
    )
    rows = _collect_hand_rows(tables, chip_deltas, agent_id)
    metrics = analyze_metrics(rows)
    report = analyze(tables, chip_deltas, agent_id, top_n=top)
    stamp = _utc_now().replace(":", "")
    out_path = reports / "analyze" / f"{stamp}.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report, encoding="utf-8")

    metrics.update({
        "ts": _utc_now(),
        "competitionId": competition_id,
        "agentId": agent_id,
        "report_path": str(out_path),
    })

    _append_jsonl(reports / "analyze" / "history.jsonl", metrics)

    sb = metrics.get("positions", {}).get("SB", {})
    btn = metrics.get("positions", {}).get("BTN", {})
    print(
        f"[monitor] analyze: hands={metrics.get('hands')} "
        f"SB avg={sb.get('avg_delta', 'n/a')} "
        f"BTN avg={btn.get('avg_delta', 'n/a')} "
        f"→ {out_path}"
    )
    return metrics


def _fetch_active_competitions(client: ArenaClient) -> list[dict]:
    try:
        body = client.get("/competition/list-active")
    except ArenaError as e:
        print(f"[monitor] list-active failed: {e}", file=sys.stderr)
        return []
    if isinstance(body, list):
        return [c for c in body if isinstance(c, dict)]
    if isinstance(body, dict):
        data = body.get("data") or body.get("competitions")
        if isinstance(data, list):
            return [c for c in data if isinstance(c, dict)]
    return []


def _eval_watch_ids() -> list[str]:
    raw = os.environ.get("ARENA_EVAL_COMPETITION_IDS", "")
    if raw.strip():
        return [x.strip() for x in raw.split(",") if x.strip()]
    single = os.environ.get("ARENA_COMPETITION_ID")
    if single:
        return [single, _DEFAULT_EVAL_IDS[1]]
    return list(_DEFAULT_EVAL_IDS)


def poll_eval_and_tournaments(
    client: ArenaClient,
    *,
    reports: Path,
    auto_benchmark: bool = False,
    benchmark_hands: int = 50,
) -> list[dict]:
    """Poll list-active; alert on new Eval/Tournament competitions."""
    active = _fetch_active_competitions(client)
    active_ids = {c.get("id") for c in active if c.get("id")}
    eval_watch = set(_eval_watch_ids())

    state_path = reports / "monitor_state.json"
    state = _load_state(state_path)
    prev_active = set(state.get("active_ids") or [])
    prev_eval_active = set(state.get("eval_ids") or [])

    newly_active = [c for c in active if c.get("id") not in prev_active]
    eval_now_active = [
        c for c in active
        if c.get("id") in eval_watch
    ]
    eval_newly = [c for c in eval_now_active if c.get("id") not in prev_eval_active]

    record = {
        "ts": _utc_now(),
        "active_count": len(active),
        "active_ids": sorted(active_ids),
        "eval_watch": sorted(eval_watch),
        "eval_active": [c.get("id") for c in eval_now_active],
        "newly_active": [
            {"id": c.get("id"), "name": c.get("name")}
            for c in newly_active
        ],
        "eval_newly_active": [
            {"id": c.get("id"), "name": c.get("name")}
            for c in eval_newly
        ],
    }
    _append_jsonl(reports / "eval_poll.jsonl", record)

    alerts: list[str] = []
    for c in newly_active:
        name = c.get("name") or c.get("id")
        cid = c.get("id")
        line = f"[{_utc_now()}] NEW ACTIVE: {name} ({cid})"
        alerts.append(line)
        print(f"[monitor] ALERT {line}")

    for c in eval_newly:
        name = c.get("name") or c.get("id")
        cid = c.get("id")
        line = f"[{_utc_now()}] POKER EVAL LIVE: {name} ({cid}) — run: uv run examples/run_cemini.py --max-hands {benchmark_hands} --competition-id {cid}"
        alerts.append(line)
        print(f"[monitor] *** {line}")

    if alerts:
        alert_path = reports / "alerts.txt"
        alert_path.parent.mkdir(parents=True, exist_ok=True)
        with alert_path.open("a", encoding="utf-8") as f:
            f.write("\n".join(alerts) + "\n")

    state["active_ids"] = sorted(active_ids)
    state["eval_ids"] = [c.get("id") for c in eval_now_active if c.get("id")]
    state["last_poll_ts"] = _utc_now()
    _save_state(state_path, state)

    if auto_benchmark and eval_newly:
        cid = eval_newly[0].get("id")
        if cid:
            _trigger_benchmark(cid, benchmark_hands)

    if not active:
        print("[monitor] poll: no active competitions")
    else:
        for c in active:
            print(f"[monitor] poll active: {c.get('name')} ({c.get('id')})")
        if not eval_now_active:
            print("[monitor] poll: Poker Eval competitions not active yet")

    return eval_newly


def _trigger_benchmark(competition_id: str, max_hands: int) -> None:
    """Optional: kick off a short eval run when competition goes live."""
    agent_dir = _EXAMPLES.parent
    cmd = [
        str(agent_dir / ".venv/bin/python") if (agent_dir / ".venv/bin/python").is_file()
        else sys.executable,
        str(_EXAMPLES / "run_cemini.py"),
        "--max-hands", str(max_hands),
        "--competition-id", competition_id,
    ]
    print(f"[monitor] auto-benchmark: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, cwd=str(agent_dir), check=False, timeout=3600)
    except Exception as e:
        print(f"[monitor] auto-benchmark failed: {e}", file=sys.stderr)


def run_once(args: argparse.Namespace, client: ArenaClient, agent_id: str) -> int:
    reports = Path(args.reports_dir or _reports_dir())
    lobby_id = (
        args.match
        or os.environ.get("ARENA_LOBBY_COMPETITION_ID")
        or "cmpr1vesh2it1x69xmtpiaecp"
    )

    if args.command in ("once", "analyze", None):
        run_analyze_pass(
            client, agent_id,
            competition_id=lobby_id,
            reports=reports,
            limit=args.limit,
            top=args.top,
        )

    if args.command in ("once", "poll-eval", None):
        poll_eval_and_tournaments(
            client,
            reports=reports,
            auto_benchmark=args.auto_benchmark,
            benchmark_hands=args.benchmark_hands,
        )

    if args.command in ("once", "poll-eval", None):
        poll_pinned_ladder_pvp(reports=reports)

    if args.command in ("once", "analyze", None) and not getattr(args, "skip_auto_analyst", False):
        _maybe_run_hl_auto_analyst(reports)
    return 0


def _maybe_run_hl_auto_analyst(reports: Path) -> None:
    """DeepSeek auto-analyst: guards, style tweaks, kill switch (after analyze)."""
    if os.environ.get("CEMINI_HL_AUTO_ANALYST", "1").strip().lower() in ("0", "false", "no"):
        return
    hist = reports / "analyze" / "history.jsonl"
    if not hist.is_file():
        return
    last_line = ""
    for line in hist.read_text(encoding="utf-8").splitlines():
        if line.strip():
            last_line = line
    if not last_line:
        return
    try:
        metrics = json.loads(last_line)
    except Exception:
        return
    report_path = metrics.get("report_path")
    if not report_path or not Path(report_path).is_file():
        # fallback: newest analyze txt
        analyze_dir = reports / "analyze"
        txts = sorted(analyze_dir.glob("*.txt"), key=lambda p: p.stat().st_mtime, reverse=True)
        if not txts:
            return
        report_path = str(txts[0])
    try:
        from cemini_hl_auto_analyst import maybe_run_after_analyze
        maybe_run_after_analyze(
            report_path=Path(report_path),
            metrics=metrics,
            reports_dir=reports,
        )
    except Exception as exc:
        print(f"[monitor] hl-auto-analyst failed: {exc}", file=sys.stderr)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Arena analyze + eval poll monitor")
    parser.add_argument(
        "command",
        nargs="?",
        default="once",
        choices=("once", "analyze", "poll-eval", "watch"),
        help="once=analyze+poll (default), analyze, poll-eval, watch",
    )
    parser.add_argument("--match", default=None, help="Lobby competitionId for analyze")
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--reports-dir", default=None)
    parser.add_argument("--auto-benchmark", action="store_true",
                        help="Start run_cemini.py when Eval competition newly active")
    parser.add_argument("--benchmark-hands", type=int, default=50)
    parser.add_argument("--interval", type=int, default=1800,
                        help="watch mode: seconds between passes (default 1800)")
    parser.add_argument("--skip-auto-analyst", action="store_true",
                        help="Skip DeepSeek HL auto-analyst after analyze")

    args = parser.parse_args(argv)

    load_dotenv()
    api_key, agent_id = _load_creds()
    if not api_key:
        print("ERROR: no API key — set ARENA_API_KEY or .arena-credentials", file=sys.stderr)
        return 2

    client = ArenaClient(os.environ.get("ARENA_API_BASE", DEFAULT_BASE), api_key=api_key)
    try:
        agent_id = _resolve_agent_id(client, agent_id)
        if not agent_id:
            print("ERROR: could not resolve agentId", file=sys.stderr)
            return 2

        if args.command == "watch":
            print(f"[monitor] watch interval={args.interval}s reports={args.reports_dir or _reports_dir()}")
            while True:
                run_once(args, client, agent_id)
                time.sleep(max(args.interval, 60))
        return run_once(args, client, agent_id)
    finally:
        client.close()


if __name__ == "__main__":
    raise SystemExit(main())
