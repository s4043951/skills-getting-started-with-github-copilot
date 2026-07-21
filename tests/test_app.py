from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant():
    response = client.post(
        "/activities/Chess Club/signup?email=test@example.com"
    )
    assert response.status_code == 200

    response = client.delete("/activities/Chess Club/unregister?email=test@example.com")
    assert response.status_code == 200

    activity = client.get("/activities").json()["Chess Club"]
    assert "test@example.com" not in activity["participants"]
