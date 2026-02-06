import pytest
import os
import sys

# Ensure src is in pythonpath
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

@pytest.fixture
def mock_env_setup():
    """Setup mock environment variables for testing"""
    os.environ["CHIMERA_ENV"] = "test"
    os.environ["REDIS_URL"] = "redis://localhost:6379/1"
    yield
    del os.environ["CHIMERA_ENV"]
