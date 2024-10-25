import pytest
from starlette.testclient import TestClient

from main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_base_route(client):
    """
    GIVEN a FastAPI application
    WHEN health check endpoint is called with GET method
    THEN response with status 200 and body OK is returned
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "Provide": "Howiti API REST",
        "Version": "0.1.1",
        "URL": "https://howiti.com",
    }
