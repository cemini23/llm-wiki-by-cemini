"""K126 Kuhn poker SFT format reference helpers.

Offline REFERENCE-only utilities for inspecting Hugging Face style
conversation rows and comparing their structure to the Arena
``decide()`` output contract. This module does not download data,
train models, or modify runtime decision logic.
"""
from __future__ import annotations

import json
import os
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

_EXAMPLES = Path(__file__).resolve().parent
_AGENT_ROOT = _EXAMPLES.parent
_FIXTURE_PATH = _AGENT_ROOT / "tests" / "fixtures" / "kuhn_sft_samples.json"

_CARD_RE = re.compile(r"Your card is:\s*([JQKA])", re.IGNORECASE)
_ROUND_RE = re.compile(r"(?:round|hand)\s*(?:id)?\s*[:#]\s*([A-Za-z0-9._-]+)", re.IGNORECASE)
_AVAILABLE_ACTIONS_RE = re.compile(r"\[([a-zA-Z-]+)\]")
_BOXED_ACTION_RE = re.compile(r"\\boxed\{\s*(\[[^\]]+\])\s*\}")
_THINK_RE = re.compile(r"<think>(.*?)</think>", re.DOTALL | re.IGNORECASE)


@dataclass(frozen=True, slots=True)
class KuhnSftDataset:
    id: str
    license: str


@dataclass(frozen=True, slots=True)
class KuhnUserPrompt:
    round_id: str | None
    player_card: str | None
    available_actions: tuple[str, ...]
    raw_content: str


@dataclass(frozen=True, slots=True)
class KuhnAssistantReply:
    boxed_action: str | None
    thinking_chars: int
    has_boxed_answer: bool
    raw_content: str


@dataclass(frozen=True, slots=True)
class KuhnTraceParsed:
    round_id: str | None
    player_card: str | None
    available_actions: tuple[str, ...]
    boxed_action: str | None
    thinking_chars: int
    has_boxed_answer: bool
    user_content: str
    assistant_content: str


KUHN_SFT_DATASETS = [
    KuhnSftDataset(
        id="the-acorn-ai/kuhn-poker-Qwen-QwQ-32B-5000-sft",
        license="NO LICENSE",
    ),
    KuhnSftDataset(
        id="spiral-rl/Spiral-Kuhn-Poker-Qwen3-32B-SFT",
        license="NO LICENSE",
    ),
]


def _truthy(raw: str | None) -> bool:
    return str(raw or "").strip().lower() in {"1", "true", "yes", "on"}


def _last_message_content(messages: list[dict[str, Any]], role: str) -> str:
    for message in reversed(messages):
        if str(message.get("role") or "").strip().lower() == role:
            return str(message.get("content") or "")
    raise ValueError(f"missing {role!r} message")


def _extract_user_prompt(content: str) -> KuhnUserPrompt:
    round_match = _ROUND_RE.search(content)
    card_match = _CARD_RE.search(content)
    actions = tuple(
        dict.fromkeys(match.lower() for match in _AVAILABLE_ACTIONS_RE.findall(content))
    )
    return KuhnUserPrompt(
        round_id=round_match.group(1) if round_match else None,
        player_card=card_match.group(1).upper() if card_match else None,
        available_actions=actions,
        raw_content=content,
    )


def _extract_assistant_reply(content: str) -> KuhnAssistantReply:
    boxed_match = _BOXED_ACTION_RE.search(content)
    think_match = _THINK_RE.search(content)
    thinking = think_match.group(1).strip() if think_match else ""
    boxed_action = None
    if boxed_match:
        boxed_action = boxed_match.group(1).strip("[] \t\r\n").lower()
    return KuhnAssistantReply(
        boxed_action=boxed_action,
        thinking_chars=len(thinking),
        has_boxed_answer=boxed_match is not None,
        raw_content=content,
    )


def _sample_messages(sample: dict[str, Any]) -> list[dict[str, Any]]:
    direct = sample.get("messages")
    if isinstance(direct, list):
        return direct
    row = sample.get("row")
    if isinstance(row, dict) and isinstance(row.get("messages"), list):
        return row["messages"]
    raise ValueError("sample does not contain messages")


def parse_kuhn_messages(messages: list[dict[str, Any]]) -> KuhnTraceParsed:
    """Parse a two-turn Kuhn SFT row into a structured trace summary."""
    user_content = _last_message_content(messages, "user")
    assistant_content = _last_message_content(messages, "assistant")
    user = _extract_user_prompt(user_content)
    assistant = _extract_assistant_reply(assistant_content)
    return KuhnTraceParsed(
        round_id=user.round_id,
        player_card=user.player_card,
        available_actions=user.available_actions,
        boxed_action=assistant.boxed_action,
        thinking_chars=assistant.thinking_chars,
        has_boxed_answer=assistant.has_boxed_answer,
        user_content=user.raw_content,
        assistant_content=assistant.raw_content,
    )


