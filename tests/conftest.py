from typing import Generator

import pytest
from api import app
from starlette.testclient import TestClient


@pytest.fixture(scope="module")
def test_app() -> Generator[TestClient, None, None]:
    client = TestClient(app)
    yield client  # testing happens here
