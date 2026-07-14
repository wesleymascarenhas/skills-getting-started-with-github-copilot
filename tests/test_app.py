import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture
def client():
    # Arrange
    app_module.activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"],
        }
    }

    with TestClient(app_module.app) as test_client:
        yield test_client


def test_remove_participant_unregisters_from_activity(client):
    # Arrange
    activity_name = "Chess Club"
    participant_email = "michael@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants/{participant_email}"
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {participant_email} from {activity_name}"
    assert participant_email not in app_module.activities[activity_name]["participants"]


def test_remove_participant_returns_404_when_not_found(client):
    # Arrange
    activity_name = "Chess Club"
    participant_email = "unknown@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants/{participant_email}"
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"
