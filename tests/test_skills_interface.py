import importlib
import inspect

import pytest


@pytest.mark.parametrize(
    "module_path, expected_params",
    [
        ("skills.skill_trend_discovery.skill", ["payload"]),
        ("skills.skill_social_publish.skill", ["payload"]),
        ("skills.skill_transaction.skill", ["payload"]),
    ],
)
def test_skill_interfaces_accept_expected_params(module_path: str, expected_params: list[str]):
    """
    This test is expected to fail until skill modules exist.
    It enforces a uniform interface contract for runtime skills.
    """
    try:
        module = importlib.import_module(module_path)
    except Exception as exc:  # noqa: BLE001
        pytest.fail(f"Skill module not implemented: {module_path}: {exc}")

    if not hasattr(module, "run"):
        pytest.fail(f"{module_path} missing run(payload) entrypoint")

    sig = inspect.signature(module.run)
    assert list(sig.parameters.keys()) == expected_params
