import pytest
from fastapi.testclient import TestClient

from src.app import app


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


def test_unregister_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email = "test@example.com"

    # Act
    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    unregister_response = client.delete(f"/activities/{activity_name}/unregister?email={email}")

    # Assert
    assert signup_response.status_code == 200
    assert unregister_response.status_code == 200

    activity = client.get("/activities").json()[activity_name]
    assert email not in activity["participants"]
