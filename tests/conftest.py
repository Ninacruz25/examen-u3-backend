import os

os.environ.setdefault("API_KEY", "test-api-key")
os.environ.setdefault("PORT", "8000")

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from app.main import app  # noqa: E402
from app.routes.items import store  # noqa: E402


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture
def api_key() -> str:
    return os.environ["API_KEY"]


@pytest.fixture(autouse=True)
def reset_store():
    store.reset()
    yield
