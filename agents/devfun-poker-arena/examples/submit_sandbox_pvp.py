#!/usr/bin/env python3
"""POST static-agent bundle to Arena sandbox PvP (see /skills/sandbox-pvp.md).

Usage:
    uv run python examples/submit_sandbox_pvp.py --competition-id <id>
    uv run python examples/submit_sandbox_pvp.py --build --competition-id <id>
    uv run python examples/submit_sandbox_pvp.py --poll <submissionId>
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Any, Optional

import httpx

_EXAMPLES = Path(__file__).resolve().parent
_AGENT_ROOT = _EXAMPLES.parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from arena_client import DEFAULT_BASE  # noqa: E402

DEFAULT_COMP = "cmqqqs05i1u7ppnu7stqbw7d8"  # heads-up sandbox beta S1


def _api_base() -> str:
    return (
        os.environ.get("ARENA_API_BASE")
        or os.environ.get("ARENA_API_URL")
        or "https://arena.dev.fun/api/arena"
    ).rstrip("/")


def _load_api_key() -> str:
    creds_path = Path(
        os.environ.get("ARENA_CREDENTIALS_FILE", _AGENT_ROOT / ".arena-credentials")
    )
    data = json.loads(creds_path.read_text(encoding="utf-8"))
    key = data.get("apiKey") or ""
    if not key:
        raise SystemExit(f"ERROR: no apiKey in {creds_path}")
    return key


def _vendor_packages() -> list[str]:
    return ["treys", "httpx", "httpcore", "h11", "certifi", "idna", "anyio", "sniffio", "dotenv"]


def build_bundle(out_zip: Path) -> Path:
    """Zip harness/, assets/, skills/ per docs.dev.fun researcher guide."""
    harness = _AGENT_ROOT / "harness" / "strategy.py"
    if not harness.is_file():
        raise SystemExit(f"ERROR: missing {harness}")

    venv_site = _AGENT_ROOT / ".venv" / "lib"
    site_packages: Optional[Path] = None
    if venv_site.is_dir():
        for p in venv_site.glob("python*/site-packages"):
            site_packages = p
            break

    research = _AGENT_ROOT / "research"
    with tempfile.TemporaryDirectory(prefix="sandbox-bundle-") as tmp:
        root = Path(tmp)
        (root / "harness").mkdir()
        shutil.copy2(harness, root / "harness" / "strategy.py")
        assets = root / "assets"
        assets.mkdir()
        for py in _EXAMPLES.glob("*.py"):
            shutil.copy2(py, assets / py.name)
        traj_cfg = _EXAMPLES / "trajectory_bound_config.json"
        if traj_cfg.is_file():
            shutil.copy2(traj_cfg, assets / traj_cfg.name)
        priv = _EXAMPLES / "private"
        if priv.is_dir():
            shutil.copytree(priv, assets / "private", dirs_exist_ok=True)
        if research.is_dir():
            shutil.copytree(research, assets / "research", dirs_exist_ok=True)
        skills_src = _AGENT_ROOT / "skills" / "sandbox"
        # static-agent template rejects skills/ in zip (Arena 400). LLM/Daytona bundles may include it.
        include_skills = os.environ.get("CEMINI_BUNDLE_INCLUDE_SKILLS", "").strip().lower() in (
            "1",
            "true",
            "yes",
            "on",
        )
        if include_skills and skills_src.is_dir():
            shutil.copytree(skills_src, root / "skills", dirs_exist_ok=True)
        if site_packages is not None:
            vendor = assets / "_vendor"
            vendor.mkdir()
            for pkg in _vendor_packages():
                src = site_packages / pkg
                if src.is_dir():
                    shutil.copytree(src, vendor / pkg, dirs_exist_ok=True)
                elif src.with_suffix(".py").is_file():
                    shutil.copy2(src.with_suffix(".py"), vendor / f"{pkg}.py")

        out_zip.parent.mkdir(parents=True, exist_ok=True)
        if out_zip.exists():
            out_zip.unlink()
        with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED) as zf:
            for path in root.rglob("*"):
                if path.is_file():
                    zf.write(path, path.relative_to(root).as_posix())
    return out_zip


def build_fold_strategy_file(path: Path) -> Path:
    """Minimal valid static-agent strategy for replace/discard cycles."""
    path.write_text(
        '''"""Arena discard placeholder — always fold/check."""
def choose_action(table):
    aa = (table.get("allowedActions") or {}).get("availableActions") or []
    action = "fold" if "fold" in aa else ("check" if "check" in aa else (aa[0] if aa else "fold"))
    return {
        "action": action,
        "message": "discard-placeholder fold/check",
        "reasoning": "discard cycle: minimal legal action to clear active PvP slot",
        "reasoning_text": "discard cycle: minimal legal action to clear active PvP slot",
    }
''',
        encoding="utf-8",
    )
    return path


class SubmissionRejected(Exception):
    """Arena rejected POST /submissions (caller may handle daily limit)."""

    def __init__(self, status_code: int, body: str, code: Optional[str] = None) -> None:
        self.status_code = status_code
        self.body = body
        self.code = code
        super().__init__(f"POST submissions failed {status_code}: {body[:500]}")


def _parse_error_code(body: str) -> Optional[str]:
    try:
        data = json.loads(body)
        return str(data.get("code") or "") or None
    except json.JSONDecodeError:
        return None


def post_submission(
    *,
    competition_id: str,
    bundle_path: Path,
    replace: bool,
) -> dict[str, Any]:
    url = f"{_api_base()}/submissions"
    headers = {"x-arena-api-key": _load_api_key()}
    data: dict[str, str] = {
        "competitionId": competition_id,
        "template": "static-agent",
    }
    if replace:
        data["replace"] = "true"
    with bundle_path.open("rb") as fh:
        files = {"file": (bundle_path.name, fh, "application/zip")}
        r = httpx.post(url, headers=headers, data=data, files=files, timeout=120.0)
    if r.status_code not in (200, 201, 202):
        raise SubmissionRejected(r.status_code, r.text, _parse_error_code(r.text))
    return r.json()


def post_strategy_py(
    *,
    competition_id: str,
    strategy_path: Path,
    replace: bool,
) -> dict[str, Any]:
    url = f"{_api_base()}/submissions"
    headers = {"x-arena-api-key": _load_api_key()}
    data: dict[str, str] = {
        "competitionId": competition_id,
        "template": "static-agent",
    }
    if replace:
        data["replace"] = "true"
    with strategy_path.open("rb") as fh:
        files = {"file": ("strategy.py", fh, "text/x-python")}
        r = httpx.post(url, headers=headers, data=data, files=files, timeout=120.0)
    if r.status_code not in (200, 201, 202):
        raise SystemExit(f"POST submissions failed {r.status_code}: {r.text[:500]}")
    return r.json()


def poll_submission(submission_id: str) -> dict[str, Any]:
    url = f"{_api_base()}/submissions/{submission_id}"
    headers = {"x-arena-api-key": _load_api_key()}
    r = httpx.get(url, headers=headers, timeout=60.0)
    if r.status_code != 200:
        raise SystemExit(f"GET submission failed {r.status_code}: {r.text[:500]}")
    return r.json()


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Submit Cemini bot to sandbox PvP")
    p.add_argument("--competition-id", default=os.environ.get("ARENA_RESEARCHER_COMP_ID", DEFAULT_COMP))
    p.add_argument("--build", action="store_true", help="Build bundle.zip before submit")
    p.add_argument(
        "--build-only",
        action="store_true",
        help="Build bundle.zip and exit (no POST /submissions)",
    )
    p.add_argument("--bundle", type=Path, default=_AGENT_ROOT / "dist" / "sandbox-pvp-bundle.zip")
    p.add_argument("--replace", action="store_true", help="Replace unfinished active PvP bot")
    p.add_argument(
        "--discard-active",
        action="store_true",
        help="Replace current active bot with minimal fold strategy (clears running slot)",
    )
    p.add_argument("--poll", metavar="SUBMISSION_ID", help="Poll existing submission")
    p.add_argument(
        "--tolerate-daily-limit",
        action="store_true",
        help="Exit 0 when Arena returns sandbox_daily_limit (for prod auto-submit timer)",
    )
    p.add_argument(
        "--state-file",
        type=Path,
        help="Write JSON result (success, skipped, or error) to this path",
    )
    args = p.parse_args(argv)

    def _write_state(payload: dict[str, Any]) -> None:
        if args.state_file:
            args.state_file.parent.mkdir(parents=True, exist_ok=True)
            args.state_file.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    if args.poll:
        rec = poll_submission(args.poll)
        print(json.dumps(rec, indent=2))
        return 0

    if args.discard_active:
        with tempfile.TemporaryDirectory(prefix="sandbox-discard-") as tmp:
            strat = build_fold_strategy_file(Path(tmp) / "strategy.py")
            print(f"==> Discard-active: replace with fold placeholder ({args.competition_id})")
            rec = post_strategy_py(
                competition_id=args.competition_id,
                strategy_path=strat,
                replace=True,
            )
            print(json.dumps(rec, indent=2))
            sub_id = rec.get("id")
            if sub_id:
                print(f"\nPoll: uv run python examples/submit_sandbox_pvp.py --poll {sub_id}")
        return 0

    bundle = args.bundle
    if args.build or args.build_only or not bundle.is_file():
        print(f"==> Building {bundle}")
        build_bundle(bundle)
    if args.build_only:
        return 0

    print(f"==> Submitting to competition {args.competition_id}")
    try:
        rec = post_submission(
            competition_id=args.competition_id,
            bundle_path=bundle,
            replace=args.replace,
        )
    except SubmissionRejected as exc:
        if args.tolerate_daily_limit and exc.code == "sandbox_daily_limit":
            skip = {
                "status": "skipped",
                "reason": "sandbox_daily_limit",
                "competitionId": args.competition_id,
                "bundle": str(bundle),
            }
            print(json.dumps(skip, indent=2))
            _write_state(skip)
            return 0
        _write_state(
            {
                "status": "error",
                "reason": exc.code or "submission_rejected",
                "httpStatus": exc.status_code,
                "body": exc.body[:500],
            }
        )
        raise SystemExit(str(exc)) from exc

    out = {"status": "submitted", "submission": rec, "bundle": str(bundle)}
    print(json.dumps(rec, indent=2))
    _write_state(out)
    sub_id = rec.get("id")
    if sub_id:
        print(f"\nPoll: uv run python examples/submit_sandbox_pvp.py --poll {sub_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
