import os

import pytest
from fastapi.testclient import TestClient

from app import main
from app.config import get_settings, Settings


def get_settings_override():
    return Settings(testing=1, databse_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")
def test_app():
    # Set up
    main.app.dependency_overrides[get_settings] = get_settings_override

    with TestClient(main.app) as test_client:
        # testing
        yield test_client
