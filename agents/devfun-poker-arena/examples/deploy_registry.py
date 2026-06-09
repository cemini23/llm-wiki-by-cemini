"""Deploy audit trail + tournament candidate selection (JSONL under reports/hl-loop/).

Schemas:
  devfun.deploy_record.v1      → deploys.jsonl
  devfun.eval_timeseries.v1    → eval_timeseries.jsonl
  devfun.tournament_candidate.v1 → tournament_candidates.jsonl
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

_EXAMPLES = Path(__file__).resolve().parent
_AGENT_ROOT = _EXAMPLES.parent
_HL_DIR = _AGENT_ROOT / "reports" / "hl-loop"

DEPLOY_SCHEMA = "devfun.deploy_record.v1"
EVAL_SCHEMA = "devfun.eval_timeseries.v1"
CANDIDATE_SCHEMA = "devfun.tournament_candidate.v1"

_ENV_PREFIXES = ("CEMINI_", "ARENA_LOBBY", "JACKPOT_", "NUTS_")
_DEPLOY_META_KEYS = ("AGENT_VERSION",)


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def hl_dir() -> Path:
    raw = os.environ.get("CEMINI_HL_REPORTS_DIR", "").strip()
    return Path(raw) if raw else _HL_DIR


def deploys_path() -> Path:
    return hl_dir() / "deploys.jsonl"


def eval_timeseries_path() -> Path:
    return hl_dir() / "eval_timeseries.jsonl"


def candidates_path() -> Path:
    return hl_dir() / "tournament_candidates.jsonl"


def preflight_metrics_path() -> Path:
    return hl_dir() / "preflight_metrics.json"


def git_commit_short(agent_dir: Optional[Path] = None) -> str:
    root = agent_dir or _AGENT_ROOT
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=root,
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except Exception:
        return "unknown"


def _parse_env_file(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    if not path.is_file():
        return out
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        if any(key.startswith(p) for p in _ENV_PREFIXES) or key in _DEPLOY_META_KEYS:
            out[key] = val.strip().strip('"').strip("'")
    return out


def collect_env_snapshot(
    *,
    env_file: Optional[Path] = None,
    extra: Optional[dict[str, str]] = None,
) -> dict[str, str]:
    """Merge os.environ CEMINI_* / ARENA_* flags with optional .env file."""
    snap: dict[str, str] = {}
    for key, val in sorted(os.environ.items()):
        if any(key.startswith(p) for p in _ENV_PREFIXES) or key in _DEPLOY_META_KEYS:
            snap[key] = val
    if env_file:
        snap.update(_parse_env_file(env_file))
    if extra:
        snap.update(extra)
    return snap


def env_digest(snapshot: dict[str, str]) -> str:
    payload = json.dumps(snapshot, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()[:16]


def _append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, separators=(",", ":")) + "\n")


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(row, dict):
            rows.append(row)
    return rows


def read_state(agent_dir: Optional[Path] = None) -> dict[str, Any]:
    path = (agent_dir or _AGENT_ROOT) / "reports" / "hl-loop" / "state.json"
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def load_preflight_metrics() -> dict[str, Any]:
    path = preflight_metrics_path()
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def write_preflight_metrics(metrics: dict[str, Any]) -> Path:
    path = preflight_metrics_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"ts": _utc_now(), **metrics}
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def append_deploy_record(
    *,
    source: str,
    commit: str = "",
    hl_round: int | None = None,
    hands: int | None = None,
    competition_id: str = "",
    preflight: str = "none",
    env_file: Optional[Path] = None,
    env_extra: Optional[dict[str, str]] = None,
    notes: str = "",
) -> dict[str, Any]:
    """Append one deploy row; returns the row written."""
    sha = commit or git_commit_short()
    state = read_state()
    snap = collect_env_snapshot(env_file=env_file, extra=env_extra)
    pf = load_preflight_metrics()

    row: dict[str, Any] = {
        "schema": DEPLOY_SCHEMA,
        "ts": _utc_now(),
        "commit": sha,
        "hl_round": hl_round if hl_round is not None else state.get("round"),
        "hands": hands if hands is not None else state.get("hands"),
        "competition_id": competition_id or state.get("competition_id", ""),
        "source": source,
        "preflight": preflight,
        "env_digest": env_digest(snap),
        "env_flags": snap,
        "eval_panel_bb100_local": pf.get("eval_panel_bb100"),
        "selfplay_bb100_rock": pf.get("selfplay_bb100_rock"),
        "preflight_ts": pf.get("ts"),
    }
    if notes:
        row["notes"] = notes
    agent_version = snap.get("AGENT_VERSION") or os.environ.get("AGENT_VERSION", "").strip()
    if agent_version:
        row["agent_version"] = agent_version

    _append_jsonl(deploys_path(), row)
    return row


def append_eval_record(
    *,
    hands: int,
    adjusted_bb100: float,
    tag: str,
    competition_id: str,
    commit: str = "",
    raw_bb100: float | None = None,
    source: str = "eval_smoke",
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "schema": EVAL_SCHEMA,
        "ts": _utc_now(),
        "tag": tag,
        "competition_id": competition_id,
        "hands": int(hands),
        "adjustedBbPer100": float(adjusted_bb100),
        "commit": commit or git_commit_short(),
        "source": source,
    }
    if raw_bb100 is not None:
        row["rawBbPer100"] = float(raw_bb100)
    _append_jsonl(eval_timeseries_path(), row)
    return row


def read_deploys() -> list[dict[str, Any]]:
    return _read_jsonl(deploys_path())


def read_eval_timeseries() -> list[dict[str, Any]]:
    return _read_jsonl(eval_timeseries_path())


def read_playground_timeseries(path: Optional[Path] = None) -> list[dict[str, Any]]:
    p = path or (hl_dir() / "playground_timeseries.jsonl")
    return _read_jsonl(p)


def _last_row_for_commit(
    rows: list[dict[str, Any]],
    commit: str,
    *,
    key: str = "commit",
) -> dict[str, Any] | None:
    for row in reversed(rows):
        if row.get(key) == commit:
            return row
    return None


def _playground_delta_since(
    commit: str,
    deploy_ts: str,
    playground_rows: list[dict[str, Any]],
) -> dict[str, Any] | None:
    """Approximate chip trend after deploy using replay delta avg on rows with matching commit."""
    matched = [
        r
        for r in playground_rows
        if r.get("commit") == commit and (r.get("ts") or "") >= deploy_ts
    ]
    if not matched:
        return None
    avgs = [r["replay_chip_delta_avg"] for r in matched if r.get("replay_chip_delta_avg") is not None]
    if not avgs:
        return None
    return {
        "samples": len(matched),
        "replay_delta_avg_mean": round(sum(avgs) / len(avgs), 2),
        "last_rank": matched[-1].get("rank"),
        "last_chips": matched[-1].get("chips"),
        "last_buffer": matched[-1].get("buffer_chips"),
    }


def score_deploy_candidate(
    deploy: dict[str, Any],
    *,
    eval_rows: list[dict[str, Any]],
    playground_rows: list[dict[str, Any]],
    min_eval_bb100: float,
) -> dict[str, Any]:
    commit = deploy.get("commit", "")
    eval_local = deploy.get("eval_panel_bb100_local")
    eval_live = _last_row_for_commit(eval_rows, commit)
    eval_bb = eval_local
    eval_source = "preflight_local"
    if eval_live and eval_live.get("adjustedBbPer100") is not None:
        eval_bb = eval_live["adjustedBbPer100"]
        eval_source = f"eval_timeseries:{eval_live.get('tag', '?')}"

    pg = _playground_delta_since(commit, deploy.get("ts", ""), playground_rows)
    eval_pass = eval_bb is not None and float(eval_bb) >= min_eval_bb100

    score = 0.0
    reasons: list[str] = []
    if eval_bb is not None:
        score += float(eval_bb)
        reasons.append(f"eval_bb100={eval_bb:+.2f}")
    else:
        reasons.append("eval_bb100=missing")

    if pg:
        score += pg.get("replay_delta_avg_mean", 0) * 0.5
        buf = pg.get("last_buffer")
        if buf is not None:
            score += min(float(buf) / 1000.0, 50.0)
            reasons.append(f"buffer={buf}")
        reasons.append(f"pg_samples={pg.get('samples')}")

    return {
        "commit": commit,
        "deploy_ts": deploy.get("ts"),
        "hl_round": deploy.get("hl_round"),
        "source": deploy.get("source"),
        "preflight": deploy.get("preflight"),
        "eval_bb100": eval_bb,
        "eval_source": eval_source,
        "eval_pass": eval_pass,
        "env_digest": deploy.get("env_digest"),
        "playground": pg,
        "score": round(score, 2),
        "reasons": reasons,
    }


def pick_deploy_for_tournament(
    *,
    min_eval_bb100: float = -17.45,
    require_eval_pass: bool = True,
    limit: int = 5,
) -> list[dict[str, Any]]:
    deploys = read_deploys()
    eval_rows = read_eval_timeseries()
    playground_rows = read_playground_timeseries()

    scored: list[dict[str, Any]] = []
    seen: set[str] = set()
    for deploy in reversed(deploys):
        commit = deploy.get("commit", "")
        if not commit or commit in seen:
            continue
        seen.add(commit)
        row = score_deploy_candidate(
            deploy,
            eval_rows=eval_rows,
            playground_rows=playground_rows,
            min_eval_bb100=min_eval_bb100,
        )
        if require_eval_pass and not row["eval_pass"]:
            row["disqualified"] = "eval_below_floor"
        else:
            row["disqualified"] = None
        scored.append(row)

    eligible = [r for r in scored if not r.get("disqualified")]
    eligible.sort(key=lambda r: r["score"], reverse=True)
    return eligible[:limit]


def append_tournament_candidate(
    *,
    label: str,
    commit: str,
    competition_id: str,
    rationale: str = "",
    lock: bool = False,
) -> dict[str, Any]:
    """Record an operator-selected (or auto-picked) tournament deploy candidate."""
    deploys = read_deploys()
    deploy = _last_row_for_commit(deploys, commit) or {}
    eval_rows = read_eval_timeseries()
    pg_rows = read_playground_timeseries()
    scored = score_deploy_candidate(
        deploy if deploy else {"commit": commit, "ts": _utc_now()},
        eval_rows=eval_rows,
        playground_rows=pg_rows,
        min_eval_bb100=float(os.environ.get("CEMINI_EVAL_PANEL_BB100_FLOOR", "-17.45")),
    )

    row: dict[str, Any] = {
        "schema": CANDIDATE_SCHEMA,
        "ts": _utc_now(),
        "label": label,
        "commit": commit,
        "competition_id": competition_id,
        "lock": lock,
        "rationale": rationale,
        "deploy": deploy,
        "scorecard": scored,
        "preflight_metrics": load_preflight_metrics(),
    }
    _append_jsonl(candidates_path(), row)

    manifest_path = hl_dir() / "tournament_candidate.json"
    manifest_path.write_text(json.dumps(row, indent=2) + "\n", encoding="utf-8")
    return row


def format_pick_report(candidates: list[dict[str, Any]], *, min_eval_bb100: float) -> str:
    lines = [
        f"Tournament deploy candidates (eval floor {min_eval_bb100:+.2f} bb/100)",
        "",
    ]
    if not candidates:
        lines.append("No eligible candidates — run full preflight + eval smoke, then deploy.")
        return "\n".join(lines)

    for i, c in enumerate(candidates, 1):
        pg = c.get("playground") or {}
        lines.append(
            f"{i}. commit={c['commit']}  score={c['score']}  "
            f"eval={c.get('eval_bb100')} ({c.get('eval_source')})  "
            f"HL R{c.get('hl_round')}  buffer={pg.get('last_buffer', 'n/a')}"
        )
        lines.append(f"   deploy_ts={c.get('deploy_ts')}  reasons: {', '.join(c.get('reasons', []))}")
    return "\n".join(lines)
