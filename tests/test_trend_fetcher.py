import importlib

import pytest


def _validate_trend_output(output: dict) -> None:
    assert isinstance(output, dict)
    assert "trends" in output
    assert isinstance(output["trends"], list)
    if output["trends"]:
        item = output["trends"][0]
        assert "topic" in item
        assert "score" in item
        assert "evidence" in item


def test_trend_data_structure_matches_contract():
    """
    This test is expected to fail until the trend discovery skill is implemented.
    It enforces the output contract defined in specs/technical.md.
    """
    try:
        module = importlib.import_module("skills.skill_trend_discovery.skill")
    except Exception as exc:  # noqa: BLE001
        pytest.fail(f"skill_trend_discovery module not implemented: {exc}")

    if not hasattr(module, "fetch_trends"):
        pytest.fail("fetch_trends() not implemented in skill_trend_discovery")

    output = module.fetch_trends(
        {
            "tenant_id": "uuid-v4",
            "sources": ["news://example"],
            "query": "fashion",
            "time_window": "2026-02-05T00:00:00Z",
        }
    )
    _validate_trend_output(output)
