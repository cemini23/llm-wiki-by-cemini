"""Tests for gambling-wiki kb-server prefetch."""
from __future__ import annotations

import httpx
import pytest
import respx

from examples.gambling_wiki_kb import (
    _dynamic_query,
    fetch_context_detail,
    fetch_gambling_wiki_briefing,
)


@respx.mock
def test_fetch_context_detail_gambling_project(monkeypatch):
    monkeypatch.setenv("LIBRARIAN_API_KEY", "test-key")
    monkeypatch.setenv("LIBRARIAN_BASE_URL", "http://10.0.0.2:3838")
    route = respx.get("http://10.0.0.2:3838/api/v1/context").mock(
        return_value=httpx.Response(
            200,
            json={
                "briefing": "Tight-passive survival on Playground S1.",
                "sources": [{"title": "Poker HL analyst loop", "path": "gambling-wiki/wiki/concepts/poker-hl-analyst-loop.md"}],
            },
        )
    )
    out = fetch_context_detail("poker HL loop")
    assert route.called
    assert route.calls[0].request.url.params.get("project") == "gambling-wiki"
    assert "survival" in out["text"]
    assert out["wiki_hits"]


def test_fetch_briefing_disabled(monkeypatch):
    monkeypatch.setenv("CEMINI_HL_WIKI_KB", "0")
    out = fetch_gambling_wiki_briefing(report_text="SB leak")
    assert out["text"] == ""
    assert out.get("skipped") == "disabled"


def test_dynamic_query_from_qual():
    q = _dynamic_query("", "first_protect rank #1 qualification")
    assert "qualification" in q.lower()


@respx.mock
def test_fetch_briefing_merges_queries(monkeypatch):
    monkeypatch.setenv("LIBRARIAN_API_KEY", "test-key")
    monkeypatch.setenv("LIBRARIAN_BASE_URL", "http://10.0.0.2:3838")

    def _handler(request: httpx.Request) -> httpx.Response:
        q = request.url.params.get("q", "")
        return httpx.Response(
            200,
            json={"briefing": f"Brief for: {q[:20]}", "sources": [{"title": q[:30]}]},
        )

    respx.get("http://10.0.0.2:3838/api/v1/context").mock(side_effect=_handler)
    out = fetch_gambling_wiki_briefing(report_text="CO worst leak", qual_summary="")
    assert out["char_count"] > 0
    assert len(out["queries"]) == 3