def arena_decide_schema() -> dict[str, Any]:
    """Return the Arena action payload contract used in this repo."""
    return {
        "type": "object",
        "required": ["action", "message", "reasoning"],
        "properties": {
            "action": {
                "type": "string",
                "enum": ["fold", "check", "call", "bet", "raise", "all-in"],
            },
            "amount": {
                "type": "integer",
                "required_for": ["bet", "raise", "all-in"],
                "omit_for": ["fold", "check", "call"],
                "semantics": "total chips committed on this street after acting",
            },
            "message": {
                "type": "string",
                "max_chars": 500,
            },
            "reasoning": {
                "type": "yaml-flow-string",
                "max_chars": 150,
            },
        },
    }


def format_comparison_matrix() -> list[dict[str, str]]:
    """Describe which Kuhn SFT traits are portable to Arena."""
    return [
        {
            "dimension": "legal_action_enumeration",
            "kuhn": "Prompt enumerates legal actions like [check], [bet].",
            "arena": "allowedActions.availableActions exposes legal actions explicitly.",
            "steal": "yes",
        },
        {
            "dimension": "minimal_decision_structure",
            "kuhn": "Single-turn prompt -> deliberate -> final action.",
            "arena": "decide() should stay short, deterministic, and structured.",
            "steal": "yes",
        },
        {
            "dimension": "reasoning_length_discipline",
            "kuhn": "Long <think> chains often exceed 150 chars.",
            "arena": "reasoning is YAML flow style capped at 150 chars.",
            "steal": "yes",
        },
        {
            "dimension": "final_action_format",
            "kuhn": "Final answer uses \\boxed{[action]}.",
            "arena": "Return JSON fields, not boxed LaTeX.",
            "steal": "no",
        },
        {
            "dimension": "bet_sizing_semantics",
            "kuhn": "Bet is implicit 1-chip sizing in a toy game.",
            "arena": "bet/raise require explicit total-chip amount semantics.",
            "steal": "no",
        },
        {
            "dimension": "message_channel",
            "kuhn": "Assistant freeform answer contains both thinking and action.",
            "arena": "message and reasoning are separate output channels.",
            "steal": "partial",
        },
        {
            "dimension": "curriculum_scope",
            "kuhn": "Three-card toy game with tiny state space.",
            "arena": "No-limit hold'em has hidden information and rich sizing trees.",
            "steal": "no",
        },
        {
            "dimension": "prompt_step_structure",
            "kuhn": "Prompt encourages ordered analysis before commitment.",
            "arena": "Short YAML reasoning can preserve step discipline without essay CoT.",
            "steal": "yes",
        },
        {
            "dimension": "license_portability",
            "kuhn": "Datasets are marked NO LICENSE.",
            "arena": "Reference-only analysis is allowed; training reuse is blocked.",
            "steal": "no",
        },
    ]


def analyze_trace(messages: list[dict[str, Any]]) -> dict[str, Any]:
    """Summarize one Kuhn SFT trace for reporting."""
    parsed = parse_kuhn_messages(messages)
    arena_reasoning_limit = int(
        arena_decide_schema()["properties"]["reasoning"]["max_chars"]
    )
    return {
        "round_id": parsed.round_id,
        "player_card": parsed.player_card,
        "boxed_action": parsed.boxed_action,
        "thinking_chars": parsed.thinking_chars,
        "available_actions": list(parsed.available_actions),
        "has_boxed_answer": parsed.has_boxed_answer,
        "thinking_exceeds_arena_reasoning": parsed.thinking_chars > arena_reasoning_limit,
    }


def build_reference_report(samples: list[dict[str, Any]]) -> dict[str, Any]:
    """Build a JSON-serializable reference-only summary."""
    assert_reference_only()
    matrix = format_comparison_matrix()
    dataset_by_id = {dataset.id: dataset for dataset in KUHN_SFT_DATASETS}
    sample_reports: list[dict[str, Any]] = []
    for sample in samples:
        dataset_id = str(sample.get("dataset") or sample.get("dataset_id") or "")
        dataset = dataset_by_id.get(dataset_id)
        sample_reports.append(
            {
                "dataset_id": dataset_id,
                "license": dataset.license if dataset else str(sample.get("license") or ""),
                "row_idx": sample.get("row_idx"),
                **analyze_trace(_sample_messages(sample)),
            }
        )
    return {
        "reference_only": True,
        "dataset_count": len(KUHN_SFT_DATASETS),
        "sample_count": len(sample_reports),
        "datasets": [asdict(dataset) for dataset in KUHN_SFT_DATASETS],
        "comparison_matrix": matrix,
        "steal_candidates": [
            row["dimension"] for row in matrix if row["steal"] in {"yes", "partial"}
        ],
        "blocked_items": [row["dimension"] for row in matrix if row["steal"] == "no"],
        "arena_schema": arena_decide_schema(),
        "samples": sample_reports,
    }


def assert_reference_only() -> None:
    """Block accidental training-mode use of this module."""
    if _truthy(os.environ.get("TRAINING_MODE")):
        raise RuntimeError(
            "Kuhn SFT helpers are reference-only; disable TRAINING_MODE before use."
        )


def load_fixture_samples() -> list[dict[str, Any]]:
    """Load embedded Hugging Face style sample rows for offline tests."""
    data = json.loads(_FIXTURE_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("kuhn_sft_samples fixture must contain a list")
    return data
