"""XSP lane_id contract for K37 reviewer-agent (pre-prod requirement).

Side-effecting provisional tool calls MUST carry ``lane_id`` so the
reviewer applies the correct lane rule set and does not second-guess
strategy across orthogonal XSP tracks.

Spec: wiki/concepts/reviewer-passive-injection-corpus.md § Pre-prod gates
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, FrozenSet, Mapping, Sequence

import yaml

from conductor.reviewer.policy_loader import PolicyParseError

# Tools that mutate Robinhood / EMS state for XSP killer v1 surface.
SIDE_EFFECTING_TOOLS = frozenset({
    "place_order",
    "close_position",
    "cancel_order",
    "withdraw",
    "notify_operator",
})

LANE_ID_REQUIRED_TOOLS = frozenset({
    "place_order",
    "close_position",
    "cancel_order",
})


class ReviewerVerdictMode(str, Enum):
    APPROVE_OR_REFUSE = "approve_or_refuse"
    REFUSE_ONLY = "refuse_only"  # no revise() on order args — v1 default for trading


class LaneAutomationPosture(str, Enum):
    EXIT_ONLY = "exit_only"
    ALERTS_ONLY = "alerts_only"
    NOT_AUTOMATED = "not_automated"
    MANUAL_ONLY = "manual_only"


@dataclass(frozen=True)
class LaneDefinition:
    lane_id: str
    label: str
    automation_v1: LaneAutomationPosture


@dataclass(frozen=True)
class LaneContract:
    version: int
    required_on_tools: FrozenSet[str]
    allowed_lane_ids: Dict[str, LaneDefinition]
    reviewer_verdict_mode: Dict[str, ReviewerVerdictMode]
    reviewer_mandate: tuple[str, ...]

    def allowed_ids(self) -> FrozenSet[str]:
        return frozenset(self.allowed_lane_ids.keys())

    def verdict_mode_for(self, tool_name: str) -> ReviewerVerdictMode:
        return self.reviewer_verdict_mode.get(
            tool_name,
            ReviewerVerdictMode.APPROVE_OR_REFUSE,
        )

    def lane_definition(self, lane_id: str) -> LaneDefinition | None:
        return self.allowed_lane_ids.get(lane_id)


class LaneContractError(ValueError):
    """Raised when a provisional call violates the lane_id contract."""


def default_lane_contract() -> LaneContract:
    """Canonical XSP lane_id contract (mirrors policy.yaml)."""
    lanes = (
        LaneDefinition(
            "lane_a",
            "Lane A — 14–60 DTE overnight swing; v1 **exit monitor only**",
            LaneAutomationPosture.EXIT_ONLY,
        ),
        LaneDefinition(
            "lane_b",
            "Lane B — LEAPS core book; v1 **alerts + manual entry**",
            LaneAutomationPosture.ALERTS_ONLY,
        ),
        LaneDefinition(
            "lane_c",
            "Lane C — mid-dated ~10:30 ET rule; **not v1 automated**",
            LaneAutomationPosture.NOT_AUTOMATED,
        ),
        LaneDefinition(
            "lane_d",
            "Lane D — weeklies; **not v1 automated**",
            LaneAutomationPosture.NOT_AUTOMATED,
        ),
        LaneDefinition(
            "manual",
            "Operator confirm-card / discretionary; human-initiated",
            LaneAutomationPosture.MANUAL_ONLY,
        ),
        LaneDefinition(
            "smb_put_credit",
            "SMB short put-credit on XSP — **orthogonal** to long-call lanes",
            LaneAutomationPosture.NOT_AUTOMATED,
        ),
        LaneDefinition(
            "hl_shadow",
            "Hyperliquid SP500 perp — timing shadow only; **no XSP options**",
            LaneAutomationPosture.NOT_AUTOMATED,
        ),
    )
    return LaneContract(
        version=1,
        required_on_tools=LANE_ID_REQUIRED_TOOLS,
        allowed_lane_ids={lane.lane_id: lane for lane in lanes},
        reviewer_verdict_mode={
            "place_order": ReviewerVerdictMode.REFUSE_ONLY,
            "close_position": ReviewerVerdictMode.REFUSE_ONLY,
            "cancel_order": ReviewerVerdictMode.REFUSE_ONLY,
        },
        reviewer_mandate=(
            "Do not second-guess strategy, edge, or timing.",
            "lane_id selects which hard-limit rule set applies; never cross-apply lanes.",
            "Refuse (do not revise order arguments) on place_order, close_position, cancel_order.",
            "Do NOT refuse place_order solely because regime is not GREEN — Lane B dip accumulation "
            "and related variants are designed for YELLOW/RED drawdown windows.",
            "Regime informs sizing caps and operator alerts; lane-specific dip rubrics override "
            "portfolio GREEN-only framing.",
            "Refuse automated place_order for lane_c, lane_d, smb_put_credit, hl_shadow until dedicated tracks ship.",
            "Lane A v1: allow close_position per exit rules; refuse automated place_order (entry is manual).",
            "Lane B v1: refuse automated place_order; alerts and manual entry only.",
        ),
    )


def parse_lane_contract(raw: Any, source: str = "policy") -> LaneContract:
    if raw is None:
        return default_lane_contract()
    if not isinstance(raw, dict):
        raise PolicyParseError(
            f"{source}: lane_id_contract must be a mapping, got {type(raw).__name__}",
        )

    version = raw.get("version", 1)
    if not isinstance(version, int):
        raise PolicyParseError(f"{source}: lane_id_contract.version must be int")

    req_tools = raw.get("required_on_tools", sorted(LANE_ID_REQUIRED_TOOLS))
    if not isinstance(req_tools, list) or not all(isinstance(t, str) for t in req_tools):
        raise PolicyParseError(f"{source}: required_on_tools must be a list of strings")
    required_on_tools = frozenset(req_tools)

    lanes_raw = raw.get("allowed_lane_ids")
    if lanes_raw is None:
        return default_lane_contract()

    if not isinstance(lanes_raw, list):
        raise PolicyParseError(f"{source}: allowed_lane_ids must be a list")

    allowed: Dict[str, LaneDefinition] = {}
    for item in lanes_raw:
        if not isinstance(item, dict):
            raise PolicyParseError(f"{source}: each allowed_lane_ids entry must be a mapping")
        lane_id = item.get("id")
        label = item.get("label")
        automation = item.get("automation_v1")
        if not isinstance(lane_id, str) or not isinstance(label, str):
            raise PolicyParseError(f"{source}: lane entry requires string id and label")
        try:
            posture = LaneAutomationPosture(automation)
        except (TypeError, ValueError) as exc:
            valid = ", ".join(p.value for p in LaneAutomationPosture)
            raise PolicyParseError(
                f"{source}: lane '{lane_id}' automation_v1 invalid "
                f"(valid: {valid})",
            ) from exc
        if lane_id in allowed:
            raise PolicyParseError(f"{source}: duplicate lane id '{lane_id}'")
        allowed[lane_id] = LaneDefinition(lane_id, label, posture)

    verdict_raw = raw.get("reviewer_verdict_mode", {})
    if not isinstance(verdict_raw, dict):
        raise PolicyParseError(f"{source}: reviewer_verdict_mode must be a mapping")
    verdict_mode: Dict[str, ReviewerVerdictMode] = {}
    for tool, mode_str in verdict_raw.items():
        try:
            verdict_mode[tool] = ReviewerVerdictMode(mode_str)
        except ValueError as exc:
            valid = ", ".join(m.value for m in ReviewerVerdictMode)
            raise PolicyParseError(
                f"{source}: reviewer_verdict_mode['{tool}'] invalid (valid: {valid})",
            ) from exc

    mandate_raw = raw.get("reviewer_mandate", [])
    if isinstance(mandate_raw, str):
        mandate = tuple(line.strip() for line in mandate_raw.strip().splitlines() if line.strip())
    elif isinstance(mandate_raw, list) and all(isinstance(m, str) for m in mandate_raw):
        mandate = tuple(mandate_raw)
    else:
        raise PolicyParseError(f"{source}: reviewer_mandate must be string or list of strings")

    return LaneContract(
        version=version,
        required_on_tools=required_on_tools,
        allowed_lane_ids=allowed,
        reviewer_verdict_mode=verdict_mode,
        reviewer_mandate=mandate,
    )


def load_lane_contract_from_policy(path: str | Any) -> LaneContract:
    from pathlib import Path

    p = Path(path)
    raw = yaml.safe_load(p.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        return default_lane_contract()
    return parse_lane_contract(raw.get("lane_id_contract"), source=str(p))


def extract_lane_id(tool_args: Mapping[str, Any] | None) -> str | None:
    if not tool_args:
        return None
    for key in ("lane_id", "strategy_track", "lane"):
        val = tool_args.get(key)
        if val is not None:
            return str(val)
    return None


def validate_provisional_call(
    tool_name: str,
    tool_args: Mapping[str, Any] | None,
    contract: LaneContract | None = None,
) -> LaneDefinition:
    """Validate lane_id on side-effecting XSP order tools.

    Returns the resolved :class:`LaneDefinition` on success.

    Raises:
        LaneContractError: missing or unknown lane_id, or v1 automation violation.
    """
    contract = contract or default_lane_contract()

    if tool_name not in contract.required_on_tools:
        return contract.lane_definition("manual") or next(iter(contract.allowed_lane_ids.values()))

    lane_id = extract_lane_id(tool_args)
    if lane_id is None:
        raise LaneContractError(
            f"tool {tool_name!r} requires lane_id in tool_args "
            f"(allowed: {sorted(contract.allowed_ids())})",
        )

    definition = contract.lane_definition(lane_id)
    if definition is None:
        raise LaneContractError(
            f"unknown lane_id {lane_id!r} on tool {tool_name!r} "
            f"(allowed: {sorted(contract.allowed_ids())})",
        )

    if tool_name == "place_order":
        if definition.lane_id == "manual":
            return definition
        if definition.lane_id == "lane_a":
            raise LaneContractError(
                "lane_a v1: automated place_order refused (exit monitor only; entry is manual)",
            )
        if definition.lane_id == "lane_b":
            raise LaneContractError(
                "lane_b v1: automated place_order refused (manual entry only)",
            )
        if definition.automation_v1 is LaneAutomationPosture.NOT_AUTOMATED:
            raise LaneContractError(
                f"lane {lane_id!r}: automated place_order refused (track not automated in v1)",
            )

    return definition


def reviewer_mandate_text(contract: LaneContract | None = None) -> str:
    contract = contract or default_lane_contract()
    lines = ["## Reviewer mandate (lane_id contract)", ""]
    lines.extend(f"- {rule}" for rule in contract.reviewer_mandate)
    lines.append("")
    lines.append("### Allowed lane_id values")
    for lane in contract.allowed_lane_ids.values():
        lines.append(
            f"- `{lane.lane_id}` — {lane.label} (`automation_v1={lane.automation_v1.value}`)",
        )
    return "\n".join(lines)
