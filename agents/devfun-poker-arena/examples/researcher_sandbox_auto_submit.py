#!/usr/bin/env python3
"""Orchestrate Researcher sandbox submit: replace → wait-for-finish → submit (no replace).

Used by scripts/run_researcher_sandbox_auto_submit.sh and prod systemd timer.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any, Optional

import httpx

_EXAMPLES = Path(__file__).resolve().parent
_AGENT_ROOT = _EXAMPLES.parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from submit_sandbox_pvp import (  # noqa: E402
    SubmissionRejected,
    build_bundle,
    poll_submission,
    post_submission,
)

DEFAULT_PIN = _AGENT_ROOT / "config" / "researcher_sandbox_submit.pin.json"
TRANSIENT_HTTP = frozenset({502, 503, 504})
# Arena /agent/submissions often returns empty — never rely on it alone for active-bot detection.
STUCK_HANDS_UNCHANGED_SEC = int(os.environ.get("CEMINI_SANDBOX_STUCK_SEC", "7200"))  # 2h


def _api_base() -> str:
    return (
        os.environ.get("ARENA_API_BASE")
        or os.environ.get("ARENA_API_URL")
        or "https://arena.dev.fun/api/arena"
    ).rstrip("/")


def _headers() -> dict[str, str]:
    from submit_sandbox_pvp import _load_api_key  # noqa: WPS433

    return {"x-arena-api-key": _load_api_key()}


def _load_creds() -> dict[str, Any]:
    creds_path = Path(
        os.environ.get("ARENA_CREDENTIALS_FILE", _AGENT_ROOT / ".arena-credentials")
    )
    return json.loads(creds_path.read_text(encoding="utf-8"))


def _load_pin(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def fetch_agent_submissions(competition_id: str) -> list[dict[str, Any]]:
    creds = _load_creds()
    agent_id = creds.get("agentId") or ""
    if not agent_id:
        return []
    base = _api_base()
    rows: list[dict[str, Any]] = []
    offset = 0
    limit = 50
    while True:
        url = (
            f"{base}/agent/submissions?agentId={agent_id}"
            f"&competitionId={competition_id}&limit={limit}&offset={offset}"
        )
        r = httpx.get(url, headers=_headers(), timeout=60.0)
        if r.status_code != 200:
            break
        body = r.json()
        batch = body.get("data") if isinstance(body, dict) else body
        if not isinstance(batch, list):
            batch = []
        if not batch:
            break
        rows.extend(batch)
        total = int(body.get("total") or len(rows)) if isinstance(body, dict) else len(rows)
        offset += len(batch)
        if offset >= total:
            break
    return rows


def pvp_progress(rec: dict[str, Any]) -> tuple[int, int, str]:
    pvp = rec.get("pvp") or {}
    ch = int(pvp.get("completedHands") or rec.get("completedHands") or 0)
    th = int(pvp.get("targetHands") or rec.get("targetHands") or 0)
    status = str(pvp.get("status") or rec.get("status") or "")
    return ch, th, status


def pvp_is_finished(rec: dict[str, Any]) -> bool:
    ch, th, status = pvp_progress(rec)
    if th > 0 and ch >= th:
        return True
    st = status.lower()
    if st and st not in ("active", "running", "pending"):
        return True
    return False


def _poll_submission_safe(submission_id: str) -> Optional[dict[str, Any]]:
    try:
        return poll_submission(submission_id)
    except SystemExit:
        return None


def _submission_ids_from_pin(pin: dict[str, Any]) -> list[str]:
    ids: list[str] = []
    for key in ("activeSubmissionId", "watchSubmissionId"):
        val = pin.get(key)
        if val:
            ids.append(str(val))
    extra = pin.get("watchSubmissionIds")
    if isinstance(extra, list):
        ids.extend(str(x) for x in extra if x)
    return ids


def _submission_ids_from_state(state: Optional[dict[str, Any]]) -> list[str]:
    if not state:
        return []
    ids: list[str] = []
    for key in ("activeSubmissionId", "submissionId"):
        val = state.get(key)
        if val:
            ids.append(str(val))
    sub = state.get("submission")
    if isinstance(sub, dict) and sub.get("id"):
        ids.append(str(sub["id"]))
    extra = state.get("watchSubmissionIds")
    if isinstance(extra, list):
        ids.extend(str(x) for x in extra if x)
    return ids


def find_active_pvp_submission(
    competition_id: str,
    *,
    pin: Optional[dict[str, Any]] = None,
    state: Optional[dict[str, Any]] = None,
) -> Optional[dict[str, Any]]:
    """Return newest in-flight PvP submission (Active + hands < target).

    Polls pinned/state submission IDs first — /agent/submissions is unreliable (often empty).
    """
    seen: set[str] = set()
    candidates: list[dict[str, Any]] = []

    def consider(sid: str) -> None:
        if sid in seen:
            return
        seen.add(sid)
        full = _poll_submission_safe(sid)
        if not full:
            return
        if str(full.get("competitionId") or "") != competition_id:
            return
        ch, th, status = pvp_progress(full)
        st = status.lower()
        top = str(full.get("status") or "").lower()
        if th > 0 and ch >= th:
            return
        if top in ("succeeded", "finished", "failed", "error"):
            return
        if st == "active" or (th > 0 and ch < th and st not in ("finished", "failed", "error")):
            candidates.append(full)

    for sid in _submission_ids_from_pin(pin or {}):
        if sid in seen:
            continue
        # Only the pinned primary ID gates submit/wait; watchSubmissionIds are monitor-only.
        pin_primary = str((pin or {}).get("activeSubmissionId") or "")
        watch_only = pin.get("watchSubmissionIds") or []
        if pin_primary and sid != pin_primary and sid in watch_only:
            continue
        consider(sid)
    for sid in _submission_ids_from_state(state):
        consider(sid)

    for row in fetch_agent_submissions(competition_id):
        sid = row.get("id") or row.get("submissionId")
        if sid:
            consider(str(sid))

    if not candidates:
        return None

    pin_active = str((pin or {}).get("activeSubmissionId") or "")
    if pin_active:
        for c in candidates:
            if str(c.get("id") or "") == pin_active:
                return c

    def sort_key(d: dict[str, Any]) -> tuple[int, int]:
        ch, _, _ = pvp_progress(d)
        return (ch, int(d.get("submittedAt") or 0))

    candidates.sort(key=sort_key, reverse=True)
    return candidates[0]


def read_state(path: Path) -> Optional[dict[str, Any]]:
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def write_state(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def stuck_payload(
    *,
    competition_id: str,
    bundle: Path,
    active: dict[str, Any],
    bundle_sha: str,
    unchanged_sec: int,
) -> dict[str, Any]:
    ch, th, status = pvp_progress(active)
    return {
        "status": "stuck_zombie",
        "competitionId": competition_id,
        "bundle": str(bundle),
        "bundleSha256": bundle_sha,
        "activeSubmissionId": active.get("id"),
        "pvpStatus": status,
        "completedHands": ch,
        "targetHands": th,
        "unchangedSeconds": unchanged_sec,
        "note": "Hands unchanged since last timer run — arena scheduler zombie; do not replace",
    }


def detect_stuck(
    prev: Optional[dict[str, Any]],
    active: dict[str, Any],
    now: float,
) -> tuple[bool, int]:
    """True if same submission + same completedHands for >= STUCK_HANDS_UNCHANGED_SEC."""
    if not prev:
        return False, 0
    sid = active.get("id")
    if not sid or str(prev.get("activeSubmissionId") or "") != str(sid):
        return False, 0
    ch, _, _ = pvp_progress(active)
    prev_ch = int(prev.get("completedHands") or -1)
    if ch != prev_ch:
        return False, 0
    last_at = float(prev.get("lastHandsAt") or prev.get("checkedAt") or 0)
    if last_at <= 0:
        return False, 0
    elapsed = int(now - last_at)
    return elapsed >= STUCK_HANDS_UNCHANGED_SEC, elapsed


def waiting_payload(
    *,
    competition_id: str,
    bundle: Path,
    active: dict[str, Any],
    bundle_sha: str,
    now: float,
) -> dict[str, Any]:
    ch, th, status = pvp_progress(active)
    return {
        "status": "waiting_for_finish",
        "competitionId": competition_id,
        "bundle": str(bundle),
        "bundleSha256": bundle_sha,
        "activeSubmissionId": active.get("id"),
        "pvpStatus": status,
        "completedHands": ch,
        "targetHands": th,
        "checkedAt": now,
        "lastHandsAt": now,
    }


def try_submit(
    *,
    competition_id: str,
    bundle: Path,
    replace: bool,
) -> dict[str, Any]:
    rec = post_submission(
        competition_id=competition_id,
        bundle_path=bundle,
        replace=replace,
    )
    return {"status": "submitted", "mode": "replace" if replace else "fresh", "submission": rec, "bundle": str(bundle)}


def run_auto(
    *,
    pin_path: Path,
    state_path: Path,
    bundle_path: Optional[Path],
) -> int:
    if not pin_path.is_file():
        print(f"SKIP: missing pin {pin_path}")
        write_state(state_path, {"status": "skipped", "reason": "missing_pin"})
        return 0

    pin = _load_pin(pin_path)
    competition_id = str(pin.get("competitionId") or "")
    if not competition_id:
        raise SystemExit("pin missing competitionId")

    bundle_rel = str(pin.get("bundlePath") or "dist/sandbox-pvp-bundle.zip")
    bundle = bundle_path or (_AGENT_ROOT / bundle_rel)
    prefer_replace = bool(pin.get("replace", False))
    prev_state = read_state(state_path)
    now = time.time()

    print(f"==> Building {bundle}")
    build_bundle(bundle)
    bundle_sha = __import__("hashlib").sha256(bundle.read_bytes()).hexdigest()
    print(f"==> bundle sha256={bundle_sha}")

    active = find_active_pvp_submission(competition_id, pin=pin, state=prev_state)
    if active and not pvp_is_finished(active):
        ch, th, status = pvp_progress(active)
        is_stuck, unchanged_sec = detect_stuck(prev_state, active, now)
        if is_stuck:
            payload = stuck_payload(
                competition_id=competition_id,
                bundle=bundle,
                active=active,
                bundle_sha=bundle_sha,
                unchanged_sec=unchanged_sec,
            )
            print(json.dumps(payload, indent=2))
            write_state(state_path, payload)
            print(
                f"==> STUCK: hands frozen at {ch}/{th} for {unchanged_sec}s "
                "— arena zombie; NOT replacing (file dev.fun ticket)"
            )
            return 0

        payload = waiting_payload(
            competition_id=competition_id,
            bundle=bundle,
            active=active,
            bundle_sha=bundle_sha,
            now=now,
        )
        # Preserve lastHandsAt when hand count unchanged between timer runs.
        if prev_state and str(prev_state.get("activeSubmissionId") or "") == str(active.get("id")):
            prev_ch = int(prev_state.get("completedHands") or -1)
            if prev_ch == ch:
                payload["lastHandsAt"] = float(prev_state.get("lastHandsAt") or now)
        print(json.dumps(payload, indent=2))
        write_state(state_path, payload)
        print(f"==> WAIT: active PvP {ch}/{th} ({status}) — will submit fresh bundle when finished")
        return 0

    if (
        not prefer_replace
        and prev_state
        and prev_state.get("status") in ("waiting_for_finish", "stuck_zombie")
        and active
        and not pvp_is_finished(active)
    ):
        print("==> SKIP submit: prior state indicates in-flight or stuck bot — replace disabled in pin")
        write_state(state_path, {**prev_state, "checkedAt": now})
        return 0

    if active and pvp_is_finished(active):
        print("==> Prior PvP finished — submitting fresh bundle (no replace)")

    if prefer_replace:
        print(f"==> Submit with replace to {competition_id}")
        try:
            out = try_submit(competition_id=competition_id, bundle=bundle, replace=True)
            print(json.dumps(out.get("submission"), indent=2))
            write_state(state_path, out)
            return 0
        except SubmissionRejected as exc:
            if exc.code == "sandbox_daily_limit":
                skip = {
                    "status": "skipped",
                    "reason": "sandbox_daily_limit",
                    "competitionId": competition_id,
                    "bundle": str(bundle),
                }
                print(json.dumps(skip, indent=2))
                write_state(state_path, skip)
                return 0
            if exc.code == "sandbox_agent_already_running":
                active = find_active_pvp_submission(
                    competition_id, pin=pin, state=prev_state
                )
                if active and not pvp_is_finished(active):
                    payload = waiting_payload(
                        competition_id=competition_id,
                        bundle=bundle,
                        active=active,
                        bundle_sha=bundle_sha,
                        now=now,
                    )
                    print(json.dumps(payload, indent=2))
                    write_state(state_path, payload)
                    print("==> WAIT: replace rejected — waiting for active bot to finish")
                    return 0
            if exc.status_code in TRANSIENT_HTTP:
                skip = {
                    "status": "skipped",
                    "reason": "transient_http",
                    "httpStatus": exc.status_code,
                    "competitionId": competition_id,
                }
                print(json.dumps(skip, indent=2))
                write_state(state_path, skip)
                return 0
            write_state(
                state_path,
                {
                    "status": "error",
                    "reason": exc.code or "submission_rejected",
                    "httpStatus": exc.status_code,
                    "body": exc.body[:500],
                },
            )
            raise SystemExit(str(exc)) from exc

    print(f"==> Submit fresh bundle (no replace) to {competition_id}")
    try:
        out = try_submit(competition_id=competition_id, bundle=bundle, replace=False)
        print(json.dumps(out.get("submission"), indent=2))
        write_state(state_path, out)
        return 0
    except SubmissionRejected as exc:
        if exc.code == "sandbox_daily_limit":
            skip = {
                "status": "skipped",
                "reason": "sandbox_daily_limit",
                "competitionId": competition_id,
                "bundle": str(bundle),
            }
            print(json.dumps(skip, indent=2))
            write_state(state_path, skip)
            return 0
        if exc.status_code in TRANSIENT_HTTP:
            skip = {
                "status": "skipped",
                "reason": "transient_http",
                "httpStatus": exc.status_code,
            }
            write_state(state_path, skip)
            return 0
        write_state(
            state_path,
            {
                "status": "error",
                "reason": exc.code or "submission_rejected",
                "httpStatus": exc.status_code,
                "body": exc.body[:500],
            },
        )
        raise SystemExit(str(exc)) from exc


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Auto-orchestrate Researcher sandbox submit")
    p.add_argument("--pin", type=Path, default=DEFAULT_PIN)
    p.add_argument(
        "--state-file",
        type=Path,
        default=_AGENT_ROOT / "reports" / "researcher-round" / "auto-submit-state.json",
    )
    p.add_argument("--bundle", type=Path, default=None)
    args = p.parse_args(argv)
    return run_auto(pin_path=args.pin, state_path=args.state_file, bundle_path=args.bundle)


if __name__ == "__main__":
    raise SystemExit(main())
