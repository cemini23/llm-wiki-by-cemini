"""Tests for lobby pace throttling."""
from __future__ import annotations

import os

import pytest

from pace_control import (
    DEFAULT_FIRST_JOIN_RETRY_S,
    DEFAULT_JOIN_RETRY_S,
    DEFAULT_LEAD_JOIN_RETRY_S,
    DEFAULT_LOW_STACK_JOIN_RETRY_S,
    DEFAULT_QUAL_JOIN_RETRY_S,
    join_retry_seconds,
)


def test_normal_pace(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("CEMINI_JOIN_RETRY_S", raising=False)
    assert join_retry_seconds(
        lead_protect=False, qual_protect=False, in_queue_only=False
    ) == DEFAULT_JOIN_RETRY_S


def test_qual_pace(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("CEMINI_QUAL_JOIN_RETRY_S", raising=False)
    assert join_retry_seconds(
        lead_protect=False, qual_protect=True, in_queue_only=False
    ) == DEFAULT_QUAL_JOIN_RETRY_S


def test_lead_pace(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("CEMINI_LEAD_JOIN_RETRY_S", raising=False)
    assert join_retry_seconds(
        first_protect=False,
        lead_protect=True, qual_protect=True, in_queue_only=False
    ) == DEFAULT_LEAD_JOIN_RETRY_S


def test_first_pace(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("CEMINI_FIRST_JOIN_RETRY_S", raising=False)
    assert join_retry_seconds(
        first_protect=True,
        lead_protect=True, qual_protect=True, in_queue_only=False
    ) == DEFAULT_FIRST_JOIN_RETRY_S


def test_env_override(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CEMINI_FIRST_JOIN_RETRY_S", "3600")
    assert join_retry_seconds(
        first_protect=True, lead_protect=True, qual_protect=False, in_queue_only=False
    ) == 3600.0
    monkeypatch.setenv("CEMINI_LEAD_JOIN_RETRY_S", "1200")
    assert join_retry_seconds(
        first_protect=False, lead_protect=True, qual_protect=False, in_queue_only=False
    ) == 1200.0


def test_volume_phase_overrides_qual(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CEMINI_PACE_PHASE", "volume")
    monkeypatch.delenv("CEMINI_JOIN_RETRY_S", raising=False)
    assert join_retry_seconds(
        first_protect=False,
        lead_protect=False,
        qual_protect=True,
        in_queue_only=False,
    ) == 20.0


def test_volume_phase_in_queue(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CEMINI_PACE_PHASE", "volume")
    monkeypatch.delenv("CEMINI_IN_QUEUE_RETRY_S", raising=False)
    assert join_retry_seconds(
        first_protect=False,
        lead_protect=False,
        qual_protect=False,
        in_queue_only=True,
    ) == 45.0


def test_volume_phase_still_respects_first_protect(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CEMINI_PACE_PHASE", "volume")
    monkeypatch.delenv("CEMINI_FIRST_JOIN_RETRY_S", raising=False)
    assert join_retry_seconds(
        first_protect=True,
        lead_protect=True,
        qual_protect=True,
        in_queue_only=False,
    ) == DEFAULT_FIRST_JOIN_RETRY_S


def test_low_stack_join_pace(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("CEMINI_LOW_STACK_JOIN_RETRY_S", raising=False)
    assert join_retry_seconds(
        first_protect=False,
        lead_protect=False,
        qual_protect=False,
        in_queue_only=False,
        hero_stack_chips=850,
        buy_in_chips=1000,
    ) == DEFAULT_LOW_STACK_JOIN_RETRY_S
    assert join_retry_seconds(
        first_protect=True,
        lead_protect=True,
        qual_protect=True,
        in_queue_only=False,
        hero_stack_chips=850,
        buy_in_chips=1000,
    ) == max(DEFAULT_FIRST_JOIN_RETRY_S, DEFAULT_LOW_STACK_JOIN_RETRY_S)
