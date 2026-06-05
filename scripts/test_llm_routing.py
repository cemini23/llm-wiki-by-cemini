"""Tests for scripts/llm_routing.py (DeepSeek → OpenRouter failover)."""

from __future__ import annotations

import httpx
import pytest

import llm_routing as lr


@pytest.fixture(autouse=True)
def _clean_llm_env(monkeypatch):
    for name in (
        "DEEPSEEK_API_KEY",
        "OPENROUTER_API_KEY",
        "LLM_FALLBACK_ENABLED",
        "LLM_FALLBACK_MODEL",
        "DEEPSEEK_MODEL",
    ):
        monkeypatch.delenv(name, raising=False)


def test_ordered_routes_primary_then_fallback(monkeypatch):
    monkeypatch.setenv("DEEPSEEK_API_KEY", "ds-key")
    monkeypatch.setenv("OPENROUTER_API_KEY", "or-key")
    monkeypatch.setenv("DEEPSEEK_MODEL", "deepseek-v4-flash")
    routes = lr.ordered_routes()
    assert len(routes) == 2
    assert routes[0].provider == "deepseek"
    assert routes[1].provider == "openrouter"
    assert routes[1].model == "deepseek/deepseek-chat"


def test_openrouter_only_when_deepseek_missing(monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "or-key")
    routes = lr.ordered_routes()
    assert len(routes) == 1
    assert routes[0].provider == "openrouter"


def test_should_failover_on_402():
    req = httpx.Request("POST", "https://api.deepseek.com/v1/chat/completions")
    resp = httpx.Response(402, request=req, text="insufficient balance")
    exc = httpx.HTTPStatusError("payment", request=req, response=resp)
    assert lr.should_failover(exc) is True


def test_should_failover_on_quota_message():
    assert lr.should_failover(RuntimeError("Error: insufficient_quota")) is True


def test_fallback_disabled(monkeypatch):
    monkeypatch.setenv("DEEPSEEK_API_KEY", "ds-key")
    monkeypatch.setenv("OPENROUTER_API_KEY", "or-key")
    monkeypatch.setenv("LLM_FALLBACK_ENABLED", "false")
    assert lr.get_fallback_route() is None
    assert len(lr.ordered_routes()) == 1
