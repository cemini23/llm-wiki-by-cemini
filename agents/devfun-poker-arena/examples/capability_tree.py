"""K164 capability-tree helpers — exclusive domains + lazy child visibility.

Hierarchical skill stack (2607.11138): top domains must not overlap; per-call
visible children capped; nested work is push/pop. Advisory by default.

K176: submit leaf also requires claimed-authorization standing from
``operator`` or ``prebind`` channel — observation/tool prose never sets
``prebind_ok`` or authorizes submit/bankroll binds.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from claimed_authorization import authorize, prebind_ok_from_channel

_REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_PATH = _REPO_ROOT / "config" / "hu_capability_tree.json"
_BINDING_DOMAINS = frozenset({"submit"})


def load_capability_tree_config(path: str | Path | None = None) -> dict[str, Any]:
    cfg_path = Path(path) if path else DEFAULT_CONFIG_PATH
    if not cfg_path.is_file():
        raise FileNotFoundError(f"capability tree config not found: {cfg_path}")
    data = json.loads(cfg_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("capability tree config must be a JSON object")
    return data


def _resolve_config(
    config: dict[str, Any] | Path | str | None,
) -> dict[str, Any]:
    if isinstance(config, (str, Path)):
        return load_capability_tree_config(config)
    if isinstance(config, dict):
        return config
    return load_capability_tree_config()


def domain_ids(config: dict[str, Any] | None = None) -> list[str]:
    cfg = config if config is not None else load_capability_tree_config()
    domains = cfg.get("top_domains") or []
    return [str(d["id"]) for d in domains if isinstance(d, dict) and d.get("id")]


def validate_exclusive_domains(config: dict[str, Any] | None = None) -> dict[str, Any]:
    """Pass when top-level domain ids are unique and non-empty."""
    cfg = config if config is not None else load_capability_tree_config()
    ids = domain_ids(cfg)
    errors: list[str] = []
    if not ids:
        errors.append("no top_domains defined")
    if len(ids) != len(set(ids)):
        errors.append(f"duplicate top-domain ids: {ids}")
    if cfg.get("require_mutually_exclusive_roots") and len(ids) != len(set(ids)):
        errors.append("require_mutually_exclusive_roots violated")
    # Child ids must not collide across domains (overlap → wrong-branch risk)
    seen_children: dict[str, str] = {}
    for dom in cfg.get("top_domains") or []:
        if not isinstance(dom, dict):
            continue
        parent = str(dom.get("id", ""))
        for child in dom.get("children") or []:
            c = str(child)
            if c in seen_children:
                errors.append(
                    f"child '{c}' shared by '{seen_children[c]}' and '{parent}'"
                )
            else:
                seen_children[c] = parent
    return {
        "schema": "devfun.hu_capability_tree.gate.v1",
        "pass": not errors,
        "domain_ids": ids,
        "errors": errors,
        "advisory_only": bool(cfg.get("advisory_only", True)),
    }


def visible_children(
    domain_id: str,
    *,
    config: dict[str, Any] | Path | str | None = None,
) -> list[str]:
    """Return children of one domain, capped by max_visible_children_per_call."""
    cfg = _resolve_config(config)
    cap = int(cfg.get("max_visible_children_per_call") or 6)
    for dom in cfg.get("top_domains") or []:
        if isinstance(dom, dict) and str(dom.get("id")) == domain_id:
            kids = [str(c) for c in (dom.get("children") or [])]
            return kids[:cap]
    raise KeyError(f"unknown domain: {domain_id}")


def capability_tree_markdown(config: dict[str, Any] | None = None) -> str:
    cfg = config if config is not None else load_capability_tree_config()
    lines = ["| Domain | Type | Children |", "|--------|------|----------|"]
    for dom in cfg.get("top_domains") or []:
        if not isinstance(dom, dict):
            continue
        kids = ", ".join(str(c) for c in (dom.get("children") or []))
        lines.append(
            f"| `{dom.get('id')}` | {dom.get('type', '')} | {kids} |"
        )
    return "\n".join(lines)


@dataclass(frozen=True)
class CapabilityFrame:
    """One nested analysis frame — domain + optional focus child."""

    domain_id: str
    focus: str | None = None
    label: str = ""
    meta: dict[str, Any] = field(default_factory=dict)


@dataclass
class CapabilityFrameStack:
    """LIFO nested-work stack (K164). Push for sub-analysis; pop returns parent.

    Binding leaves (`submit`) require ``prebind_ok=True`` and a trusted
    auth channel (``operator`` | ``prebind``) — hierarchy does not bypass
    Prebind / verifier steals (K164 + K176 claimed-authorization).
    Observation text never sets ``prebind_ok``.
    """

    config: dict[str, Any] = field(default_factory=dict)
    _stack: list[CapabilityFrame] = field(default_factory=list)
    max_depth: int = 8

    def __post_init__(self) -> None:
        if not self.config:
            self.config = load_capability_tree_config()
        raw_depth = self.config.get("max_frame_depth")
        if raw_depth is not None:
            self.max_depth = max(1, int(raw_depth))

    @property
    def depth(self) -> int:
        return len(self._stack)

    def peek(self) -> CapabilityFrame | None:
        return self._stack[-1] if self._stack else None

    def push(
        self,
        domain_id: str,
        *,
        focus: str | None = None,
        label: str = "",
        meta: dict[str, Any] | None = None,
        prebind_ok: bool = False,
        channel: str | None = None,
    ) -> CapabilityFrame:
        ids = set(domain_ids(self.config))
        if domain_id not in ids:
            raise KeyError(f"unknown domain: {domain_id}")
        if domain_id in _BINDING_DOMAINS:
            # Default channel when prebind_ok already set by operator path.
            auth_channel = channel if channel is not None else (
                "prebind" if prebind_ok else "unknown"
            )
            # Observation/tool/unknown never invent prebind standing.
            effective_prebind = bool(prebind_ok) and prebind_ok_from_channel(
                channel=auth_channel,
                operator_prebind=True,
            )
            auth = authorize(
                "submit_sandbox",
                channel=auth_channel,
                evidence={
                    "prebind_ok": prebind_ok,
                    "effective_prebind": effective_prebind,
                    **(meta or {}),
                },
            )
            if not auth["ok"]:
                raise PermissionError(
                    f"submit claimed-auth deny: {auth['reason']} "
                    f"(channel={auth['channel']})"
                )
            if not effective_prebind:
                raise PermissionError(
                    "submit domain requires prebind_ok=True from "
                    "operator/prebind channel (K164+K176 leaf governance)"
                )
            meta = {
                **dict(meta or {}),
                "auth_channel": auth["channel"],
                "claimed_auth": auth,
            }
        if focus is not None:
            kids = visible_children(domain_id, config=self.config)
            if focus not in kids:
                raise KeyError(
                    f"focus '{focus}' not in visible children of '{domain_id}': {kids}"
                )
        if self.depth >= self.max_depth:
            raise RuntimeError(
                f"capability frame depth exceeds max_depth={self.max_depth}"
            )
        frame = CapabilityFrame(
            domain_id=domain_id,
            focus=focus,
            label=label or domain_id,
            meta=dict(meta or {}),
        )
        self._stack.append(frame)
        return frame

    def pop(self) -> CapabilityFrame:
        if not self._stack:
            raise IndexError("pop from empty CapabilityFrameStack")
        return self._stack.pop()

    def visible_slice(self) -> dict[str, Any]:
        """Lazy view for prompts — active frame children only, not the mega-registry."""
        top = self.peek()
        if top is None:
            return {
                "schema": "devfun.capability_frame_slice.v1",
                "depth": 0,
                "active_domain": None,
                "visible_children": [],
                "stack_labels": [],
            }
        kids = visible_children(top.domain_id, config=self.config)
        if top.focus:
            kids = [c for c in kids if c == top.focus] or kids
        return {
            "schema": "devfun.capability_frame_slice.v1",
            "depth": self.depth,
            "active_domain": top.domain_id,
            "focus": top.focus,
            "label": top.label,
            "visible_children": kids,
            "stack_labels": [f.label for f in self._stack],
            "advisory_only": bool(self.config.get("advisory_only", True)),
        }

    def to_list(self) -> list[dict[str, Any]]:
        return [
            {
                "domain_id": f.domain_id,
                "focus": f.focus,
                "label": f.label,
                "meta": f.meta,
            }
            for f in self._stack
        ]


def simulate_hu_researcher_nested_session(
    *,
    config: dict[str, Any] | Path | str | None = None,
    prebind_ok: bool = True,
) -> dict[str, Any]:
    """One HU Researcher Round nested-frame smoke (MAFP → exploit → return → submit).

    Exercises push/pop return without unbounded chat. Returns a transcript of
    visible slices at each step for operator verification.
    """
    cfg = _resolve_config(config)
    stack = CapabilityFrameStack(config=cfg)
    transcript: list[dict[str, Any]] = []

    def _snap(event: str) -> None:
        transcript.append({"event": event, "slice": stack.visible_slice()})

    stack.push("eval", focus="researcher_round", label="hu_session_root")
    _snap("enter_hu_root")

    stack.push("policy", focus="postflop_heuristic", label="mafp_lane")
    _snap("push_mafp")

    stack.push("memory", focus="yardstick", label="exploit_vs_yardstick")
    _snap("push_exploit_nested")

    returned = stack.pop()
    _snap(f"pop_return:{returned.label}")
    assert stack.peek() is not None and stack.peek().label == "mafp_lane"

    stack.pop()  # leave mafp
    _snap("pop_mafp")

    stack.push(
        "submit",
        focus="sandbox_submit",
        label="prebind_submit",
        prebind_ok=prebind_ok,
    )
    _snap("push_submit")
    stack.pop()
    _snap("pop_submit")

    while stack.depth:
        stack.pop()
    _snap("cleared")

    return {
        "schema": "devfun.hu_capability_nested_session.v1",
        "ok": True,
        "steps": len(transcript),
        "final_depth": stack.depth,
        "transcript": transcript,
        "reference": "references/capability-tree-routing.md",
    }
